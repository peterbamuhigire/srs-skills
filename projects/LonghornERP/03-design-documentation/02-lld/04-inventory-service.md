# Inventory Module — Low-Level Design

## Overview

The Inventory module maintains a perpetual stock ledger with immutable movement records. All stock balance reads go through database views (`v_current_stock`, `v_low_stock_items`) rather than a mutable quantity column. The Advanced Inventory add-on (ADV_INVENTORY) extends this module with batch/serial tracking and landed cost allocation; its classes are instantiable only when `ModuleRegistry::isActive('ADV_INVENTORY', $tenantId)` returns `true`.

---

## ItemService

**Namespace:** `App\Modules\Inventory`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createItem(array $data): int` | Associative array of item attributes (`name`, `sku`, `unit_of_measure`, `reorder_level`, `category_id`, etc.) | New `items.id` | Validates SKU uniqueness per tenant. Inserts one row into `items`. Logs to `AuditService`. |
| `getStockBalance(int $itemId, ?int $warehouseId = null): float` | Item primary key, optional warehouse filter | Current quantity on hand as float | Reads from `v_current_stock` filtered by `item_id`, `tenant_id`, and optionally `warehouse_id`. |
| `getLowStockItems(?int $warehouseId = null): array` | Optional warehouse filter | Array of item rows where stock is at or below reorder level | Reads from `v_low_stock_items` filtered by `tenant_id` and optionally `warehouse_id`. |
| `updateItem(int $itemId, array $data): void` | Item primary key, fields to update | `void` | Updates non-financial fields on the `items` row. SKU changes are rejected if any stock movement exists. Logs to `AuditService`. |

**Views read:** `v_current_stock`, `v_low_stock_items`

**Tables read/written:** `items`

---

## StockLedgerService

**Namespace:** `App\Modules\Inventory`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

`StockLedgerService` is analogous to the GL for financial entries. Once posted, ledger rows are never updated or deleted.

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `postMovement(int $itemId, int $warehouseId, string $movementType, float $qty, float $unitCost, int $referenceId, string $referenceType): int` | Item primary key, warehouse primary key, movement type code (`GRN`, `SALE`, `ADJ_IN`, `ADJ_OUT`, `TRANSFER_OUT`, `TRANSFER_IN`, `PRODUCTION_IN`, `PRODUCTION_OUT`, `COUNT_ADJ`), signed quantity (negative for outflows), unit cost at time of movement, source document primary key, source document type label | New `stock_ledger.id` | Inserts one immutable row into `stock_ledger`. Never updates or deletes existing rows. Throws `InsufficientStockException` if the resulting on-hand balance would go negative for movement types that are outflows, unless the item is flagged `allow_negative_stock`. |

**Tables written:** `stock_ledger`

---

## GRNService

**Namespace:** `App\Modules\Inventory`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `StockLedgerService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createGRN(int $lpoId, array $lines): int` | LPO primary key, array of `['item_id', 'qty_received', 'unit_cost']` entries | New `grn_headers.id` | Validates that each item-quantity pair exists on the LPO. Inserts one row into `grn_headers` (status `draft`) and one row per item into `grn_lines`. |
| `postGRN(int $grnId): void` | GRN primary key | `void` | Opens a transaction. Calls `StockLedgerService::postMovement()` for each line (movement type `GRN`). Calls the stored procedure `CALL sp_post_purchase_to_gl(:grn_id, :tenant_id)` to create the corresponding payable and inventory GL entries. Sets `grn_headers.status = 'posted'`. Calls `AuditService::log()` inside the same transaction. Rolls back on any exception. |

**Tables read/written:** `grn_headers`, `grn_lines`

**Stored procedures called:** `sp_post_purchase_to_gl`

---

## StockAdjustmentService

**Namespace:** `App\Modules\Inventory`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `StockLedgerService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `postAdjustment(int $warehouseId, array $lines, string $reason): int` | Warehouse primary key, array of `['item_id', 'qty_counted', 'unit_cost']` entries, free-text reason | New `stock_adjustments.id` | Calculates the variance between `qty_counted` and the current ledger balance. Posts `ADJ_IN` or `ADJ_OUT` movements via `StockLedgerService::postMovement()`. Posts the corresponding inventory account journal via `AccountingService::postJournal()`. |

**Tables read/written:** `stock_adjustments`, `stock_adjustment_lines`

---

## StockTransferService

**Namespace:** `App\Modules\Inventory`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `StockLedgerService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `initiateTransfer(int $fromWarehouseId, int $toWarehouseId, array $lines): int` | Source warehouse primary key, destination warehouse primary key, array of `['item_id', 'qty']` entries | New `stock_transfers.id` | Validates available stock in the source warehouse. Inserts `stock_transfers` header (status `in_transit`) and posts `TRANSFER_OUT` movements from the source warehouse. |
| `receiveTransfer(int $transferId): void` | Transfer primary key | `void` | Posts `TRANSFER_IN` movements to the destination warehouse for each line. Sets `stock_transfers.status = 'received'` and records `received_at`. |

**Tables read/written:** `stock_transfers`, `stock_transfer_lines`

---

## PhysicalCountService

**Namespace:** `App\Modules\Inventory`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `StockLedgerService`, `StockAdjustmentService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `freezeStock(int $warehouseId): int` | Warehouse primary key | New `physical_counts.id` | Snapshots the current `v_current_stock` balances into `physical_count_snapshot` rows. Sets `physical_counts.status = 'frozen'`. No stock movements are permitted for the warehouse while a count is frozen. |
| `postCount(int $countId, array $lines): void` | Physical count primary key, array of `['item_id', 'qty_counted']` entries | `void` | Stores counted quantities in `physical_count_lines`. Status moves to `counted`. |
| `postVariance(int $countId): void` | Physical count primary key | `void` | Compares `physical_count_lines.qty_counted` against `physical_count_snapshot.qty_on_hand`. Delegates to `StockAdjustmentService::postAdjustment()` for all items with non-zero variance. Sets `physical_counts.status = 'posted'`. |

**Tables read/written:** `physical_counts`, `physical_count_lines`, `physical_count_snapshot`

---

## BatchSerialService (ADV_INVENTORY)

**Namespace:** `App\Modules\AdvInventory`

**Module guard:** `ModuleRegistry::isActive('ADV_INVENTORY', $tenantId)` must return `true`.

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `assignBatch(int $stockLedgerId, string $batchNumber, ?string $expiryDate = null): void` | Stock ledger row primary key, batch number string, optional ISO 8601 expiry date | `void` | Inserts a row into `item_batches` linked to the ledger row. Rejects duplicate batch numbers per `(item_id, tenant_id)`. |
| `assignSerial(int $stockLedgerId, string $serialNumber): void` | Stock ledger row primary key, serial number string | `void` | Inserts a row into `item_serials`. Rejects duplicate serial numbers per `(item_id, tenant_id)`. |
| `getExpiryAlerts(int $daysAhead = 30): array` | Look-ahead window in days | Array of batch rows expiring within the window | Queries `item_batches WHERE expiry_date <= DATE_ADD(NOW(), INTERVAL :days DAY) AND tenant_id = :tenant_id AND qty_remaining > 0`. |

**Tables read/written:** `item_batches`, `item_serials`

---

## LandedCostService (ADV_INVENTORY)

**Namespace:** `App\Modules\AdvInventory`

**Module guard:** `ModuleRegistry::isActive('ADV_INVENTORY', $tenantId)` must return `true`.

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `allocateLandedCost(int $grnId, float $totalCost, string $allocationMethod): void` | GRN primary key, total landed cost amount to distribute, allocation method code (`WEIGHT`, `VALUE`, `QUANTITY`) | `void` | Retrieves the GRN lines. Calculates each line's share of `$totalCost` using the chosen method: weight-based uses `items.unit_weight`, value-based uses `line_total`, quantity-based uses `qty_received`. Updates `grn_lines.landed_cost` per line. Posts the corresponding GL debit to the inventory account and credit to the landed cost payable via `AccountingService::postJournal()`. |

**Tables read/written:** `grn_lines`, `landed_cost_allocations`

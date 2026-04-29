# Inventory Module Tables

The Inventory Management (INVENTORY) module is a core module active for all tenants. The tables below support item catalogue management, unit of measure (UOM) conversions, stock movement journaling, goods receiving, inter-branch transfers, and batch tracking.

## `stock_items`

The master catalogue of all goods and materials managed in inventory. Each item carries its valuation method configuration; the application enforces First-In-First-Out (FIFO) or weighted-average costing accordingly.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `code` | VARCHAR(50) | NOT NULL | Unique item code within the tenant (e.g., `ITM-001`). |
| `name` | VARCHAR(255) | NOT NULL | Item description as displayed on invoices and reports. |
| `category_id` | BIGINT UNSIGNED | NOT NULL, FK → `item_categories.id` | Item category used for GL account mapping and grouping. |
| `uom_id` | BIGINT UNSIGNED | NOT NULL, FK → `uom.id` | Default stocking unit of measure. |
| `reorder_level` | DECIMAL(15,4) | NOT NULL, DEFAULT 0 | Quantity threshold that triggers a low-stock alert; 0 disables the alert. |
| `service_class` | ENUM('critical','standard','economy','manual') | NOT NULL, DEFAULT 'standard' | Default inventory service class used by lightweight reorder logic and Supply Chain Planning policy assignment. |
| `abc_class` | ENUM('A','B','C','UNCLASSIFIED') | NOT NULL, DEFAULT 'UNCLASSIFIED' | Value-based inventory class, recalculated by the planning job or maintained manually before enough history exists. |
| `xyz_class` | ENUM('X','Y','Z','UNCLASSIFIED') | NOT NULL, DEFAULT 'UNCLASSIFIED' | Demand-variability class, recalculated by the planning job or maintained manually before enough history exists. |
| `valuation_method` | ENUM('FIFO','WA') | NOT NULL, DEFAULT 'WA' | Costing method: FIFO or weighted average (WA). |
| `is_active` | TINYINT(1) | NOT NULL, DEFAULT 1 | 1 = item available for transactions; 0 = retired. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `code`), (`tenant_id`, `category_id`, `is_active`).

---

## `item_categories`

Hierarchical grouping of stock items. Categories drive GL account mapping via `account_mappings`.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(255) | NOT NULL | Category name. |
| `parent_id` | BIGINT UNSIGNED | NULL, FK → `item_categories.id` | Parent category for hierarchical grouping; NULL for root categories. |
| `gl_account_id` | BIGINT UNSIGNED | NULL, FK → `chart_of_accounts.id` | Default inventory GL account for items in this category. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `parent_id`).

---

## `uom`

Lookup table of units of measure (UOM). Not tenant-scoped; shared across the platform. Examples: `KG`, `PCS`, `LTR`, `BOX`.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `code` | VARCHAR(20) | NOT NULL, UNIQUE | Short code (e.g., `KG`). |
| `name` | VARCHAR(100) | NOT NULL | Full name (e.g., "Kilogram"). |

**Indexes:** PRIMARY (`id`), UNIQUE (`code`).

---

## `uom_conversions`

Defines conversion factors between UOM pairs for a specific item. Used when a purchase is received in cases but stocked in pieces, for example.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | The item to which this conversion applies. |
| `from_uom_id` | BIGINT UNSIGNED | NOT NULL, FK → `uom.id` | Source unit of measure. |
| `to_uom_id` | BIGINT UNSIGNED | NOT NULL, FK → `uom.id` | Target unit of measure. |
| `conversion_factor` | DECIMAL(18,8) | NOT NULL | Multiplier: quantity in `from_uom` × `conversion_factor` = quantity in `to_uom`. |

**Indexes:** PRIMARY (`id`), UNIQUE (`item_id`, `from_uom_id`, `to_uom_id`).

---

## `stock_balance`

Stores the current quantity on hand and average cost per item per branch. Updated by the stock posting logic whenever a movement is recorded. This table is the source of truth for the `v_current_stock` view.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | The stock item. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | The branch location. |
| `quantity` | DECIMAL(15,4) | NOT NULL, DEFAULT 0 | Current quantity on hand. |
| `reserved_quantity` | DECIMAL(15,4) | NOT NULL, DEFAULT 0 | Quantity allocated to sales orders, picking tasks, or committed transfers. |
| `inbound_quantity` | DECIMAL(15,4) | NOT NULL, DEFAULT 0 | Open confirmed inbound supply expected for this item and branch. |
| `avg_cost` | DECIMAL(18,4) | NOT NULL, DEFAULT 0 | Current weighted-average unit cost in the tenant's base currency. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `item_id`, `branch_id`).

**Derived values:** `available_quantity = quantity - reserved_quantity`. Application services and reports must derive available stock rather than store it.

---

## `stock_ledger`

The immutable movement journal for all stock transactions. Each row represents one quantity movement (inbound or outbound) with its unit cost and the originating business document. No UPDATE or DELETE operations are permitted on this table.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | The item being moved. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | The branch affected. |
| `movement_type` | ENUM('GRN','SALE','RETURN_IN','RETURN_OUT','TRANSFER_OUT','TRANSFER_IN','ADJUSTMENT','PRODUCTION_IN','PRODUCTION_OUT') | NOT NULL | Nature of the stock movement. |
| `quantity` | DECIMAL(15,4) | NOT NULL | Movement quantity; positive for inbound, negative for outbound. |
| `unit_cost` | DECIMAL(18,4) | NOT NULL | Unit cost at the time of the movement. |
| `reference_type` | VARCHAR(50) | NOT NULL | Document type that originated the movement (e.g., `GRN`, `INVOICE`). |
| `reference_id` | BIGINT UNSIGNED | NOT NULL | Primary key of the originating document. |
| `posting_date` | DATE | NOT NULL | Business date of the movement. |
| `created_by` | BIGINT UNSIGNED | NOT NULL, FK -> `users.id` | Actor who posted the movement. |
| `reason_code` | VARCHAR(50) | NULL | Required for adjustments, stocktake variances, reversals, and write-offs. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `item_id`, `posting_date`), (`tenant_id`, `branch_id`, `item_id`), (`tenant_id`, `reference_type`, `reference_id`).

---

## `goods_receipts`

Header record for a Goods Receipt Note (GRN), linking a supplier delivery to a Purchase Order (PO).

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `grn_number` | VARCHAR(30) | NOT NULL | System-generated GRN reference number. |
| `po_id` | BIGINT UNSIGNED | NULL, FK → `purchase_orders.id` | Linked purchase order; NULL for unplanned direct receipts. |
| `supplier_id` | BIGINT UNSIGNED | NOT NULL, FK → `suppliers.id` | Supplier from whom goods were received. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | Receiving branch. |
| `receipt_date` | DATE | NOT NULL | Date goods were physically received. |
| `status` | ENUM('draft','posted','cancelled') | NOT NULL, DEFAULT 'draft' | Lifecycle state; stock is updated only when status transitions to `posted`. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `grn_number`), (`tenant_id`, `supplier_id`, `status`), (`tenant_id`, `po_id`).

---

## `goods_receipt_items`

Line items for each goods receipt, specifying quantity received and actual unit cost.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `grn_id` | BIGINT UNSIGNED | NOT NULL, FK → `goods_receipts.id` | Parent GRN. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | Item received. |
| `quantity` | DECIMAL(15,4) | NOT NULL | Quantity received in the item's stocking UOM. |
| `unit_cost` | DECIMAL(18,4) | NOT NULL | Actual supplier unit cost for this receipt. |
| `batch_id` | BIGINT UNSIGNED | NULL, FK → `batches.id` | Batch reference if the Advanced Inventory module is active and batch tracking is enabled for this item. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `grn_id`), (`tenant_id`, `item_id`).

---

## `stock_transfers`

Header record for an inter-branch stock transfer.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `from_branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | Branch dispatching the stock. |
| `to_branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | Branch receiving the stock. |
| `status` | ENUM('draft','in_transit','received','cancelled') | NOT NULL, DEFAULT 'draft' | Transfer lifecycle state. |
| `transfer_date` | DATE | NOT NULL | Date the transfer was initiated. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `from_branch_id`, `status`), (`tenant_id`, `to_branch_id`, `status`).

---

## `stock_transfer_items`

Line items for a stock transfer, recording quantity and cost of each item being moved.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `transfer_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_transfers.id` | Parent transfer. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | Item being transferred. |
| `quantity` | DECIMAL(15,4) | NOT NULL | Quantity being transferred. |
| `unit_cost` | DECIMAL(18,4) | NOT NULL | Unit cost at the time of dispatch. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `transfer_id`), (`tenant_id`, `item_id`).

---

## `batches`

Tracks batch or lot numbers for items where the Advanced Inventory module is active. Stores manufacture and expiry dates for First-Expired-First-Out (FEFO) ordering.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | The item this batch belongs to. |
| `batch_number` | VARCHAR(100) | NOT NULL | Supplier or internal batch/lot number. |
| `manufacture_date` | DATE | NULL | Date of manufacture; NULL if not applicable. |
| `expiry_date` | DATE | NULL | Expiry or use-by date; NULL for non-perishable items. |
| `quantity` | DECIMAL(15,4) | NOT NULL, DEFAULT 0 | Current remaining quantity in this batch. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `item_id`, `batch_number`), (`tenant_id`, `item_id`, `expiry_date`).

---

## `warehouse_bins`

Defines physical storage locations inside a branch or warehouse.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK -> `branches.id` | Warehouse or branch. |
| `zone_code` | VARCHAR(40) | NOT NULL | Zone identifier. |
| `aisle_code` | VARCHAR(40) | NULL | Aisle identifier. |
| `bin_code` | VARCHAR(60) | NOT NULL | Unique bin within branch. |
| `storage_medium` | ENUM('floor','rack','pallet','shelf','cold_store','staging') | NOT NULL | Physical storage type. |
| `max_weight_kg` | DECIMAL(15,3) | NULL | Weight capacity. |
| `max_volume_m3` | DECIMAL(15,3) | NULL | Volume capacity. |
| `max_pallets` | DECIMAL(10,2) | NULL | Pallet capacity. |
| `is_forward_pick` | TINYINT(1) | NOT NULL, DEFAULT 0 | Forward-pick eligibility. |
| `is_active` | TINYINT(1) | NOT NULL, DEFAULT 1 | Active flag. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `branch_id`, `bin_code`), (`tenant_id`, `branch_id`, `zone_code`, `aisle_code`).

---

## `warehouse_storage_policies`

Stores putaway, replenishment, and handling rules per item and warehouse.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK -> `stock_items.id` | Item controlled by the policy. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK -> `branches.id` | Warehouse or branch. |
| `preferred_zone_code` | VARCHAR(40) | NULL | Preferred putaway zone. |
| `rotation_rule` | ENUM('FIFO','FEFO','MANUAL') | NOT NULL, DEFAULT 'FIFO' | Rotation rule. |
| `forward_pick_min_qty` | DECIMAL(15,4) | NULL | Replenishment trigger. |
| `forward_pick_max_qty` | DECIMAL(15,4) | NULL | Replenishment target. |
| `handling_constraint` | VARCHAR(100) | NULL | Cold chain, fragile, hazardous, or other constraint. |
| `stack_limit` | DECIMAL(10,2) | NULL | Maximum stack quantity where relevant. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `item_id`, `branch_id`), (`tenant_id`, `branch_id`, `preferred_zone_code`).

---

## `warehouse_tasks`

Execution tasks for putaway, picking, replenishment, staging, and count movements.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `task_type` | ENUM('putaway','pick','replenishment','stage','count') | NOT NULL | Task category. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK -> `stock_items.id` | Item. |
| `batch_id` | BIGINT UNSIGNED | NULL, FK -> `batches.id` | Batch when applicable. |
| `from_bin_id` | BIGINT UNSIGNED | NULL, FK -> `warehouse_bins.id` | Source bin. |
| `to_bin_id` | BIGINT UNSIGNED | NULL, FK -> `warehouse_bins.id` | Destination bin. |
| `quantity` | DECIMAL(15,4) | NOT NULL | Task quantity. |
| `priority` | ENUM('low','normal','high','urgent') | NOT NULL, DEFAULT 'normal' | Execution priority. |
| `status` | ENUM('open','assigned','in_progress','completed','cancelled') | NOT NULL, DEFAULT 'open' | Task status. |
| `pick_mode` | ENUM('single_order','batch','wave','zone') | NULL | Picking mode for pick tasks. |
| `sequence_no` | INT UNSIGNED | NULL | Generated pick-path sequence. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `task_type`, `status`, `priority`), (`tenant_id`, `from_bin_id`, `status`), (`tenant_id`, `to_bin_id`, `status`).

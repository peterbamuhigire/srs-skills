---
title: "Maduuka Platform — Low-Level Design, Section 4: Inventory Service"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# Inventory Service

**Document ID:** MADUUKA-LLD-004
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Overview

`StockService` manages all inventory state changes. It enforces the two cardinal inventory rules: stock movement immutability (BR-004) and FEFO batch selection (BR-006). It depends on the following injected collaborators:

- `StockMovementRepository` — append-only writes to `stock_movements`
- `StockLevelRepository` — reads and in-place updates of `stock_levels`
- `BatchRepository` — reads and updates of `batches`
- `StockCountRepository` — reads and writes to `stock_counts` and `stock_count_items`
- `StockAdjustmentRepository` — reads and writes to `stock_adjustments`
- `BusinessSettingsRepository` — reads the `adjustment_approval_threshold` setting
- `AuditLogService` — audit trail writes

---

## 2. Method Signatures and Behaviour

### 2.1 recordMovement

```php
public function recordMovement(StockMovement $movement): void;
```

`StockMovement` value object fields: `franchiseId`, `productId`, `warehouseId`, `batchId` (nullable), `movementType`, `quantity`, `unitCost` (nullable), `referenceId` (nullable), `referenceType` (nullable), `notes` (nullable), `createdBy`.

**Behaviour (BR-004):**

1. Validate that `quantity != 0`.
2. Validate that the product belongs to `franchiseId` by querying `products WHERE id = $movement->productId AND franchise_id = $franchiseId`.
3. Validate that the warehouse belongs to `franchiseId`.
4. If `batchId` is non-null, validate that the batch belongs to the product and warehouse.
5. INSERT the row into `stock_movements`. This row is never updated or deleted after insertion.
6. Apply the quantity delta to `stock_levels`: execute an upsert — if a row exists for `(product_id, warehouse_id)`, increment `quantity` by `$movement->quantity`; otherwise insert a new row.
7. If `batchId` is non-null, update `batches.quantity` by `$movement->quantity`.
8. Fire `StockMovementRecorded` event; the audit observer writes `action = 'stock.movement.{movementType}'` with `new_values = { productId, warehouseId, quantity, movementType }`.

**Immutability enforcement:** The application database user account has `INSERT` privilege only on `stock_movements`. No `UPDATE` or `DELETE` is granted at the database level.

---

### 2.2 enforceFefo

```php
public function enforceFefo(int $productId, int $franchiseId, int $warehouseId): Batch;
```

**Behaviour (BR-006):**

1. Verify `products.track_batches = TRUE` for `$productId`. If `FALSE`, throw `BusinessRuleViolationException` with code `FEFO_NOT_APPLICABLE`.
2. Query `batches` for all rows matching `product_id = $productId AND warehouse_id = $warehouseId AND franchise_id = $franchiseId AND quantity > 0 AND (expires_at IS NULL OR expires_at >= CURDATE())`.
3. Order by `expires_at ASC NULLS LAST`. Select the first row.
4. If no qualifying batch is found, throw `ResourceNotFoundException` with code `NO_STOCK_AVAILABLE`.
5. Return the selected `Batch` entity.

**Non-expired stock only:** batches with `expires_at < CURDATE()` are excluded. A separate scheduled job flags expired batches for manager review but does not auto-delete them.

---

### 2.3 initiateStockCount

```php
public function initiateStockCount(
    int $locationId,
    int $franchiseId,
    int $initiatedBy
): StockCount;
```

`$locationId` maps to `warehouses.id`.

**Behaviour:**

1. Check that no `stock_counts` row exists for this `warehouseId` with `status = 'in_progress'`. If one exists, throw `BusinessRuleViolationException` with code `COUNT_ALREADY_IN_PROGRESS`.
2. Snapshot current stock levels: query all `stock_levels` rows for `warehouse_id = $locationId AND franchise_id = $franchiseId`. For each row, insert a `stock_count_items` row with `expected_quantity = stock_levels.quantity` and `counted_quantity = NULL`.
3. Insert a `stock_counts` row with `status = 'in_progress'`, `warehouse_id = $locationId`, `started_at = UTC_NOW()`.
4. Fire `StockCountInitiated` event; the audit observer writes `action = 'stock.count.initiated'`.
5. Return the `StockCount` entity.

**Freeze note:** While a count is `in_progress`, the reporting layer marks the warehouse's stock figures as "count in progress" for dashboard display. Stock movements for the warehouse are still accepted (sales continue); variances are computed against the snapshot taken at initiation.

---

### 2.4 submitCountVariance

```php
public function submitCountVariance(
    int $countId,
    array $variances,
    int $franchiseId,
    int $submittedBy
): StockCountResult;
```

`$variances` is `array<array{ productId: int, batchId: int|null, countedQuantity: float }>`.

**Behaviour:**

1. Retrieve the `stock_counts` row; verify `status = 'in_progress'` and `franchise_id = $franchiseId`.
2. For each element in `$variances`:
   a. Find the corresponding `stock_count_items` row.
   b. Set `stock_count_items.counted_quantity = $counted`.
   c. Compute `variance = counted_quantity - expected_quantity`.
   d. Set `stock_count_items.variance = $variance`.
3. Compute the monetary value of the total variance: $VarianceValue = \sum_{i} |variance_i \times cost\_price_i|$.
4. Retrieve `businesses.adjustment_approval_threshold` for the tenant.
5. If $VarianceValue > threshold$: set `stock_counts.status = 'pending_approval'`; no stock level updates yet.
6. If $VarianceValue \leq threshold$: set `stock_counts.status = 'auto_approved'`; call `recordMovement()` for each non-zero variance with `movement_type = 'adjustment'`.
7. Fire `StockCountSubmitted` event; the audit observer writes `action = 'stock.count.submitted'`.
8. Return `StockCountResult { countId, totalVarianceValue, status, varianceItems }`.

---

### 2.5 approveAdjustment

```php
public function approveAdjustment(
    int $adjustmentId,
    int $managerId,
    int $franchiseId
): void;
```

**Pre-conditions:**

- The `stock_counts` row must have `status = 'pending_approval'`.
- `$managerId` must hold the `inventory.adjustments.approve` permission (Branch Manager or Business Owner).

**Behaviour (BR-005):**

1. Verify `$managerId` holds `inventory.adjustments.approve` permission via `RBACService::can()`.
2. For each `stock_count_items` row with non-zero variance belonging to this `adjustmentId`, call `StockService::recordMovement()` with `movement_type = 'adjustment'` and the signed variance quantity.
3. Set `stock_counts.status = 'approved'`, `approved_by = $managerId`, `approved_at = UTC_NOW()`.
4. Fire `StockAdjustmentApproved` event; audit observer writes `action = 'stock.adjustment.approved'` with `new_values = { adjustmentId, managerId, totalVarianceValue }`.

---

## 3. Low-Stock Alert

A scheduled job (`StockAlertJob`) runs every 30 minutes and queries:

```sql
SELECT sl.product_id, sl.warehouse_id, sl.quantity, p.reorder_level, p.name
FROM stock_levels sl
JOIN products p ON sl.product_id = p.id
WHERE sl.franchise_id = :franchiseId
  AND sl.quantity <= p.reorder_level
  AND p.reorder_level > 0
  AND p.is_active = TRUE;
```

For each matching row, the job calls `NotificationService::sendLowStockAlert()`, which dispatches an Africa's Talking SMS to the Business Owner's registered phone number and an in-app push notification via Firebase Cloud Messaging.

Alerts are de-duplicated: if an alert for the same `(product_id, warehouse_id)` was sent within the last 24 hours, the job skips that row.

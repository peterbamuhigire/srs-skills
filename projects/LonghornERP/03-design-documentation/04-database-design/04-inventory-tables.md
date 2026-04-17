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
| `avg_cost` | DECIMAL(18,4) | NOT NULL, DEFAULT 0 | Current weighted-average unit cost in the tenant's base currency. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `item_id`, `branch_id`).

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

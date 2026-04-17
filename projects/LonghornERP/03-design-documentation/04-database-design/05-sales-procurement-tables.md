# Sales and Procurement Module Tables

The Sales (SALES) and Procurement (PROCUREMENT) modules are core modules active for all tenants. The tables below support customer management, invoicing, payment recording, supplier management, purchase orders, goods receipt matching, and supplier invoice processing.

## `customers`

Master record for each customer of the tenant. Stores credit terms and tax identity information used on invoices and statutory reports.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(255) | NOT NULL | Customer legal or trading name. |
| `tax_id` | VARCHAR(50) | NULL | Customer Tax Identification Number (TIN) or VAT registration number; required for B2B invoicing where tax law mandates it. |
| `credit_limit` | DECIMAL(18,4) | NOT NULL, DEFAULT 0 | Maximum outstanding balance permitted; 0 means no credit limit enforced. |
| `payment_terms_days` | SMALLINT UNSIGNED | NOT NULL, DEFAULT 0 | Default payment due period in days from invoice date. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `name`).

---

## `invoices`

Sales invoice header. Each invoice represents a billing document issued to a customer for goods or services delivered.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `invoice_number` | VARCHAR(30) | NOT NULL | System-generated sequential invoice reference (e.g., `INV-2026-000001`). |
| `customer_id` | BIGINT UNSIGNED | NOT NULL, FK → `customers.id` | The billed customer. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | Branch issuing the invoice. |
| `invoice_date` | DATE | NOT NULL | Date the invoice is raised. |
| `due_date` | DATE | NOT NULL | Payment due date, calculated from `invoice_date` + `payment_terms_days`. |
| `subtotal` | DECIMAL(18,4) | NOT NULL | Sum of all line totals before tax. |
| `tax_amount` | DECIMAL(18,4) | NOT NULL, DEFAULT 0 | Total VAT charged on the invoice. |
| `total` | DECIMAL(18,4) | NOT NULL | Grand total including tax (`subtotal` + `tax_amount`). |
| `status` | ENUM('draft','posted','partially_paid','paid','overdue','cancelled') | NOT NULL, DEFAULT 'draft' | Invoice lifecycle state. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `invoice_number`), (`tenant_id`, `customer_id`, `status`), (`tenant_id`, `status`, `due_date`).

---

## `invoice_items`

Line items for a sales invoice. Each row represents one item sold with its pricing, discount, and applicable tax code.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `invoice_id` | BIGINT UNSIGNED | NOT NULL, FK → `invoices.id` | Parent invoice. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | Item sold. |
| `quantity` | DECIMAL(15,4) | NOT NULL | Quantity invoiced. |
| `unit_price` | DECIMAL(18,4) | NOT NULL | Selling price per unit before discount. |
| `discount_percent` | DECIMAL(7,4) | NOT NULL, DEFAULT 0 | Line-level discount percentage (0–100). |
| `tax_code_id` | BIGINT UNSIGNED | NULL, FK → `tax_codes.id` | Tax code applied to this line; NULL for tax-exempt lines. |
| `line_total` | DECIMAL(18,4) | NOT NULL | Computed line total: `quantity` × `unit_price` × (1 − `discount_percent` / 100), excluding tax. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `invoice_id`), (`tenant_id`, `item_id`).

---

## `payments`

Records each payment received from a customer against an invoice.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `customer_id` | BIGINT UNSIGNED | NOT NULL, FK → `customers.id` | The paying customer. |
| `invoice_id` | BIGINT UNSIGNED | NOT NULL, FK → `invoices.id` | The invoice being settled. |
| `amount` | DECIMAL(18,4) | NOT NULL | Amount received in the tenant's base currency. |
| `payment_date` | DATE | NOT NULL | Date the payment was received. |
| `payment_method` | ENUM('cash','bank_transfer','mobile_money','cheque','card') | NOT NULL | Payment channel. |
| `reference` | VARCHAR(100) | NULL | Bank reference, mobile money transaction ID, or cheque number. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `customer_id`, `payment_date`), (`tenant_id`, `invoice_id`).

---

## `suppliers`

Master record for each supplier. Stores tax and payment terms data used in procurement and statutory Withholding Tax (WHT) processing.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `name` | VARCHAR(255) | NOT NULL | Supplier legal name. |
| `tax_id` | VARCHAR(50) | NULL | Supplier TIN; required for WHT returns. |
| `payment_terms_days` | SMALLINT UNSIGNED | NOT NULL, DEFAULT 0 | Default payment due period in days. |
| `wht_applicable` | TINYINT(1) | NOT NULL, DEFAULT 0 | 1 = WHT must be deducted on payments to this supplier. |
| `bank_account` | VARCHAR(100) | NULL | Supplier bank account details for payment instructions. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `name`).

---

## `purchase_orders`

Header record for a Local Purchase Order (LPO) raised to a supplier.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `po_number` | VARCHAR(30) | NOT NULL | System-generated LPO reference number (e.g., `LPO-2026-000001`). |
| `supplier_id` | BIGINT UNSIGNED | NOT NULL, FK → `suppliers.id` | Supplier being ordered from. |
| `branch_id` | BIGINT UNSIGNED | NOT NULL, FK → `branches.id` | Branch for which the order is placed. |
| `order_date` | DATE | NOT NULL | Date the LPO was raised. |
| `status` | ENUM('draft','approved','partially_received','received','cancelled') | NOT NULL, DEFAULT 'draft' | Order lifecycle state. |
| `total` | DECIMAL(18,4) | NOT NULL | Total order value inclusive of all line items. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `po_number`), (`tenant_id`, `supplier_id`, `status`).

---

## `purchase_order_items`

Line items for a purchase order, specifying item, quantity, and agreed unit cost.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `po_id` | BIGINT UNSIGNED | NOT NULL, FK → `purchase_orders.id` | Parent purchase order. |
| `item_id` | BIGINT UNSIGNED | NOT NULL, FK → `stock_items.id` | Item being ordered. |
| `quantity` | DECIMAL(15,4) | NOT NULL | Ordered quantity. |
| `unit_cost` | DECIMAL(18,4) | NOT NULL | Agreed unit cost at the time of ordering. |
| `line_total` | DECIMAL(18,4) | NOT NULL | `quantity` × `unit_cost`. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `po_id`), (`tenant_id`, `item_id`).

---

## `purchase_invoices`

Records the supplier's invoice, linked to the purchase order and Goods Receipt Note (GRN) for three-way matching verification.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK → `tenants.id` | Tenant scope. |
| `supplier_id` | BIGINT UNSIGNED | NOT NULL, FK → `suppliers.id` | Invoicing supplier. |
| `po_id` | BIGINT UNSIGNED | NULL, FK → `purchase_orders.id` | Linked purchase order; NULL if no prior LPO was raised. |
| `grn_id` | BIGINT UNSIGNED | NULL, FK → `goods_receipts.id` | Linked goods receipt; NULL if invoice precedes delivery. |
| `invoice_number` | VARCHAR(100) | NOT NULL | Supplier's own invoice reference number. |
| `invoice_date` | DATE | NOT NULL | Date on the supplier's invoice. |
| `total` | DECIMAL(18,4) | NOT NULL | Total amount payable to the supplier. |
| `status` | ENUM('draft','matched','approved','paid','disputed','cancelled') | NOT NULL, DEFAULT 'draft' | Three-way matching and payment lifecycle state. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `supplier_id`, `status`), (`tenant_id`, `po_id`), (`tenant_id`, `grn_id`).

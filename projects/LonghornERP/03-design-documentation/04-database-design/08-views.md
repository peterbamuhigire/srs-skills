# SQL Views Specification

SQL views in Longhorn ERP provide pre-defined query surfaces for reporting, dashboards, and application list screens. All views include `tenant_id` in their SELECT list and WHERE clauses; the application layer always appends a `WHERE tenant_id = :tenant_id` binding when querying a view. Views are read-only and are never used as write targets.

## `v_current_stock`

### Purpose

Provides real-time quantity on hand and average cost for every item at every branch. This is the primary source for stock enquiry screens and the low-stock alert job.

### Base Tables

`stock_balance`, `stock_items`, `branches`, `item_categories`, `uom`

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `item_id` | Stock item primary key. |
| `item_code` | Item code. |
| `item_name` | Item description. |
| `category_name` | Item category name. |
| `branch_id` | Branch primary key. |
| `branch_name` | Branch name. |
| `uom_code` | Stocking unit of measure. |
| `quantity` | Current quantity on hand. |
| `avg_cost` | Current weighted-average unit cost. |
| `stock_value` | `quantity` × `avg_cost`. |
| `reorder_level` | Reorder threshold from `stock_items`. |
| `is_below_reorder` | 1 if `quantity` ≤ `reorder_level`, otherwise 0. |

### Use Case

Used by the Inventory module stock enquiry screen, the purchasing reorder report, and the `v_low_stock_items` view as a base source.

---

## `v_low_stock_items`

### Purpose

Filters `v_current_stock` to return only items where `quantity` is at or below `reorder_level` and `reorder_level` > 0. Used by the reorder alert dashboard and the automated purchase requisition suggestion job.

### Base Tables

`v_current_stock` (derived), `stock_items`, `item_categories`

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `item_id` | Stock item primary key. |
| `item_code` | Item code. |
| `item_name` | Item description. |
| `category_name` | Category name. |
| `branch_id` | Branch primary key. |
| `branch_name` | Branch name. |
| `quantity` | Current quantity on hand. |
| `reorder_level` | Configured reorder threshold. |
| `shortfall` | `reorder_level` − `quantity`; the quantity needed to restore to threshold. |

### Use Case

Dashboard alert widget showing items that require immediate replenishment. Also used to auto-populate purchase requisition suggestions.

---

## `v_customer_aging_analysis`

### Purpose

Computes Accounts Receivable (AR) aging by grouping outstanding invoice balances into standard aging buckets relative to today's date.

### Base Tables

`invoices`, `customers`, `payments` (aggregated as `amount_paid`)

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `customer_id` | Customer primary key. |
| `customer_name` | Customer name. |
| `invoice_id` | Invoice primary key. |
| `invoice_number` | Invoice reference. |
| `invoice_date` | Invoice date. |
| `due_date` | Payment due date. |
| `total` | Invoice total. |
| `amount_paid` | Sum of payments applied to this invoice. |
| `outstanding` | `total` − `amount_paid`. |
| `days_overdue` | `DATEDIFF(CURRENT_DATE, due_date)` where positive means overdue. |
| `current_bucket` | Outstanding amount due in ≤ 0 days (not yet overdue). |
| `bucket_1_30` | Outstanding amount 1–30 days overdue. |
| `bucket_31_60` | Outstanding amount 31–60 days overdue. |
| `bucket_61_90` | Outstanding amount 61–90 days overdue. |
| `bucket_90_plus` | Outstanding amount > 90 days overdue. |

### Use Case

AR aging report, customer statement generation, and credit control alerts. Filters on `outstanding > 0` to display only unpaid or partially paid invoices.

---

## `v_supplier_aging_analysis`

### Purpose

Computes Accounts Payable (AP) aging by grouping outstanding purchase invoice balances into aging buckets relative to today's date. Mirrors `v_customer_aging_analysis` on the payables side.

### Base Tables

`purchase_invoices`, `suppliers` (aggregated payments from the supplier payments journal)

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `supplier_id` | Supplier primary key. |
| `supplier_name` | Supplier name. |
| `purchase_invoice_id` | Purchase invoice primary key. |
| `invoice_number` | Supplier invoice reference. |
| `invoice_date` | Invoice date. |
| `due_date` | Payment due date based on supplier payment terms. |
| `total` | Invoice total. |
| `amount_paid` | Sum of payments made against this invoice. |
| `outstanding` | `total` − `amount_paid`. |
| `days_overdue` | Days past due date; negative means payment not yet due. |
| `current_bucket` | Amount not yet due. |
| `bucket_1_30` | Amount 1–30 days overdue. |
| `bucket_31_60` | Amount 31–60 days overdue. |
| `bucket_61_90` | Amount 61–90 days overdue. |
| `bucket_90_plus` | Amount > 90 days overdue. |

### Use Case

AP aging report for the finance team, cash flow planning, and supplier payment scheduling.

---

## `v_account_balances`

### Purpose

Aggregates all posted `account_ledgers` entries per account to produce the current net balance for each GL account. The balance is the sum of all debits minus the sum of all credits, or vice versa, depending on account type.

### Base Tables

`account_ledgers`, `chart_of_accounts`

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `account_id` | GL account primary key. |
| `account_code` | Account code. |
| `account_name` | Account name. |
| `account_type` | ASSET, LIABILITY, EQUITY, REVENUE, or EXPENSE. |
| `total_debit` | Sum of all debit postings to this account. |
| `total_credit` | Sum of all credit postings to this account. |
| `balance` | Net balance: debit-normal accounts return `total_debit − total_credit`; credit-normal accounts return `total_credit − total_debit`. |

### Use Case

Used as the base for `v_trial_balance`, the balance sheet, and the profit-and-loss statement.

---

## `v_trial_balance`

### Purpose

Produces a trial balance report listing all active GL accounts with their current debit or credit balance. The sum of all debit balances must equal the sum of all credit balances.

### Base Tables

`v_account_balances` (derived), `chart_of_accounts`

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `account_code` | Account code, used for ordering. |
| `account_name` | Account name. |
| `account_type` | Account classification. |
| `debit_balance` | Balance shown in the debit column; non-zero for debit-normal accounts with a positive balance. |
| `credit_balance` | Balance shown in the credit column; non-zero for credit-normal accounts with a positive balance. |

### Use Case

Trial balance report exported by the Accounting module for month-end close review and external audit preparation.

---

## `v_production_efficiency_report`

### Purpose

Aggregates manufacturing Key Performance Indicators (KPIs) per production order, including planned vs. actual material usage, yield percentage, and scrap rate. Available only when the Manufacturing (MANUFACTURING) module is active.

### Base Tables

`production_orders`, `production_order_items` (raw material issues), `bom_items` (Bill of Materials), `stock_ledger` (filtered to `PRODUCTION_IN` and `PRODUCTION_OUT` movements)

### Key Columns

| Column | Description |
|---|---|
| `tenant_id` | Tenant scope. |
| `production_order_id` | Production order primary key. |
| `order_reference` | Production order reference number. |
| `finished_item_id` | The finished goods item produced. |
| `finished_item_name` | Finished goods item name. |
| `planned_quantity` | Quantity ordered for production. |
| `actual_quantity` | Quantity confirmed as produced output. |
| `yield_percent` | `(actual_quantity / planned_quantity) × 100`. |
| `planned_material_cost` | Expected material cost from BOM valuation. |
| `actual_material_cost` | Actual material cost from `stock_ledger` PRODUCTION_OUT movements. |
| `variance` | `actual_material_cost − planned_material_cost`. |
| `scrap_quantity` | Quantity posted as scrap. |
| `scrap_percent` | `(scrap_quantity / planned_quantity) × 100`. |

### Use Case

Manufacturing efficiency dashboard and production cost variance report. Used by production managers to identify yield losses and high-variance production runs.

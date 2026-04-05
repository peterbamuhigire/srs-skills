# Schema Entity Map — Maduuka Phase 1

**Source:** `DatabaseDesign_Maduuka.docx` (30+ tables, 10 groups)
**Date:** 2026-04-05

| Table Group | Module | Key Tables (inferred from feature register) |
|---|---|---|
| 1 — POS | F-001 | `sales`, `sale_items`, `sale_payments`, `pos_sessions`, `receipts`, `held_carts` |
| 2 — Inventory | F-002 | `products`, `product_categories`, `stock_levels`, `stock_movements`, `batches`, `stock_adjustments`, `stock_transfers` |
| 3 — Customers | F-003 | `customers`, `customer_groups`, `credit_accounts`, `customer_transactions` |
| 4 — Suppliers | F-004 | `suppliers`, `purchase_orders`, `po_items`, `goods_receipts`, `supplier_invoices`, `supplier_payments` |
| 5 — Expenses | F-005 | `expense_categories`, `expenses`, `petty_cash_floats`, `expense_approvals` |
| 6 — Financial Accounts | F-006 | `payment_accounts`, `account_transactions`, `bank_reconciliations` |
| 7 — Sales Reports | F-007 | Derived from sales + inventory tables; no dedicated tables except `scheduled_reports` |
| 8 — HR / Payroll | F-008 | `staff`, `contracts`, `leave_types`, `leave_requests`, `attendance`, `salary_structures`, `payroll_runs`, `payslips`, `staff_loans` |
| 9 — Dashboard | F-009 | Derived views; no dedicated tables except `dashboard_settings` |
| 10 — Settings | F-010 | `businesses`, `branches`, `tax_settings`, `receipt_templates`, `smtp_settings`, `subscription_plans`, `connected_devices` |
| Cross-cutting | Multi-tenant | `tenants`, `users`, `roles`, `permissions`, `audit_log` |

*Note: Exact column-level detail is in `DatabaseDesign_Maduuka.docx`. This map is derived from the feature register for traceability purposes.*

## EFRIS Placeholder Columns

EFRIS column placeholders exist in the Phase 1 schema for Phase 3 readiness:
- `invoices.efris_fdn` — Fiscal Document Number from URA
- `invoices.efris_qr_code` — URA QR code for receipts
- `invoices.efris_status` — submission status (pending / submitted / confirmed / failed)
- `products.efris_item_code` — URA standard catalogue code

*These columns are nullable in Phase 1 and only populated when the EFRIS add-on (F-015) is active.*

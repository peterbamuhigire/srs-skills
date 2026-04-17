# 5. Database Architecture

## 5.1 Engine and Configuration

| Parameter | Value |
|---|---|
| Engine | MySQL 9.1 InnoDB |
| Character set | `utf8mb4` |
| Collation | `utf8mb4_unicode_ci` |
| Storage engine | InnoDB (all tables — required for foreign key constraints and ACID transactions) |
| Transaction isolation | `REPEATABLE-READ` (MySQL default) |
| Binary logging | Enabled (`binlog_format=ROW` for point-in-time recovery) |
| Foreign keys | Enabled globally (`foreign_key_checks=ON`) |

## 5.2 Schema Design Principles

1. **Single schema for all 17 modules.** All 17 operational modules share one MySQL database (`birdc_erp`). There is no schema-per-module or microservice database splitting. Cross-module joins are first-class citizens.
2. **Table naming convention:** `tbl_<domain>_<entity>` (e.g., `tbl_sales_invoices`, `tbl_inventory_batches`, `tbl_gl_journal_lines`).
3. **Primary keys:** unsigned `BIGINT AUTO_INCREMENT` on all tables. No string or composite primary keys except on bridge/pivot tables.
4. **Soft deletes:** financial records (invoices, payments, journal entries, payroll runs) are never physically deleted. A `deleted_at TIMESTAMP NULL` column marks soft-deleted records. Hard deletes are reserved for non-financial reference data only.
5. **Audit columns:** every table carries `created_at`, `created_by`, `updated_at`, `updated_by` columns.
6. **Enum types:** use `TINYINT` + application-layer constant mapping (not MySQL `ENUM`) for status fields, to avoid schema migrations when new statuses are added.
7. **Indexing:** every foreign key column is indexed. Columns appearing in `WHERE`, `ORDER BY`, and `GROUP BY` clauses in high-frequency queries carry composite indexes. Index naming: `idx_<table>_<columns>`.
8. **No nullable foreign keys on core relationships:** a journal line without a journal header, or an invoice without a customer, is a data integrity failure — enforced by `NOT NULL` constraints.

## 5.3 Foreign Key Relationships — Core Domains

The following table identifies the primary inter-domain foreign key relationships that enforce referential integrity across modules.

| Child Table | Foreign Key Column | References | Cascade Rule |
|---|---|---|---|
| `tbl_sales_invoice_lines` | `invoice_id` | `tbl_sales_invoices.id` | CASCADE DELETE |
| `tbl_sales_invoices` | `customer_id` | `tbl_customers.id` | RESTRICT |
| `tbl_pos_sale_items` | `sale_id` | `tbl_pos_sales.id` | CASCADE DELETE |
| `tbl_gl_journal_lines` | `journal_id` | `tbl_gl_journals.id` | CASCADE DELETE |
| `tbl_gl_journal_lines` | `account_id` | `tbl_coa_accounts.id` | RESTRICT |
| `tbl_inventory_movements` | `batch_id` | `tbl_inventory_batches.id` | RESTRICT |
| `tbl_agent_stock_movements` | `agent_id` | `tbl_agents.id` | RESTRICT |
| `tbl_procurement_grn_lines` | `grn_id` | `tbl_procurement_grns.id` | CASCADE DELETE |
| `tbl_procurement_grn_lines` | `lpo_line_id` | `tbl_procurement_lpo_lines.id` | RESTRICT |
| `tbl_production_orders` | `recipe_id` | `tbl_manufacturing_recipes.id` | RESTRICT |
| `tbl_production_outputs` | `production_order_id` | `tbl_production_orders.id` | CASCADE DELETE |
| `tbl_qc_inspections` | `batch_id` | `tbl_inventory_batches.id` | RESTRICT |
| `tbl_farmer_contributions` | `farmer_id` | `tbl_farmers.id` | RESTRICT |
| `tbl_farmer_contributions` | `batch_receipt_id` | `tbl_procurement_cooperative_receipts.id` | RESTRICT |
| `tbl_payroll_run_lines` | `payroll_run_id` | `tbl_payroll_runs.id` | RESTRICT |
| `tbl_payroll_run_lines` | `employee_id` | `tbl_employees.id` | RESTRICT |
| `tbl_agent_remittances` | `agent_id` | `tbl_agents.id` | RESTRICT |

## 5.4 Stored Procedures

The following stored procedures encode complex transactional business logic that must execute atomically.

| Procedure | Purpose | Triggered By |
|---|---|---|
| `sp_apply_remittance_to_invoices` | FIFO allocation of an agent remittance to outstanding invoices (BR-002) | `AgentService::applyRemittance()` |
| `sp_post_gl_journal` | Post a balanced journal entry; validate debit = credit; assign sequential JE number; compute and store hash chain entry (BR-013) | `GLService::postJournal()` |
| `sp_close_production_order` | Verify mass balance (BR-008); transfer finished goods to QC-pending inventory; close order | `ManufacturingService::recordCompletion()` |
| `sp_compute_agent_commission` | Calculate commission on invoices cleared by a verified remittance (BR-015) | `AgentService::calculateCommission()` |
| `sp_run_payroll` | Batch gross-to-net computation for all active employees in a period | `PayrollService::computePayroll()` |
| `sp_verify_three_way_match` | Validate LPO → GRN → vendor invoice price and quantity tolerances (BR-012) | `ProcurementService::threeWayMatch()` |

## 5.5 Database Triggers

| Trigger | Table | Event | Action |
|---|---|---|---|
| `trg_invoice_number_seq` | `tbl_sales_invoices` | BEFORE INSERT | Assign next sequential invoice number; detect gaps (BR-009) |
| `trg_je_number_seq` | `tbl_gl_journals` | BEFORE INSERT | Assign next sequential JE number (JE-YYYY-NNNN); detect gaps (BR-009) |
| `trg_payroll_lock` | `tbl_payroll_runs` | BEFORE UPDATE | Block modifications to approved and locked payroll runs (BR-010) |
| `trg_audit_insert` | All audited tables | AFTER INSERT | Append record to `tbl_audit_log` |
| `trg_audit_update` | All audited tables | AFTER UPDATE | Append old and new values to `tbl_audit_log` |
| `trg_budget_vote_alert` | `tbl_gl_journal_lines` | AFTER INSERT | Compute cumulative spend per vote; generate alert at 80% and 95% (BR-014) |
| `trg_agent_float_check` | `tbl_agent_stock_movements` | BEFORE INSERT | Block issuance if agent float limit would be exceeded (BR-006) |

## 5.6 Views

Commonly used complex joins are encapsulated in database views to simplify reporting queries and application code.

| View | Purpose |
|---|---|
| `vw_agent_cash_balance` | Live net liability per agent: sum(invoice values) - sum(verified remittances) |
| `vw_stock_on_hand` | Current warehouse stock balance by location, product, and batch |
| `vw_agent_stock_on_hand` | Current agent stock balance by agent, product, and batch |
| `vw_ar_aging` | Customer AR aging buckets: current, 30, 60, 90, 120+ days |
| `vw_trial_balance` | Current trial balance: account code, name, debit total, credit total, net |
| `vw_budget_vs_actual` | Parliamentary vote and commercial budget vs. actual expenditure |
| `vw_production_mass_balance` | Per-production-order mass balance: inputs vs. outputs vs. variance |

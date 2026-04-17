## Section 10 — EFRIS Queue Table

---

### tbl_efris_queue

**Purpose:** Tracks every fiscal document submission to URA EFRIS — invoices, credit notes, POS receipts. Supports retry logic on failure (up to 3 automatic retries; Finance Manager alerted on third failure).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `queue_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Queue record primary key |
| `document_type` | `ENUM('invoice','credit_note','pos_receipt','proforma')` | NOT NULL | Type of fiscal document |
| `document_id` | `INT UNSIGNED` | NOT NULL | Primary key of the document (`invoice_id` or `transaction_id`) |
| `document_number` | `VARCHAR(30)` | NOT NULL | Document number (for logging) |
| `submission_payload` | `JSON` | NOT NULL | JSON payload submitted to EFRIS API |
| `status` | `ENUM('pending','submitted','accepted','failed','permanently_failed')` | NOT NULL DEFAULT 'pending' | Submission status |
| `retry_count` | `TINYINT UNSIGNED` | NOT NULL DEFAULT 0 | Number of submission attempts |
| `last_attempted_at` | `DATETIME` | NULL | Most recent attempt timestamp |
| `fdn` | `VARCHAR(100)` | NULL | Fiscal Document Number returned by URA on acceptance |
| `qr_code` | `TEXT` | NULL | QR code data returned by URA |
| `response_payload` | `JSON` | NULL | Full URA API response |
| `error_message` | `TEXT` | NULL | Error detail on failure |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

**Indexes:** `INDEX(status)`, `INDEX(document_type, document_id)`, `INDEX(last_attempted_at)`, `INDEX(retry_count)`

```sql
CREATE TABLE tbl_efris_queue (
  queue_id           INT UNSIGNED NOT NULL AUTO_INCREMENT,
  document_type      ENUM('invoice','credit_note','pos_receipt','proforma') NOT NULL,
  document_id        INT UNSIGNED NOT NULL,
  document_number    VARCHAR(30)  NOT NULL,
  submission_payload JSON         NOT NULL,
  status             ENUM('pending','submitted','accepted','failed','permanently_failed')
                     NOT NULL DEFAULT 'pending',
  retry_count        TINYINT UNSIGNED NOT NULL DEFAULT 0,
  last_attempted_at  DATETIME     NULL,
  fdn                VARCHAR(100) NULL,
  qr_code            TEXT         NULL,
  response_payload   JSON         NULL,
  error_message      TEXT         NULL,
  created_at         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (queue_id),
  KEY idx_efris_status (status),
  KEY idx_efris_document (document_type, document_id),
  KEY idx_efris_retry (retry_count),
  KEY idx_efris_attempted (last_attempted_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Business logic:** A PHP background worker (cron job or WorkManager equivalent) polls for `status IN ('pending','failed')` AND `retry_count < 3`. On third failure, `status` is set to `permanently_failed` and the Finance Manager receives an alert email.

---

## Section 11 — Table Inventory Summary

The following table summarises all 55 primary database tables defined in this specification, grouped by module.

| # | Table Name | Module | Purpose Summary |
|---|---|---|---|
| 1 | `tbl_users` | Auth | System user accounts |
| 2 | `tbl_roles` | Auth | Role definitions |
| 3 | `tbl_permissions` | Auth | Permission codes |
| 4 | `tbl_role_permissions` | Auth | Role-permission junction |
| 5 | `tbl_user_sessions` | Auth | JWT refresh token sessions |
| 6 | `tbl_audit_log` | Auth | Immutable system audit trail |
| 7 | `tbl_invoices` | Sales | Sales invoice master |
| 8 | `tbl_invoice_items` | Sales | Invoice line items |
| 9 | `tbl_price_lists` | Sales | Named price lists |
| 10 | `tbl_price_list_items` | Sales | Price list product mappings |
| 11 | `tbl_territories` | Sales | Sales territories |
| 12 | `tbl_sales_targets` | Sales | Sales targets per territory/agent |
| 13 | `tbl_customers` | Sales | Customer master (referenced by invoices) |
| 14 | `tbl_pos_sessions` | POS | POS session management |
| 15 | `tbl_pos_transactions` | POS | POS sale transactions |
| 16 | `tbl_pos_transaction_items` | POS | POS sale line items |
| 17 | `tbl_pos_payments` | POS | POS payment methods |
| 18 | `tbl_quick_keys` | POS | Agent quick-key grid layout |
| 19 | `tbl_stock_items` | Inventory | Product catalogue |
| 20 | `tbl_stock_balance` | Inventory | Warehouse stock balances (BR-001) |
| 21 | `tbl_agent_stock_balance` | Inventory | Agent field stock (BR-001 — separate) |
| 22 | `tbl_stock_movements` | Inventory | Immutable movement ledger |
| 23 | `tbl_batches` | Inventory | Batch and lot tracking |
| 24 | `tbl_stock_locations` | Inventory | Warehouse locations |
| 25 | `tbl_uom_conversions` | Inventory | Unit of measure conversions |
| 26 | `tbl_stock_adjustments` | Inventory | Approved stock adjustments |
| 27 | `tbl_agents` | Agents | Agent master register (1,071 agents) |
| 28 | `tbl_agent_remittances` | Agents | Agent cash remittances |
| 29 | `tbl_agent_commissions` | Agents | Commission accrual records |
| 30 | `tbl_agent_territories` | Agents | Agent-territory mapping |
| 31 | `tbl_accounts` | Finance | Chart of accounts — dual-mode (DC-004) |
| 32 | `tbl_journals` | Finance | GL journal headers — hash chain (BR-013) |
| 33 | `tbl_journal_lines` | Finance | GL journal lines |
| 34 | `tbl_accounting_periods` | Finance | Open/closed accounting periods |
| 35 | `tbl_budgets` | Finance | Budget headers |
| 36 | `tbl_budget_lines` | Finance | Budget line items |
| 37 | `tbl_bank_accounts` | Finance | Bank and imprest accounts |
| 38 | `tbl_purchase_requests` | Procurement | Purchase requests (PPDA workflow) |
| 39 | `tbl_purchase_orders` | Procurement | Local Purchase Orders |
| 40 | `tbl_po_items` | Procurement | PO line items |
| 41 | `tbl_goods_receipts` | Procurement | Goods Receipt Notes |
| 42 | `tbl_grn_items` | Procurement | GRN line items |
| 43 | `tbl_vendors` | Procurement | Supplier master |
| 44 | `tbl_cooperative_batches` | Farmers | Cooperative batch receipts |
| 45 | `tbl_farmer_contributions` | Farmers | Individual farmer delivery records |
| 46 | `tbl_farmers` | Farmers | Farmer master register (6,440+) |
| 47 | `tbl_farms` | Farmers | Farm GPS profiles |
| 48 | `tbl_cooperatives` | Farmers | Cooperative organisations |
| 49 | `tbl_recipes` | Manufacturing | Recipes / Bills of Materials |
| 50 | `tbl_recipe_ingredients` | Manufacturing | Recipe inputs and outputs (circular economy) |
| 51 | `tbl_production_orders` | Manufacturing | Production order management |
| 52 | `tbl_production_completions` | Manufacturing | Actual completion quantities |
| 53 | `tbl_job_cards` | Manufacturing | Worker step instructions |
| 54 | `tbl_inspections` | QC | QC inspection records |
| 55 | `tbl_inspection_results` | QC | Per-parameter test results |
| 56 | `tbl_certificates_of_analysis` | QC | CoA per batch per market |
| 57 | `tbl_ncrs` | QC | Non-Conformance Reports |
| 58 | `tbl_equipment` | QC | Equipment and calibration register |
| 59 | `tbl_employees` | HR | Employee master |
| 60 | `tbl_leave_types` | HR | Leave type definitions |
| 61 | `tbl_leave_requests` | HR | Leave applications |
| 62 | `tbl_attendance` | HR | Attendance records (biometric + manual) |
| 63 | `tbl_payroll_runs` | Payroll | Payroll run headers |
| 64 | `tbl_payroll_lines` | Payroll | Per-employee payroll calculations |
| 65 | `tbl_payroll_elements` | Payroll | Configurable payroll element definitions |
| 66 | `tbl_efris_queue` | EFRIS | Fiscal document submission queue |

**Total: 66 tables** across 17 modules.

---

## Human Review Gate

The following open items require consultant and client review before database seeding begins:

- `[CONTEXT-GAP: GAP-012]` — confirm existence of BIRDC Chart of Accounts before seeding `tbl_accounts` with 1,307 account codes.
- `[CONTEXT-GAP: GAP-004]` — Uganda Data Protection and Privacy Act 2019 legal review required before `tbl_farmers` stores GPS coordinates, NIN, photo, and mobile money number.
- `[CONTEXT-GAP: GAP-010]` — export QC parameter limits for South Korea, EU, Saudi Arabia, Qatar, and USA required to design `tbl_inspection_results` validation constraints for `tbl_certificates_of_analysis` market-specific templates.

---

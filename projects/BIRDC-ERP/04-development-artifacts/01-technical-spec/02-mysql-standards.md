# 2. MySQL 9.1 Database Standards

## 2.1 Engine, Character Set, and Collation

All tables use InnoDB engine with `utf8mb4` character set and `utf8mb4_unicode_ci` collation. These settings are applied at both the database and table level:

```sql
CREATE DATABASE birdc_erp
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

Every `CREATE TABLE` statement explicitly declares:

```sql
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
```

`utf8mb4` supports the full Unicode character set including emoji (relevant for farmer name fields that may contain East African diacritics) and 4-byte characters.

## 2.2 Table Naming Convention

All tables use the `tbl_` prefix followed by a descriptive plural noun in `snake_case`.

| Module | Table Name Examples |
|---|---|
| Finance | `tbl_journal_entries`, `tbl_gl_entries`, `tbl_chart_of_accounts`, `tbl_invoices`, `tbl_invoice_lines` |
| Inventory | `tbl_stock_balance`, `tbl_stock_transactions`, `tbl_products`, `tbl_batches` |
| Agent Distribution | `tbl_agents`, `tbl_agent_stock_balance`, `tbl_remittances` |
| Farmers | `tbl_farmers`, `tbl_cooperatives`, `tbl_farmer_contributions`, `tbl_farmer_payments` |
| Production | `tbl_production_orders`, `tbl_production_order_lines`, `tbl_bom_headers`, `tbl_bom_lines` |
| HR / Payroll | `tbl_employees`, `tbl_payroll_runs`, `tbl_payroll_lines`, `tbl_leave_requests` |
| System | `tbl_users`, `tbl_roles`, `tbl_permissions`, `tbl_audit_log` |

**Key tables from business rules:**

- `tbl_stock_balance` — warehouse stock only (BR-001)
- `tbl_agent_stock_balance` — agent field stock only (BR-001); never joined with `tbl_stock_balance` in any query except explicitly labelled consolidated reports
- `tbl_gl_entries` — includes `hash_value` column for hash chain integrity (BR-013)

## 2.3 Mandatory Columns

Every table in the system must include the following columns:

| Column | Type | Constraint | Purpose |
|---|---|---|---|
| `id` | `INT UNSIGNED` | `NOT NULL AUTO_INCREMENT PRIMARY KEY` | Surrogate primary key |
| `created_at` | `DATETIME` | `NOT NULL DEFAULT CURRENT_TIMESTAMP` | Record creation timestamp |
| `updated_at` | `DATETIME` | `NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Last modification timestamp |
| `created_by` | `INT UNSIGNED` | `NOT NULL` | FK to `tbl_users.id` |
| `updated_by` | `INT UNSIGNED` | `NOT NULL` | FK to `tbl_users.id` |

Additionally, tables that support soft delete include:

| Column | Type | Constraint |
|---|---|---|
| `deleted_at` | `DATETIME` | `NULL` — NULL means active; timestamp means soft-deleted |
| `deleted_by` | `INT UNSIGNED` | `NULL` |

Financial tables (GL entries, invoice lines, payroll lines) do NOT support soft delete — records are immutable once posted (BR-003, BR-010). Corrections are always counter-entries.

## 2.4 Column Naming

All column names use `snake_case`. No abbreviations except established domain abbreviations defined in the project glossary (e.g., `nssf_amount`, `paye_amount`, `gl_account_id`, `momo_reference`).

Boolean columns use the `is_` prefix: `is_active`, `is_verified`, `is_locked`, `is_deleted`.

Status columns use `ENUM` types with values matching the domain vocabulary:

```sql
status ENUM('draft', 'pending_efris', 'issued', 'partially_paid', 'paid', 'void')
    NOT NULL DEFAULT 'draft'
```

Monetary columns use `DECIMAL(15, 2)` for all UGX amounts. For USD/EUR/KES multi-currency amounts: `DECIMAL(18, 4)`.

## 2.5 Foreign Key Conventions

All foreign key columns are named `[referenced_table_singular]_id`:

- `tbl_invoice_lines.invoice_id` references `tbl_invoices.id`
- `tbl_remittances.agent_id` references `tbl_agents.id`
- `tbl_farmer_contributions.farmer_id` references `tbl_farmers.id`

All foreign keys have an explicit `CONSTRAINT` with a descriptive name:

```sql
CONSTRAINT fk_invoice_lines_invoice
    FOREIGN KEY (invoice_id) REFERENCES tbl_invoices (id)
    ON DELETE RESTRICT ON UPDATE CASCADE
```

`ON DELETE RESTRICT` is the default. `ON DELETE CASCADE` is only permitted where the child records have no independent meaning (e.g., invoice lines cannot exist without an invoice). `ON DELETE SET NULL` is prohibited — null foreign keys lead to orphaned data.

## 2.6 Indexing Strategy

Every foreign key column has a corresponding index. In addition:

| Table | Additional Indexes |
|---|---|
| `tbl_invoices` | `(status)`, `(invoice_date)`, `(customer_id, status)` |
| `tbl_gl_entries` | `(account_id, transaction_date)`, `(journal_entry_id)` |
| `tbl_agent_stock_balance` | `(agent_id, product_id)` — unique composite index |
| `tbl_audit_log` | `(user_id, created_at)`, `(table_name, record_id)`, `(created_at)` |
| `tbl_farmers` | `(nin)` unique, `(cooperative_id)`, `(full_name)` FULLTEXT |
| `tbl_remittances` | `(agent_id, is_verified, created_at)` |

## 2.7 Stored Procedure Naming

All stored procedures use the `sp_` prefix followed by a verb and subject in `snake_case`:

| Stored Procedure | Purpose |
|---|---|
| `sp_apply_remittance_to_invoices` | FIFO remittance allocation per BR-002 |
| `sp_calculate_agent_commission` | Commission on verified sales per BR-015 |
| `sp_post_gl_entry` | GL posting with hash chain update per BR-013 |
| `sp_close_production_order` | Mass balance check and completion per BR-008 |
| `sp_run_payroll_batch` | Gross-to-net payroll calculation per module F-014 |
| `sp_verify_hash_chain` | Audit trigger — hash chain integrity check per BR-013 |
| `sp_check_float_limit` | Agent float limit enforcement per BR-006 |

Stored procedures that modify financial data are wrapped in a transaction with explicit `COMMIT` / `ROLLBACK`. All stored procedure parameters use the `p_` prefix: `p_agent_id`, `p_remittance_amount`.

## 2.8 Trigger Naming

Database triggers use the `tr_` prefix followed by the table name, timing, and event:

| Trigger Name | Table | Timing | Event | Purpose |
|---|---|---|---|---|
| `tr_gl_entries_after_insert` | `tbl_gl_entries` | `AFTER INSERT` | `INSERT` | Update hash chain for new GL entry |
| `tr_invoices_after_status_change` | `tbl_invoices` | `AFTER UPDATE` | `UPDATE` | Submit to EFRIS async queue when status changes to `issued` |
| `tr_agent_stock_after_update` | `tbl_agent_stock_balance` | `AFTER UPDATE` | `UPDATE` | Check float limit; raise error if exceeded |
| `tr_payroll_runs_prevent_update` | `tbl_payroll_runs` | `BEFORE UPDATE` | `UPDATE` | Block any modification to a locked payroll run (BR-010) |
| `tr_audit_log_insert` | All financial tables | `AFTER INSERT/UPDATE` | `INSERT`, `UPDATE` | Write actor, IP, old values, new values to `tbl_audit_log` |

## 2.9 GL Hash Chain Table Structure

The `tbl_gl_entries` table includes these additional columns to support BR-013:

```sql
CREATE TABLE tbl_gl_entries (
    id              INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    journal_entry_id INT UNSIGNED NOT NULL,
    account_id      INT UNSIGNED NOT NULL,
    debit           DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    credit          DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    transaction_date DATE NOT NULL,
    narration       VARCHAR(500) NOT NULL,
    prev_hash       CHAR(64) NOT NULL,   -- SHA-256 hash of previous entry in this account
    hash_value      CHAR(64) NOT NULL,   -- SHA-256 hash of this entry's content + prev_hash
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by      INT UNSIGNED NOT NULL,
    updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by      INT UNSIGNED NOT NULL,
    CONSTRAINT fk_gl_entries_journal FOREIGN KEY (journal_entry_id) REFERENCES tbl_journal_entries (id),
    CONSTRAINT fk_gl_entries_account FOREIGN KEY (account_id) REFERENCES tbl_chart_of_accounts (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

The `tr_gl_entries_after_insert` trigger calculates `hash_value` as `SHA2(CONCAT(id, account_id, debit, credit, transaction_date, narration, prev_hash), 256)` and sets `prev_hash` from the last entry in the same account.

## Section 6 — Finance & General Ledger Tables

---

### tbl_accounts

**Purpose:** Chart of accounts — 1,307 accounts configured. Supports dual-mode accounting (DC-004): PIBID parliamentary budget votes and BIRDC IFRS commercial accounts coexist in the same table, distinguished by `accounting_mode`. The `parliamentary_segment` column carries the vote code for parliamentary accounts.

**Note:** `[CONTEXT-GAP: GAP-012]` — confirm whether BIRDC holds an existing Chart of Accounts or if this needs to be designed from scratch before database seeding.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `account_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Account primary key |
| `account_code` | `VARCHAR(20)` | NOT NULL, UNIQUE | Chart of accounts code |
| `account_name` | `VARCHAR(255)` | NOT NULL | Account name |
| `parent_account_id` | `INT UNSIGNED` | NULL, FK → tbl_accounts (self) | Parent account for hierarchy |
| `account_type` | `ENUM('asset','liability','equity','revenue','expense')` | NOT NULL | Account type |
| `account_subtype` | `VARCHAR(50)` | NULL | Subtype (e.g., `current_asset`, `fixed_asset`, `operating_expense`) |
| `accounting_mode` | `ENUM('commercial','parliamentary','both')` | NOT NULL DEFAULT 'commercial' | Which mode this account applies to |
| `parliamentary_segment` | `VARCHAR(30)` | NULL | PIBID parliamentary vote code (populated for parliamentary accounts) — DC-004 |
| `normal_balance` | `ENUM('debit','credit')` | NOT NULL | Normal balance side |
| `is_control_account` | `TINYINT(1)` | NOT NULL DEFAULT 0 | 1 = control account (no direct posting) |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `gl_level` | `TINYINT UNSIGNED` | NOT NULL DEFAULT 1 | Hierarchy level |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(account_code)`, `INDEX(parent_account_id)`, `INDEX(account_type)`, `INDEX(accounting_mode)`

```sql
CREATE TABLE tbl_accounts (
  account_id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
  account_code        VARCHAR(20)  NOT NULL,
  account_name        VARCHAR(255) NOT NULL,
  parent_account_id   INT UNSIGNED NULL,
  account_type        ENUM('asset','liability','equity','revenue','expense') NOT NULL,
  account_subtype     VARCHAR(50)  NULL,
  accounting_mode     ENUM('commercial','parliamentary','both') NOT NULL DEFAULT 'commercial',
  parliamentary_segment VARCHAR(30) NULL,
  normal_balance      ENUM('debit','credit') NOT NULL,
  is_control_account  TINYINT(1)   NOT NULL DEFAULT 0,
  is_active           TINYINT(1)   NOT NULL DEFAULT 1,
  gl_level            TINYINT UNSIGNED NOT NULL DEFAULT 1,
  created_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (account_id),
  UNIQUE KEY uq_accounts_code (account_code),
  KEY idx_accounts_parent (parent_account_id),
  KEY idx_accounts_type (account_type),
  KEY idx_accounts_mode (accounting_mode),
  CONSTRAINT fk_accounts_parent FOREIGN KEY (parent_account_id) REFERENCES tbl_accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_journals

**Purpose:** General Ledger journal header. Every financial transaction in the system (invoice, payment, stock adjustment, payroll, production) creates a journal entry here. Hash chain integrity per BR-013 is maintained via `hash_prev` and `hash_self`.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `journal_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Journal primary key |
| `journal_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Sequential JE number (JE-YYYY-NNNN) — BR-009 |
| `journal_date` | `DATE` | NOT NULL | Posting date |
| `description` | `TEXT` | NOT NULL | Journal description |
| `journal_type` | `ENUM('auto','manual','adjustment','opening_balance')` | NOT NULL DEFAULT 'auto' | Source type |
| `accounting_mode` | `ENUM('commercial','parliamentary','both')` | NOT NULL | Mode this entry belongs to |
| `source_type` | `VARCHAR(50)` | NULL | Source document type (e.g., `invoice`, `pos_transaction`, `payroll_run`) |
| `source_id` | `INT UNSIGNED` | NULL | Source document primary key |
| `period_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_accounting_periods | Accounting period |
| `status` | `ENUM('draft','approved','posted','reversed')` | NOT NULL DEFAULT 'draft' | Journal status |
| `total_debit` | `DECIMAL(18,4)` | NOT NULL | Sum of all debit lines |
| `total_credit` | `DECIMAL(18,4)` | NOT NULL | Sum of all credit lines (must equal total_debit) |
| `hash_self` | `CHAR(64)` | NULL | SHA-256 hash of this entry's content (BR-013) |
| `hash_prev` | `CHAR(64)` | NULL | SHA-256 hash of the previous journal entry in sequence (BR-013) |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Creator |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Approver (≠ creator — BR-003) |
| `approved_at` | `DATETIME` | NULL | Approval timestamp |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(journal_number)`, `INDEX(journal_date)`, `INDEX(status)`, `INDEX(source_type, source_id)`, `INDEX(period_id)`

```sql
-- BR-013: hash_prev stores SHA-256 of the previous journal in sequence.
-- hash_self stores SHA-256 of this entry's own data.
-- Both are set by application on INSERT. Neither column is ever updated.
CREATE TABLE tbl_journals (
  journal_id      INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  journal_number  VARCHAR(20)   NOT NULL,
  journal_date    DATE          NOT NULL,
  description     TEXT          NOT NULL,
  journal_type    ENUM('auto','manual','adjustment','opening_balance') NOT NULL DEFAULT 'auto',
  accounting_mode ENUM('commercial','parliamentary','both') NOT NULL,
  source_type     VARCHAR(50)   NULL,
  source_id       INT UNSIGNED  NULL,
  period_id       INT UNSIGNED  NOT NULL,
  status          ENUM('draft','approved','posted','reversed') NOT NULL DEFAULT 'draft',
  total_debit     DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  total_credit    DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  hash_self       CHAR(64)      NULL COMMENT 'SHA-256 of this entrys content — BR-013',
  hash_prev       CHAR(64)      NULL COMMENT 'SHA-256 of previous journal entry — BR-013 chain',
  created_by      INT UNSIGNED  NOT NULL,
  approved_by     INT UNSIGNED  NULL,
  approved_at     DATETIME      NULL,
  created_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (journal_id),
  UNIQUE KEY uq_journals_number (journal_number),
  KEY idx_journals_date (journal_date),
  KEY idx_journals_status (status),
  KEY idx_journals_source (source_type, source_id),
  KEY idx_journals_period (period_id),
  CONSTRAINT fk_journals_created_by  FOREIGN KEY (created_by)  REFERENCES tbl_users (user_id),
  CONSTRAINT fk_journals_approved_by FOREIGN KEY (approved_by) REFERENCES tbl_users (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_journal_lines

**Purpose:** Individual debit and credit lines within a journal entry. Sum of debits must equal sum of credits per journal (validated at application layer before posting).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `line_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line primary key |
| `journal_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_journals | Parent journal |
| `account_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_accounts | GL account |
| `debit` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Debit amount |
| `credit` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Credit amount |
| `description` | `VARCHAR(255)` | NULL | Line description |
| `cost_centre_id` | `INT UNSIGNED` | NULL, FK → tbl_cost_centres | Cost centre (optional) |

**Indexes:** `INDEX(journal_id)`, `INDEX(account_id)`

---

### tbl_accounting_periods

**Purpose:** Defines open and closed accounting periods for both fiscal year models — PIBID July–June and BIRDC January–December.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `period_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Period primary key |
| `period_name` | `VARCHAR(50)` | NOT NULL | Period name (e.g., `FY2026-Q1`, `JAN-2026`) |
| `period_start` | `DATE` | NOT NULL | Period start date |
| `period_end` | `DATE` | NOT NULL | Period end date |
| `fiscal_year` | `VARCHAR(10)` | NOT NULL | Fiscal year label |
| `accounting_mode` | `ENUM('commercial','parliamentary','both')` | NOT NULL | Which mode |
| `status` | `ENUM('open','closed','locked')` | NOT NULL DEFAULT 'open' | Period status |
| `closed_by` | `INT UNSIGNED` | NULL, FK → tbl_users | User who closed |
| `closed_at` | `DATETIME` | NULL | Close timestamp |

---

### tbl_budgets

**Purpose:** Budget headers — one per department/vote per period per mode.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `budget_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Budget primary key |
| `budget_name` | `VARCHAR(100)` | NOT NULL | Budget name |
| `accounting_mode` | `ENUM('commercial','parliamentary')` | NOT NULL | Mode |
| `period_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_accounting_periods | Applicable period |
| `department_id` | `INT UNSIGNED` | NULL, FK → tbl_departments | Department (commercial mode) |
| `parliamentary_vote_code` | `VARCHAR(30)` | NULL | Vote code (parliamentary mode) |
| `total_budget` | `DECIMAL(18,4)` | NOT NULL | Total approved budget (UGX) |
| `status` | `ENUM('draft','approved','locked')` | NOT NULL DEFAULT 'draft' | Approval status |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Approver |

---

### tbl_budget_lines

**Purpose:** Budget line items — one row per account per budget.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `line_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line primary key |
| `budget_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_budgets | Parent budget |
| `account_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_accounts | GL account |
| `budgeted_amount` | `DECIMAL(18,4)` | NOT NULL | Amount budgeted for this account |
| `alert_threshold_pct` | `TINYINT UNSIGNED` | NOT NULL DEFAULT 80 | Alert when actual reaches this % — BR-014 |

---

### tbl_bank_accounts

**Purpose:** BIRDC's bank accounts and imprest (petty cash) accounts.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `bank_account_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Bank account primary key |
| `account_name` | `VARCHAR(100)` | NOT NULL | Account name |
| `bank_name` | `VARCHAR(100)` | NULL | Bank name |
| `account_number` | `VARCHAR(30)` | NULL | Bank account number |
| `account_type` | `ENUM('current','savings','imprest')` | NOT NULL | Account type |
| `currency` | `CHAR(3)` | NOT NULL DEFAULT 'UGX' | Currency |
| `gl_account_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_accounts | Linked GL account |
| `current_balance` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Current system balance |
| `last_reconciled_date` | `DATE` | NULL | Last bank reconciliation date |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

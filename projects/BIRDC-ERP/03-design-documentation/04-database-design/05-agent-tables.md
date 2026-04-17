## Section 5 — Agent Management Tables

---

### tbl_agents

**Purpose:** Master record for all 1,071 BIRDC field sales agents. Each agent has a linked user account (`tbl_users.agent_id`) and a virtual inventory store tracked in `tbl_agent_stock_balance`.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `agent_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Agent primary key |
| `agent_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Agent code (e.g., AGT-00001) |
| `user_id` | `INT UNSIGNED` | NOT NULL, UNIQUE, FK → tbl_users | Linked user account |
| `full_name` | `VARCHAR(255)` | NOT NULL | Agent full name |
| `phone` | `VARCHAR(30)` | NOT NULL | Primary phone number |
| `mobile_money_number` | `VARCHAR(30)` | NULL | MTN MoMo or Airtel Money number for commission disbursement |
| `mobile_money_provider` | `ENUM('mtn_momo','airtel_money')` | NULL | Mobile money provider |
| `territory_id` | `INT UNSIGNED` | NULL, FK → tbl_territories | Assigned territory |
| `float_limit` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Maximum stock value agent may hold (UGX) — BR-006 |
| `commission_rate` | `DECIMAL(5,2)` | NOT NULL DEFAULT 0.00 | Commission percentage |
| `status` | `ENUM('active','suspended','inactive')` | NOT NULL DEFAULT 'active' | Agent status |
| `notes` | `TEXT` | NULL | Administrative notes |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

**Relationships:** One-to-one with `tbl_users`. One-to-many with `tbl_agent_remittances`, `tbl_agent_commissions`, `tbl_agent_stock_balance`.

**Indexes:** `UNIQUE(agent_number)`, `UNIQUE(user_id)`, `INDEX(territory_id)`, `INDEX(status)`

```sql
CREATE TABLE tbl_agents (
  agent_id              INT UNSIGNED NOT NULL AUTO_INCREMENT,
  agent_number          VARCHAR(20)  NOT NULL,
  user_id               INT UNSIGNED NOT NULL,
  full_name             VARCHAR(255) NOT NULL,
  phone                 VARCHAR(30)  NOT NULL,
  mobile_money_number   VARCHAR(30)  NULL,
  mobile_money_provider ENUM('mtn_momo','airtel_money') NULL,
  territory_id          INT UNSIGNED NULL,
  float_limit           DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  commission_rate       DECIMAL(5,2) NOT NULL DEFAULT 0.00,
  status                ENUM('active','suspended','inactive') NOT NULL DEFAULT 'active',
  notes                 TEXT         NULL,
  created_at            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (agent_id),
  UNIQUE KEY uq_agents_number (agent_number),
  UNIQUE KEY uq_agents_user (user_id),
  KEY idx_agents_territory (territory_id),
  KEY idx_agents_status (status),
  CONSTRAINT fk_agents_user      FOREIGN KEY (user_id)      REFERENCES tbl_users (user_id),
  CONSTRAINT fk_agents_territory FOREIGN KEY (territory_id) REFERENCES tbl_territories (territory_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_agent_remittances

**Purpose:** Records every cash remittance submitted by an agent. FIFO allocation to outstanding invoices is performed by stored procedure `sp_apply_remittance_to_invoices` on verification (BR-002). Segregation of duties (BR-003): the creator and verifier must be different users.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `remittance_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Remittance primary key |
| `remittance_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Reference number (REM-YYYY-NNNN) |
| `agent_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_agents | Agent who remitted |
| `remittance_date` | `DATE` | NOT NULL | Date cash deposited or transferred |
| `amount` | `DECIMAL(18,4)` | NOT NULL | Amount remitted (UGX) |
| `payment_method` | `ENUM('cash_deposit','mtn_momo','airtel_money','bank_transfer')` | NOT NULL | Payment method |
| `reference` | `VARCHAR(100)` | NULL | Bank or mobile money reference |
| `deposit_slip_url` | `VARCHAR(500)` | NULL | Scanned deposit slip URL |
| `status` | `ENUM('pending_verification','verified','rejected')` | NOT NULL DEFAULT 'pending_verification' | Verification status |
| `amount_allocated` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Amount allocated to invoices so far |
| `amount_unallocated` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Unallocated balance |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Agent submitter |
| `verified_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Supervisor who verified (≠ created_by) |
| `verified_at` | `DATETIME` | NULL | Verification timestamp |
| `gl_journal_id` | `INT UNSIGNED` | NULL, FK → tbl_journals | AR receipt GL journal |
| `notes` | `TEXT` | NULL | |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(remittance_number)`, `INDEX(agent_id)`, `INDEX(status)`, `INDEX(remittance_date)`

---

### tbl_agent_commissions

**Purpose:** Commission accrual records. Commission accrues only on verified remittances per BR-015. One record per remittance-to-invoice allocation.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `commission_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Commission primary key |
| `agent_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_agents | Agent |
| `remittance_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_agent_remittances | Verified remittance that triggered this commission |
| `invoice_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_invoices | Invoice cleared by the remittance |
| `invoiced_amount` | `DECIMAL(18,4)` | NOT NULL | Invoice value cleared |
| `commission_rate` | `DECIMAL(5,2)` | NOT NULL | Rate at time of accrual |
| `commission_amount` | `DECIMAL(18,4)` | NOT NULL | Earned commission (invoiced_amount × rate / 100) |
| `status` | `ENUM('accrued','paid')` | NOT NULL DEFAULT 'accrued' | Payment status |
| `paid_at` | `DATETIME` | NULL | When commission was disbursed |
| `payment_reference` | `VARCHAR(100)` | NULL | Mobile money payment reference |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_agent_territories

**Purpose:** Maps agents to territories. Supports one agent serving multiple territories or multiple agents in one territory.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `at_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Junction primary key |
| `agent_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_agents | Agent |
| `territory_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_territories | Territory |
| `is_primary` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Primary territory flag |
| `assigned_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | Assignment date |

**Unique constraint:** `UNIQUE(agent_id, territory_id)`

---

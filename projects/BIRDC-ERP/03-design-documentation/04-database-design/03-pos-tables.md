## Section 3 — POS Tables

---

### tbl_pos_sessions

**Purpose:** Records each POS session — open, active, and closed. A session is tied to a specific location and operator (agent or cashier).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `session_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Session primary key |
| `session_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Sequential session reference (POS-YYYY-NNNN) |
| `user_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Operator (agent or cashier) |
| `agent_id` | `INT UNSIGNED` | NULL, FK → tbl_agents | Agent (if operator is an agent) |
| `location_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_locations | POS location |
| `device_id` | `VARCHAR(255)` | NOT NULL | Android device identifier |
| `opening_float` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Cash float at session open (UGX) |
| `closing_cash` | `DECIMAL(18,4)` | NULL | Declared cash at session close |
| `expected_cash` | `DECIMAL(18,4)` | NULL | Calculated expected cash (float + cash sales) |
| `variance` | `DECIMAL(18,4)` | NULL | closing_cash - expected_cash |
| `total_revenue` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Total sales value in session |
| `transaction_count` | `INT UNSIGNED` | NOT NULL DEFAULT 0 | Number of transactions |
| `status` | `ENUM('open','closed')` | NOT NULL DEFAULT 'open' | Session status |
| `opened_at` | `DATETIME` | NOT NULL | Session open time (device timestamp) |
| `closed_at` | `DATETIME` | NULL | Session close time |
| `notes` | `TEXT` | NULL | Supervisor notes on variance |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(session_number)`, `INDEX(user_id)`, `INDEX(status)`, `INDEX(opened_at)`

```sql
CREATE TABLE tbl_pos_sessions (
  session_id      INT UNSIGNED NOT NULL AUTO_INCREMENT,
  session_number  VARCHAR(20)  NOT NULL,
  user_id         INT UNSIGNED NOT NULL,
  agent_id        INT UNSIGNED NULL,
  location_id     INT UNSIGNED NOT NULL,
  device_id       VARCHAR(255) NOT NULL,
  opening_float   DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  closing_cash    DECIMAL(18,4) NULL,
  expected_cash   DECIMAL(18,4) NULL,
  variance        DECIMAL(18,4) NULL,
  total_revenue   DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  transaction_count INT UNSIGNED NOT NULL DEFAULT 0,
  status          ENUM('open','closed') NOT NULL DEFAULT 'open',
  opened_at       DATETIME     NOT NULL,
  closed_at       DATETIME     NULL,
  notes           TEXT         NULL,
  created_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  UNIQUE KEY uq_sessions_number (session_number),
  KEY idx_pos_sessions_user (user_id),
  KEY idx_pos_sessions_status (status),
  CONSTRAINT fk_pos_sessions_user FOREIGN KEY (user_id) REFERENCES tbl_users (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_pos_transactions

**Purpose:** Records each completed POS sale (or void). `local_transaction_id` prevents duplicate sync inserts from offline agents.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `transaction_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Transaction primary key |
| `session_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_pos_sessions | Parent session |
| `transaction_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Sequential receipt number (RCP-YYYY-NNNN) |
| `local_transaction_id` | `VARCHAR(36)` | NOT NULL, UNIQUE | UUID from device — idempotency key |
| `customer_id` | `INT UNSIGNED` | NULL, FK → tbl_customers | Customer (if known) |
| `transaction_time` | `DATETIME` | NOT NULL | Device-recorded sale time |
| `total_amount` | `DECIMAL(18,4)` | NOT NULL | Sale total (UGX) |
| `amount_tendered` | `DECIMAL(18,4)` | NOT NULL | Total amount received |
| `change_due` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Change returned |
| `status` | `ENUM('completed','void')` | NOT NULL DEFAULT 'completed' | Transaction status |
| `void_reason` | `TEXT` | NULL | Void justification |
| `voided_by` | `INT UNSIGNED` | NULL, FK → tbl_users | User who voided |
| `fdn` | `VARCHAR(100)` | NULL | EFRIS Fiscal Document Number |
| `qr_code_url` | `VARCHAR(500)` | NULL | EFRIS QR code |
| `synced_at` | `DATETIME` | NULL | When offline transaction was synced to server |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(transaction_number)`, `UNIQUE(local_transaction_id)`, `INDEX(session_id)`, `INDEX(transaction_time)`

---

### tbl_pos_transaction_items

**Purpose:** Line items for each POS transaction — product, batch, quantity, and price.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `item_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line item primary key |
| `transaction_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_pos_transactions | Parent transaction |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product sold |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Batch (FEFO-selected, BR-007) |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Quantity sold |
| `unit_price` | `DECIMAL(18,4)` | NOT NULL | Unit price at time of sale |
| `subtotal` | `DECIMAL(18,4)` | NOT NULL | quantity × unit_price |
| `cogs_unit_cost` | `DECIMAL(18,4)` | NULL | FIFO cost for COGS |

---

### tbl_pos_payments

**Purpose:** Records each payment method used within a transaction. Supports multi-payment (cash + mobile money split).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `payment_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Payment primary key |
| `transaction_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_pos_transactions | Parent transaction |
| `method` | `ENUM('cash','mtn_momo','airtel_money','cheque','bank_deposit')` | NOT NULL | Payment method |
| `amount` | `DECIMAL(18,4)` | NOT NULL | Amount paid via this method |
| `reference` | `VARCHAR(100)` | NULL | Mobile money or bank reference |

---

### tbl_quick_keys

**Purpose:** Stores the configurable POS quick-key grid layout per agent. Each entry maps a grid position to a product for one-tap selling.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `quick_key_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Quick key primary key |
| `agent_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_agents | Agent this layout belongs to |
| `position` | `TINYINT UNSIGNED` | NOT NULL | Grid position (1-based) |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product on this key |
| `colour` | `CHAR(7)` | NULL DEFAULT '#4CAF50' | Button background colour (hex) |
| `updated_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | User who last configured |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

**Unique constraint:** `UNIQUE(agent_id, position)` — each position can only hold one product per agent.

---

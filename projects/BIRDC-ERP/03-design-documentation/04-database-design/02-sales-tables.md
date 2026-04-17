## Section 2 — Sales & Invoices Tables

---

### tbl_invoices

**Purpose:** Master record for all sales invoices. Lifecycle: `draft` → `pending_efris` → `issued` → `partially_paid` → `paid` → `void`. BR-009 (sequential numbering) is enforced by a database trigger on `INSERT`.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `invoice_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Invoice primary key |
| `invoice_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Sequential invoice number (INV-YYYY-NNNN) — assigned on confirm |
| `customer_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_customers | Customer |
| `territory_id` | `INT UNSIGNED` | NULL, FK → tbl_territories | Sales territory |
| `price_list_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_price_lists | Price list applied |
| `invoice_date` | `DATE` | NOT NULL | Invoice date |
| `due_date` | `DATE` | NOT NULL | Payment due date |
| `subtotal` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Pre-tax subtotal (UGX) |
| `vat_amount` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | VAT at 18% (UGX) |
| `total_amount` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Total including VAT |
| `amount_paid` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Amount received |
| `balance_due` | `DECIMAL(18,4)` | GENERATED ALWAYS AS (total_amount - amount_paid) STORED | Outstanding balance |
| `status` | `ENUM('draft','pending_efris','issued','partially_paid','paid','void')` | NOT NULL DEFAULT 'draft' | Invoice lifecycle status |
| `efris_submission_id` | `INT UNSIGNED` | NULL, FK → tbl_efris_queue | EFRIS queue reference |
| `fdn` | `VARCHAR(100)` | NULL | URA Fiscal Document Number |
| `qr_code_url` | `VARCHAR(500)` | NULL | EFRIS QR code URL |
| `gl_journal_id` | `INT UNSIGNED` | NULL, FK → tbl_journals | Auto-posted GL journal |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Invoice creator |
| `confirmed_by` | `INT UNSIGNED` | NULL, FK → tbl_users | User who confirmed (≠ creator — BR-003) |
| `confirmed_at` | `DATETIME` | NULL | Confirmation timestamp |
| `void_reason` | `TEXT` | NULL | Void justification |
| `voided_by` | `INT UNSIGNED` | NULL, FK → tbl_users | User who voided |
| `notes` | `TEXT` | NULL | Internal notes |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

**Relationships:** Many-to-one with `tbl_customers`, `tbl_territories`, `tbl_price_lists`. One-to-many with `tbl_invoice_items`.

**Indexes:** `UNIQUE(invoice_number)`, `INDEX(customer_id)`, `INDEX(status)`, `INDEX(invoice_date)`, `INDEX(territory_id)`

```sql
CREATE TABLE tbl_invoices (
  invoice_id        INT UNSIGNED NOT NULL AUTO_INCREMENT,
  invoice_number    VARCHAR(20)  NULL,
  customer_id       INT UNSIGNED NOT NULL,
  territory_id      INT UNSIGNED NULL,
  price_list_id     INT UNSIGNED NOT NULL,
  invoice_date      DATE         NOT NULL,
  due_date          DATE         NOT NULL,
  subtotal          DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  vat_amount        DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  total_amount      DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  amount_paid       DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  status            ENUM('draft','pending_efris','issued','partially_paid','paid','void')
                    NOT NULL DEFAULT 'draft',
  fdn               VARCHAR(100) NULL,
  qr_code_url       VARCHAR(500) NULL,
  gl_journal_id     INT UNSIGNED NULL,
  created_by        INT UNSIGNED NOT NULL,
  confirmed_by      INT UNSIGNED NULL,
  confirmed_at      DATETIME     NULL,
  void_reason       TEXT         NULL,
  voided_by         INT UNSIGNED NULL,
  notes             TEXT         NULL,
  created_at        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (invoice_id),
  UNIQUE KEY uq_invoices_number (invoice_number),
  KEY idx_invoices_customer (customer_id),
  KEY idx_invoices_status (status),
  KEY idx_invoices_date (invoice_date),
  KEY idx_invoices_territory (territory_id),
  CONSTRAINT fk_invoices_customer FOREIGN KEY (customer_id)
    REFERENCES tbl_customers (customer_id),
  CONSTRAINT fk_invoices_confirmed_by FOREIGN KEY (confirmed_by)
    REFERENCES tbl_users (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_invoice_items

**Purpose:** Line items for each invoice — product, quantity, unit price, and subtotal.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `item_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line item primary key |
| `invoice_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_invoices | Parent invoice |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Specific batch (set on confirmation) |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Quantity sold |
| `uom` | `VARCHAR(20)` | NOT NULL | Unit of measure |
| `unit_price` | `DECIMAL(18,4)` | NOT NULL | Unit price at time of sale |
| `subtotal` | `DECIMAL(18,4)` | NOT NULL | quantity × unit_price |
| `cogs_unit_cost` | `DECIMAL(18,4)` | NULL | FIFO cost used for COGS posting |

**Indexes:** `INDEX(invoice_id)`, `INDEX(stock_item_id)`

---

### tbl_price_lists

**Purpose:** Defines named price lists — wholesale, retail, export, institutional.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `price_list_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Price list primary key |
| `name` | `VARCHAR(100)` | NOT NULL | Price list name |
| `currency` | `CHAR(3)` | NOT NULL DEFAULT 'UGX' | ISO 4217 currency code |
| `effective_date` | `DATE` | NOT NULL | Date from which this list applies |
| `expiry_date` | `DATE` | NULL | Date list expires (NULL = no expiry) |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

### tbl_price_list_items

**Purpose:** Maps stock items to prices within a price list.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `pl_item_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Price list item primary key |
| `price_list_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_price_lists | Parent price list |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `uom` | `VARCHAR(20)` | NOT NULL | Unit of measure |
| `unit_price` | `DECIMAL(18,4)` | NOT NULL | Price per unit |

**Unique constraint:** `UNIQUE(price_list_id, stock_item_id, uom)`

---

### tbl_territories

**Purpose:** Defines sales territories for agent assignment and territory-based performance reporting.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `territory_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Territory primary key |
| `territory_name` | `VARCHAR(100)` | NOT NULL | Territory name |
| `region` | `VARCHAR(100)` | NULL | Geographic region |
| `manager_user_id` | `INT UNSIGNED` | NULL, FK → tbl_users | Assigned sales manager |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

### tbl_sales_targets

**Purpose:** Stores monthly/quarterly sales targets per territory and per agent for performance reporting.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `target_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Target primary key |
| `territory_id` | `INT UNSIGNED` | NULL, FK → tbl_territories | Territory (NULL if agent-specific) |
| `agent_id` | `INT UNSIGNED` | NULL, FK → tbl_agents | Agent (NULL if territory-level) |
| `period_year` | `SMALLINT UNSIGNED` | NOT NULL | Year |
| `period_month` | `TINYINT UNSIGNED` | NOT NULL | Month (1–12) |
| `target_amount` | `DECIMAL(18,4)` | NOT NULL | Sales target amount (UGX) |
| `set_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | User who set the target |

---

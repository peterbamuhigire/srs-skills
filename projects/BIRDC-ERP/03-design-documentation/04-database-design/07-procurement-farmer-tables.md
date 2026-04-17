## Section 7 — Procurement & Farmer Tables

---

### tbl_purchase_requests

**Purpose:** Purchase Request (PR) — initiates the procurement workflow. PPDA category is automatically determined from `estimated_value`.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `pr_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | PR primary key |
| `pr_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Sequential PR number (PR-YYYY-NNNN) |
| `title` | `VARCHAR(255)` | NOT NULL | Short description |
| `department_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_departments | Requesting department |
| `required_by_date` | `DATE` | NOT NULL | When goods are needed |
| `estimated_value` | `DECIMAL(18,4)` | NOT NULL | Estimated value (UGX) |
| `ppda_category` | `ENUM('micro','small','large','restricted')` | NOT NULL | PPDA procurement category — BR-005 |
| `justification` | `TEXT` | NOT NULL | Business justification |
| `status` | `ENUM('draft','pending_approval','approved','rejected','po_raised')` | NOT NULL DEFAULT 'draft' | PR status |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Requester |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Approver (role depends on PPDA category) |
| `approved_at` | `DATETIME` | NULL | Approval timestamp |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_purchase_orders

**Purpose:** Local Purchase Orders (LPO) — Uganda standard format. Linked to a PR and a vendor.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `po_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | PO primary key |
| `po_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | LPO number (LPO-YYYY-NNNN) |
| `pr_id` | `INT UNSIGNED` | NULL, FK → tbl_purchase_requests | Source PR |
| `vendor_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_vendors | Vendor |
| `po_date` | `DATE` | NOT NULL | PO issue date |
| `delivery_date` | `DATE` | NOT NULL | Expected delivery date |
| `total_amount` | `DECIMAL(18,4)` | NOT NULL | PO total (UGX) |
| `status` | `ENUM('draft','approved','issued','partially_received','received','closed','cancelled')` | NOT NULL DEFAULT 'draft' | PO status |
| `ppda_category` | `ENUM('micro','small','large','restricted')` | NOT NULL | PPDA category |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Creator |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Approver (BR-003, BR-005) |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_po_items

**Purpose:** Line items for purchase orders.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `item_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line item primary key |
| `po_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_purchase_orders | Parent PO |
| `stock_item_id` | `INT UNSIGNED` | NULL, FK → tbl_stock_items | Product (NULL for service items) |
| `description` | `VARCHAR(255)` | NOT NULL | Item description |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Ordered quantity |
| `uom` | `VARCHAR(20)` | NOT NULL | Unit of measure |
| `unit_price` | `DECIMAL(18,4)` | NOT NULL | Agreed unit price |
| `subtotal` | `DECIMAL(18,4)` | NOT NULL | quantity × unit_price |
| `quantity_received` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Quantity received to date |

---

### tbl_goods_receipts

**Purpose:** Goods Receipt Notes (GRN) — records delivery of goods against a PO. Part of the three-way match (PO → GRN → Invoice) per BR-012.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `grn_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | GRN primary key |
| `grn_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | GRN reference (GRN-YYYY-NNNN) |
| `po_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_purchase_orders | Source PO |
| `receipt_date` | `DATE` | NOT NULL | Receipt date |
| `location_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_locations | Receiving location |
| `received_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | User who received |
| `notes` | `TEXT` | NULL | Receipt notes |
| `gl_journal_id` | `INT UNSIGNED` | NULL, FK → tbl_journals | Auto-posted GL entry |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_grn_items

**Purpose:** Line items on a GRN.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `item_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Line primary key |
| `grn_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_goods_receipts | Parent GRN |
| `po_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_po_items | PO line matched |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `quantity_received` | `DECIMAL(18,4)` | NOT NULL | Quantity received |
| `unit_cost` | `DECIMAL(18,4)` | NOT NULL | Actual cost per unit |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Batch assigned on receipt |

---

### tbl_vendors

**Purpose:** Supplier and vendor master record.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `vendor_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Vendor primary key |
| `vendor_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Vendor code |
| `vendor_name` | `VARCHAR(255)` | NOT NULL | Supplier name |
| `tin` | `VARCHAR(20)` | NULL | Uganda Revenue Authority Tax Identification Number |
| `contact_name` | `VARCHAR(100)` | NULL | Primary contact |
| `phone` | `VARCHAR(30)` | NULL | Phone |
| `email` | `VARCHAR(255)` | NULL | Email |
| `address` | `TEXT` | NULL | Physical address |
| `payment_terms` | `VARCHAR(50)` | NULL | e.g., `Net 30` |
| `wht_applicable` | `TINYINT(1)` | NOT NULL DEFAULT 0 | Subject to 6% WHT per Uganda Income Tax Act |
| `performance_rating` | `TINYINT UNSIGNED` | NULL | 1–5 star rating |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_cooperative_batches

**Purpose:** Records a batch goods receipt from a cooperative — one batch per cooperative per season. Individual farmer contributions are broken down in `tbl_farmer_contributions` (BR-011).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `batch_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Batch primary key |
| `batch_number` | `VARCHAR(30)` | NOT NULL, UNIQUE | Cooperative batch reference |
| `cooperative_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_cooperatives | Source cooperative |
| `po_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_purchase_orders | Stage 1 bulk PO |
| `receipt_date` | `DATE` | NOT NULL | Factory gate receipt date |
| `total_weight_kg` | `DECIMAL(18,4)` | NOT NULL | Total weight received (kg) |
| `farmer_breakdown_status` | `ENUM('pending','complete')` | NOT NULL DEFAULT 'pending' | BR-011: must be complete before Stage 4 |
| `stock_receipt_id` | `INT UNSIGNED` | NULL, FK → tbl_goods_receipts | Stage 4 stock receipt GRN |
| `gl_journal_id` | `INT UNSIGNED` | NULL, FK → tbl_journals | Stage 5 GL posting |
| `status` | `ENUM('stage_1','stage_2','stage_3','stage_4','stage_5','closed')` | NOT NULL DEFAULT 'stage_1' | 5-stage workflow |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_farmer_contributions

**Purpose:** Individual farmer contribution within a cooperative batch. Every kilogramme must be allocated to a specific farmer with quality grade before the batch advances (BR-011).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `contribution_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Contribution primary key |
| `cooperative_batch_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_cooperative_batches | Parent batch |
| `farmer_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_farmers | Farmer |
| `delivery_date` | `DATETIME` | NOT NULL | Device-recorded delivery time |
| `weight_kg` | `DECIMAL(18,4)` | NOT NULL | Net weight (kg) |
| `quality_grade` | `CHAR(1)` | NOT NULL | `A`, `B`, or `C` |
| `unit_price` | `DECIMAL(18,4)` | NOT NULL | Price per kg for this grade |
| `gross_payable` | `DECIMAL(18,4)` | NOT NULL | weight_kg × unit_price |
| `total_deductions` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Loan repayments + cooperative levies |
| `net_payable` | `DECIMAL(18,4)` | NOT NULL | gross_payable - total_deductions |
| `payment_status` | `ENUM('pending','paid')` | NOT NULL DEFAULT 'pending' | Payment status |
| `local_delivery_id` | `VARCHAR(36)` | NULL, UNIQUE | Device UUID — idempotency key |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_farmers

**Purpose:** Registered farmers in BIRDC's cooperative network (6,440+).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `farmer_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Farmer primary key |
| `farmer_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Farmer registration number |
| `full_name` | `VARCHAR(255)` | NOT NULL | Full name |
| `nin` | `VARCHAR(20)` | NOT NULL, UNIQUE | Uganda National Identification Number |
| `phone` | `VARCHAR(30)` | NOT NULL | Phone |
| `mobile_money_number` | `VARCHAR(30)` | NULL | Bulk payment recipient |
| `mobile_money_provider` | `ENUM('mtn_momo','airtel_money')` | NULL | Provider |
| `cooperative_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_cooperatives | Primary cooperative |
| `photo_url` | `VARCHAR(500)` | NULL | Farmer photo |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_farms

**Purpose:** Farm profiles — multiple farms per farmer. GPS polygon and banana variety data stored here.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `farm_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Farm primary key |
| `farmer_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_farmers | Owner farmer |
| `farm_name` | `VARCHAR(100)` | NULL | Farm name or identifier |
| `gps_latitude` | `DECIMAL(10,7)` | NULL | GPS latitude |
| `gps_longitude` | `DECIMAL(10,7)` | NULL | GPS longitude |
| `area_acres` | `DECIMAL(10,4)` | NULL | Farm size (acres) |
| `banana_varieties` | `JSON` | NULL | Array of cultivar names |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_cooperatives

**Purpose:** Cooperative organisations that aggregate smallholder farmer deliveries.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `cooperative_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Cooperative primary key |
| `cooperative_name` | `VARCHAR(100)` | NOT NULL | Name |
| `zone` | `VARCHAR(50)` | NULL | Geographic zone |
| `contact_name` | `VARCHAR(100)` | NULL | Secretary or chairperson |
| `phone` | `VARCHAR(30)` | NULL | Phone |
| `farmer_count` | `INT UNSIGNED` | NOT NULL DEFAULT 0 | Registered farmer count (maintained by trigger) |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

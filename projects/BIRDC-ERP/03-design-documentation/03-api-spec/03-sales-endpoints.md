## Section 2 — Sales & Invoices Endpoints

These endpoints manage the order-to-cash cycle for Tooke products: invoice lifecycle, credit notes, EFRIS submission, and territory performance reporting.

---

### 2.1 GET /sales/invoices

**Description:** Retrieve a paginated list of sales invoices. Supports filtering by status, customer, date range, and territory.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `SALES_MANAGER`

**Query parameters:**

| Parameter | Type | Description |
|---|---|---|
| `status` | `string` | Filter by invoice status: `draft`, `pending_efris`, `issued`, `partially_paid`, `paid`, `void` |
| `customer_id` | `integer` | Filter by customer |
| `territory_id` | `integer` | Filter by sales territory |
| `date_from` | `string` | ISO 8601 date — invoice date range start |
| `date_to` | `string` | ISO 8601 date — invoice date range end |
| `page` | `integer` | Page number (default: 1) |
| `per_page` | `integer` | Records per page (default: 50, max: 200) |

**Response schema (200 OK):**

Each item in `data` array:

| Field | Type | Description |
|---|---|---|
| `invoice_id` | `integer` | Invoice primary key |
| `invoice_number` | `string` | Sequential invoice number (INV-YYYY-NNNN) |
| `customer_name` | `string` | Customer name |
| `invoice_date` | `string` | ISO 8601 date |
| `due_date` | `string` | ISO 8601 date |
| `total_amount` | `number` | Invoice total (UGX) |
| `amount_paid` | `number` | Amount received to date |
| `balance_due` | `number` | Outstanding balance |
| `status` | `string` | Invoice lifecycle status |
| `fdn` | `string\|null` | EFRIS Fiscal Document Number (null if not yet submitted) |

---

### 2.2 POST /sales/invoices

**Description:** Create a new sales invoice in `draft` status. Validates customer credit limit before creation.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `FINANCE_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `customer_id` | `integer` | Required | Customer primary key |
| `invoice_date` | `string` | Required, ISO 8601 date | Invoice date |
| `due_date` | `string` | Required, ISO 8601 date | Payment due date |
| `price_list_id` | `integer` | Required | Price list to apply (wholesale, retail, export, institutional) |
| `territory_id` | `integer` | Optional | Sales territory for reporting |
| `items` | `array` | Required, min 1 item | Array of invoice line items |
| `items[].stock_item_id` | `integer` | Required | Product being invoiced |
| `items[].quantity` | `number` | Required, > 0 | Quantity in base UOM |
| `items[].unit_price` | `number` | Required, > 0 | Unit price (UGX) |
| `notes` | `string` | Optional, max 500 | Internal notes |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `invoice_id` | `integer` | Newly created invoice ID |
| `invoice_number` | `string` | Assigned sequential invoice number |
| `status` | `string` | `"draft"` |
| `total_amount` | `number` | Calculated invoice total |

---

### 2.3 GET /sales/invoices/{invoice_id}

**Description:** Retrieve full detail of a single invoice, including line items, payment history, and EFRIS status.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `SALES_MANAGER`

**Path parameters:** `invoice_id` — integer, invoice primary key

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `invoice_id` | `integer` | Invoice primary key |
| `invoice_number` | `string` | Sequential invoice number |
| `customer` | `object` | Customer name, TIN, address |
| `items` | `array` | Line items with product, quantity, unit price, subtotal |
| `totals` | `object` | Subtotal, VAT (18%), total amount (UGX) |
| `status` | `string` | Invoice lifecycle status |
| `fdn` | `string\|null` | EFRIS Fiscal Document Number |
| `qr_code_url` | `string\|null` | URL to EFRIS QR code image |
| `payments` | `array` | Payment receipts applied to this invoice |
| `audit_trail` | `array` | Status change history with actor and timestamp |

---

### 2.4 PUT /sales/invoices/{invoice_id}

**Description:** Update a draft invoice. Only invoices in `draft` status may be edited.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `FINANCE_MANAGER`

**Request body:** Same structure as `POST /sales/invoices`. All fields optional — only supplied fields are updated.

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `invoice_id` | `integer` | Invoice primary key |
| `updated_at` | `string` | ISO 8601 datetime of update |

**Error conditions:** Returns `409 CONFLICT` if invoice status is not `draft`.

---

### 2.5 POST /sales/invoices/{invoice_id}/confirm

**Description:** Confirm a draft invoice — transitions status to `pending_efris`, triggers EFRIS submission to URA, auto-posts GL entries (DR Accounts Receivable / CR Revenue, DR COGS / CR Inventory), and reduces warehouse stock.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER`, `FINANCE_DIRECTOR`

**Request body:** None

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `invoice_id` | `integer` | Invoice primary key |
| `status` | `string` | `"issued"` (or `"pending_efris"` if EFRIS submission is queued) |
| `fdn` | `string\|null` | EFRIS FDN if submission was synchronous |
| `journal_entry_id` | `integer` | ID of the auto-posted GL journal entry |

**Business rules enforced:**

- BR-003 (segregation of duties): the confirming user must not be the invoice creator.
- BR-009 (sequential numbering): invoice number assigned at this step — gap detection runs automatically.
- Stock deducted from warehouse using FEFO batch selection (BR-007).

---

### 2.6 POST /sales/invoices/{invoice_id}/void

**Description:** Void an issued invoice. The invoice number is retained and marked `VOID` per BR-009. Auto-posts a reversal GL entry.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_DIRECTOR`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `void_reason` | `string` | Required, min 10 | Written justification for voiding |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `invoice_id` | `integer` | Invoice primary key |
| `status` | `string` | `"void"` |
| `reversal_journal_entry_id` | `integer` | ID of the GL reversal journal entry |

---

### 2.7 POST /sales/invoices/{invoice_id}/credit-note

**Description:** Create a credit note against an issued invoice. Reduces outstanding balance and posts a GL reversal.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER`, `FINANCE_DIRECTOR`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `reason` | `string` | Required, min 10 | Reason for the credit note |
| `items` | `array` | Required, min 1 | Line items being credited (subset or all of original invoice) |
| `items[].invoice_item_id` | `integer` | Required | Original invoice line item ID |
| `items[].quantity` | `number` | Required, > 0 | Quantity being credited |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `credit_note_id` | `integer` | Credit note primary key |
| `credit_note_number` | `string` | Sequential credit note number (CN-YYYY-NNNN) |
| `credit_amount` | `number` | Total credit amount (UGX) |
| `fdn` | `string\|null` | EFRIS FDN for the credit note |

---

### 2.8 GET /sales/invoices/overdue

**Description:** Retrieve all overdue invoices — due date passed and balance > 0. Used by AR aging reports.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `SALES_MANAGER`

**Query parameters:** `days_overdue` (integer, optional — filter by minimum days overdue), `customer_id` (integer, optional).

**Response schema (200 OK):** Paginated list with `invoice_number`, `customer_name`, `days_overdue`, `balance_due`.

---

### 2.9 POST /sales/payments

**Description:** Record a payment receipt against one or more invoices.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER`, `FINANCE_DIRECTOR`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `customer_id` | `integer` | Required | Customer making payment |
| `payment_date` | `string` | Required, ISO 8601 date | Date of payment |
| `amount` | `number` | Required, > 0 | Amount received (UGX) |
| `payment_method` | `string` | Required | `cash`, `mtn_momo`, `airtel_money`, `bank_transfer`, `cheque` |
| `reference` | `string` | Optional, max 100 | Bank reference or mobile money transaction ID |
| `invoice_ids` | `integer[]` | Required, min 1 | Invoices to allocate payment to (oldest first) |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `receipt_number` | `string` | Sequential receipt number (RCP-YYYY-NNNN) |
| `allocated_to` | `array` | List of invoice IDs and amounts allocated |
| `journal_entry_id` | `integer` | Auto-posted GL journal entry ID |

---

### 2.10 GET /sales/price-lists

**Description:** Retrieve all active price lists. Used by Sales Agent App for offline sync.

**Auth required:** JWT Bearer

**RBAC roles permitted:** All authenticated users

**Response schema (200 OK):** Array of price lists with `price_list_id`, `name`, `currency`, `effective_date`, `items[]` (product, unit price per UOM).

---

### 2.11 GET /sales/price-lists/{price_list_id}/items

**Description:** Retrieve all items in a specific price list with full product detail. Used by Sales Agent App offline sync.

**Auth required:** JWT Bearer

**RBAC roles permitted:** All authenticated users

**Response schema (200 OK):** Paginated list with `stock_item_id`, `item_code`, `item_name`, `uom`, `unit_price`.

---

### 2.12 GET /sales/territories/{territory_id}/performance

**Description:** Retrieve sales performance metrics for a territory — revenue, invoice count, top agents, month-on-month trend.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `SALES_MANAGER`

**Query parameters:** `period_from` (ISO 8601 date), `period_to` (ISO 8601 date).

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `territory_id` | `integer` | Territory primary key |
| `territory_name` | `string` | Territory name |
| `total_revenue` | `number` | Total invoiced amount (UGX) in period |
| `invoice_count` | `integer` | Number of issued invoices in period |
| `top_agents` | `array` | Top 5 agents by revenue in territory |
| `monthly_trend` | `array` | Monthly revenue data for charting |

---

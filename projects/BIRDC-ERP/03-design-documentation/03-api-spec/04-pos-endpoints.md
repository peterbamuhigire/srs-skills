## Section 3 — POS Endpoints

These endpoints serve the Sales Agent App's offline-capable POS. The agent device caches products, price lists, and agent stock locally (Room/SQLite). Transactions are recorded locally when offline and synced when connectivity is restored via Android `WorkManager`.

---

### 3.1 POST /pos/sessions/open

**Description:** Open a new POS session for a sales agent or cashier. Records the opening float amount and start time.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT`, `SALES_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `location_id` | `integer` | Required | POS location (factory gate, distribution centre, or agent's virtual store) |
| `opening_float` | `number` | Required, ≥ 0 | Cash float at session start (UGX) |
| `device_id` | `string` | Required | Android device identifier |
| `opened_at` | `string` | Required, ISO 8601 datetime | Device-recorded session start time (used for offline sessions) |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `session_id` | `integer` | POS session primary key |
| `session_number` | `string` | Sequential session number (POS-YYYY-NNNN) |
| `status` | `string` | `"open"` |
| `message` | `string` | Confirmation message |

**Error conditions:** Returns `409 CONFLICT` if the agent already has an open session on another device.

---

### 3.2 POST /pos/sessions/{session_id}/transactions

**Description:** Record a completed POS sale within an open session. For offline agents, this endpoint is called by WorkManager during sync — the `transaction_time` field carries the device timestamp.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT`, `SALES_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `transaction_time` | `string` | Required, ISO 8601 datetime | Device time of sale |
| `items` | `array` | Required, min 1 | Products sold |
| `items[].stock_item_id` | `integer` | Required | Product ID |
| `items[].quantity` | `number` | Required, > 0 | Quantity sold |
| `items[].unit_price` | `number` | Required, > 0 | Unit price at time of sale |
| `payments` | `array` | Required, min 1 | Payment methods used |
| `payments[].method` | `string` | Required | `cash`, `mtn_momo`, `airtel_money`, `cheque`, `bank_deposit` |
| `payments[].amount` | `number` | Required, > 0 | Amount tendered per method |
| `customer_id` | `integer` | Optional | Customer (if known) |
| `local_transaction_id` | `string` | Required | UUID generated on device — used for idempotency (prevents duplicate sync inserts) |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `transaction_id` | `integer` | Server transaction primary key |
| `transaction_number` | `string` | Sequential receipt number (RCP-YYYY-NNNN) |
| `total_amount` | `number` | Total sale amount (UGX) |
| `change_due` | `number` | Change due to customer |
| `fdn` | `string\|null` | EFRIS FDN (null if queued for async submission) |

**Business rules enforced:**

- Agent stock deducted from `tbl_agent_stock_balance` (NOT from `tbl_stock_balance`) per BR-001.
- FEFO batch selection enforced per BR-007.
- Stock float limit checked — sale blocked if agent would go below zero stock per BR-006.

---

### 3.3 POST /pos/sessions/{session_id}/close

**Description:** Close a POS session. Calculates expected cash (opening float + cash sales), compares to declared closing cash, and records any variance. Triggers end-of-shift reconciliation report.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT`, `SALES_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `closing_cash` | `number` | Required, ≥ 0 | Physical cash counted at close (UGX) |
| `closing_momo` | `number` | Optional | Mobile money balance at close (for reconciliation) |
| `closed_at` | `string` | Required, ISO 8601 datetime | Device-recorded session close time |
| `notes` | `string` | Optional, max 500 | Supervisor notes on variances |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `session_id` | `integer` | Session primary key |
| `status` | `string` | `"closed"` |
| `expected_cash` | `number` | Opening float + all cash sales (UGX) |
| `actual_cash` | `number` | Declared closing cash |
| `variance` | `number` | Difference (positive = surplus, negative = shortage) |
| `total_transactions` | `integer` | Count of transactions in session |
| `total_revenue` | `number` | Total sales value in session |

---

### 3.4 POST /pos/transactions/{transaction_id}/void

**Description:** Void a POS transaction within the current open session. A void reverses the stock deduction and creates a corresponding negative transaction record. Only the session owner or Sales Manager may void.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own session only), `SALES_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `void_reason` | `string` | Required, min 10 | Written justification |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `transaction_id` | `integer` | Original transaction ID |
| `void_transaction_id` | `integer` | Reversal transaction ID |
| `status` | `string` | `"void"` |

---

### 3.5 GET /pos/products

**Description:** Retrieve the product catalogue for offline sync. Returns all active products with stock quantities, prices, and barcode data. Used by Sales Agent App to populate Room cache before going offline.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT`, `WAREHOUSE_STAFF`, `SALES_MANAGER`

**Query parameters:**

| Parameter | Type | Description |
|---|---|---|
| `sync_token` | `string` | Optional — returns only records changed since last sync |
| `price_list_id` | `integer` | Required — price list to apply for this agent's context |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `products` | `array` | Product list |
| `products[].stock_item_id` | `integer` | Product primary key |
| `products[].item_code` | `string` | Product code |
| `products[].item_name` | `string` | Product name |
| `products[].barcode` | `string\|null` | EAN-13 or Code 128 barcode |
| `products[].uom` | `string` | Base unit of measure |
| `products[].unit_price` | `number` | Price from specified price list |
| `products[].agent_stock_qty` | `number\|null` | Agent's current stock quantity (if applicable) |
| `next_sync_token` | `string` | Token for next incremental sync |

---

### 3.6 GET /pos/quick-keys

**Description:** Retrieve the quick-key layout for the agent's POS screen — a grid of frequently sold products for one-tap selling without a search. Configurable per agent by the Sales Manager.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT`, `SALES_MANAGER`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `quick_keys` | `array` | Grid layout of quick keys |
| `quick_keys[].position` | `integer` | Grid position (1-based) |
| `quick_keys[].stock_item_id` | `integer` | Product ID |
| `quick_keys[].item_name` | `string` | Display name on button |
| `quick_keys[].unit_price` | `number` | Current price |
| `quick_keys[].colour` | `string` | Button background colour (hex) |

---

### 3.7 GET /pos/sessions

**Description:** Retrieve POS session history for the authenticated agent or all agents (Sales Manager view). Supports date range filtering.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own sessions only), `SALES_MANAGER`, `FINANCE_MANAGER`

**Query parameters:** `date_from`, `date_to`, `agent_id` (Sales Manager only), `status` (`open`, `closed`).

**Response schema (200 OK):** Paginated list with `session_number`, `agent_name`, `opened_at`, `closed_at`, `total_revenue`, `variance`.

---

### 3.8 GET /pos/sessions/{session_id}

**Description:** Retrieve full detail of a single POS session, including all transactions.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own sessions only), `SALES_MANAGER`, `FINANCE_MANAGER`

**Response schema (200 OK):** Full session object with `transactions[]` array.

---

### 3.9 PUT /pos/quick-keys

**Description:** Update the quick-key layout for a specific agent.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `IT_ADMIN`

**Request body:** `agent_id` (integer), `quick_keys[]` (array of position and stock_item_id pairs).

**Response schema (200 OK):** Updated quick-key layout.

---

### 3.10 GET /pos/sessions/{session_id}/receipt/{transaction_id}

**Description:** Generate and return a receipt for a specific POS transaction — used for reprinting or sending via WhatsApp/SMS.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_AGENT` (own transactions only), `SALES_MANAGER`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `receipt_number` | `string` | Receipt number |
| `receipt_html` | `string` | HTML receipt for 80mm thermal formatting |
| `fdn` | `string\|null` | EFRIS FDN |
| `qr_code_url` | `string\|null` | EFRIS QR code URL |

---

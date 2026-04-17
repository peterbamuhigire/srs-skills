## Section 7 — Procurement & Farmers Endpoints

These endpoints serve the Farmer Delivery App (offline-capable) and the web procurement module. Farmer registration, cooperative batch receipts, and the 5-stage procurement workflow are covered here.

---

### 7.1 POST /procurement/purchase-requests

**Description:** Create a Purchase Request (PR). The system automatically classifies the PR under the PPDA procurement category based on the estimated value and enforces the corresponding approval matrix (BR-005).

**Auth required:** JWT Bearer

**RBAC roles permitted:** All staff (creator), `DIRECTOR`/`FINANCE_MANAGER` (approver — based on PPDA category)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `title` | `string` | Required, max 255 | Short description of what is being purchased |
| `department_id` | `integer` | Required | Requesting department |
| `required_by_date` | `string` | Required, ISO 8601 date | When goods are needed |
| `estimated_value` | `number` | Required, > 0 | Estimated total value (UGX) — determines PPDA category |
| `items` | `array` | Required, min 1 | Items requested |
| `items[].description` | `string` | Required | Item description |
| `items[].quantity` | `number` | Required, > 0 | Quantity |
| `items[].uom` | `string` | Required | Unit of measure |
| `items[].estimated_unit_price` | `number` | Required | Estimated unit price (UGX) |
| `justification` | `string` | Required, min 20 | Business justification |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `pr_id` | `integer` | PR primary key |
| `pr_number` | `string` | Sequential PR number (PR-YYYY-NNNN) |
| `ppda_category` | `string` | Determined PPDA category (`micro`, `small`, `large`, `restricted`) |
| `required_approvers` | `array` | List of roles required to approve this PR |
| `status` | `string` | `"pending_approval"` |

**Note:** `[CONTEXT-GAP: GAP-007]` — exact PPDA UGX thresholds for BIRDC/PIBID category classification must be confirmed before this endpoint can enforce correct category boundaries.

---

### 7.2 GET /procurement/purchase-requests

**Description:** Retrieve the paginated list of Purchase Requests. Filterable by status, department, PPDA category, and date range.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PROCUREMENT_OFFICER`, `FINANCE_MANAGER`, `DIRECTOR`

**Query parameters:** `status`, `department_id`, `ppda_category`, `date_from`, `date_to`.

**Response schema (200 OK):** Paginated list with `pr_number`, `title`, `requested_by`, `department`, `estimated_value`, `ppda_category`, `status`.

---

### 7.3 POST /farmers

**Description:** Register a new farmer in the system. Supports offline creation via Farmer Delivery App — uses `local_farmer_id` for idempotent sync.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FIELD_OFFICER`, `PROCUREMENT_OFFICER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `local_farmer_id` | `string` | Required | UUID generated on device — idempotency key |
| `full_name` | `string` | Required, max 255 | Farmer full name |
| `nin` | `string` | Required, max 20 | Uganda National Identification Number |
| `phone` | `string` | Required, max 20 | Primary phone number |
| `mobile_money_number` | `string` | Optional, max 20 | MTN MoMo or Airtel Money number |
| `cooperative_id` | `integer` | Required | Cooperative the farmer belongs to |
| `gps_latitude` | `number` | Optional | GPS latitude of primary farm |
| `gps_longitude` | `number` | Optional | GPS longitude of primary farm |
| `photo_url` | `string` | Optional | Farmer photo URL (uploaded separately) |
| `banana_varieties` | `string[]` | Optional | Array of cultivar names grown |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `farmer_id` | `integer` | Server-assigned farmer primary key |
| `farmer_number` | `string` | Farmer registration number |
| `cooperative_name` | `string` | Cooperative name |

**Note:** `[CONTEXT-GAP: GAP-004]` — farmer data collection (GPS coordinates, NIN, photo, mobile money number) requires Uganda Data Protection and Privacy Act 2019 legal review before go-live.

---

### 7.4 POST /farmers/deliveries

**Description:** Record an individual farmer's matooke delivery at a cooperative collection point or factory gate. Used offline by Farmer Delivery App and synced on reconnect.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FIELD_OFFICER`, `PROCUREMENT_OFFICER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `local_delivery_id` | `string` | Required | UUID — idempotency key |
| `farmer_id` | `integer` | Required | Farmer primary key |
| `cooperative_batch_id` | `integer` | Required | The batch goods receipt this delivery belongs to |
| `delivery_date` | `string` | Required, ISO 8601 datetime | Device-recorded delivery time |
| `weight_kg` | `number` | Required, > 0 | Net weight in kilograms (from Bluetooth scale) |
| `quality_grade` | `string` | Required | `A`, `B`, or `C` |
| `unit_price` | `number` | Required, > 0 | Price per kg for this grade (UGX) |
| `deductions` | `array` | Optional | Loan repayments, cooperative levies |
| `deductions[].type` | `string` | Required | `loan_repayment`, `cooperative_levy` |
| `deductions[].amount` | `number` | Required, > 0 | Deduction amount (UGX) |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `delivery_id` | `integer` | Delivery primary key |
| `gross_payable` | `number` | weight_kg × unit_price |
| `total_deductions` | `number` | Sum of all deductions |
| `net_payable` | `number` | Amount the farmer will receive |
| `receipt_number` | `string` | Farmer receipt number (printed on-site) |

---

### 7.5 POST /farmers/payment-schedule

**Description:** Generate a farmer payment schedule for a cooperative batch — aggregating all individual contributions, applying deductions, and calculating net payments per farmer. Used to prepare the bulk MTN MoMo/Airtel Money payment file.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER`, `PROCUREMENT_OFFICER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `cooperative_batch_id` | `integer` | Required | Batch for which payments are being scheduled |
| `payment_date` | `string` | Required, ISO 8601 date | Scheduled payment date |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `schedule_id` | `integer` | Payment schedule primary key |
| `cooperative_name` | `string` | Cooperative name |
| `total_farmers` | `integer` | Number of farmers in schedule |
| `total_gross` | `number` | Total gross payable (UGX) |
| `total_deductions` | `number` | Total deductions (UGX) |
| `total_net_payable` | `number` | Total net payout (UGX) |
| `payment_lines` | `array` | Per-farmer: name, NIN, mobile_money_number, net_payable |

---

### 7.6 GET /cooperatives

**Description:** Retrieve the list of cooperatives with farmer count and batch history.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PROCUREMENT_OFFICER`, `FINANCE_MANAGER`, `FIELD_OFFICER`, `DIRECTOR`

**Query parameters:** `zone_id` (optional), `active_only` (boolean, default: `true`).

**Response schema (200 OK):** Paginated list with `cooperative_id`, `cooperative_name`, `zone`, `farmer_count`, `total_deliveries_kg`, `last_delivery_date`.

---

### 7.7 GET /farmers

**Description:** Retrieve the paginated list of registered farmers. Supports offline sync for the Farmer Delivery App.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FIELD_OFFICER`, `PROCUREMENT_OFFICER`, `FINANCE_MANAGER`

**Query parameters:** `cooperative_id`, `search` (name or NIN), `sync_token`.

**Response schema (200 OK):** Paginated or sync-delta farmer list with `farmer_id`, `farmer_number`, `full_name`, `nin`, `cooperative_name`, `phone`.

---

### 7.8 GET /farmers/{farmer_id}/contribution-history

**Description:** Retrieve the full delivery history for a specific farmer — weight, quality grades, prices, deductions, and net payments.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FIELD_OFFICER`, `PROCUREMENT_OFFICER`, `FINANCE_MANAGER`

**Query parameters:** `date_from`, `date_to`.

**Response schema (200 OK):** Paginated delivery list with `delivery_date`, `weight_kg`, `quality_grade`, `unit_price`, `gross_payable`, `deductions`, `net_payable`, `payment_status`.

---

### 7.9 GET /procurement/vendors

**Description:** Retrieve the vendor list with performance ratings and document status.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PROCUREMENT_OFFICER`, `FINANCE_MANAGER`

**Response schema (200 OK):** Paginated vendor list with `vendor_id`, `vendor_name`, `tin`, `contact`, `performance_rating`, `document_status` (all required PPDA documents uploaded or not).

---

### 7.10 POST /procurement/purchase-orders

**Description:** Create a Local Purchase Order (LPO) from an approved PR. Three-way matching is tracked from this point (BR-012).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PROCUREMENT_OFFICER` (creator), `FINANCE_MANAGER` / `DIRECTOR` (approver per PPDA category)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `pr_id` | `integer` | Required | Approved PR this PO fulfils |
| `vendor_id` | `integer` | Required | Selected vendor |
| `po_date` | `string` | Required, ISO 8601 date | PO issue date |
| `delivery_date` | `string` | Required, ISO 8601 date | Expected delivery date |
| `items` | `array` | Required, min 1 | Ordered items with confirmed unit prices |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `po_id` | `integer` | PO primary key |
| `po_number` | `string` | LPO number (LPO-YYYY-NNNN) |
| `status` | `string` | `"issued"` |

---

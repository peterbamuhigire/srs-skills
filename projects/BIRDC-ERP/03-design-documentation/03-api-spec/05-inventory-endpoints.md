## Section 4 — Inventory Endpoints

These endpoints serve the Warehouse App and other modules requiring stock visibility. Dual-track inventory separation (BR-001) is enforced at every endpoint: warehouse stock (`tbl_stock_balance`) and agent field stock (`tbl_agent_stock_balance`) are managed by entirely separate endpoints and never merged in responses except in explicitly consolidated reports.

---

### 4.1 GET /inventory/stock-on-hand

**Description:** Retrieve current warehouse stock balances across all locations. Agent stock is NEVER included in this response (BR-001).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `SALES_MANAGER`, `WAREHOUSE_STAFF`, `PRODUCTION_SUPERVISOR`

**Query parameters:**

| Parameter | Type | Description |
|---|---|---|
| `location_id` | `integer` | Filter by warehouse location |
| `stock_item_id` | `integer` | Filter by specific product |
| `low_stock` | `boolean` | If `true`, return only items below reorder level |
| `expiry_within_days` | `integer` | Return items expiring within N days |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `items` | `array` | Stock balance items |
| `items[].stock_item_id` | `integer` | Product primary key |
| `items[].item_code` | `string` | Product code |
| `items[].item_name` | `string` | Product name |
| `items[].location_name` | `string` | Warehouse location |
| `items[].quantity_on_hand` | `number` | Current quantity |
| `items[].uom` | `string` | Unit of measure |
| `items[].unit_cost` | `number` | Moving average or FIFO cost per unit |
| `items[].total_value` | `number` | quantity × unit_cost (UGX) |
| `items[].earliest_expiry` | `string\|null` | Earliest expiry date across batches |

---

### 4.2 GET /inventory/movements

**Description:** Retrieve stock movement history for audit and traceability. Every stock increase or decrease is logged here.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `WAREHOUSE_STAFF`, `PRODUCTION_SUPERVISOR`

**Query parameters:** `stock_item_id`, `movement_type` (`receipt`, `sale`, `transfer_in`, `transfer_out`, `adjustment`, `production_issue`, `production_receipt`, `agent_issuance`, `agent_return`), `date_from`, `date_to`, `location_id`.

**Response schema (200 OK):** Paginated list with `movement_id`, `movement_date`, `movement_type`, `reference_number`, `quantity`, `unit_cost`, `total_value`, `batch_number`, `location`, `created_by`.

---

### 4.3 POST /inventory/transfers

**Description:** Initiate a stock transfer between two warehouse locations. Transfer status begins as `in_transit` until the receiving location confirms receipt.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `WAREHOUSE_STAFF`, `SALES_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `from_location_id` | `integer` | Required | Source warehouse location |
| `to_location_id` | `integer` | Required | Destination warehouse location |
| `items` | `array` | Required, min 1 | Products to transfer |
| `items[].stock_item_id` | `integer` | Required | Product ID |
| `items[].batch_id` | `integer` | Required | Specific batch (FEFO enforced per BR-007) |
| `items[].quantity` | `number` | Required, > 0 | Quantity to transfer |
| `notes` | `string` | Optional, max 500 | Transfer notes |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `transfer_id` | `integer` | Transfer primary key |
| `transfer_number` | `string` | Sequential transfer number (TRN-YYYY-NNNN) |
| `status` | `string` | `"in_transit"` |

---

### 4.4 POST /inventory/transfers/{transfer_id}/confirm

**Description:** Confirm receipt of an in-transit stock transfer at the destination location. Moves stock from source to destination and creates movement records.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `WAREHOUSE_STAFF`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `received_items` | `array` | Required | Confirmed quantities per item |
| `received_items[].transfer_item_id` | `integer` | Required | Transfer line item ID |
| `received_items[].quantity_received` | `number` | Required, > 0 | Actual quantity received |
| `notes` | `string` | Optional | Notes on any discrepancy |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `transfer_id` | `integer` | Transfer primary key |
| `status` | `string` | `"completed"` or `"partial"` |
| `discrepancy` | `number` | Quantity difference if any |

---

### 4.5 POST /inventory/counts

**Description:** Initiate a physical stock count for one or more locations. Freezes stock movement for the count period at the specified location.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `WAREHOUSE_STAFF`, `FINANCE_MANAGER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `location_id` | `integer` | Required | Location to count |
| `count_date` | `string` | Required, ISO 8601 date | Scheduled count date |
| `count_type` | `string` | Required | `full` or `cycle` |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `count_id` | `integer` | Count session primary key |
| `count_number` | `string` | Count reference number |
| `status` | `string` | `"initiated"` |
| `items_to_count` | `integer` | Number of SKUs to count |

---

### 4.6 POST /inventory/counts/{count_id}/submit

**Description:** Submit physical count results. The system calculates variances against system balances and presents them for approval before any adjustment is posted.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `WAREHOUSE_STAFF`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `count_lines` | `array` | Required | Counted quantities per item/batch |
| `count_lines[].stock_item_id` | `integer` | Required | Product ID |
| `count_lines[].batch_id` | `integer` | Required | Batch counted |
| `count_lines[].quantity_counted` | `number` | Required, ≥ 0 | Physical count quantity |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `count_id` | `integer` | Count session primary key |
| `status` | `string` | `"pending_approval"` |
| `variances` | `array` | Items with variance (system qty vs counted qty) |
| `total_variance_value` | `number` | Total monetary variance (UGX) |

---

### 4.7 POST /inventory/adjustments

**Description:** Post a stock adjustment — increase or decrease — with a written reason. Auto-posts a GL entry (DR/CR Inventory with offsetting DR/CR Stock Adjustment Expense or Gain). Requires segregation of duties (BR-003): adjuster ≠ approver.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `FINANCE_MANAGER` (approver), `WAREHOUSE_STAFF` (creator)

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `stock_item_id` | `integer` | Required | Product to adjust |
| `location_id` | `integer` | Required | Warehouse location |
| `batch_id` | `integer` | Optional | Specific batch |
| `adjustment_type` | `string` | Required | `increase` or `decrease` |
| `quantity` | `number` | Required, > 0 | Adjustment quantity |
| `unit_cost` | `number` | Required | Cost per unit for GL posting |
| `reason` | `string` | Required, min 10 | Mandatory explanation |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `adjustment_id` | `integer` | Adjustment primary key |
| `journal_entry_id` | `integer` | Auto-posted GL journal entry |
| `status` | `string` | `"pending_approval"` |

---

### 4.8 POST /inventory/agent-issuance

**Description:** Issue stock from warehouse to an agent's virtual inventory store. Deducts from `tbl_stock_balance` and credits `tbl_agent_stock_balance`. Enforces agent float limit per BR-006.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `WAREHOUSE_STAFF`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `agent_id` | `integer` | Required | Receiving agent |
| `items` | `array` | Required, min 1 | Products to issue |
| `items[].stock_item_id` | `integer` | Required | Product ID |
| `items[].batch_id` | `integer` | Required | Batch (FEFO enforced) |
| `items[].quantity` | `number` | Required, > 0 | Quantity to issue |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `issuance_id` | `integer` | Issuance record primary key |
| `issuance_number` | `string` | Reference number |
| `agent_stock_value_after` | `number` | Agent's stock value after issuance (UGX) |
| `float_limit` | `number` | Agent's configured float limit |
| `float_utilisation_pct` | `number` | Percentage of float limit used |

**Error conditions:** Returns `422 BUSINESS_RULE_VIOLATION` with `BR-006` if the issuance would cause the agent's stock value to exceed their float limit.

---

### 4.9 POST /inventory/agent-returns

**Description:** Process the return of unsold stock from an agent to the warehouse. Credits `tbl_stock_balance` and debits `tbl_agent_stock_balance`.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `SALES_MANAGER`, `WAREHOUSE_STAFF`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `agent_id` | `integer` | Required | Returning agent |
| `items` | `array` | Required, min 1 | Products returned |
| `items[].stock_item_id` | `integer` | Required | Product ID |
| `items[].batch_id` | `integer` | Required | Batch number |
| `items[].quantity` | `number` | Required, > 0 | Quantity returned |
| `condition` | `string` | Required | `saleable` or `damaged` |
| `notes` | `string` | Optional | Condition notes |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `return_id` | `integer` | Return record primary key |
| `agent_stock_value_after` | `number` | Agent's stock value after return |

---

### 4.10 GET /inventory/batches

**Description:** Retrieve batch information for a product, including manufacture date, expiry date, and QC status. Used by Warehouse App for FEFO-compliant picking.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `WAREHOUSE_STAFF`, `PRODUCTION_SUPERVISOR`, `QC_OFFICER`, `SALES_MANAGER`

**Query parameters:** `stock_item_id` (required), `status` (`approved`, `pending`, `rejected`, `on_hold`), `expiry_before` (ISO 8601 date).

**Response schema (200 OK):** Array of batches with `batch_id`, `batch_number`, `manufacture_date`, `expiry_date`, `quantity_on_hand`, `qc_status`, `location_name`.

---

### 4.11 GET /inventory/consolidated

**Description:** Retrieve consolidated stock report showing warehouse stock and agent stock separately with a combined total. Warehouse and agent figures are labelled and NEVER merged into a single quantity (BR-001).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `DIRECTOR`, `FINANCE_DIRECTOR`, `FINANCE_MANAGER`, `SALES_MANAGER`

**Response schema (200 OK):** Per product: `warehouse_quantity`, `warehouse_value`, `agent_quantity`, `agent_value`, `total_quantity`, `total_value` — all fields clearly labelled.

---

### 4.12 GET /inventory/expiry-alerts

**Description:** Retrieve products with batches expiring within configured alert thresholds (30, 60, 90 days). Used by Executive Dashboard App for push notification generation.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `WAREHOUSE_STAFF`, `SALES_MANAGER`, `PRODUCTION_SUPERVISOR`

**Response schema (200 OK):** List with `item_name`, `batch_number`, `expiry_date`, `days_remaining`, `quantity_at_risk`, `location`.

---

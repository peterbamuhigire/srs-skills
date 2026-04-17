## Section 8 — Manufacturing & QC Endpoints

These endpoints serve the Factory Floor App. They cover production order management, QC inspection submission, Certificate of Analysis (CoA) generation, and circular economy mass balance verification (BR-008).

---

### 8.1 GET /manufacturing/production-orders

**Description:** Retrieve the paginated list of production orders. Factory Floor App uses this for real-time monitoring of active orders.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`, `QC_OFFICER`, `DIRECTOR`, `FINANCE_MANAGER`

**Query parameters:** `status` (`planned`, `materials_reserved`, `in_progress`, `qc_check`, `completed`, `closed`), `date_from`, `date_to`, `product_id`.

**Response schema (200 OK):** Paginated list with `order_id`, `order_number`, `product_name`, `planned_quantity`, `planned_start`, `planned_end`, `status`, `qc_status`.

---

### 8.2 GET /manufacturing/production-orders/{order_id}

**Description:** Retrieve full detail of a production order, including recipe, materials, job cards, actual yield, and QC status.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`, `QC_OFFICER`, `FINANCE_MANAGER`

**Path parameters:** `order_id` — integer

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `order_id` | `integer` | Production order primary key |
| `order_number` | `string` | Order reference (PO-YYYY-NNNN) |
| `recipe_id` | `integer` | Recipe (Bill of Materials) used |
| `recipe_name` | `string` | Recipe name |
| `planned_input_kg` | `number` | Planned raw material input (kg) |
| `planned_output_kg` | `number` | Planned primary product output (kg) |
| `planned_byproduct_kg` | `number` | Planned by-product output (kg — biogas, bio-slurry) |
| `planned_waste_kg` | `number` | Planned scrap/waste (kg) |
| `actual_input_kg` | `number\|null` | Recorded input (populated after completion) |
| `actual_output_kg` | `number\|null` | Recorded primary output |
| `actual_byproduct_kg` | `number\|null` | Recorded by-product output |
| `actual_waste_kg` | `number\|null` | Recorded waste |
| `mass_balance_status` | `string\|null` | `balanced`, `variance_within_tolerance`, `variance_exceeded` |
| `materials` | `array` | Material issuance lines |
| `job_cards` | `array` | Job card list with worker assignments and steps |
| `qc_status` | `string` | `pending`, `under_test`, `approved`, `rejected`, `on_hold` |
| `status` | `string` | Production order lifecycle status |

---

### 8.3 POST /manufacturing/production-orders/{order_id}/complete

**Description:** Record production completion — actual quantities for primary products, by-products, and waste. The system verifies the circular economy mass balance equation per BR-008. If variance exceeds ±2%, the order CANNOT be closed and a variance report is generated.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `actual_input_kg` | `number` | Required, > 0 | Total raw matooke input processed (kg) |
| `primary_outputs` | `array` | Required, min 1 | Primary products produced |
| `primary_outputs[].stock_item_id` | `integer` | Required | Product ID |
| `primary_outputs[].quantity_kg` | `number` | Required, > 0 | Quantity produced (kg) |
| `byproduct_outputs` | `array` | Optional | By-products (biogas m³, bio-slurry kg) |
| `byproduct_outputs[].byproduct_type` | `string` | Required | `biogas`, `bio_slurry`, `other` |
| `byproduct_outputs[].quantity` | `number` | Required | Quantity and unit |
| `byproduct_outputs[].unit` | `string` | Required | `kg` or `m3` |
| `waste_kg` | `number` | Required, ≥ 0 | Unrecoverable waste (kg) |
| `completion_date` | `string` | Required, ISO 8601 datetime | Actual completion time |
| `notes` | `string` | Optional | Production notes |

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `order_id` | `integer` | Production order primary key |
| `status` | `string` | `"qc_check"` (pending QC approval) |
| `mass_balance_status` | `string` | `balanced`, `variance_within_tolerance`, or `variance_exceeded` |
| `mass_balance_variance_pct` | `number` | Calculated variance percentage |
| `message` | `string` | Outcome message (error if variance exceeded) |

**Business rules enforced:** BR-008 — if `(primary_output + byproduct + waste) / actual_input` deviates by more than ±2%, the order status remains `in_progress` and a mass balance variance report is auto-generated.

---

### 8.4 POST /manufacturing/qc/inspections

**Description:** Submit a QC inspection for a production batch. The inspection uses a configurable template with numeric, pass/fail, text, and photo parameters. Determines batch QC status.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `QC_OFFICER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `production_order_id` | `integer` | Required | Production order being inspected |
| `batch_id` | `integer` | Required | Batch being tested |
| `inspection_template_id` | `integer` | Required | QC template (domestic, export-South Korea, export-EU, etc.) |
| `inspection_date` | `string` | Required, ISO 8601 datetime | Inspection date and time |
| `results` | `array` | Required | Test results per parameter |
| `results[].parameter_id` | `integer` | Required | Parameter ID from template |
| `results[].value_numeric` | `number` | Conditional | Result for numeric parameters |
| `results[].value_pass_fail` | `boolean` | Conditional | Result for pass/fail parameters |
| `results[].value_text` | `string` | Conditional | Result for text parameters |
| `results[].photo_url` | `string` | Conditional | Photo URL for photo parameters |
| `overall_disposition` | `string` | Required | `approved`, `approved_domestic_only`, `rejected`, `on_hold` |
| `notes` | `string` | Optional | Inspector notes |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `inspection_id` | `integer` | Inspection record primary key |
| `batch_qc_status` | `string` | Updated batch QC status |
| `production_order_status` | `string` | `"completed"` if approved, `"qc_check"` if still pending |
| `coa_available` | `boolean` | `true` if batch disposition is `approved` or `approved_domestic_only` |

**Business rules enforced:** BR-004 — stock transfer to saleable inventory is BLOCKED until batch QC status is `approved`. The stock transfer API returns `422 BUSINESS_RULE_VIOLATION` for any non-approved batch.

---

### 8.5 GET /manufacturing/qc/inspections/{batch_id}/coa

**Description:** Download the Certificate of Analysis (CoA) for an approved batch. Returns market-specific CoA for export batches per BR-017.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `QC_OFFICER`, `PRODUCTION_SUPERVISOR`, `SALES_MANAGER`, `DIRECTOR`

**Query parameters:** `market` (`domestic`, `south_korea`, `eu`, `saudi_arabia`, `qatar`, `usa`) — determines which market-specific parameters are included.

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `coa_id` | `integer` | CoA record primary key |
| `batch_number` | `string` | Batch number |
| `product_name` | `string` | Product name |
| `market` | `string` | Market the CoA is valid for |
| `issue_date` | `string` | CoA issue date |
| `pdf_url` | `string` | URL to downloadable CoA PDF (generated by mPDF) |
| `parameters` | `array` | Test results included in this CoA |

**Note:** `[CONTEXT-GAP: GAP-010]` — exact test parameters and pass/fail limits for South Korea, EU, Saudi Arabia, Qatar, and USA markets must be provided by the BIRDC QC Manager before export CoA templates can be finalised.

---

### 8.6 POST /manufacturing/qc/ncrs

**Description:** Raise a Non-Conformance Report (NCR) for a batch that has failed inspection or exhibited a quality deviation.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `QC_OFFICER`

**Request body:**

| Field | Type | Constraint | Description |
|---|---|---|---|
| `batch_id` | `integer` | Required | Batch with non-conformance |
| `ncr_type` | `string` | Required | `incoming_material`, `in_process`, `finished_product` |
| `description` | `string` | Required, min 20 | Non-conformance description |
| `root_cause` | `string` | Optional, min 10 | Root cause analysis |
| `corrective_action` | `string` | Optional | Corrective action plan |
| `responsible_person_id` | `integer` | Optional | Employee assigned to corrective action |
| `due_date` | `string` | Optional, ISO 8601 date | Corrective action due date |

**Response schema (201 Created):**

| Field | Type | Description |
|---|---|---|
| `ncr_id` | `integer` | NCR primary key |
| `ncr_number` | `string` | NCR reference (NCR-YYYY-NNNN) |
| `status` | `string` | `"open"` |

---

### 8.7 GET /manufacturing/production-orders/{order_id}/job-cards

**Description:** Retrieve job cards for a production order. Used by Factory Floor App to display step-by-step instructions for workers and record attendance.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`, `QC_OFFICER`

**Response schema (200 OK):** Array of job cards with `job_card_id`, `step_number`, `description`, `assigned_workers[]`, `status` (`pending`, `in_progress`, `completed`), `start_time`, `end_time`.

---

### 8.8 GET /manufacturing/recipes

**Description:** Retrieve the list of active recipes (Bills of Materials). Includes circular economy by-product outputs.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`, `FINANCE_MANAGER`, `QC_OFFICER`

**Response schema (200 OK):** Paginated recipe list with `recipe_id`, `recipe_name`, `product_name`, `version`, `input_uom`, `primary_yield_pct`, `by_products[]` (biogas, bio-slurry), `is_active`.

---

### 8.9 GET /manufacturing/equipment

**Description:** Retrieve the equipment list with calibration status and maintenance schedule.

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`, `IT_ADMIN`

**Response schema (200 OK):** Paginated list with `equipment_id`, `name`, `type`, `location`, `last_calibration_date`, `next_calibration_due`, `calibration_status` (`current`, `due_soon`, `overdue`).

---

### 8.10 GET /manufacturing/mass-balance-report/{order_id}

**Description:** Retrieve the mass balance calculation report for a production order — showing input, primary output, by-product output, waste, and variance percentage. Required review document when variance exceeds tolerance (BR-008).

**Auth required:** JWT Bearer

**RBAC roles permitted:** `PRODUCTION_SUPERVISOR`, `FINANCE_MANAGER`, `DIRECTOR`

**Response schema (200 OK):**

| Field | Type | Description |
|---|---|---|
| `order_number` | `string` | Production order reference |
| `actual_input_kg` | `number` | Total input (kg) |
| `primary_output_kg` | `number` | Primary product output (kg) |
| `byproduct_output_kg` | `number` | By-product output (kg equivalent) |
| `waste_kg` | `number` | Scrap and unrecoverable waste (kg) |
| `accounted_total_kg` | `number` | Sum of all outputs |
| `variance_kg` | `number` | input - accounted_total |
| `variance_pct` | `number` | (variance / input) × 100 |
| `tolerance_pct` | `number` | Configured tolerance (default: 2%) |
| `status` | `string` | `balanced`, `variance_within_tolerance`, or `variance_exceeded` |

---

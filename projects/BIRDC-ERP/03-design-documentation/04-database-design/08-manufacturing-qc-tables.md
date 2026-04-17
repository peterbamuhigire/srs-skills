## Section 8 — Manufacturing & QC Tables

---

### tbl_recipes

**Purpose:** Recipe (Bill of Materials) definitions. Circular economy recipes include by-product outputs (banana peel → biogas, waste water → bio-slurry). Version-controlled.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `recipe_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Recipe primary key |
| `recipe_name` | `VARCHAR(100)` | NOT NULL | Recipe name |
| `product_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Primary product produced |
| `version` | `TINYINT UNSIGNED` | NOT NULL DEFAULT 1 | Recipe version |
| `input_quantity` | `DECIMAL(18,4)` | NOT NULL | Standard input quantity |
| `input_uom` | `VARCHAR(20)` | NOT NULL | Input unit of measure (typically `kg`) |
| `expected_primary_yield_pct` | `DECIMAL(5,2)` | NOT NULL | Primary product yield % of input |
| `expected_byproduct_yield_pct` | `DECIMAL(5,2)` | NOT NULL DEFAULT 0 | By-product yield % |
| `expected_waste_pct` | `DECIMAL(5,2)` | NOT NULL DEFAULT 0 | Waste % |
| `mass_balance_tolerance_pct` | `DECIMAL(4,2)` | NOT NULL DEFAULT 2.00 | BR-008 tolerance (default: 2%) |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Note:** `expected_primary_yield_pct + expected_byproduct_yield_pct + expected_waste_pct` must sum to 100%.

---

### tbl_recipe_ingredients

**Purpose:** Raw material inputs for a recipe. Also includes circular economy by-product output specifications (marked with `ingredient_type = 'byproduct'`).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `ingredient_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Ingredient primary key |
| `recipe_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_recipes | Parent recipe |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Material or by-product |
| `ingredient_type` | `ENUM('input','primary_output','byproduct','waste')` | NOT NULL | Role in recipe |
| `quantity_per_batch` | `DECIMAL(18,4)` | NOT NULL | Quantity per batch |
| `uom` | `VARCHAR(20)` | NOT NULL | Unit of measure |
| `byproduct_description` | `VARCHAR(255)` | NULL | Description for by-products (e.g., "Biogas from banana peel — calorific value 5,500 kcal/m³") |
| `is_critical` | `TINYINT(1)` | NOT NULL DEFAULT 0 | 1 = this ingredient must be present for mass balance to close |

---

### tbl_production_orders

**Purpose:** Production order header — from plan to completed and closed. Mass balance is verified on completion (BR-008).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `order_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Production order primary key |
| `order_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | Order reference (PRD-YYYY-NNNN) |
| `recipe_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_recipes | Recipe used |
| `planned_quantity` | `DECIMAL(18,4)` | NOT NULL | Planned output quantity |
| `planned_start` | `DATETIME` | NOT NULL | Planned start |
| `planned_end` | `DATETIME` | NOT NULL | Planned end |
| `actual_start` | `DATETIME` | NULL | Actual start |
| `actual_end` | `DATETIME` | NULL | Actual end |
| `planned_input_kg` | `DECIMAL(18,4)` | NOT NULL | Planned raw input (kg) |
| `actual_input_kg` | `DECIMAL(18,4)` | NULL | Recorded actual input (kg) — set on completion |
| `mass_balance_status` | `ENUM('pending','balanced','variance_within_tolerance','variance_exceeded')` | NOT NULL DEFAULT 'pending' | BR-008 |
| `mass_balance_variance_pct` | `DECIMAL(6,3)` | NULL | Calculated variance % |
| `status` | `ENUM('planned','materials_reserved','in_progress','qc_check','completed','closed','cancelled')` | NOT NULL DEFAULT 'planned' | Order status |
| `qc_status` | `ENUM('not_required','pending','under_test','approved','approved_domestic_only','rejected')` | NOT NULL DEFAULT 'pending' | QC disposition — BR-004 |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(order_number)`, `INDEX(status)`, `INDEX(qc_status)`, `INDEX(planned_start)`

---

### tbl_production_completions

**Purpose:** Records actual production completion data — primary output quantities, by-product quantities, and waste.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `completion_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Completion primary key |
| `order_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_production_orders | Parent order |
| `output_type` | `ENUM('primary','byproduct','waste')` | NOT NULL | Output category |
| `stock_item_id` | `INT UNSIGNED` | NULL, FK → tbl_stock_items | Product (NULL for waste) |
| `byproduct_type` | `VARCHAR(50)` | NULL | e.g., `biogas`, `bio_slurry` (if output_type = byproduct) |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Quantity produced |
| `uom` | `VARCHAR(20)` | NOT NULL | Unit |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Batch created |
| `recorded_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | |
| `recorded_at` | `DATETIME` | NOT NULL | |

---

### tbl_job_cards

**Purpose:** Step-by-step work instructions within a production order. Workers scan their attendance against job cards on the Factory Floor App.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `job_card_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Job card primary key |
| `order_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_production_orders | Parent order |
| `step_number` | `TINYINT UNSIGNED` | NOT NULL | Sequential step |
| `description` | `TEXT` | NOT NULL | Step instructions |
| `assigned_workers` | `JSON` | NULL | Array of employee IDs assigned |
| `status` | `ENUM('pending','in_progress','completed')` | NOT NULL DEFAULT 'pending' | Step status |
| `started_at` | `DATETIME` | NULL | |
| `completed_at` | `DATETIME` | NULL | |

---

### tbl_inspections

**Purpose:** QC inspection header. Linked to a production batch and an inspection template.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `inspection_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Inspection primary key |
| `production_order_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_production_orders | Production order inspected |
| `batch_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_batches | Batch inspected |
| `template_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_inspection_templates | Inspection template |
| `inspection_date` | `DATETIME` | NOT NULL | Inspection date and time |
| `inspector_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | QC Officer |
| `overall_disposition` | `ENUM('approved','approved_domestic_only','rejected','on_hold')` | NOT NULL | Final QC decision — BR-004 |
| `notes` | `TEXT` | NULL | Inspector notes |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_inspection_results

**Purpose:** Individual test results within an inspection — one row per parameter.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `result_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Result primary key |
| `inspection_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_inspections | Parent inspection |
| `parameter_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_inspection_parameters | QC parameter |
| `value_numeric` | `DECIMAL(18,6)` | NULL | Result for numeric parameters |
| `value_pass_fail` | `TINYINT(1)` | NULL | Result for pass/fail parameters |
| `value_text` | `TEXT` | NULL | Result for text parameters |
| `photo_url` | `VARCHAR(500)` | NULL | Photo URL for photo parameters |
| `is_pass` | `TINYINT(1)` | NULL | Whether this parameter passed |

---

### tbl_certificates_of_analysis

**Purpose:** Certificate of Analysis issued for approved batches. Market-specific versions for export destinations (BR-017).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `coa_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | CoA primary key |
| `coa_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | CoA reference (COA-YYYY-NNNN) |
| `batch_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_batches | Batch certified |
| `inspection_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_inspections | Source inspection |
| `market` | `ENUM('domestic','south_korea','eu','saudi_arabia','qatar','usa')` | NOT NULL | Target market — BR-017 |
| `issue_date` | `DATE` | NOT NULL | Issue date |
| `issued_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | Issuing QC Officer |
| `pdf_url` | `VARCHAR(500)` | NULL | Generated CoA PDF URL |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_ncrs

**Purpose:** Non-Conformance Reports — raised when a quality failure is detected.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `ncr_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | NCR primary key |
| `ncr_number` | `VARCHAR(20)` | NOT NULL, UNIQUE | NCR reference (NCR-YYYY-NNNN) |
| `batch_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_batches | Affected batch |
| `ncr_type` | `ENUM('incoming_material','in_process','finished_product')` | NOT NULL | Type of non-conformance |
| `description` | `TEXT` | NOT NULL | Non-conformance description |
| `root_cause` | `TEXT` | NULL | Root cause analysis |
| `corrective_action` | `TEXT` | NULL | Corrective action plan |
| `responsible_person_id` | `INT UNSIGNED` | NULL, FK → tbl_employees | Responsible person |
| `due_date` | `DATE` | NULL | Corrective action due date |
| `status` | `ENUM('open','in_progress','closed','cancelled')` | NOT NULL DEFAULT 'open' | NCR status |
| `raised_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | QC Officer |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_equipment

**Purpose:** Equipment register with calibration tracking.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `equipment_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Equipment primary key |
| `equipment_name` | `VARCHAR(100)` | NOT NULL | Name |
| `equipment_type` | `VARCHAR(50)` | NULL | Type (e.g., `weighing_scale`, `autoclave`, `dryer`) |
| `serial_number` | `VARCHAR(50)` | NULL | Serial number |
| `location` | `VARCHAR(100)` | NULL | Physical location |
| `last_calibration_date` | `DATE` | NULL | Last calibration date |
| `next_calibration_due` | `DATE` | NULL | Next calibration due date |
| `calibration_certificate_url` | `VARCHAR(500)` | NULL | Certificate URL |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

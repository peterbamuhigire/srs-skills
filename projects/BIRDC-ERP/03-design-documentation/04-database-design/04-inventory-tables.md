## Section 4 — Inventory Tables

The dual-track inventory separation required by BR-001 is enforced at the schema level: `tbl_stock_balance` holds warehouse inventory only; `tbl_agent_stock_balance` holds agent field inventory only. No foreign key, trigger, or stored procedure joins these two tables into a single stock figure without explicit labelling.

---

### tbl_stock_items

**Purpose:** Product catalogue — the master list of all stockable items (finished goods, raw materials, packaging, consumables).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `stock_item_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Product primary key |
| `item_code` | `VARCHAR(50)` | NOT NULL, UNIQUE | Internal product code |
| `item_name` | `VARCHAR(255)` | NOT NULL | Product name |
| `item_type` | `ENUM('finished_good','raw_material','packaging','consumable','byproduct')` | NOT NULL | Product category |
| `base_uom` | `VARCHAR(20)` | NOT NULL | Base unit of measure (e.g., `kg`, `pkt`, `litre`) |
| `barcode` | `VARCHAR(50)` | NULL, UNIQUE | EAN-13 or Code 128 barcode |
| `reorder_level` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Reorder alert threshold |
| `is_expiry_tracked` | `TINYINT(1)` | NOT NULL DEFAULT 0 | FEFO enforcement flag (1 = tracked) |
| `shelf_life_days` | `SMALLINT UNSIGNED` | NULL | Standard shelf life in days |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |
| `gl_inventory_account_id` | `INT UNSIGNED` | NULL, FK → tbl_accounts | GL account for inventory posting |
| `gl_cogs_account_id` | `INT UNSIGNED` | NULL, FK → tbl_accounts | GL account for COGS posting |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(item_code)`, `UNIQUE(barcode)`, `INDEX(item_type)`, `INDEX(is_active)`

---

### tbl_stock_balance

**Purpose:** Current warehouse stock balances per product, batch, and location. This is warehouse inventory ONLY — BR-001. Agent stock is in `tbl_agent_stock_balance`.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `balance_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Balance record primary key |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `location_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_locations | Warehouse location |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Specific batch (NULL for non-batch-tracked items) |
| `quantity_on_hand` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Current quantity |
| `unit_cost` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Moving average or FIFO cost per unit |
| `total_value` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | quantity_on_hand × unit_cost |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Last update |

**Unique constraint:** `UNIQUE(stock_item_id, location_id, batch_id)` — one row per product/location/batch combination.

**Indexes:** `UNIQUE(stock_item_id, location_id, batch_id)`, `INDEX(location_id)`, `INDEX(quantity_on_hand)`

```sql
CREATE TABLE tbl_stock_balance (
  balance_id      INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  stock_item_id   INT UNSIGNED  NOT NULL,
  location_id     INT UNSIGNED  NOT NULL,
  batch_id        INT UNSIGNED  NULL,
  quantity_on_hand DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  unit_cost       DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  total_value     DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  updated_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP
                  ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (balance_id),
  UNIQUE KEY uq_stock_balance (stock_item_id, location_id, batch_id),
  KEY idx_stock_balance_location (location_id),
  CONSTRAINT fk_stock_balance_item   FOREIGN KEY (stock_item_id) REFERENCES tbl_stock_items (stock_item_id),
  CONSTRAINT fk_stock_balance_location FOREIGN KEY (location_id) REFERENCES tbl_stock_locations (location_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_agent_stock_balance

**Purpose:** Current stock balances for agent field inventory. Completely separate from `tbl_stock_balance` per BR-001. A product appears in both tables only if there is warehouse stock AND agent stock — they are never summed without labelling.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `agent_balance_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Agent balance record primary key |
| `agent_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_agents | Agent holding the stock |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Specific batch |
| `quantity` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Quantity held by agent |
| `unit_cost` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | Cost per unit at time of issuance |
| `total_value` | `DECIMAL(18,4)` | NOT NULL DEFAULT 0 | quantity × unit_cost |
| `updated_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | |

**Unique constraint:** `UNIQUE(agent_id, stock_item_id, batch_id)`

```sql
-- BR-001: This table is the AGENT stock ledger.
-- It must NEVER be JOINed with tbl_stock_balance without explicit consolidated-report labelling.
CREATE TABLE tbl_agent_stock_balance (
  agent_balance_id INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  agent_id         INT UNSIGNED  NOT NULL,
  stock_item_id    INT UNSIGNED  NOT NULL,
  batch_id         INT UNSIGNED  NULL,
  quantity         DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  unit_cost        DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  total_value      DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
  updated_at       DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP
                   ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (agent_balance_id),
  UNIQUE KEY uq_agent_stock (agent_id, stock_item_id, batch_id),
  KEY idx_agent_stock_item (stock_item_id),
  CONSTRAINT fk_agent_stock_agent FOREIGN KEY (agent_id) REFERENCES tbl_agents (agent_id),
  CONSTRAINT fk_agent_stock_item  FOREIGN KEY (stock_item_id) REFERENCES tbl_stock_items (stock_item_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

### tbl_stock_movements

**Purpose:** Immutable movement ledger — every stock increase and decrease across both warehouse and agent stock. Source of truth for stock movement history and audit.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `movement_id` | `BIGINT UNSIGNED` | PK, AUTO_INCREMENT | Movement primary key (BIGINT — high volume) |
| `movement_type` | `ENUM('receipt','sale','transfer_in','transfer_out','adjustment_increase','adjustment_decrease','production_issue','production_receipt','agent_issuance','agent_return','pos_sale','pos_void')` | NOT NULL | Type of movement |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Batch |
| `location_id` | `INT UNSIGNED` | NULL, FK → tbl_stock_locations | Warehouse location (NULL for agent movements) |
| `agent_id` | `INT UNSIGNED` | NULL, FK → tbl_agents | Agent (NULL for warehouse movements) |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Movement quantity (always positive — direction encoded in type) |
| `unit_cost` | `DECIMAL(18,4)` | NOT NULL | Cost per unit at time of movement |
| `total_value` | `DECIMAL(18,4)` | NOT NULL | quantity × unit_cost |
| `reference_type` | `VARCHAR(50)` | NULL | Source document type (e.g., `invoice`, `pos_transaction`, `transfer`) |
| `reference_id` | `INT UNSIGNED` | NULL | Source document primary key |
| `reference_number` | `VARCHAR(30)` | NULL | Source document number |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | User who created the movement |
| `movement_date` | `DATETIME` | NOT NULL | Movement date and time |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `INDEX(stock_item_id, movement_date)`, `INDEX(movement_type)`, `INDEX(agent_id)`, `INDEX(location_id)`, `INDEX(reference_type, reference_id)`

---

### tbl_batches

**Purpose:** Batch and lot tracking for all products with expiry dates. FEFO enforcement (BR-007) relies on `expiry_date` in this table.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `batch_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Batch primary key |
| `batch_number` | `VARCHAR(50)` | NOT NULL, UNIQUE | Batch number |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `production_order_id` | `INT UNSIGNED` | NULL, FK → tbl_production_orders | Source production order (for manufactured batches) |
| `manufacture_date` | `DATE` | NULL | Manufacturing date |
| `expiry_date` | `DATE` | NULL | Expiry date (NULL for items without expiry) |
| `qc_status` | `ENUM('pending','under_test','approved','approved_domestic_only','rejected','on_hold')` | NOT NULL DEFAULT 'pending' | QC disposition — BR-004 |
| `qc_approved_at` | `DATETIME` | NULL | QC approval timestamp |
| `qc_approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | QC officer who approved |
| `notes` | `TEXT` | NULL | Batch notes |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `UNIQUE(batch_number)`, `INDEX(stock_item_id)`, `INDEX(expiry_date)`, `INDEX(qc_status)`

---

### tbl_stock_locations

**Purpose:** Defines warehouse locations — storage zones, rack positions, factory gate, distribution centres.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `location_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Location primary key |
| `location_code` | `VARCHAR(20)` | NOT NULL, UNIQUE | Location code |
| `location_name` | `VARCHAR(100)` | NOT NULL | Location name |
| `location_type` | `ENUM('warehouse','factory_gate','distribution_centre','transit')` | NOT NULL | Location type |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

---

### tbl_uom_conversions

**Purpose:** Unit of measure conversion engine — converts between base UOM and secondary UOM (e.g., `kg` to `pkt_1kg`, `pkt_500g`).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `conversion_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Conversion primary key |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product |
| `from_uom` | `VARCHAR(20)` | NOT NULL | Source unit |
| `to_uom` | `VARCHAR(20)` | NOT NULL | Target unit |
| `conversion_factor` | `DECIMAL(18,8)` | NOT NULL | Factor: 1 `from_uom` = `conversion_factor` `to_uom` |

**Unique constraint:** `UNIQUE(stock_item_id, from_uom, to_uom)`

---

### tbl_stock_adjustments

**Purpose:** Records every stock adjustment with reason, quantity, value impact, and GL journal reference. Requires segregation of duties (BR-003).

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `adjustment_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Adjustment primary key |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_items | Product adjusted |
| `location_id` | `INT UNSIGNED` | NOT NULL, FK → tbl_stock_locations | Location |
| `batch_id` | `INT UNSIGNED` | NULL, FK → tbl_batches | Batch (if applicable) |
| `adjustment_type` | `ENUM('increase','decrease')` | NOT NULL | Direction |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Adjustment quantity |
| `unit_cost` | `DECIMAL(18,4)` | NOT NULL | Cost per unit for GL posting |
| `total_value` | `DECIMAL(18,4)` | NOT NULL | Total adjustment value |
| `reason` | `TEXT` | NOT NULL | Mandatory justification |
| `status` | `ENUM('pending_approval','approved','rejected')` | NOT NULL DEFAULT 'pending_approval' | Approval status |
| `created_by` | `INT UNSIGNED` | NOT NULL, FK → tbl_users | User who created adjustment |
| `approved_by` | `INT UNSIGNED` | NULL, FK → tbl_users | Approver (≠ creator — BR-003) |
| `gl_journal_id` | `INT UNSIGNED` | NULL, FK → tbl_journals | Auto-posted GL journal |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

---

### tbl_warehouse_bins

**Purpose:** Physical bin, rack, aisle, zone, cold-store, and staging slots used for putaway, picking, replenishment, and stock count.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `bin_id` | `INT UNSIGNED` | PK, AUTO_INCREMENT | Bin primary key |
| `location_id` | `INT UNSIGNED` | NOT NULL, FK -> tbl_stock_locations | Parent warehouse location |
| `zone_code` | `VARCHAR(30)` | NOT NULL | Zone identifier |
| `aisle_code` | `VARCHAR(30)` | NULL | Aisle identifier |
| `rack_code` | `VARCHAR(30)` | NULL | Rack identifier |
| `bin_code` | `VARCHAR(50)` | NOT NULL | Bin identifier unique within location |
| `storage_medium` | `ENUM('floor','rack','pallet','shelf','cold_store','staging')` | NOT NULL | Storage medium |
| `max_weight_kg` | `DECIMAL(18,4)` | NULL | Weight capacity |
| `max_volume_m3` | `DECIMAL(18,4)` | NULL | Volume capacity |
| `max_pallets` | `DECIMAL(10,2)` | NULL | Pallet capacity |
| `is_forward_pick` | `TINYINT(1)` | NOT NULL DEFAULT 0 | Forward-pick flag |
| `is_active` | `TINYINT(1)` | NOT NULL DEFAULT 1 | Active flag |

**Indexes:** `UNIQUE(location_id, bin_code)`, `INDEX(zone_code, aisle_code)`, `INDEX(is_forward_pick)`

---

### tbl_warehouse_tasks

**Purpose:** Execution task queue for putaway, picking, replenishment, staging, and cycle-count work.

**Key columns:**

| Column | Type | Constraint | Description |
|---|---|---|---|
| `task_id` | `BIGINT UNSIGNED` | PK, AUTO_INCREMENT | Task primary key |
| `task_type` | `ENUM('putaway','pick','replenishment','stage','count')` | NOT NULL | Task category |
| `stock_item_id` | `INT UNSIGNED` | NOT NULL, FK -> tbl_stock_items | Product |
| `batch_id` | `INT UNSIGNED` | NULL, FK -> tbl_batches | Batch |
| `from_bin_id` | `INT UNSIGNED` | NULL, FK -> tbl_warehouse_bins | Source bin |
| `to_bin_id` | `INT UNSIGNED` | NULL, FK -> tbl_warehouse_bins | Destination bin |
| `quantity` | `DECIMAL(18,4)` | NOT NULL | Task quantity |
| `source_type` | `VARCHAR(50)` | NULL | Source document type |
| `source_id` | `INT UNSIGNED` | NULL | Source document ID |
| `priority` | `ENUM('low','normal','high','urgent')` | NOT NULL DEFAULT 'normal' | Task priority |
| `status` | `ENUM('open','assigned','in_progress','completed','cancelled')` | NOT NULL DEFAULT 'open' | Task status |
| `sequence_no` | `INT UNSIGNED` | NULL | Pick-path sequence |
| `created_at` | `DATETIME` | NOT NULL DEFAULT CURRENT_TIMESTAMP | |

**Indexes:** `INDEX(task_type, status, priority)`, `INDEX(from_bin_id, status)`, `INDEX(to_bin_id, status)`, `INDEX(source_type, source_id)`

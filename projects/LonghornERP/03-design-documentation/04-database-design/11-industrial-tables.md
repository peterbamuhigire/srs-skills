# Industrial Module Tables

This section defines the database tables for the Product Lifecycle Management (PLM) and Transportation & Fleet Operations modules. The schema preserves the architectural boundary that engineering truth, production execution, transport execution, and asset accounting are not owned by the same tables.

---

# Product Lifecycle Management (PLM)

## `plm_items`

Engineering master record for controlled product definitions.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `item_code` | VARCHAR(60) | NOT NULL | Controlled engineering code. |
| `name` | VARCHAR(255) | NOT NULL | Engineering item name. |
| `item_class` | VARCHAR(50) | NOT NULL | Item class, e.g. `FINISHED_GOOD`, `COMPONENT`, `PACKAGING`, `DOCUMENT_ONLY`. |
| `uom_id` | BIGINT UNSIGNED | NOT NULL, FK -> `uom.id` | Base engineering unit of measure. |
| `current_released_revision_id` | BIGINT UNSIGNED | NULL, FK -> `plm_item_revisions.id` | Latest released revision pointer. |
| `is_active` | TINYINT(1) | NOT NULL, DEFAULT 1 | Engineering item active flag. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `item_code`), (`tenant_id`, `item_class`, `is_active`).

---

## `plm_item_revisions`

Revision history for engineering items.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `plm_item_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_items.id` | Parent engineering item. |
| `revision_code` | VARCHAR(20) | NOT NULL | Revision label, e.g. `A`, `B`, `1.0`. |
| `lifecycle_state` | ENUM('draft','in_review','released','superseded','obsolete') | NOT NULL, DEFAULT 'draft' | Controlled revision state. |
| `effective_from` | DATETIME | NULL | Date-time from which this revision is effective when released. |
| `effective_to` | DATETIME | NULL | Optional end of effectivity. |
| `predecessor_revision_id` | BIGINT UNSIGNED | NULL, FK -> `plm_item_revisions.id` | Prior revision in the chain. |
| `created_by` | BIGINT UNSIGNED | NOT NULL, FK -> `users.id` | Author. |
| `created_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Creation timestamp. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `plm_item_id`, `revision_code`), (`tenant_id`, `lifecycle_state`, `effective_from`).

---

## `plm_boms`

Header for Engineering BOM (EBOM) and Manufacturing BOM (MBOM) structures.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `parent_revision_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_item_revisions.id` | Parent released or draft revision. |
| `bom_type` | ENUM('EBOM','MBOM') | NOT NULL | Structure type. |
| `version_label` | VARCHAR(20) | NOT NULL | BOM version label. |
| `lifecycle_state` | ENUM('draft','released','superseded') | NOT NULL, DEFAULT 'draft' | BOM lifecycle state. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `parent_revision_id`, `bom_type`, `version_label`).

---

## `plm_bom_lines`

Component lines for a BOM, including effectivity.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `bom_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_boms.id` | Parent BOM. |
| `component_revision_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_item_revisions.id` | Controlled component revision. |
| `qty_per_parent` | DECIMAL(18,6) | NOT NULL | Quantity required. |
| `uom_id` | BIGINT UNSIGNED | NOT NULL, FK -> `uom.id` | BOM line UOM. |
| `scrap_factor_pct` | DECIMAL(6,3) | NOT NULL, DEFAULT 0 | Planning scrap factor percentage. |
| `plant_id` | BIGINT UNSIGNED | NULL, FK -> `branches.id` | Optional plant effectivity. |
| `option_code` | VARCHAR(50) | NULL | Optional variant or option rule. |
| `serial_from` | VARCHAR(50) | NULL | Optional starting serial range. |
| `serial_to` | VARCHAR(50) | NULL | Optional ending serial range. |
| `effective_from` | DATETIME | NULL | Optional effective start date. |
| `effective_to` | DATETIME | NULL | Optional effective end date. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `bom_id`), (`tenant_id`, `component_revision_id`), (`tenant_id`, `plant_id`, `effective_from`).

---

## `plm_documents`

Controlled files linked to item revisions.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `revision_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_item_revisions.id` | Linked revision. |
| `document_type` | VARCHAR(50) | NOT NULL | E.g. `DRAWING`, `SPECIFICATION`, `CERTIFICATE`. |
| `title` | VARCHAR(255) | NOT NULL | Controlled document title. |
| `revision_label` | VARCHAR(20) | NOT NULL | Document revision label. |
| `storage_path` | VARCHAR(500) | NOT NULL | File storage path. |
| `file_checksum_sha256` | CHAR(64) | NOT NULL | Integrity checksum. |
| `review_status` | ENUM('draft','approved','expired') | NOT NULL, DEFAULT 'draft' | Review status. |
| `expires_on` | DATE | NULL | Expiry date if applicable. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `revision_id`, `document_type`), (`tenant_id`, `review_status`, `expires_on`).

---

## `plm_ecrs`

Engineering Change Requests.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `target_type` | VARCHAR(50) | NOT NULL | Affected object type, e.g. `REVISION`, `BOM`, `DOCUMENT`. |
| `target_id` | BIGINT UNSIGNED | NOT NULL | Affected object identifier. |
| `reason` | TEXT | NOT NULL | Change justification. |
| `impact_summary` | TEXT | NOT NULL | Short impact summary. |
| `requested_effective_date` | DATE | NULL | Requested effectivity date. |
| `status` | ENUM('draft','submitted','impact_review','approved','rejected') | NOT NULL, DEFAULT 'draft' | Workflow state. |
| `requested_by` | BIGINT UNSIGNED | NOT NULL, FK -> `users.id` | Requester. |
| `requested_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Created timestamp. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `target_type`, `target_id`), (`tenant_id`, `status`, `requested_at`).

---

## `plm_ecos`

Engineering Change Orders raised from approved ECRs.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `ecr_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_ecrs.id` | Source ECR. |
| `eco_number` | VARCHAR(40) | NOT NULL | Controlled ECO number. |
| `implementation_notes` | TEXT | NOT NULL | Implementation instructions. |
| `rollback_notes` | TEXT | NULL | Rollback notes. |
| `status` | ENUM('draft','in_review','approved','released','cancelled') | NOT NULL, DEFAULT 'draft' | ECO status. |
| `released_at` | DATETIME | NULL | Release timestamp. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `eco_number`), (`tenant_id`, `status`, `released_at`).

---

## `plm_npi_programmes`

NPI programme and stage-gate records.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `programme_code` | VARCHAR(40) | NOT NULL | NPI programme code. |
| `name` | VARCHAR(255) | NOT NULL | Programme name. |
| `owner_user_id` | BIGINT UNSIGNED | NOT NULL, FK -> `users.id` | Programme owner. |
| `stage` | ENUM('concept','feasibility','design','validation','pilot','released') | NOT NULL, DEFAULT 'concept' | Current stage. |
| `target_release_date` | DATE | NULL | Target release date. |
| `status` | ENUM('active','on_hold','cancelled','completed') | NOT NULL, DEFAULT 'active' | Programme status. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `programme_code`), (`tenant_id`, `stage`, `status`).

---

## `plm_publication_events`

Publication log from PLM to downstream modules.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `revision_id` | BIGINT UNSIGNED | NOT NULL, FK -> `plm_item_revisions.id` | Published revision. |
| `publication_state` | ENUM('pending','partial','published','failed') | NOT NULL, DEFAULT 'pending' | Aggregate publication state. |
| `payload_json` | JSON | NOT NULL | Snapshot payload delivered downstream. |
| `published_at` | DATETIME | NULL | Successful publish timestamp. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `revision_id`), (`tenant_id`, `publication_state`, `published_at`).

---

# Transportation & Fleet Operations

## `shipment_orders`

Transport-demand object created from commercial or inventory workflows.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `source_type` | VARCHAR(50) | NOT NULL | Source document type, e.g. `SALES_ORDER`, `TRANSFER_ORDER`, `PURCHASE_ORDER`. |
| `source_id` | BIGINT UNSIGNED | NOT NULL | Source document primary key. |
| `origin_branch_id` | BIGINT UNSIGNED | NOT NULL, FK -> `branches.id` | Origin branch. |
| `destination_branch_id` | BIGINT UNSIGNED | NULL, FK -> `branches.id` | Destination branch if internal. |
| `destination_party_name` | VARCHAR(255) | NULL | Destination customer or supplier name if external. |
| `requested_ship_date` | DATE | NOT NULL | Required ship date. |
| `requested_delivery_date` | DATE | NULL | Required delivery date. |
| `total_weight_kg` | DECIMAL(15,3) | NOT NULL, DEFAULT 0 | Aggregate weight. |
| `total_volume_m3` | DECIMAL(15,3) | NOT NULL, DEFAULT 0 | Aggregate volume. |
| `service_priority` | ENUM('standard','urgent','critical') | NOT NULL, DEFAULT 'standard' | Service priority. |
| `status` | ENUM('unplanned','planned','dispatched','completed','cancelled') | NOT NULL, DEFAULT 'unplanned' | Shipment-order status. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `source_type`, `source_id`), (`tenant_id`, `status`, `requested_ship_date`), (`tenant_id`, `origin_branch_id`, `service_priority`).

---

## `transport_loads`

Logical grouping of shipment orders for planning and dispatch.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `load_code` | VARCHAR(40) | NOT NULL | Load reference code. |
| `planning_status` | ENUM('draft','planned','dispatched','closed','cancelled') | NOT NULL, DEFAULT 'draft' | Load state. |
| `planned_departure_at` | DATETIME | NULL | Planned departure timestamp. |
| `estimated_cost` | DECIMAL(18,2) | NOT NULL, DEFAULT 0 | Estimated trip cost. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `load_code`), (`tenant_id`, `planning_status`, `planned_departure_at`).

---

## `transport_load_shipments`

Link table between loads and shipment orders.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `load_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_loads.id` | Parent load. |
| `shipment_order_id` | BIGINT UNSIGNED | NOT NULL, FK -> `shipment_orders.id` | Linked shipment order. |
| `sequence_no` | INT UNSIGNED | NOT NULL | Planning sequence inside the load. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `load_id`, `shipment_order_id`), (`tenant_id`, `shipment_order_id`).

---

## `transport_routes`

Route header for planned or dispatched transport movement.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `route_code` | VARCHAR(40) | NOT NULL | Route reference code. |
| `load_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_loads.id` | Source load. |
| `resource_mode` | ENUM('internal_fleet','external_carrier') | NULL | Assigned resource mode. |
| `planning_status` | ENUM('planned','dispatched','in_transit','closed','cancelled') | NOT NULL, DEFAULT 'planned' | Route state. |
| `planned_departure_at` | DATETIME | NULL | Planned departure timestamp. |
| `planned_distance_km` | DECIMAL(12,2) | NOT NULL, DEFAULT 0 | Planned distance. |
| `estimated_trip_cost` | DECIMAL(18,2) | NOT NULL, DEFAULT 0 | Planned route cost. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `route_code`), (`tenant_id`, `planning_status`, `planned_departure_at`).

---

## `transport_route_stops`

Ordered stops for a route.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `route_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_routes.id` | Parent route. |
| `stop_sequence` | INT UNSIGNED | NOT NULL | Ordered stop number. |
| `stop_type` | ENUM('pickup','delivery','checkpoint') | NOT NULL | Stop purpose. |
| `party_name` | VARCHAR(255) | NOT NULL | Destination or pickup party. |
| `address_text` | TEXT | NOT NULL | Stop address. |
| `planned_arrival_at` | DATETIME | NULL | Planned arrival timestamp. |
| `actual_arrival_at` | DATETIME | NULL | Actual arrival timestamp. |
| `actual_departure_at` | DATETIME | NULL | Actual departure timestamp. |
| `status` | ENUM('pending','arrived','completed','failed_delivery','cancelled') | NOT NULL, DEFAULT 'pending' | Stop state. |

**Indexes:** PRIMARY (`id`), UNIQUE (`tenant_id`, `route_id`, `stop_sequence`), (`tenant_id`, `status`, `planned_arrival_at`).

---

## `transport_trips`

Execution record for a dispatched route.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `route_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_routes.id` | Route being executed. |
| `vehicle_asset_id` | BIGINT UNSIGNED | NULL, FK -> `assets.id` | Referenced vehicle asset when internal fleet is used. |
| `driver_user_id` | BIGINT UNSIGNED | NULL, FK -> `users.id` | Assigned driver when internal fleet is used. |
| `carrier_name` | VARCHAR(255) | NULL | Carrier when external mode is used. |
| `status` | ENUM('dispatched','in_transit','completed','closed','cancelled') | NOT NULL, DEFAULT 'dispatched' | Trip state. |
| `actual_departure_at` | DATETIME | NULL | Actual departure timestamp. |
| `actual_close_at` | DATETIME | NULL | Close timestamp. |
| `opening_odometer_km` | DECIMAL(12,1) | NULL | Start odometer for internal-fleet mode. |
| `closing_odometer_km` | DECIMAL(12,1) | NULL | End odometer for internal-fleet mode. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `route_id`), (`tenant_id`, `status`, `actual_departure_at`), (`tenant_id`, `vehicle_asset_id`, `status`).

---

## `transport_trip_events`

Immutable milestone events for trip execution.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `trip_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_trips.id` | Parent trip. |
| `route_stop_id` | BIGINT UNSIGNED | NULL, FK -> `transport_route_stops.id` | Stop if applicable. |
| `event_type` | ENUM('dispatched','departed_origin','arrived_stop','completed_stop','exception','closed') | NOT NULL | Milestone type. |
| `event_time` | DATETIME | NOT NULL | Event timestamp. |
| `latitude` | DECIMAL(10,7) | NULL | Optional GPS latitude. |
| `longitude` | DECIMAL(10,7) | NULL | Optional GPS longitude. |
| `note` | VARCHAR(500) | NULL | Optional note. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `trip_id`, `event_time`), (`tenant_id`, `route_stop_id`, `event_type`).

---

## `transport_exceptions`

Operational exception queue.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `trip_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_trips.id` | Affected trip. |
| `route_stop_id` | BIGINT UNSIGNED | NULL, FK -> `transport_route_stops.id` | Affected stop where relevant. |
| `severity` | ENUM('low','medium','high') | NOT NULL | Exception severity. |
| `reason_code` | VARCHAR(50) | NOT NULL | Machine- or user-generated reason code. |
| `owner_user_id` | BIGINT UNSIGNED | NULL, FK -> `users.id` | Current owner. |
| `status` | ENUM('open','in_progress','resolved','cancelled') | NOT NULL, DEFAULT 'open' | Exception state. |
| `due_response_at` | DATETIME | NULL | SLA-style response deadline. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `status`, `severity`, `due_response_at`), (`tenant_id`, `owner_user_id`, `status`).

---

## `transport_proofs`

Proof capture records for stops.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `trip_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_trips.id` | Parent trip. |
| `route_stop_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_route_stops.id` | Stop being proven. |
| `proof_type` | ENUM('signature','document_image','photo','barcode_qr','override') | NOT NULL | Proof method. |
| `storage_path` | VARCHAR(500) | NULL | File storage path if file-backed. |
| `captured_by` | BIGINT UNSIGNED | NOT NULL, FK -> `users.id` | Capturing actor. |
| `captured_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Capture timestamp. |
| `override_reason` | VARCHAR(500) | NULL | Mandatory when `proof_type = 'override'`. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `trip_id`, `route_stop_id`), (`tenant_id`, `proof_type`, `captured_at`).

---

## `transport_settlements`

Freight or internal-trip settlement header.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `trip_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_trips.id` | Related trip. |
| `settlement_type` | ENUM('carrier_invoice','internal_trip_cost') | NOT NULL | Settlement type. |
| `status` | ENUM('submitted','audit_hold','approved','posted','rejected') | NOT NULL, DEFAULT 'submitted' | Settlement state. |
| `planned_cost_total` | DECIMAL(18,2) | NOT NULL, DEFAULT 0 | Planned cost basis. |
| `actual_cost_total` | DECIMAL(18,2) | NOT NULL, DEFAULT 0 | Submitted actual cost. |
| `variance_pct` | DECIMAL(8,3) | NOT NULL, DEFAULT 0 | Variance percentage versus plan. |
| `submitted_by` | BIGINT UNSIGNED | NOT NULL, FK -> `users.id` | Submitter. |
| `submitted_at` | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Submission timestamp. |
| `approved_at` | DATETIME | NULL | Approval timestamp. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `trip_id`), (`tenant_id`, `status`, `submitted_at`).

---

## `transport_settlement_lines`

Detailed cost lines for settlement.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Surrogate primary key. |
| `tenant_id` | BIGINT UNSIGNED | NOT NULL, FK -> `tenants.id` | Tenant scope. |
| `settlement_id` | BIGINT UNSIGNED | NOT NULL, FK -> `transport_settlements.id` | Parent settlement. |
| `charge_type` | VARCHAR(50) | NOT NULL | E.g. `FUEL`, `TOLL`, `LINEHAUL`, `ALLOWANCE`. |
| `amount` | DECIMAL(18,2) | NOT NULL | Charge amount. |
| `note` | VARCHAR(255) | NULL | Optional note. |

**Indexes:** PRIMARY (`id`), (`tenant_id`, `settlement_id`), (`tenant_id`, `charge_type`).

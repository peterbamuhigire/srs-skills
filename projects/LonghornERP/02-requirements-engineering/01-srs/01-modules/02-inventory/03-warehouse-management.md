# Warehouse Management

## 3.1 Overview

A warehouse is the physical or logical storage location within which inventory is held and tracked. The Warehouse Management sub-module allows tenants to configure warehouses, bin locations within warehouses, inter-branch transfer workflows, consignment stock segregation, and quarantine zones for damaged goods.

## 3.2 Functional Requirements — Warehouse Management

**FR-INV-021:** The system shall create a warehouse record containing `warehouse_name`, `warehouse_code`, `location_address`, `warehouse_type`, and `branch_id` when a user submits the warehouse creation form with all mandatory fields populated.

**FR-INV-022:** The system shall support 3 warehouse types — `main`, `transit`, and `damaged_goods` — and shall use `warehouse_type` as a filter criterion on movement-type restrictions, blocking standard sales-issue movements from a `damaged_goods` warehouse.

**FR-INV-023:** The system shall allow a tenant administrator to enable bin-location tracking per warehouse when the `bin_tracking_enabled` flag is set to `true` for that warehouse, and shall require a `bin_id` on every stock movement line for that warehouse once the flag is enabled.

**FR-INV-024:** The system shall allow the creation of bins within a warehouse by storing `bin_code`, `bin_name`, `aisle`, `rack`, and `level` when bin tracking is enabled for the warehouse.

**FR-INV-025:** The system shall assign a default warehouse to each branch when the branch default is configured, and shall pre-populate the warehouse field on all transaction forms for users associated with that branch.

**FR-INV-026:** The system shall allow a user to override the default warehouse on any individual transaction line when the user has the `warehouse_override` permission assigned to their role.

**FR-INV-027:** The system shall create an inter-branch Transfer Order (TO) document containing the source warehouse, destination warehouse, line items with quantities, and a `transfer_status` of `draft` when the user initiates an inter-branch transfer request.

**FR-INV-028:** The system shall advance the Transfer Order status through the states `draft → dispatched → received → posted` and shall deduct stock from the source warehouse when status changes to `dispatched` and add stock to the destination warehouse when status changes to `received`.

**FR-INV-029:** The system shall automatically post a double-entry journal entry debiting the destination warehouse stock account and crediting the source warehouse stock account when the Transfer Order status changes to `posted`, referencing the Transfer Order number as the journal narration.

**FR-INV-030:** The system shall track consignment stock separately from owned stock by tagging movement lines with a `stock_ownership` field set to `consignment` and a `supplier_id` when consignment stock is received, and shall display owned and consignment quantities as distinct figures on all stock balance reports.

**FR-INV-031:** The system shall allow a user to move stock into the `quarantine` bin of a `damaged_goods` warehouse by creating an internal transfer movement when the user flags items as damaged, and shall lock those quantities from being allocated to any sales order until the quarantine is resolved.

**FR-INV-032:** The system shall allow a user to resolve a quarantine by either (a) writing down the stock value and marking the goods as disposed or (b) returning the goods to a `main` warehouse bin after inspection, and shall post the corresponding stock movement and journal entry in each case.

**FR-INV-033:** The system shall display the real-time stock balance per item per warehouse and per bin when the user opens the stock balance inquiry screen, with quantities current as of the last posted movement.

**FR-INV-034:** The system shall block the deletion of a warehouse record that has at least 1 item with a non-zero stock balance, returning an HTTP 409 Conflict response identifying the items with balances.

**FR-INV-035:** The system shall maintain a warehouse-level audit log recording every change to warehouse configuration fields (`warehouse_name`, `warehouse_type`, `branch_id`, `bin_tracking_enabled`) with `changed_by` and `changed_at` timestamps.

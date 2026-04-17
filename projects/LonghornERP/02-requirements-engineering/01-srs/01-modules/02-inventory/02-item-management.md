# Item Master Management

## 2.1 Overview

The item master is the authoritative record for every stockable, non-stockable, and composite item managed within a tenant's Longhorn ERP account. All stock movements, valuations, and reorder rules reference item master records.

## 2.2 Functional Requirements — Item Master Management

**FR-INV-001:** The system shall create a stock item record containing `item_code`, `item_name`, `description`, `category_id`, `base_uom_id`, `purchase_uom_id`, `sales_uom_id`, `item_type`, and `status` when a user submits the item creation form with all mandatory fields populated.

**FR-INV-002:** The system shall enforce uniqueness of `item_code` within a tenant's namespace when a new item record is saved, returning a validation error that identifies the conflicting code if the uniqueness constraint is violated.

**FR-INV-003:** The system shall support 3 item types — `stocked`, `service`, and `composite` — and shall prevent the creation of stock movement transactions for items of type `service` when any movement-posting event is triggered.

**FR-INV-004:** The system shall allow a tenant to define a multi-level category hierarchy (parent category → sub-category) of unlimited depth when a category is created or edited, and shall cascade the category path to all child items when the parent category name is updated.

**FR-INV-005:** The system shall support multiple Units of Measure (UOM) per item by storing `purchase_uom_id`, `sales_uom_id`, and `base_uom_id` as distinct fields, and shall store a conversion factor for each non-base UOM when the item is saved.

**FR-INV-006:** The system shall convert quantities from `purchase_uom` and `sales_uom` to `base_uom` using the stored conversion factor when a stock movement is posted, so that all inventory ledger balances are maintained in the base unit.

**FR-INV-007:** The system shall store a GS1-compliant barcode value (EAN-13, EAN-8, UPC-A, or QR code) per item when provided, and shall validate the barcode check-digit against the applicable GS1 algorithm before saving.

**FR-INV-008:** The system shall store `brand`, `shelf_life_days`, `min_stock_level`, `reorder_point`, and `reorder_quantity` as optional attributes on the item master, and shall make `shelf_life_days` a required input when the item category is flagged as food, pharmaceutical, or agricultural.

**FR-INV-009:** The system shall allow up to 5 images to be attached to an item record in JPEG or PNG format, each not exceeding 2 MB, when the user uploads images via the item detail screen.

**FR-INV-010:** The system shall soft-delete an item by setting `status = inactive` when a user deactivates it, shall block the creation of new stock movement lines referencing an inactive item, and shall preserve all historical transaction records that reference that item.

**FR-INV-011:** The system shall create item variants by generating a child item record with a unique `item_code` derived from the parent code and a variant suffix when the user defines a dimension combination (e.g., size + colour), and shall link the variant to its parent item via `parent_item_id`.

**FR-INV-012:** The system shall enforce that every variant of a parent item shares the same `base_uom_id` as the parent when a variant is created or the parent UOM is updated.

**FR-INV-013:** The system shall display the full variant matrix (all dimension combinations) on the parent item detail screen when the parent item is opened, with stock quantities per variant per warehouse shown inline.

**FR-INV-014:** The system shall allow a composite item to reference a Bill of Materials (BOM) composed of one or more component items with specified quantities when the BOM is saved, and shall validate that no composite item references itself (directly or transitively) as a component.

**FR-INV-015:** The system shall prevent deletion of any item that has at least 1 posted stock movement transaction, returning an HTTP 409 Conflict response with a message identifying the blocking transactions when a delete is attempted.

**FR-INV-016:** The system shall record `created_by`, `created_at`, `updated_by`, and `updated_at` on every item master record and shall expose this audit metadata in the item detail view.

**FR-INV-017:** The system shall allow bulk import of item master records from a CSV file conforming to the published Longhorn ERP item import template when the user initiates an import, and shall produce a row-level validation report identifying every row that failed validation before any records are persisted.

**FR-INV-018:** The system shall allow a tenant administrator to define custom item attributes (field name, data type, and optional allowed values) that are appended to the item form for all items within that tenant when the custom attribute is activated.

**FR-INV-019:** The system shall allow an item's `reorder_point`, `reorder_quantity`, and `min_stock_level` to be set independently per warehouse when warehouse-level reorder settings are enabled for that tenant.

**FR-INV-020:** The system shall generate a unique, human-readable `item_code` using the tenant's configured auto-numbering sequence when a user creates a new item without supplying a manual code.

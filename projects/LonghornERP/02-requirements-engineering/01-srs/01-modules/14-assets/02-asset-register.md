# Asset Register — Asset Master, Categories, and QR/Barcode Tagging

## 2.1 Overview

The asset register is the single source of truth for every fixed asset owned or controlled by the tenant. It captures master data, category classification, physical location, custodian assignment, and unique tag identifiers. All downstream operations — depreciation, revaluation, disposal, transfer, and maintenance — reference the asset master record.

## 2.2 Asset Master Record

**FR-ASSET-001:** When an authorised user submits the Create Asset form with all mandatory fields populated, the system shall create a new asset master record, assign a unique system-generated asset number in the format `ASSET-{YYYY}-{NNNNNN}`, set the asset status to *Active*, and return HTTP 201 with the new asset number within ≤ 2 seconds at P95.

The following fields are mandatory on the Create Asset form:

- Asset description (free text, ≤ 200 characters)
- Asset category (foreign key to asset category record)
- Acquisition date (date ≤ today)
- Acquisition cost (numeric, > 0, in tenant functional currency)
- Residual value (numeric, ≥ 0, < acquisition cost)
- Useful life (integer years, 1–100)
- Location (free text or foreign key to branch/location master)
- Custodian (foreign key to HR employee or department record)

The following fields are optional on the Create Asset form:

- Serial number (text, ≤ 100 characters)
- Manufacturer / model
- Warranty expiry date
- Linked purchase order reference (foreign key to Procurement module PO)
- Notes (free text, ≤ 1,000 characters)

**FR-ASSET-002:** When an authorised user submits the Create Asset form with any mandatory field absent or invalid, the system shall reject the submission with HTTP 422 and return a field-level error message identifying each failing field within ≤ 500 ms of request receipt.

**FR-ASSET-003:** When an authorised user edits an asset master record and saves changes, the system shall update the record, write an audit log entry capturing the previous value, new value, changed field name, user identity, and timestamp within the same database transaction, and return HTTP 200 within ≤ 2 seconds at P95.

**FR-ASSET-004:** When an authorised user attempts to change the acquisition cost or acquisition date of an asset that has at least 1 posted depreciation journal, the system shall reject the change with HTTP 422 and the error message "Acquisition cost and date are locked after depreciation is posted."

**FR-ASSET-005:** When an authorised user deactivates an asset record, the system shall set the asset status to *Disposed* or *Written Off* only through the Disposal workflow defined in Section 4; direct status override outside that workflow shall be rejected with HTTP 422.

## 2.3 Asset Categories

**FR-ASSET-006:** When an administrator creates a new asset category, the system shall record the category name, a default depreciation method (Straight-Line or Reducing Balance), a default depreciation rate (percentage per annum, 1–100), a default useful life (years), and the GL account mappings for: Asset Cost account, Accumulated Depreciation account, and Depreciation Expense account.

**FR-ASSET-007:** When an asset is created and assigned to a category, the system shall pre-populate the depreciation method, depreciation rate, and useful life fields from the category defaults; the user may override each field individually on the asset record.

**FR-ASSET-008:** When an administrator updates a category's default depreciation method or rate, the system shall apply the new defaults only to assets created after the update; existing asset depreciation schedules shall remain unchanged unless the user explicitly re-applies category defaults on each asset record.

**FR-ASSET-009:** When an administrator attempts to delete an asset category that has at least 1 active asset assigned to it, the system shall reject the deletion with HTTP 422 and the message "Category has active assets; reassign or dispose all assets before deleting."

## 2.4 QR and Barcode Asset Tagging

**FR-ASSET-010:** When a new asset record is saved, the system shall automatically generate a QR code encoding the asset number and store it as a vector-renderable data string linked to the asset record within ≤ 1 second of record creation.

**FR-ASSET-011:** When an authorised user requests the asset label for a single asset or a batch of assets, the system shall render a printable PDF label sheet containing the asset number, asset description, QR code, and tenant logo, formatted for standard label stock (Avery 5160 equivalent, 38.1 mm × 21.2 mm), and return the PDF within ≤ 10 seconds for a batch of up to 200 assets.

**FR-ASSET-012:** When a user scans an asset QR or barcode tag using the Longhorn ERP mobile application, the system shall retrieve and display the asset master record — including asset number, description, category, location, custodian, NBV, and status — within ≤ 3 seconds of a successful scan on a 4G mobile connection.

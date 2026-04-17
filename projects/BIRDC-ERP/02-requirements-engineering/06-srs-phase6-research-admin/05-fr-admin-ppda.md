## 3.2 F-016: Administration & PPDA Compliance

### 3.2.1 PPDA Procurement Register

**FR-ADM-001**
When the Administration Officer or Procurement Manager creates a procurement register entry, the system shall store: procurement reference number (format: `PROC-YYYY-NNNN`), procurement description, estimated value (UGX), PPDA category (Micro / Small / Large / Restricted — based on configured UGX thresholds per BR-005), procurement method, department initiating the procurement, date initiated, and the required approval authority for that category. `[CONTEXT-GAP: GAP-007]`

**FR-ADM-002**
When a procurement transaction is created, the system shall automatically generate a document checklist for that transaction based on the PPDA category, requiring all mandatory documents to be recorded: Procurement Request, Request for Quotation (3 quotes for Small and above), Evaluation Report, Local Purchase Order, Goods Receipt Note, Supplier Invoice, and Payment Voucher. Additional document types shall be configurable per category without developer involvement (DC-002).

**FR-ADM-003**
When the Finance Manager or Administration Officer attempts to approve a payment for a procurement transaction via the Accounts Payable module (F-007), the system shall verify that all mandatory PPDA document checklist items for that transaction are marked "Received and Filed". If any mandatory item is missing, the system shall block the payment with an error message listing the missing documents (BR-005). This validation shall be enforced at the API layer, not only in the UI.

**FR-ADM-004**
When the Administration Officer marks a PPDA document checklist item as "Received and Filed", the system shall store the document type, reference number, date received, filing location or document management reference, and the user who recorded the item, creating an immutable audit record.

**FR-ADM-005**
When the Procurement Manager or Administration Officer requests the PPDA procurement register export, the system shall generate a complete register in Excel format listing all procurement transactions for the financial year with: procurement reference, description, category, value, supplier, date, document checklist completion status (complete / incomplete), and approval authority. The export shall be generated within 15 seconds for up to 500 transactions and shall be suitable for direct submission during a PPDA audit.

**FR-ADM-006**
When a procurement transaction's estimated value is entered and exceeds the configured threshold for a higher PPDA category, the system shall automatically reclassify the transaction to the higher category, update the approval authority requirement, update the document checklist accordingly, and display a notification to the Administration Officer.

**FR-ADM-007**
When the Finance Director requests a PPDA compliance dashboard, the system shall display: total procurement transactions for the current financial year by PPDA category, percentage with complete document checklists, transactions with incomplete checklists (drill-down to identify missing documents), and total procurement spend by category and department, rendered within 5 seconds.

### 3.2.2 Document Management System

**FR-ADM-008**
When an authorised user uploads a document to the centralised document store, the system shall store: document ID (format: `DOC-NNNN`), document title, document type (from a configurable category list), related module reference (e.g., procurement reference, contract reference, asset ID), file name, file size, MIME type, upload date, uploader identity, and an access control tag specifying which roles may view or download the document.

**FR-ADM-009**
When a new version of an existing document is uploaded, the system shall retain all previous versions with their version numbers, upload dates, and uploader identities. The previous version shall be accessible for download by authorised users. A document shall never be irrecoverably overwritten.

**FR-ADM-010**
When a user attempts to view or download a document, the system shall verify that the user's role is included in the document's access control list. If the user is not authorised, the system shall deny access with a permission error and log the access attempt with the user's ID, document ID, and timestamp.

**FR-ADM-011**
When a user views or downloads a document, the system shall record: user ID, document ID, version accessed, action (View / Download), timestamp, and IP address, in the immutable document audit log. The audit log for each document shall be viewable by the IT Administrator and Finance Director.

**FR-ADM-012**
When the Administration Officer searches the document store by document title, type, related reference, or upload date range, the system shall return all matching documents within 2 seconds, displaying title, type, version, upload date, and uploader.

**FR-ADM-013**
When a PPDA compliance document has a statutory retention period, the system shall enforce that the document cannot be deleted from the store until the retention period expires. Documents subject to the Uganda Companies Act 7-year retention shall be flagged and protected. Any attempted deletion within the retention period shall be blocked and logged (DC-003).

### 3.2.3 Asset Register

**FR-ADM-014**
When the Administration Officer or Finance Manager creates a new asset record, the system shall store: asset ID (format: `ASSET-NNNN`), asset name, asset category (from a configurable list: Land / Building / Plant & Machinery / Vehicles / Computer Equipment / Furniture / Other), acquisition date, acquisition cost (UGX), supplier reference, department, physical location, custodian (linked to employee record), condition (New / Good / Fair / Poor / Disposed), and depreciation method (Straight Line or Reducing Balance — configurable per asset category).

**FR-ADM-015**
When an asset record is created with a depreciable category, the system shall calculate and store the annual depreciation amount using the configured method:

For Straight Line: $Annual\_Depreciation = \frac{Acquisition\_Cost - Residual\_Value}{Useful\_Life\_Years}$

For Reducing Balance: $Annual\_Depreciation = Net\_Book\_Value \times Depreciation\_Rate$

The system shall schedule monthly GL journal entries of:

DR Depreciation Expense — [Asset Category] / CR Accumulated Depreciation — [Asset ID]

for each active depreciable asset, posted automatically at period end without manual entry.

**FR-ADM-016**
When the Finance Manager or Finance Director requests the asset register as of a specified date, the system shall display all assets with: asset ID, name, category, acquisition date, acquisition cost, total accumulated depreciation, net book value as of the date requested, and current condition. The register shall be exportable to PDF and Excel within 10 seconds.

**FR-ADM-017**
When the Finance Manager initiates the annual physical asset verification workflow, the system shall generate a physical count list of all active assets sorted by department and location. Each asset shall have a verification checkbox for the custodian to confirm "Present and in stated condition" or "Discrepancy noted". Discrepancy notes shall be logged with the verifier's identity and date.

**FR-ADM-018**
When an asset is disposed of (sold, scrapped, or donated), the Administration Officer shall record the disposal date, disposal method, disposal proceeds (UGX), and reason. The system shall compute the gain or loss on disposal as:

$Disposal\_Gain\_Loss = Disposal\_Proceeds - Net\_Book\_Value\_At\_Disposal\_Date$

and post the disposal GL entry: DR Proceeds / DR Accumulated Depreciation / DR or CR Gain-Loss on Disposal / CR Asset Cost. The asset status shall be updated to "Disposed" and the asset shall cease depreciation from the disposal date.

**FR-ADM-019**
When an asset is transferred between departments, the Administration Officer shall record the transfer date, originating department, receiving department, and the identity of the receiving custodian. The GL cost centre for monthly depreciation shall update to the receiving department from the transfer date.

### 3.2.4 Vehicle and Equipment Logbook

**FR-ADM-020**
When the Administration Officer or a vehicle custodian creates a trip entry in the vehicle logbook, the system shall store: vehicle ID (linked to asset register), driver name (linked to employee record), trip date, departure time, destination, purpose, odometer reading at departure, odometer reading at return, fuel consumed (litres), and any maintenance issues observed during the trip. The system shall automatically compute the distance travelled (odometer return minus odometer departure) and the fuel efficiency (km per litre).

**FR-ADM-021**
When a fuel purchase is recorded for a vehicle, the system shall store: vehicle ID, date, fuel station, litres purchased, cost per litre (UGX), total cost, and the authorising officer. The total cost shall post to the GL as DR Vehicle Running Expenses / CR Cash or Accounts Payable.

**FR-ADM-022**
When a maintenance event is recorded for a vehicle or piece of equipment, the system shall store: asset ID, maintenance date, maintenance type (Routine Service / Repair / Inspection / Other), description, labour cost (UGX), parts cost (UGX), total cost, service provider, and next scheduled service date or odometer reading. The total maintenance cost shall post to the GL as DR Maintenance Expense / CR Accounts Payable.

**FR-ADM-023**
When the Administration Officer requests a vehicle utilisation report for a specified period, the system shall generate a report per vehicle showing: total trips, total distance (km), total fuel consumed, fuel cost, average fuel efficiency (km/litre), and total maintenance cost, exportable to PDF and Excel within 5 seconds.

### 3.2.5 Contract Register

**FR-ADM-024**
When the Administration Officer creates a contract record, the system shall store: contract ID (format: `CONT-NNNN`), contract title, contract type (Supplier / Service / Lease / Employment / Research Partnership / Other), counterparty name, contract start date, contract end date, total contract value (UGX), payment terms, key obligations summary (text), and the BIRDC signatory (linked to employee record).

**FR-ADM-025**
When a contract record is created or updated with a contract end date, the system shall schedule automatic email reminders to the Administration Officer and Finance Manager at 90 days, 60 days, and 30 days before the expiry date, using PHPMailer. Each reminder shall include the contract ID, title, counterparty, expiry date, and total value.

**FR-ADM-026**
When the Administration Officer opens the contract register, the system shall display all contracts in a filterable list with: contract ID, title, counterparty, status (Active / Expired / Pending Renewal / Terminated), expiry date, days to expiry (negative values indicating overdue contracts), and contract value. Contracts expiring within 30 days shall be highlighted visually.

**FR-ADM-027**
When the Administration Officer attaches a signed contract document to a contract record, the system shall store the document in the centralised document store (F-016 document management), link it to the contract record, and apply the statutory 7-year document retention policy automatically.

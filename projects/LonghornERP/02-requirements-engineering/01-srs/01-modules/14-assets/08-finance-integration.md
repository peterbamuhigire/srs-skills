# Assets and Accounting Finance Integration

## 1. Purpose

This section defines the control boundary between the `ASSETS` module and the `ACCOUNTING` module for fixed asset accounting. The objective is to ensure that LonghornERP supports operational asset management without weakening capitalization discipline, depreciation governance, impairment control, retirement accounting, or general ledger integrity.

## 2. Ownership Boundary

### 2.1 `ASSETS` owns

The `ASSETS` module shall own the operational asset record and lifecycle administration for:

- asset registration and tagging
- asset class, category, model, serial, and operational identifiers
- asset condition, service status, and inspection status
- maintenance history and service interventions
- location, site, department, cost-center reference, and custody assignment
- internal transfers between sites, departments, projects, or custodians
- disposal workflow initiation and operational evidence such as photos, inspection notes, auction references, or handover records

### 2.2 `ACCOUNTING` owns

The `ACCOUNTING` module shall own finance-policy application and ledger consequences for:

- capitalization policy determination
- capitalization date and in-service date recognition for finance purposes
- depreciation books and methods
- useful life, residual value, and depreciation convention
- book and tax depreciation where supported
- impairment assessment and impairment posting
- revaluation processing where the deployment enables revaluation
- retirement accounting, gain or loss on disposal, and derecognition
- all asset-related journal generation and posting to the general ledger

### 2.3 Boundary rule

The `ASSETS` module shall not independently finalize accounting outcomes. It may capture operational facts and propose finance-impacting changes, but only the `ACCOUNTING` module shall determine book treatment and post financial entries.

## 3. Functional Requirements

### 3.1 Operational-to-finance integration

- `FR-ASSET-FIN-001` The system shall allow `ASSETS` to create or update an operational asset record before capitalization is approved, while clearly marking the asset as non-posting until finance activation occurs.
- `FR-ASSET-FIN-002` The system shall transmit asset master data required by `ACCOUNTING`, including asset identifier, description, asset class, acquisition reference, vendor or project reference where applicable, location, custodian, service date candidate, disposal status, and transfer history summary.
- `FR-ASSET-FIN-003` The system shall support a finance activation workflow in which `ACCOUNTING` confirms capitalization policy, depreciation parameters, and posting readiness before the asset becomes a depreciable accounting asset.

### 3.2 Change governance

- `FR-ASSET-FIN-004` The system shall classify asset changes into non-financial changes and finance-impacting changes.
- `FR-ASSET-FIN-005` Finance-impacting changes shall include, at minimum, acquisition cost corrections, asset class changes, in-service date changes, useful life proposals, residual value proposals, disposal proposals, impairment triggers, revaluation triggers where enabled, and changes that alter owning entity, book, or depreciation basis.
- `FR-ASSET-FIN-006` Non-financial changes such as condition notes, maintenance updates, and custodian acknowledgements may be completed within `ASSETS` without finance approval, provided they do not affect accounting treatment.
- `FR-ASSET-FIN-007` Finance-impacting changes initiated in `ASSETS` shall remain in a pending state until `ACCOUNTING` approval or rejection is recorded.

### 3.3 Disposal and retirement boundary

- `FR-ASSET-FIN-008` The `ASSETS` module shall support disposal workflow initiation, operational evidence capture, and handoff to finance for derecognition.
- `FR-ASSET-FIN-009` The `ACCOUNTING` module shall determine retirement date, proceeds treatment, accumulated depreciation release, gain or loss calculation, and retirement journal postings.
- `FR-ASSET-FIN-010` An asset shall not move to final disposed status in the enterprise record until finance retirement processing is completed or explicitly waived under an authorized policy.

### 3.4 Transfers and custody

- `FR-ASSET-FIN-011` The `ASSETS` module shall record operational transfers between locations, departments, projects, and custodians with full audit history.
- `FR-ASSET-FIN-012` Where a transfer changes legal entity, depreciation book, reporting segment, or cost attribution basis, the transfer shall be routed to `ACCOUNTING` for review before becoming effective in finance.
- `FR-ASSET-FIN-013` The system shall preserve both the operational custody trail and the accounting ownership trail when they differ.

## 4. Required Integration Events and Data

### 4.1 Events from `ASSETS` to `ACCOUNTING`

The system shall publish or queue integration events for:

- `asset_registered`
- `asset_master_changed`
- `asset_transfer_requested`
- `asset_transfer_effective`
- `asset_disposal_requested`
- `asset_condition_exception_raised`
- `asset_impairment_indicator_reported`
- `asset_revaluation_trigger_reported` where supported

Each event shall include, at minimum:

- enterprise and legal-entity identifiers
- asset identifier and asset class
- source transaction identifier
- event timestamp and effective date
- changed fields with before and after values where applicable
- user or workflow actor identity
- supporting document or evidence references where available

### 4.2 Responses from `ACCOUNTING` to `ASSETS`

The system shall publish or queue integration outcomes for:

- `asset_capitalization_approved`
- `asset_capitalization_rejected`
- `asset_depreciation_parameters_set`
- `asset_transfer_finance_approved`
- `asset_transfer_finance_rejected`
- `asset_retirement_completed`
- `asset_impairment_recorded`
- `asset_revaluation_recorded` where supported

Each outcome shall include status, decision actor, decision timestamp, finance reference number, and any rejection or exception reason needed by operations.

## 5. Controls and Approval Safeguards

- `FR-ASSET-FIN-014` The system shall prevent finance-impacting asset changes from bypassing configured finance approval workflows.
- `FR-ASSET-FIN-015` The system shall record who initiated, reviewed, approved, rejected, and executed every finance-impacting asset change.
- `FR-ASSET-FIN-016` The system shall block depreciation, retirement, impairment, and revaluation postings from using asset master changes that remain unapproved.
- `FR-ASSET-FIN-017` The system shall maintain an auditable link between the operational asset record, the finance approval record, and the resulting journal or accounting transaction.
- `FR-ASSET-FIN-018` The system shall support maker-checker controls so that a user who initiates a finance-impacting asset change cannot be the sole approver when segregation rules require independent review.
- `FR-ASSET-FIN-019` The system shall surface exceptions where operational status and accounting status diverge, including assets disposed operationally but not retired financially, or assets in service operationally but not yet capitalized.

## 6. Outcome

LonghornERP shall treat `ASSETS` as the operational system of record for the physical asset lifecycle and `ACCOUNTING` as the financial system of record for fixed asset accounting treatment and ledger impact. This separation shall preserve operational agility while enforcing finance control, auditability, and policy compliance.

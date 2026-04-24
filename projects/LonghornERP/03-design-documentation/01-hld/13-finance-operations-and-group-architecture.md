# 13. Finance Operations and Group Architecture

## 13.1 Purpose

This section extends the LonghornERP architecture with finance operations and group-finance capabilities that sit above core accounting. The design strengthens controlled cash execution, bank-facing integration boundaries, asset-accounting integration, and group reporting readiness while keeping LonghornERP as the system of record for operational ERP data and the authoritative posting engine for subledger-to-general-ledger accounting.

## 13.2 Architectural Principles

1. LonghornERP remains the ERP core for vendors, customers, invoices, payments, journals, asset registers, entity structures, and operational accounting events.
2. Payment execution is governed inside LonghornERP through preparation, approval, release, and evidence capture even when an external bank connector or treasury workstation performs the final transmission.
3. Bank connectivity is an integration boundary, not a ledger boundary. Imported bank data enriches reconciliation and cash visibility but does not replace ERP-controlled accounting.
4. Asset accounting is managed as an ERP-controlled finance operation that converts operational asset events into governed accounting runs, depreciation postings, and reporting outputs.
5. Group finance capabilities provide consolidation-ready orchestration inside LonghornERP and preserve optional integration points for external consolidation or treasury tools where regulatory scale or group complexity later demands them.

## 13.3 Capability Domains

### 13.3.1 Payment Control Domain

The payment control domain governs the lifecycle from approved payable obligations to payment release evidence. It includes:

- bank account governance
- payment batch assembly
- maker-checker approval chains
- release authorisation
- bank transmission status capture
- rejection and return handling
- audit evidence retention

This domain depends on `ACCOUNTING`, `PROCUREMENT`, and workflow services but does not duplicate invoice ownership or vendor master ownership.

### 13.3.2 Bank Connectivity and Cash Evidence Domain

This domain manages:

- internal bank-account master data
- external bank statement imports
- secure connector handoff points
- statement parsing and import staging
- reconciliation matching and exception queues
- imported bank evidence retention

The bank connectivity layer supports direct bank APIs, host-to-host files, SWIFT service providers, and manual statement import. Connector adapters remain replaceable so LonghornERP can integrate with regional African banks, PSPs, and future treasury tools without changing finance core services.

### 13.3.3 Asset Accounting Operations Domain

This domain bridges fixed-asset operational records and finance postings. It manages:

- accounting books per entity and basis
- depreciation and amortisation runs
- asset transfer and disposal accounting generation
- period-end asset close checks
- tie-out between asset subledger and general ledger

Operational asset lifecycle data continues to originate in the asset module, while finance operations govern accounting treatment and periodised posting runs.

### 13.3.4 Group Finance and Consolidation Domain

This domain supports:

- ownership hierarchies
- reporting groups
- FX translation runs
- elimination runs
- top-side adjustments
- reporting certification and sign-off

The domain is designed for SME through mid-market multi-entity groups and provides a clean export boundary for future enterprise treasury or specialist consolidation platforms.

## 13.4 Service Boundaries

### 13.4.1 ERP Core Services

ERP core services continue to own:

- entities and legal-company master data
- chart of accounts and fiscal calendars
- source transactions and journals
- asset master records and operational lifecycle events
- vendor/customer obligations

### 13.4.2 Finance Operations Services

Finance operations services own:

- bank account approval metadata
- payment batches and release controls
- bank statement ingestion metadata
- reconciliation work queues
- depreciation run orchestration
- group-finance orchestration records
- reporting certification evidence

### 13.4.3 External Tool Boundary

External treasury, banking, and specialist consolidation tools may be introduced later. When present, they must integrate through defined APIs or import/export contracts and must not become the hidden source of truth for ERP entity structures, master data, or accounting balances. LonghornERP remains the authoritative business and accounting platform; external tools may add specialised optimisation, connectivity, or advanced group-reporting workflows.

## 13.5 Reference Architecture

```text
Operational Modules -> Accounting Core -> Finance Operations Layer -> Integration Adapters -> Banks / Treasury / Consolidation Tools
                                           |                         |
                                           +-> Reporting Evidence    +-> Statements / Payment Status / FX Inputs
```

### 13.5.1 Payment Flow

1. Approved obligations are selected into payment batches.
2. Payment batches are validated against bank account policies, signer matrices, and approval thresholds.
3. Release-approved batches are transmitted through connector adapters or exported for controlled external execution.
4. Bank acknowledgements, returns, or statement events are captured back into LonghornERP.
5. Reconciliation and accounting status are updated with full audit evidence.

### 13.5.2 Group Close Flow

1. Entity books are closed in accounting.
2. Asset accounting runs complete and feed period postings.
3. FX translation runs produce reporting-currency balances.
4. Elimination runs and top-side adjustments are recorded.
5. Reporting packs are certified before publication or downstream export.

## 13.6 Integration Boundaries

### 13.6.1 Bank Connectivity Boundary

LonghornERP exposes a bank-adapter boundary for:

- payment file generation
- payment status callbacks
- statement import and parsing
- bank balance snapshots

The adapter boundary isolates bank-specific formats, security handshakes, and transport protocols from finance business rules. This keeps regional banking variation from contaminating core ERP services.

### 13.6.2 Asset Accounting Boundary

The finance operations layer consumes approved asset events, asset books, and asset valuation data from the asset module. It does not replace the operational asset register. Accounting postings generated by depreciation, impairment, disposal, or revaluation runs are handed back to the accounting core for controlled journal posting.

### 13.6.3 Group Consolidation Boundary

LonghornERP supports internal ownership hierarchies, translation, elimination, and top-side adjustments. If a future external consolidation platform is adopted, LonghornERP can export:

- entity trial balances
- ownership structures
- FX translation inputs
- elimination candidates
- certification status

This allows phased maturity without re-architecting the finance foundation.

## 13.7 Security and Control Model

The architecture requires:

- segregation between payment preparers, approvers, and releasers
- restricted maintenance of bank account master data
- immutable audit trails for payment release and reporting certification
- dual-control or threshold-based approvals for sensitive finance actions
- evidence capture for imported statements, reconciliations, and certified reports

## 13.8 Scalability and Deployment Expectations

The finance operations layer must support:

- multiple bank accounts per entity and currency
- high-volume daily statement imports
- batched payment releases
- multi-book asset accounting
- multi-entity group reporting

The design assumes asynchronous orchestration for bank imports, reconciliation suggestion generation, depreciation processing, and consolidation runs.

## 13.9 Architectural Outcome

This layer makes LonghornERP finance operationally stronger without forcing premature dependence on external treasury or consolidation suites. It gives growing African companies disciplined control of cash execution, asset accounting, and group reporting inside the ERP core, while preserving clean future integration boundaries for larger enterprise landscapes.

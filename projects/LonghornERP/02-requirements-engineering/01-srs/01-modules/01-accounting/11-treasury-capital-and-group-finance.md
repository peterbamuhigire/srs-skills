# 11. Treasury, Capital, and Group Finance

## 11.1 Overview

This section extends LonghornERP Accounting into disciplined finance-ERP behavior for cash governance, payment control, bank traceability, fixed-asset accounting, and multi-entity group-finance operations. The scope remains accounting-owned. It does not introduce treasury dealing, market-risk trading, or advanced treasury workstation capabilities.

The requirements in this section are intended to make the accounting domain operationally stronger in the following areas:

- treasury and cash governance over bank accounts, payment initiation, and liquidity visibility
- payment-file traceability from approved obligation to bank-file release and bank response
- controlled reconciliation discipline with certification and escalation
- fixed-asset accounting from capitalization through depreciation, impairment, transfer, and retirement
- group-finance workflows for ownership hierarchy, FX translation inputs, intercompany settlement discipline, eliminations, top-side adjustments, and certified close outputs

## 11.2 Treasury and Cash Governance

### Functional Requirements

- **FR-ACCT-149**: The system shall maintain governed bank-account master data including legal entity, account purpose, currency, signer or approval policy, status, effective date, and linked GL account.
- **FR-ACCT-150**: The system shall enforce segregation of duties between payment initiation, payment approval, and bank-file release according to configured finance approval policy.
- **FR-ACCT-151**: The system shall generate short-term cash-position and cash-forecast views using approved payables, approved payroll obligations, expected receivables, opening bank balances, and scheduled internal transfers.
- **FR-ACCT-152**: The system shall support liquidity classification tags on bank accounts and cash movements so finance users can distinguish operating, restricted, payroll, tax, project, and other governed cash buckets in reports.

## 11.3 Payment Governance and Bank-File Traceability

### Functional Requirements

- **FR-ACCT-153**: The system shall create governed payment batches only from approved obligations including approved supplier invoices, approved expense settlements, approved payroll outputs, and approved tax remittances.
- **FR-ACCT-154**: The system shall generate bank-payment files with immutable traceability to payment batch, source obligations, approvers, file generator, generation timestamp, file hash, and release status.
- **FR-ACCT-155**: The system shall prevent duplicate bank-file release for the same approved payment instructions unless the original file is formally recalled, voided, or marked bank-rejected under audit.
- **FR-ACCT-156**: The system shall reconcile bank-file execution outcomes back to payment instructions, cash journals, and exception status so rejected, partially executed, or returned payments remain visible for resolution.
- **FR-ACCT-157**: The system shall store positive-pay, payment-confirmation, or bank-acknowledgement evidence against the relevant payment batch or bank-file record where such evidence is used by the finance process.

## 11.4 Bank Reconciliation Discipline

### Functional Requirements

- **FR-ACCT-158**: The system shall enforce a configured reconciliation cadence per bank account and flag overdue reconciliation work on the finance cockpit.
- **FR-ACCT-159**: The system shall age unreconciled bank-statement lines and unreconciled GL cash items into configurable age buckets for operational follow-up.
- **FR-ACCT-160**: The system shall escalate stale reconciling items that exceed configured age or materiality thresholds to the Finance Manager or designated reviewer.
- **FR-ACCT-161**: The system shall support reconciliation certification by an authorised reviewer and shall preserve preparer, reviewer, certification timestamp, exceptions, and supporting evidence.

## 11.5 Fixed-Asset Accounting Lifecycle

### Functional Requirements

- **FR-ACCT-162**: The system shall capitalise fixed assets from approved acquisition or project-completion events by creating or updating the accounting asset record and posting the capitalization journal.
- **FR-ACCT-163**: The system shall maintain fixed-asset accounting books, depreciation methods, useful life, residual value, in-service date, asset class, and linked balance-sheet and expense accounts.
- **FR-ACCT-164**: The system shall execute controlled depreciation runs that post depreciation expense and accumulated depreciation journals once per asset book and period.
- **FR-ACCT-165**: The system shall support impairment, reclassification, and transfer accounting events with mandatory reason, effective date, approver, and evidence trail.
- **FR-ACCT-166**: The system shall support asset retirement, disposal, and write-off accounting including cost removal, accumulated depreciation clearance, proceeds recognition, and gain or loss calculation.
- **FR-ACCT-167**: The system shall provide period-based reconciliation between the fixed-asset subledger and the general ledger and shall identify unreconciled differences by asset, class, book, and account.

## 11.6 Multi-Entity and Group Finance Workflows

### Functional Requirements

- **FR-ACCT-168**: The system shall maintain a governed ownership hierarchy for reporting entities including parent-child relationships, effective dates, ownership percentage, and reporting currency.
- **FR-ACCT-169**: The system shall preserve FX translation foundations by storing reporting-basis exchange-rate inputs, translation method, translated balances, and translation run metadata for each group reporting period.
- **FR-ACCT-170**: The system shall govern intercompany settlement workflows by tracking counterparties, settlement status, unresolved differences, agreed balances, and clearing evidence.
- **FR-ACCT-171**: The system shall segregate elimination journals and top-side adjustments from local statutory books and shall require dedicated group-finance permissions and approval workflow for such entries.
- **FR-ACCT-172**: The system shall produce a certified group close pack that links entity submissions, translation results, elimination journals, top-side adjustments, sign-offs, and final issued reporting artefacts for the reporting period.

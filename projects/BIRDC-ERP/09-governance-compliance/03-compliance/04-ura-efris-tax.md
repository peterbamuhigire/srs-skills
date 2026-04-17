# Section 4: Uganda Revenue Authority — EFRIS, PAYE, and WHT Compliance

## 4.1 EFRIS Compliance

### 4.1.1 Legal Obligation

The Uganda Electronic Fiscal Receipting and Invoicing Solution (EFRIS) is mandated by the URA for all VAT-registered businesses. Every commercial invoice and receipt issued by BIRDC must be submitted to URA's EFRIS system in real time via the system-to-system API. Failure to submit results in the fiscal document being legally non-compliant and may trigger URA penalties.

### 4.1.2 System Implementation

FR-SAL-003 mandates real-time EFRIS submission for every sales invoice on posting. FR-POS-008 mandates submission for every POS receipt. FR-EFR-001 extends this to credit notes across all transaction types in Phase 7.

The workflow for every commercial document is:

1. User confirms the invoice or receipt in the system.
2. The system posts the GL entry and generates the fiscal document.
3. The system immediately submits the document to the URA EFRIS API.
4. URA returns a Fiscal Document Number (FDN) and verification QR code.
5. The system stores the FDN against the transaction record.
6. The FDN and QR code are printed on the invoice or receipt (FR-EFR-002).

A document is only fully issued once the FDN is received and stored. Documents pending EFRIS submission are marked "Pending EFRIS" in the invoice lifecycle (FR-SAL-001).

### 4.1.3 Failed Submission Handling

FR-EFR-003 manages a failed submission retry queue. When EFRIS submission fails (network timeout, API error, or URA system downtime), the system:

1. Marks the document as "EFRIS Submission Failed" in the retry queue.
2. Retries the submission automatically at configurable intervals.
3. Alerts the Finance Manager within 60 seconds of the first failure (FR-SAL-012).
4. Logs every submission attempt (success and failure) in the EFRIS audit log (FR-EFR-004).

The Finance Manager can view the full retry queue status on the Finance Dashboard at any time.

### 4.1.4 EFRIS Audit Log

FR-EFR-004 maintains a tamper-evident EFRIS audit log with the hash chain integrity mechanism (BR-013). This log records every submission attempt, the API request payload, the URA response, and the stored FDN. This provides the complete audit trail that URA inspectors require when verifying EFRIS compliance.

*[CONTEXT-GAP: GAP-001]: EFRIS API sandbox credentials are required before this workflow can be tested. BIRDC IT must register on the URA EFRIS developer portal and obtain sandbox API credentials before Phase 1 invoice testing sprints begin.*

### 4.1.5 EFRIS Penalty Risk

Non-submission or fraudulent document submission under EFRIS regulations carries URA penalties. The system's retry mechanism and immutable audit log are specifically designed to eliminate the risk of accidental non-compliance. Intentional circumvention of EFRIS (for example, issuing invoices outside the system) is architecturally prevented because no GL posting can occur without a corresponding EFRIS submission attempt — BIRDC cannot record revenue in the GL without triggering the EFRIS workflow.

## 4.2 PAYE Compliance

### 4.2.1 Legal Obligation

The Uganda Income Tax Act (Cap 340) requires BIRDC as an employer to withhold Pay As You Earn (PAYE) income tax from employee salaries and remit it to URA monthly.

### 4.2.2 System Implementation

FR-PAY-002 implements PAYE calculation using configurable tax bands. The tax bands are stored in a configuration table and can be updated by the Finance Director via the UI (DC-002) within 24 hours of URA publishing new bands — without requiring developer involvement. [CONTEXT-GAP: GAP-008: 2025/26 PAYE tax bands to be confirmed before payroll module development begins.]

The PAYE calculation follows the standard Uganda progressive tax formula. For each employee:

$PAYE = \sum_{i=1}^{n} (Band_i\_Rate \times min(TaxableIncome, Band_i\_Upper) - min(TaxableIncome, Band_i\_Lower))$

Where taxable income = gross salary minus exempt allowances as defined in the Income Tax Act.

The payroll run (FR-PAY-006) computes PAYE for all employees in a single batch. The Finance Manager approves and locks the payroll (BR-010, FR-PAY-007), at which point the PAYE liability is posted to the GL as a payable to URA (FR-PAY-009).

### 4.2.3 PAYE Remittance Tracking

The system tracks the monthly PAYE payable balance per URA's requirement. The Finance team can generate a PAYE remittance summary showing total PAYE deducted per period, remittance payments made to URA, and outstanding balance. This satisfies URA's monthly PAYE return requirement.

## 4.3 Withholding Tax (WHT) Compliance

### 4.3.1 Legal Obligation

Under the Uganda Income Tax Act (Cap 340), BIRDC is designated as a withholding agent. When making payments to local service suppliers (subject to WHT), BIRDC must withhold 6% of the payment value and remit it to URA. BIRDC must issue a WHT certificate to the supplier.

### 4.3.2 System Implementation

FR-AP-007 calculates WHT at 6% on all applicable local service supplier payments. The system identifies WHT-applicable suppliers through a flag on the vendor record. When the Accounts Payable module processes a qualifying payment, it:

1. Deducts 6% WHT from the payment amount automatically.
2. Posts the WHT liability: DR Expense / CR Vendor Payable / CR WHT Payable (URA).
3. Generates a URA WHT certificate (Form WHT 1) for the supplier.
4. Records the WHT amount in the WHT register for monthly URA remittance.

The Finance Director can generate a WHT remittance report for any period showing all WHT deducted, certificates issued, and outstanding remittance to URA.

## 4.4 Seven-Year Record Retention Compliance

### 4.4.1 Legal Obligation

The Uganda Income Tax Act (Cap 340) and Uganda Companies Act (Cap 110) both require BIRDC to retain financial records for 7 years.

### 4.4.2 System Implementation

FR-SYS-004 enforces 7-year retention as a system-level constraint. The database schema marks all financial records with a `retention_until` field set to 7 years from the record's creation date. The system's automated record management process cannot delete any record before this date. An IT Administrator cannot override this restriction without a database-level intervention that would generate an audit log alert.

FR-FIN-007 (hash chain integrity) ensures that retained records are tamper-evident. Any attempt to modify a historical GL entry breaks the cryptographic hash chain and is detectable by the Finance Director or OAG auditor running the hash chain verification report.

The database backup policy (FR-SYS-005) requires daily full backups completing within ≤ 4 hours, with a retention period for backups aligned to the 7-year statutory requirement. Backup storage is on BIRDC's own infrastructure (DC-006).

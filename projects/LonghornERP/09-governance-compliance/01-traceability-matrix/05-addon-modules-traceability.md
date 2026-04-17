# 5. Add-On Module Requirements Traceability

This section covers the 10 add-on modules available as per-subscription activations. All FRs in this section are flagged `[TRACE-GAP-TC]` unless a test case is explicitly cited. The central test plan does not currently include test cases for add-on modules.

*Note on modules without dedicated traceability files: Manufacturing (`FR-MFG-*`) and Sales CRM (`FR-CRM-*`) do not have `09-traceability.md` files; FR identifiers were extracted from the SRS body. These are flagged `[SRS-GAP]` in addition to `[TRACE-GAP-TC]`.*

## 5.1 HR and Payroll (FR-HR-*)

*Source: `02-requirements-engineering/01-srs/01-modules/05-hr-payroll/12-traceability.md`*

*The HR SRS traceability file uses range notation. BG mapping: HR BG-001 (payroll and statutory compliance) → PRD BG-002; BG-003 (leave/self-service) → PRD BG-001; BG-004 (audit readiness) → PRD BG-002.*

*Test cases TC-HR-001 through TC-HR-007 are defined in the test plan. All others are flagged TC-PENDING.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-HR-001 | Create employee master record with mandatory fields | BG-001, BG-002 | TC-HR-001 | |
| FR-HR-002 | Enforce employee ID uniqueness | BG-001 | TC-HR-002 | |
| FR-HR-003 | Assign employee to department and position | BG-001 | TC-HR-003 | |
| FR-HR-004 | Org chart hierarchy maintenance | BG-001 | TC-HR-004 | |
| FR-HR-005 | Grade and pay scale configuration | BG-001, BG-002 | TC-HR-005 | |
| FR-HR-006 | Employee contract records with start/end dates | BG-001 | TC-HR-006 | |
| FR-HR-007 | Employee record audit log | BG-001, BG-002 | TC-HR-007 | |
| FR-HR-008 | Employee photo and document attachments | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-009 | Employee soft-delete with history preservation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-010 | Leave type configuration (annual, sick, maternity) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-011 | Leave balance accrual calculation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-012 | Leave request submission by employee | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-013 | Leave approval workflow (manager → HR) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-014 | Leave balance update on approval | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-015 | Leave calendar view | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-016 | Public holiday configuration per profile | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-017 | Leave carry-forward per leave type rules | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-018 | Leave encashment calculation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-019 | Attendance record capture (manual and biometric) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-020 | Biometric device integration (Zkteco) | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-021 | Shift schedule definition and assignment | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-022 | Overtime calculation per shift policy | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-023 | Absence and late arrival recording | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-024 | Attendance report by department and period | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-025 | Attendance summary fed to payroll run | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-026 | Payroll element definition (earnings, deductions) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-027 | Element assignment to employee | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-028 | Pay period configuration (monthly, bi-monthly) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-029 | Payroll element effective dates | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-030 | Formula-based element calculation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-031 | Retroactive pay adjustment | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-032 | Fixed and variable element distinction | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-033 | Payroll run initiation for a period | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-034 | Net pay formula: Gross − Statutory − Voluntary deductions | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-035 | NSSF contribution calculation (employer + employee) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-036 | PAYE calculation per jurisdiction band array | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-037 | Multi-jurisdiction PAYE support (KE, TZ, RW) | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-038 | Payroll run preview before confirmation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-039 | Payroll run confirmation and lock | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-040 | GL journal posted on payroll run confirmation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-041 | Payroll run audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-042 | Payslip generation per employee | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-043 | Payslip PDF generation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-044 | Payslip email delivery to employee | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-045 | NSSF employer contribution schedule export | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-046 | PAYE e-return export for URA | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-047 | Net salary disbursement via mobile money | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-048 | Disbursement confirmation recorded per employee | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-049 | Failed disbursement retry and exception report | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-050 | Staff loan registration | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-051 | Loan repayment schedule generation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-052 | Auto-deduct loan repayment from payroll | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-053 | Salary advance recording | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-054 | Advance recovery from next payroll | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-055 | Loan and advance report | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-056 | Cap deduction at net pay; carry forward | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-057 | Exit management process initiation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-058 | Terminal benefit calculation (gratuity, notice pay) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-059 | Exit clearance checklist | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-060 | Final payslip with terminal benefits | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-061 | Employee record archived on exit | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-062 | Re-employment history preserved | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-063 | Employee self-service portal login | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-064 | Employee views own payslips | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-065 | Employee submits leave request via portal | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-066 | Employee views own leave balance | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-067 | Employee updates personal details | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-068 | Employee views own loan/advance schedule | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-HR-069 | Portal access restricted to own records only | BG-002, BG-006 | TC-PENDING | [TRACE-GAP-TC] |

## 5.2 Point of Sale (FR-POS-*)

*Source: `02-requirements-engineering/01-srs/01-modules/06-pos/08-traceability.md`*

*The POS SRS traceability file uses range notation. BG mapping: POS BG-001 (sales and GL accuracy) → PRD BG-001, BG-004; BG-002 (till management) → PRD BG-004; BG-003 (stock accuracy) → PRD BG-001; BG-004 (offline resilience) → PRD BG-001, BG-005.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-POS-001 | POS terminal registration with unique terminal ID | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-002 | Terminal assigned to branch and till | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-003 | Multi-terminal support per branch | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-004 | Restaurant/table mode configuration | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-005 | Table assignment to terminal | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-006 | Table status tracking (available/occupied/reserved) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-007 | Terminal deactivation | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-008 | Terminal configuration audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-009 | Per-terminal receipt numbering | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-010 | Terminal licence consumption per subscription plan | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-011 | Terminal hardware configuration (printer, drawer, scanner) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-012 | Terminal remote diagnostics | BG-001, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-013 | New basket opened per transaction | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-014 | Item added by barcode, code, or name search | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-015 | Price resolved from active price list | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-016 | Quantity and discount editable per basket line | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-017 | VAT auto-applied per item tax code | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-018 | Total, subtotal, and tax displayed in real time | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-019 | Hold and resume basket | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-020 | Basket void with reason | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-021 | Sales transaction posted on payment confirmation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-022 | Stock movement deducted on sale | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-023 | GL posting on sale: Revenue, VAT, AR/Cash | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-024 | Receipt printed and/or emailed on sale | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-025 | EFRIS fiscal receipt submitted on Uganda sale | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-026 | EFRIS QR code printed on receipt | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-027 | Real-time stock deduction (no negative stock default) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-028 | Till session opened with float amount | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-029 | Customer display of basket total | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-030 | Accept cash payment with change calculation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-031 | Accept card payment (POS terminal integration) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-032 | Accept mobile money payment (MTN MoMo, Airtel, M-Pesa) | BG-001, BG-003, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-033 | Accept customer account payment (invoice to AR) | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-034 | Split payment across multiple methods | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-035 | Accept credit note as payment | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-036 | Payment reversal with reason (supervisor override) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-037 | Reversal posts counter GL entries | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-038 | Refund to original payment method | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-039 | Cash rounding applied per profile | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-040 | Foreign currency accepted per profile | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-041 | Till session closed with counted cash amount | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-042 | X-report (mid-session summary) generated | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-043 | Z-report (end-of-session final report) generated | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-044 | Cash variance calculated (counted − expected) | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-045 | Cash variance formula: counted_cash − (float + cash_sales − cash_payouts) | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-046 | Till handover between cashiers | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-047 | Cashier performance report | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-048 | Till session locked after Z-report | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-049 | GL posting on till session close | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-050 | Bank deposit recorded against session cash | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-051 | Multiple sessions per terminal per day | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-052 | Offline mode auto-activated on network loss | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-053 | Local SQLite cache stores basket and payments offline | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-054 | Transaction queue persisted through power cycle | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-055 | Auto-sync queue on network restoration | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-056 | Conflict resolution for offline duplicates | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-057 | Cash payment only accepted offline (no mobile money) | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-058 | Offline receipt printed with pending sync indicator | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-059 | Stock deducted from local cache offline | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-060 | Offline mode time limit enforced (configurable) | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-061 | EFRIS submission queued offline; submitted on sync | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-062 | Offline database encrypted with AES-256 | BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-POS-063 | Sync status visible to cashier | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |

## 5.3 Advanced Inventory (FR-ADVINV-*)

*Source: `02-requirements-engineering/01-srs/01-modules/07-advanced-inventory/09-traceability.md`*

*BG mapping: BG-001 (financial valuation) → PRD BG-002; BG-002 (supply chain) → PRD BG-001; BG-003 (batch/serial traceability) → PRD BG-001, BG-002; BG-004 (cold chain / compliance) → PRD BG-002.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-ADVINV-001 | Multi-location warehouse management | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-002 | Bin-level stock tracking | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-003 | Multi-location stock balance inquiry | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-004 | Inter-location replenishment transfer | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-005 | Transfer request approval workflow | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-006 | Transfer GL posting (inter-branch) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-007 | Transfer in transit stock tracking | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-008 | Transfer discrepancy recording | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-009 | Batch/lot number creation on receipt | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-010 | Batch attributes: manufacture date, expiry, supplier lot | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-011 | Batch ledger with full movement history | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-012 | Agro-processing batch fields (farm intake, moisture) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-013 | Batch cost layer maintained per lot | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-014 | Batch split for processing runs | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-015 | Batch merge with audit trail | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-016 | Serial number assigned on goods receipt | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-017 | Serial number uniqueness enforced per tenant | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-018 | Serial number ledger tracking every custody transfer | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-019 | Serial number mandatory on sales delivery of serialised items | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-020 | Warranty expiry tracked per serial number | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-021 | Serial number trace report (full custody chain) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-022 | FEFO picking enforced for expiry-tracked items | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-023 | Expiry date alert (configurable days before expiry) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-024 | Near-expiry report by warehouse | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-025 | Expired batch auto-quarantine | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-026 | FEFO picking slip with batch expiry dates | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-027 | POS FEFO gate: block sale of expired items | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-028 | Expiry status dashboard | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-029 | Landed cost allocation across GRN lines (advanced) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-030 | Multiple landed cost components per GRN | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-031 | Landed cost allocation methods (value, weight, quantity, volume) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-032 | Landed cost variance report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-033 | Landed cost reversal on GRN return | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-034 | Inter-branch transfer with landed cost | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-035 | Custom clearance charges recorded on import GRN | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-036 | Available-to-promise (ATP) calculation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-037 | Soft reservation on sales order confirmation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-038 | Reservation released on order cancellation or delivery | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-039 | Product recall initiation by batch or serial number | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-040 | Recall trace report (all customers who received recalled items) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-041 | Recall status tracking (initiated, notified, returned) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-042 | Cold chain temperature recording per batch | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-043 | Temperature excursion alert and quarantine | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ADVINV-044 | UNBS and food safety compliance fields on batch | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |

## 5.4 Manufacturing (FR-MFG-*)

*Source: `02-requirements-engineering/01-srs/01-modules/08-manufacturing/` (body files — no dedicated traceability file)*

*`[SRS-GAP]`: No `09-traceability.md` exists. FR identifiers extracted from body files. Traceability file must be authored.*

*BG mapping: All manufacturing FRs map to PRD BG-001 (replace manual processes) and PRD BG-004 (financial visibility via COGS and costing).*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-MFG-001 | Create BOM with unique BOM ID, version, and effective dates | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-002 | BOM line records component, quantity, UOM, wastage, phantom flag | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-003 | Gross required quantity computed: $GrossQty = NetQty \div (1 - WastageRate)$ | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-004 | Multi-level BOM (max 5 levels); circular reference detection | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-005 | Uganda agro-processing BOM starter templates | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-006 | Agro-processing BOM template fields (intake batch, milling ratio, moisture) | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-007 | Standard cost roll-up: $StandardCost = \sum (ComponentCost_i \times GrossQty_i)$ | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-008 | BOM cost explosion report | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-009 | Production Order created from BOM | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-010 | Production Order status workflow (Draft → In Progress → Completed) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-011 | Material requirements plan generated from Production Order | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-012 | Stock availability check before Production Order confirmation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-013 | Production Order variance (planned vs. actual) tracked | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-014 | Production Order audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-015 | Raw material issued against Production Order | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-016 | Issue transaction deducts from raw material inventory | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-017 | Wastage recorded on issue | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-018 | FIFO/FEFO issue of raw materials from inventory | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-019 | Issue movement linked to Production Order | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-020 | Material consumption variance report | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-021 | WIP stock movement created on Production Order start | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-022 | QC inspection step before finished goods receipt | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-023 | QC pass/fail recorded per Production Order | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-024 | Failed QC triggers rework or scrap workflow | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-025 | QC results audit trail | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-026 | Finished goods receipt posted to inventory | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-027 | WIP cost transferred to finished goods on receipt | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-028 | By-product receipt recorded with separate item code | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-029 | By-product value split from main production run cost | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-030 | GL journal posted on finished goods receipt | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-031 | Actual manufacturing cost calculation per Production Order | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-032 | Overhead allocation per configurable absorption rate | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-033 | Labour cost captured per Production Order | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-034 | Standard vs. actual cost variance report | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-035 | Cost variance journal posted | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-036 | Scrap recording with reason code | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-037 | Scrap GL posting (write-off to scrap expense) | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-038 | Scrap report by Production Order and period | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-039 | Scrap salvage value recorded | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-040 | Production schedule view (Gantt-style) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-041 | Capacity utilisation indicator per work centre | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-042 | Work centre definition and machine hours | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-043 | Machine downtime recording | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-044 | Production efficiency report (actual vs. planned hours) | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-MFG-045 | Production Order linked to Cooperative intake batch | BG-001, BG-003 | TC-PENDING | [TRACE-GAP-TC] |

## 5.5 Sales CRM (FR-CRM-*)

*Source: `02-requirements-engineering/01-srs/01-modules/09-sales-crm/` (body files — no dedicated traceability file)*

*`[SRS-GAP]`: No `09-traceability.md` exists. FR identifiers extracted from body files. Traceability file must be authored.*

*BG mapping: CRM FRs map primarily to PRD BG-001 (replace manual sales pipeline management) and BG-004 (pipeline visibility and forecasting).*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-CRM-001 | Create lead record with source, status, and assigned rep | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-002 | Lead status lifecycle (New → Contacted → Qualified → Disqualified) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-003 | Lead source tracking (web, referral, event) | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-004 | Lead assignment to sales rep or team | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-005 | Lead conversion to Opportunity | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-006 | Lead activity history | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-007 | Duplicate lead detection by phone or email | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-008 | Lead import via CSV | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-009 | Lead report by source and rep | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-010 | Create Opportunity with expected value and close date | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-011 | Opportunity pipeline stage progression | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-012 | Configurable pipeline stages per tenant | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-013 | Opportunity probability by stage | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-014 | Link Opportunity to existing Customer | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-015 | Convert Opportunity to Quotation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-016 | Opportunity close date change history | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-017 | Pipeline Kanban board view | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-018 | Pipeline list view with sort and filter | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-019 | Create activity (call, email, meeting, task) against lead or opportunity | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-020 | Activity due date and reminder | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-021 | Activity completion with outcome note | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-022 | Activity calendar view | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-023 | Overdue activity alert to rep and manager | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-024 | Activity history per lead and opportunity | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-025 | Create Contact record independent of opportunity | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-026 | Link Contact to Customer record | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-027 | Contact communication history | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-028 | Contact search by name, company, phone | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-029 | Sales forecast by rep and period | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-030 | Weighted forecast calculation: value × probability | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-031 | Forecast vs. actual comparison report | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-032 | Territory definition and assignment | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-033 | Territory-based opportunity routing | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-034 | Territory performance report | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-035 | Lost deal reason capture | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-036 | Lost deal report by reason and rep | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-037 | Win rate calculation per rep and period | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-038 | Customer satisfaction score (NPS) survey trigger | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-039 | NPS response recording | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-040 | NPS aggregate report by period | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-041 | CRM dashboard (pipeline value, activity count, win rate) | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-CRM-042 | CRM data export to Excel | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |

## 5.6 Sales Agents (FR-AGENT-*)

*Source: `02-requirements-engineering/01-srs/01-modules/10-sales-agents/09-traceability.md`*

*BG mapping: Agent BG-01 (agent management) → PRD BG-001; BG-02 (mobile money payments) → PRD BG-005; BG-03 (agent portal) → PRD BG-005; BG-04 (commission rules) → PRD BG-001; BG-05 (audit/compliance) → PRD BG-002; BG-06 (stock-on-consignment) → PRD BG-001; BG-07 (territory management) → PRD BG-001.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-AGENT-001 | Create agent record with unique Agent ID | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-002 | Deactivate agent; block new attributions | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-003 | Audit trail on agent record updates | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-004 | Profile photo upload and resize to 256×256 | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-005 | Agent search by name, ID, phone within 1 second | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-006 | Territory assignment to agent | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-007 | Territory reassignment with history preserved | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-008 | Territory map view (renders within 3 s) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-009 | Product assignment restricts attribution to assigned products | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-010 | Product removal preserves historical attribution records | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-011 | Sales target creation with duplicate guard per period | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-012 | Bulk target CSV import (500-row performance test) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-013 | Target Achievement % formula and update latency | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-014 | Automatic target period closure at end date | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-015 | Auto attribution on invoice post | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-016 | Manual attribution with audit | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-017 | Re-attribution rules; lock after run finalisation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-018 | Split attribution validated to sum to 100% | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-019 | Attribution report: 90-day at 10,000 records within 3 s | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-020 | Attribution exception logged for unassigned products | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-021 | Commission rule creation with overlap guard | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-022 | Rule ID assigned; rule available in run configuration | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-023 | Rule deactivation; existing run values intact | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-024 | Flat rate commission formula | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-025 | Tiered rate commission with correct tier and amount | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-026 | Tiered rule gap and range validation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-027 | Cumulative tiered rate marginal calculation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-028 | Product-specific commission rate formula | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-029 | Missing-rate exclusion and exception log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-030 | Agent-level rule override with audit flag | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-031 | Commission run initiation with duplicate guard | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-032 | Commission run batch: 500 agents within 120 s | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-033 | Commission run summary accessible within 5 s | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-034 | Commission run exception CSV export | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-035 | Approver notified within 5 minutes on run submission | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-036 | Commission run approval and lock (irreversible) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-037 | Commission run rejection with reason | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-038 | Pre-payment MoMo number validation; missing excluded | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-039 | Bulk MoMo payment batch submission | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-040 | MoMo callback processing; per-agent status within 60 s | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-041 | Failed MoMo payment retry (max 3 attempts) | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-042 | Run closure report PDF generated within 10 s | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-043 | Portal authentication with 5-failure lockout | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-044 | Portal data isolation (cross-agent request returns 403) | BG-002, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-045 | Agent sales list: 1,000 records within 2 s | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-046 | Sales date filter with total within 2 s | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-047 | Commission run history visible from agent join date | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-048 | Commission breakdown detail with tier rows | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-049 | PDF commission statement generated within 10 s | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-050 | Target progress % with latency ≤ 5 minutes | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-051 | Target milestone notifications at 80%, 100%, 120% | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-052 | Agent payment notification within 5 minutes of Paid status | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-053 | Stock issued to agent; main ledger decremented | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-054 | Agent stock return (good and damaged) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-055 | Agent stock balance formula: issued − attributed_sales − returned | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-056 | Stock reorder alert when balance below threshold | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-057 | Stock reconciliation variance requires approval before posting | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-058 | Remittance recording; MoMo reference mandatory | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-059 | Remittance variance and tolerance gate | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-060 | Verified remittance posts receipt entry and reduces invoice balance | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-061 | Overdue remittance flagged and daily notification sent | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-AGENT-062 | Daily activity summary generated at 23:45 EAT per active agent | BG-001 | TC-PENDING | [TRACE-GAP-TC] |

## 5.7 Cooperative Management (FR-COOP-*)

*Source: `02-requirements-engineering/01-srs/01-modules/11-cooperative/09-traceability.md`*

*BG mapping: BG-COOP-01 (farmer registry/config) → PRD BG-001; BG-COOP-02 (pricing/payments) → PRD BG-004; BG-COOP-03 (MoMo payments) → PRD BG-005; BG-COOP-04 (offline mobile) → PRD BG-005; BG-COOP-05 (statements/audit) → PRD BG-002.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-COOP-001 | Create commodity type record | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-002 | Reject duplicate commodity name | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-003 | Deactivate commodity without data loss | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-004 | Add grade to commodity | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-005 | Deactivate grade with batch warning | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-006 | Assign grade price to season | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-007 | Enforce floor price on intake | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-008 | Apply price change prospectively | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-009 | Premium price calculation | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-010 | Seasonal intake window auto-open/close | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-011 | Farmer record creation with NIN validation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-012 | Reject duplicate NIN | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-013 | Farmer record audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-014 | GPS coordinate validation and storage | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-015 | Mobile GPS auto-capture | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-016 | Farmer payment method registration | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-017 | MoMo phone number prefix validation | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-018 | Group creation in hierarchy | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-019 | Primary society creation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-020 | Union creation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-021 | Hierarchy tree view with record counts | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-022 | KTDA and NAEB jurisdiction configuration | BG-002, BG-003 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-023 | Activate intake session for season | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-024 | Close intake period with supervisor PIN | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-025 | Period closure summary generation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-026 | Intake entry recorded with gross payment | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-027 | Reject zero or negative weight | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-028 | Reject intake for unregistered farmer | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-029 | Multiple-intake-per-day warning | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-030 | RS-232 weighbridge weight capture | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-031 | Weighbridge timeout fallback to manual entry | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-032 | Unstable weight rejected | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-033 | Weighbridge configuration settings | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-034 | Batch posting to Inventory and Accounting | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-035 | Block posting of flagged batch entries | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-036 | Auto-apply input loan deductions | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-037 | Cap deduction at gross payment; carry forward | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-038 | Close loan on full repayment | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-039 | Register new input loan | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-040 | Compute and apply levy deductions | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-041 | Separate society and union levy lines | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-042 | Levy configuration | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-043 | Levy deactivation prospective effect | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-044 | Bulk payment batch generation | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-045 | Submit payment instructions to MoMo API | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-046 | Handle MoMo success and failure callbacks | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-047 | MoMo API timeout handling | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-048 | Batch reconciliation and journal posting | BG-004, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-049 | Individual farmer statement generation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-050 | PDF farmer statement with cooperative branding | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-051 | Bulk statement generation (up to 500 farmers) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-052 | Seasonal summary report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-053 | Seasonal summary Excel export | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-054 | Society performance report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-055 | Levy collection report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-056 | Market price with floor price enforcement | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-057 | Price history audit trail | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-058 | Minimum support price override warning | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-059 | Offline mode auto-activation on network loss | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-060 | 72-hour offline limit warning and lock | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-061 | Encrypted local offline entry storage | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-062 | Auto-sync on connectivity restoration | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-063 | Conflict resolution for duplicate offline entries | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-064 | Interrupted sync resumption without duplicates | BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-COOP-065 | Offline database encryption and remote wipe | BG-005, BG-006 | TC-PENDING | [TRACE-GAP-TC] |

## 5.8 Project Management (FR-PROJ-*)

*Source: `02-requirements-engineering/01-srs/01-modules/12-projects/09-traceability.md`*

*BG mapping: BG-PROJ-001 (project planning) → PRD BG-001; BG-PROJ-002 (project P&L) → PRD BG-004; BG-PROJ-003 (sector compliance) → PRD BG-002; BG-PROJ-004 (automated billing) → PRD BG-004; BG-PROJ-005 (portfolio visibility) → PRD BG-004.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-PROJ-001 | Create project master record with mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-002 | Reject duplicate Project Code | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-003 | Reject End Date earlier than Start Date | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-004 | Restrict field edits after transactions posted | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-005 | Close project with outstanding items confirmation modal | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-006 | Enforce project lifecycle state transitions | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-007 | Display context-sensitive fields by project type | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-008 | Display PPDA informational banner for Government projects | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-009 | Define project budget lines by cost category | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-010 | Compute and display total project budget in real time | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-011 | Visual budget utilisation indicator (amber at 85%, red at 100%) | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-012 | Full audit trail on project master record changes | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-013 | Require active client for Commercial/Construction projects | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-014 | Display Client Projects count on Sales client record | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-015 | Create WBS task with mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-016 | Enforce maximum 4 levels of WBS nesting | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-017 | Warn when marking parent task complete with incomplete children | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-018 | Cancel draft timesheets on task cancellation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-019 | Persist WBS task sort order after reorder | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-020 | Define Finish-to-Start dependencies; reject circular dependencies | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-021 | Warn on predecessor/successor date conflict | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-022 | Create milestone with required fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-023 | Trigger billing workflow on milestone achievement | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-024 | Auto-set milestone to Missed when Due Date passes | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-025 | Display chronological milestone timeline | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-026 | Create timesheet line with mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-027 | Reject timesheet lines exceeding 24 hours per day | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-028 | Reject timesheet entry against Closed/Cancelled project | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-029 | Display weekly timesheet grid view | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-030 | Route submitted timesheets to Project Manager for approval | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-031 | Set timesheet line to Approved; appear in cost aggregation | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-032 | Reject timesheet line with mandatory reason; notify employee | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-033 | Lock Draft timesheets at period end | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-034 | Maintain employee billing rate records with effective dates | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-035 | Apply effective-date billing rate; flag missing rates | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-036 | Project-level billing rate override per employee | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-037 | Create resource allocation record with required fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-038 | Display resource utilisation summary with % | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-039 | Flag overlapping project allocations | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-040 | Resource Utilisation Report with filters and export | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-041 | Aggregate project costs from Procurement, Payroll, and Expenses | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-042 | Reverse cost ledger entry on source document reversal | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-043 | Display project cost summary by category with utilisation % | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-044 | Compute T&M billing from approved billable timesheets | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-045 | Send confirmed T&M billing to Sales as draft invoice | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-046 | Prevent double-billing of timesheet lines | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-047 | Generate milestone invoice on billing milestone achievement | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-048 | Display Billing Schedule with invoice references | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-049 | Compute Project P&L: Revenue − Costs | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-050 | Display structured P&L with gross margin % | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-051 | Auto-refresh Project P&L within ≤ 5 s on new cost/invoice | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-052 | Export Project P&L to Excel and PDF | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-053 | Create project subcontractor record with required fields | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-054 | Compute total subcontract value | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-055 | Link PO to subcontractor; enforce supplier match | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-056 | Display subcontractor cost summary with paid/outstanding | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-057 | Auto-update subcontractor Paid to Date on payment confirmation | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-058 | Warn when payments reach subcontract ceiling | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-059 | Display PPDA compliance warning for Government project subcontractors | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-060 | Allow document attachments on subcontractor records | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-061 | Generate Subcontractor Compliance Report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-062 | Compute and deduct retention per invoice | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-063 | Maintain running Retention Ledger | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-064 | Release full retention on project close | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-065 | Support partial retention release | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-066 | Display Donor & Grant panel with utilisation on NGO project | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-067 | Define grant budget lines per NGO project | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-068 | Tag project cost entries with grant budget line | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-069 | Generate Donor Expenditure Report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-070 | Support logframe document upload on NGO project | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-071 | Render Gantt chart with tasks, milestones, dependencies | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-072 | Gantt chart renders within ≤ 3 s for 200-task project | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-073 | Export Gantt chart to PDF | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-074 | Display Portfolio Dashboard with all active projects | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-075 | Compute portfolio Health Indicator per defined rules | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-076 | Filter Portfolio Dashboard and export | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROJ-077 | Display Portfolio Summary aggregate figures | BG-004 | TC-PENDING | [TRACE-GAP-TC] |

## 5.9 Strategy and Balanced Scorecard (FR-BSC-*)

*Source: `02-requirements-engineering/01-srs/01-modules/13-strategy-bsc/09-traceability.md`*

*BG mapping: BG-BSC-001 (strategy definition/monitoring) → PRD BG-001; BG-BSC-002 (ERP data feeds) → PRD BG-004; BG-BSC-003 (NGO/logframe/NDP III) → PRD BG-002; BG-BSC-004 (audit) → PRD BG-002; BG-BSC-005 (board reports) → PRD BG-004.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-BSC-001 | Create/update mission and vision statements | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-002 | Create strategic theme with name, description, and colour | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-003 | Edit theme; block deletion of theme with active objectives | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-004 | Display themes as colour-coded filter chips on dashboard | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-005 | Pre-populate 4 default BSC perspectives at module activation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-006 | Rename, reorder, toggle, and block deletion of perspective | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-007 | Create custom perspective; enforce max 8 active perspectives | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-008 | Hide perspectives in OKR mode; restore on revert | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-009 | Set framework mode (BSC / OKR / Hybrid) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-010 | Audit log on framework mode change | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-011 | Create strategic objective with mandatory fields; assign OBJ-NNNN | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-012 | Require change reason on title/period edit when actuals exist | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-013 | Manage objective status; block deletion if KPIs or initiatives linked | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-014 | Display objectives grouped by perspective, sortable | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-015 | Create KPI with mandatory fields; assign KPI-NNNN ID | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-016 | Define KPI formula with ERP token validation | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-017 | Set numeric target and baseline per period | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-018 | Configure RAG thresholds; enforce red < amber ordering | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-019 | Display KPI detail panel with all 11 specified fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-020 | Inverse-polarity KPI scoring | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-021 | Enforce exactly-1 objective linkage per KPI | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-022 | Aggregate objective score as unweighted mean of linked KPI scores | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-023 | Manual actual entry with period, comment, source = manual | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-024 | Recalculate score and RAG within ≤ 3 s of manual entry | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-025 | Block manual entry on Auto-Pull KPIs | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-026 | Allow strategy.admin to edit/delete manual actual; audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-027 | Auto-pull GL KPI actuals; source = auto_gl | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-028 | Apply period filter when querying GL data | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-029 | Auto-pull HR KPI actuals; source = auto_hr | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-030 | Auto-pull Sales KPI actuals; source = auto_sales | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-031 | Auto-pull Projects KPI actuals; source = auto_proj | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-032 | Generate data collection task; mark Overdue after 5 business days | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-033 | Data Collection Status screen with filters | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-034 | KPI score formula: (Actual/Target) × 100, capped at 200% | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-035 | Assign RAG status per thresholds; No Data for missing actuals | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-036 | Aggregate objective RAG based on objective score | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-037 | Perspective RAG by majority rule | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-038 | Dashboard renders within ≤ 2 s at P95 under 50 sessions | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-039 | Dashboard presents all required elements without scroll at 1920×1080 | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-040 | Dashboard filter updates within ≤ 1 s without page reload | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-041 | Scorecard Summary Banner with period selector | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-042 | Consistent RAG colour codes throughout UI | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-043 | WCAG 2.1 AA accessible text label on RAG indicators | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-044 | 3-level drill-down with breadcrumb navigation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-045 | Create strategic initiative; assign INIT-NNNN ID | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-046 | Initiative status transitions; require reactivation reason | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-047 | Calculate and display budget variance on initiative | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-048 | Display linked initiatives on objective detail screen | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-049 | Initiatives section on dashboard with RAG-style status indicators | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-050 | Initiative status update stored as immutable record | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-051 | Display chronological status update history | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-052 | Generate executive PDF report with all specified sections | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-053 | PDF generation within ≤ 15 s at P95; 90-day archive | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-054 | Activate OKR mode; replace perspective hierarchy on dashboard | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-055 | Create OKR Objective; assign OKR-OBJ-NNNN ID | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-056 | Add up to 5 Key Results per OKR Objective | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-057 | Key Result progress score formula; Binary and inverse variants | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-058 | OKR Objective confidence score as mean of KR scores | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-059 | Weekly OKR check-in stored as immutable record | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-060 | Activate Logframe mode; 4-level hierarchy; coexist with BSC/OKR | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-061 | Define Logframe Matrix entries at all 4 levels | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-062 | Link Logframe Output/Outcome to BSC or OKR objective | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-063 | Record actual indicator values against Logframe entries | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-064 | Read-only NDP III reference data set; searchable | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-065 | Map tenant KPI to NDP III indicator; NDP III Alignment Report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-066 | Create department workplan; assign WP-DEPT-NNNN ID | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-067 | Record activity completion status and percentage | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-BSC-068 | Display Strategic Alignment indicator on workplan activities | BG-001 | TC-PENDING | [TRACE-GAP-TC] |

## 5.10 Asset Management (FR-ASSET-*)

*Source: `02-requirements-engineering/01-srs/01-modules/14-assets/09-traceability.md`*

*BG mapping: BG-ASSET-001 (lifecycle accountability) → PRD BG-001; BG-ASSET-002 (IAS 16/12 compliance) → PRD BG-002; BG-ASSET-003 (URA tax compliance) → PRD BG-002; BG-ASSET-004 (verification/QR) → PRD BG-001; BG-ASSET-005 (fleet) → PRD BG-001.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-ASSET-001 | Create asset master record; auto-generate ASSET-{YYYY}-{NNNNNN} | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-002 | Reject asset creation with missing mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-003 | Audit log on asset master edit | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-004 | Lock acquisition cost and date after depreciation posted | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-005 | Restrict status change to Disposal workflow only | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-006 | Create asset category with depreciation defaults and GL mappings | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-007 | Pre-populate asset depreciation fields from category defaults | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-008 | Apply category default rate changes prospectively only | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-009 | Block deletion of category with active assets | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-010 | Auto-generate QR code on asset record creation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-011 | Generate printable QR label PDF batch | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-012 | Mobile QR scan retrieves asset master record within 3 s | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-013 | Compute straight-line monthly depreciation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-014 | Compute reducing balance monthly depreciation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-015 | Cap depreciation charge at residual value ceiling | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-016 | Monthly depreciation run — atomic GL posting | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-017 | Depreciation run summary screen | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-018 | Reject duplicate depreciation run for same period | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-019 | Pro-rate first-period depreciation on mid-period acquisition | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-020 | GL journal structure for depreciation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-021 | Abort depreciation run on GL posting failure | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-022 | Depreciation journal tagged with source module and run reference | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-023 | Block reversal of depreciation run in Hard Closed period | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-024 | Reverse depreciation run in Open or Soft Closed period | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-025 | Post upward revaluation with Revaluation Reserve credit | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-026 | Reverse prior P&L loss before crediting Revaluation Reserve | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-027 | Post downward revaluation to Profit and Loss | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-028 | Use Revaluation Reserve before debiting P&L on downward revaluation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-029 | Require revaluation basis note | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-030 | Disposal by sale — mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-031 | Write-off disposal — mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-032 | GL journal structure for disposal | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-033 | Set asset status to Disposed after disposal | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-034 | Transfer Revaluation Reserve to Retained Earnings on disposal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-035 | Reverse disposal with approval | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-036 | Initiate inter-branch transfer with mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-037 | GL journal for inter-branch transfer | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-038 | Rollback transfer on GL posting failure | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-039 | Update asset master and log transfer history | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-040 | Custodian change audit log (no GL entry) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-041 | Display full custodian change history | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-042 | Configure maintenance schedule | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-043 | Auto-generate work order and notify when due date reached | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-044 | Recompute future work orders on schedule change | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-045 | Work order state machine and completion fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-046 | Optional GL posting for work order cost | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-047 | Maintenance history list on asset detail | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-048 | Create insurance policy record | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-049 | Compute days-to-expiry; flag Expiring Soon at ≤ 30 days | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-050 | Notify Asset Manager on Expiring Soon status | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-051 | Set policy to Expired; flag asset after expiry | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-052 | Renew insurance policy and clear Expired flag | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-053 | Insurance Expiry Report with ≤ 90-day filter | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-054 | Create physical verification session | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-055 | Record asset scan during verification session | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-056 | Flag Location Mismatch when scanned location differs from register | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-057 | Generate Physical Verification Discrepancy Report on session close | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-058 | URA tax depreciation rate field on asset category | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-059 | Compute and store both book and tax depreciation per run | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-060 | Post deferred tax GL journal on depreciation run | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-061 | Book vs. Tax Depreciation Report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-062 | Apply URA rate changes prospectively | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-063 | Fleet data fields on Vehicle Fleet category assets | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-064 | Record mileage log entry and update cumulative mileage | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-065 | Record fuel log and compute fuel efficiency | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-066 | Record vehicle service record linked to maintenance history | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-067 | Trigger work order and notification near service threshold | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ASSET-068 | Fleet Utilisation Report | BG-001 | TC-PENDING | [TRACE-GAP-TC] |

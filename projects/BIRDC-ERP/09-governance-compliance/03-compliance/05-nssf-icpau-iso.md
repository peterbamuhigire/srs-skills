# Section 5: NSSF, ICPAU, ISO 22000, and OAG Compliance

## 5.1 NSSF Act Compliance

### 5.1.1 Legal Obligation

The Uganda National Social Security Fund Act requires BIRDC to deduct NSSF contributions from employee salaries and remit the combined employer and employee contributions monthly to NSSF Uganda. The employer contribution rate is 10% of gross salary; the employee contribution rate is 5% of gross salary.

### 5.1.2 System Implementation

FR-PAY-003 calculates NSSF contributions for every employee in the payroll run:

- Employee deduction: $NSSF_{employee} = GrossSalary \times 0.05$
- Employer contribution: $NSSF_{employer} = GrossSalary \times 0.10$
- Total monthly NSSF remittance: $NSSF_{total} = NSSF_{employee} + NSSF_{employer}$

Both rates are stored in a configuration table (DC-002) and can be updated by the Finance Director via the UI if Parliament amends the NSSF Act rates.

FR-PAY-004 generates the NSSF remittance schedule in the exact format required by NSSF Uganda for employer bulk remittance. The schedule includes: employee name, NIN, gross salary, employee deduction, employer contribution, and total contribution per employee, with aggregate totals.

*[CONTEXT-GAP: GAP-009]: BIRDC HR must obtain the current NSSF Uganda employer contribution schedule template to confirm the exact column layout and file format required. The system will generate the schedule once the format specification is confirmed.*

The payroll GL posting (FR-PAY-009) includes the NSSF liability entries: DR Salary Expense (employer NSSF) / CR NSSF Payable; DR Employee NSSF Deduction / CR NSSF Payable.

## 5.2 ICPAU and IFRS for SMEs Compliance

### 5.2.1 Accounting Standards Obligation

ICPAU (Institute of Certified Public Accountants of Uganda) requires BIRDC's commercial financial statements to comply with IFRS for SMEs. PIBID's parliamentary accounts follow the Government of Uganda Public Finance Management Act framework. The system must support both standards simultaneously.

### 5.2.2 IFRS for SMEs Implementation (BIRDC Commercial Mode)

FR-FIN-001 implements IFRS for SMEs double-entry accounting with a hierarchical chart of accounts. The financial statement outputs mandated by FR-FIN-009 include:

- Statement of Profit or Loss and Other Comprehensive Income (P&L)
- Statement of Financial Position (Balance Sheet — IAS-format presentation)
- Statement of Cash Flows (IAS 7 — indirect method)
- Statement of Changes in Equity
- Trial Balance (internal management report)

The chart of accounts hierarchy (1,307 accounts as referenced in the features register, subject to Finance Director confirmation per [CONTEXT-GAP: GAP-012]) is structured to produce IFRS-compliant financial statements automatically by aggregating leaf-node account balances to the relevant IFRS presentation lines.

### 5.2.3 Dual-Mode Accounting Implementation

FR-FIN-002 implements dual-mode accounting (DC-004): PIBID parliamentary budget votes and BIRDC commercial IFRS accounts are tracked simultaneously. Every operational transaction is posted to both the PIBID segment and the BIRDC segment as appropriate. The Finance Director can generate:

- A BIRDC-only P&L and Balance Sheet for commercial reporting.
- A PIBID-only Budget vs. Actual statement for parliamentary reporting.
- A consolidated view showing total operations.

This satisfies the dual nature of the organisation (government initiative + commercial enterprise) without requiring parallel accounting systems.

### 5.2.4 ICPAU Audit Readiness

The hash chain integrity mechanism (FR-FIN-007, BR-013) provides ICPAU-level assurance that the financial records are tamper-evident. An ICPAU-accredited auditor conducting the annual audit can:

1. Run the hash chain verification report (all chains intact = no tampering).
2. Drill from any financial statement line to the constituent journal entries.
3. Drill from any journal entry to the originating transaction (invoice, GRN, payroll run, etc.).
4. Export any GL period in Excel or CSV format for independent recalculation.

## 5.3 ISO 22000 and Codex Alimentarius Compliance

### 5.3.1 Food Safety Management Obligation

ISO 22000:2018 (Food Safety Management Systems) is the international standard governing food safety in manufacturing and processing. BIRDC's export customers (South Korea, Saudi Arabia, Qatar, Italy, USA) require CoA documentation that aligns with both ISO 22000 principles and the relevant Codex Alimentarius standards for banana-based food products.

### 5.3.2 System Implementation

The QC module (F-012) supports ISO 22000 compliance through the following mechanisms:

**Configurable inspection templates (FR-QC-001):** The QC Manager can define inspection templates for each product type and processing stage with numeric limits, pass/fail criteria, and photo evidence requirements. These templates map directly to the HACCP (Hazard Analysis and Critical Control Points) control points required under ISO 22000.

**In-process QC checkpoints (FR-QC-003):** QC checkpoints are embedded within production job cards at each critical control point. This creates a documented record of food safety controls at every stage of processing, satisfying ISO 22000's requirement for monitoring records at CCPs.

**Batch traceability chain (FR-INV-004, FR-MFG-004, FR-QC-009):** Every product batch can be traced from raw matooke delivery (with farmer identity, GPS coordinates, and quality grade) through processing stages to the finished product CoA and export shipment. This end-to-end traceability chain satisfies both ISO 22000 §8.3 (traceability system) and Codex Alimentarius General Principles of Food Hygiene (CAC/RCP 1-1969).

**Non-Conformance Reports (FR-QC-008):** NCRs with root cause analysis and corrective action tracking satisfy ISO 22000's requirement for documented corrective actions when food safety deviations occur.

**Certificate of Analysis generation (FR-QC-004, FR-QC-005):** The system generates CoAs for domestic and export markets. Export-grade CoAs include all parameters required by each destination market's food safety authority:

| Market | Regulatory Authority | Key Parameters |
|---|---|---|
| South Korea | Ministry of Food and Drug Safety (MFDS) | [CONTEXT-GAP: GAP-010 — exact parameters pending] |
| European Union (Italy) | EU RASFF / MAAIF | [CONTEXT-GAP: GAP-010 — exact parameters pending] |
| Saudi Arabia | Saudi Food and Drug Authority (SFDA) | [CONTEXT-GAP: GAP-010 — exact parameters pending] |
| Qatar | Ministry of Public Health (MOPH) | [CONTEXT-GAP: GAP-010 — exact parameters pending] |
| United States | US Food and Drug Administration (FDA) | [CONTEXT-GAP: GAP-010 — exact parameters pending] |

The CoA template system is configurable (DC-002): the QC Manager can update parameter sets for each market via the UI when import requirements change, without developer involvement.

**Export dispatch control (FR-QC-006, BR-017):** A batch with only "Approved for Domestic" status is blocked from being allocated to an export shipment. An export-grade CoA with the destination market's parameter set must be generated and approved before the export dispatch can proceed. This hard block prevents accidental export of products that have not been certified to the destination market's standard.

## 5.4 OAG Uganda Audit Readiness

### 5.4.1 OAG Audit Obligation

The Office of the Auditor General (OAG Uganda) conducts an annual audit of PIBID's parliamentary accounts. The OAG team expects to find complete, readily accessible financial records with full source traceability, no manual reconciliation required.

### 5.4.2 What the OAG Team Will Find

When the OAG audit team arrives, the system provides the following capabilities without any preparation or data compilation by BIRDC staff:

| OAG Requirement | System Capability | FR Reference |
|---|---|---|
| Trial Balance for any period | Generated within ≤ 5 seconds without period closing | FR-FIN-008 |
| Full General Ledger detail (any account, any period) | Exportable in Excel/CSV; drillable to source transactions | FR-FIN-009, FR-SYS-003 |
| Budget vs. Actual for all parliamentary votes | Real-time report for any budget period | FR-BUD-003 |
| Hash chain integrity verification | One-click integrity check; broken chains reported immediately | FR-FIN-007 |
| Procurement register with full PPDA documentation status | Searchable, filterable, exportable | FR-ADM-002, FR-ADM-003 |
| Payroll records with PAYE and NSSF calculations | Locked, immutable payroll runs per period; exportable | FR-PAY-007 |
| Any individual transaction audit trail | Audit log searchable by user, action, date, and table; results within ≤ 5 seconds | FR-SYS-003 |
| 7-year record completeness | Retention enforcement; no gaps; hash chain verifiable | FR-SYS-004, FR-FIN-007 |

The system eliminates the manual reconciliation exercise that typically requires weeks of staff time before an OAG audit. The Finance Director can hand the audit team direct read-only access to the relevant reports with confidence that no manual compilation is necessary.

### 5.4.3 Audit Trail Exportability

FR-SYS-003 provides a searchable audit trail with results returned within ≤ 5 seconds for any 30-day period queried. The audit trail is exportable to Excel and PDF. The OAG team can query by:

- User identity (who took the action)
- Action type (create, approve, post, void, delete)
- Date range (any period within the 7-year retention window)
- Module (GL, Procurement, Payroll, etc.)
- Specific transaction identifier

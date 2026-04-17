# Section 4: Traceability Gap Analysis

## 4.1 FRs with No Test Case Assigned (TC-PENDING)

All test case identifiers in Section 1 of this RTM are designated TC-[MODULE]-[NNN] and are pre-assigned for authoring in the Test Plan (Phase 5 documentation suite). No FR in this RTM has a blank or missing test case reference. All 213 FRs have corresponding TC identifiers. The Test Plan document must author the full test case specification for each TC identifier listed in Section 1 before Phase 7 (Go-Live) can commence.

The following FRs carry open context gaps that will affect test case design until the gaps are resolved:

| FR ID | Context Gap | Impact on Testing |
|---|---|---|
| FR-SAL-003, FR-EFR-001 through FR-EFR-004 | GAP-001 — EFRIS API sandbox credentials unavailable | EFRIS integration tests cannot run until sandbox is provisioned |
| FR-AGT-009, FR-AP-006, FR-PAY-011 | GAP-002 — MTN MoMo sandbox credentials unavailable | Mobile money payment tests cannot run until sandbox is provisioned |
| FR-HR-003, FR-HR-004 | GAP-005 — ZKTeco device model and SDK version unknown | Biometric import test cannot be authored until device model is confirmed |
| FR-PAY-002 | GAP-008 — PAYE tax bands not confirmed for 2025/26 | Payroll calculation test values cannot be hardcoded until current bands are confirmed |
| FR-PAY-004 | GAP-009 — NSSF schedule format not confirmed | NSSF export test cannot verify format compliance until format specimen is received |
| FR-PRO-002, FR-ADM-001 | GAP-007 — PPDA threshold values not confirmed | Procurement approval matrix test values are pending confirmation |
| FR-QC-005, FR-QC-006 | GAP-010 — Export CoA parameters not confirmed | Export CoA format test cannot verify market compliance until parameter lists are received |
| FR-FAR-001, FR-FAR-009 | GAP-004 — DPPA legal review not completed | Farmer PII handling tests must be reviewed against legal advice before go-live |

## 4.2 Business Goals with FR Coverage Assessment

| Business Goal | FR Count | Coverage Status |
|---|---|---|
| BG-001 — Operational Unity | 89 FRs (all modules) | Fully covered |
| BG-002 — Financial Integrity | 56 FRs (FIN, AR, AP, BUD, PAY, SYS) | Fully covered |
| BG-003 — Agent Accountability | 18 FRs (POS, AGT, AR) | Fully covered |
| BG-004 — Circular Economy Visibility | 29 FRs (PRO, FAR, MFG, QC, RES) | Fully covered |
| BG-005 — Government Replicability | 14 FRs (PRO, PAY, FIN, SYS, ADM) | Fully covered |

All 5 business goals have substantive FR coverage. No business goal is unaddressed.

## 4.3 Imprest Anomaly (BR-018 Partial Coverage)

As noted in Section 2, BR-018 (Imprest Account Control) is only partially covered by existing FRs. The imprest blocking rule (disbursement rejected when balance would go below zero) and GL posting requirement for every imprest transaction lack dedicated FRs. This is the only internal gap in the BR-to-FR coverage matrix.

**Recommended remediation:** Add two FRs to the F-005 (Financial Accounting) specification:
- `FR-FIN-013`: When a requested imprest disbursement would reduce the imprest account balance below zero, the system shall reject the disbursement, display the current balance and requested amount, and require Finance Manager approval for an override.
- `FR-FIN-014`: The system shall post every imprest transaction (disbursement and replenishment) individually to the GL and generate a receipt.

## 4.4 Summary Counts

| Category | Count |
|---|---|
| Total FRs in this RTM | 213 |
| FRs fully traceable to a BG and a TC ID | 213 |
| FRs with open context gaps (TC affected) | 16 |
| Business Rules fully covered | 17 |
| Business Rules partially covered | 1 (BR-018) |
| Business Goals fully covered | 5 |
| Design Covenants fully covered | 7 |

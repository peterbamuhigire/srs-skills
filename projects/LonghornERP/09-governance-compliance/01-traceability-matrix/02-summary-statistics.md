# 2. Summary Statistics

## 2.1 Coverage Summary by Component

The table below aggregates FR counts and traceability coverage for every platform component and functional module. A requirement is considered to have a Business Goal (BG) link if it maps to at least 1 of BG-001 through BG-006. A requirement is considered to have a Test Case (TC) link if a TC identifier has been assigned in the test plan.

*Note on module-level business goals: Each SRS defines local business goal identifiers (e.g., BG-PLT-01, BG-ACCT-001) scoped to that module. For this RTM, those local goals are mapped to the 6 PRD-level business goals (BG-001 through BG-006). The mapping is documented in Sections 3, 4, and 5. FRs where the local business goal cannot be confidently mapped to a PRD goal are flagged `[TRACE-GAP-BG]`.*

| Component | FR Prefix | Total FRs | FRs with BG Link | FRs with TC Link | BG Gaps | TC Gaps |
|---|---|---|---|---|---|---|
| Multi-Tenancy and Billing | FR-PLAT | 53 | 53 | 0 | 0 | 53 |
| Role-Based Access Control | FR-RBAC | 59 | 59 | 59 | 0 | 0 |
| Audit Log | FR-AUDIT | 55 | 55 | 0 | 0 | 55 |
| Localisation and Statutory | FR-LOC | 74 | 74 | 0 | 0 | 74 |
| Mobile API | FR-MAPI | 64 | 64 | 0 | 0 | 64 |
| Integration Layer | FR-INTG | 91 | 91 | 0 | 0 | 91 |
| **Platform Subtotal** | | **396** | **396** | **59** | **0** | **337** |
| Accounting and GL | FR-ACCT | 122 | 122 | 10 | 0 | 112 |
| Inventory Management | FR-INV | 87 | 87 | 5 | 0 | 82 |
| Sales | FR-SALES | 96 | 96 | 3 | 0 | 93 |
| Procurement | FR-PROC | 51 | 51 | 0 | 0 | 51 |
| HR and Payroll | FR-HR | 69 | 69 | 7 | 0 | 62 |
| Point of Sale | FR-POS | 63 | 63 | 0 | 0 | 63 |
| Advanced Inventory | FR-ADVINV | 44 | 44 | 0 | 0 | 44 |
| Manufacturing | FR-MFG | 45 | 45 | 0 | 0 | 45 |
| Sales CRM | FR-CRM | 42 | 42 | 0 | 0 | 42 |
| Sales Agents | FR-AGENT | 62 | 62 | 0 | 0 | 62 |
| Cooperative Management | FR-COOP | 65 | 65 | 0 | 0 | 65 |
| Project Management | FR-PROJ | 77 | 77 | 0 | 0 | 77 |
| Strategy and BSC | FR-BSC | 68 | 68 | 0 | 0 | 68 |
| Asset Management | FR-ASSET | 68 | 68 | 0 | 0 | 68 |
| **Module Subtotal** | | **959** | **959** | **25** | **0** | **934** |
| **TOTAL** | | **1,355** | **1,355** | **84** | **0** | **1,271** |

## 2.2 Traceability Coverage Analysis

| Metric | Value |
|---|---|
| Total functional requirements | 1,355 |
| FRs with business goal link | 1,355 (100%) |
| FRs with assigned test case | 84 (6.2%) |
| FRs pending test case assignment | 1,271 (93.8%) |
| BG trace gaps | 0 |
| TC trace gaps | 1,271 |

## 2.3 Interpretation

**Business Goal Coverage:** All 1,355 functional requirements are mapped to at least 1 PRD business goal. No BG trace gaps exist. This confirms full upstream traceability from every requirement to a stakeholder need.

**Test Case Coverage:** The test plan (`05-testing-documentation/02-test-plan/`) was authored in parallel with this RTM and covers platform components (TC-PLAT-001 through TC-PLAT-012), accounting (TC-ACCT-001 through TC-ACCT-010), inventory (TC-INV-001 through TC-INV-005), sales (TC-SALES-001 through TC-SALES-003), and HR (TC-HR-001 through TC-HR-007). The remaining 1,271 FRs are flagged `[TRACE-GAP-TC]` and require test case assignments before the implementation phase completes.

**Remediation Action:** The test plan must be extended to cover all modules prior to the System Integration Testing (SIT) gate. The gap register in Section 6 provides the full list of `[TRACE-GAP-TC]` items.

## 2.4 SRS Completeness Note

Two modules — Manufacturing (`FR-MFG-*`) and Sales CRM (`FR-CRM-*`) — do not have dedicated `09-traceability.md` files in their SRS directories. FR identifiers for these modules were extracted directly from the SRS body files. These modules are flagged `[SRS-GAP]` and their traceability files must be authored as part of SRS baseline completion.

# 6. Gap Register

This section consolidates all traceability gaps identified across the full requirements set. All gaps were identified during generation of this RTM on 2026-04-05.

## 6.1 Business Goal Trace Gaps (TRACE-GAP-BG)

No business goal trace gaps were identified. All 1,355 functional requirements map to at least 1 of the 6 PRD business goals (BG-001 through BG-006).

## 6.2 Test Case Trace Gaps (TRACE-GAP-TC)

A total of 1,271 functional requirements have no assigned test case identifier. This gap arises because the test plan was authored in parallel with the SRS suite and covers only a subset of modules.

The full list below is grouped by component. The Resolution Action for all items is identical: **extend the test plan to cover all listed FRs before the System Integration Testing (SIT) gate**.

### 6.2.1 Platform Components

| Gap ID | FR ID | Gap Type | Description | Resolution Action |
|---|---|---|---|---|
| G-TC-001 | FR-PLAT-001 through FR-PLAT-060 (53 FRs) | TRACE-GAP-TC | No test cases assigned in central test plan | Extend test plan with Multi-Tenancy and Billing test cases |
| G-TC-002 | FR-AUDIT-006 through FR-AUDIT-077 (52 FRs) | TRACE-GAP-TC | Audit Log FRs not covered by existing TC-PLAT series | Extend test plan with Audit Log test cases |
| G-TC-003 | FR-LOC-001 through FR-LOC-105 (74 FRs) | TRACE-GAP-TC | No test cases assigned for Localisation | Extend test plan with Localisation test cases |
| G-TC-004 | FR-MAPI-001 through FR-MAPI-093 (59 FRs, excluding those covered by TC-PLAT series) | TRACE-GAP-TC | Most Mobile API FRs lack test case assignment | Extend test plan with Mobile API test cases |
| G-TC-005 | FR-INTG-001 through FR-INTG-091 (91 FRs) | TRACE-GAP-TC | No test cases assigned for Integration Layer | Extend test plan with Integration Layer test cases |

### 6.2.2 Core Module Components

| Gap ID | FR ID | Gap Type | Description | Resolution Action |
|---|---|---|---|---|
| G-TC-006 | FR-ACCT-011 through FR-ACCT-122 (112 FRs) | TRACE-GAP-TC | Only FR-ACCT-001 to FR-ACCT-010 have TC assignments | Extend test plan to cover full Accounting module |
| G-TC-007 | FR-INV-004, FR-INV-007 through FR-INV-087 (82 FRs) | TRACE-GAP-TC | Only FR-INV-001 to FR-INV-006 have TC assignments | Extend test plan to cover full Inventory module |
| G-TC-008 | FR-SALES-004 through FR-SALES-096 (93 FRs) | TRACE-GAP-TC | Only FR-SALES-001 to FR-SALES-003 have TC assignments | Extend test plan to cover full Sales module |
| G-TC-009 | FR-PROC-001 through FR-PROC-051 (51 FRs) | TRACE-GAP-TC | No test cases assigned for Procurement | Extend test plan with Procurement test cases |

### 6.2.3 Add-On Module Components

| Gap ID | FR ID | Gap Type | Description | Resolution Action |
|---|---|---|---|---|
| G-TC-010 | FR-HR-008 through FR-HR-069 (62 FRs) | TRACE-GAP-TC | Only FR-HR-001 to FR-HR-007 have TC assignments | Extend test plan to cover full HR and Payroll module |
| G-TC-011 | FR-POS-001 through FR-POS-063 (63 FRs) | TRACE-GAP-TC | No test cases assigned for POS | Extend test plan with POS test cases |
| G-TC-012 | FR-ADVINV-001 through FR-ADVINV-044 (44 FRs) | TRACE-GAP-TC | No test cases assigned for Advanced Inventory | Extend test plan with Advanced Inventory test cases |
| G-TC-013 | FR-MFG-001 through FR-MFG-045 (45 FRs) | TRACE-GAP-TC | No test cases assigned for Manufacturing | Extend test plan with Manufacturing test cases |
| G-TC-014 | FR-CRM-001 through FR-CRM-042 (42 FRs) | TRACE-GAP-TC | No test cases assigned for Sales CRM | Extend test plan with Sales CRM test cases |
| G-TC-015 | FR-AGENT-001 through FR-AGENT-062 (62 FRs) | TRACE-GAP-TC | No test cases assigned for Sales Agents | Extend test plan with Sales Agents test cases |
| G-TC-016 | FR-COOP-001 through FR-COOP-065 (65 FRs) | TRACE-GAP-TC | No test cases assigned for Cooperative Management | Extend test plan with Cooperative Management test cases |
| G-TC-017 | FR-PROJ-001 through FR-PROJ-077 (77 FRs) | TRACE-GAP-TC | No test cases assigned for Project Management | Extend test plan with Project Management test cases |
| G-TC-018 | FR-BSC-001 through FR-BSC-068 (68 FRs) | TRACE-GAP-TC | No test cases assigned for Strategy and BSC | Extend test plan with Strategy and BSC test cases |
| G-TC-019 | FR-ASSET-001 through FR-ASSET-068 (68 FRs) | TRACE-GAP-TC | No test cases assigned for Asset Management | Extend test plan with Asset Management test cases |

## 6.3 SRS Structural Gaps (SRS-GAP)

| Gap ID | Component | Gap Type | Description | Resolution Action |
|---|---|---|---|---|
| G-SRS-001 | Manufacturing (`FR-MFG-*`) | SRS-GAP | No dedicated `09-traceability.md` file in the Manufacturing SRS directory | Author `09-traceability.md` for the Manufacturing module with full FR-to-BG mapping and test oracle column |
| G-SRS-002 | Sales CRM (`FR-CRM-*`) | SRS-GAP | No dedicated `09-traceability.md` file in the Sales CRM SRS directory | Author `09-traceability.md` for the Sales CRM module with full FR-to-BG mapping and test oracle column |

## 6.4 Context Gaps Affecting Traceability (CONTEXT-GAP)

The following context gaps were identified in the source SRS documents. These gaps do not block RTM publication but do affect the completeness of the affected requirements and their eventual test oracles.

| Gap ID | Source SRS | Context Gap Reference | Affected Requirements | Status |
|---|---|---|---|---|
| CG-001 | Localisation | GAP-001: URA EFRIS API endpoint and credentials | FR-LOC-057, FR-LOC-058, FR-LOC-059; FR-INTG-001–FR-INTG-020 | Open |
| CG-002 | Localisation | GAP-002: URA PAYE and VAT return formats (2024/25) | FR-LOC-053, FR-LOC-054, FR-LOC-060, FR-LOC-062, FR-LOC-066, FR-LOC-070; FR-HR-036, FR-HR-046 | Open |
| CG-003 | HR and Payroll | GAP-003: NSSF employer schedule upload format | FR-HR-045 | Open |
| CG-004 | Multi-Tenancy | GAP-004: Independent security review of tenant_id enforcement | NFR-PLAT-002 | Open |
| CG-005 | Multi-Tenancy | GAP-005: Formal module dependency map | FR-PLAT-032 | Open |
| CG-006 | Localisation; Procurement | GAP-006: PPDA procurement thresholds (current) | FR-LOC-085, FR-LOC-086, FR-PROC-012, FR-PROC-046 | Open |
| CG-007 | HR and Payroll | GAP-007: Uganda Data Protection Act compliance specification | NFR-HR-008 | Open |
| CG-008 | HR and Payroll | GAP-009 (HR): Biometric device API specification | FR-HR-020 | Open |
| CG-009 | Integration Layer | GAP-009 (INTG): KRA eTIMS API specification | FR-INTG-046–FR-INTG-062 | Open |
| CG-010 | Integration Layer | GAP-013: NSSF Uganda and Kenya contribution file format | FR-INTG-063–FR-INTG-072 | Open |
| CG-011 | Multi-Tenancy | GAP-011: MTN MoMo Business API specification | FR-PLAT-049, FR-LOC-098 | Open |
| CG-012 | Multi-Tenancy | GAP-012: M-Pesa Daraja B2C API specification | FR-PLAT-049 | Open |
| CG-013 | Multi-Tenancy | GAP-015: White-labelling policy decision | FR-PLAT-058 | Open |
| CG-014 | Localisation | GAP-010: OHADA SYSCOHADA 2017 Chart of Accounts | FR-LOC-080, FR-LOC-081 | Open |
| CG-015 | Projects | CONTEXT-GAP: expense claims module | FR-PROJ-041 | Open |
| CG-016 | Assets | CONTEXT-GAP: deferred tax asset recognition policy | FR-ASSET-059 to FR-ASSET-061 | Open |
| CG-017 | Assets | CONTEXT-GAP: disposal approval workflow tiers | FR-ASSET-035 | Open |
| CG-018 | Cooperative | CG-COOP-002: NIRA NIN verification API | FR-COOP-011 | Open |
| CG-019 | Cooperative | CG-COOP-004: MTN MoMo Uganda API version | FR-COOP-045–FR-COOP-047 | Open |
| CG-020 | Sales Agents | CONTEXT-GAP: Mobile Money API credentials and sandbox | FR-AGENT-039–FR-AGENT-041 | Open |

## 6.5 Gap Remediation Summary

| Category | Count | Priority | Owner |
|---|---|---|---|
| TRACE-GAP-TC (test plan extension required) | 1,271 FRs across 19 gap entries | High — must close before SIT gate | Test Lead |
| SRS-GAP (traceability file missing) | 2 modules (Manufacturing, CRM) | Medium — must close before SRS baseline | SRS Author |
| CONTEXT-GAP (external specification required) | 20 items | High — blocks affected FR implementation | Product Owner / Consultant |
| TRACE-GAP-BG (business goal mapping missing) | 0 | N/A | N/A |

*All TRACE-GAP-TC items are resolved by extending the test plan. The test plan owner must create at least 1 deterministic test oracle per FR, confirming a specific pass/fail criterion, before the affected FR may be moved to the Verified state under the IEEE 1012 V&V cycle.*

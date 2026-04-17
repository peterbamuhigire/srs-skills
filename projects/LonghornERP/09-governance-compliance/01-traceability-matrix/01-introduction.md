# 1. Introduction

## 1.1 Purpose

This Requirements Traceability Matrix (RTM) demonstrates that every functional requirement across all 20 Longhorn ERP software components — 6 platform components and 14 functional modules — traces to at least 1 business goal from the Product Requirements Document (PRD) and to at least 1 test case that provides a deterministic pass/fail criterion.

Traceability is mandatory under IEEE Std 830-1998 Section 3.2.4, which requires that requirements be *traceable*, meaning each requirement's source and its test verification path must be identifiable. This document is the primary evidence artifact for that requirement.

## 1.2 Standard Basis

This matrix is constructed per the following standards:

- **IEEE 1012-2016** — Software Verification and Validation: the traceability analysis prescribed in Section 5.2.2 (Evaluation of Software Requirements).
- **IEEE Std 830-1998** — Recommended Practice for Software Requirements Specifications: completeness, consistency, and verifiability criteria.
- **ISO/IEC 15504 (SPICE)** — Process assessment; traceability artifacts support the Integrity Level evidence required for audit review.

## 1.3 Scope

This matrix covers all Software Requirements Specifications (SRSs) authored for Longhorn ERP as of 2026-04-05. The SRS set comprises:

**Platform SRS components:**

1. Multi-Tenancy and Billing (`FR-PLAT-*`)
2. Role-Based Access Control (`FR-RBAC-*`)
3. Audit Log (`FR-AUDIT-*`)
4. Localisation and Statutory Compliance (`FR-LOC-*`)
5. Mobile API (`FR-MAPI-*`)
6. Integration Layer (`FR-INTG-*`)

**Functional module SRS components:**

1. Accounting and General Ledger (`FR-ACCT-*`)
2. Inventory Management (`FR-INV-*`)
3. Sales (`FR-SALES-*`)
4. Procurement (`FR-PROC-*`)
5. HR and Payroll (`FR-HR-*`)
6. Point of Sale (`FR-POS-*`)
7. Advanced Inventory (`FR-ADVINV-*`)
8. Manufacturing (`FR-MFG-*`)
9. Sales CRM (`FR-CRM-*`)
10. Sales Agents (`FR-AGENT-*`)
11. Cooperative Management (`FR-COOP-*`)
12. Project Management (`FR-PROJ-*`)
13. Strategy and Balanced Scorecard (`FR-BSC-*`)
14. Asset Management (`FR-ASSET-*`)

## 1.4 Business Goals Reference

The following business goals are sourced from the Longhorn ERP Product Requirements Document (PRD). All FRs in this matrix are mapped against these goals.

| ID | Business Goal |
|---|---|
| BG-001 | Replace spreadsheet and manual ERP processes for SMEs in Uganda and East Africa |
| BG-002 | Provide statutory compliance out-of-the-box (URA VAT, PAYE, NSSF, EFRIS) |
| BG-003 | Support multi-currency and multi-country expansion across Africa |
| BG-004 | Enable real-time financial visibility and decision-making |
| BG-005 | Support mobile-first operations for field staff and cooperative agents |
| BG-006 | Provide a complete platform for Chwezi Core Systems to build a SaaS business |

## 1.5 Test Case Reference

Test case identifiers are sourced from the Longhorn ERP Test Plan (`05-testing-documentation/02-test-plan/`). The test plan is being authored in parallel with the SRS suite. Where a test case identifier has been defined, it is cited. Where no TC identifier has yet been assigned, the cell reads `TC-PENDING` and the requirement is flagged `[TRACE-GAP-TC]` in Section 6 (Gap Register).

## 1.6 How to Read This Matrix

Each row in the traceability tables represents one functional requirement. The columns are:

- **FR ID** — The requirement identifier as defined in the source SRS.
- **Description (brief)** — A condensed, one-line summary of the requirement's stimulus-response contract.
- **Business Goal(s)** — One or more of BG-001 through BG-006, representing the PRD need the requirement fulfils.
- **Test Case(s)** — The TC identifier(s) that will verify the requirement. `TC-PENDING` means no TC has been assigned.
- **Gaps** — Any flags raised per the V&V SOP: `[TRACE-GAP-BG]` for missing business goal link; `[TRACE-GAP-TC]` for missing test case.

## 1.7 Gap Classification

The following gap codes are used throughout this document:

- `[TRACE-GAP-BG]` — The requirement has no mappable business goal link. This is an anomaly requiring resolution before the SRS is baselined.
- `[TRACE-GAP-TC]` — The requirement has no assigned test case. The test plan must be extended before the development phase completes.
- `[SRS-GAP]` — The module SRS does not yet contain a dedicated traceability section; FR identifiers were extracted directly from the SRS body. The module traceability file must be authored.

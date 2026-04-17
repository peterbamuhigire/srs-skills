# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Phase 1 (Commerce Foundation) of the BIRDC Enterprise Resource Planning (ERP) system. Phase 1 covers four modules: Sales and Distribution (F-001), Point of Sale (F-002), Inventory and Warehouse Management (F-003), and Agent Distribution Management (F-004).

This document is addressed to BIRDC/PIBID stakeholders, the development team, and external auditors. It serves as the contractual baseline for Phase 1 development, acceptance testing, and audit trail compliance. All requirements are traceable to the business goals defined in the BIRDC ERP Vision document (2026-04-05).

## 1.2 Scope

The BIRDC ERP system is a purpose-built, single-tenant enterprise resource planning system for the Banana Industrial Research and Development Centre (BIRDC) and the Presidential Initiative on Banana Industrial Development (PIBID), located at Nyaruzinga Hill, Bushenyi District, Western Uganda. BIRDC operates Uganda's only industrial-scale banana processing facility, producing Tooke-branded products for domestic retail and international export.

Phase 1 establishes the commerce transaction layer on which all subsequent phases (financial accounting, procurement, production, HR) depend. The scope of this document is limited to Phase 1 modules.

### 1.2.1 In Scope

- Sales and Distribution: order-to-cash lifecycle for Tooke products, EFRIS integration, GL auto-posting
- Point of Sale: factory gate, distribution centre, and agent checkout contexts with offline capability
- Inventory and Warehouse Management: multi-location stock, batch tracking, FEFO enforcement, stock valuation
- Agent Distribution Management: agent virtual store, cash balance tracking, FIFO remittance allocation, commission

### 1.2.2 Out of Scope (Deferred to Later Phases)

- Financial Accounting and General Ledger (Phase 2, F-005)
- Accounts Receivable and Accounts Payable (Phase 2, F-006/F-007)
- Budget Management (Phase 2, F-008)
- Procurement and Farmer Management (Phase 3)
- Manufacturing, QC, HR, Payroll (Phases 4 and 5)

## 1.3 Product Overview

The BIRDC ERP system replaces fragmented spreadsheets and manual registers across all 17 operational domains. It is deployed on-premise at BIRDC Nyaruzinga on BIRDC-owned hardware (**DC-006**: data sovereignty). No cloud vendor holds BIRDC data. The system has three access panels:

- Main ERP Workspace (`/public/`) — all BIRDC/PIBID staff
- Sales Agent Portal (`/public/sales-agents/`) — 1,071 field sales agents
- System Administration (`/public/admin/`) — IT administrators

Six Android mobile applications extend the system to field operations.

## 1.4 Definitions, Acronyms, and Abbreviations

All terms in this document are defined per IEEE Std 610.12-1990. Domain-specific terms are defined in the BIRDC ERP Glossary (`_context/glossary.md`). Key terms used in this document:

| Term | Definition |
|---|---|
| Agent | A field sales agent contracted by BIRDC to sell Tooke products in a defined territory. BIRDC has 1,071 agents. |
| Agent Cash Balance | Real-time net liability: total cash collected from sales minus total verified remittances. |
| BIRDC | Banana Industrial Research and Development Centre. |
| CoA | Certificate of Analysis. |
| DC | Design Covenant — one of 7 binding design constraints. |
| EFRIS | Electronic Fiscal Receipting and Invoicing Solution (URA system-to-system API). |
| FDN | Fiscal Document Number — unique identifier returned by URA EFRIS per fiscal document. |
| FEFO | First Expiry First Out — inventory allocation rule. |
| Float Limit | Maximum monetary value of inventory an agent may hold at any time. |
| GL | General Ledger. |
| GRN | Goods Receipt Note. |
| JE | Journal Entry. |
| NIN | National Identification Number (Uganda). |
| PIBID | Presidential Initiative on Banana Industrial Development. |
| POS | Point of Sale. |
| PPDA | Public Procurement and Disposal of Public Assets Authority. |
| SRS | Software Requirements Specification (this document). |
| TIN | Tax Identification Number (URA). |
| URA | Uganda Revenue Authority. |
| WIP | Work In Progress. |

## 1.5 References

| Reference | Title |
|---|---|
| IEEE Std 830-1998 | IEEE Recommended Practice for Software Requirements Specifications |
| IEEE Std 1233-1998 | IEEE Guide for Developing System Requirements Specifications |
| IEEE Std 610.12-1990 | IEEE Standard Glossary of Software Engineering Terminology |
| ASTM E1340 | Standard Guide for Rapid Prototyping of Computerized Systems |
| Uganda Income Tax Act, Cap 340 | Tax obligations including PAYE and Withholding Tax |
| Uganda Companies Act, 2012 | 7-year financial records retention requirement |
| PPDA Act, Cap 330 | Public procurement compliance |
| URA EFRIS Technical Specification | System-to-system API for fiscal document submission |
| BIRDC ERP Vision Document | `_context/vision.md`, 2026-04-05 |
| BIRDC ERP Feature Register | `_context/features.md`, 2026-04-05 |
| BIRDC ERP Business Rules | `_context/business_rules.md`, 2026-04-05 |

## 1.6 Overview of This Document

- Section 2 describes the overall system description and constraints.
- Section 3 contains the specific requirements for each Phase 1 module.
- Section 4 contains non-functional requirements applicable to all modules.
- Section 5 contains design constraints and compliance requirements.
- Section 6 contains the requirements traceability matrix.
- Appendix A contains open items and gap flags.

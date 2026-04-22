# Introduction to the Accounting and General Ledger Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Accounting and General Ledger (GL) module of Longhorn ERP, a multi-tenant Software as a Service (SaaS) enterprise resource planning platform developed by Chwezi Core Systems. The document is addressed to the lead developer, internal engineering team, and any contracted technical reviewers. All requirements are prospective: they describe behaviour the system shall exhibit upon implementation.

## 1.2 Scope

The Accounting and General Ledger module provides the financial backbone of Longhorn ERP. It covers Chart of Accounts (CoA) management, double-entry journal posting, financial statement generation, bank reconciliation, tax management, budgeting, and period-close processing. It further defines the record-to-report control framework required for a world-class finance ERP, including close orchestration, close task management, recurring and reversing journal foundations, intercompany and elimination-ready journal structure, approval and segregation-of-duties controls, and disciplined finance reporting outputs. The module integrates with all other Longhorn ERP sub-ledger modules ??? Sales, Purchases, Payroll, Inventory, Assets, Manufacturing, and Transportation ??? receiving automated journal postings from each. The scope boundary for this document excludes sub-ledger transaction origination; those modules carry their own SRS documents. Integration touch-points are noted as deferred to the FR-INTG series.
## 1.3 Definitions, Acronyms, and Abbreviations

The following terms are used throughout this document per IEEE Std 610.12-1990 definitions unless otherwise noted.

| Term | Definition |
|---|---|
| CoA | Chart of Accounts — the structured list of GL accounts belonging to a tenant |
| GL | General Ledger — the master record of all financial transactions |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| IFRS | International Financial Reporting Standards |
| IAS | International Accounting Standard |
| VAT | Value Added Tax |
| PAYE | Pay As You Earn — Uganda income tax withheld at source |
| EFRIS | Electronic Fiscal Receipting and Invoicing System (Uganda Revenue Authority) |
| URA | Uganda Revenue Authority |
| SaaS | Software as a Service |
| SRS | Software Requirements Specification |
| P95 | 95th percentile response time under measured load |
| HTTP 422 | Unprocessable Entity — server-side validation failure response code |
| PIF | Project Input Folder — `_context/` directory holding authoritative project context |
| EBITDA | Earnings Before Interest, Taxes, Depreciation, and Amortisation |
| OFX | Open Financial Exchange — standard file format for bank statement import |

## 1.4 Applicable Standards

The requirements in this document are grounded in the following standards and legislation.

- IEEE Std 830-1998 — Recommended Practice for Software Requirements Specifications
- IEEE Std 1233-1998 — Guide for Developing System Requirements Specifications
- IEEE Std 610.12-1990 — Standard Glossary of Software Engineering Terminology
- ASTM E1340 — Standard Guide for Rapid Prototyping of Computerised Systems
- IFRS — International Financial Reporting Standards (all financial statements)
- IAS 2 — Inventories (stock valuation methods)
- IAS 7 — Statement of Cash Flows (indirect method)
- IAS 16 — Property, Plant and Equipment
- IAS 19 — Employee Benefits (leave accruals)
- Uganda VAT Act — VAT registration, input/output tax, and return format
- Uganda Income Tax Act — PAYE bands and withholding tax rates
- Uganda Companies Act — statutory reporting obligations

## 1.5 Overview of This Document

Section 2 provides the Chart of Accounts requirements. Section 3 covers Journal Entry requirements. Section 4 defines Financial Statement requirements. Section 5 addresses Bank Reconciliation. Section 6 specifies Tax Management requirements. Section 7 covers Budgeting. Section 8 defines Period-Close Processing, close orchestration, consolidation foundations, and finance reporting discipline. Section 9 lists Non-Functional Requirements. Section 10 presents the Traceability Matrix mapping every FR to a business goal.
## 1.6 Business Goals

The following business goals govern requirement priority and traceability throughout this SRS.

- **BG-001:** Achieve statutory compliance with Uganda VAT Act, Uganda Income Tax Act, and Uganda Companies Act requirements.
- **BG-002:** Enable management reporting through accurate financial statements, budget variance analysis, and comparative period reporting.
- **BG-003:** Improve operational efficiency through automated sub-ledger journal posting and intelligent bank reconciliation matching.
- **BG-004:** Ensure audit readiness through journal immutability, complete audit trails, and role-based access controls.
- **BG-005:** Reduce days-to-close through controlled orchestration of close tasks, recurring finance processes, and exception management.
- **BG-006:** Establish multi-entity, intercompany, and elimination-ready finance structures that support scalable consolidation and disciplined reporting.
## 1.7 Assumptions and Dependencies

- Each tenant has completed the onboarding workflow, which triggers auto-creation of system accounts (see FR-ACCT-016 through FR-ACCT-018).
- The Platform Integration Layer (FR-INTG series) is responsible for EFRIS connectivity; this document defers to that series for EFRIS-specific behaviour.
- The HR/Payroll module owns PAYE band application; this document records the tax configuration interface only.
- Currency exchange rates are configured at the platform level and consumed by this module; rate-source management is out of scope here.

- Legal entity master data, group structures, and functional/reporting currency setup are maintained by shared platform configuration services and consumed by this module during close and group-reporting processes.
- This SRS specifies consolidation-ready accounting structures and outputs inside Longhorn ERP; advanced external consolidation scenarios such as minority interest, equity pickup, and external statutory filing packages may be extended in a later phase.

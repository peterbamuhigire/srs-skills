# Introduction to the Project Management Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Project Management module of Longhorn ERP, a multi-tenant Software as a Service (SaaS) enterprise resource planning platform developed by Chwezi Core Systems. The document is addressed to the lead developer, internal engineering team, and any contracted technical reviewers. All requirements are prospective: they describe behaviour the system shall exhibit upon implementation.

## 1.2 Scope

The Project Management module enables organisations to plan, execute, monitor, and close projects of any type — commercial, construction, government, and Non-Governmental Organisation (NGO) donor-funded. The module covers the full project lifecycle: project registration, Work Breakdown Structure (WBS) and milestone planning, timesheet capture and resource allocation, cost aggregation, billing (time-and-materials and milestone-based), subcontractor management, retention management, NGO donor tracking, procurement linkage, Gantt chart visualisation, and portfolio reporting.

The module integrates with four other Longhorn ERP modules:

- **Procurement** — receives Purchase Order (PO) costs tagged to projects.
- **General Ledger (GL)** — posts project revenue and cost journals; feeds the Project Profit and Loss (P&L) view.
- **HR/Payroll** — sources employee billing rates and payroll timesheet costs.
- **Sales** — converts milestone billing and time-and-materials billing events into confirmed sales invoices.

The scope boundary for this document excludes the internal GL posting logic (owned by the Accounting SRS), payroll computation (owned by the HR/Payroll SRS), and PO procurement workflow (owned by the Procurement SRS). Integration touch-points with those modules are noted as deferred to the FR-INTG series.

## 1.3 Definitions, Acronyms, and Abbreviations

The following terms are used throughout this document per IEEE Std 610.12-1990 definitions unless otherwise noted.

| Term | Definition |
|---|---|
| WBS | Work Breakdown Structure — a hierarchical decomposition of a project into manageable tasks and deliverables |
| Milestone | A named project event with a defined due date that marks the completion of a significant deliverable or phase |
| Milestone Billing | A billing event triggered automatically when a milestone is marked complete, generating an invoice for the agreed milestone amount |
| T&M Billing | Time-and-Materials Billing — project billing computed as $TnMBilling = \sum (Hours_i \times Rate_i)$ across all billable timesheet lines for a period |
| Retention | A contractual holdback (expressed as a percentage of each invoice) withheld by the client until project completion or a defined retention release event; common in the construction industry |
| NGO Logframe | Logical Framework — a planning matrix used by NGOs and donors that maps project inputs, activities, outputs, outcomes, and impact against a budget |
| Donor | An external funding organisation (government, foundation, or multilateral) providing a grant to an NGO project |
| Grant | A defined fund allocation from a donor for a specific project purpose, governed by a grant agreement |
| Budget Line | A named expenditure category within a grant budget, each with an approved ceiling amount |
| PPDA | Public Procurement and Disposal of Public Assets Authority — the Ugandan statutory body governing public procurement; PPDA compliance applies to government-funded projects |
| PO | Purchase Order — a Procurement module document authorising expenditure with a supplier |
| P&L | Profit and Loss — the financial summary of a project: $ProjectPL = Revenue - \sum Costs$ |
| Gantt Chart | A bar chart representing project tasks, durations, and dependencies against a timeline axis |
| Portfolio | The collection of all active projects belonging to a tenant, viewed in aggregate by status, health, and budget utilisation |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| SaaS | Software as a Service |
| SRS | Software Requirements Specification |
| GL | General Ledger |
| HR | Human Resources |
| PIF | Project Input Folder — `_context/` directory holding authoritative project context |
| P95 | 95th percentile response time under measured load |
| HTTP 422 | Unprocessable Entity — server-side validation failure response code |
| UGX | Ugandan Shilling |

## 1.4 Applicable Standards

The requirements in this document are grounded in the following standards and legislation.

- IEEE Std 830-1998 — Recommended Practice for Software Requirements Specifications
- IEEE Std 1233-1998 — Guide for Developing System Requirements Specifications
- IEEE Std 610.12-1990 — Standard Glossary of Software Engineering Terminology
- ASTM E1340 — Standard Guide for Rapid Prototyping of Computerised Systems
- PPDA Act (Uganda) — Public Procurement and Disposal of Public Assets Act, Cap 83 — governs procurement compliance for government-funded projects
- IFRS 15 — Revenue from Contracts with Customers (milestone and T&M revenue recognition)
- IAS 11 — Construction Contracts (retention accounting and percentage-of-completion method)
- NGO Act (Uganda) — Non-Governmental Organisations Act 2016 — governs donor fund reporting obligations

## 1.5 Overview of This Document

Section 2 defines the Project Register requirements. Section 3 covers WBS and Milestone management. Section 4 specifies Timesheet and Resource Allocation requirements. Section 5 addresses Cost Aggregation and Billing. Section 6 defines Subcontractor Management. Section 7 covers Retention Management, NGO Donor Tracking, Gantt Chart, and Portfolio Dashboard. Section 8 lists Non-Functional Requirements. Section 9 presents the Traceability Matrix mapping every FR to a business goal.

## 1.6 Business Goals

The following business goals govern requirement priority and traceability throughout this SRS.

- **BG-PROJ-001:** Enable project-based organisations (professional services, construction, NGOs, government contractors) to plan and track all project work within a single ERP, eliminating standalone spreadsheets and disconnected tools.
- **BG-PROJ-002:** Provide accurate, real-time project P&L by aggregating costs from Procurement, Payroll, and Expenses against project revenue, enabling management decisions during project execution.
- **BG-PROJ-003:** Support sector-specific compliance: PPDA procurement rules for government projects, retention accounting for construction, and donor logframe budget tracking for NGOs.
- **BG-PROJ-004:** Streamline project billing by automating milestone invoices and T&M invoice generation, reducing billing lag and improving cash collection.
- **BG-PROJ-005:** Provide portfolio-level visibility so management can monitor all projects simultaneously by budget health, schedule status, and profitability.

## 1.7 Assumptions and Dependencies

- The HR/Payroll module has completed employee records with defined billing rates before any timesheet entry can be created.
- The Procurement module is active and POs are tagged with a `project_id` field before cost aggregation can pull PO costs.
- The Sales module is active and capable of receiving billing requests to generate confirmed invoices.
- The GL module is active; the Project Management module does not post journals directly — all postings are mediated by the GL auto-journal mechanism.
- Currency is configurable at the tenant level; this module consumes the tenant's configured functional currency and exchange rates without owning them.
- PPDA compliance guidance for government projects is implemented as workflow flags and audit notes within this module; full PPDA eTendering integration is deferred to the FR-INTG series.

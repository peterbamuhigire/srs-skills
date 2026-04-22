# Introduction to the Asset Management Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Asset Management module of Longhorn ERP, a multi-tenant Software as a Service (SaaS) enterprise resource planning platform developed by Chwezi Core Systems. The document is addressed to the lead developer, internal engineering team, and any contracted technical reviewers. All requirements are prospective: they describe behaviour the system shall exhibit upon implementation.

## 1.2 Scope

The Asset Management module provides the fixed-asset lifecycle management backbone of Longhorn ERP. It covers asset registration, categorisation, depreciation computation, revaluation, disposal, inter-branch transfer, maintenance scheduling, insurance tracking, physical verification, book versus tax depreciation with deferred tax computation, and vehicle fleet management. The module posts all financial consequences — depreciation charges, disposal gains and losses, revaluation adjustments, and transfer entries — to the General Ledger (GL) module automatically. Asset acquisitions originate from the Procurement module when a purchase order receipt is classified as a capital item; the Procurement module carries requirements for that origination flow. Role-Based Access Control (RBAC) is enforced on every Asset Management endpoint; access control definitions are owned by the User Management and RBAC module and referenced here only at the integration boundary.

For vehicle assets, Asset Management remains the system of record for capital-asset accounting, depreciation, maintenance history, insurance and statutory compliance history, transfers, revaluation, and disposal. The Transportation module owns dispatch, trip execution, route planning, driver run assignment, shipment movement, and live fleet operations; any vehicle-operational data retained in Asset Management exists only to support asset history, maintenance planning, compliance evidence, and financial control.

## 1.3 Definitions, Acronyms, and Abbreviations

The following terms are used throughout this document per IEEE Std 610.12-1990 definitions unless otherwise noted.

| Term | Definition |
|---|---|
| Asset | A resource controlled by the organisation from which future economic benefits are expected, per IAS 16. |
| Asset Register | The master list of all fixed assets owned or controlled by a tenant. |
| NBV | Net Book Value — the carrying amount of an asset: cost less accumulated depreciation and impairment. |
| Residual Value | The estimated amount an asset would fetch if disposed of at the end of its useful life, per IAS 16. |
| Useful Life | The period over which an asset is expected to be available for use by the organisation, expressed in years or units of production, per IAS 16. |
| Straight-Line Depreciation | A method that allocates an equal charge each period: $Dep = \frac{Cost - ResidualValue}{UsefulLife}$ |
| Reducing Balance Depreciation | A method that applies a fixed rate to the NBV at the start of each period: $Dep_n = NBV_{n-1} \times Rate$ |
| Revaluation Reserve | The equity reserve account that accumulates upward revaluation surpluses, per IAS 16 §39. |
| Deferred Tax Liability (DTL) | The tax obligation arising when the carrying amount of an asset exceeds its tax base: $DTL = (TaxBase - CarryingAmount) \times TaxRate$ |
| Tax Base | The amount attributable to an asset for tax purposes, computed using Uganda Revenue Authority (URA) allowable depreciation rates. |
| Gain on Disposal | The excess of disposal proceeds over Net Book Value: $Gain = DisposalProceeds - NBV$ |
| Work Order | A maintenance task instruction generated from the planned maintenance calendar, assigned to a technician or contractor. |
| Physical Verification | The periodic process of scanning asset QR/barcode tags in the field to confirm existence and location. |
| Custodian | The employee or department assigned responsibility for the day-to-day care of a specific asset. |
| FR | Functional Requirement — format `FR-ASSET-NNN`. |
| NFR | Non-Functional Requirement — format `NFR-ASSET-NNN`. All NFRs carry a measurable metric per IEEE 982.1. |
| GL | General Ledger — the master record of all financial transactions. |
| IAS 16 | International Accounting Standard 16 — Property, Plant and Equipment. |
| IAS 12 | International Accounting Standard 12 — Income Taxes (deferred tax). |
| IFRS | International Financial Reporting Standards. |
| URA | Uganda Revenue Authority. |
| RBAC | Role-Based Access Control. |
| SaaS | Software as a Service. |
| SRS | Software Requirements Specification. |
| P95 | 95th percentile response time under measured load. |
| QR | Quick Response — a two-dimensional barcode standard. |
| PPDA | Public Procurement and Disposal of Public Assets Authority (Uganda). |

## 1.4 Applicable Standards

The requirements in this document are grounded in the following standards and legislation.

- IEEE Std 830-1998 — Recommended Practice for Software Requirements Specifications
- IEEE Std 1233-1998 — Guide for Developing System Requirements Specifications
- IEEE Std 610.12-1990 — Standard Glossary of Software Engineering Terminology
- ASTM E1340 — Standard Guide for Rapid Prototyping of Computerised Systems
- IAS 16 — Property, Plant and Equipment (recognition, depreciation, revaluation, disposal)
- IAS 12 — Income Taxes (deferred tax liability computation)
- IAS 36 — Impairment of Assets
- Uganda Income Tax Act, Third Schedule — Prescribed depreciation rates for tax purposes
- PPDA Act (Uganda) — Asset disposal procedures for public-sector tenants

## 1.5 Overview of This Document

Section 2 specifies the Asset Register requirements, including asset master data, categories, and QR/barcode tagging. Section 3 covers Depreciation (straight-line, reducing balance, GL posting, period lock). Section 4 defines Revaluation and Disposal requirements. Section 5 addresses Asset Transfers and Maintenance. Section 6 specifies Insurance Tracking and Physical Verification. Section 7 covers Book versus Tax Depreciation, deferred tax computation, and Vehicle Fleet Management. Section 8 lists Non-Functional Requirements. Section 9 presents the Traceability Matrix mapping every FR to a business goal.

## 1.6 Business Goals

The following business goals govern requirement priority and traceability throughout this SRS.

- **BG-ASSET-001:** Ensure complete, auditable accountability for every fixed asset across its full lifecycle — acquisition, depreciation, transfer, maintenance, and disposal.
- **BG-ASSET-002:** Achieve compliance with IAS 16 (Property, Plant and Equipment) and IAS 12 (Income Taxes) in all asset accounting computations and disclosures.
- **BG-ASSET-003:** Satisfy Uganda Revenue Authority (URA) requirements for tax depreciation, enabling accurate computation and reporting of deferred tax liabilities.
- **BG-ASSET-004:** Reduce asset loss and misappropriation through physical verification, QR/barcode tagging, and custodian assignment.
- **BG-ASSET-005:** Improve vehicle fleet utilisation and maintenance reliability through scheduled maintenance calendars, mileage tracking, and fuel consumption logs.

## 1.7 Integrations

| Integrated Module | Integration Point | Direction |
|---|---|---|
| General Ledger | Depreciation expense, accumulated depreciation, disposal gain/loss, revaluation reserve, deferred tax, transfer entries | Asset → GL |
| Procurement | Capital asset creation from confirmed purchase order receipt | Procurement → Asset |
| Transportation | Odometer, utilisation, and compliance events needed for maintenance planning, asset history, or audit support; dispatch, trips, routes, and live fleet control remain owned by Transportation | Transportation → Asset |
| User Management & RBAC | Role and permission checks on all asset endpoints | RBAC → Asset |
| Audit Log | Immutable record of all create, update, approve, and dispose actions | Asset → Audit Log |
| Notifications | Renewal alerts for insurance policies expiring within 30 days | Asset → Notification |

## 1.8 Assumptions and Dependencies

- The GL module Chart of Accounts is configured and includes asset accounts (Fixed Assets, Accumulated Depreciation, Depreciation Expense, Disposal Gain/Loss, Revaluation Reserve, Deferred Tax Liability) before asset transactions are processed.
- The platform Localisation Engine supplies the active tenant currency and financial year start month; this document assumes Uganda defaults (UGX, 1 July fiscal year) unless the tenant configures otherwise.
- URA tax depreciation rates are configurable per asset class in the asset category setup screen; the specific rates in force at the time of tenant onboarding are the administrator's responsibility to enter.
- Physical verification workflows require the mobile app (Android or iOS) with camera access for QR/barcode scanning.

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Longhorn ERP Localisation Engine. The Localisation Engine is the platform service responsible for applying country-specific and tenant-specific configuration to all system behaviour — financial calculations, display formatting, statutory integrations, gateway routing, and compliance artefacts — without code changes.

This document is addressed to the development team, lead architect, and client representatives who must verify that requirements are complete, unambiguous, and verifiable per IEEE 830-1998.

### 1.2 Scope

The Localisation Engine covers:

- Localisation profile lifecycle management (create, assign, update, version, inherit).
- Currency, language, date, and number formatting per tenant.
- Financial year configuration per tenant.
- Tax and statutory deduction configuration per profile.
- Fiscal receipt and payroll statutory API endpoint configuration per profile.
- Chart of Accounts starter template assignment per profile.
- Invoice legal text and address format per profile.
- Payment and SMS gateway configuration per profile.
- Graceful degradation when a configured gateway is unavailable.

The Localisation Engine does not execute statutory return filings or process payment transactions. It stores the configuration that the Integration Layer uses to perform those actions.

### 1.3 Core Design Principle

*One codebase, all markets via configuration.*

Every market-specific behaviour in Longhorn ERP is determined by a localisation profile stored in the database, not by conditional code branches, environment variables, or deployment-time constants. Adding a new country requires inserting a new `localisation_profiles` record and mapping it to the tenant. No code deployment is required.

This principle applies without exception. Any proposed requirement that cannot be expressed as a profile parameter shall be rejected at design review and re-specified as a configuration field.

### 1.4 Definitions

| Term | Definition |
|---|---|
| ERP | Enterprise Resource Planning — integrated management software unifying core business processes. |
| Localisation Engine | The platform service that applies country-specific and tenant-specific configuration without code changes. |
| Localisation Profile | A configuration record in the `localisation_profiles` table defining all market-specific parameters for a tenant's jurisdiction. |
| Tenant | An independent organisation subscribing to Longhorn ERP, operating within its own isolated data environment. |
| FR | Functional Requirement — a requirement that specifies a behaviour the system shall perform. Format: `FR-LOC-NNN`. |
| NFR | Non-Functional Requirement — a quality attribute or constraint with a measurable metric. Format: `NFR-LOC-NNN`. |
| PAYE | Pay As You Earn — statutory income tax deducted from employee salaries. |
| NSSF | National Social Security Fund — statutory social security scheme (Uganda; analogous bodies in other jurisdictions). |
| VAT | Value Added Tax — consumption tax levied at each stage of the supply chain. Uganda standard rate: 18%. |
| URA | Uganda Revenue Authority — tax authority for Uganda (VAT, PAYE, withholding tax, customs). |
| EFRIS | Electronic Fiscal Receipting and Invoicing System — URA-mandated system for real-time electronic submission of tax invoices in Uganda. |
| eTIMS | Electronic Tax Invoice Management System — KRA-mandated equivalent for Kenya. |
| COA | Chart of Accounts — hierarchical list of General Ledger accounts for a tenant. |
| PPDA | Public Procurement and Disposal of Public Assets Authority — Ugandan body governing public-sector procurement. |
| ISO 4217 | International standard defining currency codes (e.g., UGX, KES, TZS, RWF). |
| SRS | Software Requirements Specification — formal requirements document per IEEE 830. |
| WHT | Withholding Tax — tax deducted at source by the paying organisation. |
| MoMo | Mobile Money — generic term for mobile-phone-based financial services (MTN MoMo, Airtel Money, M-Pesa). |

### 1.5 Applicable Standards

| Standard | Application |
|---|---|
| IEEE 830-1998 | Requirements specification structure, completeness, and verifiability criteria. |
| IEEE 610.12-1990 | Terminology definitions used throughout this document. |
| IEEE 1012-2016 | Verification and Validation framework applied in Section 8. |
| ISO 4217 | Currency codes for all currency configuration parameters. |
| IFRS | Accounting framework for Chart of Accounts starter templates. |
| OHADA SYSCOHADA 2017 | COA standard for Francophone Africa profiles (Phase 3). `[CONTEXT-GAP: GAP-010]` |

### 1.6 Document Organisation

| Section | Content |
|---|---|
| Section 2 | Profile management — lifecycle, version control, inheritance, parameter catalogue. |
| Section 3 | Currency, language, date, number, and financial year configuration. |
| Section 4 | Tax, VAT, statutory deductions, and fiscal/payroll API endpoint configuration. |
| Section 5 | Chart of Accounts starter templates, invoice legal text, PPDA workflow, address formats. |
| Section 6 | SMS gateway and mobile money gateway configuration; graceful degradation. |
| Section 7 | Non-functional requirements. |
| Section 8 | Requirements traceability matrix. |

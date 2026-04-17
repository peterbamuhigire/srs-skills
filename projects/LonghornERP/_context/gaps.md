# Open Design Gaps — Longhorn ERP

These are unresolved design decisions and external dependencies that must be resolved before the relevant document can be finalised. Each is tagged with priority and the document it blocks.

## HIGH Priority — Resolve Before Phase 1

### GAP-001: URA EFRIS API Specification

- **Description:** The URA Electronic Fiscal Receipting and Invoicing System (EFRIS) API specification and sandbox credentials are required before the Sales and Accounting modules can specify invoice submission behaviour.
- **Action:** Obtain API spec and sandbox credentials from URA (`efris@ura.go.ug`).
- **Blocks:** SRS: Sales, SRS: Accounting & GL, SRS: Integration Layer
- **Status:** Open

### GAP-002: URA PAYE and VAT Return Formats (2024/25)

- **Description:** URA return file formats change without notice. The current official templates must be confirmed before specifying HR/Payroll and Accounting statutory reporting.
- **Action:** Download current formats from the URA portal; verify against SRS requirements annually.
- **Blocks:** SRS: HR & Payroll, SRS: Accounting & GL
- **Status:** Partially Resolved — templates analysed 2026-04-05. Key fields confirmed below.

#### VAT Return — Form DT-2031 (Monthly)

Standard structure confirmed from official URA template:

| Section | Description | Rate |
|---|---|---|
| C-1 | Zero rated sales (local) | 0% |
| C-2 | Zero rated sales (exports) | 0% |
| C-3 | Exempt local sales | — |
| C-4 | Standard rated sales | **18%** |
| C-5 | Capital goods sold | 18% |
| C-6 | Imported services | 18% |
| D-1 | Local purchases (input tax) | 18% |
| D-2 | Excisable imports | 18% |
| D-3 | Non-excisable imports | 0% |
| H | Net VAT liability = Output Tax − Input Tax | — |

4 CSV upload schedules: (1) Sales detail, (2) Local purchases, (3) Imports, (4) Admin expenses.

Amendment workflow: mark return as AMENDED, supply original Return Number and Return Date.

#### PAYE Return — Forms DT-2001 (Individual) and DT-2002 (Non-Individual) (Annual)

| Entity Type | Form | Standard Rate |
|---|---|---|
| Individual (business income) | DT-2001 | 30% standard; graduated bands apply |
| Company/Trust/NGO | DT-2002 | 30% standard |
| Mining companies | DT-2002 | 25% |

Employment Schedule (SCH 4 of DT-2001): Employer TIN, Employer Name, Annual Salary, Exempt Allowances, Non-Exempt Allowances, PAYE Deducted.

WHT Schedule (SCH 11): Agent TIN, Gross Amount, Payment Date, Tax Deducted.

**Remaining action:** Confirm current graduated PAYE band thresholds from URA portal (amounts change in each Finance Act). Rate percentages confirmed; thresholds require annual verification.

### GAP-003: NSSF Uganda Employer Upload Format

- **Description:** The NSSF employer portal upload format must be confirmed to specify the payroll statutory schedule export.
- **Action:** Obtain current format from the NSSF employer portal.
- **Blocks:** SRS: HR & Payroll
- **Status:** Open

### GAP-004: Multi-Tenancy Security Formal Review

- **Description:** Independent second-developer review of `tenant_id` enforcement is required before any tenant is onboarded. Formal sign-off required.
- **Action:** Commission security review of tenant isolation implementation.
- **Blocks:** SRS: Platform (Multi-tenancy), 09-governance-compliance/03-compliance
- **Status:** Open

### GAP-005: Module Dependency Map

- **Description:** A formal dependency graph is required to prevent undefined behaviour from misconfigured module activation (e.g., Manufacturing requires Advanced Inventory; Cooperative Procurement requires Inventory).
- **Action:** Define and document all inter-module dependencies before module activation logic is finalised.
- **Blocks:** SRS: Platform (Multi-tenancy), SRS: Advanced Inventory, SRS: Manufacturing
- **Status:** Open

### GAP-006: PPDA Procurement Thresholds (Current)

- **Description:** Current micro/small/large procurement limits under the PPDA Act must be verified before approval workflow thresholds are hardcoded.
- **Action:** Verify current thresholds from PPDA Uganda website.
- **Blocks:** SRS: Procurement
- **Status:** Open

### GAP-007: Uganda Data Protection and Privacy Act 2019 — Legal Review

- **Description:** Legal review required covering: data retention obligations, employee access rights, sub-processor obligations, consent requirements for HR medical and financial data.
- **Action:** Commission legal review before HR & Payroll module is finalised.
- **Blocks:** SRS: HR & Payroll, 09-governance-compliance/03-compliance
- **Status:** Open

### GAP-008: Accounting Period Close — Audit-Grade Behaviour

- **Description:** Precise specification required for: behaviour of late-arriving transactions, reversal mechanisms, and year-end GL entries. This must be defined before the Accounting module SRS is finalised.
- **Action:** Design and document accounting period close rules with an IFRS-qualified accountant.
- **Blocks:** SRS: Accounting & GL
- **Status:** Open

## MEDIUM Priority — Resolve Before Phase 2

### GAP-009: Kenya KRA iTax API Credentials

- **Action:** Register on KRA Developer Portal; obtain iTax API spec and sandbox.
- **Blocks:** SRS: Integration Layer (Kenya)
- **Status:** Open

### GAP-010: OHADA SYSCOHADA 2017 Chart of Accounts

- **Action:** Obtain official OHADA SYSCOHADA 2017 COA to define the Francophone Africa localisation profile.
- **Blocks:** SRS: Localisation Engine (Francophone)
- **Status:** Open

### GAP-011: MTN MoMo Business API (Bulk Payment) — Uganda and Kenya

- **Action:** Register on MTN MoMo Developer Portal; obtain bulk payment API spec.
- **Blocks:** SRS: Integration Layer, SRS: HR & Payroll, SRS: Cooperative Procurement
- **Status:** Open

### GAP-012: M-Pesa Daraja B2C API (Safaricom)

- **Action:** Register on Safaricom Developer Portal; obtain Daraja B2C API spec.
- **Blocks:** SRS: Integration Layer (Kenya)
- **Status:** Open

### GAP-013: Odoo and ERPNext Migration Import Scripts

- **Description:** Migration scripts to import customer data from Odoo and ERPNext would accelerate sales. Required before Phase 2 market launch.
- **Action:** Design migration data model and field mapping for Odoo and ERPNext.
- **Blocks:** 08-end-user-documentation/02-installation-guide
- **Status:** Open

### GAP-014: NITA-U SaaS Compliance Review

- **Action:** Review NITA-U SaaS cloud provider obligations under Uganda's ICT framework.
- **Blocks:** 09-governance-compliance/03-compliance
- **Status:** Open

## Internal Decisions Required

### GAP-015: White-Labelling Policy

- **Decision:** Allow Enterprise tenants to brand as their own ERP?
- **Blocks:** SRS: Platform (Multi-tenancy), 01-strategic-vision/03-business-case
- **Status:** Undecided

### GAP-016: Hospitality Module Scope

- **Decision:** Phase 3 add-on or separate Chwezi product?
- **Blocks:** 01-strategic-vision/01-prd
- **Status:** Undecided

### GAP-017: Academia Pro / Medic8 / Kulima Integration Points

- **Decision:** Define data flows and integration contracts between Longhorn ERP and sibling Chwezi products.
- **Blocks:** SRS: Integration Layer
- **Status:** Undecided

### GAP-018: Source Code Strategy

- **Decision:** Proprietary SaaS forever, or future open-source community edition?
- **Blocks:** 01-strategic-vision/03-business-case
- **Status:** Undecided

---
title: "Compliance and Data Protection — Maduuka"
version: "0.1-DRAFT"
date: "2026-04-05"
status: "DRAFT — pending legal review (GAP-002)"
owner: "Peter Bamuhigire"
---

# Compliance and Data Protection — Maduuka

**Status:** *DRAFT — this document must not be used as legal advice. Legal review under GAP-002 is mandatory before any personally identifiable information (PII) is collected from end users in a production environment.*

**Purpose:** document Maduuka's compliance posture under Uganda law and applicable international standards, identify data categories processed by the system, and record required actions before production launch.

## Section 1: Regulatory Scope

Maduuka processes PII on behalf of business tenants operating primarily in Uganda. The following regulatory instruments apply:

- Uganda Data Protection and Privacy Act 2019 (DPPA 2019)
- Uganda Revenue Authority EFRIS requirements (Phase 3)
- National Drug Authority (NDA) Uganda — Pharmacy and Drugs Act Cap 280 (Phase 2)
- Uganda National Social Security Fund Act (payroll module, Phase 1)
- Uganda Income Tax Act — PAYE (payroll module, Phase 1)

## Section 2: Uganda Data Protection and Privacy Act 2019

<!-- [DOMAIN-DEFAULT: legal-uganda] -->
**[CRITICAL: GAP-002 — Legal review by a Uganda-qualified data protection adviser is required before any PII is collected in the production environment.]**
<!-- [END DOMAIN-DEFAULT] -->

### Applicable Provisions

The following sections of the DPPA 2019 directly constrain Maduuka's data handling:

| Section | Obligation |
|---|---|
| Section 13 | Data collectors must notify data subjects of the purpose of data collection at the time of collection. |
| Section 15 | Personal data must be used only for the disclosed purpose for which it was collected. |
| Section 19 | Data subjects have the right to access their personal data held by a data controller. |
| Section 21 | Data subjects have the right to rectification of inaccurate personal data. |
| Section 22 | Data subjects have the right to erasure of personal data ("right to be forgotten"). |
| Section 27 | Data controllers must implement appropriate technical and organisational security measures to protect personal data. |

### Data Categories Processed

| Data Category | Examples | Legal Basis | Retention Period |
|---|---|---|---|
| Customer PII | Name, phone number, address, NIN | Contractual (credit sales, customer account) | 7 years (tax and audit requirement) |
| Employee data | NIN, salary, bank account number, biometrics (if used) | Employment contract | 7 years post-termination |
| Patient data (Phase 2) | Name, NIN, allergies, prescriptions | Healthcare provision | [CONTEXT-GAP: NDA Uganda retention period for prescription records not confirmed — GAP-009] |
| Guest data (Phase 3) | Name, NIN, ID document photograph | Hotel registration regulation | [CONTEXT-GAP: Uganda hotel guest registration regulation and required retention period not confirmed] |
| Transaction data | Sales, payments, refunds, receipts | Contractual obligation and Uganda tax law | 7 years |

### Required Actions Before Production (GAP-002)

The following actions are assigned to Peter and must be completed before any PII is collected in the production environment:

1. Engage a Uganda-qualified data protection adviser to review this document and the system's data flows.
2. Register Maduuka (Chwezi Core Systems) as a data controller with the Personal Data Protection Office (PDPO) Uganda.
3. Draft a Privacy Policy for display to tenants and end users at account creation.
4. Design and implement the data subject request workflow within Maduuka settings: access, rectification, and erasure requests, each with a documented response time commitment.
5. Execute written data processing agreements with all third-party sub-processors: Africa's Talking (SMS/WhatsApp), Wasabi Technologies (cloud storage), MTN Uganda (MoMo), and Airtel Uganda (Airtel Money).

## Section 3: URA Tax Compliance

Maduuka's payroll module (F-008) computes and records statutory deductions. The following obligations apply to each Maduuka tenant operating in Uganda:

- *PAYE:* deducted from employee gross pay per the Uganda Income Tax Act graduated bands. Remitted to URA by the 15th of the month following the payroll period.
- *NSSF:* employer contribution 10%, employee contribution 5% of gross pay. Remitted to NSSF by the 15th of the month following the payroll period.
- *LST:* Local Service Tax, configurable per local government authority. Collected and remitted per the tenant's registered local government.

Maduuka is not a Value Added Tax (VAT) collection agent. The system enables tenants who are VAT-registered businesses to calculate, record, and report VAT accurately. EFRIS integration (F-015, Phase 3) provides fiscal compliance for businesses mandated to use the URA Electronic Fiscal Receipting and Invoicing Solution.

*Note: Uganda PAYE tax bands change when URA issues updated rates. GAP-008 requires a defined process for applying updated tax bands and handling payrolls already processed under prior rates.*

## Section 4: NDA Pharmacy Compliance (Phase 2)

The following requirements apply to tenants operating the Pharmacy/Drug Store Module (F-012):

- A controlled drugs dispensing register must be maintained per NDA Uganda requirements under the Pharmacy and Drugs Act Cap 280.
- A written dispensing policy must be held at each pharmacy outlet.
- Dispensing records must be retained for the NDA-required period.

[CONTEXT-GAP: GAP-003 — NDA Uganda approved drug codes and controlled drugs register format and required fields not yet confirmed. This section must be updated when GAP-003 is resolved.]

## Section 5: Security Standards Alignment

| Standard | Requirement | Alignment | Status |
|---|---|---|---|
| OWASP Top 10 (2021) | Address all 10 vulnerability categories | Addressed in Security Hardening phase (Phase 14, Sprint 11) | Planned |
| TLS 1.3 | All data in transit encrypted | Enforced on all API and web endpoints | In design |
| AES-256 | Local storage encryption on mobile devices | Applied to SQLite offline database on Android and iOS | In design |
| bcrypt (cost ≥ 12) | Password hashing | Applied to all stored user credentials | In design |
| Immutable audit log | All data mutations recorded with user, timestamp, and previous value | Implemented across all write operations | In design |
| RBAC enforcement | Role-based access control on every API endpoint | PHPStan-verified middleware on all routes | In design |

## Section 6: Document Maintenance

This document must be updated when:

- A gap listed in Section 2 or Section 4 is resolved.
- A new data category is introduced by a new module or feature.
- Uganda law or URA/NDA regulations are amended.
- A new third-party sub-processor is engaged.

All updates must increment the version number and record the change in `docs/CHANGELOG.md`.

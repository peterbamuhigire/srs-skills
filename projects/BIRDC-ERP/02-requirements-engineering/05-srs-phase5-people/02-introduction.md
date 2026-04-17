# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines all functional and non-functional requirements for Phase 5 of the BIRDC Enterprise Resource Planning (ERP) system. Phase 5 covers two modules:

- **F-013:** Human Resources — employee lifecycle, attendance, leave, factory worker registry, and HR Self-Service
- **F-014:** Payroll — configurable payroll elements, Uganda statutory computations, payroll run, payslip delivery, and GL integration

This document is the authoritative input for detailed design, development, and acceptance testing of these modules.

## 1.2 Scope

The BIRDC ERP system is a single-tenant, on-premise enterprise resource planning platform purpose-built for the *Banana Industrial Research and Development Centre* (BIRDC) and the *Presidential Initiative on Banana Industrial Development* (PIBID), located at Nyaruzinga Hill, Bushenyi District, Western Uganda.

Phase 5 requirements govern:

- All 150+ permanent BIRDC and PIBID staff
- Casual factory workers assigned to production orders
- The Android HR Self-Service App used by all 150+ staff for leave, payslips, and attendance
- Integration with ZKTeco biometric fingerprint attendance devices (BR-016)
- Uganda statutory deductions: Pay As You Earn (PAYE), National Social Security Fund (NSSF), and Local Service Tax (LST)
- Payroll General Ledger (GL) auto-posting into the BIRDC commercial and PIBID parliamentary accounts (DC-004)

## 1.3 Business Context and Goals

BIRDC operates under a dual mandate: a government body accountable to Parliament and a commercial enterprise pursuing export markets. The People modules must satisfy both contexts simultaneously:

- PIBID staff are remunerated on government pay scales; BIRDC staff on commercial pay scales
- Payroll auto-posts to both PIBID budget votes and BIRDC commercial GL accounts without manual journal entries
- Every payroll transaction is permanently auditable under the Uganda Companies Act and Income Tax Act 7-year retention requirement (DC-003)

The strategic goals from `_context/vision.md` that Phase 5 directly satisfies are:

1. **Operational unity** — replace spreadsheet-based payroll and manual attendance registers
2. **Financial integrity** — immutable payroll records with hash-chained GL entries
3. **Government replicability** — all PAYE bands, NSSF rates, and LST tiers configurable via the UI by the Finance Director, requiring no developer involvement (DC-002)

## 1.4 Definitions and Acronyms

The following terms are used throughout this document. Full definitions appear in `_context/glossary.md`.

| Term | Definition |
|---|---|
| BIRDC | Banana Industrial Research and Development Centre |
| PIBID | Presidential Initiative on Banana Industrial Development |
| ERP | Enterprise Resource Planning |
| GL | General Ledger |
| HR | Human Resources |
| PAYE | Pay As You Earn — Uganda income tax withheld from salaries |
| NSSF | National Social Security Fund |
| LST | Local Service Tax |
| NIN | National Identification Number |
| BR | Business Rule — see `_context/business_rules.md` |
| DC | Design Covenant — one of 7 binding design constraints |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| SRS | Software Requirements Specification |
| API | Application Programming Interface |
| JWT | JSON Web Token |
| TOTP | Time-based One-Time Password |

## 1.5 References

- IEEE Std 830-1998 — Recommended Practice for Software Requirements Specifications
- IEEE Std 1233-1998 — Guide for Developing System Requirements Specifications
- IEEE Std 610.12-1990 — Standard Glossary of Software Engineering Terminology
- ASTM E1340 — Standard Guide for Rapid Prototyping of Computerized Systems
- Uganda Income Tax Act (Cap. 340) — PAYE, NSSF, and LST obligations
- Uganda Companies Act 2012 — 7-year financial record retention
- `_context/vision.md` — BIRDC ERP vision and design covenants
- `_context/business_rules.md` — BR-001 through BR-018
- `_context/tech_stack.md` — implementation platform specifications
- `_context/gap-analysis.md` — open items and unresolved dependencies

## 1.6 Document Overview

- Section 2 presents the overall system description for Phase 5 modules
- Section 3 defines all functional requirements for F-013 (Human Resources) and F-014 (Payroll)
- Section 4 defines non-functional requirements applicable to Phase 5
- Section 5 lists design constraints and external interface requirements

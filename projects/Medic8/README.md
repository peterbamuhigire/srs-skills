# Medic8

**Status:** Phase 1 — Strategic Vision (Pending)
**Owner:** Peter — Chwezi Core Systems (chwezicore.com)
**Domain:** healthcare (Africa-first; globally configurable)
**Methodology:** Hybrid (Water-Scrum-Fall) — formal requirements gate per phase; iterative delivery within phases
**Started:** 2026-04-03

---

## Quick Links

- `DOCUMENTATION-STATUS.md` — Full document inventory, generation status, and progress summary

## Context Files

- `_context/vision.md` — Product vision, 4-phase build plan, globally configurable positioning
- `_context/domain.md` — Healthcare domain baseline (Uganda regulatory + global configurability)
- `_context/features.md` — Module list (30+ modules across 4 phases)
- `_context/tech_stack.md` — Technology decisions (same as Academia Pro + FHIR/DICOM/HL7)
- `_context/business_rules.md` — Clinical, financial, data, HMIS, prescribing rules
- `_context/quality_standards.md` — Uptime, offline, bandwidth, encryption targets
- `_context/glossary.md` — Project terminology (50+ terms, IEEE 610.12 format)
- `_context/stakeholders.md` — 18 built-in roles with access scopes
- `_context/personas.md` — 6 market segment personas
- `_context/metrics.md` — Tier pricing, MRR targets, phase gate criteria
- `_context/gap-analysis.md` — 7 HIGH / 8 MEDIUM priority gaps
- `_context/competitor-analysis.md` — ClinicMaster and OpenMRS analysis
- `_context/payment-landscape.md` — Mobile money, insurance, donor funds
- `_context/literature-insights.md` — Insights from 10 health informatics books
- `_context/quality-log.md` — QA issue log

---

## Design Covenant

> Automate every clinical and administrative process as much as possible, yet remain simple enough for a single receptionist to operate — provided each user has completed the onboarding for their assigned modules. Clinically safe and globally configurable; fast and intuitive in daily use.

---

## Phase Progress

| Phase | Folder | Status | Deliverables |
|---|---|---|---|
| 01 — Strategic Vision | `01-strategic-vision/` | Pending | PRD, Vision Statement, Business Case |
| 02 — Requirements Engineering | `02-requirements-engineering/` | Pending | SRS, User Stories, Stakeholder Analysis |
| 03 — Design Documentation | `03-design-documentation/` | Pending | HLD, LLD, API Spec, DB Design, UX Spec |
| 04 — Development Artifacts | `04-development-artifacts/` | Pending | Technical Spec, Coding Guidelines |
| 05 — Testing Documentation | `05-testing-documentation/` | Pending | Test Strategy, Test Plan, Test Report |
| 06 — Deployment & Operations | `06-deployment-operations/` | Pending | Deployment Guide, Runbook |
| 07 — Agile Artifacts | `07-agile-artifacts/` | Pending | Sprint Planning, DoD, DoR |
| 08 — End User Documentation | `08-end-user-documentation/` | Pending | User Manual, Installation Guide, FAQ |
| 09 — Governance & Compliance | `09-governance-compliance/` | Pending | Traceability Matrix, Audit Report, Compliance, Risk Assessment |

---

## User Roles

18 built-in roles with scoped access:

- Super Admin
- Facility Admin/Medical Director
- Doctor/Physician
- Clinical Officer
- Nurse/Midwife
- Pharmacist
- Lab Technician
- Radiographer
- Receptionist/Front Desk
- Cashier/Billing Clerk
- Insurance Clerk
- Accountant
- Store Keeper
- Records Officer
- Facility Director/Owner
- Auditor
- Patient/Client
- Community Health Worker (VHT/CHW)

---

## 4-Phase Build Plan Summary

| Phase | Scope | Target | MRR Target |
|---|---|---|---|
| 1 — MVP | Patient registration, OPD, pharmacy, basic lab, billing (cash) | 10 clinics | UGX 1.5M |
| 2 — Growth | IPD, maternity, immunisation, insurance, inventory, HR/payroll, HMIS | 50 facilities | UGX 15M |
| 3 — Programmes | HIV/AIDS, TB, FHIR, PEPFAR, CHW app, patient app | PEPFAR partners | UGX 40M |
| 4 — Enterprise | Theatre, blood bank, PACS, multi-facility, Director platform | Hospital networks | UGX 100M |

---

## Phase 1 Development Gate: Gap Status

**Gate opens when all 7 HIGH-priority gaps are resolved.** Current status:

| Gap | Description | Status |
|---|---|---|
| HIGH-001 | Clinical safety — medication error prevention | Unresolved |
| HIGH-002 | Data Protection Act 2019 — healthcare data | Unresolved |
| HIGH-003 | Uganda medical licensing — software regulation | Unresolved |
| HIGH-004 | Clinical decision support specificity | Unresolved |
| HIGH-005 | HIV and confidential record access | Unresolved |
| HIGH-006 | Emergency access to cross-facility records | Unresolved |
| HIGH-007 | HMIS form versions | Unresolved |

**Resolved: 0 of 7.**

---

## External Actions Required

These cannot be completed by the AI and require Peter's direct action:

| Action | Purpose |
|---|---|
| Uganda NDA drug interaction database | Medication safety and prescribing rules |
| NHIS claims format and API docs | Insurance billing integration |
| NMS LMIS data submission format | National supply chain reporting |
| CPHL specimen submission process | Lab specimen referral workflow |
| Uganda MoH HMIS forms 105, 108, 033b | Government health reporting compliance |
| Uganda Diagnostic Imaging standards | Radiology module regulatory alignment |
| WHO Essential Medicines List (Uganda adaptation) | Formulary and prescribing baseline |
| PEPFAR MER Indicator Reference Guide | Phase 3 programme reporting compliance |
| UBTS blood transfusion guidelines | Phase 4 blood bank module compliance |
| UMDPC software registration enquiry | Medical software licensing requirement |
| Data Protection Officer consultation | Data Protection Act 2019 compliance |

---

## Internal Decisions Required

These require strategic decisions from the product owner before implementation:

| Decision | Impact |
|---|---|
| Clinical decision support liability disclaimer | Legal risk mitigation for CDS features |
| Drug interaction database: build vs licence | Phase 1 medication safety architecture |
| FHIR server: full HAPI FHIR vs export-only | Phase 3 interoperability scope |
| White-labelling policy | Multi-tenant branding and pricing model |
| Government facility pricing | Public sector go-to-market strategy |
| Telemedicine launch timing | Phase sequencing and regulatory readiness |

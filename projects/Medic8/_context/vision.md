# Project Vision

**Project:** Medic8
**Client Contact:** Peter — Chwezi Core Systems (chwezicore.com)
**Date:** 2026-04-03

## Problem Statement

Hospitals and clinics across Uganda and Africa operate on fragmented, paper-heavy workflows — patient records in exercise books, pharmacy stock counted manually, billing via handwritten receipts, and statutory HMIS reports compiled by hand at month-end. Existing solutions fall into three traps: open-source systems such as OpenMRS carry a total cost of ownership (TCO) of USD 35,000-130,000 over three years once implementation, training, and server hosting are factored in; legacy incumbents such as ClinicMaster are desktop-bound, lack mobile-first design, and offer no offline resilience, mobile money integration, or FHIR compliance; and foreign-built enterprise systems assume stable power, reliable internet, and an on-site IT department. Medic8 does for hospitals what Academia Pro does for schools: delivers an enterprise-grade, Africa-first healthcare information management system at a price the market can sustain, deployed as multi-tenant SaaS so no on-premise IT infrastructure is required.

## Design Covenant (Binding Constraint)

> Automate every clinical and administrative process as much as possible, yet remain simple enough for a single receptionist to operate — provided each user has completed the onboarding for their assigned modules. Clinically safe and globally configurable; fast and intuitive in daily use.

**Derived hard requirements:**

- Maximum automation by default: prescription alerts, stock reorder triggers, insurance pre-authorisation checks, and HMIS report generation fire without manual intervention
- Zero-config defaults: a Ugandan private clinic is operational within 60 minutes of signup
- Role-scoped UX: a pharmacist never sees an HR screen; a lab technician never sees payroll; complexity is hidden behind role boundaries
- Onboarding-path architecture: each module ships with embedded guided onboarding; users learn module-by-module
- Progressive disclosure: advanced clinical, insurance, and reporting settings exist but do not clutter the daily workflow
- Single-receptionist survivability: if the IT officer leaves, the receptionist and clinic manager can continue operating the system
- Clinical safety: drug interaction warnings, allergy flags, and dosage alerts are non-negotiable defaults that cannot be silently disabled

## Positioning

Africa-first, globally configurable. Uganda is the launch market. The country configuration layer enables expansion to Kenya, Tanzania, Rwanda, DRC, Nigeria, India, and Australia without forking the codebase. Regulatory, clinical, financial, and reporting requirements adapt per tenant through the configuration layer.

## Target Market Segments

1. **Private clinics** — Small to medium outpatient clinics with 1-5 consultation rooms, pharmacy, and basic lab. Uganda has 3,000+ registered facilities. Primary revenue driver.
2. **Mission / NGO hospitals** — Faith-based and NGO hospitals (Holy Family, Mengo, Nsambya, Lacor, Kisiizi, Hope Missionary). Multi-department with inpatient, maternity, lab, and pharmacy. Require insurance processing and donor fund reporting.
3. **Government-aided hospitals** — HC IVs, General Hospitals, and Regional Referrals. Require HMIS compliance, NMS integration, and capitation grant tracking. Approximately 3,000 facilities in Uganda.
4. **Multi-facility networks** — Hospital groups (Aga Khan, AAR, Case Medical, Norvik). Require multi-site patient record sharing and consolidated reporting.
5. **PEPFAR / Global Fund implementing partners** — NGOs receiving USAID/PEPFAR funding for HIV/TB programmes. Currently use OpenMRS/UgandaEMR. Require PEPFAR MER indicators and donor fund accounting.
6. **National referral hospitals** — Mulago, Kiruddu, Kawempe, Butabika. Phase 4 target.

## Key Competitive Positions

1. **Superior to ClinicMaster in every dimension:** mobile-first, SaaS delivery, AI analytics, mobile money integration, FHIR R4 compliance, patient portal, and offline resilience.
2. **Lower TCO than OpenMRS:** OpenMRS costs USD 35,000-130,000 over 3 years; Medic8 costs USD 9,400-71,000 over the same period and includes billing, insurance, HR, payroll, mobile money, patient app, and local support.

## Architecture Decisions

- Centralised multi-tenant model with `facility_id` isolation, not federated
- openEHR two-level modelling for multi-country clinical configurability
- EHR as data bus — event-driven architecture
- FHIR R4 native API from day 1
- Offline-first for all clinical workflows
- Global patient identity layer (shared architectural pattern with Academia Pro's global student identity)

## Goals (4-Phase Build Sequence)

1. **Phase 1 MVP (6 months):** Patient registration, OPD, pharmacy, basic lab, billing (cash). Target 10 private clinics. MRR target UGX 1,500,000.
2. **Phase 2 Growth:** IPD, maternity, immunisation, insurance, inventory, HR/payroll, HMIS. Target 50 facilities. MRR target UGX 15,000,000.
3. **Phase 3 Programmes:** HIV/AIDS, TB, FHIR API, PEPFAR MER indicators, CHW app, patient app. Target PEPFAR implementing partners. MRR target UGX 40,000,000.
4. **Phase 4 Enterprise:** Theatre, blood bank, PACS, multi-facility, Director platform. Target hospital networks and national referrals. MRR target UGX 100,000,000.

## Stakeholders

See `_context/stakeholders.md` for the full register.

Key groups: Clinic Owner/Director, Hospital Administrator, Doctor/Clinical Officer, Nurse, Pharmacist, Lab Technician, Accounts/Billing Officer, Insurance Liaison, HR Officer, Patient, Community Health Worker, Ministry of Health (HMIS), PEPFAR/Global Fund (donor reporting), Chwezi Core Systems (operator).

## Success Criteria

- Phase 1 gate: all MVP modules functional, 100% test pass rate, at least 3 pilot clinics live, cash billing reconciliation rate at 95%+
- Phase 2 gate: insurance claim submission and reconciliation functional, HMIS monthly report export validated by MoH field officer
- Phase 3 gate: PEPFAR MER indicator reports verified against UgandaEMR baseline data, FHIR R4 API passes ONC certification test suite
- Phase 4 gate: multi-facility patient record sharing demonstrated across at least 2 sites with sub-second lookup, consolidated Director dashboard operational

## Global Vision

Uganda is the launch market. Planned expansion sequence: Kenya, Tanzania, Rwanda, DRC, Nigeria. Future markets: India, Australia. The country configuration layer adapts regulatory frameworks (licensing, reporting), clinical protocols (formularies, disease classifications), financial systems (currencies, tax, insurance schemes), and reporting requirements per tenant without forking the codebase.

## Methodology Note (Water-Scrum-Fall Confirmation)

Methodology is Hybrid (Water-Scrum-Fall): formal requirements sign-off and phase gate before each phase; iterative sprints within each phase. This pattern was confirmed by Peter on 2026-04-03. Phase gate criteria are defined in `_context/metrics.md`. No phase begins development until `_context/` files for that phase are reviewed and signed off.

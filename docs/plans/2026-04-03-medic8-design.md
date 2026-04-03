# Medic8 — Project Design Document

**Date:** 2026-04-03
**Author:** Peter — Chwezi Core Concepts (chwezicore.com)
**Status:** Approved
**Domain:** Healthcare
**Methodology:** Hybrid (Water-Scrum-Fall)

---

## 1. Product Vision

Medic8 is a multi-tenant SaaS healthcare information management system. It does for hospitals what Academia Pro does for schools: provides an enterprise-grade, Africa-first, globally configurable system at a price that makes sense for the market, deployed as SaaS so there is no on-premise IT infrastructure required.

**Positioning:** Africa-first, globally configurable. Uganda is the launch market. The country configuration layer enables expansion to Kenya, Tanzania, Rwanda, DRC, Nigeria, India, and Australia without forking the codebase.

**Target segments:** Private clinics, mission/NGO hospitals, government-aided hospitals, multi-facility health networks, PEPFAR/Global Fund implementing partners, and national referral hospitals.

**Primary competitors:** ClinicMaster (commercial, 200+ facilities, East Africa) and OpenMRS (open-source, 8,000+ facilities, 70+ countries).

---

## 2. Architecture Decisions

### 2.1 Multi-Tenant Data Architecture

Same centralised multi-tenant architecture as Academia Pro. Single database with row-level tenant isolation via `facility_id`. No federated or per-country database separation. Data sovereignty handled through regional cloud deployments if needed, not at the application architecture level.

### 2.2 EHR as Data Bus

The EHR is the foundational data bus, not a module (Coiera, Ch 10). Every module (pharmacy, lab, radiology, billing) reads from and writes to this bus. A clinical encounter triggers downstream effects (lab order, pharmacy dispense, charge capture, HMIS tally) automatically via an event-driven architecture (Brown, Ch 1).

### 2.3 openEHR Two-Level Modelling

Stable Reference Model (Level 1 — database schema) that never changes per country. Clinical Archetypes and Templates (Level 2) loaded per tenant configuration for country-specific forms, validation rules, and clinical workflows (Sinha et al., Ch 18). This is the pattern that enables "one codebase, many countries."

### 2.4 Country Configuration Layer

A single codebase adapts to different countries' regulatory, clinical, and financial requirements:

| Layer | Universal (single codebase) | Country-configurable |
|---|---|---|
| Clinical core | SOAP notes, prescribing, lab orders, vital signs, ward management | Reference ranges, drug formulary, immunisation schedule, prescribing authority rules |
| Coding | ICD-10 engine, LOINC engine, FHIR R4 API | Which code system is primary, SNOMED CT availability, local terminology mappings |
| Billing | Charge capture, receipt generation, payment collection, insurance claims engine | Currency, tax rules, insurance scheme definitions, pricing tiers, mobile money providers |
| Reporting | Report engine, dashboard framework, export formats | HMIS form definitions per country, national reporting API endpoints |
| HR/Payroll | Staff registry, leave management, payroll engine | Tax tables, professional council licence types, salary scales |
| Security | Audit trail, encryption, RBAC + ABAC, break-the-glass | Session timeout, MFA requirements, data retention period, breach notification deadline, consent model |
| Patient identity | Global patient index, EMPI matching, biometric | National ID type, validation rules, cross-facility sharing rules |
| Mobile money | Payment gateway abstraction layer | Provider APIs (MTN MoMo, M-Pesa, Airtel Money, UPI, none for Australia) |

### 2.5 Terminology Service

Single gateway to all code systems (Sinha et al., Ch 11-17). Priority implementation order:

1. **ICD-10/ICD-11** — mandatory everywhere for diagnosis coding and reporting
2. **LOINC** — laboratory results and observations from day one
3. **SNOMED CT** — clinical documentation richness, internal concept storage
4. **RxNorm / ATC** — medications, mapped per country
5. **CPT/HCPCS** — only for markets requiring it (USA, some insurers)

Store clinical data internally using SNOMED CT concept IDs. Map to ICD-10 at the reporting/billing boundary (Coiera, Ch 22-23).

### 2.6 ABAC Layered on RBAC

Role grants base access, but Attribute-Based Access Control policies enforce fine-grained rules: HIV status visible only to the treating clinician; mental health notes require explicit patient consent; adolescent reproductive health records restricted by jurisdiction-specific rules (Sinha et al., Ch 32).

### 2.7 Configurable Consent Engine

Core platform service. India's ABDM requires opt-in consent artefacts. Australia's My Health Record uses opt-out. Uganda has minimal digital consent infrastructure. Four models supported: general consent, general consent with specific denials, general denial with specific consents, general denial (Coiera, Ch 19). Tenant-level configuration.

### 2.8 FHIR R4 Native API

Primary API and data exchange standard from day one. Minimum viable FHIR resources:

- `Patient` — demographics, EMPI linkage
- `Encounter` — OPD visits, IPD admissions
- `Condition` — ICD-10/SNOMED coded diagnoses
- `MedicationRequest` / `MedicationDispense` — pharmacy workflow
- `Observation` — lab results (LOINC-coded), vitals
- `DiagnosticReport` — radiology, lab panels
- `Immunization` — EPI programme tracking
- `ServiceRequest` — lab/radiology orders
- `Claim` / `ExplanationOfBenefit` — insurance billing
- `AllergyIntolerance` — patient allergies

Every FHIR response includes a human-readable HTML narrative fallback (Rowlands, Ch 46). Support SMART on FHIR for third-party app substitutability. CDA R2 documents generated for discharge summaries and referral letters.

---

## 3. Clinical Safety Design

### 3.1 Medication Safety

- **Four-tier CDS alert architecture**: Info / Warning / Serious / Fatal. Override logging with rate tracking per facility (Rowlands Ch 44, Volpe Ch 5)
- **Five Rights of Medication Administration** enforced at CPOE: right patient, drug, dose, route, time (Volpe Ch 6)
- **Tall Man Lettering** for look-alike/sound-alike drugs (Volpe Ch 6)
- **Weight-based dosing** with inline mg/kg calculators, dose rounding, adult ceiling dose cap (Lehmann Ch 25-26)
- **Decimal error guards** for neonatal dosing — 10x/100x overdose prevention (Lehmann Ch 28)
- **Drug-drug, drug-allergy, drug-pregnancy, drug-disease interaction checks** at order entry (Rowlands Ch 44)
- **Medication reconciliation** at every transition of care: OPD to IPD, IPD to discharge, facility to facility (Volpe Ch 6)
- **Barcode Medication Administration (BCMA)** for IPD drug rounds (Volpe Ch 6, Hussey Ch 3)
- **FMEA framework** for medication workflow safety — severity x occurrence x detection scoring (Lehmann Ch 29)

### 3.2 Patient Safety

- **Early Warning Scores (NEWS2) calibrated for SSA populations** — vital signs scoring for clinical deterioration prediction (Rivas Ch 7)
- **Age-specific vital sign ranges** for paediatric patients — record cuff size, route, position (Lehmann Ch 31)
- **Age-specific laboratory normal ranges** — adult ranges are dangerous for children (Lehmann Ch 31)
- **Incident reporting module** — medication errors, system downtime, alert overrides (Rowlands Ch 50)
- **14 Nursing Sensitive Outcomes** as system quality indicators (Hussey Ch 9)
- **Braden scale** (pressure ulcer risk) and fall risk auto-scoring at admission (Hussey Ch 9)
- **Task resumption aid** — bookmark clinician's position on interruption, highlight incomplete fields on return (Coiera Ch 4)
- **Swiss cheese model** with layered defences (Coiera Ch 13)

### 3.3 Paediatric Safety

- **WHO growth charts** with Z-scores, percentiles, growth velocity, prematurity correction (Lehmann Ch 32)
- **Mother-baby dyad linkage** — maternal record linked to neonatal record at birth (Lehmann Ch 4)
- **Catch-up immunisation schedule generation** when doses are missed (Lehmann Ch 17-18)
- **Guardian consent complexity** — consent-by-proxy, multiple guardians, emancipated minors, adolescent confidentiality (Lehmann Ch 5)
- **Developmental screening** — ASQ/PEDS tools triggering referral pathways (Lehmann Ch 6)

---

## 4. UX and Adoption Design

### 4.1 Clinical Workflow

- **Single-page OPD clinical summary** — vitals, problems, labs, meds, allergies visible without scrolling (Rowlands Ch 35)
- **Configurable workflow state machines** per facility type — mission vs government protocols (Brown Ch 4)
- **Semi-structured nursing notes** — coded templates + mandatory free-text narrative (Hussey Ch 7)
- **NANDA-I/NIC/NOC care plan model** — nursing diagnoses linked to interventions linked to outcomes (Hussey Ch 7)
- **Evidence-based data visualisation** — lab trend lines, icon-based severity, task-specific summary views (Coiera Ch 4)
- **Computer-assisted ICD coding** — searchable lookup mapping local terms to codes, auto-suggest from symptoms (WHO Manual Ch 2)

### 4.2 Ward Management

- **Real-time nurse manager dashboard** — bed census, acuity scores, staffing vs actual, patient churn rate (Hussey Ch 9)
- **C-HOBIC minimum dataset** at admission/shift/discharge — functional status, continence, symptoms, safety outcomes (Hussey Ch 3)
- **One-handed tablet design** for bedside drug rounds (Hussey Ch 3)

### 4.3 Adoption Strategy

- **Per-module activation** — facility starts with registration + OPD, adds modules progressively (WHO Manual Ch 5)
- **Parallel-run mode** — printable ward sheets and MAR forms mirroring paper formats during transition (Rowlands Ch 50)
- **Downtime kit** — pre-printable patient lists, medication sheets, census forms for offline use (WHO Manual Ch 4)
- **Structured onboarding bundled into subscription** — workflow mapping, super-user training, 30/60/90 day check-ins (Rowlands Ch 48)
- **Data quality enforcement at point of entry** — mandatory fields, structured dropdowns, completion checklists (WHO Manual Ch 1)
- **Auto-save every form interaction** — power-loss resilience (WHO Manual Ch 3)
- **Interruption recovery** — session state persistence, resume without data loss (Volpe Ch 7)

### 4.4 Patient Engagement

- **Patient Activation Measure (PAM)** scoring in patient portal (Volpe Ch 2)
- **Digital nudging for ART/TB adherence** — SMS reminders, adherence streak visualisation, opt-out appointment scheduling (Rivas Ch 10)
- **SDoH screening (PRAPARE/ICD-10 Z-codes)** embedded in patient intake (Volpe Ch 24)

---

## 5. Commercial Strategy Enhancements

- **Quadruple Aim sales positioning** — patient experience, population health, cost reduction, provider experience (Rivas Ch 1)
- **CHW app as go-to-market channel** for government and NGO contracts (Rivas Ch 13)
- **Missing charge reports** matching encounters to billing to catch revenue leakage (Volpe Ch 4)
- **Drug supply chain hash-chain** for pharmacy stock provenance — combat counterfeit medicines (Rivas Ch 9)
- **Store-and-forward telemedicine** for rural-to-urban specialist consultations (Coiera Ch 21)
- **RPA-ready task automation layer** for billing/claims (Volpe Ch 9)
- **India market entry** — fragmented national landscape, no entrenched competitor (Sinha Ch 25)

---

## 6. Directory Structure

```
projects/Medic8/
+-- README.md
+-- DOCUMENTATION-STATUS.md
+-- _context/
|   +-- vision.md
|   +-- domain.md
|   +-- features.md
|   +-- tech_stack.md
|   +-- business_rules.md
|   +-- quality_standards.md
|   +-- glossary.md
|   +-- stakeholders.md
|   +-- personas.md
|   +-- quality-log.md
|   +-- metrics.md
|   +-- gap-analysis.md
|   +-- competitor-analysis.md
|   +-- payment-landscape.md
|   +-- literature-insights.md
+-- 01-strategic-vision/
|   +-- 01-prd/manifest.md
|   +-- 02-vision-statement/manifest.md
|   +-- 03-business-case/manifest.md
+-- 02-requirements-engineering/
|   +-- 01-srs/manifest.md
|   +-- 02-user-stories/manifest.md
|   +-- 03-stakeholder-analysis/manifest.md
+-- 03-design-documentation/
|   +-- 01-hld/manifest.md
|   +-- 02-lld/manifest.md
|   +-- 03-api-spec/manifest.md
|   +-- 04-database-design/manifest.md
|   +-- 05-ux-spec/manifest.md
+-- 04-development-artifacts/
|   +-- 01-technical-spec/manifest.md
|   +-- 02-coding-guidelines/manifest.md
+-- 05-testing-documentation/
|   +-- 01-test-strategy/manifest.md
|   +-- 02-test-plan/manifest.md
|   +-- 03-test-report/manifest.md
+-- 06-deployment-operations/
|   +-- 01-deployment-guide/manifest.md
|   +-- 02-runbook/manifest.md
+-- 07-agile-artifacts/
|   +-- 01-sprint-planning/manifest.md
|   +-- 02-dod/manifest.md
|   +-- 03-dor/manifest.md
+-- 08-end-user-documentation/
|   +-- 01-user-manual/manifest.md
|   +-- 02-installation-guide/manifest.md
|   +-- 03-faq/manifest.md
+-- 09-governance-compliance/
    +-- 01-traceability-matrix/manifest.md
    +-- 02-audit-report/manifest.md
    +-- 03-compliance/manifest.md
    +-- 04-risk-assessment/manifest.md
```

**15 context files** (11 standard + 4 custom: gap-analysis, competitor-analysis, payment-landscape, literature-insights). All pre-populated from the 17-section specification and 10 health informatics books.

**29 document directories** across 9 phases, each with a `manifest.md`.

---

## 7. NFR Domain Defaults (Uganda-Adapted)

9 requirements injected into `02-requirements-engineering/01-srs/06-nfr.md`, tagged `[DOMAIN-DEFAULT: healthcare]`:

**NFR-HC-001: Patient Data Audit Trail.** The system shall maintain a complete, tamper-proof audit log of all create, read, update, and delete operations on patient health records in compliance with Uganda Data Protection and Privacy Act 2019 Section 24.

**NFR-HC-002: Data Encryption at Rest.** The system shall encrypt all patient health data stored in the database using AES-256-GCM.

**NFR-HC-003: Data Encryption in Transit.** All transmission of patient data shall use TLS 1.2 or higher.

**NFR-HC-004: Session Timeout.** The system shall automatically terminate inactive clinical user sessions after 15 minutes of inactivity.

**NFR-HC-005: Multi-Factor Authentication.** MFA required for Super Admin, Facility Admin, Accountant, and Auditor roles. Optional for clinical staff.

**NFR-HC-006: Availability and Offline Resilience.** 99.9% uptime for cloud. Core clinical modules shall function at full capacity with 0% internet connectivity.

**NFR-HC-007: Data Retention.** Minimum 10 years from last clinical encounter (Uganda MoH policy).

**NFR-HC-008: Breach Notification.** Identify and report affected records within 72 hours (PDPA 2019 Section 31).

**NFR-HC-009: HMIS Compliance.** Auto-populate HMIS 105, 108, and 033b from clinical data without manual re-entry.

---

## 8. Context File Pre-Population Plan

| File | Source | Key Content |
|---|---|---|
| `vision.md` | Spec Sections 1, 9, 10, 16 | Product vision, Africa-first globally configurable, offline-first, global patient identity, 4-phase build, MRR targets |
| `domain.md` | Adapted from `domains/healthcare/INDEX.md` | Uganda regulatory (MoH, NDA, NHIS, PDPA 2019), FHIR R4, ICD-10/11, HL7 v2, HMIS |
| `features.md` | Spec Sections 3, 4, 5, 7, 8 | All modules by tier and phase: 14 core clinical, 8 specialty, 5 admin, 4 financial, 3 HMIS, patient portal |
| `tech_stack.md` | Spec Section 1.2 | PHP 8.2+, MySQL 8.x, Bootstrap 5/Tabler, Kotlin/Jetpack Compose, Swift/SwiftUI, FHIR R4, DICOM, HL7 v2 |
| `business_rules.md` | Spec Sections 3-7, 9, 10, 14 | Clinical rules, financial rules, data rules, HMIS rules, prescribing authority |
| `quality_standards.md` | Spec Sections 10, 11, 15 | Uptime 99.9%, offline capability, bandwidth thresholds, Android 7.0+, FHIR R4 compliance |
| `glossary.md` | Throughout | 50+ terms: HMIS, DHIS2, FHIR, HL7, ICD, PEPFAR, PMTCT, EmONC, NMS, LOINC, SNOMED CT, etc. |
| `stakeholders.md` | Spec Section 2 | 18 built-in roles with access scopes |
| `personas.md` | Spec Section 1.1 | 6 market segments as personas |
| `metrics.md` | Spec Sections 15, 16 | Tier pricing, MRR targets per phase, add-on pricing |
| `gap-analysis.md` | Spec Section 17 | 7 HIGH gaps, 8 MEDIUM gaps, 11 external resources, 6 internal decisions |
| `competitor-analysis.md` | Spec Sections 12, 13 | ClinicMaster: 14 matched + 15 advantages. OpenMRS: 12 matched + 12 gaps. TCO table. |
| `payment-landscape.md` | Spec Sections 6, 15 | MTN MoMo, Airtel Money, NHIS, 20+ insurers, donor funds, subscription via MoMo |
| `literature-insights.md` | 10 books | Clinical safety, data architecture, UX/adoption, commercial strategy enhancements |

---

## 9. Literature Sources

| Book | Author(s) | Key Contributions |
|---|---|---|
| *Health Informatics: A Systems Perspective* | Brown et al. | Event-driven architecture, configurable workflows, disease registries, LOINC, break-the-glass |
| *Health Informatics: Multidisciplinary Approaches* | Volpe (2022) | Medication safety (5 Rights, Tall Man), EMPI, revenue cycle, FHIR resources, SDoH, RPA |
| *Digital Health* | Rivas & Boillat (2023) | Quadruple Aim, EWS for SSA, CHW go-to-market, digital nudging, telemedicine revenue |
| *Practitioner's Guide to Health Informatics in Australia* | Rowlands (2017) | Four-tier alerts, FHIR narrative, parallel-run mode, onboarding methodology, Level 4 interop |
| *Guide to Health Informatics* | Coiera (2015) | EHR as data bus, SNOMED internally / ICD at boundary, consent engine, CDS workflow fit, safety |
| *Pediatric Informatics* | Lehmann, Kim & Johnson (2009) | Weight-based dosing, growth charts, mother-baby linkage, catch-up immunisation, guardian consent |
| *EHR Manual for Developing Countries* | WHO (2006) | Fuzzy patient matching, data quality enforcement, per-module activation, downtime kit, auto-save |
| *Introduction to Nursing Informatics* | Hussey & Kennedy (2021) | Semi-structured notes, ward dashboard, NANDA-I/NIC/NOC, C-HOBIC, NSOs, bedside tablet design |
| *EHR Standards, Coding Systems, Frameworks* | Sinha et al. (2013) | openEHR two-level modelling, ABAC, terminology service, CDA R2, PKI, India market |

---

## 10. Next Steps

1. Invoke `writing-plans` skill to create the implementation plan for scaffolding and populating the Medic8 project
2. Scaffold the full directory structure under `projects/Medic8/`
3. Pre-populate all 15 `_context/` files from the specification and literature
4. Inject 9 Uganda-adapted NFR defaults into the SRS NFR stub
5. Generate Phase 01 documents (PRD, Vision Statement, Business Case)

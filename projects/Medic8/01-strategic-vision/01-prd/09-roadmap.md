# 9 Product Roadmap and Release Strategy

This section defines the four-phase build sequence, module delivery per phase, gate criteria, geographic expansion timeline, and standards traceability for the Medic8 Product Requirements Document.

## 9.1 Release Strategy Overview

Medic8 follows a Water-Scrum-Fall delivery methodology: formal requirements sign-off and phase gate review before each phase; iterative sprints within each phase. No phase begins development until the preceding phase gate criteria are satisfied and `_context/` files for that phase are reviewed and signed off.

| Phase | Name | Timeline | Target Facilities | MRR Target | Key Milestone |
|---|---|---|---|---|---|
| Phase 1 | MVP | Month 1-6 | 10 private clinics (Kampala) | UGX 1.5M | First paying customer |
| Phase 2 | Growth | Month 7-12 | 50 facilities (clinics + mission hospitals + HC IVs) | UGX 15M | First government facility; first mission hospital |
| Phase 3 | Programmes | Month 13-18 | PEPFAR implementing partners, NGOs | UGX 40M | First PEPFAR-funded facility; first cross-border deployment (Kenya/Tanzania) |
| Phase 4 | Enterprise | Month 19-24 | Hospital networks, regional referral hospitals | UGX 100M | First hospital network; first India deployment |

## 9.2 Phase 1 — MVP (Month 1-6)

### 9.2.1 Modules

| Module | Scope | Key Capabilities |
|---|---|---|
| Authentication and RBAC | Core | Session + JWT dual auth; role-based access control with facility-scoped permissions; MFA for admin roles; ABAC for sensitive records (HIV, mental health) |
| Patient Registration | Core | EMPI with probabilistic + fuzzy matching; minimum fields enforced (name, sex, age/DOB, contact); NIN manual entry with format validation; global patient identity layer |
| OPD (Outpatient Department) | Clinical | Single-page clinical summary; vitals capture with age-specific normal ranges; ICD-10 computer-assisted coding; clinical documentation with semi-structured templates; task resumption aid for interruption recovery |
| Pharmacy | Clinical | CPOE with Five Rights enforcement; drug interaction checking (licensed database); allergy-prescription conflict detection; weight-based paediatric dosing with decimal error guards; Tall Man Lettering; dispensing workflow; basic stock tracking |
| Basic Laboratory | Clinical | Test ordering (ServiceRequest); manual result entry; critical value flagging with clinician notification (< 30 min acknowledgment target); LOINC coding from day 1 |
| Billing (Cash) | Financial | Cash billing; receipt generation; mobile money integration (MTN MoMo, Airtel Money); missing charge detection; daily reconciliation report |
| Appointments | Operational | Appointment scheduling; SMS reminders via Africa's Talking; walk-in queue management |
| CDS Engine | Clinical safety | Four-tier alert architecture (Info / Warning / Serious / Fatal); override logging with clinician ID, timestamp, reason, patient ID, alert ID; per-facility override rate tracking |

### 9.2.2 Infrastructure (Phase 1)

- Multi-tenant SaaS deployment with `facility_id` row-level isolation
- Offline-first architecture for all clinical modules (Room database on Android)
- openEHR Reference Model and initial Archetypes (Uganda)
- Terminology service: ICD-10, LOINC, RxNorm, ATC (offline bundles + server)
- FHIR R4 data model (internal); API exposure deferred to Phase 3
- Auto-save on every form interaction; session state persistence
- Tamper-proof audit trail for all PHI CRUD operations
- Configurable consent engine (Uganda: routine clinical consent model)
- Parallel-run mode: printable ward sheets mirroring paper formats
- Downtime kit: pre-printable patient lists, medication sheets

### 9.2.3 Pre-Development Prerequisites

All 7 HIGH-priority gaps must be resolved before Phase 1 development begins:

| Gap | Description | Resolution Action |
|---|---|---|
| HIGH-001 | Drug interaction database not specified | Licence DrugBank, RxNorm/NLM, or NDA formulary |
| HIGH-002 | PDPA 2019 healthcare data compliance not documented | Engage Uganda data protection lawyer; document consent categories and lawful basis |
| HIGH-003 | UMDPC/NDA software registration status unknown | Contact UMDPC and NDA for regulatory determination |
| HIGH-004 | CDS specificity not defined | Define alert types, override workflow, liability disclaimer; consult practising clinician |
| HIGH-005 | Confidential record access controls not defined | Implement ABAC for HIV, mental health, reproductive health, substance abuse records |
| HIGH-006 | Emergency cross-facility access not fully specified | Define two-factor confirmation, data scope, 24-hour expiry, patient SMS notification, audit trail |
| HIGH-007 | HMIS form version management not specified | Version-control mappings in configuration tables; 30-day update turnaround |

### 9.2.4 Phase 1 Gate Criteria

All criteria must be satisfied before Phase 2 begins:

1. All 7 HIGH gaps resolved and documented
2. Core clinical workflow tested end-to-end (registration → consultation → prescription → dispensing → billing → receipt)
3. Medication safety validation complete (drug interactions, allergy conflicts, paediatric dosing guards)
4. Zero patient safety incidents attributable to system error during pilot
5. At least 3 pilot clinics live and processing real patients
6. Cash billing reconciliation rate ≥ 95%
7. 100% test pass rate for all Phase 1 modules
8. Facility onboarding demonstrated within 2-4 hours

## 9.3 Phase 2 — Growth (Month 7-12)

### 9.3.1 Modules

| Module | Scope | Key Capabilities |
|---|---|---|
| IPD (Inpatient Department) | Clinical | Bed management; admission/discharge/transfer workflow; medication reconciliation at every transition of care; discharge summary (CDA R2); Braden scale and fall risk auto-scoring at admission |
| Maternity / ANC | Clinical | Antenatal care tracking; delivery records; mother-baby dyad data linkage; partograph; postnatal care; catch-up immunisation schedule |
| Immunisation | Clinical | EPI Uganda schedule; catch-up schedule generation for missed doses; batch tracking; adverse event following immunisation (AEFI) reporting |
| Emergency | Clinical | Triage scoring; Early Warning Scores (NEWS2) calibrated for SSA populations; critical pathway workflows |
| Insurance Management | Financial | Pre-authorisation workflow; claims submission and tracking; reconciliation with 3+ Uganda insurers (AAR, Jubilee, NHIS when available); 3 schemes (Starter) / unlimited (Growth+) |
| HR and Payroll | Administrative | Staff records; payroll processing; leave management; duty roster; up to 100 staff (Growth tier) |
| HMIS 105/108/033b | Reporting | Auto-population from clinical data; version-controlled form mappings; DHIS2 API submission; ≥ 99% accuracy vs manual tally |
| Full Laboratory | Clinical | HL7 v2 analyser interfaces (ORM/ORU); ASTM E1394 for older analysers; full result management; specimen tracking; CPHL interface |
| Radiology | Clinical | DICOM gateway; image storage (AWS S3, WiFi-only download for large images); reporting; store-and-forward for specialist consultations |
| Inventory | Operational | Multi-location stock management; reorder triggers; NMS commodity ordering integration; batch/expiry tracking; stock valuation |
| Dental | Clinical | Dental charting; procedure documentation; billing integration |
| Eye Care | Clinical | Visual acuity recording; ophthalmic examination templates; referral pathways |
| Mortuary | Administrative | Body registration; release workflow; documentation |
| Referral Management | Clinical | Electronic referral letters (CDA R2); referral tracking; receiving facility confirmation |
| Medical Records | Administrative | Record retrieval; filing tracking; record completeness auditing |
| Disease Surveillance | Public health | Disease registries (HIV, TB, maternal, NCD) as first-class entities; notifiable disease alerts; outbreak reporting |
| Incident Reporting | Quality | Medication errors, system downtime, alert overrides; accreditation support |
| Nursing | Clinical | Semi-structured nursing notes; NANDA-I/NIC/NOC care plan model; nurse manager dashboard (bed census, acuity, staffing); C-HOBIC minimum dataset; Nursing Sensitive Outcomes (NSOs); BCMA for IPD drug rounds |

### 9.3.2 Phase 2 Gate Criteria

1. Phase 1 in production with 10+ paying facilities
2. Zero patient safety incidents reported across all Phase 1 facilities
3. Insurance claim submission and reconciliation functional with at least 3 Uganda insurers
4. HMIS monthly report export validated by MoH field officer (≥ 99% accuracy)
5. At least 1 government facility (HC IV) onboarded
6. At least 1 mission hospital onboarded

## 9.4 Phase 3 — Programmes (Month 13-18)

### 9.4.1 Modules

| Module | Scope | Key Capabilities |
|---|---|---|
| HIV/AIDS Programme | Clinical / reporting | ART register; regimen tracking; viral load monitoring; TX_CURR, TX_NEW, TX_PVLS indicators; defaulter tracing; digital nudging for ART adherence (SMS reminders, streak visualisation); ABAC-enforced access |
| TB Programme | Clinical / reporting | TB register; treatment outcomes; MDR-TB tracking; PEPFAR TB indicators |
| FHIR R4 API | Interoperability | 14 FHIR resource types exposed via RESTful API; HTML narrative fallback; SMART on FHIR for third-party apps; ONC certification test suite |
| PEPFAR MER Indicators | Reporting | TX_CURR, TX_NEW, TX_PVLS, and other MER indicators; automated calculation from clinical data; < 1% variance vs manual calculation; DATIM-compatible export |
| CHW/VHT Mobile App | Community health | Simplified registration, immunisation, ANC on low-end Android (2G); offline-first; sync to facility record; household visit tracking |
| Patient Mobile App | Patient engagement | Appointment booking; lab result viewing; medication reminders; Patient Activation Measure (PAM) scoring; prescription refill requests; Android 7.0+ / iOS 15.0+ |
| Telemedicine | Clinical | Store-and-forward (dermatology, radiology, pathology); video consultation scheduling; regulatory compliance verified against Uganda MoH guidelines |
| Nutrition | Clinical | Nutritional assessment; WHO growth charts with Z-scores (gestational age correction for premature infants); feeding programme tracking |
| Community Health | Public health | Community outreach planning; VHT supervision; household health profiles |
| SDoH Screening | Clinical | PRAPARE tool embedded in patient intake; ICD-10 Z-codes for social determinants (housing, food security, education); relevant for NGO facilities |
| Developmental Screening | Paediatric | ASQ, PEDS screening tools triggering referral pathways |

### 9.4.2 Phase 3 Gate Criteria

1. FHIR R4 conformance tested against ONC certification test suite for 14 resource types
2. PEPFAR MER indicators (TX_CURR, TX_NEW, TX_PVLS) validated against manual calculation with < 1% variance
3. First OpenMRS/UgandaEMR data migration completed successfully
4. At least 1 PEPFAR-funded facility onboarded
5. At least 1 cross-border deployment (Kenya or Tanzania) operational

## 9.5 Phase 4 — Enterprise (Month 19-24)

### 9.5.1 Modules

| Module | Scope | Key Capabilities |
|---|---|---|
| Theatre / Surgical | Clinical | Surgical scheduling; WHO surgical safety checklist; anaesthesia record; procedure documentation; post-operative monitoring |
| Blood Bank | Clinical | UBTS integration; blood product inventory; cross-match records; transfusion reactions; expiry tracking |
| PACS (Picture Archiving and Communication System) | Clinical | Full DICOM image management; radiologist worklist; image sharing across facilities; integration with radiology module |
| Ambulance Management | Operational | Dispatch tracking; GPS-based nearest facility routing; pre-hospital care documentation; handoff to emergency module |
| Physiotherapy | Clinical | Treatment plans; progress tracking; outcome measurement; appointment scheduling |
| Director Platform | Enterprise | Multi-facility consolidated dashboard; cross-site patient record sharing with sub-second lookup; comparative facility performance analytics; aggregated financial reporting |
| Advanced AI Analytics | Enterprise | Predictive analytics (readmission risk, disease outbreak detection); prescribing pattern analysis; revenue forecasting; population health dashboards |
| RPA for Insurance Claims | Automation | Bot-driven claims follow-up; automated claim status checking; denial management workflow; missing documentation alerts |
| Drug Supply Chain Verification | Safety | Lightweight hash-chain for pharmacy stock provenance; counterfeit medicine detection; batch verification against NDA records |

### 9.5.2 Phase 4 Gate Criteria

1. 50+ active facilities across all tiers
2. Director Platform validated with at least 1 multi-facility network
3. Multi-facility patient record sharing demonstrated across at least 2 sites with sub-second lookup
4. Insurance claims processing validated with 3+ insurers
5. Enterprise SLA defined and tested
6. PACS integration tested with at least 1 radiology department
7. Consolidated Director dashboard operational

## 9.6 Geographic Expansion Timeline

| Market | Entry Phase | Regulatory Profile | Key Requirements | Target Segment |
|---|---|---|---|---|
| Uganda | Phase 1 | PDPA 2019, NDA, UMDPC, HMIS 105/108/033b | Launch market; all modules validated here first | Private clinics, mission hospitals, government facilities |
| Kenya | Phase 3 | Kenya DPA 2019, PPB, Kenya MOH 105 | Kiswahili localisation; Kenya NHIF integration; PPB drug formulary; Huduma Namba patient ID | Private clinics, mission hospitals |
| Tanzania | Phase 3 | EPOCA, TMDA | Kiswahili localisation; NHIF Tanzania; TMDA drug scheduling | Private clinics, mission hospitals |
| Rwanda | Phase 3/4 | Law No. 058/2021, RBC | French localisation; RBC health data standards; community health insurance (Mutuelle de Santé) | Mission hospitals, government facilities |
| Nigeria | Phase 4 | NDPA 2023, NHIA Act | Multi-currency (NGN); NHIA integration; FMOH reporting; scale to 200M population market | Private hospitals, HMO-focused facilities |
| DRC | Phase 4 | DRC data protection framework | French localisation; limited infrastructure (extreme offline-first); CDF currency | NGO/mission hospitals |
| India | Phase 4 | DISHA (draft), ABDM | ABHA health ID integration; HL7 v2.5 + CDA + DICOM; India HMIS; multi-state regulatory variance; INR currency; UIP immunisation schedule; CDSCO formulary | Private hospital chains, clinics |
| Australia | Phase 4+ | Privacy Act 1988, My Health Records Act, TGA | Medicare Number integration; My Health Record connectivity; NIP immunisation; TGA drug formulary; AUD currency; high compliance bar | Specialist clinics, allied health |

## 9.7 Standards Traceability Appendix

This appendix maps each PRD section to the applicable clauses of IEEE 29148-2018 (Systems and Software Engineering — Life Cycle Processes — Requirements Engineering) and IEEE 1233-1998 (Guide for Developing System Requirements Specifications).

| PRD Section | IEEE 29148-2018 Clause | IEEE 1233-1998 Clause | Notes |
|---|---|---|---|
| 1 Executive Summary | 6.4.1 (Business requirements specification) | 4.1 (System definition) | Establishes the business context and problem statement |
| 2 Problem Statement | 6.4.1.2 (Business opportunity) | 4.1.1 (System purpose) | Defines the gap in current solutions |
| 3 Target Users and Market | 6.4.1.3 (Business objectives) | 4.3 (System operational concepts) | Identifies stakeholder groups and market segments |
| 4 Product Vision and Positioning | 6.4.1.1 (Business purpose) | 4.1.2 (System scope) | Competitive positioning and design covenant |
| 5 Feature Overview | 6.4.2 (Stakeholder requirements specification) | 5.1 (Requirements identification) | Module catalogue mapped to stakeholder needs |
| 6 Pricing and Revenue Model | 6.4.1.3 (Business objectives) | 4.2 (System justification) | Subscription tiers and revenue targets |
| 7 Success Metrics | 6.4.1.4 (Success metrics) | 5.3.4 (Testability — measurable requirements) | KPIs with baselines, targets, and measurement methods |
| 8 Constraints and Assumptions | 6.4.3.3 (System requirements — constraints); 6.4.3.4 (Assumptions and dependencies) | 5.2.4 (Design constraints); 5.2.5 (External interface requirements) | Technical, regulatory, business, and clinical safety constraints |
| 9 Roadmap | 6.4.1.5 (Priorities); 6.4.2.3 (User requirements — operational scenarios) | 4.4 (System modes and states — phased capability delivery) | Four-phase build sequence with gate criteria |
| Appendix: Gap Analysis | 6.4.3.4 (Assumptions and dependencies) | 5.3.1 (Completeness) | HIGH and MEDIUM gaps requiring resolution |
| Appendix: Tech Stack | 6.4.3.3 (System requirements — design constraints) | 5.2.4 (Design constraints) | Technology selections and rationale |
| Appendix: Quality Standards | 6.4.3.2 (System requirements — non-functional) | 5.2.3 (Performance requirements) | Availability, performance, security, data quality targets |
| Cross-cutting: Terminology | 6.4.1.6 (Terms and definitions) | 3 (Definitions, acronyms, and abbreviations) | ICD-10, FHIR, HMIS, PDPA, EMPI, ABAC, CDS, CDA, DICOM, LOINC, SNOMED CT |
| Cross-cutting: Traceability | 6.1 (Requirements engineering process overview — traceability) | 5.3.3 (Traceability) | Each requirement traceable to business goal and test case |

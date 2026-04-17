# 8 Constraints, Assumptions, and Dependencies

This section documents the binding constraints, working assumptions, and external dependencies that shape the Medic8 platform design, development sequence, and go-to-market strategy. Each item is classified by type, priority, and the phase where it takes effect.

## 8.1 Constraints

### 8.1.1 Technical Constraints

| ID | Constraint | Rationale | Phase |
|---|---|---|---|
| TC-001 | Backend: PHP 8.2+ (strict typing), MySQL 8.x InnoDB, Redis 7, Laravel Horizon. Frontend: Bootstrap 5 / Tabler UI, vanilla JavaScript + jQuery. Mobile: Kotlin/Jetpack Compose (Android), Swift/SwiftUI (iOS). | Shared technology stack and skill set with Academia Pro. Solo developer must maintain both products without context-switching penalty. | All |
| TC-002 | Offline-first architecture required for all clinical modules (patient registration, OPD consultation, prescribing, dispensing, lab result entry). | Ugandan health facilities experience intermittent power and connectivity. Clinical workflows must not halt during outages. Room database (Android) and Core Data/SwiftData (iOS) provide local storage; sync engine reconciles on connectivity restoration. | Phase 1+ |
| TC-003 | Mobile app must support Android 7.0+ (API level 24) on devices with 1 GB RAM. | Target market includes 5-year-old budget phones commonly used by clinical staff in Uganda. | Phase 1+ |
| TC-004 | System must function for real-time clinical use on 256 Kbps bandwidth; full sync requires 1 Mbps; view-only mode on any SMS-capable connection. | Bandwidth constraints in rural and peri-urban facilities. Performance tiers defined in `quality_standards.md` Section 2. | Phase 1+ |
| TC-005 | FHIR R4 compliance required for interoperability. 14 FHIR resource types exposed via RESTful API with HTML narrative fallback. SMART on FHIR support for third-party app integration. | Interoperability with PEPFAR systems, DHIS2, and international health information exchanges. | Phase 1 (data model); Phase 3 (API exposure) |
| TC-006 | HL7 v2 messaging (ORM/ORU) required for laboratory analyser interfaces. ASTM E1394 support for older analysers. | Laboratory analysers in Ugandan facilities use HL7 v2 or ASTM serial protocols. | Phase 1 (basic lab); Phase 2 (full lab) |
| TC-007 | openEHR two-level modelling: stable Reference Model (database schema) + configurable clinical Archetypes per country/facility. | Enables multi-country clinical configurability without forking the codebase. Uganda launch with expansion to Kenya, Tanzania, Rwanda, Nigeria, India, Australia. | Phase 1 |
| TC-008 | Multi-tenant architecture with row-level `facility_id` isolation enforced at the Repository layer before every query. | Centralised SaaS model. Patient data must never leak across facility boundaries. | Phase 1 |
| TC-009 | Encryption: AES-256-GCM at rest for all patient health data; TLS 1.2+ in transit on all endpoints; TLS 1.0/1.1 disabled. | PDPA 2019 Section 24 and healthcare data protection baseline. | Phase 1 |
| TC-010 | Session timeout: 15 minutes inactive for clinical users. MFA required for Super Admin, Facility Admin, Accountant, Auditor. | Security baseline per `quality_standards.md` Section 3. | Phase 1 |

### 8.1.2 Regulatory Constraints

| ID | Constraint | Rationale | Phase |
|---|---|---|---|
| RC-001 | Uganda Data Protection and Privacy Act 2019 (PDPA) compliance mandatory before launch. Consent categories defined per data type (routine clinical, HIV, mental health, reproductive health, substance abuse). Breach notification within 72 hours to PDPO. | Gap HIGH-002. Lawful basis for processing each PHI category must be documented. Cross-border data sharing rules required for FHIR/DHIS2 integrations. | Phase 1 (pre-launch) |
| RC-002 | UMDPC/NDA software registration may be required if Medic8 supports prescribing, dispensing, and clinical decision support. | Gap HIGH-003. Determination pending regulatory enquiry. This is a blocker before commercial sale to licensed health facilities. | Phase 1 (pre-launch) |
| RC-003 | HMIS 105 (Outpatient), HMIS 108 (Inpatient), and HMIS 033b (Laboratory) compliance required for government facility customers. HMIS form mappings must be version-controlled in configuration tables, not hardcoded. | Uganda MoH mandatory reporting. Gap HIGH-007 requires a 30-day maximum turnaround for updating mappings after MoH publishes a new form version. | Phase 2 |
| RC-004 | Country-specific data protection laws required for each expansion market: Kenya DPA 2019, Tanzania EPOCA, Rwanda Law No. 058/2021, Nigeria NDPA 2023, India DISHA, Australia Privacy Act 1988, USA HIPAA (PEPFAR scope). | Each deployment must activate the applicable regulatory profile at tenant configuration time. The system shall not permit operation without an assigned regulatory profile. | Per market entry |
| RC-005 | Drug interaction database must be licensed from an authoritative source (DrugBank, RxNorm/NLM, or Uganda NDA formulary), not built in-house. | Gap HIGH-001. Clinical safety liability and data quality. Building a proprietary drug interaction database carries unacceptable risk for a solo development team. | Phase 1 (pre-CDS activation) |
| RC-006 | Clinical decision support must be decision-support only, not decision-making. Terms of Service must explicitly disclaim clinical liability; clinical liability remains with the prescribing clinician. | Gap HIGH-004. CDS provides alerts; the clinician makes the decision. Every alert and override must be audited. | Phase 1 |
| RC-007 | HIV, mental health, reproductive health, and substance abuse records require a separate access tier using Attribute-Based Access Control (ABAC) layered on RBAC. "Break the glass" emergency access with mandatory post-access audit. | Gap HIGH-005. Not all clinical staff should see HIV status. Patient SMS notification required when emergency access is exercised. | Phase 1 |
| RC-008 | Data retention: minimum 10 years from last clinical encounter per Uganda MoH policy. | `quality_standards.md` Section 3. | All |
| RC-009 | Telemedicine regulatory compliance must be verified against Uganda MoH telemedicine guidelines before telemedicine module launch. | MEDIUM gap. Regulatory landscape evolving. | Phase 3 |
| RC-010 | Prescribing authority rules: clinical officers and nurses have different prescribing scopes per Uganda Medical and Dental Practitioners Act. The system must enforce role-based prescribing restrictions. | MEDIUM gap. | Phase 1 |

### 8.1.3 Business Constraints

| ID | Constraint | Rationale | Phase |
|---|---|---|---|
| BC-001 | Solo development team (Peter, Chwezi Core Systems). No additional developers, QA engineers, or DevOps staff. | All architecture, development, testing, deployment, sales, and support executed by one person. This constraint drives the choice of shared tech stack (TC-001), phased delivery, and automation-first approach. | All |
| BC-002 | Medic8 must share codebase patterns, technology stack, and operational skill set with Academia Pro. | Reduces context-switching cost and enables code reuse (authentication, multi-tenancy, billing, mobile money integration, RBAC patterns). | All |
| BC-003 | Subscription pricing must be accessible to the African healthcare market: UGX 150,000/month (Starter) to UGX 700,000/month (Pro), with custom Enterprise pricing. | Target facilities operate on thin margins. Pricing must undercut OpenMRS TCO (USD 35,000-130,000 over 3 years) while sustaining revenue-funded growth. | All |
| BC-004 | No venture capital. Revenue-funded growth only. | Cash flow from paying facilities funds all development, infrastructure, and expansion. No external runway. | All |
| BC-005 | 7 HIGH-priority gaps must be resolved before clinical module development begins (Phase 1 gate criterion). | Gaps HIGH-001 through HIGH-007 involve clinical safety, regulatory compliance, and data protection. Proceeding without resolution creates patient safety and legal risk. | Phase 1 (pre-development) |

### 8.1.4 Clinical Safety Constraints

| ID | Constraint | Rationale | Phase |
|---|---|---|---|
| CS-001 | Four-tier CDS alert architecture (Info / Warning / Serious / Fatal). Fatal alerts are hard stops (not overridable). Serious alerts require documented override reason. | Literature insight: competitors use binary on/off alerts with 90%+ override rates. Tiered architecture reduces alert fatigue while maintaining safety for critical interactions. | Phase 1 |
| CS-002 | Five Rights of Medication Administration enforced at CPOE: right patient, drug, dose, route, time. | 56% of medication errors occur at prescribing (Volpe Ch 6). | Phase 1 |
| CS-003 | Weight-based paediatric dosing with inline mg/kg calculators, dose rounding, and adult ceiling dose cap. Decimal error guards to prevent 10x/100x overdose. | Children face 3x the adult risk of medication errors (Lehmann Ch 25-26). | Phase 1 |
| CS-004 | Age-specific vital sign and lab normal ranges. Adult ranges must not be applied to paediatric patients. | Adult reference ranges are clinically dangerous for children (Lehmann Ch 31). | Phase 1 |
| CS-005 | Tall Man Lettering for look-alike/sound-alike drugs (e.g., hydrOXYzine vs hydrALAZINE). | Critical in Sub-Saharan Africa where multiple generics share similar names (Volpe Ch 6). | Phase 1 |
| CS-006 | Auto-save every form interaction, not just on submit. Session state persistence for interruption recovery. | Power-loss resilience. Clinical environments average 6-7 interruptions per hour (Coiera Ch 4). | Phase 1 |

## 8.2 Assumptions

Each assumption carries risk if invalidated. The mitigation column identifies the contingency action.

| ID | Assumption | Confidence | Mitigation if Invalid | Phase |
|---|---|---|---|---|
| A-001 | Private clinics in Kampala are willing to pay UGX 150,000/month for SaaS healthcare software. | Medium | Offer freemium tier for patient registration only; convert to paid on pharmacy/billing module activation. Validate with 5 clinic owner interviews before Phase 1 launch. | Phase 1 |
| A-002 | Facilities with unreliable internet will accept offline-first architecture with periodic sync. | High | Offline-first is a core differentiator vs ClinicMaster. If rejected, investigate dedicated connectivity partnerships (e.g., bundled data SIM). | Phase 1 |
| A-003 | Mobile money (MTN MoMo and Airtel Money) is the primary payment channel for both patient billing and Medic8 subscription payments. | High | Add bank transfer and card payment as secondary channels. Mobile money penetration in Uganda exceeds 60%. | Phase 1 |
| A-004 | NHIS Uganda will publish a provider API within 12 months of Medic8 launch. | Low | Build insurance claims module with manual submission workflow first; add API integration when available. NHIS API is a MEDIUM gap. | Phase 2 |
| A-005 | Uganda MoH will continue to require HMIS 105/108 reporting in the current format for the next 3 years. | High | HMIS form mappings are version-controlled in configuration tables (gap HIGH-007 resolution). 30-day turnaround for format updates. | Phase 2 |
| A-006 | ClinicMaster will not pivot to a SaaS delivery model within the Medic8 launch window (24 months). | Medium | Accelerate Phase 1 launch to establish market position. ClinicMaster's desktop architecture makes SaaS pivot technically difficult. | Phase 1 |
| A-007 | OpenMRS implementing partners are price-sensitive and open to commercial alternatives with lower total cost of ownership. | Medium | Target PEPFAR-funded facilities where TCO reduction is a procurement criterion. Provide OpenMRS data migration tool as acquisition accelerator. | Phase 3 |
| A-008 | Licensed drug interaction databases (DrugBank, RxNorm) provide adequate coverage for drugs dispensed in Ugandan facilities, including local generics. | Medium | Supplement licensed database with Uganda NDA Essential Medicines List mappings. Flag uncovered drugs with `[DRUG-DB-GAP]` for pharmacist manual review. | Phase 1 |
| A-009 | PEPFAR implementing partners will accept a commercial SaaS platform as an alternative to open-source (OpenMRS/UgandaEMR) for MER indicator reporting. | Medium | Demonstrate PEPFAR MER indicator accuracy within 1% variance of manual calculation. Offer FHIR-based data export to existing PEPFAR data pipelines as a bridge. | Phase 3 |
| A-010 | A single consulting clinician (engaged per gap HIGH-004 resolution) can validate CDS alert categories and thresholds for the Uganda market. | Medium | Engage a second clinician for independent validation. Cross-reference against WHO Essential Medicines List interaction data. | Phase 1 |
| A-011 | Uganda's regulatory environment will not require Medic8 to register as a medical device (gap HIGH-003 pending). | Low | Engage UMDPC and NDA for formal determination. If registration is required, budget 3-6 months for the process. This is a launch blocker. | Phase 1 (pre-launch) |
| A-012 | AWS S3 provides sufficient availability and compliance posture for clinical document and medical image storage in the East Africa region. | High | AWS has an Africa (Cape Town) region. If latency is unacceptable, evaluate Azure South Africa or a Uganda-based hosting provider for data residency. | Phase 1 |

## 8.3 External Dependencies

| ID | Dependency | Provider | Status | Impact if Unavailable | Mitigation | Phase |
|---|---|---|---|---|---|---|
| D-001 | SMS gateway (appointment reminders, OTP, critical lab value notifications, patient emergency access alerts) | Africa's Talking | Available; API documented | Appointment reminders fail; OTP-based MFA unavailable; patient notifications delayed | Integrate secondary SMS provider (e.g., Yo! Uganda) as failover | Phase 1 |
| D-002 | Mobile money — subscription payments and patient billing | MTN MoMo API | Available; API documented | Subscription collection fails; patient billing reverts to cash-only | Add Airtel Money (D-003) as primary alternative; bank transfer as tertiary | Phase 1 |
| D-003 | Mobile money — subscription payments and patient billing | Airtel Money API | Available; API documented | Reduced payment channel coverage (Airtel holds approximately 30% of Uganda mobile money market) | MTN MoMo (D-002) covers approximately 60% of market; bank transfer as fallback | Phase 1 |
| D-004 | HMIS aggregate reporting submission | DHIS2 API (hmis2.health.go.ug) | Available; API documented | Government facility customers cannot submit HMIS reports electronically; must export and manually upload | Generate DHIS2-compatible CSV/ADX export for manual upload | Phase 2 |
| D-005 | Drug interaction checking, allergy-drug conflict detection | Licensed drug interaction database (DrugBank / RxNorm / NDA formulary) | Not yet licensed (gap HIGH-001) | CDS medication safety alerts non-functional; Phase 1 gate fails | Resolve HIGH-001 before clinical development. No acceptable workaround — this is a hard dependency. | Phase 1 (blocker) |
| D-006 | Clinical terminology resolution (ICD-10, SNOMED CT, LOINC, RxNorm, ATC) | FHIR terminology server (self-hosted or cloud) | Architecture defined; not yet deployed | Coded diagnoses, lab results, and medication orders lack standardised terminology; interoperability degraded | Deploy terminology server during Phase 1 infrastructure setup. Use offline terminology bundles as fallback. | Phase 1 |
| D-007 | Clinical document and medical image storage | AWS S3 | Available | Clinical documents (discharge summaries, referral letters, radiology images) cannot be stored or retrieved | Evaluate Azure Blob Storage or DigitalOcean Spaces as alternative. Local NAS as emergency fallback for single-facility deployments. | Phase 1 |
| D-008 | National Health Insurance Scheme claims submission | NHIS Uganda API | Not yet published (MEDIUM gap) | Insurance claims for NHIS-covered patients require manual submission; reconciliation delays | Build manual claims submission workflow; add API integration when published (assumption A-004) | Phase 2 |
| D-009 | National ID verification for patient identity | NIRA (Uganda National Identification and Registration Authority) | API availability unknown | NIN-based patient identity verification unavailable; EMPI relies on name + DOB + phone + manual NIN entry | Manual NIN entry with format validation; integrate NIRA API when available | Phase 2 |
| D-010 | PEPFAR MER indicator definitions and validation rules | PEPFAR/DATIM (datim.org) | Available; indicator reference guide published annually | MER indicator reports cannot be generated or validated | Download current FY MER Indicator Reference Guide; implement indicator logic from published definitions | Phase 3 |
| D-011 | Radiology image management | DICOM gateway | Architecture defined; not yet deployed | Radiology module cannot receive, store, or display medical images from imaging equipment | Deploy DICOM gateway during Phase 2 (radiology module). Store-and-forward workflow as interim. | Phase 2 |
| D-012 | Laboratory analyser connectivity | HL7 v2 / ASTM E1394 interfaces | Protocol support designed; analyser-specific configurations pending | Lab results require manual entry instead of auto-population from analysers | Manual lab result entry is the baseline workflow; analyser integration is an enhancement | Phase 1 (manual); Phase 2 (automated) |

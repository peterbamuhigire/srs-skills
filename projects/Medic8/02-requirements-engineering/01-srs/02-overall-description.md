# 2 Overall Description

## 2.1 Product Perspective

Medic8 is a standalone multi-tenant SaaS healthcare information management system. It is not a replacement module within an existing system, nor is it a component of a larger product suite. The platform operates as a centralised cloud-hosted service with offline-capable client applications, serving multiple independent health facilities (tenants) from a single deployment with row-level data isolation via `facility_id`.

### System Context

Medic8 sits at the centre of a health facility's digital operations, interfacing with external systems across 7 integration domains:

**1. National HMIS Reporting (DHIS2)**
Medic8 auto-populates Uganda HMIS forms (105, 108, 033b) from clinical encounter data and submits aggregate reports to the District Health Information Software 2 (DHIS2) platform via REST API. The integration uses DHIS2 ADX/JSON export format with organisation unit mapping per facility. Data flows outbound from Medic8 to DHIS2; no inbound clinical data is consumed from DHIS2.

**2. Insurance Companies (Claims Processing)**
Medic8 submits pre-authorisation requests, claim batches, and reconciliation reports to insurance providers including NHIS Uganda, AAR Healthcare, Jubilee Insurance, and Prudential. Each insurer exposes a distinct claims API or accepts structured file submissions. Medic8 maintains a configurable scheme register mapping each insurer's benefit schedule, pre-authorisation rules, and claim format.

**3. Mobile Money Providers (Patient Payments)**
Medic8 integrates with MTN Mobile Money and Airtel Money via their respective REST APIs for patient payment collection, refunds, and payment verification. Transactions are initiated from the billing module or patient portal and confirmed via callback. The integration supports micro-payments common in private clinic settings.

**4. Laboratory Analysers (Diagnostic Results)**
Medic8 receives diagnostic results from automated laboratory analysers (Cobas, Mindray, Sysmex) via HL7 v2 messaging (ORM/ORU messages) over MLLP/TCP connections. Legacy analysers that do not support HL7 v2 are interfaced via ASTM E1394 over serial or TCP connections. Result data flows inbound from analysers to Medic8; order messages flow outbound.

**5. Radiology Imaging Systems (PACS)**
Medic8 integrates with Picture Archiving and Communication Systems (PACS) via the DICOM protocol over TCP for radiology image storage, retrieval, and display. The DICOM gateway handles modality worklist (MWL) for scheduling and storage commitment for image archival. Image data resides in the PACS; Medic8 stores study metadata and report text.

**6. National ID Systems (Patient Identity Verification)**
Medic8 verifies patient identity against the National Identification and Registration Authority (NIRA) database via REST API using the National Identification Number (NIN). Future markets add support for Aadhaar (India), Huduma Namba (Kenya), and Medicare Number (Australia) through the country configuration layer. Identity verification is optional and supplements the internal Enterprise Master Patient Index (EMPI).

**7. SMS and Notification Gateways**
Medic8 sends appointment reminders, medication alerts, test result notifications, and missed appointment follow-ups via Africa's Talking REST API for SMS and USSD. WhatsApp Business API integration is planned for facilities that prefer messaging over SMS. Push notifications use Firebase Cloud Messaging (FCM) for Android and Apple Push Notification service (APNs) for iOS.

## 2.2 Product Functions -- Phase Summary

The following table summarises all modules by delivery phase. Module count reflects discrete functional areas, not individual features.

| Phase | Name | Modules | Count |
|---|---|---|---|
| 1 | Foundation | Patient Registration, OPD, Pharmacy, Lab (basic), Billing, Appointments, Auth/RBAC | 7 |
| 2 | Expansion | IPD, Maternity, Immunisation, Emergency, Insurance, HR/Payroll, HMIS, Inventory, Full Lab, Radiology, Dental, Eye Care, Mortuary, Referral, Medical Records, Accounting, Disease Surveillance | 17 |
| 3 | Programmes | HIV/AIDS, TB, FHIR API, PEPFAR MER, CHW App, Patient App, Telemedicine, Nutrition, Community Health | 9 |
| 4 | Advanced Specialty | Theatre, Blood Bank, PACS, Ambulance, Physiotherapy, Director Platform, AI Analytics | 7 |
| | **Total** | | **40** |

### Phase 1 -- Foundation (MVP)

Phase 1 delivers the minimum viable product for a private outpatient clinic. A patient registers, receives triage, consults a doctor, receives a prescription, has laboratory tests ordered and resulted, pays the bill (cash or mobile money), and books a follow-up appointment. All 7 modules are mandatory for Phase 1 acceptance.

### Phase 2 -- Expansion

Phase 2 extends Medic8 to multi-department hospitals. Inpatient admission, maternity, emergency, and specialty clinics (dental, eye care) are added alongside the administrative backbone: insurance, HR/payroll, inventory, accounting, medical records, and HMIS reporting. Disease surveillance enables notifiable disease alerting.

### Phase 3 -- Programmes and Patient Engagement

Phase 3 introduces vertical programme management (HIV/AIDS, TB, nutrition) with PEPFAR MER indicator reporting, the patient-facing mobile application and portal, community health worker (CHW) integration, and the FHIR R4 API for external interoperability.

### Phase 4 -- Advanced Specialty

Phase 4 delivers surgical theatre management, blood bank, PACS integration, ambulance management, physiotherapy, the Director analytics platform for multi-facility networks, and AI-powered analytics.

## 2.3 User Classes and Characteristics

Medic8 supports 18 built-in user roles. Each role is scoped to specific modules and workflows. The following table defines each role's operational characteristics.

| # | Role | Description | Frequency of Use | Technical Proficiency | Clinical Access Level |
|---|---|---|---|---|---|
| 1 | Super Admin | Platform operator (Chwezi Core Systems). Full access across all tenants, global configuration, tenant provisioning, and platform monitoring. | Daily | High | Full (all tenants) |
| 2 | Facility Admin / Medical Director | Manages a single facility. Configures modules, manages staff, reviews audit trails, and generates facility-level reports. | Daily | Medium-High | Full (own facility) |
| 3 | Facility Director / Owner | Aggregate and cross-facility view. Accesses financial dashboards, approval workflows, and strategic reporting. No direct clinical record access. | Weekly | Medium | None (aggregate only) |
| 4 | Doctor / Physician | Conducts OPD consultations and IPD ward rounds. Orders investigations, writes prescriptions, records diagnoses, and generates referral letters. | Daily | Medium | Full clinical (own facility) |
| 5 | Clinical Officer | Same clinical scope as Doctor within regulatory limits. Restricted prescribing authority per Uganda Allied Health Professionals Council regulations. | Daily | Medium | Full clinical (restricted prescribing) |
| 6 | Nurse / Midwife | Records vital signs, triage, nursing notes, drug administration (MAR), maternity/ANC documentation, and immunisation. No prescribing authority. | Daily | Low-Medium | Clinical documentation (no prescribing) |
| 7 | Pharmacist | Dispenses medications, manages pharmacy stock, reviews drug interactions, maintains the narcotic register, and tracks expiry dates. | Daily | Medium | Prescription data only |
| 8 | Lab Technician | Collects samples, enters results, manages quality control records, and triggers critical value alerts. | Daily | Medium | Lab request and result data only |
| 9 | Radiographer | Manages the radiology worklist, enters reports, uploads images, and tracks study status. | Daily | Medium | Radiology request and report data only |
| 10 | Receptionist / Front Desk | Registers patients, books appointments, manages queues, and submits file requests. The role most likely to operate without IT support. | Daily | Low | Registration data only |
| 11 | Records Officer | Tracks physical medical files, archives discharge summaries, generates medical certificates, and manages HMIS form inventory. Read-only clinical access. | Daily | Low-Medium | Read-only clinical |
| 12 | Cashier / Billing Clerk | Collects payments (cash, mobile money), generates receipts, reconciles daily cash, and verifies MoMo transactions. | Daily | Low | Patient account data only |
| 13 | Insurance Clerk | Verifies insurance membership, submits pre-authorisation requests, generates and submits claims, and manages rejections. | Daily | Medium | Insurance and billing data only |
| 14 | Accountant | Manages financial accounting (journal entries, bank reconciliation, financial statements), reviews payroll, and reports on donor funds. Read-only billing access. | Daily | Medium-High | Read-only financial |
| 15 | Store Keeper | Receives goods (GRN), transfers stock, manages expiry, orders from NMS, and conducts stock counts. | Daily | Low-Medium | Inventory data only |
| 16 | Auditor | Read-only access to all financial records, audit trails, compliance reports, and transaction logs. No data modification permitted. | Monthly | High | Read-only financial and audit |
| 17 | Patient / Client | Accesses own medical records, test results, appointments, invoices, payment history, and medication reminders via the patient portal and mobile app. | Weekly | Low | Own records only |
| 18 | Community Health Worker (VHT/CHW) | Registers patients in the community, submits referrals, documents home visits, and reports activities via the CHW Android app. | Daily | Low | Community patient data (assigned area only) |

## 2.4 Operating Environment

### Server Environment

| Component | Specification |
|---|---|
| Language | PHP 8.2+ with strict typing enabled |
| Database | MySQL 8.x InnoDB (strict mode, utf8mb4 charset) |
| High Availability | InnoDB Cluster |
| Cache / Queue | Redis 7 (cache and queue driver) |
| Job Queue | Laravel Horizon |
| Object Storage | AWS S3 (clinical documents, medical images, reports) |
| Operating System | Linux (Ubuntu 22.04 LTS or later recommended) |
| Authentication | Session + JWT dual authentication; Laravel Sanctum for token management |

### Client Environment -- Web

| Component | Specification |
|---|---|
| Supported Browsers | Google Chrome 90+, Mozilla Firefox 90+, Microsoft Edge 90+, Apple Safari 15+ |
| Minimum Resolution | 1024 x 768 pixels |
| UI Framework | Bootstrap 5 / Tabler UI |
| Data Operations | AJAX for all data operations |
| JavaScript | Vanilla JavaScript + jQuery where needed |

### Client Environment -- Mobile

| Platform | Language | UI Framework | Architecture | Offline Storage | Minimum OS |
|---|---|---|---|---|---|
| Android | Kotlin | Jetpack Compose | MVVM | Room database | Android 7.0 (API 24), 1 GB RAM |
| iOS | Swift | SwiftUI | MVVM | Core Data / SwiftData | iOS 15.0 |

### Network Requirements

| Tier | Bandwidth | Capability |
|---|---|---|
| Full sync | 1 Mbps | All features, real-time data synchronisation, image downloads |
| Real-time clinical use | 256 Kbps | Clinical workflows (OPD, prescribing, lab), deferred image loading |
| Minimum useful operation | 64 Kbps | Text-based clinical data, no images |
| Offline mode | 0 Kbps | Core clinical modules operate from local cache; sync on reconnect |
| View-only mode | Any SMS-capable connection | USSD-based patient lookup and appointment confirmation |

## 2.5 Design and Implementation Constraints

### Multi-Tenant Architecture

The system shall use a centralised multi-tenant model with row-level tenant isolation. Every tenant-scoped database table shall include a `facility_id` column. The Repository layer shall enforce `facility_id` filtering before every query. Cross-tenant data access shall be prohibited except through the global patient identity layer (EMPI) under controlled, audited conditions.

### Clinical Modelling

The system shall implement openEHR two-level modelling: a stable Reference Model layer and configurable clinical Archetypes per country and facility. This constraint enables multi-country clinical configurability without schema changes. Clinical templates (e.g., ANC visit form, OPD SOAP note) are defined as Archetype compositions and are editable by facility administrators through the configuration interface.

### Interoperability

The system shall expose a FHIR R4 compliant API covering 14 clinical resource types: Patient, Encounter, Observation, Condition, MedicationRequest, MedicationDispense, DiagnosticReport, ServiceRequest, Immunization, AllergyIntolerance, Procedure, Location, Practitioner, and Organization. Every FHIR response shall include an HTML narrative fallback. The system shall support SMART on FHIR for third-party application substitutability.

### Offline-First Clinical Modules

Core clinical workflows -- patient registration, vital signs capture, prescription writing, dispensing, and lab result entry -- shall operate at full capacity with 0% internet connectivity. The offline-first architecture shall use local storage (Room on Android, Core Data/SwiftData on iOS) and synchronise with the server when connectivity resumes. The system shall detect power restoration and immediately sync the offline queue.

### Data Protection

The system shall comply with the Uganda Data Protection and Privacy Act 2019 (PDPA). All patient health data shall be encrypted at rest using AES-256-GCM and in transit using TLS 1.2 or higher. Patient data shall reside in-country unless the regulatory profile explicitly permits cross-border transfer. The system shall maintain a tamper-proof audit trail of all CRUD operations on patient data per PDPA Section 24. Breach notification shall be completed within 72 hours per PDPA Section 31.

### HMIS Compliance

The system shall auto-populate Uganda HMIS forms (105, 108, 033b) from clinical encounter data. HMIS form mappings shall be stored in configuration tables, not hardcoded. The system shall support DHIS2 ADX/JSON export and direct API push for report submission.

### Technology Stack Constraint

Medic8 shares the same base technology stack as Academia Pro (PHP 8.2+, MySQL 8.x, Bootstrap 5/Tabler, Redis 7, Kotlin/Jetpack Compose for Android, Swift/SwiftUI for iOS). This constraint enables shared infrastructure, deployment tooling, and developer expertise across both products.

## 2.6 Assumptions and Dependencies

### Assumptions

1. Health facilities in the target market have at least intermittent internet connectivity (256 Kbps minimum for real-time use, 0 Kbps supported via offline mode).
2. Clinical staff at target facilities can operate a web browser or mobile application after completing the module-specific onboarding programme. No prior EHR experience is assumed.
3. Each facility designates at least 1 staff member (Facility Admin or Receptionist) who completes full system training and serves as the on-site first-line support contact.
4. Uganda MoH HMIS form versions (105, 108, 033b) remain stable during Phase 1 development. Form version changes during later phases are handled through configurable mappings with a 30-day update turnaround.
5. Mobile money APIs (MTN MoMo, Airtel Money) remain available with stable endpoint contracts. API deprecation or contract changes require a 90-day migration window.
6. Drug interaction data is sourced from a licensed third-party database (DrugBank, RxNorm/NLM, or Uganda NDA formulary). The specific source is an unresolved dependency (see HIGH-001 in gap analysis).
7. Uganda's Data Protection and Privacy Act 2019 is the governing data protection framework for the launch market. No additional healthcare-specific data protection legislation is enacted before Phase 2 completion.
8. The NIRA NIN verification API is available for patient identity verification. If the API is unavailable at Phase 1 launch, NIN is captured as a text field with deferred verification.

### Dependencies

| ID | Dependency | Type | Phase | Impact if Unavailable |
|---|---|---|---|---|
| DEP-001 | Drug interaction database licence (DrugBank, RxNorm, or NDA formulary) | External | 1 | Drug interaction checking disabled; clinical safety risk. Blocks Phase 1 acceptance. |
| DEP-002 | MTN MoMo API credentials and merchant account | External | 1 | Mobile money payments unavailable; cash-only billing. Degrades but does not block. |
| DEP-003 | Airtel Money API credentials and merchant account | External | 1 | Airtel Money payments unavailable; MTN MoMo and cash remain. |
| DEP-004 | Africa's Talking API credentials | External | 1 | SMS/USSD notifications disabled; appointment reminders unavailable. |
| DEP-005 | NIRA NIN verification API access | External | 1 | Patient identity verification deferred to manual NIN entry. |
| DEP-006 | DHIS2 API access and organisation unit mapping | External | 2 | HMIS report submission falls back to manual file export. |
| DEP-007 | NHIS Uganda claims API documentation | External | 2 | Insurance claims submission uses manual file upload instead of API integration. |
| DEP-008 | NMS LMIS data submission format | External | 2 | NMS ordering falls back to manual process outside the system. |
| DEP-009 | PEPFAR MER Indicator Reference Guide (current FY) | External | 3 | PEPFAR indicator reports cannot be validated against official definitions. |
| DEP-010 | UBTS blood transfusion integration specification | External | 4 | Blood bank module operates standalone without national supply chain integration. |
| DEP-011 | Uganda data protection legal review (health data, HIV, mental health) | Internal | 1 | Consent workflows for sensitive data categories cannot be finalised. Blocks HIV module (Phase 3). |
| DEP-012 | UMDPC/NDA software registration enquiry | Internal | 1 | Commercial sale to licensed health facilities may be blocked if registration is required. |
| DEP-013 | CDS liability terms in Terms of Service | Internal | 1 | Clinical decision support alert engine cannot be deployed without legal clarity on liability. |

### Unresolved Gaps

7 HIGH-priority gaps identified in the gap analysis must be resolved before clinical module development begins. These are tracked in `_context/gap-analysis.md` and cover: medication safety (HIGH-001), PDPA compliance for health data (HIGH-002), software medical device classification (HIGH-003), CDS specificity and liability (HIGH-004), HIV/confidential record access controls (HIGH-005), emergency cross-facility record access (HIGH-006), and HMIS form version management (HIGH-007).

*No downstream SRS sections for clinical safety, CDS rules, or sensitive record access shall be marked as final until the corresponding HIGH-priority gap is resolved and signed off by the product owner.*

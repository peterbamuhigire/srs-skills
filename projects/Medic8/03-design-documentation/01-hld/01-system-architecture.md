# System Architecture — Medic8

**Document ID:** DD-01-01
**Project:** Medic8
**Author:** Chwezi Core Systems
**Date:** 2026-04-03
**Version:** 1.0
**Status:** Draft — Pending Consultant Review

---

## 1. Architecture Overview

### 1.1 System Context

Medic8 is a multi-tenant Software-as-a-Service (SaaS) healthcare management system. Each tenant is a health facility (hospital, health centre, clinic) identified by a unique `facility_id`. The platform serves clinical, administrative, and financial workflows across multiple countries, with Uganda as the primary deployment target.

External systems that integrate with Medic8:

- **DHIS2** (hmis2.health.go.ug) — aggregate HMIS data push and individual-level Tracker push
- **Laboratory analysers** — HL7 v2 ORM/ORU messaging over MLLP/TCP (Cobas, Mindray, Sysmex, GeneXpert)
- **PACS/DICOM servers** — radiology image storage and retrieval
- **Mobile money APIs** — MTN Mobile Money, Airtel Money for payment collection
- **SMS/USSD gateway** — Africa's Talking for appointment reminders, critical alerts, breach notifications
- **Insurance platforms** — electronic pre-authorisation and claim submission per insurer API
- **National ID services** — NIN (Uganda), Aadhaar (India), Medicare (Australia) for identity verification
- **Third-party clinical apps** — SMART on FHIR integration

### 1.2 Architectural Style

Medic8 uses a **monolithic application with a modular service layer**. All modules (OPD, IPD, Laboratory, Pharmacy, Billing, HR, HMIS) run within a single Laravel application process, sharing the same database and deployment unit. Module boundaries are enforced at the code level through dedicated service classes, repository classes, and route groups.

An **event-driven internal bus** (Laravel Events) decouples cross-module side effects. A clinical encounter in OPD does not call the Billing service directly; it dispatches an `EncounterCreated` event that the Billing listener handles independently.

**Rationale:** A monolith reduces operational complexity for small facility IT teams (1-2 staff), eliminates inter-service latency on low-bandwidth African networks, and simplifies offline-first synchronisation. The modular service layer preserves the option to extract services later without architectural rework.

### 1.3 Deployment Model

- **Primary:** Cloud-hosted (AWS or equivalent), multi-tenant, accessed via HTTPS
- **Optional:** Local server mode for facilities with unreliable internet — a facility-local instance synchronises with the cloud when connectivity is available
- **Mobile:** Native Android and iOS apps with offline-first local databases that sync to the server API

---

## 2. Logical Architecture

The system is organised into 5 horizontal layers. Every request traverses these layers top-to-bottom; every response traverses bottom-to-top.

### 2.1 Presentation Layer

| Client | Technology | Notes |
|---|---|---|
| Web UI (Staff) | Bootstrap 5 / Tabler commercial template, vanilla JS + jQuery, AJAX, DataTables.js, SweetAlert2, Flatpickr | Session-authenticated, CSRF-protected |
| Android App | Kotlin, Jetpack Compose, MVVM, Dagger Hilt, Retrofit | JWT-authenticated, offline-first via Room |
| iOS App | Swift, SwiftUI, MVVM, async/await | JWT-authenticated, offline-first via Core Data / SwiftData |
| Patient Portal | Bootstrap 5 / Tabler (web), Android, iOS | Own-records-only access, mobile money payment |
| CHW App | Android (Kotlin, Jetpack Compose) | Low-spec device support, 2G/EDGE connectivity, offline-first |

### 2.2 API Layer

| Endpoint Group | Protocol | Purpose |
|---|---|---|
| `/api/v1/*` | RESTful JSON over HTTPS | Primary API for web AJAX, Android, iOS, Patient Portal |
| `/fhir/r4/*` | HL7 FHIR R4 over HTTPS | 14 FHIR resources (Patient, Encounter, Observation, Condition, MedicationRequest, MedicationDispense, DiagnosticReport, ServiceRequest, Immunization, AllergyIntolerance, Procedure, Location, Practitioner, Organization) |
| `/hl7/v2` | HL7 v2 over MLLP/TCP | Laboratory analyser interface — ORM (orders) and ORU (results) messages |
| `/smart` | OAuth 2.0 (SMART on FHIR) | Third-party clinical app authorisation |

All API routes pass through the `AuthenticateTenant` middleware, which binds the authenticated user's `facility_id` to the request context (see Section 3.2).

### 2.3 Business Logic Layer

Each functional module has a dedicated service class. Cross-cutting clinical services are shared across modules:

| Service | Responsibility |
|---|---|
| `OpdService` | Consultation workflow: triage, SOAP notes, diagnosis, orders, prescriptions, referrals |
| `IpdService` | Admission, bed management, ward rounds, nursing notes, drug rounds, discharge |
| `LabService` | Lab request lifecycle, sample tracking, result entry, critical value escalation |
| `PharmacyService` | Dispensing, stock management, narcotic register, formulary, expiry tracking |
| `BillingService` | Auto-charge posting, payment collection, receipt generation, reconciliation |
| `InsuranceService` | Pre-authorisation, claim generation, submission, rejection management |
| `AccountingService` | Journal entries, ledger management, financial statements, donor fund accounting |
| `HrService` | Staff directory, attendance, leave, payroll, licence tracking |
| `InventoryService` | GRN, stock transfers, adjustments, minimum levels, NMS ordering |
| `HmisService` | HMIS 105/108/033b auto-population, DHIS2 push, PEPFAR MER indicators |
| `AppointmentService` | Booking, SMS/WhatsApp reminders, queue management |
| `ReferralService` | Internal/external referral, electronic referral letter |
| **CDS Engine** | Four-tier drug interaction alerts (Info/Warning/Serious/Fatal), Five Rights validation, weight-based dosing, NEWS2 scoring, Braden scale |
| **Terminology Service** | Single gateway to ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm, ATC. SNOMED CT stored internally; ICD-10 mapped at the reporting boundary |
| **Consent Engine** | Configurable per jurisdiction — opt-in (India ABDM), opt-out (Australia My Health Record), minimal digital consent (Uganda). Governs data sharing, FHIR export, and cross-facility access |
| **EMPI Service** | Enterprise Master Patient Index: probabilistic matching, duplicate detection, patient merge/unmerge |
| **Event Dispatcher** | Laravel Events — dispatches domain events to registered listeners (see Section 5) |

### 2.4 Data Access Layer

**Pattern:** Repository pattern with tenant-scoped queries.

Every repository for a tenant-scoped entity extends `TenantAwareRepository`. The base class resolves `facility_id` from the service container on instantiation and appends `WHERE facility_id = ?` to every query builder chain.

```
TenantAwareRepository (abstract)
├── resolves facility_id from app('facility_id') on construct
├── all()      → query()->where('facility_id', $this->facilityId)->get()
├── find($id)  → query()->where('facility_id', $this->facilityId)->findOrFail($id)
├── create()   → sets facility_id on the model before save
├── update()   → scopes the update to facility_id
├── delete()   → scopes the delete to facility_id
└── rawQuery() → throws TenantScopeException (raw queries not allowed)
```

**Secondary defence:** Every tenant-scoped Eloquent model uses a `TenantScope` global scope that automatically applies `WHERE facility_id = ?` to all queries. This catches any code path that bypasses the repository.

**Exceptions:** The `global_patients` table and `patient_identifiers` table are platform-level and carry no `facility_id`. Access to these tables uses `GlobalPatientRepository`, which is not tenant-scoped.

### 2.5 Data Layer

| Component | Technology | Purpose |
|---|---|---|
| Primary database | MySQL 8.x InnoDB (strict mode, utf8mb4) | All transactional data |
| High availability | InnoDB Cluster | Database replication and failover |
| Cache | Redis 7 | Session cache, permission cache, query cache |
| Queue | Redis 7 + Laravel Horizon | Background jobs: DHIS2 push, SMS dispatch, report generation, sync |
| Object storage | AWS S3 | Clinical documents, medical images, DICOM files, generated reports |
| Offline (Android) | Room database | Local queue for offline clinical workflows |
| Offline (iOS) | Core Data / SwiftData | Local queue for offline clinical workflows |
| Offline (Web) | IndexedDB | Auto-save and offline transaction queue |

---

## 3. Multi-Tenancy Architecture

### 3.1 Isolation Strategy

Medic8 uses **row-level tenant isolation**. Every tenant-scoped table includes a `facility_id` column (integer, not null, indexed). Isolation is enforced at 4 layers:

| Layer | Mechanism | Failure Mode |
|---|---|---|
| Repository | `TenantAwareRepository` base class appends `WHERE facility_id = ?` to every query | Compile-time: repository methods are final; subclasses cannot omit the scope |
| Model | Eloquent `TenantScope` global scope applies `WHERE facility_id = ?` | Runtime: catches any query that bypasses the repository |
| CI pipeline | Static analysis rule rejects raw SQL queries that do not include `facility_id` in the WHERE clause | Build-time: pull request blocked if raw query lacks tenant scope |
| API response | `StripTenantId` middleware removes `facility_id` from all outbound JSON responses | Response-time: prevents leaking internal tenant identifiers to clients |

### 3.2 Tenant Context Binding

On every authenticated request, the `AuthenticateTenant` middleware:

1. Extracts `facility_id` from the session (web) or JWT claims (mobile/API)
2. Binds it to the Laravel service container: `app()->instance('facility_id', $facilityId)`
3. Binds it to the request attributes: `$request->attributes->set('facility_id', $facilityId)`
4. All downstream repositories, global scopes, and event listeners resolve `facility_id` from the container

### 3.3 Queue Job Isolation

Every queued job serialises `facility_id` as a job property. When the job executes, the `TenantAwareJob` base class re-binds `facility_id` to the container before any repository call:

```
class TenantAwareJob implements ShouldQueue
{
    public int $facilityId;

    public function __construct(int $facilityId)
    {
        $this->facilityId = $facilityId;
    }

    public function handle(): void
    {
        app()->instance('facility_id', $this->facilityId);
        // subclass logic runs with correct tenant context
    }
}
```

### 3.4 Super Admin Cross-Tenant Access

Super Admin accounts carry `facility_id = null` in their session/JWT. When a Super Admin needs to query a specific tenant, they call `withoutTenantScope($facilityId)` on the repository, which:

1. Temporarily binds the specified `facility_id`
2. Executes the query
3. Restores the previous context
4. Logs the cross-tenant access to the audit trail with `action = 'cross_tenant_read'`

---

## 4. openEHR Two-Level Modelling

Medic8 separates **what the database stores** (Reference Model) from **what the clinical form looks like** (Archetypes and Templates). This separation enables one codebase to serve multiple countries without schema changes.

### 4.1 Reference Model (Stable Schema)

The Reference Model is the database layer. It stores clinical data in a generic, stable structure that never changes per country. Tables include:

- `ehr_compositions` — a clinical document (consultation, discharge summary, ANC visit)
- `ehr_entries` — individual data entries within a composition (a single observation, a single order)
- `ehr_elements` — atomic data values (a blood pressure reading, a diagnosis code, a drug name)

Each element records its `archetype_node_id` (which archetype field it belongs to) and its `value` (stored as a typed JSON column supporting quantity, coded_text, date_time, ordinal, and other openEHR data types).

### 4.2 Archetypes (Clinical Form Definitions)

Archetypes define the structure and constraints of a clinical concept. They are stored as JSON documents in the `archetypes` table and are configurable per country or per facility.

Example archetypes:

- `openEHR-EHR-OBSERVATION.blood_pressure.v2` — defines systolic, diastolic, position, cuff size
- `openEHR-EHR-INSTRUCTION.medication_order.v3` — defines drug name, dose, route, frequency, duration
- `openEHR-EHR-EVALUATION.problem_diagnosis.v1` — defines diagnosis name, ICD code, severity, date of onset

### 4.3 Templates (Composed Forms)

Templates compose multiple archetypes into a complete clinical form. A template for "Uganda OPD Consultation" might include:

1. `OBSERVATION.blood_pressure`
2. `OBSERVATION.body_weight`
3. `OBSERVATION.body_temperature`
4. `OBSERVATION.pulse`
5. `OBSERVATION.pulse_oximetry`
6. `EVALUATION.problem_diagnosis` (repeating)
7. `INSTRUCTION.medication_order` (repeating)
8. `INSTRUCTION.service_request` (lab/radiology orders)

Templates drive UI generation: the frontend reads the template definition and renders the appropriate form fields with validation rules derived from archetype constraints.

### 4.4 Country Configuration Layer

Each tenant is assigned a country profile that controls:

| Configuration Area | Examples |
|---|---|
| Regulatory framework | PDPA 2019 (Uganda), HIPAA (USA), Privacy Act 1988 (Australia), DISHA (India) |
| National ID systems | NIN (Uganda), Aadhaar (India), Medicare Number (Australia), Huduma Namba (Kenya) |
| Financial localisation | Currency (UGX, KES, INR, AUD), tax tables, insurance models |
| HMIS form definitions | HMIS 105/108 (Uganda), MOH 105 (Kenya), HMIS (India) |
| Immunisation schedules | EPI Uganda, UIP India, NIP Australia |
| Drug formularies | NDA Uganda, PPB Kenya, CDSCO India, TGA Australia |
| Consent model | Minimal digital (Uganda), opt-in (India ABDM), opt-out (Australia My Health Record) |
| Clinical templates | Country-specific OPD, ANC, IPD templates composed from shared archetypes |
| Vital sign ranges | Population-adjusted thresholds for NEWS2, paediatric vitals |

Country profiles are stored in the `country_configurations` table and applied at login. The profile ID is cached in the user session alongside `facility_id`.

---

## 5. Event-Driven Architecture (EHR as Data Bus)

Clinical encounters produce downstream effects across multiple modules. Rather than coupling modules with direct service calls, Medic8 dispatches domain events through Laravel's event system. Each module subscribes to the events it needs.

### 5.1 Core Domain Events

| Event | Dispatched When | Payload |
|---|---|---|
| `PatientRegistered` | New patient created | `patient_id`, `facility_id`, `registration_type` |
| `EncounterCreated` | OPD visit, IPD admission, or emergency visit started | `encounter_id`, `patient_id`, `facility_id`, `encounter_type` |
| `DiagnosisRecorded` | ICD-10 diagnosis saved | `encounter_id`, `patient_id`, `icd_code`, `facility_id` |
| `PrescriptionWritten` | Doctor submits a prescription | `prescription_id`, `encounter_id`, `patient_id`, `drugs[]`, `facility_id` |
| `DrugDispensed` | Pharmacist dispenses a medication | `dispense_id`, `prescription_id`, `patient_id`, `drug_id`, `quantity`, `facility_id` |
| `LabResultEntered` | Lab technician submits a result | `result_id`, `request_id`, `patient_id`, `test_code`, `value`, `is_critical`, `facility_id` |
| `VitalsRecorded` | Nurse enters vital signs | `vitals_id`, `encounter_id`, `patient_id`, `news2_score`, `facility_id` |
| `PatientAdmitted` | Patient admitted to IPD | `admission_id`, `encounter_id`, `patient_id`, `ward_id`, `bed_id`, `facility_id` |
| `PatientDischarged` | Patient discharged from IPD | `discharge_id`, `admission_id`, `patient_id`, `facility_id` |
| `CriticalValueDetected` | Lab result exceeds panic threshold | `result_id`, `patient_id`, `requesting_doctor_id`, `test_code`, `value`, `facility_id` |
| `ImmunisationGiven` | Vaccine administered | `immunisation_id`, `patient_id`, `vaccine_code`, `dose_number`, `facility_id` |
| `DeathRecorded` | Patient death documented | `patient_id`, `cause_of_death_icd`, `facility_id` |

### 5.2 Event Listener Mappings

| Event | Listener | Action |
|---|---|---|
| `EncounterCreated` | `BillingAutoChargeListener` | Posts consultation fee to patient account from facility price list |
| `EncounterCreated` | `HmisCounterListener` | Increments OPD visit tally for HMIS 105 Section 1 by age group and sex |
| `DiagnosisRecorded` | `HmisCounterListener` | Tallies diagnosis to HMIS 105 by ICD-10 code, age group, sex |
| `DiagnosisRecorded` | `DiseaseRegistryListener` | Enrols patient in disease registry (HIV, TB, NCD) if diagnosis matches registry criteria |
| `DiagnosisRecorded` | `SurveillanceListener` | Checks against IDSR priority disease list; flags for HMIS 033b if matched |
| `PrescriptionWritten` | `CdsAlertListener` | Triggers drug interaction check, Five Rights validation, weight-based dosing check |
| `DrugDispensed` | `BillingAutoChargeListener` | Posts drug charge to patient account |
| `DrugDispensed` | `InventoryDeductionListener` | Deducts dispensed quantity from pharmacy stock |
| `DrugDispensed` | `NarcoticRegisterListener` | Logs controlled substance dispensing to narcotic register (BR-RX-001) |
| `LabResultEntered` | `BillingAutoChargeListener` | Posts lab test charge to patient account |
| `LabResultEntered` | `HmisCounterListener` | Tallies lab test to HMIS 105 Section 2 |
| `CriticalValueDetected` | `CriticalValueEscalationListener` | Sends WebSocket/push/SMS notification to requesting doctor; starts 30-minute escalation timer (BR-CLIN-003) |
| `VitalsRecorded` | `News2ScoreListener` | Calculates NEWS2 score; triggers clinical alert if score >= 5 |
| `PatientAdmitted` | `BillingAutoChargeListener` | Posts admission deposit charge; starts bed-day charge accumulation |
| `PatientAdmitted` | `BedManagementListener` | Marks bed as occupied; updates ward census |
| `PatientDischarged` | `HmisCounterListener` | Tallies discharge to HMIS 108 by diagnosis, age group, sex |
| `PatientDischarged` | `InsuranceClaimListener` | Auto-generates insurance claim if patient has active insurance scheme (BR-INS-002) |
| `PatientDischarged` | `BedManagementListener` | Marks bed as available; updates ward census |
| `ImmunisationGiven` | `HmisCounterListener` | Tallies immunisation to HMIS 105 Section 6 |
| `DeathRecorded` | `HmisCounterListener` | Tallies death to HMIS 108 |
| `DeathRecorded` | `MortuaryListener` | Creates mortuary intake record |

### 5.3 Event Infrastructure

- **Synchronous listeners:** CDS alerts, Five Rights validation (must block the workflow if a fatal interaction is detected)
- **Asynchronous listeners (queued):** HMIS tallying, billing auto-charge, SMS dispatch, DHIS2 push (processed via Redis + Laravel Horizon)
- **Real-time delivery:** WebSocket (Laravel Echo + Pusher/Soketi) for critical lab values and emergency notifications
- **Retry policy:** Failed queued jobs retry 3 times with exponential backoff (10s, 60s, 300s), then move to the failed jobs table for manual review

---

## 6. Offline-First Architecture

### 6.1 Scope

Core clinical workflows must function at full capacity with 0% internet connectivity (NFR-HC-006, NFR-HC-013). The following modules operate offline:

1. Patient registration
2. OPD consultation (triage, SOAP notes, diagnosis, prescriptions)
3. Prescribing
4. Dispensing
5. Lab result entry

### 6.2 Offline Storage

| Platform | Technology | Capacity |
|---|---|---|
| Web | IndexedDB via Dexie.js wrapper | Browser storage limits (typically 50 MB-1 GB) |
| Android | Room database (SQLite) | Device storage |
| iOS | Core Data / SwiftData (SQLite) | Device storage |

### 6.3 Sync Protocol

1. Every data mutation (create, update) is written to a local `sync_queue` table with fields: `id`, `entity_type`, `entity_id`, `action`, `payload` (JSON), `facility_id`, `user_id`, `timestamp`, `status` (pending/synced/conflict)
2. A background sync worker checks connectivity every 30 seconds
3. When connectivity is detected, the worker sends queued items to the server in chronological order via `POST /api/v1/sync/batch`
4. The server processes each item, applies tenant scoping, and returns a result per item (success/conflict/error)
5. On power restoration (generator-aware), the system triggers an immediate sync attempt (BR-DATA-005)

### 6.4 Conflict Resolution (BR-DATA-003)

When the same record is modified offline at two workstations:

- **Non-clinical fields** (address, phone, next of kin): last-write-wins based on timestamp
- **Clinical fields** (diagnoses, prescriptions, allergies): both versions are preserved in a `conflict_log` table and flagged for clinician review. The system displays both versions side-by-side until a clinician selects the authoritative version

No clinical data is silently overwritten.

### 6.5 Offline Queue Limits

- Maximum offline queue duration: **72 hours** (NFR-HC-013)
- If the queue approaches 72 hours without sync, the system displays a warning to the user at 48 hours and 64 hours
- After 72 hours, the system continues to accept new entries but marks them as "over-limit" for priority review on sync

### 6.6 Auto-Save (NFR-HC-016)

Every form interaction (keystroke, dropdown selection, checkbox toggle, date picker change) triggers an auto-save to local storage. On power loss, browser crash, or app crash, the last auto-saved state is restored when the user reopens the form. The restoration prompt displays the auto-save timestamp and allows the user to accept or discard the recovered state.

---

## 7. Global Patient Identity Layer

### 7.1 Data Model

Patient identity is managed at the **platform level**, not the tenant level. This enables cross-facility patient lookup while maintaining clinical data isolation.

```
global_patients (no facility_id)
├── id (PK)
├── uuid
├── first_name
├── last_name
├── date_of_birth
├── sex
├── blood_group
├── photo_url
├── created_at
├── updated_at

patient_identifiers (no facility_id)
├── id (PK)
├── global_patient_id (FK → global_patients.id)
├── identifier_type (enum: NIN, MRN, PASSPORT, UNHCR, NHIS, PHONE, EMAIL)
├── identifier_value
├── issuing_facility_id (nullable — which facility issued this MRN)
├── verified (boolean)
├── created_at

facility_encounters (tenant-scoped, has facility_id)
├── id (PK)
├── global_patient_id (FK → global_patients.id)
├── facility_id (FK → facilities.id)
├── encounter_type (enum: OPD, IPD, EMERGENCY, ANC, IMMUNISATION)
├── encounter_date
├── ... (all clinical data lives in tenant-scoped tables)
```

### 7.2 EMPI Probabilistic Matching (BR-PID-001)

At patient registration, the EMPI service searches for existing records using weighted probabilistic matching:

| Field | Weight | Algorithm |
|---|---|---|
| National ID (NIN) | 0.95 | Exact match |
| Phone number | 0.80 | Exact match (normalised to E.164) |
| Date of birth | 0.70 | Exact match |
| Full name | 0.60 | Soundex + Metaphone (adapted for African naming patterns: compound surnames, clan names, spelling variations) |
| Sex | 0.30 | Exact match |

A composite score above **0.80** triggers a mandatory duplicate warning that cannot be dismissed without action (BR-PID-002). The registrar must explicitly confirm "New Patient" or select the existing record.

### 7.3 Cross-Facility Privacy Rules

- **Identity lookup:** Facility B can confirm that a patient exists in the system and see identity data (name, age, sex, identifiers) — but cannot read clinical notes, diagnoses, or prescriptions from Facility A (BR-DATA-001)
- **Emergency access:** Requires two-factor patient confirmation (name + DOB). Reveals: allergies, current medications, blood group, HIV status (only if prior consent), last 3 diagnoses. Expires after 24 hours. Patient notified via SMS. Full audit trail recorded (BR-DATA-002)
- **Consent-based sharing:** Patient grants explicit consent for Facility B to view specific clinical data from Facility A, managed by the Consent Engine

### 7.4 Patient Merge (BR-PID-003)

- Only Records Officer or Facility Admin may merge
- Merge consolidates all clinical history, billing, and encounters under the surviving record
- Reversible (unmerge) within 30 days
- Full audit trail: performing user, source records, surviving record, timestamp

---

## 8. Interoperability Architecture

### 8.1 FHIR R4 API (NFR-HC-014)

Medic8 exposes 14 FHIR R4 resource types:

| FHIR Resource | Medic8 Source | Operations |
|---|---|---|
| Patient | `global_patients` + `patient_identifiers` | Read, Search, Create |
| Encounter | `facility_encounters` | Read, Search |
| Observation | `ehr_elements` (vitals, lab results) | Read, Search, Create |
| Condition | `ehr_elements` (diagnoses) | Read, Search |
| MedicationRequest | `prescriptions` | Read, Search |
| MedicationDispense | `dispensing_records` | Read, Search |
| DiagnosticReport | `lab_results` + `radiology_reports` | Read, Search |
| ServiceRequest | `lab_requests` + `radiology_requests` | Read, Search, Create |
| Immunization | `immunisation_records` | Read, Search |
| AllergyIntolerance | `patient_allergies` | Read, Search, Create |
| Procedure | `procedures` | Read, Search |
| Location | `facilities` + `wards` + `rooms` | Read, Search |
| Practitioner | `users` (clinical roles) | Read, Search |
| Organization | `facilities` | Read, Search |

**FHIR Narrative:** Every FHIR response includes a human-readable HTML narrative in the `text.div` field, ensuring clinical safety when receiving systems cannot fully process structured data.

**SMART on FHIR:** Third-party apps authenticate via OAuth 2.0, receive scoped access tokens, and interact with FHIR resources within their granted scope.

### 8.2 HL7 v2 Gateway

- **Protocol:** MLLP (Minimum Lower Layer Protocol) over TCP
- **Message types:** ORM (order messages from Medic8 to analyser), ORU (result messages from analyser to Medic8)
- **Supported analysers:** Cobas, Mindray, Sysmex, GeneXpert
- **Legacy support:** ASTM E1394 for older analysers that do not support HL7 v2
- **Flow:** Lab request dispatched → HL7 ORM sent to analyser → analyser processes sample → HL7 ORU returned → `LabResultEntered` event dispatched

### 8.3 DHIS2 Integration (BR-HMIS-004)

| Integration Type | Method | Use Case |
|---|---|---|
| Aggregate data push | DHIS2 API (`/api/dataValueSets`) | HMIS 105, HMIS 108, HMIS 033b monthly/weekly submissions |
| Tracker individual-level push | DHIS2 Tracker API | PEPFAR MER indicators (TX_CURR, TX_NEW, TX_PVLS, HTS_TST, VMMC), individual immunisation tracking |
| Export fallback | CSV/Excel download | Manual upload when API connectivity is unavailable |

### 8.4 CDA R2 (Clinical Document Architecture)

- **Discharge summaries:** Generated as CDA R2 XML documents on patient discharge, containing diagnoses (ICD-10), procedures, medications, and follow-up plan
- **Referral letters:** Generated as CDA R2 XML for electronic referrals between facilities
- Both formats are machine-readable and include a human-readable HTML section

### 8.5 DICOM Gateway

- DICOM Worklist (MWL) pushes radiology orders from Medic8 to the modality
- DICOM Storage (C-STORE) receives completed images from the modality and stores them in the PACS/S3
- DICOM Query/Retrieve (C-FIND, C-MOVE) enables image retrieval from the PACS for viewing in the web UI

---

## 9. Module Dependency Map

The following table shows inter-module dependencies. A module in the "Depends On" column must be active for the module in the first column to function. A module in the "Depended On By" column consumes data or events from the first-column module.

| Module | Depends On | Depended On By |
|---|---|---|
| Patient Registration & EMPI | — (foundational) | All clinical modules, Billing, Insurance, HMIS, Patient Portal |
| OPD | Patient Registration, Terminology Service, CDS Engine | Laboratory, Radiology, Pharmacy, Billing, HMIS, IPD, Referral |
| IPD & Ward Management | Patient Registration, OPD (for admission source), Terminology Service | Laboratory, Radiology, Pharmacy, Billing, HMIS, Mortuary |
| Emergency (A&E) | Patient Registration | OPD, IPD, Laboratory, Radiology, Pharmacy, Billing |
| Laboratory (LIS) | Patient Registration, OPD/IPD (for lab requests) | OPD, IPD, Billing, HMIS, FHIR API |
| Radiology & Imaging | Patient Registration, OPD/IPD (for radiology requests), DICOM Gateway | OPD, IPD, Billing, HMIS |
| Pharmacy & Dispensary | Patient Registration, OPD/IPD (for prescriptions), Inventory | Billing, HMIS, Narcotic Register |
| Maternity & ANC | Patient Registration, OPD | Immunisation, Laboratory, HMIS, PMTCT |
| Immunisation | Patient Registration | HMIS, Patient Portal |
| Billing & Revenue | Patient Registration, all clinical modules (via events) | Insurance, Accounting, Patient Portal |
| Insurance Management | Billing, Patient Registration | Accounting |
| Financial Accounting | Billing, Insurance, Inventory, HR/Payroll | Director Platform |
| Inventory & Stores | — (foundational for stock) | Pharmacy, Theatre, Ward supplies |
| HR & Payroll | — (foundational for staff) | Accounting, Duty Roster |
| HMIS Reporting | OPD, IPD, Laboratory, Pharmacy, Maternity, Immunisation | DHIS2 Integration |
| Disease Surveillance | OPD (diagnoses) | HMIS (033b), Public Health authorities |
| Appointments & Scheduling | Patient Registration | OPD, Patient Portal |
| Referral Management | OPD, IPD | External facilities (via CDA R2) |
| Patient Portal | Patient Registration, Billing, Laboratory, Appointments | — (consumer endpoint) |
| CHW App | Patient Registration | Referral, HMIS, DHIS2 Tracker |
| Terminology Service | — (foundational) | OPD, IPD, Laboratory, Pharmacy, HMIS, FHIR API |
| CDS Engine | Terminology Service, Pharmacy (formulary) | OPD, IPD, Pharmacy |
| Consent Engine | Patient Registration | FHIR API, Cross-facility access, Data export |
| FHIR R4 API | All clinical modules | Third-party apps (via SMART on FHIR) |
| HL7 v2 Gateway | Laboratory | Laboratory analysers |
| DICOM Gateway | Radiology | PACS, Modalities |
| Director Platform | Accounting, Billing, HMIS | — (consumer endpoint) |

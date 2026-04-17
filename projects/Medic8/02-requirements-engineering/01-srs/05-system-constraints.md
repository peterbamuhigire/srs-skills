# 5 System Constraints

This section defines the legal, regulatory, technology, performance, and design constraints that bound the Medic8 system architecture. All constraints are binding unless explicitly marked as advisory.

**Standards:** IEEE 830-1998 Section 3.4, IEEE 29148-2018 Section 6.5.

---

## 5.1 Legal and Regulatory Constraints

### 5.1.1 Uganda Data Protection and Privacy Act 2019 (PDPA)

The system shall comply with the Uganda Data Protection and Privacy Act 2019 in all aspects of patient data handling.

- **Consent:** The system shall obtain and record patient consent before collecting, processing, or sharing personal health data (PDPA Section 6). The consent record shall include the data categories consented to, the date, and the method of consent.
- **Data Retention:** The system shall retain patient health records for a minimum of 10 years from the date of the last clinical encounter, in accordance with Uganda Ministry of Health (MoH) policy.
- **Breach Notification:** The system shall support identification and reporting of all affected patient records within 72 hours of a confirmed data breach (PDPA Section 31). The system shall generate a breach impact report listing affected records, data categories exposed, and breach timeline.
- **Cross-Border Transfer:** The system shall not transfer patient health data outside Uganda unless the destination country provides adequate data protection as determined by the Personal Data Protection Office (PDPO), or the patient has given explicit consent for the transfer. The system shall enforce this restriction at the FHIR API and DHIS2 export layers.
- **Right of Access:** The system shall enable patients to request and receive a copy of their health records in a readable format within 30 days of the request.

### 5.1.2 Uganda HMIS Compliance

The system shall auto-populate the following Uganda MoH Health Management Information System forms from clinical data without manual re-entry:

- **HMIS 105** — Outpatient Monthly Report (8 sections: diagnoses by age/sex, laboratory, radiology, maternity, HIV/AIDS, immunisation, dental, eye services)
- **HMIS 108** — Inpatient Monthly Report (admissions, discharges, deaths by diagnosis/age/sex, bed occupancy, surgical operations)
- **HMIS 033b** — Weekly Epidemiological Surveillance Report (27 priority diseases from IDSR disease codes)

The system shall support DHIS2 API submission to the Uganda eHMIS instance (`hmis2.health.go.ug`). HMIS form mappings shall be version-controlled in configuration tables and updated within 30 days of MoH publication of a new form version (gap HIGH-007).

### 5.1.3 Uganda National Drug Authority (NDA)

- The system shall enforce compliance with the NDA drug formulary for all prescribing and dispensing operations.
- The system shall maintain a narcotic register for all Schedule I-V controlled substance dispensing events. Each entry shall record: patient name, drug name and strength, quantity dispensed, prescribing doctor, dispensing pharmacist, witness, and running balance.
- Any discrepancy between the physical stock count and the system balance for controlled substances shall trigger an immediate alert to the Facility Admin.

### 5.1.4 Uganda Medical and Dental Practitioners Council (UMDPC)

The system supports prescribing, dispensing, and clinical decision support functions. Whether Medic8 requires registration with UMDPC or NDA as a medical device or regulated software is under investigation (gap HIGH-003). The system shall not be commercially deployed to licensed health facilities until this regulatory determination is resolved.

### 5.1.5 HIV/AIDS Prevention and Control Act 2014

The system shall require explicit, documented patient consent before disclosing HIV status to any user. HIV status fields shall be protected by attribute-based access control (ABAC) and shall display "[Restricted]" to users without explicit "sensitive record" permission and an active treatment relationship with the patient.

### 5.1.6 Expansion Market Regulations

The system shall support a configurable compliance engine that enforces the data protection and health-sector regulations of each target market. The following regulatory profiles constitute the global superset:

| Country | Data Protection Law | Health Sector Standards | Drug Regulatory Body |
|---|---|---|---|
| Uganda | Data Protection and Privacy Act 2019 (PDPA) | MoH HMIS 105/108/033b, DHIS2 | National Drug Authority (NDA) |
| Kenya | Data Protection Act 2019 | Kenya Health Information System (KHIS) | Pharmacy and Poisons Board (PPB) |
| Tanzania | Electronic and Postal Communications Act (EPOCA) | TMDA health data regulations | Tanzania Medicines and Medical Devices Authority (TMDA) |
| Rwanda | Law No. 058/2021 on Protection of Personal Data and Privacy | Rwanda Biomedical Centre (RBC) standards | Rwanda FDA |
| Nigeria | Nigeria Data Protection Act 2023 (NDPA) | FMOH National Health ICT Strategic Framework | NAFDAC |
| India | Digital Information Security in Healthcare Act (DISHA, draft) | Ayushman Bharat Digital Mission (ABDM), ABHA health ID | Central Drugs Standard Control Organisation (CDSCO) |
| Australia | Privacy Act 1988 (Australian Privacy Principles), My Health Records Act 2012 | Therapeutic Goods Act 1989 | Therapeutic Goods Administration (TGA) |
| USA (PEPFAR) | HIPAA Privacy Rule and Security Rule | PEPFAR MER indicator compliance | FDA |

Each deployment shall activate the applicable regulatory profile at tenant configuration time. The system shall not permit clinical operation without an assigned regulatory profile.

---

## 5.2 Technology Constraints

### 5.2.1 Backend Platform

- The system shall be built on PHP 8.2+ with strict typing enabled and PSR-4 autoloading. The backend codebase is shared with Academia Pro via common architectural patterns.
- The system shall use MySQL 8.x with InnoDB engine, strict mode enabled, and `utf8mb4` character set.
- The system shall implement row-level multi-tenancy via a `facility_id` column on every tenant-scoped table, enforced at the Repository layer before every query. The architecture is centralised (single database), not federated.
- The system shall use Redis 7 for caching and job queue management (Laravel Horizon).

### 5.2.2 Offline-First Architecture

- Core clinical modules (patient registration, OPD consultation, prescribing, dispensing, lab result entry) shall function at full capacity with 0% internet connectivity.
- The Android mobile app shall use Room database for offline-first local storage.
- The iOS mobile app shall use SwiftData for offline-first local storage.
- The system shall queue all offline transactions locally and synchronise automatically when connectivity resumes, with a maximum offline queue duration of 72 hours without data loss.

### 5.2.3 Mobile Application Constraints

- **Android:** The app shall support Android 7.0+ (API level 24) on devices with 1 GB RAM minimum. The app shall be built in Kotlin with Jetpack Compose UI and MVVM architecture.
- **iOS:** The app shall support iOS 15.0+. The app shall be built in Swift with SwiftUI and MVVM architecture.
- The base installation shall consume no more than 50 MB of device storage.

### 5.2.4 Bandwidth Constraints

| Mode | Minimum Bandwidth | Capability |
|---|---|---|
| Full sync | 1 Mbps | All data synchronisation |
| Real-time clinical use | 256 Kbps | Live clinical workflows |
| Data-lite mode | 64 Kbps (2G/EDGE) | Basic operations |
| View-only mode | SMS-capable connection | Read-only access |

### 5.2.5 Healthcare Interoperability Standards

- **HL7 FHIR R4:** The system shall expose 14 FHIR R4 resource types via a RESTful API: Patient, Encounter, Observation, Condition, MedicationRequest, MedicationDispense, DiagnosticReport, ServiceRequest, Immunization, AllergyIntolerance, Procedure, Location, Practitioner, Organization. Every FHIR response shall include a human-readable HTML narrative element.
- **SMART on FHIR:** The system shall support SMART on FHIR for third-party app integration.
- **HL7 v2:** The system shall support HL7 v2 messaging (ORM/ORU) for laboratory analyser interfaces.
- **ASTM E1394:** The system shall support ASTM E1394 protocol for interfacing with older laboratory analysers.
- **CDA R2:** The system shall generate CDA R2 clinical documents for discharge summaries and referral letters.
- **DICOM:** The system shall support DICOM for radiology image management via a DICOM gateway.
- **DHIS2:** The system shall support DHIS2 API integration for HMIS aggregate reporting (ADX/JSON export).

---

## 5.3 Performance Constraints

### 5.3.1 API Response Time

The system shall maintain an API response time at or below 500 ms at the 95th percentile under normal load, defined as up to 50 concurrent users per facility.

### 5.3.2 Page Load Time

The system shall load any clinical page within 2 seconds on a 1 Mbps connection, including all required assets.

### 5.3.3 Cloud Availability

The system shall maintain 99.9% uptime for all clinical-facing modules, measured monthly. Maximum permissible downtime is 8.76 hours per year.

$$Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$$

Generator-aware sync: the system shall detect power restoration and immediately initiate synchronisation of the offline queue.

### 5.3.4 Offline Sync Queue

The system shall support a maximum of 72 hours of queued offline transactions without data loss. All queued transactions shall synchronise automatically when connectivity resumes, completing within 5 minutes for a standard day's workload (up to 200 patient encounters).

### 5.3.5 Database Query Performance

The system shall execute clinical data retrieval queries at or below 200 ms at the 95th percentile. This applies to patient record lookups, encounter histories, medication lists, and lab result queries.

### 5.3.6 Mobile App Launch Time

The Android app shall launch and display the home screen within 3 seconds (cold start) on a device meeting the minimum specification (Android 7.0, 1 GB RAM).

---

## 5.4 Design Constraints

### 5.4.1 openEHR Two-Level Modelling

The system shall implement openEHR two-level modelling:

- **Level 1 (Reference Model):** A stable database schema that does not change per country or facility.
- **Level 2 (Archetypes and Templates):** Configurable clinical archetypes and templates loaded per tenant configuration for country-specific forms, validation rules, and clinical workflows.

This architecture enables a single codebase to serve multiple countries without codebase forking.

### 5.4.2 Country Configuration Layer

The system shall support a country configuration layer that adapts regulatory, clinical, and financial behaviour per tenant. Configurable layers include:

- Regulatory frameworks (consent model, data retention, breach notification timeline)
- National ID systems (NIN Uganda, Aadhaar India, Medicare Number Australia, Huduma Namba Kenya)
- Financial localisation (currency, tax tables, insurance models, mobile money providers)
- HMIS form definitions (Uganda 105/108, Kenya MOH 105, India HMIS)
- Immunisation schedules (EPI Uganda, UIP India, NIP Australia)
- Drug formularies (NDA Uganda, PPB Kenya, CDSCO India, TGA Australia)

### 5.4.3 Access Control Model

The system shall implement ABAC layered on RBAC:

- **RBAC** grants base access permissions per role (19 built-in roles: clinician, pharmacist, lab technician, records officer, administrator, AI Administrator, and others as defined in the stakeholder registry).
- **ABAC** enforces fine-grained attribute-based policies for sensitive data categories (HIV status, mental health, substance abuse, reproductive health).

### 5.4.4 Configurable Consent Engine

The system shall implement a configurable consent engine supporting 4 consent models:

1. General consent (patient consents to all data use)
2. General consent with specific denials (patient consents broadly but denies specific categories)
3. General denial with specific consents (patient denies broadly but consents to specific categories)
4. General denial (patient denies all non-essential data use)

The active consent model shall be configurable at the tenant level to match jurisdictional requirements (India ABDM: opt-in; Australia My Health Record: opt-out; Uganda: general consent with specific denials for HIV/mental health).

### 5.4.5 Terminology Service

The system shall implement a single Terminology Service gateway providing access to:

- **ICD-10 / ICD-11** — diagnosis coding (mandatory for all facilities)
- **SNOMED CT** — internal clinical concept storage
- **LOINC** — laboratory observations and results
- **RxNorm / ATC** — medication coding, mapped per country
- **CPT/HCPCS** — procedure coding (only for markets requiring it)

Clinical data shall be stored internally using SNOMED CT concept identifiers and mapped to ICD-10 at the reporting and billing boundary.

### 5.4.6 FHIR HTML Narrative

Every FHIR R4 response generated by the system shall include a human-readable HTML narrative `<div>` element within the `text` field. This ensures clinical safety when receiving systems cannot fully process structured FHIR data.

### 5.4.7 Event-Driven Architecture

The system shall implement an event-driven architecture where the Electronic Health Record (EHR) functions as the central data bus. A clinical encounter shall trigger downstream effects (laboratory order, pharmacy dispense, charge capture, HMIS tally) automatically via published events. Modules shall subscribe to relevant events rather than polling or being called directly.

### 5.4.8 Enterprise Master Patient Index (EMPI)

The system shall maintain a global patient identity at the platform level, independent of facility tenancy. The `global_patients` table shall carry no `facility_id` column. The EMPI shall use probabilistic matching on name, date of birth, National Identification Number (NIN), and phone number, with Soundex and Metaphone algorithms adapted for African naming patterns (compound surnames, clan names, spelling variations).

### 5.4.9 Clinical Decision Support Constraint

The system shall implement clinical decision support (CDS) as data-driven configuration (database-stored rules), not hardcoded logic. All CDS rules, alert thresholds, and override behaviours shall be maintainable by the pharmacy lead or clinical administrator without code deployment. The system's Terms of Service shall explicitly state that Medic8 is decision support, not a decision maker — clinical liability remains with the prescribing clinician (gap HIGH-004).

---

## 5.5 AI Intelligence Module Constraints

### CONSTRAINT-AI-001: No Auto-Save of AI-Generated Clinical Content

The AI Intelligence module shall never auto-save AI-generated content (clinical notes, differential diagnoses, ICD code selections) to the patient record without explicit clinician approval. This constraint cannot be overridden by any role-level configuration. Every AI-generated draft presented to a clinician shall require an affirmative **Approve** action before the content is written to the patient record. Clicking **Discard** shall remove the draft without any write operation.

### CONSTRAINT-AI-002: Patient Data Minimisation for AI Prompts

Patient data sent to external AI provider APIs shall be minimised per the DPPA 2019 data minimisation principle. Prompts shall not include patient NIN, full legal name, or NIRA registration number. Anonymised encounter IDs shall be used in place of direct patient identifiers. This constraint is enforced at the `AIProviderInterface` layer before any prompt is dispatched to an external provider and applies to all 4 supported providers (OpenAI, Anthropic, DeepSeek, Google Gemini).

### CONSTRAINT-AI-003: Graceful Degradation on AI Provider Failure

When the primary AI provider API returns an error or fails to respond within 10 s, the system shall automatically attempt the request with the secondary configured provider. If the secondary provider also fails, the system shall degrade gracefully: AI capability UI elements are hidden and a non-blocking notification is displayed to the user. No clinical workflow shall be blocked by AI provider unavailability. Patient registration, OPD consultation, prescribing, dispensing, lab result entry, and all billing operations shall continue without interruption.

---

## 5.6 Internationalisation Constraints

### CONSTRAINT-I18N-001: Externalised User-Visible Strings

All user-visible strings in the web portal, Android application, and iOS application shall be externalised into locale-specific resource files:

- PHP (Laravel): `lang/<locale>/` (e.g., `lang/en/`, `lang/fr/`, `lang/sw/`)
- Android: `values-<locale>/strings.xml` (e.g., `values-fr/strings.xml`, `values-sw/strings.xml`)
- iOS: `<locale>.lproj/Localizable.strings` (e.g., `fr.lproj/Localizable.strings`, `sw.lproj/Localizable.strings`)

No user-visible string shall be hardcoded in application logic or templates.

### CONSTRAINT-I18N-002: Supported Locales and Fallback Chain

The supported locales at launch are `en` (English, primary), `fr` (French), and `sw` (Kiswahili). The locale fallback chain is `sw` → `en` and `fr` → `en`. A missing translation shall fall through to English and shall be flagged `[I18N-GAP: <key>]` in the build log. No production release shall contain any unresolved `[I18N-GAP]` tags.

### CONSTRAINT-I18N-003: Clinical Alert Severity Labels

Clinical alert severity labels (Fatal, Serious, Warning, Info) shall always render in the clinician's configured UI language. These labels shall not be auto-translated mid-workflow. The translations for these 4 labels in all 3 supported locales are mandatory strings; a build shall fail if any of these 12 strings is absent from any locale resource file.

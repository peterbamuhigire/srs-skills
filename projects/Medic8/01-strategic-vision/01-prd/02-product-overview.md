# Product Overview

## Product Vision

Medic8 does for hospitals what Academia Pro does for schools: it delivers an enterprise-grade, Africa-first healthcare information management system at a price the market can sustain, deployed as multi-tenant SaaS so no on-premise IT infrastructure is required.

### Design Covenant

> Automate every clinical and administrative process as much as possible, yet remain simple enough for a single receptionist to operate — provided each user has completed the onboarding for their assigned modules. Clinically safe and globally configurable.

The design covenant establishes 7 binding constraints that govern all product decisions:

1. **Maximum automation by default.** Prescription alerts, stock reorder triggers, insurance pre-authorisation checks, and HMIS report generation fire without manual intervention.
2. **Zero-configuration defaults.** A Ugandan private clinic reaches operational status within 60 minutes of signup.
3. **Role-scoped user experience.** A pharmacist never sees an HR screen; a lab technician never sees payroll. Complexity is hidden behind role boundaries, with 18 built-in roles spanning platform, facility management, clinical, diagnostic, administrative, financial, and external user categories.
4. **Onboarding-path architecture.** Each module ships with embedded guided onboarding. Users learn module-by-module, not system-wide.
5. **Progressive disclosure.** Advanced clinical, insurance, and reporting settings exist but do not clutter the daily workflow.
6. **Single-receptionist survivability.** If the IT officer leaves, the receptionist and clinic manager can continue operating the system without external support.
7. **Clinical safety as a non-negotiable default.** Drug interaction warnings (4-tier: Info, Warning, Serious, Fatal), allergy flags, and dosage alerts cannot be silently disabled.

### Africa-First, Globally Configurable

Uganda is the launch market, with an addressable base of over 6,000 registered health facilities. The planned expansion sequence is Kenya, Tanzania, Rwanda, DRC, and Nigeria, with future markets including India and Australia. The country configuration layer adapts 5 dimensions per tenant without forking the codebase:

- **Regulatory frameworks:** Data protection laws (PDPA Uganda, DPA Kenya, EPOCA Tanzania, NDPA Nigeria, DISHA India, Privacy Act 1988 Australia), health-sector licensing, and dispensing regulations
- **Clinical protocols:** Drug formularies (NDA Uganda, PPB Kenya, CDSCO India, TGA Australia), disease classification systems, and immunisation schedules (EPI Uganda, UIP India, NIP Australia)
- **Financial systems:** Currencies, tax tables, insurance models, and mobile money providers per country
- **HMIS form definitions:** Uganda 105/108, Kenya MOH 105, India HMIS
- **National identity systems:** NIN (Uganda), Huduma Namba (Kenya), Aadhaar (India), Medicare Number (Australia)

Each deployment must activate an applicable regulatory profile at tenant configuration time. The system shall not permit operation without an assigned regulatory profile.

## Product Architecture Summary

### Centralised Multi-Tenant Model

Medic8 uses a centralised multi-tenant architecture with row-level tenant isolation via a `facility_id` column on every tenant-scoped table, enforced at the Repository layer before every database query. This is not a federated model — all tenants share the same application instance and database cluster, with logical isolation rather than physical separation. This design reduces operational cost, simplifies upgrades, and enables cross-facility features such as the global patient identity layer and multi-facility analytics.

### openEHR Two-Level Modelling

Clinical data is structured using openEHR two-level modelling, which separates a stable Reference Model (the data persistence layer) from configurable clinical Archetypes (the clinical content definitions). This separation enables multi-country clinical configurability: a Ugandan facility and a Kenyan facility can use different clinical templates, formularies, and reporting structures without schema changes. Country-specific clinical content is loaded at tenant configuration time through the Archetype library.

### EHR as Data Bus

The Electronic Health Record serves as the central data bus in an event-driven architecture. Clinical events — patient registration, consultation, lab order, result entry, prescription, dispensing, admission, discharge — publish domain events that downstream modules consume. This decouples modules and enables real-time workflows: a lab result entry triggers a notification to the ordering clinician; a dispensing event triggers stock deduction and billing charge accumulation; a diagnosis entry triggers HMIS indicator tallying.

### FHIR R4 Native API

Medic8 exposes an HL7 FHIR R4 RESTful API as the primary interoperability layer, covering 14 clinical resources: Patient, Encounter, Observation, Condition, MedicationRequest, MedicationDispense, DiagnosticReport, ServiceRequest, Immunization, AllergyIntolerance, Procedure, Location, Practitioner, and Organization. Every FHIR response includes an HTML narrative fallback for systems that cannot parse structured FHIR resources. SMART on FHIR is supported for third-party application substitutability. The FHIR API enables integration with national health information exchanges, donor reporting platforms, and research data extraction tools.

### Offline-First Architecture

Core clinical workflows operate without internet connectivity: patient registration, vital signs capture, prescription writing, dispensing, and sample collection function on the local device and synchronise when connectivity resumes. The mobile applications use Room (Android) and Core Data/SwiftData (iOS) as local offline databases. The web application employs browser-based local storage for offline queue management. Conflict resolution during synchronisation follows a last-write-wins strategy with audit logging of all merge decisions.

### Global Patient Identity Layer

An Enterprise Master Patient Index (EMPI) provides a global patient identity across all facilities in the Medic8 network. The EMPI uses probabilistic matching to detect duplicate registrations across facilities, supporting lookup by name, phone number, National Identification Number (NIN), passport, NIRA, UNHCR Refugee ID, or insurance member number. Cross-facility lookup enables a patient who registers at Facility A to be recognised at Facility B without re-registration, provided both facilities are on the Medic8 platform. This architectural pattern is shared with Academia Pro's global student identity layer.

### Country Configuration Layer

The country configuration layer is a runtime-configurable subsystem that governs jurisdiction-specific behaviour across 5 domains: regulatory compliance, clinical protocols, financial localisation, HMIS form definitions, and national identity systems. Configuration is applied at tenant provisioning time and can be updated without code deployment. The layer enforces the regulatory superset documented in the domain context, including Uganda PDPA 2019, Kenya DPA 2019, Tanzania EPOCA, Rwanda Law No. 058/2021, India DISHA, Australia Privacy Act 1988, Nigeria NDPA 2023, and USA HIPAA (for PEPFAR-funded facilities).

### Terminology Service

A centralised Terminology Service provides a single gateway to 6 clinical code systems: ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm, and ATC. The service supports code lookup, value set expansion, concept mapping between systems, and hierarchical navigation. All clinical documentation — diagnoses, procedures, lab tests, medications — references terminology codes through this service, ensuring consistent coding across modules and enabling accurate HMIS and PEPFAR MER indicator computation.

### ABAC + RBAC Security Model

Access control combines Role-Based Access Control (RBAC) with Attribute-Based Access Control (ABAC). RBAC assigns users to 1 of 18 built-in roles (Super Admin, Facility Admin, Doctor, Nurse, Pharmacist, Lab Technician, Radiographer, Receptionist, Records Officer, Cashier, Insurance Clerk, Accountant, Store Keeper, Auditor, Clinical Officer, Facility Director, Patient, and Community Health Worker), each with defined module access permissions and restrictions. ABAC extends RBAC with contextual attributes: facility scope (users access only their assigned facility's data), shift context (nursing drug administration restricted to on-duty nurses), and emergency override (clinicians can access restricted data in emergencies with mandatory audit logging).

### Configurable Consent Engine

The consent engine manages patient consent for data access, sharing, and processing according to the regulatory profile of each jurisdiction. It supports 3 consent models — opt-in (explicit consent required before data use), opt-out (consent assumed unless withdrawn), and mixed (different consent rules for different data categories) — configurable per jurisdiction and per data type. All consent decisions are logged with timestamp, actor, and consent scope for audit purposes.

## Technology Stack Summary

### Backend

- **Language:** PHP 8.2+ with strict typing enabled, PSR-4 autoloading
- **Architecture:** Service/Repository pattern with multi-tenant row-level isolation
- **Database:** MySQL 8.x InnoDB (strict mode, utf8mb4 charset) with InnoDB Cluster for high availability
- **Cache and Queue:** Redis 7 with Laravel Horizon for job queue management
- **Authentication:** Dual authentication — Session-based for web UI, JWT with refresh token rotation for mobile and API clients; Laravel Sanctum for token management
- **API:** RESTful JSON API

### Frontend (Web)

- **Language:** JavaScript (vanilla + jQuery)
- **UI Framework:** Bootstrap 5 / Tabler UI (commercial template)
- **Data Operations:** AJAX for all data operations; DataTables.js for tabular data
- **UI Components:** SweetAlert2 for confirmations and alerts; Flatpickr for date/time inputs

### Mobile Applications

- **Android:** Kotlin with Jetpack Compose UI, MVVM architecture, Room database for offline-first storage, Dagger Hilt for dependency injection, Retrofit for API communication
- **iOS:** Swift with SwiftUI, MVVM architecture, Core Data/SwiftData for offline-first storage, async/await for concurrency

### Security

- CSRF protection for all web forms
- JWT refresh token rotation for mobile sessions
- TLS 1.2+ for all communications in transit
- AES-256-GCM encryption for data at rest
- 8-point security audit layer
- RBAC + ABAC access control model

### Healthcare-Specific Integrations

- **FHIR R4:** 14-resource RESTful API with SMART on FHIR for third-party app integration
- **HL7 v2:** ORM/ORU messaging for laboratory analyser interfaces (Cobas, Mindray, Sysmex)
- **ASTM E1394:** Legacy analyser protocol support for older laboratory equipment
- **CDA R2:** Clinical Document Architecture for discharge summaries and referral letters
- **DICOM:** Gateway for radiology image management and PACS integration
- **DHIS2:** API integration for HMIS aggregate reporting (ADX/JSON export)
- **openEHR:** Two-level clinical modelling with configurable Archetypes
- **Terminology:** ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm, ATC code systems via centralised Terminology Service
- **Real-Time:** WebSocket for critical lab value alerts and emergency notifications

### Infrastructure

- **Object Storage:** AWS S3 for clinical documents, medical images, and reports
- **SMS/USSD:** Africa's Talking for SMS notifications, USSD booking, and appointment reminders
- **Payments:** MTN Mobile Money API and Airtel Money API for patient payment collection

## Deployment Model

### Cloud SaaS (Primary)

The primary deployment model is cloud-hosted multi-tenant SaaS. All tenants share a common application instance and database cluster with logical isolation via `facility_id`. This model eliminates the need for on-premise servers, reduces TCO, and enables Chwezi Core Systems to manage upgrades, backups, and security patches centrally. The cloud infrastructure supports automated daily backups with a Recovery Point Objective (RPO) of 24 hours and a Recovery Time Objective (RTO) of 4 hours.

### Local Server Option

For facilities with no internet connectivity or regulatory requirements mandating on-premise data storage, Medic8 supports deployment on a local server within the facility. The local deployment runs the same codebase as the cloud version and synchronises with the central platform when connectivity is available. This model targets government facilities in remote areas and jurisdictions where data residency laws prohibit cloud-hosted patient data.

### Offline-First with Synchronisation

All deployment models incorporate offline-first capability. The mobile applications (Android and iOS) maintain a local database that mirrors the subset of clinical data relevant to the logged-in user. The web application uses browser-based queue management for offline data entry. When connectivity resumes, the synchronisation engine pushes queued transactions to the central database with conflict detection and resolution. Offline capability covers patient registration, vital signs entry, prescription writing, dispensing, and sample collection — the workflows most critical during connectivity outages.

### Regional Cloud Deployments for Data Sovereignty

Patient data must reside in-country unless the regulatory profile of the jurisdiction explicitly permits cross-border transfer. To meet this requirement, Medic8 supports regional cloud deployments:

- **East Africa region:** Hosted within East African data centres for Uganda, Kenya, Tanzania, and Rwanda tenants
- **West Africa region:** Hosted within West African data centres for Nigeria tenants
- **India region:** Hosted within Indian data centres for compliance with DISHA and Ayushman Bharat Digital Mission (ABDM) requirements
- **Australia region:** Hosted within Australian data centres for compliance with the Privacy Act 1988 and My Health Records Act 2012
- **USA (PEPFAR):** HIPAA-compliant hosting for US-government-funded health data at PEPFAR-supported facilities

Each regional deployment connects to the global Medic8 platform for cross-facility features (where consent and regulatory profiles permit) while keeping patient health information within the required jurisdiction. Tenant assignment to a regional deployment is configured at provisioning time and enforced at the infrastructure layer.

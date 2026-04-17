# Technology Stack — Medic8

## Backend (Web Application)

- **Language:** PHP 8.2+ (strict typing enabled)
- **Autoloading:** PSR-4
- **Architecture:** Multi-tenant SaaS with row-level tenant isolation (`facility_id` on every tenant-scoped table, enforced at the Repository layer before every query)
- **Design Pattern:** Service / Repository pattern
- **Database:** MySQL 8.x InnoDB (strict mode enabled; utf8mb4 charset)
- **High Availability:** InnoDB Cluster
- **Cache / Queue:** Redis 7 (queue driver: Redis; cache driver: Redis)
- **Job Queue:** Laravel Horizon
- **Authentication:** Session + JWT dual authentication (Session for web UI, JWT for mobile/API); Laravel Sanctum for token management
- **API:** RESTful JSON API

## Frontend (Web Portals)

- **Language:** JavaScript (vanilla + jQuery where needed)
- **UI Framework:** Bootstrap 5 / Tabler UI (commercial template)
- **Data Operations:** AJAX for all data operations
- **Tabular Data:** DataTables.js
- **Confirmations / Alerts:** SweetAlert2
- **Date/Time Inputs:** Flatpickr

## Mobile Applications (Android)

- **Language:** Kotlin
- **UI:** Jetpack Compose
- **Architecture:** MVVM
- **Offline:** Room database (offline-first local storage)
- **Dependency Injection:** Dagger Hilt
- **API Client:** Retrofit

## Mobile Applications (iOS)

- **Language:** Swift
- **UI:** SwiftUI
- **Architecture:** MVVM
- **Offline:** Core Data / SwiftData (offline-first local storage)
- **Concurrency:** async/await

## Security

- **Web Protection:** CSRF protection
- **Mobile Token Security:** JWT refresh token rotation
- **Transport Security:** TLS 1.2+ for all communications
- **Encryption at Rest:** AES-256-GCM
- **Security Audit:** 8-point security audit layer
- **Access Control:** RBAC + ABAC (Attribute-Based Access Control)

## Infrastructure

- **Cache / Queue:** Redis 7 + Laravel Horizon
- **Object Storage:** AWS S3 (clinical documents, medical images, reports)
- **SMS / USSD:** Africa's Talking
- **Payments:** MTN Mobile Money API, Airtel Money API

## Healthcare Interoperability

- **FHIR:** HL7 FHIR R4 API layer — 14 clinical resources (Patient, Encounter, Observation, Condition, MedicationRequest, MedicationDispense, DiagnosticReport, ServiceRequest, Immunization, AllergyIntolerance, Procedure, Location, Practitioner, Organization)
- **FHIR Narrative:** HTML narrative fallback in every FHIR response
- **Third-Party App Integration:** SMART on FHIR for third-party app substitutability
- **Laboratory Interfaces:** HL7 v2 messaging for laboratory analyser interfaces (ORM/ORU messages)
- **Legacy Analyser Protocol:** ASTM E1394 for older analysers
- **Clinical Document Exchange:** CDA R2 for discharge summaries and referral letters
- **HMIS Reporting:** DHIS2 API integration

## Clinical Architecture

- **Clinical Modelling:** openEHR two-level modelling — stable Reference Model + configurable clinical Archetypes per country/facility
- **Terminology Service:** Single gateway to ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm, ATC code systems
- **Clinical Decision Support:** Four-tier alert engine (Info / Warning / Serious / Fatal)
- **Consent Management:** Configurable Consent Engine (opt-in, opt-out, mixed — per jurisdiction)
- **Patient Identity:** EMPI (Enterprise Master Patient Index) with probabilistic matching
- **Radiology:** DICOM gateway for radiology image management
- **Real-Time Alerts:** WebSocket for critical lab values and emergency notifications

## Country Configuration Layer

- **Regulatory Frameworks:** PDPA 2019 (Uganda), HIPAA (USA), Privacy Act 1988 (Australia), DISHA (India)
- **National ID Systems:** NIN (Uganda), Aadhaar (India), Medicare Number (Australia), Huduma Namba (Kenya)
- **Financial Localisation:** Currency, tax tables, and insurance models per country
- **HMIS Form Definitions:** Uganda 105/108, Kenya MOH 105, India HMIS
- **Immunisation Schedules:** EPI Uganda, UIP India, NIP Australia
- **Drug Formularies:** NDA Uganda, PPB Kenya, CDSCO India, TGA Australia

# Domain: Healthcare (Uganda/Africa-Adapted, Globally Configurable)

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | Uganda Ministry of Health (MoH), Uganda National Drug Authority (NDA), NHIS Uganda, Uganda MoH eHealth Division |
| **Key Standards** | Uganda PDPA 2019, HL7 FHIR R4, ICD-10/ICD-11, LOINC, SNOMED CT, HL7 v2, HMIS 105/108/033b, DHIS2 |
| **Risk Level** | High — patient health data, clinical safety implications |
| **Audit Requirement** | Mandatory — all patient data access must be logged |
| **Data Classification** | Patient Health Information (PHI), Personally Identifiable Information (PII) |

## Global Regulatory Superset

Medic8 is designed for deployment across multiple jurisdictions. The system must support a configurable compliance engine that enforces the data protection and health-sector regulations of each target market. The following frameworks constitute the regulatory superset:

- **Uganda:** Data Protection and Privacy Act 2019 (PDPA), MoH HMIS standards (HMIS 105, HMIS 108, HMIS 033b), NDA drug scheduling and dispensing regulations
- **Kenya:** Data Protection Act 2019, MoH Kenya Health Information System (KHIS) standards, Pharmacy and Poisons Board regulations
- **Tanzania:** Electronic and Postal Communications Act (EPOCA), Health Data regulations under the Tanzania Medicines and Medical Devices Authority (TMDA)
- **Rwanda:** Law No. 058/2021 on the Protection of Personal Data and Privacy, Rwanda Biomedical Centre (RBC) health data standards
- **India:** Digital Information Security in Healthcare Act (DISHA, draft), Ayushman Bharat Digital Mission (ABDM) interoperability standards, ABHA health ID integration
- **Australia:** Privacy Act 1988 (including Australian Privacy Principles), My Health Records Act 2012, Therapeutic Goods Act 1989
- **Nigeria:** Nigeria Data Protection Act 2023 (NDPA), National Health Insurance Authority (NHIA) Act, FMOH National Health ICT Strategic Framework
- **USA (PEPFAR facilities):** HIPAA Privacy Rule and Security Rule apply to all US-government-funded health data; PEPFAR Monitoring, Evaluation, and Reporting (MER) indicator compliance

Each deployment must activate the applicable regulatory profile at tenant configuration time. The system shall not permit operation without an assigned regulatory profile.

## Default Feature Modules

- Patient Management (registration, global identity, Enterprise Master Patient Index)
- Clinical Documentation (OPD, IPD, Emergency, Maternity)
- Pharmacy and Dispensary
- Laboratory Information System (LIS)
- Radiology and Imaging
- Billing and Revenue Management
- Insurance Management
- Financial Accounting (dual mode: cash-basis for small clinics, accrual for hospitals)
- Human Resources and Payroll
- HMIS Reporting and DHIS2 Integration
- Patient Portal and Mobile App

## Auto-Injected Requirements

The following `[DOMAIN-DEFAULT]` non-functional requirements are injected at scaffold time. Each requirement is adapted from generic healthcare baselines to reflect Uganda/Africa operational constraints (intermittent connectivity, low-bandwidth environments, multi-language support).

See `references/nfr-defaults.md` for the full tagged blocks. Key injected areas:

- **NFR-HC-001:** Audit logging — all PHI access, modification, and export events must be logged with actor, timestamp, IP address, and action type
- **NFR-HC-002:** Data encryption — AES-256 at rest, TLS 1.2+ in transit; encryption must function on low-spec hardware common in Ugandan health facilities
- **NFR-HC-003:** Access control — role-based access control (RBAC) with facility-scoped permissions; support for MoH-defined user roles (clinician, pharmacist, lab technician, records officer, administrator)
- **NFR-HC-004:** Offline capability — core clinical workflows (patient registration, vitals capture, prescription writing) must operate offline and synchronise when connectivity resumes
- **NFR-HC-005:** Performance under constraint — page load time of 3 seconds or less on 3G connections (downstream 1 Mbps); API response time of 2 seconds or less at P95 under normal load
- **NFR-HC-006:** Data residency — patient data must reside in-country unless the regulatory profile explicitly permits cross-border transfer; configurable per jurisdiction
- **NFR-HC-007:** Interoperability — HL7 FHIR R4 RESTful API for patient, encounter, observation, and medication resources; DHIS2 ADX/JSON export for HMIS aggregate reporting
- **NFR-HC-008:** Localisation — support for English, Luganda, Kiswahili, and French at minimum; date, currency, and number formatting configurable per locale
- **NFR-HC-009:** Backup and recovery — automated daily backups with a Recovery Point Objective (RPO) of 24 hours and Recovery Time Objective (RTO) of 4 hours; backup verification must be testable without production data exposure

## References

- [regulations.md](references/regulations.md) — Uganda PDPA 2019, HIPAA (PEPFAR scope), HL7/FHIR, NDA, MoH HMIS framework
- [architecture-patterns.md](references/architecture-patterns.md) — PHI isolation, audit logging, multi-tenant with facility-scoped data, offline-first synchronisation
- [security-baseline.md](references/security-baseline.md) — encryption, access control, PHI handling adapted for low-resource environments
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection (NFR-HC-001 through NFR-HC-009)

### Additional References

- Uganda MoH HMIS Tools (HMIS 105 Outpatient, HMIS 108 Inpatient, HMIS 033b Laboratory)
- PEPFAR Monitoring, Evaluation, and Reporting (MER) Indicator Reference Guide
- WHO Model List of Essential Medicines (adapted for Uganda Essential Medicines and Health Supplies List)
- DHIS2 Developer Documentation (API integration, data elements, organisation units)

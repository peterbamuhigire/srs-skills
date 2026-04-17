# Executive Summary

| Field | Value |
|---|---|
| **Project** | Medic8 |
| **Version** | 1.0 |
| **Date** | 2026-04-03 |
| **Authors** | Peter — Chwezi Core Systems (chwezicore.com) |
| **Status** | Draft |
| **Standards** | IEEE 29148-2018, IEEE 1233-1998 |

## Executive Summary

Medic8 is a multi-tenant Software-as-a-Service (SaaS) healthcare information management system engineered to replace the fragmented, paper-heavy workflows that dominate hospitals and clinics across Uganda and Africa. The platform delivers a unified electronic health record spanning patient registration, outpatient and inpatient care, pharmacy, laboratory, billing, insurance, human resources, and statutory Health Management Information System (HMIS) reporting. Medic8 targets 6 market segments — private clinics, mission and NGO hospitals, government-aided facilities, multi-facility networks, PEPFAR/Global Fund implementing partners, and national referral hospitals — serving an addressable market of over 6,000 registered health facilities in Uganda alone.

The platform is positioned as Africa-first and globally configurable. Uganda is the launch market, with a country configuration layer that adapts regulatory frameworks, clinical protocols, financial systems, and reporting requirements per tenant to enable expansion to Kenya, Tanzania, Rwanda, the Democratic Republic of Congo (DRC), Nigeria, India, and Australia without forking the codebase. Medic8 does for hospitals what Academia Pro does for schools: delivers enterprise-grade capability at a price the market can sustain. Against ClinicMaster, Medic8 offers mobile-first design, SaaS delivery, offline resilience, mobile money integration, HL7 FHIR R4 compliance, and a patient portal — capabilities ClinicMaster's desktop architecture cannot match. Against OpenMRS and its Uganda fork UgandaEMR, Medic8 delivers a 3-year total cost of ownership (TCO) of USD 9,400-71,000 versus USD 35,000-130,000 for OpenMRS, while including billing, insurance, HR, payroll, and local Uganda-based support that OpenMRS lacks.

The system architecture centres on centralised multi-tenant isolation via `facility_id`, openEHR two-level modelling for multi-country clinical configurability, an event-driven Electronic Health Record (EHR) data bus, and a FHIR R4 native API. An offline-first design ensures that core clinical workflows — patient registration, vital signs capture, prescription writing, and dispensing — operate without internet connectivity and synchronise when connectivity resumes. The technology stack uses PHP 8.2+ with MySQL 8.x on the backend, Bootstrap 5/Tabler on the web frontend, and native Kotlin (Android) and Swift (iOS) mobile applications. Healthcare interoperability is achieved through FHIR R4, HL7 v2 for laboratory analysers, DICOM for radiology, and DHIS2 integration for HMIS reporting.

Medic8 follows a 4-phase build strategy. Phase 1 (Foundation, 6 months) delivers patient registration, outpatient department (OPD), pharmacy, basic laboratory, and cash billing, targeting 10 private clinics. Phase 2 (Expansion) adds inpatient care, maternity, immunisation, insurance, inventory, HR/payroll, and HMIS reporting, targeting 50 facilities. Phase 3 (Programmes and Patient Engagement) introduces HIV/AIDS and TB programme management, PEPFAR Monitoring, Evaluation, and Reporting (MER) indicators, the patient portal, and Community Health Worker (CHW) mobile application, targeting PEPFAR implementing partners. Phase 4 (Advanced Specialty) delivers theatre, blood bank, Picture Archiving and Communication System (PACS), multi-facility patient record sharing, and the Director analytics platform, targeting hospital networks and national referral hospitals.

## Purpose and Scope

### Purpose

This Product Requirements Document (PRD) defines the functional scope, architectural constraints, deployment model, and phased delivery plan for Medic8. It serves as the authoritative requirements baseline for all design, development, testing, and acceptance activities across the 4-phase build sequence. The document is governed by IEEE 29148-2018 (Systems and Software Engineering — Life Cycle Processes — Requirements Engineering) and IEEE 1233-1998 (Guide for Developing System Requirements Specifications). All requirements herein are subject to formal review and sign-off before development begins, consistent with the project's Water-Scrum-Fall methodology.

### In Scope

The following capabilities are within the scope of this PRD, organised by delivery phase:

- **Phase 1 (Foundation):** Patient registration and master index, OPD consultation workflow, pharmacy and dispensary, basic laboratory information system, appointments and scheduling, billing and revenue management (cash payments, mobile money)
- **Phase 2 (Expansion):** Inpatient department and ward management, emergency department, maternity and antenatal care, immunisation, dental services, eye care, mortuary management, radiology and imaging, referral management, human resources and payroll, medical records management, insurance management, financial accounting (dual mode), inventory and stores management, Uganda HMIS reporting and DHIS2 integration, disease surveillance
- **Phase 3 (Programmes and Patient Engagement):** HIV/AIDS programme management, TB programme management, nutrition and dietetics, community health integration, patient portal and mobile application, FHIR R4 API for external interoperability, PEPFAR MER indicator reporting
- **Phase 4 (Advanced Specialty):** Theatre and surgical management, blood bank and transfusion, ambulance management, physiotherapy and rehabilitation, multi-facility patient record sharing, Director analytics platform, PACS integration

### Out of Scope

The following are excluded from this PRD:

- Telemedicine and video consultation capabilities
- Electronic prescribing to external retail pharmacies
- Health insurance exchange or marketplace functionality
- Research data repositories or clinical trial management
- Integration with wearable medical devices or Internet of Things (IoT) sensors
- Artificial intelligence diagnostic imaging (computer-aided detection)
- Consumer wellness features unrelated to clinical care delivery

## Definitions and References

### Definitions

All domain-specific terms, acronyms, and abbreviations used in this document are defined in the project glossary at `_context/glossary.md`. Key terms include but are not limited to: EHR, FHIR, HMIS, DHIS2, openEHR, PEPFAR, MER, EMPI, ABAC, RBAC, PHI, and PACS.

### Governing Standards

- **IEEE 29148-2018** — Systems and Software Engineering — Life Cycle Processes — Requirements Engineering. Governs the structure, content, and quality attributes of all requirements in this document.
- **IEEE 1233-1998** — Guide for Developing System Requirements Specifications. Provides guidance on elicitation, analysis, and specification of system-level requirements.

### Supplementary References

- Uganda Data Protection and Privacy Act 2019 (PDPA)
- HL7 FHIR R4 Specification (hl7.org/fhir/R4)
- Uganda Ministry of Health HMIS Tools (HMIS 105, HMIS 108, HMIS 033b)
- PEPFAR Monitoring, Evaluation, and Reporting (MER) Indicator Reference Guide
- ICD-10 and ICD-11 Classification of Diseases
- DHIS2 Developer Documentation
- openEHR Architecture Overview and Archetype Model
- WHO Model List of Essential Medicines (Uganda adaptation)

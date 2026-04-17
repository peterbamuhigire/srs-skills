# 1 Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Medic8, a multi-tenant Software-as-a-Service (SaaS) healthcare information management system developed by Chwezi Core Systems. The document serves as the authoritative requirements baseline for all design, development, testing, and acceptance activities across the 4-phase build sequence.

This SRS is governed by IEEE 830-1998 (Recommended Practice for Software Requirements Specifications) and IEEE 29148-2018 (Systems and Software Engineering -- Life Cycle Processes -- Requirements Engineering). All requirements herein are subject to formal review and sign-off before development begins, consistent with the project's Water-Scrum-Fall methodology.

The intended audience for this document includes:

- **Software developers and architects** responsible for implementing Medic8 modules
- **Quality assurance engineers and testers** responsible for verifying requirements through test cases
- **Project stakeholders** including the product owner, facility administrators, and clinical advisors who validate that requirements reflect operational needs
- **Regulatory reviewers** including Uganda Ministry of Health (MoH) eHealth Division, National Drug Authority (NDA), and data protection compliance officers who verify adherence to statutory obligations

## 1.2 Document Conventions

### Requirement Identifiers

All requirements in this SRS carry a unique identifier using the following prefixes:

- **FR-** -- Functional Requirement (e.g., FR-OPD-001)
- **NFR-** -- Non-Functional Requirement (e.g., NFR-SEC-001)

Identifiers follow the pattern `{PREFIX}-{MODULE}-{SEQUENCE}`, where `{MODULE}` is a 2-4 character abbreviation of the functional area and `{SEQUENCE}` is a zero-padded 3-digit number.

### Priority Levels

Each requirement is assigned one of 4 priority levels:

| Priority | Definition |
|---|---|
| Critical | Must be implemented for the system to function. Failure to implement blocks deployment of the containing phase. |
| High | Must be implemented within the assigned phase. Deferral requires formal change request and stakeholder approval. |
| Medium | Should be implemented within the assigned phase. May be deferred to the next phase with project manager approval. |
| Low | May be implemented if time and budget permit within the assigned phase. |

### Keyword Conventions

The following keywords carry specific contractual meaning per IEEE 830-1998:

- **Shall** -- The requirement is mandatory. The system must satisfy it to pass acceptance testing.
- **Should** -- The requirement is recommended. The system is expected to satisfy it unless a documented justification for omission exists.
- **May** -- The requirement is optional. Implementation is at the discretion of the development team.

### Typographic Conventions

- `Monospace` denotes file paths, code identifiers, database fields, API endpoints, and terminal commands.
- **Bold** denotes UI element names, field labels, and requirement identifiers.
- *Italic* denotes critical warnings, caveats, and first use of defined terms.

## 1.3 Intended Audience and Reading Suggestions

| Reader Role | Recommended Sections | Rationale |
|---|---|---|
| Product Owner / Facility Director | 1, 2, 3.2 (System Features) | Validates scope, user classes, and feature coverage against business goals |
| Software Architect | 2, 3 (all subsections), 4, 5 | Drives design decisions from interfaces, constraints, and quality attributes |
| Backend Developer | 2.4, 2.5, 3.2, 3.3, 4 | Implements functional requirements, software interfaces, and data models |
| Frontend / Mobile Developer | 3.1, 3.2, 4 | Builds user interfaces against specified UI requirements and quality attributes |
| QA Engineer / Tester | 1.2 (conventions), 3 (all subsections), 4 | Derives test cases from functional and non-functional requirements |
| Clinical Advisor / Doctor | 2.1, 2.3, 3.2 (clinical modules) | Reviews clinical workflow accuracy and safety requirements |
| Regulatory / Compliance Officer | 1.6, 2.5, 3.3, 4 (security, privacy) | Verifies PDPA 2019, HMIS, and interoperability compliance |
| Database Administrator | 2.4, 2.5, 3.3, 4 (performance) | Plans schema design, multi-tenancy isolation, and performance targets |
| Project Manager | 1, 2, 5 (appendices) | Tracks scope, assumptions, dependencies, and phase boundaries |

## 1.4 Product Scope

### System Description

Medic8 is a multi-tenant SaaS healthcare information management system that delivers a unified electronic health record spanning patient registration, outpatient and inpatient care, pharmacy, laboratory, radiology, billing, insurance, human resources, payroll, and statutory Health Management Information System (HMIS) reporting. The platform is Africa-first and globally configurable: Uganda is the launch market, with a country configuration layer that adapts regulatory frameworks, clinical protocols, financial systems, and reporting requirements per tenant to enable expansion to Kenya, Tanzania, Rwanda, the Democratic Republic of Congo (DRC), Nigeria, India, and Australia without forking the codebase.

### Target Market

Medic8 targets 6 market segments across an addressable market of over 6,000 registered health facilities in Uganda:

1. Private clinics (1-5 consultation rooms, pharmacy, basic lab)
2. Mission and NGO hospitals (multi-department with inpatient, maternity, lab, pharmacy)
3. Government-aided hospitals (HC IVs, General Hospitals, Regional Referrals)
4. Multi-facility hospital networks (Aga Khan, AAR, Case Medical, Norvik)
5. PEPFAR/Global Fund implementing partners (HIV/TB programme management)
6. National referral hospitals (Phase 4 target)

### 4-Phase Build Plan

Medic8 follows a phased delivery strategy. This SRS covers all 4 phases, with Phase 1 treated as the MVP priority for initial development and acceptance.

| Phase | Name | Duration | Modules | Target |
|---|---|---|---|---|
| 1 | Foundation | 6 months | Patient Registration, OPD, Pharmacy, Basic Lab, Billing, Appointments, Auth/RBAC | 10 private clinics |
| 2 | Expansion | TBD | IPD, Maternity, Immunisation, Emergency, Insurance, HR/Payroll, HMIS, Inventory, Full Lab, Radiology, Dental, Eye Care, Mortuary, Referral, Medical Records, Accounting, Disease Surveillance | 50 facilities |
| 3 | Programmes | TBD | HIV/AIDS, TB, FHIR API, PEPFAR MER, CHW App, Patient App, Telemedicine, Nutrition, Community Health | PEPFAR implementing partners |
| 4 | Advanced Specialty | TBD | Theatre, Blood Bank, PACS, Ambulance, Physiotherapy, Director Platform, AI Analytics | Hospital networks and national referrals |

### Relationship to Other Systems

Medic8 is a standalone SaaS platform. It is not a component of a larger system. It interfaces with external systems (DHIS2, insurance companies, mobile money providers, laboratory analysers, PACS, national ID systems, and SMS gateways) through defined integration points documented in Section 3 of this SRS.

## 1.5 Definitions, Acronyms, and Abbreviations

The complete project glossary is maintained in `_context/glossary.md` and governs all terminology in this SRS. The 20 most critical acronyms are listed below for immediate reference.

| Acronym | Full Form |
|---|---|
| FHIR | Fast Healthcare Interoperability Resources (HL7 standard for health data exchange via RESTful APIs) |
| HL7 | Health Level Seven International (health information exchange standards organisation) |
| ICD-10 | International Classification of Diseases, 10th Revision (WHO diagnostic coding standard) |
| SNOMED CT | Systematised Nomenclature of Medicine Clinical Terms (comprehensive clinical terminology) |
| LOINC | Logical Observation Identifiers Names and Codes (laboratory observation coding standard) |
| HMIS | Health Management Information System (Uganda MoH health facility data reporting system) |
| DHIS2 | District Health Information Software 2 (MoH aggregate reporting platform) |
| PEPFAR | President's Emergency Plan for AIDS Relief (US government HIV/AIDS funding programme) |
| EMPI | Enterprise Master Patient Index (cross-facility unique patient identity system) |
| RBAC | Role-Based Access Control (permission model assigning access rights to roles) |
| ABAC | Attribute-Based Access Control (fine-grained permission model based on user, resource, and environment attributes) |
| CPOE | Computerised Physician Order Entry (electronic system for entering medical orders) |
| CDS | Clinical Decision Support (computer-based patient-specific clinical recommendations) |
| BCMA | Barcode Medication Administration (barcode-verified medication dispensing) |
| MAR | Medication Administration Record (per-dose medication tracking document) |
| NEWS2 | National Early Warning Score 2 (standardised acute illness severity scoring) |
| EPI | Expanded Programme on Immunisation (WHO childhood vaccination programme) |
| NMS | National Medical Stores (Uganda government medicines supply agency) |
| PDPA | Data Protection and Privacy Act 2019 (Uganda's primary data protection legislation) |
| MoMo | Mobile Money (mobile-based financial transaction service, e.g., MTN MoMo, Airtel Money) |

## 1.6 References

The following standards, specifications, and regulatory instruments govern this SRS:

### IEEE Standards

1. IEEE 830-1998 -- Recommended Practice for Software Requirements Specifications
2. IEEE 29148-2018 -- Systems and Software Engineering -- Life Cycle Processes -- Requirements Engineering
3. IEEE 1233-1998 -- Guide for Developing System Requirements Specifications
4. IEEE 610.12-1990 -- Standard Glossary of Software Engineering Terminology

### Healthcare Interoperability Standards

5. HL7 FHIR R4 -- Fast Healthcare Interoperability Resources, Release 4 (hl7.org/fhir/R4)
6. HL7 v2 -- Health Level Seven Version 2 Messaging Standard (laboratory analyser interface)
7. ASTM E1394 -- Standard Specification for Transferring Information Between Clinical Laboratory Instruments and Computer Systems
8. DICOM -- Digital Imaging and Communications in Medicine (radiology image exchange)
9. openEHR -- Open Electronic Health Record architecture and archetype model

### Clinical Terminology Standards

10. WHO ICD-10 -- International Classification of Diseases, 10th Revision
11. WHO ICD-11 -- International Classification of Diseases, 11th Revision
12. LOINC -- Logical Observation Identifiers Names and Codes (Regenstrief Institute)
13. SNOMED CT -- Systematised Nomenclature of Medicine Clinical Terms (SNOMED International)
14. RxNorm -- Standardised Nomenclature for Clinical Drugs (US National Library of Medicine)

### Regulatory Instruments

15. Uganda Data Protection and Privacy Act 2019 (PDPA)
16. Uganda Ministry of Health HMIS Tools (HMIS 105, HMIS 108, HMIS 033b)
17. PEPFAR Monitoring, Evaluation, and Reporting (MER) Indicator Reference Guide

## 1.7 Overview

The remainder of this SRS is organised as follows:

- **Section 2 -- Overall Description** describes the product perspective, product functions summarised by phase, user classes and characteristics, operating environment, design and implementation constraints, and assumptions and dependencies. This section provides the context necessary to interpret the specific requirements in Section 3.

- **Section 3 -- External Interface Requirements** specifies the user interfaces, hardware interfaces, software interfaces, and communications interfaces that Medic8 exposes or consumes. Each interface is described with sufficient detail to enable design and testing.

- **Section 4 -- System Features** (planned) defines the functional requirements for each module organised by phase, using stimulus-response format. Each feature includes a description, priority, stimulus/response sequences, and associated non-functional constraints.

- **Section 5 -- Non-Functional Requirements** (planned) specifies performance, security, availability, data quality, FHIR compliance, and localisation requirements with measurable thresholds.

- **Section 6 -- Appendices** (planned) includes the traceability matrix mapping requirements to business goals, the glossary cross-reference, and the change history for this document.

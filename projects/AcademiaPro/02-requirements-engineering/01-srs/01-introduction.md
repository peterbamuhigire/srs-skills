# Software Requirements Specification — Academia Pro

## Section 1: Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Academia Pro, a multi-tenant Software as a Service (SaaS) school management platform developed by Chwezi Core Systems. This document governs Phase 1 of a 12-phase build sequence and constitutes the formal requirements baseline for Phase 1 development.

This SRS is the authoritative contract between the product owner and the development team. No Phase 1 feature shall be implemented that is not described herein. No Phase 1 feature described herein shall be omitted from the deliverable without a formal change request and written approval from the product owner.

### 1.2 Document Conventions

This document conforms to IEEE Std 830-1998 (Software Requirements Specifications) and applies terminology defined in IEEE Std 610.12-1990 (Standard Glossary of Software Engineering Terminology).

| Convention | Meaning |
|---|---|
| **The system shall** | Mandatory requirement — must be implemented |
| **The system should** | Desirable requirement — implement if feasible |
| **The system may** | Optional capability — implement at product owner's discretion |
| `FR-XXX-NNN` | Functional requirement identifier |
| `NFR-XXX-NNN` | Non-functional requirement identifier |
| `BR-XXX-NNN` | Business rule cross-reference |
| `[CONTEXT-GAP: topic]` | Required context absent from `_context/` files |
| `[V&V-FAIL: reason]` | Requirement fails verification/validation gate |
| `[GLOSSARY-GAP: term]` | Term used but not yet defined in `_context/glossary.md` |

**Emphasis rules (Three-Emphasis Rule):**

- `**Bold**` — requirement identifiers and UI element names only
- `*Italic*` — critical warnings and first use of defined terms
- `` `Monospace` `` — file paths, environment variables, API endpoints, code identifiers

**Numbering:** All version numbers, section references, measurements, and thresholds use figures, not words.

### 1.3 Intended Audience and Reading Suggestions

| Audience | Recommended Sections |
|---|---|
| Product Owner (Peter — Chwezi Core Systems) | All sections; Section 4 requires sign-off before development begins |
| Lead Developer / Architect | Sections 2, 3, 4, 5, and 6 (NFR) |
| Frontend Engineer (React/TypeScript) | Sections 3.1, 4 (FR-AUTH, FR-SIS, FR-FEE, FR-ATT, FR-EXM, FR-RPT, FR-RBAC) |
| Backend Engineer (PHP/Laravel) | Sections 3.3, 3.4, 4 (all FR groups), Section 5 |
| Mobile Engineer (Android/Kotlin) | Sections 3.1, 3.2, 4 (FR-AUTH, FR-SIS, FR-ATT, FR-EXM, FR-RBAC) |
| QA / Test Engineer | Section 4 (Verifiability criteria for every FR), Section 6 (NFR) |
| Compliance Officer | Sections 5.1, 6 (EDU-NFR-001 through EDU-NFR-004, UG-NFR-002) |

### 1.4 Product Scope

Academia Pro is a *multi-tenant SaaS* school management platform targeting schools in Uganda and Sub-Saharan Africa. Each subscribing school is an isolated *tenant* on the shared platform. The system automates repeatable school administrative processes — fee collection, attendance recording, mark entry, report card generation, and government (EMIS) reporting — while remaining operable by a single school administrator after module-specific training.

**Phase 1 scope** covers the following modules delivered as a web application:

1. Student Information System (SIS)
2. Academics Setup
3. Fees Management (manual cash/bank entry; SchoolPay integration is Phase 2)
4. Attendance
5. Examinations and UNEB Grading Engine
6. Report Card Generation
7. User Roles and Role-Based Access Control (RBAC)
8. EMIS / Government Data Export
9. Tenant Lifecycle Management (Super Admin functions)
10. Audit Trail (cross-cutting)

**Out of Phase 1 scope** (deferred to later phases): SchoolPay webhook integration, HR, Library, Transport, Hostel, Communication module, Homework, Download Centre, Calendar, Certificates, Front CMS, Android mobile applications, iOS applications, pan-Africa currency/grading engines, Claude AI analytics.

**Business goals addressed by Phase 1:**

- Capture 500 Uganda schools within 24 months of launch.
- Provide fully automated UNEB-graded report cards (PLE, UCE, UACE) with zero manual computation.
- Deliver EMIS/MoES integration so schools submit statutory reports without re-entering data.

See `_context/vision.md` Section "Goals" for the full goal set and success criteria.

### 1.5 Definitions, Acronyms, and Abbreviations

The following terms are used throughout this document. Complete definitions are maintained in `_context/glossary.md`. First use in this document is *italicised*.

| Term / Acronym | Definition |
|---|---|
| SRS | Software Requirements Specification |
| SaaS | Software as a Service |
| Tenant | A subscribing school on the Academia Pro platform. Equivalent to "franchise" in the `multi-tenant-saas-architecture` skill reference. |
| `tenant_id` | The unique integer identifier for a tenant, present on every tenant-scoped database row and in every authenticated JWT payload. |
| RBAC | Role-Based Access Control |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| BR | Business Rule |
| IEEE 830 | IEEE Recommended Practice for Software Requirements Specifications (1998) |
| IEEE 610.12 | IEEE Standard Glossary of Software Engineering Terminology (1990) |
| PLE | Primary Leaving Examination — Uganda national examination for Primary 7 |
| UCE | Uganda Certificate of Education — O-Level national examination |
| UACE | Uganda Advanced Certificate of Education — A-Level national examination |
| UNEB | Uganda National Examinations Board |
| EMIS | Education Management Information System — MoES statutory reporting |
| MoES | Ministry of Education and Sports (Uganda) |
| PDPO | Personal Data Protection and Privacy Act 2019 (Uganda) |
| NIN | National Identification Number (NIRA Uganda) |
| LIN | Learner Identification Number (MoES Uganda) |
| EAT | East Africa Time (UTC+3) |
| JWT | JSON Web Token (RFC 7519) |
| CSRF | Cross-Site Request Forgery |
| TLS | Transport Layer Security |
| AES | Advanced Encryption Standard |
| P95 | 95th percentile response time |
| CRUD | Create, Read, Update, Delete |
| PWA | Progressive Web Application |
| FCM | Firebase Cloud Messaging |
| API | Application Programming Interface |
| REST | Representational State Transfer |
| UUID | Universally Unique Identifier (RFC 4122) |
| Three-tier panel | The architectural separation of the platform into: school admin workspace (`/`), super admin panel (`/adminpanel/`), and end-user portal (`/memberpanel/`) per the `multi-tenant-saas-architecture` skill |

### 1.6 References

| Identifier | Document |
|---|---|
| IEEE 830-1998 | IEEE Recommended Practice for Software Requirements Specifications |
| IEEE 610.12-1990 | IEEE Standard Glossary of Software Engineering Terminology |
| IEEE 1233-1998 | IEEE Guide for Developing System Requirements Specifications |
| IEEE 1012-2016 | IEEE Standard for System, Software, and Hardware Verification and Validation |
| ASTM E1340 | Standard Guide for Rapid Evaporation Immunoassay Measurement (not applicable — referenced in project standard set per `CLAUDE.md`) |
| PDPO-2019 | Uganda Personal Data Protection and Privacy Act 2019 |
| UNEB-PLE | UNEB Primary Leaving Examination marking guide (current edition) |
| UNEB-UCE | UNEB Uganda Certificate of Education marking guide (current edition) |
| UNEB-UACE | UNEB Uganda Advanced Certificate of Education marking guide (current edition) |
| MoES-EMIS | MoES EMIS Data Dictionary (current edition) |
| `_context/vision.md` | Academia Pro Project Vision |
| `_context/features.md` | Academia Pro Feature List by Phase |
| `_context/business_rules.md` | Academia Pro Business Rules Register |
| `_context/tech_stack.md` | Academia Pro Technology Stack |
| `_context/stakeholders.md` | Academia Pro Stakeholder Register |
| `_context/personas.md` | Academia Pro User Personas |
| `_context/gap-analysis.md` | Academia Pro Gap Analysis (HIGH/MEDIUM/LOW priority gaps) |
| `_context/glossary.md` | Academia Pro Project Glossary |
| `01-strategic-vision/01-prd/` | Academia Pro Product Requirements Document |
| `01-strategic-vision/02-vision-statement/` | Academia Pro Vision Statement |
| `01-strategic-vision/03-business-case/` | Academia Pro Business Case |
| `skills/multi-tenant-saas-architecture` | Multi-Tenant SaaS Architecture Skill (Chwezi internal) |
| `skills/dual-auth-rbac` | Dual Authentication and RBAC Skill (Chwezi internal) |
| `skills/php-modern-standards` | PHP Modern Standards Skill (Chwezi internal) |
| `skills/mysql-best-practices` | MySQL Best Practices Skill (Chwezi internal) |
| `skills/android-development` | Android Development Skill (Chwezi internal) |

### 1.7 Overview

This SRS is organised as follows:

- **Section 2 — Overall Description:** Places Academia Pro in its product context, summarises Phase 1 functions, characterises user classes, specifies the operating environment, and states design constraints and assumptions.
- **Section 3 — External Interface Requirements:** Specifies all interfaces between the system and external entities — user interfaces, hardware interfaces, third-party software interfaces, and communications interfaces.
- **Section 4 — Functional Requirements:** Specifies every Phase 1 functional requirement using IEEE 830 stimulus-response form. Each requirement includes input specifications, output specifications, error conditions, business rule references, and a verifiability criterion.
- **Section 5 — System Constraints:** Specifies design constraints, regulatory constraints, and implementation constraints that restrict the solution space.
- **Section 6 — Non-Functional Requirements:** Specifies measurable quality attributes (performance, availability, security, data protection, Uganda-specific).

Sections 4 and 6 constitute the acceptance baseline for Phase 1. A feature is accepted only if it satisfies the verifiability criterion stated in its requirement.

# 1 Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Kulima, a multi-tenant Software as a Service (SaaS) Farm Management Information System (FMIS). The document serves as the binding contract between the product owner, development team, and quality assurance personnel for what the system shall do.

**Intended audience:**

- Product owner and project stakeholders
- Software architects and developers implementing the Chwezi Core backend, Android (Kotlin/Jetpack Compose), and iOS (SwiftUI) clients
- Quality assurance engineers deriving test cases from verifiable requirements
- Integration partners (Jaguza IoT, mobile money providers, camera manufacturers)
- Banks, cooperatives, and regulatory bodies evaluating system capabilities

This SRS is structured in accordance with IEEE Std 830-1998 and supplemented by IEEE 29148-2018 guidance on stakeholder and system requirements.

## 1.2 Scope

**Product name:** Kulima

**Product description:** Kulima is an offline-first, mobile-money-integrated FMIS providing web and mobile applications for individual farmers, farm businesses, cooperatives, and investors to manage farms, crops, livestock, finances, workers, inventory, IoT devices, CCTV surveillance, GPS tracking, supply chain traceability, marketplace, and an AI-powered farm advisor.

**What Kulima does:**

- Manages farm and plot registration with GPS polygon boundaries and Uganda administrative hierarchy
- Tracks complete crop lifecycle (planning, planting, activities, inputs, health monitoring, harvest, yield analysis)
- Tracks individual animal records and herd/flock management for 12+ species
- Records farm income, expenses, budgets, and generates bank-ready financial reports
- Manages tasks, worker profiles, payroll, and mobile money wage disbursement
- Provides farm-specific weather forecasts and climate-smart advisory
- Manages input inventory, equipment, and produce storage with expiry and low-stock alerts
- Enables supply chain traceability with QR codes and EU Deforestation Regulation (EUDR) Due Diligence Statement (DDS) generation
- Integrates Jaguza IoT ear tags for livestock health monitoring and disease early warning
- Provides GPS animal tracking with geofence breach alerts (2-minute SLA)
- Proxies live CCTV camera streams (RTSP to HLS) with motion detection alerts
- Delivers AI-powered pest/disease identification and natural language farm advisory via Claude API
- Supports cooperative member management, collection centres, quality grading, and bulk mobile money disbursement
- Provides a director platform for consolidated multi-farm oversight and approval workflows
- Operates as a marketplace connecting farmers with buyers, agro-dealers, and service providers

**What Kulima does not do:**

- Kulima does not store video recordings; camera streams are proxied in real time
- Kulima does not validate mobile money transaction IDs against provider APIs; transaction references are recorded but not reconciled
- Kulima does not auto-deduct loan repayments; outstanding balances are manually tracked
- Kulima does not fetch market prices automatically in Phase 1; prices are manually recorded
- Kulima does not replace government extension services; it provides a referral channel
- Kulima does not process payments for marketplace transactions; it connects buyers and sellers who transact independently

## 1.3 Definitions, Acronyms, and Abbreviations

The complete glossary is maintained in `_context/glossary.md`. Key terms used throughout this SRS:

| Term | Definition |
|---|---|
| FMIS | Farm Management Information System |
| Chwezi Core | Custom PHP/MySQL multi-tenant SaaS framework shared across Kulima, Academia Pro, and Medic8 |
| Tenant | A single customer account (individual farmer, farm business, or cooperative) with complete data isolation |
| Enterprise | A distinct production unit within a farm (e.g., maize crop enterprise, dairy cattle enterprise) |
| Crop Season | A defined period during which a specific crop variety is grown on a specific plot |
| Collection Centre | A physical location where cooperative members deliver produce for weighing and grading |
| DDS | Due Diligence Statement required under EUDR |
| EUDR | EU Deforestation Regulation 2023/1115 |
| GeoJSON | Open standard format for encoding geographic data structures using JSON |
| Geofence | A virtual geographic boundary triggering alerts when a tracked entity exits the perimeter |
| RBAC | Role-Based Access Control |
| JWT | JSON Web Token |
| HLS | HTTP Live Streaming |
| RTSP | Real-Time Streaming Protocol |
| NDVI | Normalised Difference Vegetation Index |
| IoT | Internet of Things |
| MoMo | MTN Mobile Money |
| SACCO | Savings and Credit Cooperative Organisation |
| NIN | National Identification Number (Uganda) |
| NSSF | National Social Security Fund |
| PAYE | Pay As You Earn income tax |
| MAAIF | Ministry of Agriculture, Animal Industry and Fisheries (Uganda) |
| UCDA | Uganda Coffee Development Authority |
| NAADS | National Agricultural Advisory Services |
| OWC | Operation Wealth Creation |
| UGX | Uganda Shilling |

## 1.4 References

| Standard | Title | Relevance |
|---|---|---|
| IEEE Std 830-1998 | Recommended Practice for Software Requirements Specifications | Primary structural template for this SRS |
| IEEE 29148-2018 | Systems and Software Engineering — Life Cycle Processes — Requirements Engineering | Supplementary guidance on stakeholder and system requirements |
| IEEE Std 610.12-1990 | Standard Glossary of Software Engineering Terminology | Terminology definitions |
| IEEE Std 1233-1998 | Guide for Developing System Requirements Specifications | System-level requirements guidance |
| ASTM E1340 | Standard Guide for Rapid Prototyping of Computerized Systems | Prototyping and validation methodology |
| Uganda Data Protection and Privacy Act 2019 | Data protection compliance for GPS, financial, and personal data |
| EU Deforestation Regulation (EUDR) 2023/1115 | Traceability and deforestation-free commodity certification |
| Uganda Employment Act 2006 | Labour law compliance for farm worker management |
| OWASP Top 10 (2021) | Web application security risks |

## 1.5 Overview

This SRS is organised into the following sections:

- **Section 1 (Introduction):** States the purpose, scope, definitions, references, and document organisation
- **Section 2 (Overall Description):** Describes product perspective, functions, user characteristics, constraints, and assumptions
- **Section 3 (Specific Requirements — Functional):** Specifies all functional requirements organised by module, using stimulus-response format with verifiability test cases
- **Section 4 (Specific Requirements — Non-Functional):** Specifies performance, availability, security, data integrity, usability, scalability, and accessibility requirements with measurable thresholds
- **Section 5 (External Interfaces):** Details user, hardware, software, and communication interfaces
- **Section 6 (Appendices):** Contains glossary reference, standards traceability matrix, and phase-feature matrix

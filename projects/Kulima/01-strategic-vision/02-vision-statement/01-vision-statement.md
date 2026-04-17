---
title: "Kulima — Vision Statement"
date: 2026-04-04
version: "1.0"
author: "Peter Bamuhigire"
standard: "IEEE 29148-2018 Sec 6.2"
---

# Vision Statement for the Kulima Farm Management Information System

## 1 Elevator Pitch

Kulima is a multi-tenant Farm Management Information System (FMIS) that provides Ugandan farmers — from 2-acre smallholders to 200-acre commercial estates — with a single offline-capable platform for crop management, livestock management, financial records, IoT sensor integration, CCTV surveillance, GPS animal tracking, supply chain traceability, and AI-powered farm advisory. The system replaces fragmented paper notebooks, Excel spreadsheets, and narrow single-purpose tools with one integrated mobile and web application built for African farming realities: low-spec Android phones, mobile money payments, and intermittent internet connectivity.

## 2 Product Positioning Statement

For individual farmers, farm businesses, cooperatives, and investors who need an affordable, offline-capable system to manage crops, livestock, finances, workers, and supply chain traceability on African farms, **Kulima** is a multi-tenant SaaS Farm Management Information System that provides integrated crop-to-market management with IoT monitoring, AI advisory, and EU Deforestation Regulation (EUDR) compliance in a single platform. Unlike Farmbrite (USD 49-179/month, no offline mode, no mobile money), Shambapro (data deletion on inactivity), Jaguza (IoT hardware only, no farm management), and FarmTrace (traceability only), Kulima combines all farm management domains in one application designed for low-spec Android devices, offline-first operation, and mobile money integration at a price point starting from free (individual farmers) to UGX 40,000/month.

## 3 Value Propositions

### 3.1 Replace Paper Records with Verifiable Digital Farm Data

Kulima eliminates paper-based record-keeping that is vulnerable to physical damage and prevents financial analysis. Farmers shall maintain digital records of crop seasons, livestock events, and financial transactions that persist across device replacements and generate bank-ready loan application reports.

**Measurable outcome:** Farmers produce standardised financial reports accepted by Savings and Credit Cooperative Organisations (SACCOs), Microfinance Institutions (MFIs), and commercial banks for loan risk assessment, reducing loan application preparation time from 3 days (manual compilation) to under 10 minutes.

### 3.2 Enable Offline-First Operation on Low-Spec Devices

The system shall function at full capacity with zero internet connectivity on Android devices with 2 GB RAM and 32 GB storage. All core operations — recording activities, viewing dashboards, managing livestock — execute locally with background synchronisation when connectivity resumes.

**Measurable outcome:** 100% of core Create, Read, Update, and Delete (CRUD) operations complete successfully with no internet connection, synchronising queued changes within 60 seconds of connectivity restoration.

### 3.3 Consolidate Multi-Farm Visibility for Directors and Investors

Farm directors and investors shall access a consolidated dashboard displaying financial performance, IoT health alerts, harvest forecasts, and approval workflows across their entire farm portfolio through the Director Platform.

**Measurable outcome:** Directors view consolidated Profit and Loss (P&L) statements across all invested farms within 5 seconds of dashboard load, replacing unverifiable WhatsApp summaries with auditable, system-generated financial data.

### 3.4 Deliver EUDR-Compliant Supply Chain Traceability

Cooperatives and export-oriented farms shall generate Due Diligence Statements (DDS) with GPS polygon verification, deforestation baseline checks, input history, and chain of custody documentation — all accessible to buyers via QR code scan.

**Measurable outcome:** Cooperatives generate EUDR-compliant traceability reports for 100% of export batches, with each batch linked to verified GPS farm boundaries, input records, and a complete chain of custody from farm origin to buyer delivery.

### 3.5 Provide AI-Powered Pest and Disease Identification

The system shall use the Claude API to identify crop pests and livestock diseases from farmer-submitted photographs and deliver actionable treatment recommendations with escalation to registered veterinary officers and extension officers when the AI confidence score falls below the defined threshold.

**Measurable outcome:** AI pest/disease identification returns results within 15 seconds per image submission, with a minimum 80% identification accuracy validated against expert agronomist assessments during Phase 1 pilot. [CONTEXT-GAP: AI accuracy target not confirmed in context files — 80% is a provisional target pending stakeholder validation.]

## 4 Target Audience

| Segment | Role | Primary Goals | Technical Proficiency |
|---|---|---|---|
| Individual Farmer (Smallholder) | Farm owner-operator managing 1-10 acres | Digital records replacing paper, offline operation, local language interface, affordable pricing, crop and livestock activity tracking | Low — feature phone upgrade to low-spec Android (2 GB RAM), comfortable with MTN MoMo and WhatsApp |
| Farm Business / Company | Multi-farm enterprise with employed staff | Multi-user access with Role-Based Access Control (RBAC), double-entry accounting, staff and payroll management, professional investor and bank reports | Medium to High — smartphone and laptop users, comfortable with English |
| Cooperative / NGO / Programme | Programme manager overseeing 100-1,000+ member farmers | Member registration, bulk input distribution tracking, collection centre operations, quality grading, collective sales, mobile money payment distribution, EUDR compliance reporting | Medium — smartphone users, mixed literacy among field agents |
| Farm Director / Investor | Portfolio owner with investments in multiple managed farms | Consolidated multi-farm dashboard, financial summary across portfolio, approval workflows, IoT health alerts, harvest forecasts | Medium — smartphone users preferring simplified dashboards |
| Buyer / Off-taker | European or regional commodity purchaser | Verifiable traceability data via QR code, EUDR compliance proof, farm origin story, input history, certification verification | High — laptop and smartphone, web portal access |
| Farm Worker | Daily or permanent on-farm labourer | View assigned tasks, mark tasks complete, verify logged hours, receive wage payment via mobile money | Low to Medium — Android Go devices (16 GB storage), comfortable with MoMo |
| Banks / SACCOs / MFIs | Financial institution loan officers | Standardised farm financial data for loan risk assessment, farm asset records, production history, repayment capacity indicators | Medium to High — formal report consumers (PDF, Excel) |
| MAAIF / Government | Ministry of Agriculture, Animal Industry and Fisheries (MAAIF) officials and extension officers | Aggregate agricultural data for policy planning, extension service delivery channel, National Agricultural Advisory Services (NAADS) / Operation Wealth Creation (OWC) programme tracking | Medium — formal data sharing agreements, aggregate report consumers |

## 5 Success Criteria

| Criterion | Metric | Baseline | Target | Timeline |
|---|---|---|---|---|
| Paying farmer acquisition | Number of individual and business tenants with active paid subscriptions | 0 | 100 paying farmers | 6 months from development start (Phase 1) |
| Monthly Recurring Revenue (Phase 1) | UGX collected per month from subscriptions | UGX 0 | UGX 4,000,000/month | Phase 1 completion |
| Monthly Recurring Revenue (Phase 4) | UGX collected per month from all revenue streams | UGX 0 | UGX 150,000,000/month | Phase 4 completion |
| Offline operation reliability | Percentage of core CRUD operations completing successfully with zero internet | N/A (no existing system) | 100% | Phase 1 MVP launch |
| Crop lifecycle tracking | Percentage of crop lifecycle stages (plan, plant, activity, harvest) tracked digitally | 0% (paper-based) | 100% operational for all active crop seasons | Phase 1 MVP launch |
| Livestock individual tracking | Percentage of registered animals with complete individual records and herd management data | 0% (paper-based) | 100% operational for all registered animals | Phase 1 MVP launch |
| Bank-ready financial reports | Number of report templates accepted by partner financial institutions for loan applications | 0 | Minimum 1 standardised report format accepted by at least 1 partner bank or SACCO | Phase 1 MVP launch |
| Sync latency | Time to synchronise queued offline changes after connectivity restoration | N/A | 60 seconds or less for up to 500 queued operations | Phase 1 MVP launch |

## 6 Scope Boundaries

### 6.1 In Scope

| Item | Description |
|---|---|
| Crop management | Full crop season lifecycle: plot creation, planting, activities (spraying, weeding, fertilising), harvest recording, yield analysis per enterprise |
| Livestock management | Individual animal registration, herd management, health records, breeding records, production tracking (milk, eggs), vaccination scheduling |
| Financial records (Dual-Mode Accounting) | Simple Mode ("Money in", "Money out") for smallholders and Advanced Mode (double-entry with chart of accounts, journal entries, financial statements) for commercial farms |
| Worker management | Staff profiles with National Identification Number (NIN), task assignment, attendance tracking, payroll with Pay As You Earn (PAYE) and National Social Security Fund (NSSF) deductions, mobile money wage disbursement |
| IoT integration | Jaguza ear tag device data ingestion via API, GPS collar tracking with geofence alerts, soil sensor and weather station data display |
| CCTV surveillance | IP camera integration via Real-Time Streaming Protocol (RTSP) to HTTP Live Streaming (HLS) proxy, live view in web and mobile apps, motion alerts |
| GPS and GIS | Farm boundary mapping via GeoJSON polygons, plot subdivision, satellite imagery integration (Sentinel-2 Normalised Difference Vegetation Index), animal location tracking |
| Supply chain traceability | Batch creation, collection centre operations (weighing, quality grading), chain of custody documentation, QR code generation, EUDR DDS report generation |
| AI farm advisor | Claude API integration for pest/disease photo identification, natural language farm advisory, escalation to registered veterinary and extension officers |
| Mobile apps | Native Android (Kotlin, Jetpack Compose, Room with SQLCipher) and iOS (Swift, SwiftUI, SwiftData) applications |
| Web application | Multi-tenant SaaS web application on the Chwezi Core framework (PHP/MySQL) |
| Director Platform | Consolidated multi-farm dashboard for directors and investors with approval workflows |
| Multi-language support | English, French, Portuguese, Luganda, Swahili, Kinyarwanda at launch |
| Mobile money integration | MTN MoMo for subscription payments, worker wages, and marketplace transactions |
| Agro-dealer directory and marketplace | Directory listing for input suppliers, input voucher redemption tracking |
| Veterinary and extension officer directory | Professional directory with AI advisor escalation referrals |
| Cooperative (Franchise) management | Member farmer registration, bulk input distribution, collection centres, collective sales, automated payment distribution |
| Offline-first architecture | All core operations function without internet; background sync on connectivity restoration |

### 6.2 Out of Scope

| Item | Rationale |
|---|---|
| Hardware manufacturing | Kulima integrates with third-party IoT devices (Jaguza ear tags, GPS collars, IP cameras) but does not manufacture hardware |
| Drone imagery capture | Satellite imagery (Sentinel-2) provides sufficient vegetation health analysis; drone integration is deferred to a future phase |
| Commodity trading exchange | Kulima tracks farm-gate sales and cooperative collective sales but does not operate a commodity exchange or futures market |
| Crop insurance products | Financial module records transactions but does not underwrite or administer insurance policies; integration with insurance providers is deferred |
| Seed and input e-commerce fulfilment | The agro-dealer directory provides visibility and voucher tracking but does not handle logistics, warehousing, or delivery |
| Direct bank API integration | Phase 1-3 generate bank-ready PDF/Excel reports; direct API integration with banking systems is planned for Phase 4 |
| Aquaculture-specific modules | Fish pond management is represented as a plot type with basic activity tracking; specialised aquaculture features (water quality, feed conversion ratios) are deferred |
| USSD interface implementation | USSD is identified as a fallback channel for farmers without smartphones; implementation is deferred pending user research on demand [CONTEXT-GAP: USSD implementation timeline not specified in context files] |

## 7 Assumptions and Risks

### 7.1 Assumptions

1. Target smallholder farmers own or have access to an Android smartphone with minimum 2 GB RAM and 32 GB storage.
2. MTN MoMo remains the dominant digital payment method in Uganda and supports the API integrations required for subscription billing and wage disbursement.
3. Jaguza provides a stable, documented API for ear tag device data ingestion and agrees to commercial partnership terms.
4. The Chwezi Core framework (shared with Academia Pro and Medic8) provides production-ready authentication, RBAC, billing, notifications, audit, and Director Platform infrastructure.
5. The Claude API remains commercially available and provides vision capabilities sufficient for pest/disease photo identification at the required accuracy level.
6. Sentinel-2 satellite imagery remains freely available for NDVI crop health analysis.
7. Ugandan internet penetration continues to grow, but offline-first architecture remains necessary for rural areas through at least 2028.
8. EUDR enforcement timelines proceed as legislated, sustaining demand for digital traceability among export cooperatives.

### 7.2 Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Low smartphone penetration among target smallholders limits adoption | Medium | High | Design for lowest-spec Android devices (2 GB RAM); investigate USSD fallback channel; partner with device financing programmes |
| Jaguza API instability or partnership failure | Medium | Medium | Abstract IoT integration behind a device-agnostic adapter layer; support alternative sensor providers |
| MTN MoMo API changes or downtime disrupts payments | Low | High | Implement payment retry queues; support Airtel Money as secondary provider; maintain manual payment recording |
| Claude API pricing increases make AI advisory uneconomical | Medium | Medium | Cache common pest/disease identifications locally; implement usage quotas per tenant tier; evaluate alternative AI providers |
| EUDR regulation delayed or amended, reducing urgency for traceability features | Low | Medium | Traceability module serves domestic market transparency and buyer confidence regardless of EUDR status |
| Competing FMIS enters the Ugandan market with similar offline-first capabilities | Medium | Medium | First-mover advantage in Uganda-specific feature set (mobile money, local languages, Jaguza integration); maintain rapid iteration cycle |
| Farm data privacy concerns under Uganda Data Protection and Privacy Act 2019 | Medium | High | Implement consent management for GPS collection; encrypt local databases with SQLCipher; conduct Data Protection Impact Assessment before launch |
| Solo development team creates single point of failure for delivery timeline | High | High | Leverage Chwezi Core shared infrastructure to reduce custom development; prioritise Phase 1 MVP scope ruthlessly; document architecture for future team onboarding |

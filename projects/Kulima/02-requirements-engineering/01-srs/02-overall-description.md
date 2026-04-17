# 2 Overall Description

## 2.1 Product Perspective

Kulima is a vertical application built on the Chwezi Core platform — a custom PHP 8.2/MySQL 8.x multi-tenant SaaS framework that provides shared infrastructure for authentication, RBAC, billing, notifications, audit logging, and the director platform. Kulima shares this foundation with two sibling products: Academia Pro (school management) and Medic8 (healthcare management). Each vertical extends Chwezi Core with domain-specific modules while inheriting common capabilities.

**System context:**

Kulima operates as a three-tier architecture:

1. **Backend tier:** PHP 8.2 REST API on Apache/Nginx (Ubuntu), MySQL 8.x database, S3-compatible object storage for photos and documents
2. **Web client tier:** Bootstrap 5/Tabler admin dashboard accessed via modern browsers
3. **Mobile client tier:** Native Android (Kotlin/Jetpack Compose) and iOS (Swift/SwiftUI) apps with offline-first architecture using Room (SQLCipher) and SwiftData respectively

**External system relationships:**

- Open-Meteo API provides weather forecast data
- Africa's Talking provides SMS and USSD services
- MTN MoMo API and Airtel Money API process mobile money payments
- Firebase Cloud Messaging delivers push notifications
- Google Maps SDK and OpenStreetMap provide mapping and satellite imagery
- Sentinel-2 via Google Earth Engine provides NDVI crop health imagery
- Jaguza API provides IoT livestock monitoring data via OAuth integration
- Claude API (Anthropic) provides AI pest/disease identification and farm advisory
- Hik-Connect, Dahua DMSS, Reolink APIs provide camera integration
- mediamtx/ffmpeg provides RTSP-to-HLS stream conversion

**Relationship to sibling products:**

- Academia Pro, Medic8, and Kulima share the Chwezi Core codebase for tenant management, authentication, RBAC, billing, and director platform infrastructure
- A single director can oversee farms (Kulima), schools (Academia Pro), and clinics (Medic8) from one consolidated director interface
- Each product maintains its own domain-specific database schema extensions and API endpoints

## 2.2 Product Functions

Kulima provides the following high-level modules, grouped by deployment phase:

**Phase 1 — MVP (Core Modules):**

- **Farm and Plot Management:** Register farms with GPS coordinates, subdivide into plots/paddocks (25+ types), record soil data, irrigation, and land tenure. Uganda administrative hierarchy (District, Sub-County, Parish, Village)
- **Crop Management:** 200+ crop library with local names, variety tracking, season planning, planting records, 20+ activity types, input tracking, crop health monitoring with photo upload, harvest records, yield analysis, crop rotation planner
- **Livestock Management:** Individual animal tracking for 12+ species, breed-specific benchmarks, health events (vaccination, treatment, deworming), reproduction, production records (milk, eggs, honey), feeding, movement, sales, mortality, herd/flock dashboards
- **Financial Records (Simple Mode):** Income/expense recording, activity-expense linking, budgets, enterprise profitability, cash flow, market prices, loan tracking, receipt upload, PDF/Excel export, invoice generation, mobile money payment tracking
- **Task and Worker Management:** Task CRUD with plot and worker assignment, mobile task completion, daily work log, worker profiles, payroll calculation, calendar view, recurring tasks, Kanban board
- **Weather and Advisory:** Farm-specific forecasts, real-time weather, weather alerts, historical data, climate-smart advisory, frost alerts, irrigation scheduling
- **Authentication and Tenancy:** Dual auth (session + JWT), RBAC (Owner, Manager, Worker), multi-tenant isolation, subscription tier enforcement
- **Offline-First Android App:** Room database, queue-based sync, conflict resolution, compressed photo sync, pre-loaded reference data
- **Web Dashboard:** Full CRUD for all modules, farm overview dashboard
- **Notifications:** SMS (Africa's Talking), push (FCM), in-app alerts

**Phase 2 — Growth:**

- **GPS Polygon Mapping:** Farm/plot boundary mapping via Google Maps SDK with GeoJSON storage
- **NDVI Satellite Analysis:** Sentinel-2 crop health imagery with colour-coded overlays
- **Inventory Management:** Input/equipment/produce inventory, stock receipts, automatic deduction, expiry and low-stock alerts, maintenance scheduling, post-harvest loss tracking
- **Supply Chain Traceability:** Batch creation, chain of custody, QR codes, GeoJSON export, EUDR DDS generation, buyer portal, certification tracking
- **Marketplace:** Produce/livestock listings, buyer search, market price database, directories, order management
- **Cooperative Module:** Member registration, farm mapping, input distribution, collection centres, quality grading, bulk mobile money payment, aggregate reports, field agent app
- **Advanced Financial Records (Dual-Mode):** Double-entry accounting, chart of accounts, financial statements, bank reconciliation, tax computation
- **iOS App:** SwiftUI with same offline-first architecture
- **Additional Languages:** French, Portuguese, Kinyarwanda

**Phase 3 — IoT and Surveillance (Add-on Modules):**

- **Jaguza IoT Integration:** Device management, 10-minute polling, webhook alerts, animal health dashboard, heat detection, disease early warning
- **GPS Animal Tracking:** Tracker registration, live map, geofence creation, breach alerts (2-minute SLA), historical playback, speed/theft detection
- **Camera Surveillance:** Camera registration (Hikvision/Dahua/Reolink/ONVIF), RTSP-to-HLS proxy, live viewing, multi-camera grid, PTZ control, motion alerts
- **AI Farm Advisor:** Natural language Q&A, photo diagnosis (Claude Vision), personalised recommendations, seasonal planning, market timing, offline fallback
- **Sensor Integration:** Soil moisture/temperature sensors, on-farm weather stations, drone imagery

**Phase 4 — Enterprise:**

- **Director Platform:** Consolidated multi-farm view, financial summary, health dashboard, harvest forecast, approval workflows, inter-farm transfers
- **Multi-Country Expansion:** Kenya, Tanzania, Rwanda configuration
- **EUDR DDS Automation:** Automated submission to EU TRACES system
- **White-Label:** Custom branding for agribusinesses
- **Bank and Insurance API:** Direct loan application and insurance integration
- **USSD/SMS Fallback:** Feature phone transaction recording
- **WhatsApp Business API:** Alert delivery and marketplace communication

## 2.3 User Characteristics

| User Type | Education Level | Technical Experience | Domain Expertise | Primary Device | Language Preference |
|---|---|---|---|---|---|
| Smallholder Farmer | Primary (P.7) to Secondary (S.4) | Low — comfortable with MoMo and WhatsApp only | High — lifelong farming experience | Low-spec Android (Tecno Spark, 2GB RAM) | Luganda, Swahili, or local language |
| Commercial Farmer | University-educated | High — uses laptop, smartphone, Excel | High — professional agriculture | iPhone or high-end Android, laptop | English |
| Farm Worker | Secondary (S.4) or below | Low-Medium — basic smartphone use | Medium — task-specific farming skills | Entry-level Android (Itel A18, Android Go) | Luganda, Swahili, or English |
| Cooperative Manager | Diploma or university | Medium — smartphone, basic office apps | High — programme management, agribusiness | Mid-range Android (Samsung A14) | English, local language |
| Farm Director / Investor | University-educated | Medium — prefers dashboards, not detailed screens | Medium — business management, not hands-on farming | iPhone, laptop | English |
| Buyer / Off-taker | University-educated | High — web browser, PDF tools | High — commodity trading, compliance | Laptop, smartphone | English, European languages |
| Field Agent | Secondary or diploma | Medium — uses mobile apps daily | Medium — trained in data collection | Mid-range Android | English, local language |

## 2.4 Constraints

### 2.4.1 Regulatory Constraints

- **Uganda Data Protection and Privacy Act 2019:** The system shall obtain explicit consent before collecting GPS location data and shall enforce data retention policies configurable per tenant
- **EU Deforestation Regulation (EUDR) 2023/1115:** The traceability module shall generate a DDS that includes farm GPS polygon, crop type, harvest date, and deforestation check result against the 31 December 2020 baseline
- **Uganda Employment Act 2006:** The worker management module shall support NSSF and PAYE deductions for permanent staff and shall record worker NIN for payroll compliance
- **UCDA Regulations:** The coffee traceability module shall support UCDA farmer registration numbers
- **NAADS/OWC Programme Rules:** The cooperative module shall track government input distribution compliance

### 2.4.2 Hardware Constraints

- **Target Android devices:** Minimum 2GB RAM, 16GB storage, Android 10+ (Android Go edition supported). The app APK base size shall not exceed 30MB
- **Network conditions:** The system shall function fully offline and sync over 2G/3G connections with sync payloads not exceeding 1MB per batch
- **Photo upload:** Images shall be compressed to a maximum of 512KB before upload
- **GPS accuracy:** GPS polygon capture shall achieve accuracy within 5 metres of the actual boundary

### 2.4.3 Technology Constraints

- **Chwezi Core framework:** All backend development shall use PHP 8.2+ with the Chwezi Core framework conventions (routing, ORM, middleware, RBAC)
- **MySQL 8.x:** All relational data shall be stored in MySQL; GeoJSON data shall use MySQL JSON columns with spatial indexing
- **No server-side video storage:** Camera streams shall be proxied (RTSP to HLS) in real time; the system shall not store video recordings
- **Single-codebase backend:** The REST API shall serve web, Android, and iOS clients from the same endpoints

### 2.4.4 Offline-First Constraint

- All core operations (create, read, update, delete for farms, crops, livestock, finances, tasks) shall execute locally without network connectivity
- The mobile app shall pre-load reference data (crop library, disease library, species, breeds, administrative hierarchy) during initial setup
- Write operations shall queue locally and sync automatically when connectivity is detected

## 2.5 Assumptions and Dependencies

### 2.5.1 Assumptions

- Target users own or have access to an Android smartphone with at least 2GB RAM and 16GB storage
- MTN MoMo and Airtel Money APIs remain available and maintain backward-compatible interfaces
- Open-Meteo continues to provide free weather forecast data without API key restrictions
- Google Maps SDK remains available for farm boundary mapping (with OpenStreetMap as fallback for offline use)
- Jaguza maintains their OAuth API for IoT device data retrieval
- Users have access to a mobile money account for subscription payments
- Uganda's two-season agricultural calendar (Season A: March-June, Season B: August-November) remains the standard cropping pattern
- Internet penetration in rural Uganda continues to improve, but 2G/3G remains the dominant connection type during the product lifecycle

### 2.5.2 Dependencies

| Dependency | Type | Impact if Unavailable |
|---|---|---|
| Open-Meteo API | External API | Weather forecasts and climate advisory unavailable; cached historical data still accessible |
| Africa's Talking | External API | SMS notifications and USSD fallback unavailable; push notifications and in-app alerts continue |
| MTN MoMo API | External API | Mobile money subscription payment and worker disbursement unavailable; manual payment recording continues |
| Airtel Money API | External API | Airtel Money payments unavailable; MTN MoMo remains primary channel |
| Firebase Cloud Messaging | External API | Push notifications unavailable; SMS and in-app alerts continue |
| Google Maps SDK | External API | Satellite imagery and map tiles unavailable; OpenStreetMap offline tiles serve as fallback |
| Sentinel-2 / Google Earth Engine | External API | NDVI crop health analysis unavailable; manual crop health recording continues |
| Jaguza API | External API (Phase 3) | IoT livestock data unavailable; manual animal health recording continues |
| Claude API (Anthropic) | External API (Phase 3) | AI advisor and photo pest/disease ID unavailable; offline pre-loaded guides serve as fallback |
| Hik-Connect / Dahua DMSS / Reolink | External API (Phase 3) | Cloud-managed camera features unavailable; direct RTSP/ONVIF connection remains functional |
| Global Forest Watch | External dataset | Deforestation baseline check unavailable; DDS generation proceeds with `[CONTEXT-GAP: deforestation check]` flag |
| Chwezi Core framework | Internal dependency | All backend functionality blocked; this is a hard dependency |
| MySQL 8.x | Infrastructure | All data persistence blocked; this is a hard dependency |

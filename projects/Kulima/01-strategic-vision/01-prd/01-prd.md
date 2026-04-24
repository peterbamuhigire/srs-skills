# Product Requirements Document: Kulima

| Field | Value |
|---|---|
| Project | Kulima |
| Version | 1.0 |
| Date | 2026-04-04 |
| Author | Peter Bamuhigire |
| Status | Draft |
| Standard | IEEE 29148-2018, IEEE 1233-1998 |

---

## 1 Executive Summary

Kulima is a multi-tenant Software-as-a-Service (SaaS) farm operating system designed to replace fragmented paper, spreadsheet, and WhatsApp-based management for Ugandan farms across the smallholder-to-commercial spectrum. The product focus is management usefulness first: whole-farm planning, crop and livestock operations, labour control, procurement, inventory, post-harvest handling, finance, sales, and compliance. Advanced intelligence and hardware integrations remain part of the roadmap, but they are positioned as add-ons that strengthen a management core rather than define it. Built on the Chwezi Core framework (PHP 8.2 / MySQL 8.x), Kulima operates offline-first on low-specification Android devices, integrates mobile money natively, and targets a 4-phase rollout beginning with a Uganda-focused MVP and expanding to East Africa, West Africa, and global markets.

## 2 Market Context

### 2.1 Problem Space

Ugandan farmers, especially commercial and growth-stage farms, lack an affordable, offline-capable, mobile-money-integrated system that connects planning, execution, control, and analysis in one application. Record-keeping remains predominantly paper-based or spreadsheet-based, which results in data loss, poor procurement control, weak labour accountability, limited stock visibility, delayed financial reporting, and exclusion from formal credit and premium buyer channels. Commercial farms often rely on fragmented spreadsheets managed by periodic accountant visits, preventing real-time operational visibility and making it difficult to manage the full loop from enterprise plan to harvest to sale.

### 2.2 Target Market Segments

| Segment | Size Indicator | Primary Need |
|---|---|---|
| Individual smallholder farmers | 2-50 acres, Uganda-first | Affordable digital records, offline-capable, local language |
| Farm businesses / companies | 50-500+ acres, multi-staff | Multi-user access, formal accounting, investor reporting |
| Cooperatives / NGOs / programmes | 100-5,000+ member farmers | Member registration, collection management, bulk mobile money payments, EUDR compliance |
| Farm directors / investors | Portfolio of 2+ farms | Consolidated multi-farm dashboard, approval workflows |
| Buyers / off-takers | European and regional importers | Verifiable traceability, EUDR Due Diligence Statement (DDS) |
| Banks / SACCOs / MFIs | Lending institutions | Standardised farm financial data for loan risk assessment |

### 2.3 Competitive Landscape

| Competitor | Pricing | Strengths | Weaknesses |
|---|---|---|---|
| Farmbrite | $49-179/month | Comprehensive features, established | Expensive for African farmers, no offline mode, no mobile money |
| Shambapro | Freemium | East Africa focus | Deletes data on inactivity, limited feature set |
| Jaguza | Hardware-bundled | IoT ear tags, disease detection | IoT-only, no crop management, no financial records |
| iKnowFarm | [COST-TBD] | Advisory focus | Narrow scope, no integrated farm management |
| FarmTrace | [COST-TBD] | Supply chain traceability | Traceability-only, no operational farm management |

Kulima differentiates by combining whole-farm planning, crop and livestock operations, labour control, procurement, finance, commercial execution, traceability, and optional intelligence in one platform at price points starting from a free tier to UGX 40,000/month, with offline-first architecture and native mobile money integration.

## 3 Product Objectives

Each objective derives from a business goal stated in the project vision and follows the SMART framework.

| ID | Objective | Metric | Target | Timeline |
|---|---|---|---|---|
| OBJ-01 | Replace fragmented paper, spreadsheet, and WhatsApp-based farm records with a digital system that functions offline on low-spec mobile devices | Number of paying farmers on the platform | 100 paying farmers | Within 6 months of development start |
| OBJ-02 | Give commercial farms and cooperatives a usable whole-farm planning and enterprise budget workflow | Percentage of pilot commercial tenants maintaining monthly budget vs actuals | 70% of pilot commercial tenants | Within 3 months of pilot onboarding |
| OBJ-03 | Provide commercial farms and cooperatives with bank-ready and buyer-ready reporting generated from live farm records | Reports accepted by at least 2 lending or buyer stakeholders | [METRIC-TBD] acceptance rate | Phase 2 completion |
| OBJ-04 | Reduce commercial leakage through procurement, stock, and post-harvest controls | Unexplained stock variance on pilot commercial farms | < 5% variance | Phase 2 completion |
| OBJ-05 | Enable AI-powered pest/disease identification and personalised farm advisory as optional add-ons to a proven management core | Number of active AI-enabled tenants and diagnosis accuracy | [METRIC-TBD] | Phase 3 completion |
| OBJ-06 | Achieve UGX 4M Monthly Recurring Revenue (MRR) in Phase 1, scaling to UGX 150M MRR by Phase 4 | MRR in UGX | Phase 1: UGX 4M, Phase 2: UGX 20M, Phase 3: UGX 60M, Phase 4: UGX 150M | Phase 1: Month 6, Phase 4: [METRIC-TBD] end date |

## 4 Target Users and Personas

### 4.1 Nakato Grace (Smallholder Farmer)

- **Role:** Individual farmer, 3 acres, Mbarara
- **Key characteristics:** 38 years old, P.7 education, widow, grows matooke and beans, keeps 5 Ankole cattle and 30 kienyeji chickens
- **Goals:** Digital records for SACCO loan application, vaccination scheduling, enterprise profitability tracking
- **Pain points:** Lost 6 months of paper records to water damage, cannot calculate profit per enterprise, missed vaccination dates causing calf mortality
- **Usage frequency:** Daily (evening recording sessions)
- **Technical proficiency:** Low -- Tecno Spark (2GB RAM, 32GB), comfortable with MTN MoMo and WhatsApp, prefers Luganda interface
- **Critical design requirement:** Offline-capable, large touch targets for dim-light usage, 3-tap-or-fewer core operations

### 4.2 Mugisha Robert (Commercial Farmer)

- **Role:** Farm business owner, 200-acre coffee estate (Kasese) and 50-acre cattle ranch (Mbarara), 15 permanent + 30+ seasonal staff
- **Key characteristics:** 52 years old, university-educated, manages from Kampala
- **Goals:** Professional financial reporting for Centenary Bank, input cost optimisation per acre, remote worker and payroll management, CCTV surveillance on both farms
- **Pain points:** Monthly accountant visits prevent real-time visibility, unverified worker hours, no remote monitoring capability
- **Usage frequency:** Daily (morning dashboard review), fortnightly farm visits
- **Technical proficiency:** High -- iPhone 15, laptop, English

### 4.3 Apio Sarah (Cooperative Programme Manager)

- **Role:** Programme manager, Acholi Organic Coffee Cooperative (Gulu), 320 member farmers across 4 sub-counties
- **Key characteristics:** 45 years old, NGO-funded digitisation mandate
- **Goals:** Register all members with GPS boundaries, track input distribution, manage collection centres, automate member payments via mobile money, generate EUDR compliance reports
- **Pain points:** Paper registers, 3-day manual payment calculations, no input distribution verification, European buyer demanding digital EUDR traceability
- **Usage frequency:** Daily (office), intensive during biannual harvest season
- **Technical proficiency:** Medium -- Samsung A14 (Android), English and Acholi; field agents have mixed smartphone literacy

### 4.4 Katumba James (Farm Director / Investor)

- **Role:** Director, portfolio of 3 farms (dairy in Entebbe, poultry in Mukono, vanilla in Bundibugyo)
- **Key characteristics:** 60 years old, retired banker
- **Goals:** Consolidated financial performance across all investments, purchase approval workflows (above UGX 5M), automated alerts for disease outbreaks, security breaches, and budget overruns
- **Pain points:** Non-standardised WhatsApp summaries from farm managers, no way to verify reported numbers, suspected expense inflation
- **Usage frequency:** Daily (5-minute dashboard check), quarterly farm visits
- **Technical proficiency:** Medium -- iPhone, English, prefers simple dashboards

### 4.5 Ocan David (Farm Worker)

- **Role:** Casual worker, coffee estate in Kasese, daily wage UGX 15,000 via MTN MoMo
- **Key characteristics:** 24 years old, S.4 education
- **Goals:** View daily task assignments, mark tasks complete, verify hours logged accurately, receive timely wage payment
- **Pain points:** Supervisor forgets to record hours causing lost pay, verbal task instructions forgotten
- **Usage frequency:** Daily (task check-in morning, task completion throughout day, hours verification evening)
- **Technical proficiency:** Low-Medium -- Itel A18 (Android Go, 16GB), comfortable with MoMo, prefers Luganda or English

### 4.6 Van der Berg Hans (European Coffee Buyer)

- **Role:** Specialty coffee buyer, German roasting company, sources from Kasese and Luwero
- **Key characteristics:** 48 years old, EUDR compliance deadline pressure
- **Goals:** Verify deforestation-free compliance via QR code scan, access farm origin story and input history per batch, verify certifications (organic, RainForest Alliance)
- **Pain points:** Paper certificates, expensive auditing, no digital traceability system
- **Usage frequency:** Per-shipment (scan QR code, review buyer portal, download EUDR DDS report)
- **Technical proficiency:** High -- laptop and smartphone, English and German

## 5 Feature Priority Matrix

### 5.1 Phase 1 -- MVP (Core Modules)

| Feature | Description | Priority | Effort | Value | MoSCoW | Rationale |
|---|---|---|---|---|---|---|
| Whole-Farm Planning and Performance Management | Annual and seasonal farm plans, enterprise selection, target yields, resource allocation, enterprise budgets, KPI tracking, and management review workspace | Critical | M | High | Must | Commercial farms need a planning and control layer before advanced add-ons become useful |
| Farm and Plot Management | Farm registration, land mapping, plot subdivision, 25+ plot types, Uganda administrative hierarchy, land tenure recording, acre/hectare conversion | Critical | L | High | Must | Foundation module; all other modules depend on farm and plot entities |
| Crop Management | Full crop lifecycle (plan-plant-activity-harvest), 200+ crop library with local names, variety tracking, season planning, activity logging (20+ types), input tracking, health monitoring with photo upload, harvest records with quality grading, yield analysis, crop rotation planner, MAAIF crop calendar, Uganda cash crop pre-configuration, pest/disease alerts | Critical | XL | High | Must | Core value proposition for crop farmers; largest user segment |
| Livestock Management | Individual animal tracking and herd/flock management for 12+ species, breed tracking with benchmarks, health events (vaccination, treatment, deworming), reproductive events, production records (milk, eggs, honey), feeding records, movement log, sales/mortality, herd summary dashboard, Uganda-specific breed metrics and disease library | Critical | XL | High | Must | Core value proposition for livestock farmers; combined crop+livestock differentiates from competitors |
| Basic Financial Records | Income/expense recording with categories, expense-to-activity linking, budget planning, budget vs actuals, profitability per enterprise, cash flow summary, market price recording, loan tracking, input cost auto-calculation, receipt photo upload, PDF/Excel export, invoice generation, mobile money payment tracking, SACCO loan formats, multi-currency support, bank loan credibility report | Critical | L | High | Must | Enables loan applications; direct revenue impact for farmers |
| Procurement and Supplier Controls | Supplier register, purchase requests, approvals, purchase orders, receipt capture, category discipline, and requested vs received vs paid visibility | Critical | M | High | Must | Commercial usefulness depends on controlling leakage and purchase flow, not only recording expenses after the fact |
| Task and Worker Management | Task creation with plot/worker assignment, mobile task completion, daily work log, worker profiles with payment details, payroll calculation/export, calendar view, recurring tasks, Kanban board, activity planner with reminders, casual worker mobile money payment, NSSF/PAYE for permanent staff | Critical | L | High | Must | Addresses verified worker hours pain point; operational efficiency |
| Sales, Post-Harvest, and Customer Management | Produce allocation, customer records, invoices, delivery scheduling, contract tracking, basic receivables, and dispatch readiness from available stock | Critical | M | High | Must | Commercial farms need visibility from harvest to cash collection, not only production records |
| Weather, Climate, and Advisory | Farm-specific weather forecast (3-day free, 8-day paid), real-time weather per farm GPS, weather alerts (SMS/push), historical data, climate-smart advisory, frost alerts, irrigation scheduling, Uganda Met Authority integration, agro-ecological zone awareness, El Nino/La Nina alerts | High | M | High | Must | Low-effort, high-value feature; differentiator for smallholders |
| User Roles and Authentication | Dual-auth (session + JWT), RBAC (Farm Owner, Farm Manager, Worker), multi-tenant isolation, subscription tier enforcement at API level | Critical | M | High | Must | Security and multi-tenancy foundation; required for all user types |
| Notifications | SMS via Africa's Talking, push via Firebase Cloud Messaging; types: weather alerts, task reminders, low stock alerts, expiry alerts, payment confirmations | High | M | Medium | Must | Engagement driver; critical for time-sensitive alerts (weather, tasks) |
| Offline-First Android App | Room database mirroring all farm data, queue-based background sync, conflict resolution (last-write-wins + conflict log), compressed photo sync, pre-loaded reference data (crop library, disease library, species, admin hierarchy), low bandwidth auto-detection | Critical | XL | High | Must | Non-negotiable for target market; most farmers have intermittent or no connectivity |
| Web Dashboard | Bootstrap 5/Tabler admin panel, full CRUD for all modules, dashboard with farm overview, crop status, livestock summary, financial summary, task calendar | High | L | High | Must | Primary interface for commercial farmers and cooperative managers |
| Mobile Money Subscription Payment | MTN MoMo and Airtel Money for subscription payments from within the app, annual discount (pay 10, get 12) | Critical | M | High | Must | Revenue collection mechanism; farmers do not have credit/debit cards |
| Multi-lingual (Phase 1 subset) | English, Luganda, Swahili | High | S | Medium | Must | Accessibility for Nakato Grace persona; expands addressable market |

### 5.2 Phase 2 -- Growth

| Feature | Description | Priority | Effort | Value | MoSCoW | Rationale |
|---|---|---|---|---|---|---|
| GPS Polygon Farm/Plot Boundary Mapping | Google Maps SDK boundary drawing by walking perimeter or satellite imagery, GeoJSON storage, plot subdivision with labelled geo-polygons, farm overview map with colour-coded plots | High | L | High | Should | Required for EUDR compliance and cooperative member mapping |
| NDVI Satellite Crop Health Analysis | Sentinel-2 free satellite imagery via Google Earth Engine API, crop health colour-coding on farm map | High | M | Medium | Should | Proactive crop health monitoring; uses free data source |
| Advanced Inventory, Packhouse, and Asset Operations | Stock receipts with lot control, automatic deduction, low stock and expiry alerts, chemical withholding windows, produce inventory by store, equipment maintenance, fuel log, asset utilisation, and post-harvest loss tracking | High | L | High | Should | Extends Phase 1 controls into full commercial operations and auditability |
| Supply Chain Traceability and Compliance | Batch creation, chain of custody, QR codes, GeoJSON export, buyer portal, certification tracking, deforestation checks, dispatch compliance gates, and EUDR DDS generation | High | XL | High | Should | Directly addresses export-market requirements and premium buyer trust |
| Marketplace and Commercial Execution | Produce and livestock listings, buyer search, market price database, price alerts, order management, sales contracts, delivery scheduling, customer account management, and cooperative bulk sales support | High | XL | Medium | Should | Extends production visibility into repeatable market execution and cash collection |
| Cooperative Module | Cooperative as single franchise tenant with multiple member farms, member registration, GPS farm mapping via field agent app, bulk input distribution tracking, collection centre management (weigh, record, grade), quality grading, member payment calculation with mobile money bulk disbursement, aggregate supply reports, compliance monitoring, field agent app, farmer performance ranking, primary society to apex body hierarchy, NAADS/OWC structure, MTN/Airtel bulk payment APIs | High | XL | High | Should | High-value segment; single cooperative = hundreds of paying member accounts |
| Advanced Financial Records and Scenario Planning | Simple Mode ("Money in/out/owe/owed") default for all users; Advanced Mode: chart of accounts, double-entry journal, trial balance, income statement, balance sheet, cash flow, bank reconciliation, scenario planning, and capital investment evaluation | High | XL | High | Should | Serves both smallholder simplicity and commercial-farm management analysis requirements |
| iOS App | SwiftUI, SwiftData, same offline-first architecture as Android | High | XL | Medium | Should | Serves Mugisha Robert and Katumba James personas (iPhone users) |
| Remaining Languages | French, Portuguese, Kinyarwanda added to complete 6-language launch set | Medium | M | Medium | Should | Required for Kenya, Tanzania, Rwanda, DRC expansion |

### 5.3 Phase 3 -- IoT and Surveillance

| Feature | Description | Priority | Effort | Value | MoSCoW | Rationale |
|---|---|---|---|---|---|---|
| Jaguza IoT Integration (Add-on) | OAuth integration with Jaguza API, device management, 10-minute polling + real-time webhook alerts, animal detail page with Jaguza tab (activity graph, temperature trend, fertility index), herd health dashboard (green/amber/red), heat/fertility detection alerts, disease early warning, fertility calendar, milk yield correlation overlay, drone mission link | Medium | L | Medium | Could | Premium add-on revenue; partnership with existing IoT provider |
| GPS Animal Tracking (Add-on) | GPS tracker registration (IMEI + SIM), live map with moving animal icons, geofence creation and breach alerts (SMS + push + WhatsApp), overnight monitoring, historical playback (7/14/30 days), herd clustering, speed tracking for theft detection, multi-protocol support (MQTT, HTTP, TCP), vehicle tracking, theft investigation report, cattle rustling context (Karamoja, Teso), 2-minute alert SLA | Medium | XL | Medium | Could | Addresses cattle theft -- a material risk in pastoral regions |
| Live Farm Camera Surveillance (Add-on) | Camera registration (Hikvision/Dahua/Reolink/RTSP/ONVIF), RTSP proxy (mediamtx/ffmpeg) to HLS, single and multi-camera grid views, PTZ control, night mode, stream quality selector, zone-based motion detection alerts (push + SMS + WhatsApp with snapshot), alert scheduling, false alarm reduction, two-way audio, time-limited access sharing, low-bandwidth 360p mode, solar-powered camera support | Medium | XL | Medium | Could | Premium add-on; addresses Mugisha Robert remote monitoring need |
| AI Farm Advisor (Add-on) | Natural language farm Q&A using farm data context, photo-based pest/disease diagnosis (Claude Vision API), personalised recommendations, seasonal planning advisor, market timing advice, financial coaching, offline fallback (pre-loaded guides), extension officer escalation on low confidence, multi-lingual responses (6 languages) | Medium | L | High | Could | Differentiator; scales extension services beyond government capacity |
| Drone Imagery Integration | Connect drone survey results to farm map, aerial crop health monitoring, livestock headcount, fence inspection | Low | M | Low | Could | Niche use case; dependent on farmer owning or hiring drone services |
| Soil Sensor Integration | Soil moisture and temperature sensors reporting to Kulima, data on plot detail screen, informs irrigation decisions | Low | S | Low | Could | Limited sensor adoption in target market; future growth opportunity |
| On-Farm Weather Station Integration | Local weather station data (rainfall, temperature, wind) overrides API weather with actual local readings | Low | S | Low | Could | Supplements API weather; value limited to farms with weather stations |

### 5.4 Phase 4 -- Enterprise

| Feature | Description | Priority | Effort | Value | MoSCoW | Rationale |
|---|---|---|---|---|---|---|
| Director Platform | Consolidated farm overview across all owned/managed farms, financial summary, livestock health dashboard (all IoT alerts), crop status map with NDVI, harvest forecast, staff productivity, approval workflow (large purchases), inter-farm transfer, director mobile app | Medium | XL | High | Could | Serves Katumba James persona; high willingness-to-pay segment |
| Multi-Country Expansion | Kenya, Tanzania, Rwanda configuration: currency, crop library, admin hierarchy, regulatory context, language defaults | Medium | L | High | Could | Market expansion; Phase 4 revenue target depends on multi-country reach |
| EUDR DDS Automation | Automated submission of Due Diligence Statement to EU TRACES system | Medium | M | Medium | Could | Regulatory value; dependent on EU TRACES API availability |
| White-Label | Agribusinesses can white-label Kulima with their own branding | Low | M | Medium | Won't (Phase 4) | Revenue diversification; requires stable product first |
| Bank and Insurance API Integrations | Farm financial data as direct input to bank loan applications (Centenary, Equity), insurance eligibility check and premium calculation (UAP, Jubilee) | Medium | L | High | Could | Addresses financial inclusion goal; dependent on bank API readiness |
| USSD/SMS Fallback | USSD short code for basic transaction recording on feature phones, SMS commands to dedicated number | Low | M | Medium | Won't (Phase 4) | Extends reach to feature phone users; significant telco coordination overhead |
| WhatsApp Business API | Motion alerts, marketplace communication, notification delivery via WhatsApp | Low | S | Medium | Won't (Phase 4) | Supplementary channel; core notifications already covered by SMS and push |

## 6 Success Metrics

| KPI | Baseline | Target | Measurement Method | Timeline |
|---|---|---|---|---|
| Monthly Recurring Revenue (MRR) | UGX 0 | Phase 1: UGX 4M, Phase 2: UGX 20M, Phase 3: UGX 60M, Phase 4: UGX 150M | Subscription payment records in billing system | Phase 1: Month 6, Phase 2: Month 12, Phase 3: Month 18, Phase 4: Month 24 [METRIC-TBD: confirm phase end dates] |
| Paying farmer count | 0 | Phase 1: 100, Phase 2: 500, Phase 3: 1,500, Phase 4: 5,000 [METRIC-TBD: confirm Phase 2-4 targets] | Active subscription count in tenant database | Aligned with MRR timeline |
| Commercial pilot budget adoption | 0 | 70% of pilot commercial farms maintain monthly budget vs actuals for 3 consecutive months | Budget records and month-end close activity logs | Phase 1 Month 3 onward |
| Enterprise gross margin coverage | 0 | 90% of active pilot enterprises have monthly gross margin reports | Enterprise profitability report generation log | Phase 1 Month 3 onward |
| Unexplained stock variance | [BASELINE-TBD] | < 5% on pilot commercial farms | Cycle count variance reports by item and location | Phase 2 completion |
| On-time critical task completion | [BASELINE-TBD] | >= 90% | Task due date vs completion timestamp analysis | Phase 1 launch onward |
| Offline sync success rate | [BASELINE-TBD] | 99.5% of queued records sync within 30 seconds of connectivity | Sync completion logs with timestamp delta analysis | Phase 1 launch onward |
| API response time (P95) | [BASELINE-TBD] | < 500ms for CRUD operations under 1,000 concurrent users | Server-side request duration logging at P95 percentile | Phase 1 launch onward |
| EUDR compliance reports generated | 0 | 50 EUDR DDS reports generated for export batches | Report generation audit log | Phase 2 completion |
| User retention (30-day) | [BASELINE-TBD] | 70% of registered farmers return within 30 days of first use [METRIC-TBD: confirm target] | Login event analysis: distinct users with activity in days 2-30 after registration | Phase 1 Month 3 onward |

## 7 Constraints and Dependencies

### 7.1 Budget Constraints

- Solo developer (Peter Bamuhigire) for all phases -- limits parallel workstream capacity
- No external funding secured; development funded from existing SaaS revenue (Academia Pro, Medic8)
- Infrastructure costs shared with Academia Pro and Medic8 on the same hosting environment
- [COST-TBD] -- Total development cost estimate per phase not yet established

### 7.2 Technology Constraints

- Backend framework fixed to Chwezi Core (PHP 8.2 / MySQL 8.x) for code reuse across the SaaS portfolio
- Android app must function on devices with 2GB RAM and 16GB storage (Android Go compatible)
- APK base size must remain below 30MB
- Sync payloads must remain below 1MB per batch to accommodate 2G connections
- Photo compression to 512KB maximum before upload

### 7.3 Regulatory Constraints

- Uganda Data Protection and Privacy Act (2019) -- personal farmer data handling, consent requirements, data localisation considerations
- European Union Deforestation Regulation (EUDR) -- supply chain traceability, GPS polygon export, deforestation-free verification against Global Forest Watch baseline, Due Diligence Statement generation
- Uganda Employment Act (2006) -- NSSF and PAYE computation for permanent farm workers
- Uganda National Identification and Registration Authority (NIRA) -- National Identification Number (NIN) recording for worker profiles

### 7.4 External Dependencies

| Dependency | Type | Risk Level | Mitigation |
|---|---|---|---|
| Jaguza API | IoT partner API (OAuth) | Medium | Phase 3 dependency; core product functions without IoT |
| MTN MoMo API | Payment integration | High | Primary revenue collection; Airtel Money as fallback |
| Airtel Money API | Payment integration | Medium | Secondary payment channel |
| Africa's Talking | SMS/USSD gateway | Medium | Alternative: Twilio (higher cost) |
| Firebase Cloud Messaging | Push notifications | Low | Google-maintained; stable service |
| Open-Meteo API | Weather data (free) | Low | Free tier; fallback to cached forecasts |
| Google Maps SDK | Mapping (web + mobile) | Low | OpenStreetMap/Mapbox as offline fallback |
| Sentinel-2 / Google Earth Engine | Satellite imagery (free) | Medium | Phase 2 dependency; NDVI is supplementary, not core |
| Claude API (Anthropic) | AI pest/disease diagnosis | Medium | Phase 3 add-on; offline fallback with pre-loaded guides |
| Hikvision/Dahua/Reolink APIs | Camera integration | Medium | Phase 3 add-on; generic RTSP/ONVIF as universal fallback |
| Flutterwave / Paystack | International payments | Low | Phase 4 dependency for non-Uganda markets |

## FR-AI: AI Farm Advisor — Intelligent Farming Add-On

> **Positioning:** The AI Farm Advisor is a paid add-on, off by default. Farmers and agribusinesses activate it when they are ready for the next level of intelligence. Every feature is described in terms that a smallholder farmer or cooperative manager will understand immediately.

> **Pricing (indicative):** Starter — UGX 30,000/month; Growth — UGX 100,000/month; Enterprise — UGX 300,000/month. All plans include a configurable monthly query budget. The system enforces the budget and alerts the account owner at 80% consumption.

---

### AI Feature 1: Ask Any Farming Question in Your Language

**Who benefits:** Individual farmers, extension officers, cooperative field staff.

**The problem it solves:** A smallholder farmer in Mbale wakes up and notices yellow patches on her maize. She does not know a doctor or an agronomist she can call. Google results are in English and assume laboratory-grade equipment. By the time she gets help, a third of the crop may be lost.

**What it does:** The farmer types or voice-inputs her question in English, Luganda, or Swahili and the system returns a plain-language answer with photos and step-by-step guidance, specifically calibrated for East African crops and conditions.

**Why farmers pay for it:** It replaces the need for an on-call extension officer for day-to-day questions. For a cooperative, it means 200 farmers get agronomic guidance simultaneously without hiring 200 extension workers.

**Pricing tier:** Starter and above.

**FR-AI-001** — see SRS Section 3, FR-AI-001 for full technical specification.

---

### AI Feature 2: Photograph a Sick Crop — Get an Instant Diagnosis

**Who benefits:** Individual farmers, cooperative field officers, farm managers.

**The problem it solves:** Pest and disease identification requires years of training. By the time a farmer identifies a problem and waits for an extension visit, a preventable outbreak has spread across the farm.

**What it does:** The farmer takes a photo of the affected leaf, stem, or fruit with their phone. Within 10 seconds, the system identifies the most likely cause — for example, "Banana Fusarium wilt — 91% confidence" — and recommends immediate action: isolate the affected stool, avoid irrigation spread, contact your cooperative.

**Why farmers pay for it:** Early detection prevents crop loss. A single prevented outbreak on a 2-acre banana farm is worth more than a year of subscription fees.

**Pricing tier:** Starter and above.

**FR-AI-002** — see SRS Section 3, FR-AI-002 for full technical specification.

---

### AI Feature 3: Get a Farm Plan Built for Your Specific Conditions

**Who benefits:** Farm managers, serious smallholders, agribusiness owners.

**The problem it solves:** Generic advice does not account for the farmer's specific soil type, elevation, rainfall pattern, available inputs, or crop history. Following generic advice on degraded soil produces generic — poor — results.

**What it does:** The system reads the farm's recorded soil data, historical yields, GPS location (weather zone), available budget for inputs, and target market, then produces a personalised growing plan: which variety to plant, how much input to apply, when to irrigate, what yield to target, and which diseases to watch for.

**Why farmers pay for it:** A plan built on real farm data produces measurable yield improvements. Cooperatives use it as a member benefit that justifies the subscription.

**Pricing tier:** Growth and above.

**FR-AI-003** — see SRS Section 3, FR-AI-003 for full technical specification.

---

### AI Feature 4: Know When to Plant — Not Just the Calendar Date

**Who benefits:** Farmers planning a new season, cooperative procurement officers.

**The problem it solves:** The official planting calendar says "plant in March." But this year, rains started three weeks late. Farmers who followed the calendar planted into dry soil and lost germination. Climate variability has made fixed calendars unreliable.

**What it does:** Two weeks before the typical planting window, the system generates a "Plant or Wait?" advisory based on current Open-Meteo forecast data and historical rainfall records for the farm's GPS zone. It tells the farmer the adjusted planting window based on actual rainfall conditions rather than the fixed calendar date.

**Why farmers pay for it:** A planting timing miss costs an entire season. Climate-adjusted advice is the most valuable agronomic guidance a farmer can receive.

**Pricing tier:** Growth and above.

**FR-AI-004** — see SRS Section 3, FR-AI-004 for full technical specification.

---

### AI Feature 5: Know When to Sell for the Best Price

**Who benefits:** Individual farmers, cooperative marketing officers, agribusiness traders.

**The problem it solves:** Smallholder farmers sell when they need cash, not when prices are highest. Traders exploit this by buying at harvest and holding until prices rise. Farmers leave 20–40% of potential revenue on the table every season.

**What it does:** Based on historical market price patterns for the farmer's crop and nearest market, the system predicts the optimal selling window. For example: "Maize prices at Jinja market typically peak in weeks 8–10 post-harvest. If you can store 10 bags, selling then vs. now would earn you an additional UGX 120,000." The farmer makes an informed choice.

**Why farmers pay for it:** A single optimal selling decision recovers the entire cost of the annual subscription. Cooperatives use it to coordinate bulk selling and negotiate higher prices.

**Pricing tier:** Growth and above.

**FR-AI-005** — see SRS Section 3, FR-AI-005 for full technical specification.

---

### AI Farm Advisor Packaging Summary

| Feature | Starter (UGX 30K/mo) | Growth (UGX 100K/mo) | Enterprise (UGX 300K/mo) |
|---|---|---|---|
| Natural Language Q&A | Yes | Yes | Yes |
| Photo Pest/Disease Diagnosis | Yes | Yes | Yes |
| Personalised Farm Plan | — | Yes | Yes |
| Seasonal Planting Advisory | — | Yes | Yes |
| Market Timing Advice | — | Yes | Yes |
| Offline Fallback Guides | Yes | Yes | Yes |

**All features are off by default within the purchased plan.** The account owner enables each feature individually from the AI Advisor settings screen.

## 8 Release Strategy

### 8.1 Phase 1 -- MVP (Core Modules)

- **Scope:** Whole-farm planning and performance management, farm and plot management, crop management, livestock management, basic financial records, procurement and supplier controls, task and worker management, sales/post-harvest/customer basics, weather and advisory, user roles and authentication, notifications, offline-first Android app, web dashboard, mobile money subscription payment, 3 languages (English, Luganda, Swahili)
- **Target:** 100 paying farmers, UGX 4M/month MRR
- **Market:** Uganda
- **Timeline:** 6 months from development start [METRIC-TBD: confirm start date]

### 8.2 Phase 2 -- Growth

- **Scope:** GPS polygon mapping, advanced inventory/packhouse/asset operations, supply chain traceability (EUDR), marketplace and commercial execution, cooperative module, advanced financial records and scenario planning, NDVI satellite analysis, iOS app, remaining 3 languages (French, Portuguese, Kinyarwanda)
- **Target:** UGX 20M/month MRR, 5 cooperatives onboarded
- **Market:** Uganda + Kenya, Tanzania, Rwanda (configuration only)
- **Timeline:** Months 7-12 [METRIC-TBD: confirm timeline]

### 8.3 Phase 3 -- IoT and Surveillance

- **Scope:** AI farm advisor (add-on), Jaguza IoT integration (add-on), GPS animal tracking (add-on), live farm camera surveillance (add-on), drone imagery integration, soil sensor integration, on-farm weather station integration
- **Target:** UGX 60M/month MRR
- **Market:** Uganda, Kenya, Tanzania, Rwanda
- **Timeline:** Months 13-18 [METRIC-TBD: confirm timeline]

### 8.4 Phase 4 -- Enterprise

- **Scope:** Director platform, multi-country expansion (Nigeria, Ghana, Zambia), EUDR DDS automation, white-label, bank and insurance API integrations, USSD/SMS fallback, WhatsApp Business API
- **Target:** UGX 150M/month MRR
- **Market:** Uganda, East Africa, West Africa, global
- **Timeline:** Months 19-24 [METRIC-TBD: confirm timeline]

## 9 Standards Traceability Appendix

| PRD Section | IEEE 29148-2018 Clause | IEEE 1233-1998 Clause | Notes |
|---|---|---|---|
| 1 Executive Summary | 5.2 (System overview) | 4.1 (Purpose) | High-level system description |
| 2 Market Context | 6.2.2 (Business environment) | 4.2 (Scope) | Problem space, market segments, competitive analysis |
| 3 Product Objectives | 6.2.1 (Business purpose) | 4.3 (Definitions, acronyms, abbreviations) | SMART objectives derived from business goals |
| 4 Target Users and Personas | 6.2.3 (Stakeholder identification) | 5.1 (Required states and modes) | Stakeholder-driven persona definitions |
| 5 Feature Priority Matrix | 6.4.1 (System requirements) | 5.2 (Requirements) | Prioritised feature inventory mapped to build phases |
| 6 Success Metrics | 6.2.4 (Success criteria) | 5.3 (Verification approach) | Measurable KPIs with baselines and targets |
| 7 Constraints and Dependencies | 6.5 (Design constraints), 6.6 (External interfaces) | 5.4 (Constraints) | Budget, technology, regulatory, and integration constraints |
| 8 Release Strategy | 6.2.5 (Release planning) | 6.0 (Implementation guidance) | 4-phase rollout with scope, targets, and timelines |
| 9 Standards Traceability | 6.1 (Traceability) | 3.0 (Standards conformance) | Clause-level mapping to governing standards |

# Feature List

## Phase 1 — MVP (Core Modules)

### Farm and Plot Management
Foundation module. Farmer registers farm(s), maps land, subdivides into plots/paddocks. Supports 25+ plot types (cropland, pasture, greenhouse, poultry house, fish pond, apiary, etc.). Uganda administrative hierarchy (District, Sub-County, Parish, Village). Land tenure type recording (customary, freehold, leasehold, mailo). Acre as primary unit with hectare/sq.m conversion.

### Crop Management
Full crop lifecycle from planning through harvest. Pre-loaded 200+ crop library with local names (Luganda, Swahili, Kinyarwanda). Variety/cultivar tracking with maturity periods and expected yields. Season planning, planting records, activity logging (20+ activity types), input tracking per activity, crop health monitoring with photo upload, harvest records with quality grading, yield analysis (actual vs planned), crop rotation planner. Uganda-specific: MAAIF crop calendar, key cash crops pre-configured (coffee, tea, vanilla, cocoa), matooke enterprise tracking, common pest/disease alerts (Fall Armyworm, Cassava Mosaic, BXW, Coffee Wilt).

### Livestock Management
Individual animal tracking and herd/flock management for any species (cattle, goats, sheep, pigs, chickens, ducks, turkeys, rabbits, donkeys, horses, bees, fish). Breed tracking with breed-specific benchmarks (Ankole vs Friesian). Individual records (tag, RFID, name, sex, DOB, pedigree). Health events (vaccination, treatment, deworming, dipping). Reproductive events (mating, pregnancy check, birth, weaning). Production records (milk, eggs, honey, wool, manure). Feeding records. Movement log. Sales and mortality records. Herd summary dashboard. Flock management for poultry. Uganda-specific: Ankole Longhorn metrics, kienyeji chicken benchmarks, NLIS/UIA tag format, East African disease library.

### Basic Financial Records
Farm income and expense recording with categories. Linking expenses to farm activities. Budget planning (season/year). Budget vs actuals comparison. Profitability per enterprise (crop season/livestock type). Cash flow summary with bar chart. Market price recording and history. Loan tracking (SACCO, MFI, mobile money). Input cost per unit auto-calculation. Receipt photo upload. PDF/Excel export for bank loan presentation. Invoice generation. Uganda-specific: mobile money payment tracking (MTN MoMo, Airtel Money), SACCO loan formats, credit for farming inputs, UGX primary currency with KES/TZS/RWF/NGN/GHS/ZMW support, bank loan credibility report.

### Task and Worker Management
Task creation with plot assignment, worker assignment, due dates, estimated hours. Task completion by workers on mobile. Daily work log. Worker profiles (name, phone, rate, NIN, bank/mobile money details). Payroll calculation and export. Calendar view. Recurring tasks. Kanban board (To Do / In Progress / Done). Activity planner with reminders. Uganda-specific: casual worker mobile money payment, NSSF and PAYE for permanent staff.

### Weather, Climate, and Advisory
Farm-specific weather forecast (3-day for free tier, 8-day for paid). Real-time weather for each farm GPS location. Weather alerts (SMS/push for extreme events). Historical weather data. Climate-smart advisory ("Ideal day to spray", "Delay planting"). Frost alerts for highland farms. Irrigation scheduling recommendations. Uganda-specific: Uganda Met Authority integration, agro-ecological zone awareness, El Nino/La Nina alerts.

### User Roles and Authentication
Dual-auth (session + JWT). RBAC: Farm Owner, Farm Manager, Worker. Multi-tenant isolation. Subscription tier enforcement at API level.

### Notifications
SMS via Africa's Talking. Push via Firebase Cloud Messaging. Notification types: weather alerts, task reminders, low stock alerts, expiry alerts, payment confirmations.

### Offline-First Android App
Room database mirroring all farm data. Queue-based background sync. Conflict resolution (last-write-wins + conflict log). Compressed photo sync. Pre-loaded reference data (crop library, disease library, species, admin hierarchy). Low bandwidth auto-detection.

### Web Dashboard
Bootstrap 5/Tabler admin panel. Full CRUD for all modules. Dashboard with farm overview, crop status, livestock summary, financial summary, task calendar.

### Mobile Money Subscription Payment
MTN MoMo and Airtel Money for subscription payments from within the app. Annual discount (pay 10, get 12).

### Multi-lingual (Phase 1 subset)
English, Luganda, Swahili.

## Phase 2 — Growth

### GPS Polygon Farm/Plot Boundary Mapping
Google Maps SDK for drawing boundaries by walking perimeter or drawing on satellite imagery. GeoJSON storage in MySQL JSON columns. Plot subdivision with labelled geo-polygons. Farm overview map with colour-coded plots.

### NDVI Satellite Crop Health Analysis
Sentinel-2 free satellite imagery via Google Earth Engine API. Crop health colour-coding on farm map.

### Inventory and Input Management
Input inventory (seeds, fertilisers, pesticides, feed, medicine). Stock receipts with supplier, batch number, expiry date. Automatic stock deduction on activity logging. Low stock and expiry alerts. Equipment and tools inventory with maintenance scheduling and fuel log. Harvest produce inventory per storage location. Post-harvest loss tracking. Uganda-specific: NAADS input voucher tracking, agro-dealer directory.

### Supply Chain Traceability
Batch creation from harvest with origin plot(s) and quality grade. Chain of custody (farm → collection → processor → exporter). QR code generation per batch. GPS polygon export as GeoJSON for EUDR compliance. Farmer profile for export buyers. Input traceability per batch. Certification tracking (organic, RainForest Alliance, UTZ, GlobalGAP, FairTrade). Deforestation-free verification against Global Forest Watch baseline. EUDR Due Diligence Statement generation. Buyer portal (read-only, no auth). Uganda-specific: coffee EUDR compliance, UEPB requirements, NAADS/OWC traceability.

### Marketplace and Market Linkage
Produce and livestock listings. Buyer search by crop type and location. Market price database (all major Uganda markets). Price alerts. Agro-dealer directory. Vet and extension officer directory. Transport matching. Order management. Verified reviews. Uganda-specific: district-level market prices, WhatsApp direct link, cooperative bulk sales aggregation.

### Cooperative Module
Cooperative managed as a single franchise (tenant) with multiple member farms. Member farmer registration. Member farm mapping (GPS boundaries via field agent mobile app). Bulk input distribution tracking. Collection centre management (weigh, record, grade). Quality grading at collection. Member payment calculation (quantity x grade) with mobile money bulk disbursement. Aggregate supply reports. Compliance monitoring. Field agent app (simplified). Farmer performance ranking. Uganda-specific: primary society → apex body hierarchy, NAADS/OWC structure, MTN/Airtel bulk payment APIs.

### Advanced Financial Records (Dual-Mode)
Simple Mode: "Money in", "Money out", "What I owe", "What's owed to me" — default for all users. Advanced Mode: chart of accounts, double-entry journal, trial balance, income statement, balance sheet, cash flow. Farm-specific chart of accounts pre-loaded. Bank reconciliation. Investor/director reporting. Tax computation. PAYE/NSSF for permanent farm workers.

### iOS App
SwiftUI, SwiftData, same offline-first architecture as Android.

### Remaining Languages
French, Portuguese, Kinyarwanda added to complete the 6-language launch set.

## Phase 3 — IoT and Surveillance

### Jaguza IoT Integration (Add-on)
OAuth integration with Jaguza API. Device management (register, assign to animal, battery status). 10-minute polling + real-time webhook alerts. Animal detail page with Jaguza tab (activity graph, temperature trend, fertility index). Herd health dashboard (green/amber/red). Heat/fertility detection alerts. Disease early warning. Fertility calendar. Milk yield correlation overlay. Drone mission link.

### GPS Animal Tracking (Add-on)
Standalone GPS tracker registration (IMEI + SIM). Live map with moving animal icons. Geofence creation and breach alerts (SMS + push + WhatsApp). Overnight monitoring. Historical playback (7/14/30 days). Herd clustering detection. Speed tracking for theft detection. Multi-protocol support (MQTT, HTTP, TCP). Vehicle tracking. Theft investigation report for police/insurance. Uganda-specific: cattle rustling context (Karamoja, Teso), 2-minute alert SLA, Uganda Police report format.

### Live Farm Camera Surveillance (Add-on)
Camera registration (Hikvision/Dahua/Reolink/Generic RTSP/ONVIF). RTSP proxy server (mediamtx/ffmpeg) converting to HLS. Single camera and multi-camera grid views. PTZ control. Night mode. Stream quality selector (Auto/High/Medium/Low). Zone-based motion detection alerts (push + SMS + WhatsApp with snapshot). Alert scheduling (night-only). False alarm reduction. Two-way audio. Share access (time-limited). Uganda-specific: Hikvision/Dahua dominant brands, low-bandwidth 360p mode, solar-powered camera support, WhatsApp motion alert.

### AI Farm Advisor (Add-on)
Natural language farm Q&A using farm's own data context. Photo-based pest/disease diagnosis (Claude Vision API). Personalised recommendations based on activity records and yield analysis. Seasonal planning advisor. Market timing advice. Financial coaching. Offline fallback (pre-loaded guides). Extension officer escalation on low confidence. Multi-lingual responses (all 6 launch languages).

### Drone Imagery Integration
Connect drone survey results to Kulima farm map. Aerial crop health monitoring, livestock headcount, fence inspection.

### Soil Sensor Integration
Soil moisture and temperature sensors reporting to Kulima. Data displayed on plot detail screen. Informs irrigation decisions.

### On-Farm Weather Station Integration
Local weather station data (rainfall, temperature, wind) overrides API weather with actual local readings.

## Phase 4 — Enterprise

### Director Platform
Consolidated farm overview across all owned/managed farms. Financial summary (income vs expenses across farms). Livestock health dashboard (all IoT alerts from all farms). Crop status map with NDVI overlay. Harvest forecast. Staff productivity reports. Approval workflow (large purchase requests). Inter-farm transfer (equipment, animals). Director mobile app (same architecture as Academia Pro/Medic8).

### Multi-Country Expansion
Kenya, Tanzania, Rwanda configuration. Country-specific: currency, crop library, administrative hierarchy, regulatory context, language defaults.

### EUDR DDS Automation
Automated submission of Due Diligence Statement to EU TRACES system.

### White-Label
Agribusinesses can white-label Kulima with their own branding.

### Bank and Insurance API Integrations
Farm financial data as direct input to bank loan applications (Centenary, Equity). Insurance eligibility check and premium calculation (UAP, Jubilee).

### USSD/SMS Fallback
USSD short code for basic transaction recording on feature phones. SMS commands to dedicated number.

### WhatsApp Business API
Motion alerts, marketplace communication, notification delivery via WhatsApp.

## AI Farm Advisor (Phase 3 Add-On)

**Tier:** Growth and Enterprise | **Phase:** 3 (add-on, off by default)

- AI-powered natural language Q&A in English, Luganda, and Swahili
- Photo-based pest and disease diagnosis (camera capture → instant identification)
- Personalised agronomic recommendations based on farm profile, crop, soil, and weather
- Seasonal planting calendar advisory adjusted for GPS-zone rainfall patterns
- Market timing advice (optimal sell window based on historical price patterns)
- Offline fallback: pre-loaded diagnostic guides when connectivity is unavailable

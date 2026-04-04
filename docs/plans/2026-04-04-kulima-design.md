# Kulima Farm Management SaaS — Design Document

**Date:** 2026-04-04
**Author:** Peter Bamuhigire
**Status:** Approved
**Domain:** Agriculture (new domain — to be created)
**Methodology:** Hybrid (Water-Scrum-Fall)

## 1. Project Overview

**Project Name:** Kulima
**Tagline:** *from the farm, for the farm*

Kulima is a multi-tenant SaaS Farm Management Information System (FMIS) providing web and mobile apps (Android + iOS) for individual farmers, farm businesses, cooperatives, and investors to manage farms, crops, livestock, finances, workers, inventory, IoT devices, CCTV surveillance, GPS tracking, supply chain traceability, and an AI-powered farm advisor — built Uganda-first, offline-capable, mobile-money integrated, and globally extensible.

### Target Markets (launch order)
Uganda → Kenya, Tanzania, Rwanda → Nigeria, Ghana, Zambia → Global

### Languages at Launch
English, French, Portuguese, Luganda, Swahili, Kinyarwanda

### Team
Solo developer (Peter Bamuhigire) + AI

## 2. User Types

| User Type | Description |
|---|---|
| **Individual Farmer** | Smallholder, family farmer, or emerging commercial farmer managing their own farm(s). Primary user base. Access via Android app primarily. |
| **Farm Business / Company** | Registered farming company, estate, or agribusiness with multiple farms, managers, employees, and professional reporting requirements. |
| **Cooperative / NGO / Programme** | Organisation managing a group of member farmers. Managed as a single franchise with multiple farms. Handles collective sales and payment distribution to members via mobile money. |
| **Farm Director / Investor** | Owns or has invested in multiple farms. Uses the Director Platform for consolidated reports, approvals, and performance monitoring. |
| **Buyer / Off-taker** | Commodity buyer, exporter, processor, or retailer accessing traceability data via QR code scan or Buyer Portal (read-only, no authentication required). |

## 3. Architecture Decision: Chwezi Core Extension + Selective Service Extraction

### Decision
Build Kulima as another vertical on the existing Chwezi Core platform (same as Academia Pro and Medic8). Shared infrastructure: Auth, Multi-tenancy, RBAC, Billing, Mobile Money, Notifications, Audit, Director Platform, Dual-mode Accounting, Payroll, Reports.

Agriculture-specific modules built as pluggable modules on top.

Three components run as optional standalone edge services due to fundamentally different runtime characteristics:

1. **IoT Gateway** — WebSocket server for real-time Jaguza/sensor data
2. **Camera Proxy** — RTSP-to-HLS conversion server (mediamtx/ffmpeg)
3. **GPS Tracker Receiver** — TCP/MQTT listener for tracker protocols

These are add-on modules — not mandatory for all farmers. Most farmers (Seedling/Grower tiers) will never use them. They spin up only when a farmer activates the add-on.

### Alternatives Considered

**Approach B: Independent Platform, Shared Libraries** — Rejected. Significant duplication of effort, three codebases to maintain solo, loses the "same architecture" advantage.

**Approach C: Microservices / API-First** — Rejected. Massive operational complexity for a solo developer, overkill for current scale, slowest path to MVP.

## 4. System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    KULIMA PLATFORM                       │
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │              CHWEZI CORE (PHP/MySQL)               │  │
│  │                                                    │  │
│  │  Auth · Multi-tenancy · RBAC · Billing · MoMo     │  │
│  │  Notifications · Audit · Director Platform         │  │
│  │  Dual-mode Accounting · Payroll · Reports          │  │
│  │                                                    │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │ Farm &   │ │  Crop    │ │   Livestock       │   │  │
│  │  │ Plot Mgmt│ │  Mgmt    │ │   Management      │   │  │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │Financial │ │Inventory │ │ Task & Worker     │   │  │
│  │  │Records   │ │& Inputs  │ │ Management        │   │  │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │Weather & │ │Marketplace│ │ Supply Chain     │   │  │
│  │  │Advisory  │ │& Market  │ │ Traceability     │   │  │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │  │
│  │  ┌──────────┐ ┌──────────┐                        │  │
│  │  │AI Farm   │ │Cooperative│                        │  │
│  │  │Advisor   │ │Management │                        │  │
│  │  └──────────┘ └──────────┘                        │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ┌─────────────── OPTIONAL EDGE SERVICES ────────────┐  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │IoT Gate- │ │Camera    │ │GPS Tracker       │   │  │
│  │  │way (WS)  │ │Proxy(HLS)│ │Receiver(TCP/MQTT)│   │  │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
         │                │                  │
    ┌────┴────┐     ┌─────┴─────┐    ┌──────┴──────┐
    │Android  │     │  iOS App  │    │  Web App    │
    │(Kotlin) │     │  (Swift)  │    │(Bootstrap5) │
    └─────────┘     └───────────┘    └─────────────┘
```

### Key Architectural Decisions
- **Multi-tenancy:** Same tenant isolation pattern as Academia Pro/Medic8 — tenant-scoped database queries, no data leakage
- **Modular activation:** Add-on modules (IoT, cameras, GPS, traceability, cooperative, marketplace) are feature-flagged per tenant subscription tier
- **REST API layer:** All mobile and web clients communicate through a unified REST API — no direct database access from clients
- **Offline-first mobile:** Android (Room) and iOS (SwiftData) store all farm data locally; background sync via API when connectivity returns
- **Edge services talk to core via internal REST API:** IoT Gateway, Camera Proxy, and GPS Receiver push data into the core's database through authenticated internal endpoints
- **Cooperative model:** Cooperatives are managed as a single franchise (tenant) with multiple member farms. Supports collective sales aggregation and mobile money payment distribution to members.

## 5. Data Architecture

**Database:** MySQL 8.x (consistent with Chwezi Core)

### Core Entity Model

**Farm Layer:**
- `farms` — tenant_id, name, type, total_size, size_unit, location, land_tenure_type, admin_hierarchy, geo_boundary (GeoJSON), operational_status, photos
- `plots` — farm_id, name, type (25+ types), area, geo_boundary (GeoJSON), soil_type, soil_ph, irrigation_type, water_source, stocking_rate, status

**Crop Layer:**
- `crops` — library: name, scientific_name, local_names (JSON), category, linked varieties
- `crop_varieties` — crop_id, name, maturity_days, expected_yield_per_acre, disease_resistance, drought_tolerance, certified_flag
- `crop_seasons` — farm_id, plot_id, crop_variety_id, planned/actual dates, budget, planting_method, seed_source/qty/cost
- `crop_activities` — season_id, plot_id, activity_type, date, inputs_used (JSON), quantity_applied, cost, performed_by, notes, photos
- `crop_health_events` — season_id, plot_id, type (pest/disease), severity, description, photo, ai_diagnosis (JSON), action_taken
- `harvests` — season_id, plot_id, date, quantity, quality_grade, moisture_content, storage_location_id, market_price

**Livestock Layer:**
- `species` — library: name, local_names (JSON), category
- `breeds` — species_id, name, benchmarks (JSON)
- `animals` — farm_id, species_id, breed_id, tag_number, rfid_id, name, sex, dob, colour_markings, acquisition_method, sire_id, dam_id, status, current_plot_id
- `animal_health_events` — animal_id, type (vaccination/treatment/deworming/dipping), date, details (JSON), administered_by, next_due_date
- `animal_reproduction` — animal_id, type (mating/pregnancy_check/birth/weaning), date, details (JSON), sire_used, offspring_count
- `animal_production` — animal_id, type (milk/eggs/honey/wool/manure), date, quantity, unit, session
- `animal_feeding` — animal_id_or_herd_id, date, feed_type, quantity, cost
- `animal_movements` — animal_id, from_plot_id, to_plot_id, date
- `animal_sales` — animal_id, buyer, sale_price, sale_date, weight_at_sale
- `flocks` — farm_id, species_id, breed_id, name, head_count, plot_id

**Financial Layer (extends Chwezi Core accounting):**
- `farm_income` — tenant_id, farm_id, enterprise_type, category, amount, date, payer, payment_method, reference, receipt_photo
- `farm_expenses` — tenant_id, farm_id, enterprise_type, category, amount, date, payee, payment_method, linked_activity_id
- `farm_budgets` — farm_id, period, enterprise_type, planned_income, planned_expenses, categories (JSON)
- `market_prices` — crop_id, market_name, district, price_per_unit, date
- `loans` — tenant_id, lender_type, lender_name, principal, interest_rate, repayment_schedule (JSON), outstanding_balance

**Inventory Layer:**
- `input_items` — farm_id, type, name, unit, current_stock, min_stock_level
- `input_receipts` — item_id, supplier, quantity, unit_cost, batch_number, expiry_date, date
- `storage_locations` — farm_id, name, type, capacity
- `produce_inventory` — farm_id, storage_location_id, crop_id, quantity, quality_grade, harvest_id
- `equipment` — farm_id, name, type, purchase_date, value, maintenance_schedule (JSON), fuel_log (linked)

**Task Layer:**
- `farm_tasks` — farm_id, description, plot_id, assigned_workers (JSON), due_date, estimated_hours, status, recurring_config (JSON)
- `worker_profiles` — tenant_id, name, phone, daily_rate, nin, payment_method, mobile_money_number
- `work_logs` — worker_id, farm_id, date, hours, task_id, wage_paid

**Traceability Layer (add-on):**
- `batches` — farm_id, plot_ids (JSON), crop_id, variety, harvest_date, quantity, quality_grade, qr_code, geo_polygon_export
- `batch_chain` — batch_id, stage, handler, location, date, notes
- `certifications` — farm_id, type, certificate_file, issue_date, expiry_date

**IoT Layer (add-on):**
- `iot_devices` — farm_id, animal_id, type, device_id, battery, signal_strength, last_sync
- `iot_readings` — device_id, timestamp, data (JSON), raw_payload (JSON)
- `iot_alerts` — device_id, animal_id, alert_type, severity, timestamp, acknowledged, message

**Camera Layer (add-on):**
- `cameras` — farm_id, brand, name, plot_id, stream_url, cloud_account_token (encrypted), map_position (JSON), status
- `camera_alerts` — camera_id, type, timestamp, snapshot_path, zone_config (JSON), delivered_via

**GPS Layer (add-on):**
- `gps_trackers` — farm_id, animal_id_or_vehicle_id, imei, sim_number, protocol, battery, last_position (JSON)
- `gps_positions` — tracker_id, timestamp, lat, lng, speed, heading
- `geofences` — farm_id, name, boundary (GeoJSON), alert_enabled
- `geofence_breaches` — geofence_id, tracker_id, timestamp, exit_position (JSON), alert_delivered

**Marketplace Layer (add-on):**
- `listings` — tenant_id, type, details (JSON), quantity, price, location, status, photos
- `marketplace_orders` — listing_id, buyer_id, quantity, status, messages (JSON)
- `reviews` — order_id, reviewer_id, rating, comment
- `directories` — type (agro_dealer/vet/extension_officer/transporter), name, district, contact, verified

### GIS Storage
Farm and plot boundaries stored as GeoJSON in MySQL JSON columns with spatial indexing for proximity queries.

### Multi-lingual
All user-facing strings externalised into translation tables — same i18n pattern as Chwezi Core. Crop/species libraries store local_names as a JSON map (e.g., `{"en": "Maize", "lg": "Kasooli", "sw": "Mahindi", "fr": "Maïs", "pt": "Milho", "rw": "Ikigori"}`).

### Offline Sync
Each table includes `synced_at`, `local_id`, `server_id`, and `is_deleted` columns for conflict-aware bidirectional sync between mobile and server.

## 6. Mobile Architecture and Offline Strategy

**Platforms:** Android (Kotlin, Jetpack Compose) + iOS (Swift, SwiftUI)

**Offline-first principle:** The app must work at full capacity with zero internet. Sync is a background convenience, not a prerequisite.

### Local Storage
- Android: Room database with all farm data tables mirrored locally
- iOS: SwiftData with equivalent schema
- Pre-loaded at install: Uganda crop library (200+ crops), species/breed library, disease library, pest library, unit conversions, administrative hierarchy (districts/sub-counties)

### Sync Strategy
- Queue-based: every create/update/delete operation is written locally and queued for sync
- Background sync triggers when connectivity detected — even briefly (2G is enough)
- Conflict resolution: last-write-wins by timestamp, with a conflict log the farmer can review if the same record was edited on two devices
- Attachment sync (photos, receipts): queued separately, uploaded when on WiFi or strong 3G/4G — compressed client-side before upload (max 512KB)
- Sync priority order: financial transactions first, then activities, then animals, then reference data updates

### Low Bandwidth Mode
- App detects connection quality and switches to text-only mode automatically
- Images lazy-loaded, thumbnails used in lists
- API responses compressed (gzip)

### USSD/SMS Fallback (Feature Phones)
- USSD short code for basic recording: harvest, sale, expense
- SMS commands to a dedicated number for key transactions
- These feed into the same API, same database

### Mobile App Module Structure
- Core modules always installed: Farm/Plot, Crop, Livestock, Financial, Inventory, Tasks, Weather
- Add-on modules downloaded on activation: IoT dashboard, Camera viewer, GPS map, Marketplace, Traceability, Cooperative
- Keeps base APK/IPA size small for farmers on limited storage

## 7. Integration Architecture

### Phase 1 (MVP)
| Integration | Purpose | Protocol |
|---|---|---|
| Open-Meteo API | Weather forecast (free, accurate for Africa) | REST, no auth |
| Africa's Talking | SMS notifications, USSD gateway | REST + API key |
| MTN MoMo API | Subscription payments, worker wage disbursement | REST + OAuth |
| Airtel Money API | Alternative mobile money | REST + API key |
| Firebase Cloud Messaging | Push notifications (Android + iOS) | FCM SDK |

### Phase 2 (Growth)
| Integration | Purpose | Protocol |
|---|---|---|
| Google Maps SDK | Farm boundary drawing, satellite imagery, plot maps | SDK + API key |
| OpenStreetMap/Mapbox | Offline map tiles fallback | Tile download |
| Sentinel-2 / Google Earth Engine | NDVI crop health satellite analysis (free) | REST + OAuth |
| Global Forest Watch / Hansen | Deforestation baseline for EUDR compliance | REST |
| Uganda Met Authority | Official seasonal forecasts | TBD (data agreement needed) |

### Phase 3 (IoT and Surveillance)
| Integration | Purpose | Protocol |
|---|---|---|
| Jaguza API | Ear tag sensor data, alerts, device management | REST + OAuth |
| Hik-Connect API | Hikvision camera stream URLs | REST + OAuth |
| Dahua DMSS API | Dahua camera stream URLs | REST + OAuth |
| Reolink Open API | Reolink camera stream URLs | REST + API key |
| mediamtx/ffmpeg | RTSP-to-HLS stream proxy server | Internal service |
| Claude API (Anthropic) | AI pest/disease identification, farm advisory, NLQ | REST + API key |

### Phase 4 (Enterprise)
| Integration | Purpose | Protocol |
|---|---|---|
| EU TRACES system | EUDR Due Diligence Statement submission | XML/REST |
| Bank APIs (Centenary, Equity) | Farm loan applications from Kulima financial data | TBD |
| Insurance APIs (UAP, Jubilee) | Farm insurance eligibility and premium calculation | TBD |
| WhatsApp Business API | Motion alerts, marketplace communication, notifications | REST |

### Integration Fallback Pattern
All external APIs wrapped in a service layer within the core. Each integration has a fallback:
- Weather: Open-Meteo fails → cached forecast displayed
- Maps: Google Maps unavailable → OpenStreetMap offline tiles
- Mobile money: MoMo fails → retry queue with SMS notification to farmer
- AI advisor: Claude API unavailable → pre-loaded offline pest/disease guide
- Camera stream: internet drops → last cached snapshot shown

## 8. Multi-lingual and Localisation Strategy

**Languages at launch:** English, French, Portuguese, Luganda, Swahili, Kinyarwanda

### Implementation
- All UI strings externalised into translation tables (same i18n pattern as Chwezi Core)
- Language selectable per user, not per tenant
- Crop and species libraries store local names as JSON maps per language
- AI advisor responses generated in the user's selected language (Claude API supports all 6)
- USSD/SMS interactions follow the user's language preference
- Date formats, number formats, and currency symbols localised per country context

### Content That Gets Translated
UI labels, buttons, menus, error messages, tooltips; crop names, species names, breed names, disease names; pre-loaded advisory content; notification templates; report headers and labels; marketplace listing categories

### Content That Stays in User's Input Language
Farm names, plot names, animal names, notes, descriptions; financial records, task descriptions; marketplace listing free-text descriptions

### Translation Expansion Roadmap
Professional translation for launch languages, with a community translation portal on the roadmap for adding more African languages (Amharic, Hausa, Yoruba, Chichewa) as the product expands.

## 9. Subscription and Monetisation Architecture

| Tier | Price | Key Limits |
|---|---|---|
| **Seedling (Free)** | UGX 0 | 1 farm, 5 plots, 1 user, 50 animals, 2 seasons/yr, 5 AI queries/mo |
| **Grower** | UGX 40,000/mo | 5 farms, unlimited plots, 3 users, unlimited animals, 50 AI queries/mo |
| **Harvest** | UGX 100,000/mo | Unlimited farms/plots, 10 users, unlimited AI, all add-ons included |
| **Enterprise** | Custom | Unlimited everything, dedicated CSM, white-label option |

### Architectural Decisions
- Feature gating enforced at API level — middleware checks tenant subscription
- Add-on activation: IoT, cameras, GPS, traceability, cooperative, marketplace — each is a boolean feature flag with own monthly price
- No data deletion on free tier (competitive advantage over Shambapro)
- Payment methods: MTN MoMo, Airtel Money from app; Flutterwave/Paystack for international
- Annual option: pay 10 months, get 12
- Cooperative billing: per-cooperative flat fee (UGX 80,000/mo for up to 50 members), per-member pricing above 50

### Revenue from Integrations
- Jaguza partnership: revenue share or referral fee (commercial terms TBD)
- Marketplace: transaction fee on completed sales (percentage TBD)
- Camera cloud recording: optional upsell for cloud storage beyond local NVR

## 10. Security, Privacy and Compliance

### Authentication and Access
- Session-based auth (web) + JWT (mobile/API) — dual-auth pattern from Chwezi Core
- RBAC with tenant-scoped permissions: Farm Owner, Farm Manager, Worker, Director, Cooperative Admin, Field Agent, Buyer (read-only portal)
- Workers get a simplified mobile interface — assigned tasks only
- Buyer portal: unauthenticated QR code scan shows traceability data only

### Uganda Data Protection Act 2019
- Explicit opt-in consent for GPS farm boundary collection, location tracking, and photo uploads
- Traceability data shared with buyers only with farmer's explicit approval per batch
- Account deletion request purges personal data within 30 days
- Data residency: primary hosting in Africa

### Farm Data Sensitivity
- Farm GPS boundaries encrypted at rest, never exposed in marketplace listings
- Financial records accessible only to farmer and explicitly granted users
- IoT device tokens and camera credentials encrypted at rest with per-tenant encryption keys
- Mobile money credentials never stored — handled via API redirect flow

### EUDR Compliance Data Handling
- Traceability data exports include only minimum required: farm polygon, crop type, harvest date, deforestation check result
- No personal farmer financial or health data included in EUDR exports

### Offline Security
- Mobile local database encrypted (Android: SQLCipher, iOS: Core Data encryption)
- Biometric lock option on app launch (fingerprint/face)
- Auto-logout after configurable inactivity period
- Offline data wiped on device if account is remotely deactivated

## 11. Build Phases and MVP Scope

### Phase 1: MVP — The Farmer's Essential Toolkit
**Goal:** A working product that a smallholder in Mbarara can use tomorrow to replace their paper notebook.

**Modules:** Farm and plot management (manual area entry), crop management (full lifecycle), livestock management (individual + flock), basic financial records, task and worker management, weather forecast (Open-Meteo), user roles, SMS/push notifications, offline-first Android app, web dashboard, mobile money subscription payment.

**Languages:** English, Luganda, Swahili (3 of 6)

**Not in Phase 1:** GPS mapping, satellite imagery, marketplace, traceability, IoT, cameras, GPS tracking, AI advisor, cooperative module, iOS app, director platform, advanced accounting, French/Portuguese/Kinyarwanda

### Phase 2: Growth — Commercial Farmers and Export Compliance
**Adds:** GPS polygon mapping, NDVI satellite analysis, inventory and input management, supply chain traceability (EUDR), marketplace, cooperative module (franchise model), advanced accounting (dual-mode), iOS app, remaining languages (French, Portuguese, Kinyarwanda)

### Phase 3: IoT and Surveillance — Technology-Forward Farms
**Adds:** Jaguza API integration, GPS animal tracking, live CCTV integration, AI farm advisor (Claude API), drone imagery, soil sensor integration, on-farm weather station integration

### Phase 4: Enterprise — Scale and Ecosystem
**Adds:** Director platform, multi-country expansion (Kenya, Tanzania, Rwanda), EUDR DDS automation, white-label, bank/insurance API integrations, USSD/SMS fallback, WhatsApp Business API

### SRS Approach
Full SRS covering all 4 phases, with each requirement clearly marked with its target phase. This gives a complete picture for planning while making the MVP boundary explicit.

## 12. Reference Materials

| Book | Relevance |
|---|---|
| Olson and Westra — The Economics of Farm Management (2022) | Enterprise budgets, financial analysis, risk management, operations management, strategic planning |
| Yasunaga — Farm and Rural Community Management in Less Favored Areas (2020) | Rural community economics, cooperative module, policy integration |
| Chaudhary — Digital Ecosystem for Innovation in Agriculture (2023) | IoT frameworks, remote sensing, AI/ML, data fusion |
| Kaushalya — Digital Agriculture: Role of Data and IT (2023) | Precision agriculture, sensor technologies, big data, IoT, AI/ML, data security |
| Alabi — Rise of Digital Agriculture (2021) | Africa-focused digital agriculture, ICT in African farming |
| Popkova — Digital Agriculture for Food Security (2023) | Food security policy, quality management, sustainable development, export potential |

## 13. Open Decisions and Gaps

Carried forward from the product spec Section 15:

### HIGH Priority (resolve before development)
- Jaguza API specification (obtain from Jaguza team)
- Camera streaming infrastructure cost at scale
- EUDR deforestation baseline data source integration
- Uganda agricultural regulatory compliance check (MAAIF)
- GPS tracker protocol testing (purchase and test 3-5 Uganda models)
- Data Protection Act 2019 compliance review extension to Kulima

### MEDIUM Priority (resolve before Phase 2)
- Uganda Met Authority API access agreement
- UCDA registration integration
- Uganda market price data API access
- Insurance API specs (UAP, Jubilee)
- Bank/SACCO API integration (MTN MoMo Business, Centenary, Equity)
- NAADS/OWC programme integration

### Internal Decisions
- Free tier data retention policy (confirmed: never delete)
- Jaguza partnership model (revenue share vs API fee vs white-label)
- Camera cloud recording (Kulima storage vs redirect to camera vendor cloud)
- Cooperative module pricing (per-cooperative up to 50 members, per-member above 50)
- EUDR as core feature or premium add-on

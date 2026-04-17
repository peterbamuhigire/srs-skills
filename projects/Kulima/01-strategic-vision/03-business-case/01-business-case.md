# Business Case: Kulima Farm Management Information System

**Project:** Kulima
**Prepared by:** Peter Bamuhigire
**Date:** 2026-04-04
**Standard:** IEEE 1058-1998 (adapted)
**Version:** 1.0

---

## 1 Executive Summary

Kulima addresses a structural gap in Sub-Saharan African agriculture: the absence of an affordable, offline-capable, mobile-money-integrated Farm Management Information System (FMIS) that unifies crop management, livestock management, IoT sensor integration, CCTV surveillance, GPS animal tracking, supply chain traceability, and AI advisory in a single platform. The investment required is one solo developer (Peter Bamuhigire) working full-time using the existing Chwezi Core framework, Claude AI development tokens, and standard cloud infrastructure. The project follows a 4-phase delivery model targeting Monthly Recurring Revenue (MRR) growth from UGX 4M in Phase 1 (100 paying farmers) to UGX 150M in Phase 4, with payback projected within Phase 2.

## 2 Problem Statement

### 2.1 Current State

Ugandan agriculture is dominated by smallholder farmers (approximately 69% of the population engages in agriculture per Uganda Bureau of Statistics). Farm record-keeping remains overwhelmingly paper-based: handwritten notebooks for planting dates, harvest quantities, income, and expenses. Farmers who have adopted digital tools face fragmented solutions — Jaguza for IoT ear tags only, FarmTrace for traceability only, Shambapro for basic crop records with a data deletion policy on inactivity.

### 2.2 Pain Points

1. **Data loss:** Paper records are destroyed by rain, termites, and misplacement. No backup, no historical analysis capability.
2. **No profitability analysis:** Farmers cannot determine which enterprise (crop or livestock) generates profit and which operates at a loss. Input costs are not tracked against harvest revenue at the enterprise level.
3. **Missed veterinary schedules:** Vaccination, deworming, and dipping schedules are tracked mentally or on wall calendars. Missed treatments lead to preventable livestock disease and mortality.
4. **No bank-ready financial records:** Farmers seeking SACCO, MFI, or commercial bank loans cannot produce standardised financial statements. Loan officers report that [IMPACT-TBD]% of smallholder loan applications lack adequate documentation.
5. **No EUDR compliance capability:** Uganda exported $817M in coffee (2022/23, UCDA). The EU Deforestation Regulation (effective 30 December 2025) requires GPS polygon farm boundaries, input traceability, and deforestation-free verification. No affordable tool provides this for smallholder coffee farmers.
6. **Fragmented tool landscape:** A farmer needing crop records, livestock management, IoT monitoring, and traceability must subscribe to 3-4 separate platforms at a combined cost exceeding $100/month.

### 2.3 Cost of Inaction

- **Income leakage:** Farmers who do not track input costs against harvest revenue lose an estimated [IMPACT-TBD]% of potential profit to untracked waste, theft, and post-harvest loss.
- **EUDR market exclusion:** Export farmers and cooperatives without GPS-polygon traceability will be unable to sell coffee, cocoa, and timber commodities to EU buyers from 30 December 2025 onward. Uganda's coffee exports to the EU represent approximately 60% of total coffee export value [IMPACT-TBD: verify exact percentage].
- **Preventable livestock mortality:** Missed vaccination and treatment schedules contribute to livestock disease losses estimated at [IMPACT-TBD]% of herd value annually in Uganda.

## 3 Proposed Solution

### 3.1 Approach

Kulima is built as a multi-tenant SaaS extension of the Chwezi Core framework (shared with Academia Pro and Medic8), delivered in 4 phases:

1. **Phase 1 (MVP):** Core farm, crop, livestock, financial, task, weather, and offline-first mobile modules
2. **Phase 2 (Growth):** GPS mapping, NDVI satellite imagery, inventory, supply chain traceability (EUDR), marketplace, cooperative module, iOS app, dual-mode accounting
3. **Phase 3 (IoT and Surveillance):** Jaguza IoT integration, GPS animal tracking, live CCTV surveillance, AI farm advisor, drone and sensor integration
4. **Phase 4 (Enterprise):** Director platform, multi-country expansion, EUDR DDS automation, white-label, bank/insurance API integration, USSD/SMS fallback, WhatsApp Business API

### 3.2 Key Capabilities

| Capability | Business Goal Addressed | Phase |
|---|---|---|
| Offline-first Android app with Room database | Eliminate data loss; serve farmers with no/intermittent internet | 1 |
| Per-enterprise profitability analysis | Enable data-driven farming decisions; produce bank-ready records | 1 |
| Livestock health event scheduling with SMS alerts | Reduce preventable disease and mortality from missed treatments | 1 |
| GPS polygon farm mapping with GeoJSON export | EUDR compliance for export farmers and cooperatives | 2 |
| Supply chain traceability with QR code and DDS generation | Maintain EU market access for Uganda's coffee and cocoa exports | 2 |
| Jaguza IoT integration with real-time health alerts | Early disease detection; reduce livestock losses | 3 |
| AI-powered pest/disease photo identification | Immediate diagnostic support where extension officers are unavailable | 3 |

## 4 Cost-Benefit Analysis

### 4.1 Development Costs

| Cost Item | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Notes |
|---|---|---|---|---|---|
| Developer time (Peter, full-time) | Opportunity cost | Opportunity cost | Opportunity cost | Opportunity cost | Solo developer; no salary outflow |
| Claude AI tokens (development) | [COST-TBD] | [COST-TBD] | [COST-TBD] | [COST-TBD] | AI-assisted development |
| Claude API (production, AI advisor) | — | — | [COST-TBD] | [COST-TBD] | Per-request cost for farm advisory |
| Cloud hosting (Africa-based) | [COST-TBD]/month | [COST-TBD]/month | [COST-TBD]/month | [COST-TBD]/month | Shared infrastructure with Academia Pro, Medic8 |
| Google Maps API | [COST-TBD]/month | [COST-TBD]/month | [COST-TBD]/month | [COST-TBD]/month | $200 free credit/month; excess billed per request |
| Africa's Talking SMS | [COST-TBD]/month | [COST-TBD]/month | [COST-TBD]/month | [COST-TBD]/month | ~UGX 30/SMS in Uganda |
| Domain and SSL | ~$15/year | — | — | — | Let's Encrypt (free SSL) |
| Apple Developer Programme | — | $99/year | $99/year | $99/year | Required for iOS App Store |
| Google Play Developer | $25 (one-time) | — | — | — | One-time registration |

### 4.2 Operational Costs (Monthly, at Scale)

| Cost Item | Per-User Estimate | At 1,000 Users | At 5,000 Users |
|---|---|---|---|
| Server hosting (proportional) | [COST-TBD] | [COST-TBD] | [COST-TBD] |
| SMS notifications | ~UGX 150/user/month (5 SMS) | UGX 150,000 | UGX 750,000 |
| Mobile money transaction fees | ~1.5% of subscription value | Variable | Variable |
| Google Maps API (beyond free tier) | [COST-TBD] | [COST-TBD] | [COST-TBD] |
| Camera proxy (mediamtx/ffmpeg) | [COST-TBD] per stream | [COST-TBD] | [COST-TBD] |
| Claude API (AI advisor) | [COST-TBD] per query | [COST-TBD] | [COST-TBD] |
| Customer support | [COST-TBD] | [COST-TBD] | [COST-TBD] |

### 4.3 Revenue Projections

#### 4.3.1 Subscription Tiers

| Tier | Monthly Price (UGX) | Target Segment |
|---|---|---|
| Seedling (Free) | 0 | Smallholder onboarding; 1 farm, basic records |
| Grower | 40,000 | Active individual farmers; full crop + livestock + financial |
| Harvest | 100,000 | Farm businesses; multi-user, advanced accounting, reports |
| Enterprise | Custom | Cooperatives, programmes, large estates |

#### 4.3.2 Add-On Revenue (Phase 3+)

| Add-On | Monthly Price (UGX) | Description |
|---|---|---|
| IoT Integration (Jaguza) | 50,000 | Per-farm IoT dashboard and alerts |
| GPS Animal Tracking | 30,000 | Per-farm live tracking and geofencing |
| Live Camera Surveillance | 40,000 | Per-farm CCTV streaming and motion alerts |
| Supply Chain Traceability | 60,000 | Per-cooperative/exporter EUDR compliance |
| Cooperative Module | 80,000 | Per-cooperative member management and payments |

#### 4.3.3 Revenue by Phase

| Phase | Target Users (Paying) | Average Revenue per User (UGX/month) | Projected MRR (UGX) |
|---|---|---|---|
| Phase 1 | 100 | 40,000 | 4,000,000 |
| Phase 2 | 300 | 66,667 | 20,000,000 |
| Phase 3 | 600 | 100,000 | 60,000,000 |
| Phase 4 | 1,500 | 100,000 | 150,000,000 |

### 4.4 Net Present Value

The NPV of the project over a 4-year horizon is calculated as:

$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$

Where:

- $CF_t$ = net cash flow in period $t$ (monthly revenue minus operational costs)
- $r$ = discount rate (assumed 20% annually to reflect Uganda risk premium and opportunity cost)
- $n$ = 48 months (4-year projection)

[COST-TBD: Populate with actual monthly cash flow projections once development and operational cost estimates are confirmed.]

## 5 ROI Projection

### 5.1 Return on Investment

$$ROI = \frac{\text{Net Profit}}{\text{Total Investment}} \times 100\%$$

### 5.2 Payback Period

$$\text{Payback Period} = \frac{\text{Total Investment}}{\text{Monthly Net Cash Flow}}$$

### 5.3 Assumptions

1. Developer time is valued at opportunity cost only (no salary outflow); if valued at market rate, solo senior PHP/Kotlin developer in Kampala commands approximately UGX 5-8M/month [COST-TBD: confirm rate].
2. Free tier conversion rate to paid: 15% within 3 months of registration.
3. Monthly churn rate: 5% for Phase 1, declining to 3% by Phase 3 as switching costs increase.
4. Mobile money transaction fee: 1.5% of subscription value on average.
5. Uganda shilling exchange rate: approximately UGX 3,750 per USD (2026 estimate).
6. Cloud hosting costs are shared across Kulima, Academia Pro, and Medic8; Kulima's proportional share is estimated at 33%.
7. Phase 1 revenue is 100% subscription; add-on revenue begins in Phase 3.
8. Annual discount (pay 10 months, receive 12) reduces effective per-user revenue by approximately 17% for annual subscribers.

## 6 Risk Assessment

### 6.1 Probability-Impact Matrix

|  | **Low Impact** | **Medium Impact** | **High Impact** |
|---|---|---|---|
| **High Probability** | | Farmer smartphone adoption rate lower than projected | Single developer bus factor |
| **Medium Probability** | | EUDR regulation timeline changes | Jaguza API partnership fails to materialise; Shambapro competitive response |
| **Low Probability** | | Mobile money API reliability in rural areas | Camera streaming infrastructure cost exceeds projections |

### 6.2 Risk Register

| # | Risk | P | I | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | Jaguza API partnership fails to materialise — no IoT ear tag integration available | M | H | Design IoT module with abstraction layer supporting multiple hardware providers. Defer IoT to Phase 3 add-on; core product does not depend on it. Identify alternative providers (mOOvement, Digitanimal). | Peter |
| R2 | EUDR regulation timeline changes — EU extends or modifies compliance deadlines, reducing urgency | M | M | Traceability module delivers standalone value (buyer trust, quality assurance) regardless of EUDR timeline. Market the module as "export readiness" rather than solely EUDR compliance. | Peter |
| R3 | Shambapro competitive response — Shambapro accelerates feature development to match Kulima's scope | M | H | Compete on depth (offline-first, IoT, CCTV, traceability, cooperative module) and on trust (no data deletion policy). Accelerate Phase 1 launch to establish market position. | Peter |
| R4 | Mobile money API reliability in rural areas — MTN MoMo and Airtel Money APIs experience downtime or latency in rural Uganda | L | M | Implement retry queues with exponential backoff. Support manual payment confirmation as fallback. Cache subscription status locally to avoid blocking app access during payment API outages. | Peter |
| R5 | Farmer smartphone adoption rate lower than projected — fewer farmers own Android smartphones capable of running the app | H | M | Target Tecno Spark and equivalent devices (2 GB RAM, Android 11+) which dominate Uganda's affordable smartphone market. Phase 4 includes USSD/SMS fallback for feature phone users. Cooperative model enables field agents to record on behalf of farmers. | Peter |
| R6 | Camera streaming infrastructure cost exceeds projections — mediamtx/ffmpeg proxy servers require more compute than budgeted for concurrent streams | L | H | Camera module is a paid add-on; revenue must cover infrastructure cost per stream. Implement stream quality auto-downgrade (360p for low bandwidth). Set maximum concurrent streams per tenant. Price add-on after infrastructure cost validation in pilot. | Peter |
| R7 | Single developer bus factor — project depends entirely on one developer for all development, operations, and support | H | H | Chwezi Core shared framework reduces Kulima-specific code surface. Comprehensive documentation (SRS, design docs, CLAUDE.md) enables onboarding of a second developer. Modular architecture allows feature-level handoff. Revenue from Phase 2 onward funds contractor hiring. | Peter |

## 7 Timeline and Milestones

| Phase | Duration | Target Start | Target End | Key Deliverables | Decision Gate |
|---|---|---|---|---|---|
| Phase 1 (MVP) | 6 months | [TBD] | [TBD] | Web dashboard, Android app (offline-first), crop/livestock/financial/task/weather modules, mobile money subscription | **Go/No-Go:** 100 paying farmers, UGX 4M MRR |
| Phase 2 (Growth) | 6 months | Phase 1 + 1 month | — | GPS mapping, NDVI, inventory, traceability (EUDR), marketplace, cooperative module, iOS app, dual-mode accounting | **Go/No-Go:** UGX 20M MRR, 1 cooperative onboarded, 1 EUDR-compliant export batch |
| Phase 3 (IoT) | 6 months | Phase 2 + 1 month | — | Jaguza IoT, GPS tracking, CCTV surveillance, AI advisor, drone/sensor integration | **Go/No-Go:** UGX 60M MRR, 3 IoT farms active, camera proxy cost validated |
| Phase 4 (Enterprise) | 6 months | Phase 3 + 1 month | — | Director platform, multi-country (KE, TZ, RW), EUDR DDS automation, white-label, bank API, USSD/SMS, WhatsApp | **Go/No-Go:** UGX 150M MRR, 1 white-label client, 2 countries live |

## 8 Go/No-Go Criteria

Each phase gate requires meeting the following measurable thresholds before committing resources to the next phase.

| # | Criterion | Threshold | Measurement Method |
|---|---|---|---|
| G1 | Paying farmer count | Phase target met (100 / 300 / 600 / 1,500) | Subscription database count of active, paid tenants |
| G2 | MRR target | Phase MRR met (UGX 4M / 20M / 60M / 150M) | Sum of monthly subscription and add-on revenue from payment gateway records |
| G3 | Offline sync reliability | 99.9% of queued records sync successfully within 60 seconds of connectivity | Sync success rate from server-side sync logs |
| G4 | API response time | P95 < 500 ms for CRUD operations under current user load | Application Performance Monitoring (APM) P95 metric |
| G5 | Monthly churn rate | Below 8% in Phase 1, below 5% from Phase 2 onward | (Cancelled subscriptions / active subscriptions at month start) x 100 |

If any gate criterion is not met, the project pauses Phase (N+1) development and redirects effort to closing the gap in the current phase.

## 9 Pilot / Proof of Concept Plan

Per Royce's "Do It Twice" principle (Royce, 1970), a controlled pilot precedes full commercial launch.

### 9.1 Pilot Scope

- **Location:** Mbarara district, Western Uganda (high dairy and crop farming density; strong mobile money penetration; Ankole Longhorn cattle population for livestock module validation)
- **Participants:** 10-20 farmers, comprising:
  - 5-8 smallholder mixed farmers (crops + livestock, 2-10 acres)
  - 3-5 dairy farmers (cattle-focused, herd size 10-50)
  - 2-3 commercial crop farmers (coffee, matooke, or tea enterprises)
  - 1-2 cooperative collection centre operators (if available)
- **Duration:** 8 weeks

### 9.2 Pilot Objectives

1. Validate offline-first architecture on Tecno Spark and equivalent devices in areas with intermittent connectivity
2. Confirm that a new farmer can register and record their first activity within 5 minutes without external help
3. Measure actual sync success rate against the 99.9% target
4. Collect usability feedback on crop, livestock, and financial modules from farmers with no prior digital record-keeping experience
5. Validate mobile money subscription payment flow (MTN MoMo, Airtel Money)
6. Identify missing crop varieties, livestock breeds, disease names, and local terminology gaps

### 9.3 Pilot Success Criteria

| Criterion | Target |
|---|---|
| Farmer retention (still using after 8 weeks) | 80% of pilot participants |
| Offline sync success rate | 99.9% |
| Onboarding time (register + first record) | Median < 5 minutes |
| Critical bugs reported | 0 unresolved at pilot end |
| Willingness to pay (post-pilot survey) | 70% of pilot participants state willingness to subscribe at UGX 40,000/month |

### 9.4 Pilot-to-Launch Decision

If pilot success criteria are met, proceed to commercial Phase 1 launch targeting 100 farmers. If criteria are not met, iterate on identified gaps and run a second 4-week pilot cycle before launch.

## 10 Approval

| Role | Name | Decision (Go / No-Go / Defer) | Date |
|---|---|---|---|
| Project Owner | Peter Bamuhigire | | |
| Technical Reviewer | | | |
| Business Advisor | | | |

---

*This business case is a living document. Financial projections marked [COST-TBD] and impact figures marked [IMPACT-TBD] shall be populated as vendor quotes and market research data become available. All figures are subject to revision at each phase gate review.*

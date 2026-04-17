# 3 Market Opportunity

## 3.1 Uganda Market Sizing

### 3.1.1 Total Addressable Market (TAM)

Uganda has over 6,000 registered health facilities. The TAM assumes every facility adopts a healthcare management system at the average subscription price across tiers.

| Segment | Facilities | Avg Monthly Subscription (UGX) | Annual Revenue (UGX) | Annual Revenue (USD) |
|---|---|---|---|---|
| Private clinics | 4,000 | 150,000 (Starter) | 7,200,000,000 | 1,920,000 |
| Government facilities (HC II-IV, General Hospitals) | 2,800 | 350,000 (Growth) | 11,760,000,000 | 3,136,000 |
| Mission / NGO hospitals | 150 | 700,000 (Pro) | 1,260,000,000 | 336,000 |
| Multi-facility networks | 20 | 2,000,000 (Enterprise, estimated) | 480,000,000 | 128,000 |
| National referral hospitals | 6 | 5,000,000 (Enterprise, estimated) | 360,000,000 | 96,000 |
| PEPFAR implementing partners (facility count) | 200 | 700,000 (Pro) | 1,680,000,000 | 448,000 |
| TOTAL TAM (Uganda) | ~7,176 | | 22,740,000,000 | ~6,064,000 |

Uganda TAM: approximately UGX 22.7 billion (USD 6.1 million) per year. The private clinic segment alone (4,000 facilities) represents UGX 7.2 billion (USD 1.9 million) per year — with ClinicMaster's installed base of 200+ facilities representing less than 5% penetration.

### 3.1.2 Serviceable Addressable Market (SAM)

SAM filters the TAM to segments Medic8 can realistically serve within 3 years, given the product roadmap and sales capacity. This excludes national referral hospitals (Phase 4+ target requiring enterprise sales cycles) and limits government facilities to those with internet access and digital readiness.

| Segment | SAM Facilities | Annual Revenue (UGX) | Annual Revenue (USD) |
|---|---|---|---|
| Private clinics (urban + peri-urban) | 1,500 | 2,700,000,000 | 720,000 |
| Government facilities (HC IV + General Hospitals) | 300 | 1,260,000,000 | 336,000 |
| Mission / NGO hospitals | 100 | 840,000,000 | 224,000 |
| PEPFAR implementing partners | 100 | 840,000,000 | 224,000 |
| Multi-facility networks | 10 | 240,000,000 | 64,000 |
| TOTAL SAM (Uganda) | ~2,010 | 5,880,000,000 | ~1,568,000 |

Uganda SAM: approximately UGX 5.9 billion (USD 1.6 million) per year.

### 3.1.3 Serviceable Obtainable Market (SOM) — 24-Month Target

SOM represents the realistic acquisition target within the 24-month roadmap, accounting for solo-developer sales capacity and the phased product build.

| Phase | Target Facilities | MRR (UGX) | Annual Revenue (UGX) | Annual Revenue (USD) |
|---|---|---|---|---|
| Phase 1 (Month 6) | 10 | 1,500,000 | 18,000,000 | 4,800 |
| Phase 2 (Month 12) | 50 | 15,000,000 | 180,000,000 | 48,000 |
| Phase 3 (Month 18) | 80 | 40,000,000 | 480,000,000 | 128,000 |
| Phase 4 (Month 24) | 150 | 100,000,000 | 1,200,000,000 | 320,000 |

24-month SOM: UGX 100M MRR (USD 320,000 annualised) from approximately 150 facilities.

## 3.2 Francophone Africa Market

The French-language interface unlocks a market that is structurally inaccessible to English-only competitors. No commercial EHR with a complete, clinician-reviewed French interface currently operates in this market.

| Country | Registered Facilities | Population | Entry Phase | Key Driver |
|---|---|---|---|---|
| DRC | 1,200+ (formal sector) | 100M+ | Phase 4 | Largest Francophone healthcare IT greenfield in Africa; significant donor-funded health infrastructure (PEPFAR, Global Fund, USAID) |
| Rwanda | 1,500+ | 14M | Phase 3/4 | Actively digitising health sector; government-mandated Mutuelle de Santé insurance scheme; advanced national HMIS |
| Cameroon | 3,000+ | 28M | Phase 4+ | French-English bilingual population; growing private clinic market |
| Burundi | 800+ | 13M | Phase 4+ | French official language; early-stage health IT market; significant NGO presence |

Combined Francophone market: 6,500+ health facilities where the French-language interface removes the primary adoption barrier. This market is directly unlocked by the i18n architecture built for Phase 1 — no additional infrastructure investment is required to enter these markets.

DRC market note: DRC alone has 1,200+ registered health facilities and a population of 100M+. The healthcare sector is heavily donor-funded (PEPFAR, Global Fund, UNICEF, MSF), which provides a familiar sales motion for an EHR that offers PEPFAR MER indicators, donor fund accounting, and FHIR R4 API in a French-language interface.

Rwanda market note: Rwanda has 1,500+ registered facilities and an actively digitising government health sector. The government-mandated Mutuelle de Santé community health insurance scheme creates a specific workflow requirement (insurance management) that Medic8 addresses. French is a co-official language alongside Kinyarwanda. The Rwandan health sector has demonstrated willingness to adopt digital tools that integrate with the national HMIS.

## 3.3 East Africa Expansion Multiplier

The country configuration layer enables expansion without forking the codebase. East African markets multiply the Uganda TAM significantly.

| Country | Estimated Facilities | Entry Phase | Multiplier vs Uganda TAM |
|---|---|---|---|
| Kenya | 12,000+ | Phase 3 | 2.0x |
| Tanzania | 8,000+ | Phase 3 | 1.3x |
| Rwanda | 1,500+ | Phase 3/4 | 0.25x |
| DRC | 4,000+ (formal sector) | Phase 4 | 0.7x |
| Nigeria | 30,000+ | Phase 4 | 5.0x |

East Africa (Kenya + Tanzania + Rwanda) TAM multiplier: approximately 3.5x the Uganda TAM, bringing the regional TAM to approximately USD 19.5 million per year. With Francophone Africa added (DRC + Cameroon + Burundi), the total addressable region exceeds USD 25 million per year.

## 3.4 Global AI in Healthcare Market

The global generative AI in healthcare market is projected to exceed USD 45 billion by 2030, with a compound annual growth rate exceeding 40% from 2024. The primary growth drivers are clinical documentation automation, revenue cycle management AI, and clinical decision support.

East Africa positioning within this trend:

- The generative AI adoption wave in clinical documentation began in 2023 in North America and Europe. East Africa is 2-3 years behind this curve — the adoption window is open.
- Facilities that adopt AI-assisted documentation early establish workflow efficiency advantages (15-20 minutes per clinician per day recovered from documentation) and accumulate structured clinical data that supports population health analytics over time.
- AI claim scrubbing, which predicts insurance rejection before submission, is an immediately monetisable capability. Every rejected insurance claim costs a facility in delayed reimbursement and administrative rework. A 20% reduction in first-submission rejection rate is a direct revenue improvement.
- No competitor in the East Africa market currently offers clinician-facing generative AI at the point of care. The early-mover window is structurally limited: once one EHR establishes AI credibility in this market, switching costs make displacement difficult.

Medic8's AI Intelligence module is positioned as a standalone credit pack or flat fee add-on — not bundled into a premium tier — so any facility can activate it regardless of clinical subscription tier. This maximises adoption velocity.

## 3.5 Future Markets: India and Australia

- India: Over 70,000 private hospitals and 30,000+ primary health centres. The private hospital chain segment alone (500-bed+ networks) represents a multi-billion dollar HIS market. Medic8 targets mid-tier private hospital chains in Phase 4 via the country configuration layer. ABDM (Ayushman Bharat Digital Mission) ABHA health ID integration is a market entry requirement.
- Australia: High-compliance, high-ARPU market for specialist clinics and allied health. Medicare Number integration and My Health Record connectivity are required. Smaller facility count but significantly higher per-facility revenue (AUD 500-2,000/month).

## 3.6 TCO Competitive Advantage

The TCO comparison against OpenMRS is the primary migration pitch for PEPFAR-funded facilities and mission hospitals.

| Cost Category | OpenMRS (3-Year) | Medic8 (3-Year) | Medic8 Advantage |
|---|---|---|---|
| Software licence | $0 | $3,150-$23,700 | — |
| Server/infrastructure | $1,800-$6,000 | Included | $1,800-$6,000 saved |
| Initial implementation | $10,000-$50,000 | $0-$1,500 | $8,500-$48,500 saved |
| Ongoing customisation | $15,000-$60,000 | Included | $15,000-$60,000 saved |
| Billing system | $3,000-$15,000 | Included | $3,000-$15,000 saved |
| HR/Payroll | $2,000-$8,000 | Included | $2,000-$8,000 saved |
| Insurance management | $5,000-$25,000 | Included | $5,000-$25,000 saved |
| Training/support | $6,000-$30,000 | Included | $6,000-$30,000 saved |
| AI Intelligence module | Custom build $5,000-$20,000 | Credit pack add-on | $5,000-$20,000 saved |
| TOTAL | $35,000-$130,000 | $9,450-$71,100 | $25,550-$58,900 saved |

Medic8 saves the average facility USD 25,550-58,900 over 3 years compared to OpenMRS, while delivering billing, insurance, HR, payroll, mobile money, a patient app, AI Intelligence capabilities, and local Uganda-based support. The migration pitch: "OpenMRS is free to download and costs $35,000-$130,000 to run. Medic8 costs $9,450-$71,100 and includes everything OpenMRS requires you to build separately."

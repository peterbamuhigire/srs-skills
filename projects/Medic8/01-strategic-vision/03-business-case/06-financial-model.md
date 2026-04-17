# 6 Financial Model

## 6.1 Development Costs

### 6.1.1 Developer Cost

Medic8 is developed by a solo developer (Peter) under Chwezi Core Systems. There is no salary expense; the cost is measured as opportunity cost of time allocated to Medic8 versus alternative revenue-generating activities.

| Item | Estimate | Notes |
|---|---|---|
| Developer opportunity cost (Phase 1, 6 months) | ~USD 12,000-18,000 | Based on comparable freelance PHP/mobile developer rates in Uganda (USD 2,000-3,000/month). This is not an outflow -- it is the opportunity cost of time that could be billed to clients. |
| Codebase reuse from Academia Pro | 30-40% reduction in effort | Multi-tenant architecture, authentication, RBAC, country configuration, mobile money integration, offline-first patterns, and global identity layer are shared. |

### 6.1.2 Infrastructure Costs (Annual)

| Item | Annual Cost (USD) | Notes |
|---|---|---|
| Cloud hosting (AWS/DigitalOcean) | 1,200-3,600 | Scales with facility count; initial deployment on shared infrastructure with Academia Pro |
| Domain name | 15-30 | `.com` or `.health` domain |
| SSL certificate | 0 | Let's Encrypt (free) |
| SMS gateway (Africa's Talking) | 600-1,200 | Appointment reminders, OTP, alerts; ~UGX 30-50 per SMS; estimated 1,500-3,000 SMS/month initially |
| Mobile money API setup (MTN MoMo) | 0-200 | One-time merchant registration; ongoing transaction fees are pass-through |
| Mobile money API setup (Airtel Money) | 0-200 | One-time merchant registration |
| Email service (transactional) | 0-120 | Free tier initially; scales with usage |
| **TOTAL Infrastructure (Year 1)** | **1,815-5,350** | |

### 6.1.3 Licensing Costs (Annual)

| Item | Annual Cost (USD) | Notes |
|---|---|---|
| Drug interaction database (DrugBank or equivalent) | 1,000-5,000 | `[CONTEXT-GAP: exact licensing cost]` -- requires vendor quote. DrugBank Academic is free; commercial licence pricing varies. RxNorm/NLM is free for US entities. |
| SNOMED CT | 0 | Free for Low- and Middle-Income Countries (LMICs) via SNOMED International |
| LOINC | 0 | Free, open licence |
| ICD-10/ICD-11 | 0 | Free, WHO licence |
| openEHR tools | 0 | Open-source |
| **TOTAL Licensing (Year 1)** | **1,000-5,000** | |

### 6.1.4 Total Phase 1 Estimated Cost

| Category | Low Estimate (USD) | High Estimate (USD) |
|---|---|---|
| Developer opportunity cost (6 months) | 12,000 | 18,000 |
| Infrastructure (Year 1) | 1,815 | 5,350 |
| Licensing (Year 1) | 1,000 | 5,000 |
| Legal review (PDPA, UMDPC) | 500 | 2,000 |
| **TOTAL Phase 1** | **15,315** | **30,350** |

*Note: Developer opportunity cost is not a cash outflow. Excluding opportunity cost, the cash investment for Phase 1 is USD 3,315-12,350.*

## 6.2 Operational Costs (Monthly)

### 6.2.1 Per-Facility Infrastructure Cost

| Tier | Estimated Hosting Cost per Facility (USD/month) | Gross Margin |
|---|---|---|
| Starter (UGX 150,000 / ~USD 40) | 2-5 | 87-95% |
| Growth (UGX 350,000 / ~USD 93) | 5-10 | 89-95% |
| Pro (UGX 700,000 / ~USD 187) | 10-20 | 89-95% |
| Enterprise (custom) | 20-50 | Negotiated |

Multi-tenant SaaS amortises infrastructure costs across all tenants on shared servers. Gross margin improves as facility count increases.

### 6.2.2 Monthly Operating Expenses (at scale, 50+ facilities)

| Item | Monthly Cost (USD) | Notes |
|---|---|---|
| Cloud hosting (50 facilities) | 200-500 | Shared multi-tenant infrastructure |
| SMS costs (Africa's Talking) | 100-300 | ~5,000-15,000 SMS/month across all facilities |
| Customer support staff (1 hire) | 300-500 | First support hire at ~50 facilities; Kampala-based |
| Mobile money transaction fees | Pass-through | Charged to patient or facility; not a Medic8 expense |
| Drug interaction database | 83-417 | Annual licence amortised monthly |
| **TOTAL Monthly OpEx** | **683-1,717** | |

## 6.3 Revenue Projections (24 Months)

Revenue projections follow the 4-phase roadmap with subscription pricing from `_context/metrics.md`. All UGX to USD conversions use the rate UGX 3,750 = USD 1.

| Month | Phase | New Facilities | Total Facilities | Avg MRR/Facility (UGX) | MRR (UGX) | MRR (USD) |
|---|---|---|---|---|---|---|
| 1-3 | Phase 1 (build) | 0 | 0 | -- | 0 | 0 |
| 4 | Phase 1 (pilot) | 3 | 3 | 0 (free pilot) | 0 | 0 |
| 5 | Phase 1 (launch) | 3 | 6 | 150,000 | 900,000 | 240 |
| 6 | Phase 1 | 4 | 10 | 150,000 | 1,500,000 | 400 |
| 7-8 | Phase 2 | 5 | 15 | 200,000 | 3,000,000 | 800 |
| 9 | Phase 2 | 5 | 20 | 225,000 | 4,500,000 | 1,200 |
| 10 | Phase 2 | 10 | 30 | 250,000 | 7,500,000 | 2,000 |
| 11 | Phase 2 | 10 | 40 | 275,000 | 11,000,000 | 2,933 |
| 12 | Phase 2 | 10 | 50 | 300,000 | 15,000,000 | 4,000 |
| 13-14 | Phase 3 | 5 | 55 | 350,000 | 19,250,000 | 5,133 |
| 15 | Phase 3 | 5 | 60 | 400,000 | 24,000,000 | 6,400 |
| 16-17 | Phase 3 | 10 | 70 | 450,000 | 31,500,000 | 8,400 |
| 18 | Phase 3 | 10 | 80 | 500,000 | 40,000,000 | 10,667 |
| 19-20 | Phase 4 | 15 | 95 | 550,000 | 52,250,000 | 13,933 |
| 21 | Phase 4 | 15 | 110 | 600,000 | 66,000,000 | 17,600 |
| 22-23 | Phase 4 | 20 | 130 | 650,000 | 84,500,000 | 22,533 |
| 24 | Phase 4 | 20 | 150 | 667,000 | 100,000,000 | 26,667 |

*Note: Average MRR per facility increases over time as higher-tier facilities (Growth, Pro, Enterprise) are onboarded in later phases and existing Starter facilities adopt add-ons.*

### 6.3.1 Cumulative Revenue (24 Months)

Total cumulative revenue over 24 months: approximately UGX 460,000,000 (USD 122,700).

`[CONTEXT-GAP: revenue projection assumptions]` -- These projections assume zero churn, linear facility acquisition within each phase, and no annual discount. Actual results will vary based on sales velocity, churn rate, and tier mix. Sensitivity analysis should be conducted for 10%, 20%, and 30% churn scenarios.

## 6.4 ROI Projection

### 6.4.1 Return on Investment

Using the cash investment figure (excluding developer opportunity cost):

$$ROI = \frac{Net\ Benefits - Total\ Costs}{Total\ Costs} \times 100\%$$

| Scenario | Total Cash Investment (24 months, USD) | Cumulative Revenue (24 months, USD) | Net Benefit (USD) | ROI |
|---|---|---|---|---|
| Conservative | 25,000 | 80,000 | 55,000 | 220% |
| Base case | 20,000 | 122,700 | 102,700 | 514% |
| Optimistic | 15,000 | 160,000 | 145,000 | 967% |

### 6.4.2 Payback Period

$$Payback = \frac{Total\ Investment}{Annual\ Net\ Benefit}$$

| Scenario | Total Cash Investment (USD) | Year 2 Annual Revenue (USD) | Year 2 Annual OpEx (USD) | Annual Net Benefit (USD) | Payback (months) |
|---|---|---|---|---|---|
| Conservative | 25,000 | 150,000 | 30,000 | 120,000 | 2.5 |
| Base case | 20,000 | 200,000 | 25,000 | 175,000 | 1.4 |
| Optimistic | 15,000 | 320,000 | 20,000 | 300,000 | 0.6 |

## 6.5 Break-Even Analysis

Break-even occurs when Monthly Recurring Revenue (MRR) exceeds monthly operational costs.

**Monthly operational cost at minimum scale:** USD 683 (Section 6.2.2, low estimate).

**Break-even MRR:** USD 683 = approximately UGX 2,561,250.

**Break-even facility count:**

| Tier Mix | Facilities Required | Timeline (estimated) |
|---|---|---|
| All Starter (UGX 150,000) | 18 facilities | Month 8-9 |
| Mixed (avg UGX 225,000) | 12 facilities | Month 7-8 |
| Weighted toward Growth/Pro | 8 facilities | Month 6-7 |

**Conclusion:** Medic8 reaches operational break-even between Month 7 and Month 9, coinciding with the Phase 2 launch. This assumes the developer does not draw a salary; if a market-rate developer salary of USD 2,500/month is included, break-even shifts to approximately 25-30 facilities (Month 10-11).

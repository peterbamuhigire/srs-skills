# Financial Model — Academia Pro

**Version:** 1.0
**Date:** 2026-03-28

*All figures in this section are planning estimates used for investment decision support. They are clearly marked as assumptions, not audited projections. Currency: Uganda Shillings (UGX). Exchange rate assumption: USD 1 = UGX 3,750 (planning rate, March 2026).*

---

## 1. Pricing Model

### 1.1 Subscription Tiers

Three tiers, priced per school per month in UGX, billed monthly. Annual prepay receives a 10% discount.

| Tier | Pupil Range | Monthly Price (UGX) | Annual Price (UGX) | Annual Discount Price (UGX) |
|---|---|---|---|---|
| **Starter** | 50–200 pupils | 150,000 | 1,800,000 | 1,620,000 |
| **Growth** | 201–500 pupils | 280,000 | 3,360,000 | 3,024,000 |
| **Pro** | 501+ pupils | 450,000 | 5,400,000 | 4,860,000 |

**Pricing assumptions and rationale:**

- UGX 150,000/month (Starter) = approximately USD 40/month. A 150-pupil school collecting UGX 1,500 per pupil per term in fees generates UGX 675,000/term in fee revenue. The SaaS subscription is 7% of one month's term fee — within range for a product that automates reconciliation, reporting, and UNEB grading.
- UGX 280,000/month (Growth) = approximately USD 75/month. A 350-pupil school at UGX 2,000/term collects UGX 2,100,000/term. The subscription is 4% of one term's fee collection.
- UGX 450,000/month (Pro) = approximately USD 120/month. A 700-pupil school at UGX 3,000/term collects UGX 6,300,000/term. The subscription is 2% of one term's fee collection.
- These are launch prices. Pricing is reviewed annually. ARPU growth is expected as optional modules (Phase 2) are activated.

### 1.2 Revenue Mix Assumption

**Assumption F1:** School distribution across tiers at Year 3:

| Tier | % of Schools | Conservative (300 schools) | Optimistic (600 schools) |
|---|---|---|---|
| Starter | 55% | 165 | 330 |
| Growth | 35% | 105 | 210 |
| Pro | 10% | 30 | 60 |

**Blended ARPU calculation (conservative Year 3):**

$$ARPU = \frac{(165 \times 150{,}000) + (105 \times 280{,}000) + (30 \times 450{,}000)}{300}$$

$$ARPU = \frac{24{,}750{,}000 + 29{,}400{,}000 + 13{,}500{,}000}{300} = \frac{67{,}650{,}000}{300} = UGX\ 225{,}500/month$$

---

## 2. Revenue Projections

### 2.1 Conservative Scenario

**Assumption F2 (Conservative):** 50 schools at Phase 8 go-live (Year 1), 150 schools by Year 2, 300 schools by Year 3. Average school onboards at Starter tier; upgrades to Growth within 6 months.

| Year | Schools | Blended ARPU (UGX/mo) | Annual Revenue (UGX) | Annual Revenue (USD) |
|---|---|---|---|---|
| Year 1 | 50 | 175,000 | 105,000,000 | ~28,000 |
| Year 2 | 150 | 210,000 | 378,000,000 | ~100,800 |
| Year 3 | 300 | 225,500 | 811,800,000 | ~216,480 |

Year 1 ARPU is lower (50,000 below Year 3) because the school cohort is predominantly Starter-tier early adopters. ARPU rises as Phase 2 optional modules are activated and the Growth/Pro mix grows.

### 2.2 Optimistic Scenario

**Assumption F3 (Optimistic):** 100 schools at Year 1, 300 at Year 2, 600 at Year 3. Assumes faster word-of-mouth conversion within the SchoolPay school network.

| Year | Schools | Blended ARPU (UGX/mo) | Annual Revenue (UGX) | Annual Revenue (USD) |
|---|---|---|---|---|
| Year 1 | 100 | 175,000 | 210,000,000 | ~56,000 |
| Year 2 | 300 | 210,000 | 756,000,000 | ~201,600 |
| Year 3 | 600 | 225,500 | 1,623,600,000 | ~432,960 |

### 2.3 Revenue Formula

$$Revenue_{annual} = Schools \times ARPU_{monthly} \times 12$$

$$Year\ 3\ Conservative:\ 300 \times 225{,}500 \times 12 = UGX\ 811{,}800{,}000$$

$$Year\ 3\ Optimistic:\ 600 \times 225{,}500 \times 12 = UGX\ 1{,}623{,}600{,}000$$

---

## 3. Cost Assumptions

*All cost figures are estimates based on publicly available pricing as of March 2026. Actual costs depend on final vendor selection, negotiated rates, and usage volume.*

### 3.1 Infrastructure Costs

| Item | Phase 1–7 (VPS) (UGX/mo) | Phase 8+ (AWS ECS) (UGX/mo) | Notes |
|---|---|---|---|
| Server / compute | 450,000 | 1,500,000–3,750,000 | VPS ~USD 120/mo; ECS scales with usage |
| MySQL (managed) | Included in VPS | 750,000 | AWS RDS or equivalent |
| Redis (managed) | Included in VPS | 375,000 | ElastiCache or equivalent |
| AWS S3 + CloudFront | 75,000 | 375,000–750,000 | Scales with PDF storage volume |
| Cloudflare (DNS + WAF) | 75,000 | 75,000–375,000 | Pro plan |
| SSL / Let's Encrypt | 0 | 0 | Auto-renew; free |
| **Infrastructure subtotal** | **~600,000** | **~3,000,000–6,000,000** | At 300 schools, mid-range estimate |

### 3.2 Per-School Variable Costs (Communication)

| Item | Unit Cost | Usage Assumption | Cost/School/Month (UGX) |
|---|---|---|---|
| SMS (Africa's Talking) | UGX 65/SMS | 50 SMS/school/month (attendance alerts, fee reminders) | 3,250 |
| WhatsApp (Meta Business API) | ~UGX 40/conversation | 20 conversations/school/month | 800 |
| Email (Mailgun/Postmark) | ~UGX 0.4/email | 200 emails/school/month | 80 |
| Push notifications (FCM) | Free (Firebase free tier) | Unlimited | 0 |
| **Variable comms/school/month** | | | **~4,130** |

At 300 schools: UGX 4,130 × 300 = **UGX 1,239,000/month** in variable comms costs.

### 3.3 AI API Costs (Claude API)

**Assumption F4:** The Claude API (claude-sonnet-4-6) is used for predictive defaulter alerts, attendance pattern analysis, and natural-language report commentary. Estimated usage at 300-school scale:

- Average tokens per school per month: ~50,000 input + 10,000 output
- At Anthropic published rates (~USD 3/million input tokens, USD 15/million output tokens):
- Cost per school per month: ~USD 0.30 (UGX 1,125)
- At 300 schools: **UGX 337,500/month** (approximately)

### 3.4 Total Operating Cost Summary (Year 3, 300 Schools)

| Cost Category | Monthly (UGX) | Annual (UGX) |
|---|---|---|
| Infrastructure (Phase 8+ mid) | 4,500,000 | 54,000,000 |
| Variable communications | 1,239,000 | 14,868,000 |
| Claude API | 337,500 | 4,050,000 |
| Support / tooling (GitHub, monitoring, etc.) | 300,000 | 3,600,000 |
| **Total OpEx (Year 3)** | **~6,376,500** | **~76,518,000** |

### 3.5 Gross Margin

$$Gross\ Margin = \frac{Revenue - Variable\ Costs}{Revenue} \times 100\%$$

At Year 3 Conservative (Revenue = UGX 811,800,000; Variable Costs = UGX 76,518,000):

$$Gross\ Margin = \frac{811{,}800{,}000 - 76{,}518{,}000}{811{,}800{,}000} \times 100\% = 90.6\%$$

This is consistent with a multi-tenant SaaS on shared infrastructure — marginal cost per additional school is predominantly the variable communications and API cost (UGX ~5,255/month), well below the minimum ARPU of UGX 150,000.

---

## 4. Break-Even Analysis

**Assumption F5:** Fixed costs (Peter's time is currently sweat equity, excluded from Year 1 calculation). At Phase 8+ with AWS infrastructure:

$$Break\ Even\ Schools = \frac{Fixed\ Monthly\ Costs}{ARPU - Variable\ Cost\ Per\ School}$$

$$Break\ Even = \frac{4{,}800{,}000}{150{,}000 - 5{,}255} = \frac{4{,}800{,}000}{144{,}745} \approx 33\ schools$$

The business reaches cash-flow positive on infrastructure costs at approximately **33 Starter-tier schools**. At 50 schools (Year 1 conservative), the platform is cash-flow positive from go-live.

---

## 5. Assumptions Register

| ID | Assumption | Impact if Wrong |
|---|---|---|
| F1 | Tier distribution 55/35/10 | ARPU differs; adjust blended revenue calculation |
| F2 | Conservative adoption 50/150/300 | Core investment decision basis — downside is slower IRR |
| F3 | Optimistic adoption 100/300/600 | Upside scenario only |
| F4 | Claude API cost ~USD 0.30/school/month | Costs scale linearly; adjust if usage is higher |
| F5 | Peter's time excluded from Year 1 cost | Real economic cost is higher; included once team is hired |
| F6 | Exchange rate UGX 3,750 = USD 1 | USD-denominated costs (AWS, Claude) are exposed to UGX/USD movement |

[CONTEXT-GAP: No actual SchoolPay school count has been independently verified. If the true addressable baseline is materially different from ~11,000, adoption scenario timelines require adjustment.]


---

## AI Module Revenue Line

The AI Module is a direct new revenue stream for Academia Pro, sold as a monthly subscription on top of the core platform fee.

### Indicative AI Module Revenue

| AI Plan | Monthly Fee (UGX) | Target Adoption | Monthly Revenue |
|---|---|---|---|
| Starter | 50,000 | 40% of active schools | 50,000 × 0.40 × N schools |
| Growth | 200,000 | 20% of active schools | 200,000 × 0.20 × N schools |
| Enterprise | 800,000 | 5% of active schools | 800,000 × 0.05 × N schools |

**At 100 active schools:** ~65 on Starter (UGX 3.25M/mo) + ~20 on Growth (UGX 4M/mo) + ~5 on Enterprise (UGX 4M/mo) = approximately **UGX 11.25M/month** ($3,000/month) in AI add-on revenue.

**At 500 schools (24-month target):** AI module revenue alone exceeds UGX 50M/month ($13,000/month) at 40/20/5% adoption rates.

### Cost Structure

Raw AI token cost per school per month is $0.50–$3.00 depending on school size and feature usage. At 5–10× markup, the AI module is highly profitable at all plan tiers. The token budget ceiling per tenant controls Chwezi's maximum cost exposure even at full feature utilisation.

**Key financial controls:**
- Monthly budget ceiling enforced per tenant (`tenant_ai_modules.monthly_budget_ugx`).
- Token cost tracked in UGX at exchange rate at time of call (`ai_usage_log.cost_ugx`).
- Pre-aggregated monthly totals (`ai_usage_monthly`) enable real-time profitability monitoring by the Super Admin.

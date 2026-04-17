# Market Opportunity — Academia Pro

**Version:** 1.0
**Date:** 2026-03-28

*All market size figures are estimates based on publicly available MoES, SchoolPay, and regional education authority data. They are clearly marked as assumptions and are used for planning purposes only.*

---

## 1. Uganda Market

### 1.1 Total Registered Schools

**Assumption A1:** Uganda has approximately 25,000 registered primary and secondary schools as of the MoES 2023 annual census. This figure includes:

- ~15,000 registered primary schools (P1–P7)
- ~5,000 registered secondary schools (O-Level and A-Level)
- ~5,000 registered nursery/pre-primary, vocational, and special-needs institutions

The initial product scope targets primary and secondary schools only. The serviceable market is therefore approximately 20,000 institutions.

### 1.2 Addressable Baseline via SchoolPay

SchoolPay has approximately 11,000 Uganda schools on its payment platform (source: SchoolPay public statements and payment-landscape context). These schools already collect fees via MTN MoMo and Airtel Money through SchoolPay's infrastructure. They represent the highest-conversion segment because:

- They are already digitised for payments — the largest adoption barrier (changing payment habits) does not apply.
- Academia Pro integrates with SchoolPay in Phase 1 — these schools gain a full ERP layer on top of their existing payment setup with zero payment disruption.
- SchoolPay's ERP product is structurally immature, creating an upsell gap.

**Assumption A2:** Conversion target for the SchoolPay baseline:

| Year | Target Schools (Conservative) | Target Schools (Optimistic) | Penetration Rate (Conservative) |
|---|---|---|---|
| Year 1 (Phase 8 go-live) | 50 | 100 | 0.45% |
| Year 2 | 150 | 300 | 1.36% |
| Year 3 | 300 | 600 | 2.73% |

Even the Year 3 conservative target of 300 schools represents 2.7% of the SchoolPay-connected addressable baseline — a conservative conversion assumption for a product that directly targets SchoolPay schools.

### 1.3 School Size and Fee Volume

**Assumption A3:** Uganda school size distribution (private primary and secondary):

| School Tier | Pupil Range | Estimated % of Market |
|---|---|---|
| Small | 50–200 pupils | ~60% |
| Medium | 201–500 pupils | ~30% |
| Large | 501–1,000 pupils | ~8% |
| Enterprise | 1,000+ pupils | ~2% |

**Assumption A4:** Annual fee revenue per school (tuition only, excl. boarding and transport):

| School Tier | Estimated Annual Fee Revenue (UGX) |
|---|---|
| Small (150-pupil average) | UGX 90,000,000–180,000,000 |
| Medium (350-pupil average) | UGX 210,000,000–420,000,000 |
| Large (700-pupil average) | UGX 420,000,000–840,000,000 |

A SaaS subscription priced at UGX 150,000–400,000/month represents 0.1%–0.4% of annual fee revenue for a medium school — a price-to-value ratio that is commercially defensible.

### 1.4 SaaS Revenue Model

Academia Pro uses a per-school, tier-based subscription model. Pricing is denominated in UGX to eliminate currency risk for schools and to avoid the perception of a foreign-priced product.

Three subscription tiers are proposed (detailed financial model in Section 06):

- **Starter:** 50–200 pupils — covers standard modules
- **Growth:** 201–500 pupils — standard modules + optional add-ons
- **Pro:** 501+ pupils — all modules, priority support, custom branding

Revenue formula per cohort:

$$Revenue = Schools_{tier} \times ARPU_{tier} \times 12\ months$$

At Year 3 conservative (300 schools, blended ARPU UGX 230,000):

$$Revenue = 300 \times 230{,}000 \times 12 = UGX\ 828{,}000{,}000\ (\approx USD\ 220{,}000)$$

---

## 2. Pan-Africa Total Addressable Market

### 2.1 Regional School Counts

**Assumption A5:** Registered school counts by country (sources: respective Ministries of Education, UNESCO Institute for Statistics 2022–2023 data):

| Country | Registered Primary + Secondary Schools (Estimate) | Dominant Mobile Payment | Regulatory Curriculum |
|---|---|---|---|
| Uganda | ~20,000 | MTN MoMo, Airtel Money | UNEB (PLE, UCE, UACE) |
| Kenya | ~18,000 | M-Pesa (Safaricom) | KNEC (KCPE, KCSE) |
| Tanzania | ~18,000 | Airtel Tanzania, Tigo Pesa | NECTA |
| Nigeria | ~60,000+ | Paystack, Flutterwave | WAEC, NECO |
| Ghana | ~15,000 | MTN MoMo Ghana | WAEC |
| **Total TAM** | **~131,000** | | |

### 2.2 Pan-Africa TAM Narrative

The core SaaS infrastructure (multi-tenant architecture, React web app, Android apps, PHP/Laravel API) is country-agnostic by design. Country-specific requirements are isolated to data-driven profiles:
- Curriculum and grading engine (UNEB → KCSE → NECTA → WAEC)
- Payment gateway (SchoolPay/MTN MoMo → M-Pesa → Paystack/Flutterwave)
- Government integration format (EMIS → NEMIS → equivalent)
- Currency and locale (UGX → KES → TZS → NGN)

Each country's entry cost is therefore incremental, not a full rebuild.

**Assumption A6:** Pan-Africa addressable market narrative (planning estimate):

| Expansion Phase | Countries | Reachable Schools | Entry Timeline |
|---|---|---|---|
| Phase 1–8 | Uganda | ~20,000 | 2026–2027 |
| Phase 11 — East Africa | Kenya, Tanzania | ~36,000 additional | 2027–2028 |
| Phase 11 — West Africa | Nigeria, Ghana | ~75,000 additional | 2028–2029 |

A 2% penetration of the East Africa combined total (~56,000 schools) by end of Year 5 equals 1,120 schools. At a blended ARPU of KES 1,800/month (Kenya, equivalent purchasing power):

$$Revenue_{Kenya,Y5} = 500 \times 1{,}800 \times 12 = KES\ 10{,}800{,}000\ (\approx USD\ 83{,}000)$$

Combined with Uganda Year 5 revenue, the pan-Africa two-country scenario reaches approximately USD 300,000–500,000 ARR at conservative penetration rates, before Nigeria and Ghana are included.

### 2.3 Market Entry Assumptions

- **Kenya (Phase 11):** NEMIS integration and M-Pesa Daraja API are the two unlock requirements. M-Pesa has ~30 million registered users. School fee payment via M-Pesa is already standard practice. No payment behaviour change required.
- **Nigeria (Phase 11):** The largest school count (~60,000) but also the highest localisation complexity (federal vs. state curricula, multiple exam boards). Nigeria is a Year 3+ entry market after Uganda and Kenya are stable.
- **Tanzania:** NECTA curriculum and Airtel/Tigo payment rails. Similar structural profile to Uganda. Phase 11 entry alongside Kenya.

---

## 3. Key Assumptions Summary

| ID | Assumption | Basis |
|---|---|---|
| A1 | 25,000 Uganda registered schools | MoES 2023 estimate |
| A2 | SchoolPay baseline ~11,000 schools | SchoolPay public statements |
| A3 | 60% small / 30% medium / 10% large distribution | Domain research; no MoES breakdown available |
| A4 | Fee revenue per school as stated | Market research; not audited |
| A5 | Regional school counts as stated | UNESCO UIS 2022–2023 |
| A6 | 2% addressable penetration achievable by Year 5 | Conservative SaaS benchmark for vertical-specific platforms |

[CONTEXT-GAP: No independently audited MoES school count for Uganda primary + secondary has been confirmed in context files. A1 and A2 should be validated against the MoES EMIS published statistical abstract before the financial model is finalised.]

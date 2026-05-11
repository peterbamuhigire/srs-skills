# SaaS Metric & KPI Catalogue (Phase 01 reference)

Canonical SaaS metric library. Every PRD, business case, and monitoring spec must trace its KPIs to entries here. Source: Mersch, *Hacking SaaS* (2023); Walling, *SaaS Playbook* (2022); Cotton, *How to Run a SaaS Business*.

## A. Top-line revenue metrics

| Metric | Definition | Formula | Source system | Cadence |
|--------|------------|---------|---------------|---------|
| ACV | Annual Contract Value | sum of recurring revenue normalised to 12 mo | CRM / billing | per deal |
| TCV | Total Contract Value | ACV × contract term + non-recurring | CRM | per deal |
| ARR | Annual Recurring Revenue | sum of active subscription ACV | billing | monthly |
| MRR | Monthly Recurring Revenue | ARR / 12 | billing | monthly |
| CARR | Contracted ARR | ARR + signed-not-active | billing + CRM | monthly |
| CMRR | Committed MRR | MRR under term ≥ 1 mo | billing | monthly |
| Exposed ARR | ARR up for renewal in period | billing | per renewal cycle |
| New Bookings (ACV) | new-customer subscription ACV | CRM | weekly |
| Renewal Bookings (ACV) | renewed subscription ACV | CRM | monthly |
| Expansion Bookings | upsell + cross-sell ACV | CRM | monthly |
| Fast-follow Bookings | expansion within same quarter as initial | CRM | quarterly |
| Reactivation Bookings | ACV from re-acquired churned logos | CRM | monthly |
| Billings | invoiced amount | billing | monthly |

## B. Unit economics

| Metric | Definition | Formula | Cadence |
|--------|------------|---------|---------|
| Gross churn rate | ARR not renewing at renewal date | Σ churned ARR / Σ ARR up for renewal | monthly |
| Renewal rate | renewed / up for renewal | | monthly |
| Expansion rate | expansion ARR / existing ARR | | monthly |
| Net churn rate | Gross churn − Expansion (negative is good) | | monthly |
| DBNR / NDR | (start ARR + expansion − churn − contraction) / start ARR | | monthly |
| CAC | new-customer S&M spend / new customers | | monthly |
| CAC payback | CAC / gross-margin-adjusted MRR | months | per cohort |
| LTV | (ARPA × gross margin) / gross churn rate | | per cohort |
| LTV : CAC | LTV / CAC | target ≥ 3× | per cohort |

## C. Financial / valuation

| Metric | Definition | Cadence |
|--------|------------|---------|
| Subscription gross margin | (subscription revenue − COR) / subscription revenue, target ≥ 75% | quarterly |
| Deferred revenue | billed but not yet recognised | monthly |
| RPO | contracted not yet recognised | monthly |
| Free Cash Flow | CF from operations + CF for investing | monthly |
| Rule of 40 | growth rate (%) + FCF margin (%), target ≥ 40 | quarterly |
| Magic Number | (4 × ΔQARR) / S&M expense last quarter, target ≥ 0.75 | quarterly |
| Sales Efficiency | New ACV / S&M in same period, target ≥ 0.5 | quarterly |
| Burn multiple | net burn / net new ARR | monthly |

## D. Customer success

| Metric | Definition | Cadence |
|--------|------------|---------|
| Time-to-Go-Live (TGL) | days from signing to go-live | per deal |
| Time-to-Value (TTV) | days to first value milestone | per cohort |
| Time-to-Grow (TTG) | days to first expansion | per cohort |
| New feature adoption | % users adopting feature in N days | per feature |
| Activation rate | % users completing aha-moment | per cohort |
| Aha-moment | product-specific event marking first perceived value | per product |
| Customer Health Score | composite (usage, engagement, support, NPS, sentiment) | weekly |
| NPS | promoters − detractors (%) | quarterly |
| CSAT | satisfaction with last interaction | per ticket |

## E. SaaS support & operations

| Metric | Definition | Cadence |
|--------|------------|---------|
| Per-tenant gross margin | tenant revenue − tenant infra cost − support allocation | monthly |
| Per-tier availability | per SLO doc | monthly |
| First-response time | per support tier | per ticket |
| Resolution time | per severity | per ticket |
| Error-budget burn | per SLO doc | weekly |

## F. Marketing / funnel (per Garbugli)

| Metric | Definition |
|--------|------------|
| Send volume | emails sent |
| Open rate | opens / delivered |
| Click rate | clicks / opens |
| Goal completion rate | goal events / opens |
| Reply rate | replies / sent |
| Delivery rate | delivered / sent |
| Activation cohort retention | retention by signup cohort |

## Usage

When generating a PRD or business case, the engine MUST select at minimum: ARR target, MRR target, CAC payback target, gross retention floor, net retention target, Rule of 40 trajectory, activation rate target, and TTV target. Every selected metric MUST cite this catalogue.

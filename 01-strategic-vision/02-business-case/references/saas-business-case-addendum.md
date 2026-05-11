# SaaS Business Case Addendum

Use this addendum when the project is a SaaS. It supplements the generic `02-business-case` skill with SaaS-economic structure sourced from Mersch (*Hacking SaaS*) and Cotton (*How to Run a SaaS Business*).

## A. SaaS revenue & cost model

Required model rows (in addition to standard NPV / ROI):

| Row | Definition | Source |
|-----|------------|--------|
| New ARR / period | new-customer subscription ACV | bookings forecast |
| Expansion ARR / period | upsell + cross-sell ARR | retention model |
| Churned ARR / period | lost ARR | retention model |
| Net new ARR / period | New + Expansion − Churn | computed |
| Beginning ARR | end-of-prior period | running |
| Ending ARR | begin + Net new | running |

Project ARR over 36 months minimum.

## B. Unit economics — mandatory fields

| Field | Target |
|-------|--------|
| CAC | $<value> per new logo |
| CAC payback (months) | ≤ 12 (SMB) / ≤ 18 (mid-market) / ≤ 24 (enterprise) |
| Gross retention | ≥ 90% (SMB) / ≥ 95% (mid-market+) |
| Net retention (DBNR/NDR) | ≥ 110% target; ≥ 120% best-in-class |
| LTV : CAC | ≥ 3× |
| Gross margin | ≥ 75% |

## C. Rule of 40 trajectory

Plot the modelled `growth % + FCF margin %` over 36 months. Show when the company is expected to cross 40.

## D. Cohort retention curve

Provide a stylised retention curve by cohort (month-0 = 100%, retained-MRR-% by month-N). State assumptions and source comparables.

## E. CAC payback math

```
CAC payback months = CAC / (ARPA × gross_margin / 12)
```

Compute and present per segment.

## F. Magic Number / Sales Efficiency target

```
Magic Number = 4 × ΔQ-ARR / S&M(prior Q)
Sales Efficiency = New ACV / S&M(same period)
```

Target Magic Number ≥ 0.75 sustained; > 1.0 indicates strong investment efficiency.

## G. Pricing assumptions cross-link

Cite the `Pricing_And_Packaging_Spec.md` and use its tier mix to derive ARPA.

## H. Go / No-go gates

In addition to the generic NPV gate, require:

- Modelled CAC payback within band.
- Modelled net retention ≥ 100% by month 18.
- Modelled gross margin ≥ 70% by month 24.

Fail the gate if any of these is not credible.

## I. Sensitivity analysis (mandatory)

Run sensitivities on: CAC ±25%, gross retention ±5 pp, conversion rate ±25%, ARPA ±20%. Show ARR @ M36 and break-even month under each scenario.

## J. Reference

- Hacking SaaS (Mersch 2023) Ch.3-6.
- Cotton (2020) Essay 4 (Runway to $100M).
- Mersch Ch.7-14 (segment-specific financial profiles).
- The SaaS Metric & KPI Catalogue (Phase 01 reference).

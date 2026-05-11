# SaaS PRD Addendum

Supplements the generic `01-prd-generation` skill when the project is a SaaS.

## A. Mandatory PRD sections for SaaS

1. **ICP & target persona** — segment, firmographics, technographics, buying committee, trigger events.
2. **Pricing & packaging summary** — link to `Pricing_And_Packaging_Spec.md`; state value metric, tiers, expansion mechanics.
3. **Tenancy & isolation expectation** — at minimum a target pattern per major service; cross-link to the multi-tenancy architecture spec.
4. **Tier-mapped feature matrix** — every feature is tagged with the tier(s) at which it is available.
5. **KPI targets traceable to the SaaS Metric Catalogue** — pick at minimum: activation rate, gross retention, net retention, CAC payback, time-to-value, expansion-ARR target.
6. **Onboarding journey expectation** — aha-moment, target activation rate.
7. **Trust & compliance posture** — required attestations (SOC 2 / ISO 27001 / GDPR / vertical regs).
8. **Risks specific to SaaS** — churn, scaling-without-margin, regulatory cliff, single-channel-dependency, isolation-incident reputational risk.

## B. Feature triage rules (Walling 3Q)

Every feature in scope answers:

1. Use case (problem solved)?
2. Estimated % of customers using it?
3. Vision fit?

Decision log appended to the PRD.

## C. Competitive signal monitoring (Walling)

State which of these signals will be monitored and what triggers a response:

- High-level updates (announcements in industry press).
- Deals lost to a specific competitor.
- Low-level details (employees moving, social signals).
- Funding events.

## D. Anti-moats (Walling)

The PRD must NOT rely on "unique features" as a moat. Moat candidates are referred to `Moat_And_Defensibility_Plan.md`.

## E. Cross-links

- `Pricing_And_Packaging_Spec.md`
- `Multi_Tenancy_Architecture_Spec.md`
- `Moat_And_Defensibility_Plan.md`
- `MVP_Scoping_Doc.md` (for early-stage)
- `Onboarding_Journey_Spec.md`
- SaaS Metric & KPI Catalogue (Phase 01 reference)

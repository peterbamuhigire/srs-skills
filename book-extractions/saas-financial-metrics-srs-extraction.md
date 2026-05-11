# Hacking SaaS (Eric Mersch) — SRS-Engine Extraction

**Source:** Eric Mersch, *Hacking SaaS: An Insider's Guide to Managing Software Business Success*, 2023. (Despite the filename `hacking-saas.md`, this book is a CFO's financial-and-operating-metrics handbook.)

**Lens:** Which SDLC documents capture the SaaS financial, metering, billing, revenue-recognition, and KPI surfaces this book defines?

## One-line takeaway

A SaaS business runs on a **specific instrumented metric stack** — ARR, MRR, CARR, bookings (new/renewal/expansion), churn (gross/net), CAC, CAC payback, LTV, Rule of 40, Magic Number, DBNR — and the SaaS-grade SRS/PRD/business-case must define, source, and govern every one of these as **measurable system requirements**, not as marketing language.

## Distinctive documentation surface

### 1. SaaS metric catalogue

The book is itself a catalogue. The engine must own a **SaaS Metric & KPI Catalogue** that every PRD, business case, monitoring spec, and dashboard requirement traces to:

- Top-line: Bookings (new subscription / renewal / cross-sell / upsell / fast-follow / reactivation), Billings, ACV, TCV, ARR, CARR, MRR, CMRR, Exposed ARR.
- Unit economics: Gross/Net Churn, Renewal Rate, Expansion Rate, DBNR/NDR, CAC, CAC Payback, LTV, LTV:CAC.
- Financial: Subscription Gross Margin, Deferred Revenue, RPO, FCF, Rule of 40, Magic Number, Sales Efficiency.
- Customer-success: TGL, TTV, TTG, New Feature Adoption.
- Cost-of-revenue buckets: hosting, third-party SW, support, customer success allocation.

### 2. Revenue recognition spec

ASC 606 / IFRS-aligned revenue-recognition rules drive: contract terms, milestones, deferred revenue, RPO. The engine should produce a **Revenue-Recognition Specification** — a Phase 02 cross-cutting NFR/constraint document. Many SaaS bugs are billing bugs; the SRS must specify when revenue is recognized vs deferred.

### 3. Cost-of-revenue / unit-economics spec

A doc that classifies every cost line as direct vs indirect and ties it to a service tier. Drives pricing decisions and per-tenant cost attribution.

### 4. GTM-segment-specific model docs

Different financial profiles for Enterprise, Mid-Market/SMB, B2C, Horizontal vs Vertical SaaS. The engine should produce a **GTM Segment Profile** document picking one of these archetypes and specifying its CAC payback, sales-cycle, expansion mechanics, and retention floor.

### 5. Metering & billing requirements

Implicit but critical: every metric in the catalogue requires events to be captured. The engine must produce a **Metering & Billing SRS** — what events are emitted, with what granularity, with what tenant-context, into what bus, with what retention. (Cross-cuts Phase 02 + Phase 03.)

### 6. Financial-reporting integration spec

Bookings, billings, deferred-revenue need to feed Finance/ERP. The engine should produce a **Finance Integration Spec** — accounting-period rules, export schedules, audit trail.

## Documentation patterns the book recommends

- Every metric must have a **definition**, a **formula**, a **source system**, a **reporting cadence**, and an **owner**. SRS-equivalent rigor.
- "If you can't measure it, you don't know it" — every business decision in SaaS is downstream of these metrics; the SRS must enumerate them as first-class requirements.
- Benchmark every metric externally — comparison thresholds in the doc.

## Implications for the SDLC-Docs-Engine

1. Add Phase 02 skill **`08-saas-billing-and-metering-spec`** — events, granularity, propagation, tenant-context, retention, finance handoff.
2. Add Phase 01 reference **`saas-metric-and-kpi-catalogue.md`** that all PRDs/business cases must cite.
3. Add Phase 02 reference **`saas-revenue-recognition-spec-template.md`** that every billing-touching project must populate.
4. Enhance `01-strategic-vision/02-business-case` with mandatory SaaS-metrics section (ARR plan, CAC payback target, retention floor, Rule-of-40 trajectory).
5. Enhance `06-deployment-operations/03-monitoring-setup` with mandatory tenant-scoped + metric-catalogue dashboards.

## Source mapping

- Ch.3 Top-Line Metrics → Metric Catalogue + Bookings spec.
- Ch.4 Unit Economics → CAC, LTV, Churn formulas.
- Ch.5 Financial Metrics → Rev-Rec + Deferred Revenue + Rule of 40.
- Ch.7-9 Enterprise / 10-11 SMB / 12-14 B2C → GTM Segment Profile.
- Ch.15-16 Horizontal vs Vertical → Vertical-SaaS positioning addendum.

# How to Run a SaaS Business (Ben Cotton) — SRS-Engine Extraction

**Source:** Ben Cotton, *How to Run a SaaS Business: Lessons Learned from a Trio of Billion Dollar Companies (HubSpot, Indeed, Automation Anywhere).*

**Lens:** Which SDLC documents must the engine produce to capture the operational, financial, brand, and revenue-engine concerns this book identifies?

## One-line takeaway

A SaaS business is run by an interlocking system of **published pricing, brand investment, sales-and-marketing alignment, churn-control mechanisms, and customer-success operations** — and every one of those concerns generates a documentation surface (PRD addenda, pricing spec, lifecycle journey, support model, churn-control plan) that a pure software SRS does not cover.

## Distinctive documentation surface

### 1. Rules-to-run-by document (Essay 1)

Cotton opens with operating principles every SaaS company should make explicit (publish pricing, invest in brand, never have one sales rep, etc.). The engine should produce a **SaaS Operating Principles Charter** — a Phase 01 strategic-vision artefact that captures the operating-model commitments executives must hold.

### 2. Published pricing as a documentation artefact (Essay 5)

Cotton argues pricing must be published. This implies the engine must produce:

- **Pricing & Packaging Specification** — tier definitions, what's in each tier, per-seat vs per-usage, expansion mechanics, public price page copy, enterprise contact-us path.
- **Discount & Concession Policy** — who can give what discount, approval thresholds, audit trail.

### 3. Brand-investment doc (Essay 3)

Brand is treated as a measurable investment, not a soft asset. The engine should produce a **Brand & Authority Investment Plan** — content cadence, owned channels, distribution, success metrics. (Phase 01.)

### 4. Sales-and-marketing engine documentation (Essays 7, 8)

The book treats sales-and-marketing as a single instrumented engine. Documentation surface:

- **Marketing-Sales SLA / Service Definition** — what marketing hands to sales, when, with what data; what sales does in return.
- **Lead-handoff and qualification spec** (BANT, MEDDIC, etc.).
- **Sales team capacity / ramp plan** — quotas, ramp, coverage. (Phase 01 / Phase 08.)

### 5. Churn-control as a system (Essay 9)

Churn is a "quiet killer." The engine should produce:

- **Churn Reduction Plan** — leading-indicator metrics, intervention playbooks at each customer-lifecycle stage, retention experiments.
- **Customer Health Score Spec** — inputs, weights, thresholds, actions per band.

### 6. Runway-to-$100M plan (Essay 4)

Documentation of the growth model: cohorts, expansion revenue assumptions, CAC/LTV envelope, retention floor, the financial path. The engine should produce a **SaaS Growth & Financial Path** document distinct from a generic business case. (Phase 01.)

### 7. Marketing arbitrage / paid acquisition (Essay 6)

A **Paid Acquisition Spec** with channel mix, CAC bands per channel, payback envelope, and experiment plan.

## Documentation patterns the book recommends

- Publish, don't hide (pricing must be a *document*, not a sales-call surprise).
- Quantify everything (every operating principle has a metric).
- Treat brand, marketing, and sales as one revenue engine with a shared SLA.
- Churn-control is a *plan* with intervention playbooks, not a hope.

## Implications for the SDLC-Docs-Engine

1. Add Phase 01 skill **`08-saas-pricing-and-packaging-spec`** (Phase 01 + 02 spans).
2. Add Phase 01 skill **`09-saas-operating-principles-charter`** (lightweight, executive-facing).
3. Add Phase 08 skill **`05-saas-customer-success-playbook`** (covers churn-control plan, health-score spec, intervention playbooks).
4. Add cross-cutting template **`saas-pricing-and-packaging-spec-template.md`**.
5. Enhance `01-strategic-vision/02-business-case` with a SaaS-economics addendum (cohort, CAC, LTV, payback, Rule of 40, runway-to-$100M).

## Source mapping

- Essay 1 (rules to run by) → SaaS Operating Principles Charter.
- Essays 3, 6 → Brand & Paid Acquisition Plan addenda.
- Essay 5 → Pricing & Packaging Specification skill.
- Essays 7-8 → Sales-Marketing SLA and capacity plan.
- Essay 9 → Customer Success / Churn-control playbook.
- Essay 4 → Business-case SaaS-economics addendum.

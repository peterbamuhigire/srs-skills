# SaaS SDLC-Docs Skills Audit — May 2026

Walks the existing engine catalogue phase by phase, contrasts it with what the seven SaaS books reveal a world-class SaaS documentation pipeline should contain, and emits a prioritised gap list. Source extractions live in this same directory (`*-srs-extraction.md`).

Convention: skill IDs follow the existing numbered pattern inside each phase. New skill numbering starts at the next free slot in each phase.

## Summary of new artefacts created this session

- **New skills (12):** see "New skills" table below.
- **Enhanced skills (5):** see "Enhancements" table below.
- **Cross-cutting templates (14):** see "Templates / reference files" table below.

---

## Phase 01 — Strategic Vision

### Existing

01-prd-generation · 02-business-case · 03-vision-statement · 04-lean-canvas · 05-system-overview · 06-ai-economic-value-brief · 07-premium-product-positioning.

### Gaps the books reveal

| # | Gap | Source |
|---|-----|--------|
| 1 | No SaaS-specific MVP scoping / stair-step doc | Walling Ch.1-3 |
| 2 | No moat & defensibility plan | Walling Ch.4-5 |
| 3 | No pricing & packaging spec (Phase 01/02 boundary) | Walling Ch.7-8 + Cotton Essay 5 |
| 4 | No SaaS operating-principles charter | Cotton Essays 1-2 |
| 5 | No SaaS metric-and-KPI catalogue baked into PRD | Mersch Ch.3-5 |
| 6 | Business case lacks SaaS-economics structure (ARR plan, CAC payback, Rule of 40) | Mersch + Cotton |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `10-saas-mvp-scoping-doc` | `01-strategic-vision/10-saas-mvp-scoping-doc/` | MVP + stair-step scope, escape-velocity thresholds, feature-triage decision log |
| `11-saas-moat-and-defensibility-plan` | `01-strategic-vision/11-saas-moat-and-defensibility-plan/` | Moat taxonomy, false-moat traps, defensibility roadmap |
| `12-saas-pricing-and-packaging-spec` | `01-strategic-vision/12-saas-pricing-and-packaging-spec/` | Tiers, value metric, expansion mechanics, grandfathering, public price page contract |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `02-business-case` | SaaS-economics addendum (ARR plan, CAC payback target, gross/net retention floor, Rule-of-40 trajectory) via `references/saas-business-case-addendum.md` |
| `01-prd-generation` | Feature-triage decision-log addendum + KPI-catalogue traceability via `references/saas-prd-addendum.md` |

### Cross-cutting templates dropped in Phase 01

- `references/saas-metric-and-kpi-catalogue.md`
- `references/saas-pricing-and-packaging-spec-template.md`
- `references/saas-operating-principles-charter.md`

---

## Phase 02 — Requirements Engineering

### Existing

waterfall/ (8-skill IEEE 830 SRS pipeline) · agile/ (4 skills) · fundamentals · hybrid · 11-experience-mapping-requirements · 12-service-blueprint-requirements.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No billing-and-metering SRS (events, granularity, tenant-context, retention) | Mersch + Golding Ch.2 |
| 2 | No tenancy decision driving NFRs | Golding Ch.2-3 |
| 3 | No SaaS NFR catalogue (tenant isolation SLOs, noisy-neighbor caps, blast radius) | Golding Ch.2-3 |
| 4 | No revenue-recognition / ASC 606 spec | Mersch Ch.5 |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `13-saas-billing-and-metering-spec` | `02-requirements-engineering/13-saas-billing-and-metering-spec/` | Event catalogue, granularity, tenant context, propagation bus, retention, ERP/finance handoff, rev-rec rules |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `waterfall/07-attribute-mapping` | Reference `references/saas-nfr-catalog.md` enumerating SaaS-distinctive NFR families |

### Cross-cutting templates dropped in Phase 02

- `references/saas-nfr-catalog.md`
- `references/saas-billing-and-metering-srs-template.md`
- `references/saas-revenue-recognition-spec-template.md`

---

## Phase 03 — Design Documentation

### Existing

01-high-level-design · 02-low-level-design · 03-api-specification · 04-database-design · 05-ux-specification · 06-infrastructure-design · 07-iot-system-design · 08-engineering-strategy-brief · 09-ux-content-and-form-specification.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No multi-tenancy architecture spec (two-plane + tenancy-pattern per microservice) | Golding Ch.2-3 entire |
| 2 | HLD does not enforce SaaS mode (control plane vs application plane, tenant context propagation, isolation strategy) | Golding Ch.2 |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `10-saas-multi-tenancy-architecture-spec` | `03-design-documentation/10-saas-multi-tenancy-architecture-spec/` | Two-plane decomposition (control / application), per-microservice tenancy-pattern matrix (silo / pool / mixed / pod / VPC-per-tenant), tenant-context spec, isolation strategy, ADR seeds |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `01-high-level-design` | Reference `references/saas-hld-mode.md` invoked when project is SaaS — adds two-plane decomposition, tenant context section, tenancy-pattern table, isolation strategy section |

### Cross-cutting templates dropped in Phase 03

- `references/saas-tenancy-decision-template.md`

---

## Phase 04 — Development Artifacts

### Existing

01-technical-specification · 02-coding-guidelines · 03-dev-environment-setup · 04-contribution-guide.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No multi-tenant coding-guidelines addendum (tenant context propagation, tenant-scoped logging, fail-safe on missing tenant) | Golding Ch.2 |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `02-coding-guidelines` | Reference `references/saas-multi-tenant-coding-guidelines-addendum.md` covering tenant-context propagation rules, tenant-scoped logging, isolation enforcement at the code layer, audit logging of cross-tenant attempts |

---

## Phase 05 — Testing Documentation

### Existing

01-test-strategy · 02-test-plan · 03-test-report.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No SaaS-specific test additions (isolation tests, noisy-neighbor tests, tenant-context propagation tests, billing-event tests, churn-prevention regression) | Golding + Mersch |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `01-test-strategy` | Reference `references/saas-test-strategy-addendum.md` enumerating mandatory SaaS test families: tenant-isolation tests, cross-tenant-access penetration test, noisy-neighbor load test, tenant-context propagation test, billing-event correctness test, dunning/churn-recovery test |

---

## Phase 06 — Deployment & Operations

### Existing

01-deployment-guide · 02-runbook · 03-monitoring-setup · 04-infrastructure-docs · 05-go-live-readiness · 06-customer-adoption-and-support-plan.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No tenant-lifecycle runbook (provision / tier-change / suspend / offboard / delete) | Golding Ch.2 + GDPR |
| 2 | No SaaS SLO & error-budget doc (per-tier SLOs, error budgets, freeze rules) | SRE + Golding tiering |
| 3 | Monitoring-setup does not enforce per-tenant + KPI-catalogue dashboards | Mersch Ch.3-6 |
| 4 | No incident-response & postmortem template tuned for SaaS-tenant-impact reporting | Golding Ch.2 blast radius |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `07-saas-tenant-lifecycle-runbook` | `06-deployment-operations/07-saas-tenant-lifecycle-runbook/` | Provisioning, tier change, suspension, offboarding, data export, hard delete with retention obligations and audit trail |
| `08-saas-slo-and-error-budget-doc` | `06-deployment-operations/08-saas-slo-and-error-budget-doc/` | Per-tier SLOs, error-budget math, burn-rate alerts, freeze rules, customer-facing SLA mapping |
| `09-saas-incident-response-and-postmortem` | `06-deployment-operations/09-saas-incident-response-and-postmortem/` | SaaS-tuned severity (tenant-scope vs platform-scope), blast-radius reporting, customer-comms templates, blameless postmortem template |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `03-monitoring-setup` | Reference `references/saas-monitoring-addendum.md` mandating per-tenant dashboards, KPI-catalogue dashboards, control-plane vs application-plane separation |
| `02-runbook` | Cross-link to `07-saas-tenant-lifecycle-runbook` so the generic runbook hands off to SaaS-tenant-specific playbooks |

### Cross-cutting templates dropped in Phase 06

- `references/saas-tenant-lifecycle-runbook-template.md`
- `references/saas-slo-and-error-budget-template.md`
- `references/saas-incident-response-and-postmortem-template.md`

---

## Phase 07 — Agile Artifacts

### Existing

01-sprint-planning · 02-definition-of-done · 03-definition-of-ready · 04-retrospective-template.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No growth-experiment / A-B-test design doc | Garbugli + Walling + Mersch |
| 2 | DoD does not enforce SaaS hygiene (tenant-context test, billing event emitted, isolation regression) | Golding |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `05-saas-growth-experiment-doc` | `07-agile-artifacts/05-saas-growth-experiment-doc/` | Hypothesis, metric, segment, MDE, duration, stop rule, post-mortem |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `02-definition-of-done` | Reference `references/saas-dod-addendum.md` — mandatory SaaS-DoD items (tenant-context test, billing-event emission test, per-tenant log, isolation regression green) |

---

## Phase 08 — End-User Documentation

### Existing

01-user-manual · 02-installation-guide · 03-faq · 04-release-notes.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No customer-success playbook (health score, churn-prevention plays, expansion plays) | Cotton Essay 9 |
| 2 | No onboarding-journey spec mapping product activation to email/in-app/push | Garbugli + Walling |
| 3 | No lifecycle email strategy doc | Garbugli entire |
| 4 | No sales-enablement doc pack (ICP, methodology, discovery script, demo script, battlecards, closing playbook) | Winning by Design two volumes |
| 5 | No discovery framework spec (SPI/TALKER) | WbD Fundamentals |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `05-saas-customer-success-playbook` | `08-end-user-documentation/05-saas-customer-success-playbook/` | Health score, intervention plays, expansion plays, dunning plays, churn-reduction plan |
| `06-saas-onboarding-journey-spec` | `08-end-user-documentation/06-saas-onboarding-journey-spec/` | Activation milestones, channel orchestration, KPI thresholds |
| `07-saas-lifecycle-email-strategy-doc` | `08-end-user-documentation/07-saas-lifecycle-email-strategy-doc/` | Lifecycle map, per-stage campaigns, pre-send QA checklist, measurement |
| `08-saas-sales-enablement-doc-pack` | `08-end-user-documentation/08-saas-sales-enablement-doc-pack/` | ICP, sales methodology selection, discovery meeting script, demo script, battlecards, closing playbook |

### Cross-cutting templates dropped in Phase 08

- `references/saas-customer-success-playbook-template.md`
- `references/saas-onboarding-journey-spec-template.md`
- `references/saas-lifecycle-email-strategy-doc-template.md`
- `references/saas-sales-enablement-doc-pack-template.md`
- `references/saas-value-quantification-worksheet.md`

---

## Phase 09 — Governance & Compliance

### Existing

01-traceability-matrix · 02-audit-report · 03-compliance-documentation · 04-risk-assessment · 05-architecture-decision-records · 05-formal-review-gates · 06-CCB-charter · 06-change-impact-analysis · 07-baseline-delta · 08-waiver-management · 09-sign-off-ledger · 10-evidence-pack-builder.

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No tenant-data-isolation evidence pack | Golding Ch.2 |
| 2 | No trust-center document pack (security overview, compliance attestations, sub-processor list, DPA template) | SOC2/ISO/GDPR conventions |
| 3 | No DPA / privacy doc set (DPA, sub-processor register, ROPA, breach-notification SLA) | GDPR/POPIA |
| 4 | No SaaS-tenancy ADR catalogue (silo-vs-pool, freemium-yes/no, raise-prices, whitelabel, vertical-expansion) | Golding + Walling |

### New skills created

| Skill | Path | Purpose |
|-------|------|---------|
| `11-saas-data-isolation-evidence-pack` | `09-governance-compliance/11-saas-data-isolation-evidence-pack/` | Evidence at each layer (network, compute, storage, IAM, code path), control mapping, test artefacts, attestation memo |
| `12-saas-trust-center-document-pack` | `09-governance-compliance/12-saas-trust-center-document-pack/` | Public security overview, compliance attestations, sub-processor list, DPA template, status-page commitment |
| `13-saas-dpa-and-privacy-doc-set` | `09-governance-compliance/13-saas-dpa-and-privacy-doc-set/` | DPA, sub-processor register, ROPA, breach-notification SLA, retention schedule |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `05-architecture-decision-records` | Reference `references/saas-adr-catalogue.md` with required SaaS ADR families (tenancy-model-per-service, freemium, pricing-raise, whitelabel, vertical-expansion, sub-processor, data-residency) |

### Cross-cutting templates dropped in Phase 09

- `references/saas-data-isolation-evidence-pack-template.md`
- `references/saas-trust-center-document-pack-template.md`
- `references/saas-dpa-and-privacy-doc-templates.md`
- `references/saas-adr-catalogue.md`

---

## Cross-cutting reference files (full list)

See `references/saas-*` directories inside each phase. Master list of templates added:

1. `saas-tenancy-decision-template.md` (Phase 03)
2. `saas-nfr-catalog.md` (Phase 02)
3. `saas-slo-and-error-budget-template.md` (Phase 06)
4. `saas-pricing-and-packaging-spec-template.md` (Phase 01)
5. `saas-billing-and-metering-srs-template.md` (Phase 02)
6. `saas-revenue-recognition-spec-template.md` (Phase 02)
7. `saas-data-isolation-evidence-pack-template.md` (Phase 09)
8. `saas-tenant-lifecycle-runbook-template.md` (Phase 06)
9. `saas-trust-center-document-pack-template.md` (Phase 09)
10. `saas-dpa-and-privacy-doc-templates.md` (Phase 09)
11. `saas-incident-response-and-postmortem-template.md` (Phase 06)
12. `saas-customer-success-playbook-template.md` (Phase 08)
13. `saas-onboarding-journey-spec-template.md` (Phase 08)
14. `saas-lifecycle-email-strategy-doc-template.md` (Phase 08)
15. `saas-sales-enablement-doc-pack-template.md` (Phase 08)
16. `saas-metric-and-kpi-catalogue.md` (Phase 01)
17. `saas-operating-principles-charter.md` (Phase 01)
18. `saas-adr-catalogue.md` (Phase 09)
19. `saas-value-quantification-worksheet.md` (Phase 08)

---

## Open gaps recommended for follow-up sessions

- **AI-feature SaaS docs** — model-card, evaluation harness spec, hallucination-control SLO, prompt-injection threat model (LLM-SaaS distinctive). Recommend dedicated session.
- **Vertical-SaaS regulatory packs** — fintech (PCI-DSS), health (HIPAA), insurance (NAIC). Recommend domain-specific session.
- **FinOps for multi-tenant** — per-tenant cost attribution dashboards, gross-margin instrumentation, savings-plan optimisation docs. Recommend a "SaaS FinOps" session.
- **Marketplace / app-store ecosystem docs** — partner program, public API contract, revenue share, marketplace listing pack.
- **Customer-contract templates** — MSA, order form, SLA, DPA combined into a unified contract doc pack. (Beyond docs-engine scope; legal-engine handoff.)
- **Multi-region & data-residency** runbook (entitled tenants in EU/UK/US/APAC).
- **Tenant migration playbooks** — silo→pool, pool→pod, pool→silo migrations.

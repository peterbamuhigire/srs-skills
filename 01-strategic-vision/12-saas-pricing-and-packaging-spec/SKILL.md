---
name: 12-saas-pricing-and-packaging-spec
description: Use when a SaaS product needs testable tiers, a value metric, feature gates, expansion mechanics, freemium decision, grandfathering and price-change policy; use business-case for investment viability and PRD generation for feature requirements.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# SaaS Pricing & Packaging Spec Skill
<!-- dual-compat-start -->
## Use When

- Commercial and product owners must turn buyer value and cost-to-serve into enforceable packaging rules.

## Do Not Use When

- Do not use to guess prices without customer, willingness-to-pay or unit-cost evidence, or to implement billing architecture.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| ICP, buyer value and willingness-to-pay evidence | Research, sales and product owners | Required | Return hypotheses and a research plan if evidence is absent. |
| Feature entitlements and cost-to-serve | PRD, finance and operations | Required | Block package approval where margin or entitlement ownership is unknown. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the SaaS Pricing and Packaging Specification through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the SaaS Pricing and Packaging Specification to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| SaaS Pricing and Packaging Specification | Product, sales, finance, billing and web teams | Tiers, value metric, entitlements, upgrade/downgrade, public claims and change policies agree and are testable. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified SaaS Pricing and Packaging Specification draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Metric tracks customer value and scales predictably | Use as the primary value metric | Expansion is understandable |
| Metric is internal cost or easy to game | Reject or pair with a guardrail | Pricing punishes normal use |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Copying a competitor's three tiers. Fix: derive packages from buyer jobs and willingness to pay.
- Using seats when value does not scale by user. Fix: test a value-correlated metric.
- Hiding material limits from the price page. Fix: align public claims with entitlement rules.
- Offering freemium without an acquisition and conversion thesis. Fix: document thresholds or reject it.
- Ignoring grandfathering and downgrade effects. Fix: specify lifecycle and communication rules.

## References

- [Pricing template](references/saas-pricing-and-packaging-spec-template.md)
- [AI tier guidance](references/ai-tier-guidance.md)
<!-- dual-compat-end -->




## Overview

Generates the SaaS pricing & packaging specification, sourced from Walling (Pricing chapters), Cotton (publish your pricing), and Mersch (unit economics).

## Core Instructions

### Step 1: Choose the value metric

The value metric is the unit on which the customer's payment scales. It must grow with the customer's value extraction. Candidates: seats, API calls, GB stored, transactions processed, MAUs, contacts in CRM, video minutes recorded, properties managed.

State the chosen value metric and the rejection reasons for the runner-up.

### Step 2: Define tiers

Recommended 3-4 public tiers + 1 enterprise (contact-us):

| Tier | Price/mo | Value-metric units included | Key features | Support | SLA |
|------|----------|------------------------------|--------------|---------|-----|
| Free / Indie | $0 / $29 | small | core | community / NBD | none / 99.5% |
| Pro | $99 | medium | + collaboration | email 24h | 99.9% |
| Business / Studio | $299 | large | + integrations + SSO | priority chat | 99.95% |
| Enterprise | contact | unlimited | + dedicated infra, SSO, audit, custom DPA | named CSM, 15 min SEV1 | 99.99% |

### Step 3: Feature gates

Server-side gating only. Each gate evaluates `tenant.tier` from the signed context. Document the gate inventory and the fallback (upsell prompt, limit-reached UX).

### Step 4: Expansion levers

Per Walling, expansion is the SaaS cheat-code. Define:

- **Value-metric expansion** — more seats / more usage as customer grows.
- **Feature expansion** — upsell to next tier.
- **Cross-sell** — adjacent products.

Each lever has: trigger event, in-product upsell UX, sales-assisted upsell path, expected conversion rate.

### Step 5: Freemium decision

Decide yes/no with explicit drivers: high virality? acquisition channel? cost-to-serve free user? conversion rate? competitor pressure? Document the decision as an ADR.

### Step 6: Credit-card-up-front decision

Decide yes/no — trial with CC vs no-CC. Document trade-offs (signup friction vs activated-trial quality).

### Step 7: Price-raise & grandfathering policy

State the cadence (typically annual), the trigger (Rule of 10: ≥ 10% MRR uplift), the grandfathering window (existing customers protected for 12 months), the announcement protocol, the discount-offer to migrate.

### Step 8: Discount & concession authority

| Role | Max discount | Approval |
|------|--------------|----------|
| AE | 10% | self |
| Sales lead | 20% | self |
| VP Sales | 30% | self |
| CFO | > 30% | required |

### Step 9: Public price page contract

The page MUST show prices, tiers, features, limits, FAQ. State what is NOT shown (negotiated enterprise pricing).

### Step 10: Write the spec

`Pricing_And_Packaging_Spec.md` with sections: 1) Value Metric, 2) Tier Definitions, 3) Feature Gates Inventory, 4) Expansion Levers, 5) Freemium / Trial Decision, 6) Credit-Card-Up-Front Decision, 7) Price-Raise & Grandfathering Policy, 8) Discount & Concession Authority, 9) Public Price Page Contract, 10) Traceability to PRD & Business Case.

## Standards

- IEEE 29148-2018 — Stakeholder requirements.
- Walling (2022) — Pricing structure chapters.
- Cotton (2020) — Essay 5: Publish your pricing.

## Resources

- `logic.prompt`, `README.md`, `references/saas-pricing-and-packaging-spec-template.md`.

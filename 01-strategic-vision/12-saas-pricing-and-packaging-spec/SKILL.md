---
name: "saas-pricing-and-packaging-spec"
description: "Generate a SaaS Pricing & Packaging Specification: tiers, value metric, feature gates, expansion mechanics, freemium decision, grandfathering, price-raise policy, public price-page contract, enterprise contact-us path."
metadata:
  use_when: "Use for any SaaS that monetises via subscription, usage, seats, or hybrid — i.e. essentially every SaaS."
  do_not_use_when: "Do not use for open-source or internal-only tools."
  required_inputs: "PRD.md, vision.md, competitive scan, target ICP, business case (CAC payback target)."
  workflow: "Choose value metric, define tiers, define gates, define expansion levers, decide freemium / credit-card-up-front, decide raise/grandfather policy, draft public price page, write the spec."
  quality_standards: "Every tier shall list features, limits, price, SLA, support level. Every gate shall be enforceable server-side. Every expansion lever shall be measurable."
  anti_patterns: "Do not omit the value metric. Do not pick a value metric that does not grow with customer value. Do not gate features in the client."
  outputs: "Pricing_And_Packaging_Spec.md."
  references: "references/saas-pricing-and-packaging-spec-template.md"
---

# SaaS Pricing & Packaging Spec Skill

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

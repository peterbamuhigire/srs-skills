---
name: "saas-mvp-scoping-doc"
description: "Generate a SaaS MVP & Stair-Step Scoping Document: in/out for v1, single acquisition channel committed, escape-velocity success thresholds, feature-triage decision log."
metadata:
  use_when: "Use for early-stage or bootstrapped SaaS, or for any new product line within an established SaaS."
  do_not_use_when: "Do not use for mature products with established roadmaps."
  required_inputs: "Lean_Canvas.md or vision.md, market evidence, target ICP, founder commitments."
  workflow: "Pick stair-step stage, choose single channel, define v1 IN/OUT, set escape-velocity thresholds, run feature-triage decision log, write the spec."
  quality_standards: "v1 scope shall be narrow enough to ship in ≤ 90 days. Single channel chosen. Each cut feature has a documented reason."
  anti_patterns: "Do not include 'nice to have' in v1. Do not commit to multiple channels in v1."
  outputs: "MVP_Scoping_Doc.md."
  references: "references/saas-mvp-scoping-template.md"
---

# SaaS MVP Scoping Doc Skill

## Overview

Anchored in Walling's *SaaS Playbook* (stair-step method, escape velocity, feature triage). Forces explicit cuts and a single channel.

## Core Instructions

### Step 1: Choose stair-step stage

Identify the current stage: Step 1 (one organic channel proof), Step 2 (rinse-and-repeat), Step 3 (standalone SaaS). State implications: hiring, capital, risk tolerance.

### Step 2: Single channel commitment

Choose ONE acquisition channel for v1 (content/SEO, paid ads, integrations partnership, cold outbound, marketplace listing, founder network). State why; state the others rejected.

### Step 3: Define v1 IN / OUT

| Bucket | Items | Reason |
|--------|-------|--------|
| IN | feature 1, feature 2, ... | minimum to validate value proposition |
| OUT (deferred to v2) | feature X, Y, Z | not on validation path |
| OUT (rejected) | feature P, Q | not on vision / out of moat |

Hard rule: IN list ships in ≤ 90 days.

### Step 4: Escape-velocity thresholds

Walling-style triggers for moving past Step 1:

- MRR ≥ $X.
- Logo count ≥ N.
- Activation rate ≥ Y%.
- Retention floor ≥ Z%.
- Top-of-funnel attributable to chosen channel ≥ M leads/mo.

State each threshold with the date by which it should be hit.

### Step 5: Feature-triage decision log

Apply Walling's 3 questions to every requested feature:

1. What's the use case? (problem solved)
2. % of customers using it? (estimate)
3. Does it fit the vision?

| Feature | Use case | % adoption (est) | Vision fit | Decision | Date |

Outcomes: Crackpot (reject), No-brainer (in v1 if cheap), In-between (decided by use-case × adoption × fit). Every cut is logged so the founder doesn't relitigate.

### Step 6: Write the doc

`MVP_Scoping_Doc.md` with sections: 1) Stair-Step Stage, 2) Single Channel Commitment, 3) v1 IN / OUT / Deferred / Rejected, 4) Escape-Velocity Thresholds, 5) Feature-Triage Decision Log, 6) Risk register (v1 risks), 7) Re-evaluation date (e.g. 60 days post-launch).

## Standards

- IEEE 29148-2018.
- Walling (2022) *SaaS Playbook*.

## Resources

- `logic.prompt`, `README.md`, `references/saas-mvp-scoping-template.md`.

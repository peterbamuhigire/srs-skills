---
name: 10-saas-mvp-scoping-doc
description: Use when an early-stage or new SaaS product line needs a tightly bounded v1, one acquisition channel, explicit cuts, escape-velocity measures and a feature-triage log; use lean-canvas while the customer problem is still untested and PRD generation for the approved v1.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# SaaS MVP Scoping Doc Skill
<!-- dual-compat-start -->
## Use When

- A SaaS team must decide what can ship in v1 and what evidence justifies the next stair step.

## Do Not Use When

- Do not use for a mature product with an established roadmap or to force a 90-day scope without delivery evidence.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Validated Lean Canvas or vision and ICP | Phase 01 discovery | Required | Stop if the target customer and problem remain undefined. |
| Delivery capacity, market evidence and founder commitments | Delivery team and sponsor | Required | Return scope options if capacity or channel ownership is unknown. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the SaaS MVP Scoping Document through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the SaaS MVP Scoping Document to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| SaaS MVP Scoping Document | Product, delivery and go-to-market owners | Every v1 item passes the triage rule, every cut has a reason, one channel has an owner, and success thresholds determine the next step. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified SaaS MVP Scoping Document draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Feature is necessary to test core value | Keep in v1 | MVP can test the thesis |
| Feature serves scale, polish or a later segment | Move out with revisit trigger | Scope expands before learning |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Adding nice-to-have features to avoid a hard conversation. Fix: apply the feature-triage log.
- Choosing several acquisition channels. Fix: commit one owner to one initial channel.
- Setting a deadline without capacity evidence. Fix: reconcile scope with staffed delivery estimates.
- Calling sign-ups escape velocity. Fix: use activation, retention and revenue evidence suited to the model.
- Deleting cut features without rationale. Fix: record the reason and revisit trigger.

## References

- [MVP scoping template](references/saas-mvp-scoping-template.md)
- [Lean Canvas neighbour](../04-lean-canvas/SKILL.md)
<!-- dual-compat-end -->




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

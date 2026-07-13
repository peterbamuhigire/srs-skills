---
name: 11-saas-moat-and-defensibility-plan
description: Use when a SaaS product needs an evidence-based defensibility plan covering integrations, owned channels, switching costs, proprietary data, brand or network effects; use competitive discovery for market facts and MVP scoping for initial release boundaries.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# SaaS Moat & Defensibility Plan Skill
<!-- dual-compat-start -->
## Use When

- The team must choose one to three credible moat mechanisms and a hardening roadmap.

## Do Not Use When

- Do not use to relabel ordinary features, temporary execution speed or customer lock-in abuse as a moat.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Vision, PRD and competitive evidence | Approved project artefacts and verified market scan | Required | Qualify competitive gaps; do not invent competitor weaknesses. |
| Customer behaviour and asset evidence | Product analytics, interviews and operations | Required | Mark unmeasured moat candidates as hypotheses. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Moat and Defensibility Plan through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Moat and Defensibility Plan to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Moat and Defensibility Plan | Product strategy, investment and delivery owners | Each selected moat has current evidence, strength score, milestone, owner, measure and failure signal; false moats are rejected. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Moat and Defensibility Plan draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Mechanism compounds with use and is hard to copy | Select and harden it | Resources build durable advantage |
| Advantage is only a feature or temporary lead | Treat it as execution, not a moat | Strategy relies on false defensibility |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Calling a unique feature a moat. Fix: test whether it compounds and resists copying.
- Selecting six primary moats. Fix: fund one to three mechanisms with evidence.
- Using contractual lock-in as switching-cost strategy. Fix: create customer-owned accumulated value and portability.
- Claiming network effects without a cross-user benefit loop. Fix: map the loop and threshold.
- Assigning milestones without owners or measures. Fix: name both and define failure signals.

## References

- [Defensibility template](references/saas-moat-and-defensibility-template.md)
- [MVP scoping neighbour](../10-saas-mvp-scoping-doc/SKILL.md)
<!-- dual-compat-end -->




## Overview

Anchored in Walling's moat taxonomy. Forces explicit identification of real vs false moats and a hardening roadmap.

## Core Instructions

### Step 1: Moat candidates inventory

| Moat type | Description | Current strength (1-5) | Trend |
|-----------|-------------|-----------------------|-------|
| Integrations / network effect | depth of integrations into customer workflow | | |
| Brand | recognised authority in segment | | |
| Owned traffic channels | direct audience (newsletter, podcast, community) | | |
| Switching costs | data, workflows, integrations make leaving expensive | | |
| Data network effect | usage produces data that improves the product | | |
| Marketplace / two-sided | supply + demand both onboard | | |
| Regulatory / certifications | hard-won attestations | | |
| Geographic / vertical specialisation | depth in narrow segment | | |

### Step 2: False-moat watch

Per Walling, "unique features" is the false moat — competitors can copy in months. Flag the false moats currently being relied on.

### Step 3: Pick the 1-3 primary moats

Focus is more valuable than breadth. Choose at most three primary moats; the rest are "passive" (maintained, not invested).

### Step 4: Per-moat hardening plan

For each primary moat:

| Moat | Current state | Target state (12 mo) | Owner | Milestones | Investment |
|------|---------------|----------------------|-------|------------|------------|
| | | | | quarterly | $/headcount |

### Step 5: Anti-moats to avoid

- Underpricing.
- Translating product before product-market fit.
- White-labelling at small scale.
- Adding verticals too early.

### Step 6: Write the plan

`Moat_And_Defensibility_Plan.md` with: 1) Inventory, 2) False moats identified, 3) Primary moats chosen, 4) Per-moat hardening plan, 5) Anti-moats to avoid, 6) Quarterly review schedule.

## Standards

- Walling (2022).
- IEEE 29148-2018 (strategic requirements).

## Resources

- `logic.prompt`, `README.md`, `references/saas-moat-and-defensibility-template.md`.

---
name: 06-saas-onboarding-journey-spec
description: Use when specifying a SaaS aha event, activation milestones, segmented paths, nudges, measurement sources, and drop-off interventions. Use customer-success-playbook for ongoing intervention and user-manual for product procedures.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Onboarding Journey Spec Skill

<!-- dual-compat-start -->

## Use When

- Use when specifying a SaaS aha event, activation milestones, segmented paths, nudges, measurement sources, and drop-off interventions. Use customer-success-playbook for ongoing intervention and user-manual for product procedures.

## Do Not Use When

- Do not use when there is no signup flow.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: PRD.md, Pricing_And_Packaging_Spec.md, user-research notes, product-analytics access (events catalogue). | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A claim, segment, trigger, metric, or intervention lacks product evidence | Qualify it and request the missing source | Generic playbooks detached from product reality |
| Consent, suppression, fairness, or customer-harm guardrail fails | Stop the affected play or campaign | Dark patterns or non-compliant outreach |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| SaaS Onboarding Journey Spec | Customer, support, success, sales, or implementation owner | Aha-moment is a single named event. Every milestone has a target completion window and a measurement source. Every nudge has a channel and a trigger. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Onboarding Journey Spec evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Aha-moment is a single named event. Every milestone has a target completion window and a measurement source. Every nudge has a channel and a trigger.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Onboarding Journey Spec from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a claim, segment, trigger, metric, or intervention lacks product evidence, qualify it and request the missing source. Record the evidence and result in the validation record; this avoids generic playbooks detached from product reality.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

Sourced from Garbugli (lifecycle email) and Walling (activation as escape-velocity threshold). Produces the explicit onboarding-journey doc many SaaS lack.

## Core Instructions

### Step 1: Define the aha-moment

A single named product event where the user first perceives value. State it precisely (e.g. "first invoice sent", "first deal closed in pipeline", "first dashboard published"). Activation rate = % of signups reaching this event within N days.

### Step 2: Define activation milestones

| # | Milestone | Event name | Target window | Why it matters |
|---|-----------|------------|---------------|----------------|
| 1 | Sign-up complete | `user.signed_up` | T0 | enter funnel |
| 2 | Profile complete | `user.profile_completed` | T+5 min | reduces friction |
| 3 | First action | `<product-specific>` | T+1 day | hands-on engagement |
| 4 | Aha moment | `<aha event>` | T+7 day | core activation |
| 5 | Team invited / integration | `team.invited` or `integration.connected` | T+14 day | stickiness |
| 6 | Habit formed | `user.returned_3_times` in 7 d | T+21 day | retention indicator |

### Step 3: Channel orchestration

For each milestone, define the nudge program if the milestone hasn't fired:

| Stage | In-app | Email | Push | SMS | CSM (Gold/Ent) |
|-------|--------|-------|------|-----|----------------|
| Sign-up | welcome modal | welcome email | – | – | – |
| 24h no profile | tooltip | reminder | – | – | – |
| Day 3 no first action | guided tour | activation tip | – | – | – |
| Day 7 no aha | targeted offer / on-screen template | aha-moment story | – | – | call (Gold) |
| Day 14 no team | invite prompt | team-onboarding playbook | – | – | – |

Max 3 touches per day per user.

### Step 4: Drop-off interventions

For each commonly-dropped step, design an intervention (in-product flow, CSM call, integration concierge, refund-trial-extend offer).

### Step 5: KPI thresholds

| Metric | Target | Owner |
|--------|--------|-------|
| Sign-up → activation | ≥ 30% | Product + Growth |
| Time-to-aha P50 | ≤ 5 days | Product |
| Day-30 retention of activated cohort | ≥ 60% | Product + CS |
| Email open rate (onboarding) | ≥ 40% | Lifecycle |
| In-app nudge click-through | ≥ 25% | Growth |

### Step 6: Segmented paths

Per ICP and per tier. Enterprise has CSM-led onboarding overlay; SMB is product-led; freelance is fully self-serve. Document the differences.

### Step 7: Write the spec

`Onboarding_Journey_Spec.md` with sections: 1) Aha-Moment, 2) Activation Milestones, 3) Channel Orchestration, 4) Drop-off Interventions, 5) KPI Thresholds, 6) Segmented Paths, 7) Event Catalogue (events emitted at each milestone), 8) Review cadence.

## Standards

- ISO 26514 (user documentation).
- IEEE 29148 (stakeholder requirements).
- Garbugli (SaaS Email Marketing Playbook).

## Resources

- `logic.prompt`, `README.md`, `references/saas-onboarding-journey-spec-template.md`.

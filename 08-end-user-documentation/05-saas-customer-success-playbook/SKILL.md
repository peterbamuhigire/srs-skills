---
name: 05-saas-customer-success-playbook
description: Use when defining SaaS health scoring, lifecycle intervention plays, QBRs, dunning recovery, escalation, renewal, and expansion operations. Use onboarding-journey-spec for activation design and lifecycle-email-strategy-doc for email execution.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Customer Success Playbook Skill

<!-- dual-compat-start -->

## Use When

- Use when defining SaaS health scoring, lifecycle intervention plays, QBRs, dunning recovery, escalation, renewal, and expansion operations. Use onboarding-journey-spec for activation design and lifecycle-email-strategy-doc for email execution.

## Do Not Use When

- Do not use for tools without a CS function (rare).
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: PRD.md, Pricing_And_Packaging_Spec.md, Onboarding_Journey_Spec.md (if available), churn data, contract types. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| SaaS Customer Success Playbook | Customer, support, success, sales, or implementation owner | Every play shall have trigger, owner, action, measurement of success, escalation rule. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Customer Success Playbook evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every play shall have trigger, owner, action, measurement of success, escalation rule.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Customer Success Playbook from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

Produces the playbook that operationalises churn-control and expansion. Sourced from Cotton (Essay 9: churn is the quiet killer) and Garbugli (lifecycle email tactics).

## Core Instructions

### Step 1: Customer Health Score spec

Composite of (usage depth, breadth, engagement frequency, support sentiment, NPS, contract age, expansion signal). State weights, scoring formula, refresh cadence (weekly), bands (Green / Yellow / Red), action per band.

### Step 2: Segment customers

By tier (Bronze/Silver/Gold/Enterprise) × stage (onboarding 0-90 d / adoption 90-365 d / renewal-window / at-risk / churned-recoverable). Different plays per segment.

### Step 3: Per-stage plays

For each (segment, stage) pair produce a play:

```
### Play: <name>
- Trigger:
- Owner: (CSM / CS-Ops / automation)
- Action:
- Channels (in-app / email / call):
- Frequency:
- Success measurement:
- Escalation rule:
```

Required plays (minimum):

- **Onboarding kickoff** (Day 0)
- **First-value milestone check** (Day 7)
- **30-day health review**
- **At-risk intervention** (health → Red)
- **Renewal forecast** (T-90, T-60, T-30)
- **Renewal at-risk save**
- **Expansion / upsell** (health → Green + signal)
- **Dunning recovery** (payment-failure)
- **Churned recoverable** (re-engagement)

### Step 4: QBR template

Quarterly Business Review template: business objectives, usage review, value delivered, support summary, expansion opportunities, action items.

### Step 5: Escalation matrix

When does an account escalate from CSM to CS Lead, to CRO, to executive sponsor? Triggers (health, ARR, contract anniversary, executive contact change, integration partner change).

### Step 6: Write the playbook

`Customer_Success_Playbook.md` with sections: 1) Health Score Spec, 2) Segmentation, 3) Per-Stage Plays, 4) QBR Template, 5) Dunning Recovery, 6) Escalation Matrix, 7) Tooling & Source-of-Truth, 8) Cadence & Review.

## Standards

- Cotton (2020) Essay 9.
- Pulse / TSIA customer-success frameworks.
- IEEE 29148-2018 (service-level requirements).

## Resources

- `logic.prompt`, `README.md`, `references/saas-customer-success-playbook-template.md`.

---
name: 05-saas-growth-experiment-doc
description: Use when specifying a SaaS product, pricing, onboarding, or lifecycle experiment with a hypothesis, primary metric, sample logic, guardrails, stop rule, instrumentation, and decision rule. Use retrospective-template for team process learning.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Growth Experiment Doc Skill

<!-- dual-compat-start -->

## Use When

- Use when specifying a SaaS product, pricing, onboarding, or lifecycle experiment with a hypothesis, primary metric, sample logic, guardrails, stop rule, instrumentation, and decision rule. Use retrospective-template for team process learning.

## Do Not Use When

- Do not use for prod hotfixes.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: Onboarding_Journey_Spec.md or Lifecycle_Email_Strategy_Doc.md or Pricing_And_Packaging_Spec.md (whichever the experiment touches), product analytics, A/B platform. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Primary metric, instrumentation, or stop rule is unverified | Do not launch; repair the experiment contract | Peeking, false attribution, or harmful rollout |
| Pre-registered rule is met without a guardrail breach | Apply the declared ship, iterate, or stop decision | Post-hoc goal changing |

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
| SaaS Growth Experiment Doc | Product owner and delivery team | Every experiment has a single primary metric, a pre-registered stop rule, and at least one guardrail metric. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Growth Experiment Doc evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every experiment has a single primary metric, a pre-registered stop rule, and at least one guardrail metric.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Growth Experiment Doc from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if primary metric, instrumentation, or stop rule is unverified, do not launch; repair the experiment contract. Record the evidence and result in the validation record; this avoids peeking, false attribution, or harmful rollout.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

Codifies the experiment design that good growth teams operate on. Anchored in standard A/B-test rigor + Garbugli's lifecycle experiment chapters.

## Core Instructions

### Step 1: Hypothesis

`If <change>, then <metric> will <direction> by <magnitude>, because <mechanism>.`

State explicitly. Frame as falsifiable.

### Step 2: Primary metric + guardrails

- One primary metric (e.g. activation rate, week-1 retention, MRR per signup).
- 1-3 guardrail metrics that MUST NOT regress (e.g. churn, support load, page latency).
- One leading-indicator metric.

### Step 3: Segment & sample size

- Segment: who is exposed (e.g. signups in last 7 d in EU on Pro tier).
- Baseline conversion: <%>.
- Minimum Detectable Effect (MDE): <%>.
- Statistical power: 80%.
- Significance: 95%.
- Required sample size per arm: computed.
- Estimated duration: <weeks>.

### Step 4: Stop rule

- Maximum duration: <weeks>.
- Early-stop on guardrail breach: yes if guardrail regresses by > <threshold>.
- Early-stop on success: only at full sample (Bayesian / sequential rules pre-registered if used).
- Pre-registered analysis date.

### Step 5: Decision rule

- Ship if primary metric +X% with p<0.05 AND no guardrail regresses by > Y%.
- Reject if primary -X% OR any guardrail regresses by > Y%.
- Iterate if inconclusive.

### Step 6: Instrumentation

- Variant assignment: deterministic by user_id hash.
- Tenant-context: variant exposed at user level (consider tenant-scoping for multi-user SaaS).
- Events emitted: variant_assignment, primary_metric, guardrails.
- A/B platform: <name>.

### Step 7: Risks & ethics

- Reversibility: can we roll back instantly?
- Customer-impact: does any variant degrade experience for paying users?
- Pricing tests: extra care with paying tenants — usually segment to free or new-trial.
- Notification: do users need to know?

### Step 8: Post-mortem

After experiment:

- Result summary.
- Did we learn what we hypothesised?
- Action taken: ship / reject / iterate.
- Surprising findings.
- Process notes.

### Step 9: Write the doc

`Growth_Experiment_Doc.md` with sections: 1) Hypothesis, 2) Metrics (primary, guardrails, leading), 3) Segment & Sample Size, 4) Stop Rule, 5) Decision Rule, 6) Instrumentation, 7) Risks & Ethics, 8) Timeline, 9) Post-mortem (filled after).

## Standards

- IEEE 29148 (requirements engineering).
- Industry A/B-test rigour (Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments*).

## Resources

- `logic.prompt`, `README.md`, `references/saas-growth-experiment-template.md`.

---
name: 10-ai-hallucination-slo-doc
description: Use when defining an AI hallucination SLO for factuality, citation validity, abstention, severity, sampling, error budget, and release response; use saas-slo-and-error-budget-doc for ordinary service reliability.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Hallucination SLO Doc Skill

<!-- dual-compat-start -->
## Use When

- Produce or update service-level objective document from approved project evidence.
- Resolve decisions about SLIs, objectives, error budgets, burn alerts, exclusions, and response policy.
- Prepare a reviewable handoff for Service owners, SRE, and release teams.

## Do Not Use When

- The task is primarily owned by monitoring-setup; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Service-level Objective Document | Service owners, SRE, and release teams | Each SLO has a computable SLI, justified target, data source, exclusions, burn policy, and linked response. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose objectives from user harm and measured baseline and produce the full artefact. | Unmeasurable reliability promises. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring monitoring-setup concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when each SLO has a computable SLI, justified target, data source, exclusions, burn policy, and linked response.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

The AI complement to the SaaS SLO doc. Treats hallucination, citation, abstention, and safety violations as first-class SLIs with their own error budgets and rollback rules.

## Core Instructions

### Step 1: SLI inventory per AI feature

Required SLIs:

- **Factuality SLI** — % of responses on a production-sample where judge-LLM marks all claims as supported.
- **Citation accuracy SLI** (RAG only) — % of citations matching source spans within tolerance.
- **Abstention precision SLI** — % of abstain responses that correctly should have abstained.
- **Abstention recall SLI** — % of should-abstain inputs that did abstain.
- **Safety violation SLI** — count of outputs hitting content-policy or PII filters per million calls.
- **Latency SLI** (already in parent SLO doc, restated for AI clarity).
- **Cost-per-call SLI** (cross-link to cost runbook).

### Step 2: Measurement procedure

For each SLI state the measurement source and sample method:

- Factuality and citation: production-sample replayed through the judge-LLM nightly. Sample rate per feature.
- Abstention: classify production responses by abstain-payload; spot-check by humans monthly to verify abstain correctness.
- Safety violation: counted at content-filter; alarmed on each event.

### Step 3: Set per-feature SLO targets

Per feature × tier:

| Tier | Factuality | Citation | Abstention precision | Safety violations |
|------|-----------|----------|-----------------------|--------------------|
| Free | >= 0.85 | n/a or >= 0.85 | >= 0.70 | 0 |
| Pro | >= 0.92 | >= 0.90 | >= 0.80 | 0 |
| Enterprise | >= 0.95 | >= 0.95 | >= 0.85 | 0 |

### Step 4: Error budgets

Standard formula: `error_budget = (1 - SLO) × calls_in_window`. Safety violations: zero-budget; any breach is SEV1.

### Step 5: Multi-burn-rate alerts

| Alert | Burn rate | Window | Threshold |
|-------|-----------|--------|-----------|
| Fast burn | 14× | 1 h | 2% of monthly budget |
| Medium burn | 6× | 6 h | 5% |
| Slow burn | 1× | 3 d | 10% |
| Safety | n/a | 0 | any |

### Step 6: Freeze and rollback rules

- Error budget exhausted: freeze prompt and model changes; eval bumps require executive approval.
- Citation accuracy drop > 5 pp in 24 h: auto-rollback to last green prompt tag.
- Safety violation: pause feature; SEV1; postmortem; provider escalation if upstream.

### Step 7: Customer-facing AI-quality commitments

Mirror the parent SLO doc pattern. Per tier, define what is contractually committed (likely abstention behaviour and uptime; not numerical factuality, since per-output verifiability remains imperfect). Define how customers report a perceived hallucination (flag button -> ticket -> review).

### Step 8: Write the doc

`AI_Hallucination_SLO_Doc.md` sections: 1) AI SLI Inventory, 2) Measurement Procedure, 3) Per-Feature SLO Targets, 4) Error Budgets, 5) Burn-Rate Alerts, 6) Freeze & Rollback Rules, 7) Customer-Facing AI Commitments, 8) Review Cadence.

## Standards

- Google SRE applied to AI features
- ISO/IEC 25010 (functional correctness)
- ISO/IEC 42001 Clause 9 (performance evaluation)

---
name: 08-saas-slo-and-error-budget-doc
description: Use when defining SaaS availability, latency, tenant-impact SLIs, error budgets, burn alerts, exclusions, and response policy; use monitoring-setup to specify collection, dashboards, and alert implementation.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# SaaS SLO and Error-Budget Doc Skill

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

Produces the SLO/error-budget document for a SaaS system, with per-tier targets and customer-SLA mapping. Anchored in Google SRE practice and Golding (2024) tiering.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Multi_Tenancy_Architecture_Spec.md, Monitoring_Setup.md, quality_standards.md, pricing & packaging spec |
| **Output** | `SLO_And_Error_Budget_Doc.md` |
| **Standard** | Google SRE / ISO/IEC 25010 |

## Core Instructions

### Step 1: Inventory SLIs

For every service-tier combination, list Service Level Indicators:

- Availability (success ratio of valid requests).
- Latency P95 / P99.
- Throughput (requests/sec).
- Correctness (e.g. billing-event-emission rate).
- Freshness (data lag, replication lag).
- Durability (data loss probability).

Each SLI declares: definition, measurement source, sampling window, exclusions (planned maintenance).

### Step 2: Set per-tier SLOs

| Tier | Availability | Latency P95 | Latency P99 | Support response | Notes |
|------|--------------|-------------|-------------|------------------|-------|
| Bronze | 99.5% | 800 ms | 2000 ms | next business day | shared pool |
| Silver | 99.9% | 400 ms | 1000 ms | 4 h | shared pool with reserved capacity |
| Gold | 99.95% | 200 ms | 500 ms | 1 h | pod-isolated |
| Enterprise | 99.99% | 150 ms | 300 ms | 15 min, named CSM | silo or dedicated pod |

### Step 3: Compute error budgets

- Bronze 99.5% over 30 d = 3 h 36 min downtime allowed.
- Silver 99.9% over 30 d = 43 min 12 s.
- Gold 99.95% over 30 d = 21 min 36 s.
- Enterprise 99.99% over 30 d = 4 min 19 s.

State error budget per SLO and the formula `error_budget_minutes = (1 - SLO) × period_minutes`.

### Step 4: Burn-rate alerts

Define multi-window multi-burn-rate alerts:

| Alert | Severity | Burn rate | Window | Threshold |
|-------|----------|-----------|--------|-----------|
| Fast burn | SEV2 | 14.4× | 1 h | 2% of monthly budget |
| Medium burn | SEV3 | 6× | 6 h | 5% of monthly budget |
| Slow burn | SEV4 | 1× | 3 d | 10% of monthly budget |

### Step 5: Freeze rules

State the rules that take effect when error budget is exhausted: no risky deploys, increased review, postmortem actions blocked from being skipped, executive notification at < 0% budget remaining.

### Step 6: Customer-SLA mapping

For each tier, map the internal SLO to the contractual SLA commitment (which is typically more conservative — internal 99.95% backs external 99.9%). Define service-credit schedule (% credit per breach band), the exclusions, the measurement method, the credit-request process.

### Step 7: Write the doc

`SLO_And_Error_Budget_Doc.md` with sections: 1) SLI Inventory, 2) Per-Tier SLO Targets, 3) Error-Budget Math, 4) Burn-Rate Alerts, 5) Freeze Rules, 6) Customer-SLA Mapping & Service Credits, 7) Review Cadence (monthly SLO review, quarterly target review).

## Standards

- Google SRE: SLO/Error Budget, Multi-Burn-Rate Alerting.
- ISO/IEC 25010 — Quality model.

## Resources

- `logic.prompt`, `README.md`, `references/saas-slo-and-error-budget-template.md`.

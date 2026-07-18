---
name: 05-go-live-readiness
description: Use when producing or updating go-live readiness assessment for evidence-based release gates, owners, waivers, rollback readiness, and launch decision. Use deployment-guide for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Go-Live Readiness Skill

<!-- dual-compat-start -->
## Use When

- Produce or update go-live readiness assessment from approved project evidence.
- Resolve decisions about evidence-based release gates, owners, waivers, rollback readiness, and launch decision.
- Prepare a reviewable handoff for Release authority and project sponsor.

## Do Not Use When

- The task is primarily owned by deployment-guide; route there and use this skill only for its named output.
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
| Go-live Readiness Assessment | Release authority and project sponsor | Every mandatory gate is passed with evidence or carries a named, time-bound waiver accepted by the release authority. |
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
| Evidence is complete and authority is explicit | Choose go/no-go from mandatory evidence and residual risk and produce the full artefact. | Launching on optimistic status summaries. |
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
- Mixing the neighbouring deployment-guide concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every mandatory gate is passed with evidence or carries a named, time-bound waiver accepted by the release authority.

## References

- [Repository router](../../README.md) - project pathing, phase sequence, and delivery rules.
<!-- dual-compat-end -->

## Use When

- A release, pilot, migration, public-sector launch, SaaS rollout, AI deployment, website launch, or production cutover needs a go/no-go decision.
- Deployment, monitoring, support, training, communication, rollback, hypercare, and organisational readiness must be reviewed together.

## Do Not Use When

- The project is still in early design with no release scope, target environment, operating owner, or launch window.
- The task is only a deployment procedure; use deployment/runbook skills first.

## Required Inputs

- Release scope, deployment guide, runbook, monitoring setup, infrastructure docs, test report, support model, training plan, risks, blockers, rollback plan, and approvers.

## Workflow

1. Define release decision context, launch type, launch window, owners, and approvers.
2. Evaluate product, deployment, rollback, monitoring, support, security, data, training, communication, vendor, and transition readiness.
3. Score each dimension as ready, conditionally ready, or blocked.
4. Build blocker register with owner, evidence gap, due date, and mitigation.
5. Build launch control plan with cutover timeline, decision checkpoints, abort triggers, communications, hypercare, and success metrics.
6. Route adoption/support gaps to `06-deployment-operations/06-customer-adoption-and-support-plan`.
7. Record go, conditional-go, or no-go recommendation.

## Quality Standards

- Every conditional or blocked item must have evidence, owner, due date, and decision impact.
- Technical readiness is insufficient without support, training, communication, rollback, and operating ownership.
- The final recommendation must be usable in a real go/no-go meeting.

## Anti-Patterns

- Declaring readiness because tests passed while support, rollback, or training is missing.
- Launching without named incident, communication, and recovery owners.
- Treating premium or public-sector user support as generic post-launch help.

## Outputs

- Go-live readiness report, blocker register, launch control plan, cutover decision record, and adoption/support handoff.

## References

- `references/`
- `06-deployment-operations/06-customer-adoption-and-support-plan`


## Overview

This skill closes the loop between design, delivery, and operations by determining whether the product is actually ready to launch. It synthesizes deployment, monitoring, runbook, infrastructure, and transition evidence into a decision record that supports go, conditional go, or no-go outcomes.

## When to Use

- Before a production launch, customer rollout, pilot, migration, or major cutover
- When release stakeholders need a structured readiness review rather than ad hoc signoff
- When support, training, communication, operational ownership, or rollback planning could affect launch success
- When the team needs an explicit blocker list and conditional-release criteria

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md`, `projects/<ProjectName>/<phase>/<document>/Runbook.md`, `projects/<ProjectName>/<phase>/<document>/Monitoring_Setup.md`, `projects/<ProjectName>/<phase>/<document>/Infrastructure_Docs.md` (recommended), release-specific evidence |
| **Output** | `projects/<ProjectName>/<phase>/<document>/Go_Live_Readiness.md` |
| **Tone** | Decision-oriented, risk-aware, operationally concrete |
| **Standards** | Production readiness, transition governance, and operational acceptance practices |

## Core Instructions

### Step 1: Define the Release Decision Context

State:
- release scope
- target environment and launch window
- launch type such as big-bang, phased, pilot, or canary
- accountable approvers and operating owners

### Step 2: Evaluate Readiness Dimensions

Assess at minimum:
- product scope completeness
- deployment and rollback readiness
- monitoring and alerting readiness
- support and incident response readiness
- security and compliance readiness
- data migration or cutover readiness
- training, communication, and organizational transition readiness
- vendor or dependency readiness

### Step 3: Score and Classify Findings

For each dimension, mark:
- ready
- conditionally ready
- blocked

Every conditional or blocked item must include an owner, evidence gap, due date, and mitigation path.

### Step 4: Build the Launch Control Plan

Document:
- cutover timeline
- decision checkpoints
- rollback triggers
- communications cadence
- hypercare support period
- first-day and first-week success metrics

If adoption, training, service desk, customer recovery, or maintenance commitments are material to launch success, invoke `06-deployment-operations/06-customer-adoption-and-support-plan` and attach its support scripts and adoption metrics as readiness evidence.

### Step 5: Record the Go/No-Go Recommendation

Choose one outcome:
- go
- conditional go
- no-go

State the reasoning, unresolved risks, and exact conditions for changing the decision.

### Step 6: Generate Output

Write `projects/<ProjectName>/<phase>/<document>/Go_Live_Readiness.md` with readiness assessment, blocker register, cutover plan, and recommendation.

## Common Pitfalls

- Treating technical deployment readiness as the whole launch decision
- Launching without named incident, rollback, and business-communication owners
- Ignoring customer support, operations staffing, or training gaps
- Declaring readiness without measurable success and abort criteria

## Verification Checklist

- [ ] The launch scope, timing, and accountable owners are explicit.
- [ ] Every readiness dimension has evidence and a status.
- [ ] Every blocker or conditional item has an owner and due date.
- [ ] Rollback triggers and hypercare support are defined.
- [ ] The final recommendation is explicit and justified.
- [ ] The document can support an actual go/no-go meeting without extra reconstruction.

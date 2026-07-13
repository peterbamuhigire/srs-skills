---
name: 12-solution-evaluation-and-transition
description: "Use when planning adoption, readiness, go/no-go evidence, transition, and post-implementation outcome evaluation; use go-live-readiness for the release-day operational gate."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Solution Evaluation And Transition Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- planning adoption, readiness, go/no-go evidence, transition, and post-implementation outcome evaluation; use go-live-readiness for the release-day operational gate.
- Use this procedure when the required source artefacts are available and `Solution evaluation and transition plan` is the next lifecycle deliverable.

## Do Not Use When

- Use `go-live-readiness` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved requirements, delivered solution evidence, stakeholder impacts, and success measures | Project sponsor, operations, users, and delivery records | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Solution evaluation and transition plan`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Solution evaluation and transition plan | Sponsor, adoption leads, operations, and benefits owner | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Solution evaluation and transition plan` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. This procedure is read-only by default. Editing the reviewed artefact, publishing, production mutation, destructive action, spending, or certification requires explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A transition dependency has no owner or observable readiness evidence | Block the affected transition milestone and assign evidence ownership. | Go-live without operational or organisational readiness. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Solution evaluation and transition plan` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Solution evaluation and transition plan` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `go-live-readiness` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../../docs/skill-authoring-standard.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview

This skill closes the gap between completed requirements or delivery artifacts and real organizational adoption. It plans transition activities, readiness evidence, go/no-go framing, post-implementation evaluation, and success measurement so the engine supports actual solution rollout, not only analysis and design.

## When to Use

- When requirements, design, testing, or deployment artifacts are mature enough for rollout planning
- Before a pilot, cutover, or formal go/no-go decision
- When the project changes user behavior, operating procedures, or support responsibilities
- After early release to define solution performance evaluation criteria

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/<phase>/<document>/validation_report.md`, `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md` (optional), `projects/<ProjectName>/<phase>/<document>/Runbook.md` (optional), `projects/<ProjectName>/<phase>/<document>/Test_Report.md` (optional), `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md` |
| **Output** | `projects/<ProjectName>/<phase>/<document>/solution_evaluation_transition_plan.md` |
| **Tone** | Operational, adoption-focused, evidence-based |
| **Standards** | PMI BA transition and solution evaluation practices |

## Core Instructions

### Step 1: Assess Transition Scope

Document who must change, including:
- end users
- approvers or supervisors
- support teams
- operations teams
- downstream systems or partners

### Step 2: Define Readiness Evidence

Collect evidence required for transition:
- requirement and test coverage
- unresolved defect or risk summary
- training or enablement readiness
- support and operations readiness
- rollback and cutover preparedness

### Step 3: Plan Organizational Transition

Specify:
- training activities
- communications
- cutover sequence
- support model during hypercare
- ownership after handoff

### Step 4: Frame the Go/No-Go Decision

State:
- go criteria
- no-go triggers
- conditional-go criteria
- approvers
- evidence package required

### Step 5: Define Solution Evaluation Measures

Define post-launch evaluation measures:
- adoption
- task completion
- error or defect rate
- operational burden
- user satisfaction
- business outcome measures tied to project goals

### Step 6: Write Output

Write `projects/<ProjectName>/<phase>/<document>/solution_evaluation_transition_plan.md` with transition actions, readiness gaps, decision criteria, and evaluation metrics.

## Common Pitfalls

- Launching without naming operational owners
- Treating training as optional for behavior-changing systems
- Using vague go/no-go criteria
- Measuring only delivery output instead of actual solution performance

## Verification Checklist

- [ ] Transition-affected groups are identified.
- [ ] Readiness evidence is defined and reviewed.
- [ ] Go/no-go criteria are explicit and measurable.
- [ ] Adoption, support, and hypercare plans are documented.
- [ ] Post-implementation evaluation metrics are tied to goals.

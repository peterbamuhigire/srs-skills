---
name: 10-prototyping-and-solution-discovery
description: "Use when comparing solution candidates or prototypes to reduce uncertainty before locking requirements or design; use UX-specification after the chosen interaction direction is approved."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Prototyping And Solution Discovery Skill

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- comparing solution candidates or prototypes to reduce uncertainty before locking requirements or design; use UX-specification after the chosen interaction direction is approved.
- Use this procedure when the required source artefacts are available and `Prototype plan, evaluation evidence, and decision record` is the next lifecycle deliverable.

## Do Not Use When

- Use `ux-specification` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Discovery question, candidate options, constraints, users, risks, and success criteria | Product owner, users, architecture, and research evidence | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Prototype plan, evaluation evidence, and decision record`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Prototype plan, evaluation evidence, and decision record | Requirements, product, design, and architecture owners | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Prototype plan, evaluation evidence, and decision record` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A prototype has no falsifiable question or decision threshold | Rewrite the experiment before building it. | Prototype theatre with no decision value. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Prototype plan, evaluation evidence, and decision record` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Prototype plan, evaluation evidence, and decision record` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `ux-specification` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../../docs/skill-authoring-standard.md)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview

This skill creates structured candidate solutions and prototype-driven learning before the project commits to a detailed design. It supports sacrificial prototypes, ready-made solution evaluation, comparison matrices, and explicit learning loops so the engine reduces requirement and design risk early.

## When to Use

- When the solution space is still open or disputed
- When user workflows are hard to understand without concrete examples
- When ready-made products or platform choices must be compared
- When high-risk assumptions need to be tested before baselining requirements

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md` (recommended), `projects/<ProjectName>/<phase>/<document>/requirements_analysis_report.md` (optional) |
| **Output** | `projects/<ProjectName>/<phase>/<document>/solution_discovery_report.md` |
| **Tone** | Exploratory but disciplined, evidence-seeking |
| **Standards** | Volere discovery and prototype-driven requirements practices |

## Core Instructions

### Step 1: Define the Uncertainty

State:
- the problem being explored
- the assumptions most likely to be wrong
- the decision that the prototype or comparison must support

### Step 2: Generate Multiple Candidates

Produce at least three candidate solution directions when feasible:
- build custom
- configure or buy
- hybrid or phased option

For each candidate, define intended benefits, risks, and major constraints.

### Step 3: Define Prototype Strategy

Choose the smallest prototype type that can answer the question:
- paper or wireframe
- click-through UX
- workflow simulation
- proof-of-concept integration
- technical spike

### Step 4: Compare Candidates

Evaluate candidates against:
- business fit
- user fit
- technical feasibility
- implementation cost
- operational impact
- compliance or security risk

### Step 5: Record Learnings

For each prototype or experiment, document:
- hypothesis
- what was tested
- stakeholders involved
- findings
- decision impact
- follow-up work

### Step 6: Write Output

Write `projects/<ProjectName>/<phase>/<document>/solution_discovery_report.md` including candidates, prototype strategy, evaluation matrix, learnings, and recommendation.

## Common Pitfalls

- Treating a prototype as implicit approval for production implementation
- Testing visuals while leaving workflow or policy risks untouched
- Comparing options without agreed evaluation criteria
- Running discovery without recording what decision it should influence

## Verification Checklist

- [ ] The uncertainty or decision to resolve is explicit.
- [ ] More than one solution direction was considered where feasible.
- [ ] Prototype type matches the learning goal.
- [ ] Evaluation criteria include business and operational impact, not only UX.
- [ ] Findings lead to a recommendation or a clearly defined next experiment.

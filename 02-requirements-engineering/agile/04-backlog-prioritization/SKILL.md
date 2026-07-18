---
name: 04-backlog-prioritization
description: "Use when ranking an approved backlog with MoSCoW and WSJF and assigning release or sprint order; use story-mapping when the user journey and walking skeleton are not yet visible."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Backlog Prioritization Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- ranking an approved backlog with MoSCoW and WSJF and assigning release or sprint order; use story-mapping when the user journey and walking skeleton are not yet visible.
- Use this procedure when the required source artefacts are available and `Prioritised backlog and release allocation` is the next lifecycle deliverable.

## Do Not Use When

- Use `story-mapping` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Approved backlog, dependencies, capacity, cost of delay, and release goal | Product owner, delivery team, and business context | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Prioritised backlog and release allocation`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Prioritised backlog and release allocation | Sprint planning, product governance, and delivery team | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Prioritised backlog and release allocation` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. Editing is allowed only when the request authorises creation or repair of the named requirements artefact. Publishing, production mutation, destructive action, spending, and certification require explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A high-ranked item has no value, urgency, risk, or dependency evidence | Return it for scoring evidence instead of guessing a rank. | Priority theatre and unstable release commitments. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Prioritised backlog and release allocation` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Prioritised backlog and release allocation` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `story-mapping` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview

Run this skill after user stories, acceptance criteria, and (optionally) story mapping artifacts exist. It applies formal prioritization frameworks -- MoSCoW classification and Weighted Shortest Job First (WSJF) scoring -- to produce a ranked, sprint-allocated backlog and a milestone-driven release plan. Every prioritization decision is grounded in quantifiable business-goal alignment drawn from `vision.md`.

## When to Use This Skill

- After user stories have been generated by `01-user-story-generation`.
- Optionally after story mapping (`03-story-mapping`) provides journey context.
- When the team needs a data-driven sprint allocation rather than ad-hoc ordering.
- Before sprint planning begins to ensure the backlog reflects strategic priorities.

## Quick Reference

- **Inputs:** `projects/<ProjectName>/<phase>/<document>/user_stories.md`, `projects/<ProjectName>/_context/vision.md`, optionally `projects/<ProjectName>/<phase>/<document>/story_map.md`
- **Outputs:** `projects/<ProjectName>/<phase>/<document>/prioritized_backlog.md`, `projects/<ProjectName>/<phase>/<document>/release_plan.md`
- **Tone:** Analytical, data-driven, quantitative

## Input Files

| File | Source | Required? |
|------|--------|-----------|
| `user_stories.md` | `projects/<ProjectName>/<phase>/<document>/` | Yes |
| `vision.md` | `projects/<ProjectName>/_context/` | Yes |
| `story_map.md` | `projects/<ProjectName>/<phase>/<document>/` | Optional |

## Output Files

| File | Contents | Destination |
|------|----------|-------------|
| `prioritized_backlog.md` | MoSCoW classification, WSJF scores, dependency notes | `projects/<ProjectName>/<phase>/<document>/` |
| `release_plan.md` | Sprint-by-sprint allocation, milestones, capacity, risk flags | `projects/<ProjectName>/<phase>/<document>/` |

## Core Instructions

### Step 1: Read Inputs

Read `projects/<ProjectName>/<phase>/<document>/user_stories.md` and `projects/<ProjectName>/_context/vision.md`. If `projects/<ProjectName>/<phase>/<document>/story_map.md` exists, read it for journey and dependency context. Log every file path read.

### Step 2: MoSCoW Classification

Classify each user story into exactly one MoSCoW category:

| Category | Criterion |
|----------|-----------|
| **Must Have** | Blocks the MVP; without it the release has no value |
| **Should Have** | Delivers significant user or business value but MVP survives without it |
| **Could Have** | Nice-to-have enhancement; included only if capacity permits |
| **Won't Have** | Explicitly out of scope for this release; deferred to a future iteration |

### Step 3: Score WSJF Factors

For each story, score the following factors on a **1--10 integer scale** using business goals from `vision.md` as the alignment baseline:

- **Business Value (BV):** Degree of alignment with stated business goals.
- **Time Criticality (TC):** Market urgency or dependency-driven deadline pressure.
- **Risk Reduction (RR):** Technical or business risk mitigated by completing the story early.
- **Job Size (JS):** Story points as a proxy for effort (use the estimate from `user_stories.md`).

### Step 4: Calculate WSJF

Compute the WSJF score for each story:

$$WSJF = \frac{BV + TC + RR}{JS}$$

Higher WSJF indicates higher priority per unit of effort.

### Step 5: Sort Stories

Sort stories by WSJF score in descending order within each MoSCoW category. Must-Have stories appear first, followed by Should-Have, Could-Have, and Won't-Have.

### Step 6: Sprint Allocation

Allocate stories to sprints using an assumed velocity of **20 story points per sprint** (adjustable). Fill each sprint to capacity, placing higher-WSJF stories first.

### Step 7: Dependency Ordering

Review dependency chains across allocated sprints. Move blocking stories earlier in the plan so that no story is scheduled before its prerequisites. Flag any circular dependencies as `[DEP-CYCLE]`.

### Step 8: Generate Output Files

Write `projects/<ProjectName>/<phase>/<document>/prioritized_backlog.md` and `projects/<ProjectName>/<phase>/<document>/release_plan.md` following the output format below. Log story count, sprint count, and Must-Have percentage.

## Output Format

### prioritized_backlog.md

```markdown
# Prioritized Backlog: [Project Name]

**Generated:** [Date]
**Framework:** MoSCoW + WSJF (SAFe)
**Standards:** IEEE 29148-2018 Sec 6.4.6

---

## MoSCoW Summary

| Category   | Stories | Points | Percentage |
|------------|---------|--------|------------|
| Must Have  | N       | N      | N%         |
| Should Have| N       | N      | N%         |
| Could Have | N       | N      | N%         |
| Won't Have | N       | N      | N%         |

---

## WSJF Scoring Detail

| Story ID | Title | MoSCoW | BV | TC | RR | JS | WSJF  | Sprint |
|----------|-------|--------|----|----|----|----| ------|--------|
| US-001   | ...   | Must   | 9  | 8  | 7  | 3  | 8.00  | 1      |
| US-002   | ...   | Must   | 8  | 7  | 6  | 5  | 4.20  | 1      |

---

## Dependency Notes

- US-003 blocks US-007 (data model prerequisite).
- [Additional dependency annotations]
```

### release_plan.md

```markdown
# Release Plan: [Project Name]

**Generated:** [Date]
**Assumed Velocity:** 20 points/sprint

---

## Sprint Allocation

### Sprint 1 -- [Milestone Name] (N points / 20 capacity)

| Story ID | Title           | Points | MoSCoW | WSJF |
|----------|-----------------|--------|--------|------|
| US-001   | ...             | 3      | Must   | 8.00 |
| US-002   | ...             | 5      | Must   | 4.20 |

**Capacity Utilization:** N / 20 (N%)
**Risk Flags:** [None | list of risks]

### Sprint 2 -- [Milestone Name] (N points / 20 capacity)
[... continue for each sprint ...]

---

## Release Metrics

| Metric                | Value |
|-----------------------|-------|
| Total Stories         | N     |
| Total Sprints         | N     |
| Must-Have Coverage    | N%    |
| Average Utilization   | N%    |
```

## Common Pitfalls

- **Ignoring dependencies:** Scheduling a story before its blocker leads to sprint failure. Always enforce dependency ordering after WSJF sorting.
- **Equal-scoring everything:** If all stories receive identical BV/TC/RR scores, the WSJF ranking collapses. Force-rank by comparing stories against each other, not in isolation.
- **Unrealistic velocity:** Using an inflated velocity produces a plan the team cannot deliver. Default to 20 points/sprint and adjust only with historical data.
- **Omitting Won't-Have items:** Explicitly listing Won't-Have stories prevents scope creep by making exclusions visible to all stakeholders.

## Verification Checklist

- [ ] Every Must-Have story is allocated to a sprint.
- [ ] WSJF is calculated for every story with no division-by-zero (JS >= 1).
- [ ] No circular dependencies exist in the sprint plan.
- [ ] Sprint capacity does not exceed assumed velocity.
- [ ] MoSCoW percentages sum to 100%.
- [ ] Release plan includes risk flags for high-complexity or high-dependency stories.

## Integration

- **Upstream:** `01-user-story-generation`, `03-story-mapping`
- **Downstream:** `07-agile-artifacts/01-sprint-planning`

## Standards

- **IEEE Std 29148-2018** Section 6.4.6: Requirements prioritization and allocation.
- **SAFe WSJF Framework:** Weighted Shortest Job First for economic sequencing.
- **IEEE Std 610.12-1990:** Terminology definitions for requirement attributes.

## Resources

- `logic.prompt`: Prompt-level instructions for executing this skill.
- `README.md`: Quick-start summary and quality reminders.

---
**Last Updated:** 2026-02-28
**Skill Version:** 1.0.0

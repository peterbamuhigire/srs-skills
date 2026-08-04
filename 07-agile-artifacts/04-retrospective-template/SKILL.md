---
name: 04-retrospective-template
description: Use when facilitating a sprint retrospective that turns evidence into owned, time-bound improvement actions. Use sprint-planning for forward commitment and audit-report for an independent compliance review.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Retrospective Template Skill

<!-- dual-compat-start -->

## Use When

- Use when facilitating a sprint retrospective that turns evidence into owned, time-bound improvement actions. Use sprint-planning for forward commitment and audit-report for an independent compliance review.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Sprint goal and outcome; delivery metrics; spillover and incident records; stakeholder feedback; previous retrospective actions | Delivery team and product owner | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A concern could expose or punish an individual | Aggregate or anonymise it and focus on the system | Retaliation and suppressed learning |
| An improvement has an owner, due date, and measure | Adopt it and review it next sprint | Action lists that never change work |

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
| Retrospective Template | Product owner and delivery team | The session protects candour, separates evidence from attribution, and produces owned actions with due dates and measures. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Retrospective Template evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Retrospective Template from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a concern could expose or punish an individual, aggregate or anonymise it and focus on the system. Record the evidence and result in the validation record; this avoids retaliation and suppressed learning.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Kaizen retrospective and product loop](references/kaizen-retrospective-and-product-loop.md): use for value retrospectives, hypotheses, evidence, owners, and standardisation.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

This skill produces a reusable sprint retrospective template that structures the retrospective ceremony. It provides multiple facilitation formats (Start-Stop-Continue, 4Ls, Sailboat), action item tracking with ownership and deadlines, and continuous improvement metrics to ensure retrospectives drive measurable process improvement. The output conforms to the Scrum Guide.

## When to Use This Skill

- When establishing or refreshing the team's retrospective ceremony structure.
- After `vision.md` is present in `projects/<ProjectName>/_context/` for project context.
- At the end of each sprint to generate a fresh retrospective artifact.
- When the team wants to rotate facilitation formats to prevent ceremony fatigue.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/_context/vision.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Retrospective_Template.md` |
| **Standard** | Scrum Guide |
| **Time**    | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `projects/<ProjectName>/_context/vision.md` | Yes | Project goals and context for grounding retrospective themes |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Retrospective_Template.md | `projects/<ProjectName>/<phase>/<document>/Retrospective_Template.md` | Complete retrospective template with facilitation formats, action tracking, and metrics |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. Halt if the required file is missing.

### Step 2: Define Sprint Summary Section

Generate a sprint summary template that SHALL:
- Record the sprint number, date range, and sprint goal.
- Record team members who participated.
- Summarize sprint outcome (goal met, partially met, not met).
- Note velocity and any significant sprint events.

### Step 3: Define What Went Well Section

Generate a "What Went Well" section that SHALL:
- Provide a structured space for team members to record positive observations.
- Categorize observations by theme (process, collaboration, technical, delivery).
- Include a voting mechanism to identify top positive themes.
- Encourage specific examples rather than general statements.

### Step 4: Define What Could Be Improved Section

Generate a "What Could Be Improved" section that SHALL:
- Provide a structured space for team members to record improvement areas.
- Categorize observations by theme (process, collaboration, technical, delivery).
- Include a voting mechanism to prioritize improvement areas.
- Require specific, observable descriptions rather than blame-oriented statements.

### Step 5: Define Action Items Section

Generate an action item tracking section that SHALL:
- Capture each action item with a unique identifier.
- Assign an owner responsible for follow-through.
- Set a target completion date (typically before the next retrospective).
- Define a measurable success criterion for each action.
- Track status (open, in progress, completed, deferred).

### Step 6: Define Facilitation Formats

Generate three alternative facilitation formats the team can rotate through:

**Start-Stop-Continue:** Three columns for new practices to start, current practices to stop, and effective practices to continue. Each column SHALL require specific, actionable entries.

**4Ls (Liked, Learned, Lacked, Longed For):** Four quadrants capturing what the team liked, what they learned, what was lacking, and what they longed for. Each quadrant SHALL link observations to potential actions.

**Sailboat:** Visual metaphor with wind (helping forces), anchors (hindering forces), rocks (risks ahead), and island (sprint goal). Each element SHALL map to a concrete team experience from the sprint.

### Step 7: Define Improvement Metrics and Write Output

Generate a continuous improvement metrics section that SHALL:
- Track action item completion rate across sprints.
- Track recurring themes to identify systemic issues.
- Measure team satisfaction or morale trend (optional anonymous survey).
- Include a follow-up tracking table for previous sprint action items.
- Include the experiment hypothesis, baseline, guardrail, stop rule, result,
  decision, owner and next-cycle measure for the highest-priority action.
Assemble all sections into the final template. Write to `projects/<ProjectName>/<phase>/<document>/Retrospective_Template.md`. Log completion.

## Output Format Specification

The generated `Retrospective_Template.md` SHALL contain these sections in order:

1. **Document Header** -- project name, sprint number, date, standards reference
2. **Sprint Summary** -- sprint goal, outcome, participants, velocity
3. **What Went Well** -- categorized positive observations with voting
4. **What Could Be Improved** -- categorized improvement areas with voting
5. **Action Items** -- tracked items with owner, deadline, success criteria, status
6. **Facilitation Formats** -- Start-Stop-Continue, 4Ls, Sailboat templates
7. **Improvement Metrics** -- action completion rate, recurring themes, satisfaction trend
8. **Follow-Up Tracking** -- status of previous sprint action items

## Common Pitfalls

- Action items without owners or deadlines -- every action SHALL have an assigned owner and target date.
- Improvement areas stated as blame -- observations SHALL focus on process and outcomes, not individuals.
- No follow-up on previous actions -- the template SHALL include a section to review prior sprint actions.
- Single facilitation format causing ceremony fatigue -- the template SHALL provide at least three rotation options.
- Metrics not tracked across sprints -- the template SHALL include fields for cross-sprint trend tracking.

## Verification Checklist

1. `Retrospective_Template.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all eight sections populated.
2. Sprint summary captures goal, outcome, participants, and velocity.
3. "What Went Well" and "What Could Be Improved" sections include categorization and voting.
4. Every action item has an owner, deadline, and measurable success criterion.
5. At least three facilitation formats are documented with instructions.
6. Improvement metrics section tracks action completion rate and recurring themes.
7. Follow-up tracking section references previous sprint action items.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Project context (vision.md) | Consumes project goals for retrospective context |
| Lateral | 01-sprint-planning | Retrospective actions may inform next sprint planning |
| Lateral | 02-definition-of-done | Retrospective may refine DoD criteria |
| Downstream | Phase 09 (governance) | Retrospective metrics feed governance reporting |

## Standards Compliance

- **Scrum Guide** -- Governs the Sprint Retrospective as a ceremony for inspecting and adapting the team's process.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step retrospective template generation logic.
- `README.md` -- Quick-start guide for this skill.

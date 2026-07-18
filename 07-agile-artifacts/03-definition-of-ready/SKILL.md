---
name: 03-definition-of-ready
description: Use when defining the evidence a backlog item needs before sprint commitment, including acceptance criteria, sizing, dependencies, and design clarity. Use definition-of-done for completion criteria and sprint-planning for the sprint commitment.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Definition of Ready Skill

<!-- dual-compat-start -->

## Use When

- Use when defining the evidence a backlog item needs before sprint commitment, including acceptance criteria, sizing, dependencies, and design clarity. Use definition-of-done for completion criteria and sprint-planning for the sprint commitment.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Candidate backlog items; acceptance criteria; sizing method; dependency map; design evidence; product priority and sprint horizon | Product owner, analysts, designers, and delivery team | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A criterion lacks an observable test oracle | Rewrite it before adopting the checklist | Subjective gate decisions |
| Evidence satisfies every mandatory criterion | Record the item as ready or done, as applicable | Premature admission or completion |

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
| Definition of Ready | Product owner and delivery team | Every admitted item has testable acceptance criteria, a size, resolved or owned dependencies, and enough design evidence for commitment. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Definition of Ready evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Definition of Ready from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a criterion lacks an observable test oracle, rewrite it before adopting the checklist. Record the evidence and result in the validation record; this avoids subjective gate decisions.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

This skill produces a Definition of Ready (DoR) checklist that establishes the minimum refinement standard for backlog items before they can be committed to a sprint. It covers story completeness, acceptance criteria requirements, sizing and estimation, dependency resolution, and design clarity to prevent poorly defined work from entering a sprint. The output conforms to the Scrum Guide.

## When to Use This Skill

- When establishing or revising the team's readiness gate for backlog refinement.
- After `vision.md` is present in `projects/<ProjectName>/_context/` with project goals for context.
- When `features.md` is present in `projects/<ProjectName>/_context/` with feature definitions to inform readiness criteria.
- Before sprint planning to ensure backlog items meet readiness standards.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/features.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Definition_of_Ready.md` |
| **Standard** | Scrum Guide |
| **Time**    | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `projects/<ProjectName>/_context/vision.md` | Yes | Project goals and scope to ground readiness criteria |
| features.md | `projects/<ProjectName>/_context/features.md` | No | Feature definitions to inform story completeness and design clarity criteria |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Definition_of_Ready.md | `projects/<ProjectName>/<phase>/<document>/Definition_of_Ready.md` | Complete DoR checklist with refinement criteria and process guidance |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `projects/<ProjectName>/_context/`. Optionally read `features.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. Halt if the required file is missing.

### Step 2: Define Story Completeness Criteria

Generate story completeness checklist items that SHALL:
- Require a clear user story statement in "As a [role], I want [goal], so that [benefit]" format.
- Require a unique identifier assigned to the backlog item.
- Require a clear description of the business value or user need.
- Require the item to be linked to a project goal or feature in `vision.md`.

### Step 3: Define Acceptance Criteria Requirements

Generate acceptance criteria checklist items that SHALL:
- Require at least one acceptance criterion per backlog item.
- Require acceptance criteria written in Given-When-Then or equivalent testable format.
- Require acceptance criteria to cover the primary success path.
- Require acceptance criteria to cover at least one error or edge-case path.
- Require acceptance criteria reviewed and agreed upon by the product owner.

### Step 4: Define Sizing and Estimation Criteria

Generate sizing checklist items that SHALL:
- Require a story point estimate or time estimate assigned by the team.
- Require the item to be small enough to complete within a single sprint.
- Require items exceeding a team-defined threshold to be split before commitment.
- Require estimation to be performed by the development team, not assigned by others.

### Step 5: Define Dependency Resolution Criteria

Generate dependency resolution checklist items that SHALL:
- Require all external dependencies identified and documented.
- Require external dependencies to have a confirmed resolution date before the sprint ends.
- Require blocking dependencies resolved or a mitigation plan in place.
- Require third-party API contracts or interface agreements finalized.

### Step 6: Define Design Clarity Criteria

Generate design clarity checklist items that SHALL:
- Require UI/UX mockups or wireframes available for user-facing items.
- Require data model or schema changes identified.
- Require technical approach discussed and agreed upon by the team.
- Require non-functional requirements (performance, security) specified where applicable.

### Step 7: Define Refinement Process and Write Output

Generate a refinement process section describing how items move from "not ready" to "ready":
- Frequency and format of refinement sessions.
- Roles responsible for ensuring readiness.
- Escalation path for items that remain unready.
Assemble all sections into the final document. Write to `projects/<ProjectName>/<phase>/<document>/Definition_of_Ready.md`. Log completion.

## Output Format Specification

The generated `Definition_of_Ready.md` SHALL contain these sections in order:

1. **Document Header** -- project name, date, version, standards reference
2. **Story Completeness Criteria** -- user story format, identifier, business value, goal linkage
3. **Acceptance Criteria Requirements** -- testable format, success path, error path, PO agreement
4. **Sizing & Estimation Criteria** -- team estimate, sprint-sized, split threshold
5. **Dependency Resolution Criteria** -- identification, resolution dates, mitigation plans
6. **Design Clarity Criteria** -- mockups, data model, technical approach, NFRs
7. **Refinement Process** -- session cadence, responsible roles, escalation

## Common Pitfalls

- Acceptance criteria written as vague descriptions instead of testable statements -- every criterion SHALL use Given-When-Then or equivalent format.
- No size limit enforced -- items SHALL be required to fit within a single sprint.
- Dependencies left unresolved at sprint commitment -- every dependency SHALL have a confirmed resolution plan.
- Design clarity skipped for "simple" items -- the DoR SHALL apply uniformly to all backlog items.
- Refinement process undefined -- the DoR SHALL include guidance on how items reach readiness.

## Verification Checklist

1. `Definition_of_Ready.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all seven sections populated.
2. Story completeness requires user story format and goal linkage.
3. Acceptance criteria require Given-When-Then or equivalent testable format.
4. Sizing criteria require items to fit within a single sprint.
5. Dependency criteria require confirmed resolution dates or mitigation plans.
6. Design clarity criteria require mockups for user-facing items.
7. Refinement process defines session cadence and responsible roles.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Project context (vision.md, features.md) | Consumes project goals and feature definitions |
| Lateral | 02-definition-of-done | DoR and DoD form complementary quality gates |
| Lateral | 01-sprint-planning | Sprint planning consumes only "ready" items |
| Downstream | Phase 02 (backlog refinement) | DoR criteria guide the refinement process |

## Standards Compliance

- **Scrum Guide** -- Governs backlog refinement and the readiness standard for sprint commitment.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step DoR generation logic.
- `README.md` -- Quick-start guide for this skill.

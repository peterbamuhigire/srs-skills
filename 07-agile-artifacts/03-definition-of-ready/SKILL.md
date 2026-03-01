---
name: definition-of-ready
description: Generate a Definition of Ready checklist ensuring backlog items are sufficiently refined before sprint commitment per the Scrum Guide.
---

# Definition of Ready Skill

## Overview

This skill produces a Definition of Ready (DoR) checklist that establishes the minimum refinement standard for backlog items before they can be committed to a sprint. It covers story completeness, acceptance criteria requirements, sizing and estimation, dependency resolution, and design clarity to prevent poorly defined work from entering a sprint. The output conforms to the Scrum Guide.

## When to Use This Skill

- When establishing or revising the team's readiness gate for backlog refinement.
- After `vision.md` is present in `../project_context/` with project goals for context.
- When `features.md` is present in `../project_context/` with feature definitions to inform readiness criteria.
- Before sprint planning to ensure backlog items meet readiness standards.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../project_context/vision.md`, `../project_context/features.md` |
| **Output**  | `../output/Definition_of_Ready.md` |
| **Standard** | Scrum Guide |
| **Time**    | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `../project_context/vision.md` | Yes | Project goals and scope to ground readiness criteria |
| features.md | `../project_context/features.md` | No | Feature definitions to inform story completeness and design clarity criteria |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Definition_of_Ready.md | `../output/Definition_of_Ready.md` | Complete DoR checklist with refinement criteria and process guidance |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `../project_context/`. Optionally read `features.md` from `../project_context/`. Log the absolute path of each file read. Halt if the required file is missing.

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
Assemble all sections into the final document. Write to `../output/Definition_of_Ready.md`. Log completion.

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

1. `Definition_of_Ready.md` exists in `../output/` with all seven sections populated.
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

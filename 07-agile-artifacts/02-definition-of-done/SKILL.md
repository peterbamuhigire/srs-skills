---
name: "definition-of-done"
description: "Generate a Definition of Done checklist covering code quality, testing, documentation, review, and deployment readiness criteria per the Scrum Guide."
metadata:
  use_when: "Use when the task matches definition of done skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Definition of Done Skill

## Overview

This skill produces a comprehensive Definition of Done (DoD) checklist that establishes the quality bar for increments. It defines criteria across code quality, testing, documentation, review, and deployment readiness to ensure every product backlog item meets a consistent, verifiable standard before it can be considered complete. The output conforms to the Scrum Guide.

## When to Use This Skill

- When establishing or revising the team's quality gate for "done" increments.
- After `quality_standards.md` is present in `projects/<ProjectName>/_context/` with project-specific quality requirements.
- When `tech_stack.md` is present in `projects/<ProjectName>/_context/` to tailor criteria to the technology platform.
- Before sprint planning to ensure the team has a shared DoD reference.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/_context/quality_standards.md`, `projects/<ProjectName>/_context/tech_stack.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Definition_of_Done.md` |
| **Standard** | Scrum Guide |
| **Time**    | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| quality_standards.md | `projects/<ProjectName>/_context/quality_standards.md` | Yes | Project quality requirements, coding standards, coverage targets |
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | No | Technology choices to tailor criteria (linters, test frameworks, CI/CD tools) |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Definition_of_Done.md | `projects/<ProjectName>/<phase>/<document>/Definition_of_Done.md` | Complete DoD checklist with item-level, increment-level, and release-level criteria |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `quality_standards.md` from `projects/<ProjectName>/_context/`. Optionally read `tech_stack.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. Halt if the required file is missing.

### Step 2: Define Code Quality Criteria

Generate code quality checklist items that SHALL:
- Require code to compile and build without errors or warnings.
- Require adherence to the project coding standard defined in `quality_standards.md`.
- Require static analysis or linting to pass with zero violations.
- Require no known security vulnerabilities introduced.

### Step 3: Define Testing Criteria

Generate testing checklist items that SHALL:
- Require unit tests written and passing for all new and modified code.
- Require code coverage to meet or exceed the threshold in `quality_standards.md`.
- Require integration tests passing for affected interfaces.
- Require no regression in existing test suites.
- Require edge cases and error paths tested.

### Step 4: Define Documentation Criteria

Generate documentation checklist items that SHALL:
- Require inline code comments for non-obvious logic.
- Require API documentation updated for new or changed endpoints.
- Require user-facing documentation updated if behavior changes.
- Require changelog entry added for the increment.

### Step 5: Define Review Criteria

Generate review checklist items that SHALL:
- Require peer code review completed and approved.
- Require all review comments addressed or explicitly deferred with rationale.
- Require design review for architectural changes.
- Require product owner acceptance of acceptance criteria.

### Step 6: Define Deployment Criteria

Generate deployment readiness checklist items that SHALL:
- Require CI/CD pipeline passing all stages (build, test, scan).
- Require deployment to a staging environment verified.
- Require rollback procedure documented or confirmed.
- Require configuration changes documented per environment.

### Step 7: Define Increment-Level and Release-Level DoD

Generate higher-level DoD criteria:
- Increment-level: all selected backlog items meet item-level DoD, sprint goal validated, no critical defects open.
- Release-level: all increments meet increment-level DoD, release notes complete, performance benchmarks met, stakeholder sign-off obtained.

### Step 8: Assemble and Write Output

Assemble all criteria into the final checklist document. Write the completed document to `projects/<ProjectName>/<phase>/<document>/Definition_of_Done.md`. Log completion and total count of checklist items.

## Output Format Specification

The generated `Definition_of_Done.md` SHALL contain these sections in order:

1. **Document Header** -- project name, date, version, standards reference
2. **Code Quality Criteria** -- build, standards, static analysis, security
3. **Testing Criteria** -- unit, integration, coverage, regression, edge cases
4. **Documentation Criteria** -- comments, API docs, user docs, changelog
5. **Review Criteria** -- code review, design review, PO acceptance
6. **Deployment Criteria** -- CI/CD, staging verification, rollback, configuration
7. **Increment-Level DoD** -- aggregate criteria for sprint increments
8. **Release-Level DoD** -- aggregate criteria for production releases

## Common Pitfalls

- Vague criteria like "code is clean" -- every criterion SHALL be verifiable with a pass/fail outcome.
- Missing coverage thresholds -- testing criteria SHALL reference the specific percentage from `quality_standards.md`.
- No distinction between item, increment, and release levels -- the DoD SHALL define criteria at all three levels.
- Deployment readiness omitted -- the DoD SHALL include CI/CD and staging verification criteria.
- Criteria not tailored to the tech stack -- use `tech_stack.md` to reference specific tools and frameworks.

## Verification Checklist

1. `Definition_of_Done.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all eight sections populated.
2. Every criterion is verifiable with a clear pass/fail outcome.
3. Testing criteria reference specific coverage thresholds from `quality_standards.md`.
4. Code quality criteria reference the project coding standard.
5. Deployment criteria include CI/CD pipeline and staging verification.
6. Increment-level and release-level DoD criteria are present and distinct.
7. All criteria are stated using "SHALL" language for mandatory requirements.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Project context (quality_standards.md) | Consumes quality thresholds and coding standards |
| Lateral | 01-sprint-planning | Sprint plan references DoD artifact |
| Lateral | 03-definition-of-ready | DoR and DoD form complementary quality gates |
| Downstream | Phase 05 (test planning) | DoD testing criteria inform test plan scope |

## Standards Compliance

- **Scrum Guide** -- Governs the Definition of Done as a formal description of the state of the Increment when it meets quality measures.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step DoD generation logic.
- `README.md` -- Quick-start guide for this skill.

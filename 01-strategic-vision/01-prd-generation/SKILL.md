---
name: 01-prd-generation
description: Use when converting approved discovery evidence into a traceable PRD with objectives, prioritised features, success measures, constraints, and release scope; use vision-statement for the strategic north star and lean-canvas while assumptions still need testing.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# PRD Generation Skill
<!-- dual-compat-start -->
## Use When

- Discovery is sufficient to define product outcomes, users, feature priorities, measurable success and release boundaries.

## Do Not Use When

- Do not use to test an unvalidated business model; use `04-lean-canvas`. Do not use for implementation design; route approved requirements to Phase 03.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Project context and discovery evidence | `projects/<ProjectName>/_context/` and approved research | Required | Stop and list the missing discovery decisions; do not invent requirements. |
| Vision, scope and stakeholder decisions | Approved Phase 01 artefacts and decision log | Required | Mark unresolved conflicts and withhold affected requirements. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Product Requirements Document and manifest through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Product Requirements Document and manifest to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Product Requirements Document and manifest | Requirements, UX, architecture and delivery teams | Every feature traces to an objective and has a measurable acceptance or success condition; exclusions and open decisions are explicit. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Product Requirements Document and manifest draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Discovery maturity: Evidence resolves target user, problem and outcome | Write the PRD | Premature requirements harden guesses |
| Material assumption remains untested | Route it to the Lean Canvas hypothesis board | False certainty enters the backlog |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Writing a feature list without objective traceability. Fix: map each feature to a named objective and measure.
- Turning stakeholder wishes into requirements without evidence. Fix: label the source and decision owner.
- Using `high/medium/low` without a rule. Fix: apply the priority matrix in this skill.
- Hiding scope exclusions in prose. Fix: maintain an explicit out-of-scope register.
- Claiming a metric without a baseline or measurement method. Fix: name the baseline gap and instrumentation owner.

## References

- [SaaS PRD addendum](references/saas-prd-addendum.md)
- [AI feature PRD addendum](references/ai-feature-prd-addendum.md)
- [Generation logic](logic.prompt)
<!-- dual-compat-end -->




> **SaaS mode:** if the project is a multi-tenant SaaS, apply `references/saas-prd-addendum.md` in addition to the generic steps below.


## Overview

This is the second skill in Phase 01 (Strategic Vision). It builds on the Vision Statement to create a comprehensive Product Requirements Document (PRD) that bridges strategic intent and detailed requirements engineering. The PRD serves as the authoritative source for product scope, feature prioritization, and measurable objectives before downstream skills decompose features into formal SRS-level requirements.

## When to Use

- After the `03-vision-statement` skill has produced `Vision_Statement.md` in `projects/<ProjectName>/<phase>/<document>/`.
- Directly after `00-meta-initialization` if the team is working without a formal vision document but has populated `vision.md` and `features.md` in `projects/<ProjectName>/_context/`.

## Quick Reference

| Attribute   | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| **Inputs**  | `projects/<ProjectName>/_context/vision.md`, `features.md`, `stakeholders.md`; optionally `projects/<ProjectName>/<phase>/<document>/Vision_Statement.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/PRD.md`                                                    |
| **Tone**    | Strategic-technical, data-driven, no marketing language               |
| **Standards** | IEEE 29148-2018, IEEE 1233-1998                                    |

## Input Files

| File                  | Location                        | Required | Purpose                                      |
|-----------------------|---------------------------------|----------|----------------------------------------------|
| vision.md             | `projects/<ProjectName>/_context/vision.md`  | Yes      | Business goals, problem statement, constraints|
| features.md           | `projects/<ProjectName>/_context/features.md`| Yes      | Feature list with descriptions                |
| stakeholders.md       | `projects/<ProjectName>/_context/stakeholders.md` | Yes | User roles, personas, stakeholder groups      |
| Vision_Statement.md   | `projects/<ProjectName>/<phase>/<document>/Vision_Statement.md` | No       | Enriches executive summary and market context |

## Output Files

| File    | Location             | Description                                           |
|---------|----------------------|-------------------------------------------------------|
| PRD.md  | `projects/<ProjectName>/<phase>/<document>/PRD.md`   | Complete Product Requirements Document with all sections |

## Core Instructions

Follow these nine steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md`, `features.md`, and `stakeholders.md` from `projects/<ProjectName>/_context/`. Optionally read `Vision_Statement.md` from `projects/<ProjectName>/<phase>/<document>/`. Log every file path read. If `vision.md` or `features.md` is missing, halt execution and report the gap.

### Step 2: Generate Document Header

Write the document header containing:
- Project name (from `vision.md`)
- Version: `1.0`
- Date: current date
- Authors: extracted from context or marked `[AUTHOR-TBD]`
- Document Status: `Draft`

### Step 3: Generate Executive Summary

Write one paragraph in active voice that distills the product purpose, the primary user segment it serves, and the key value proposition. Avoid superlatives and marketing language.

### Step 4: Generate Market Context

- **Problem Space**: Extract directly from the Problem Statement in `vision.md`.
- **Target Market Segments**: Derive from `stakeholders.md` user roles and domains.
- **Competitive Landscape**: Infer from domain constraints and technology choices. Flag any assertions that lack grounding with `[INFERRED]`.
- **Premium Positioning**: If the product targets premium, affluent, executive, enterprise, luxury, high-ticket, or elite users, load `../07-premium-product-positioning/SKILL.md` and apply its requirements gate before finalising market context, feature priorities, success metrics, or release strategy.

### Step 5: Generate Product Objectives

Create one objective per business goal listed in `vision.md`. Each objective shall follow SMART format:
- **S**pecific: what exactly will be achieved
- **M**easurable: quantitative metric
- **A**chievable: feasibility note
- **R**elevant: link to business goal
- **T**ime-bound: target date or release

Flag any goal that lacks a measurable metric with `[METRIC-TBD]`.

### Step 6: Generate Target Users and Personas

From `stakeholders.md`, produce a summary of user segments including:
- Persona name and role
- Key characteristics and goals
- Pain points relevant to the product
- Usage frequency and technical proficiency

### Step 7: Generate Feature Priority Matrix

Produce a table with the following columns:

| Feature | Description | Priority | Effort | Value | MoSCoW | Rationale |
|---------|-------------|----------|--------|-------|--------|-----------|

- **Priority**: Critical / High / Medium / Low (by business impact)
- **Effort**: S / M / L / XL (by technical complexity)
- **Value**: High / Medium / Low (by user benefit)
- **MoSCoW**: Must / Should / Could / Won't (by MVP criticality)
- **Rationale**: one sentence justifying the classification

Every feature in `features.md` shall appear in this table.

### Step 8: Generate Success Metrics

Define 3-5 Key Performance Indicators. Each KPI shall include:

| KPI | Baseline | Target | Measurement Method | Timeline |
|-----|----------|--------|--------------------|----------|

Flag unknown baselines with `[BASELINE-TBD]`.

### Step 9: Generate Remaining Sections and Write Output

- **Constraints and Dependencies**: Budget, timeline, technology, and regulatory constraints from `vision.md`. External system dependencies and API integrations.
- **Release Strategy**: Phased rollout plan mapping features to releases by priority tier.
- **Standards Traceability Appendix**: Table mapping each PRD section to the corresponding IEEE 29148-2018 and IEEE 1233-1998 clause numbers.

Write the completed document to `projects/<ProjectName>/<phase>/<document>/PRD.md`. Log the total section count and feature count.

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in this document's directory listing the section files in the correct assembly order:

```markdown
# Document Manifest — PRD
# Generated by prd-generation. Edit to reorder or exclude sections before building.
01-purpose.md
02-scope.md
03-stakeholders.md
04-features.md
05-constraints.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Output Format

The generated `PRD.md` shall follow this template structure:

```
# Product Requirements Document: [Project Name]

## Document Header
## 1. Executive Summary
## 2. Market Context
### 2.1 Problem Space
### 2.2 Target Market Segments
### 2.3 Competitive Landscape
## 3. Product Objectives
## 4. Target Users and Personas
## 5. Feature Priority Matrix
## 6. Success Metrics
## 7. Constraints and Dependencies
### 7.1 Constraints
### 7.2 Dependencies
## 8. Release Strategy
## 9. Standards Traceability
## Appendix A: Glossary
```

## Common Pitfalls

1. **Solution bias in the problem statement**: Describe the problem, not the solution. The PRD defines *what* and *why*, not *how*.
2. **Unmeasurable objectives**: Every objective needs a metric. If one cannot be defined, flag it explicitly.
3. **Missing feature rationale**: A priority without justification is an opinion. Every row in the matrix requires a Rationale entry.
4. **Vague success metrics**: "Improve performance" is not a KPI. Specify baseline, target, and method.

## Verification Checklist

- [ ] All required input files were read and logged.
- [ ] Every business goal in `vision.md` maps to at least one SMART objective.
- [ ] Every feature in `features.md` appears in the Feature Priority Matrix with all columns populated.
- [ ] Success Metrics include baseline, target, method, and timeline for each KPI.
- [ ] No marketing language or subjective adjectives appear without a defined metric.
- [ ] Standards Traceability appendix maps sections to IEEE 29148 and IEEE 1233 clauses.

## Integration

| Direction  | Skill                       | Relationship                              |
|------------|-----------------------------|-------------------------------------------|
| Upstream   | `01-strategic-vision/03-vision-statement` | Consumes Vision_Statement.md     |
| Downstream | `01-strategic-vision/02-business-case`    | Feeds objectives and metrics     |
| Downstream | `02-requirements-engineering`             | Feeds feature list for SRS decomposition |

## Standards

- **IEEE 29148-2018**: Systems and software engineering -- Life cycle processes -- Requirements engineering. Governs the structure and content of requirements documentation.
- **IEEE 1233-1998**: Guide for Developing System Requirements Specifications. Provides guidance on well-formed requirements and traceability.

## Resources

- `logic.prompt` -- executable prompt for automated PRD generation.
- `README.md` -- quick-start guide for this skill.

## Strategic foundations check (added 2026-05-04 from Levy + Branson)

Canonical reference: `docs/ux-foundations.md` Sections 1 and 2.

Three checks before producing or finalizing the PRD:

### 1. Four Tenets check (Levy)

Verify the upstream artifacts and PRD scope contain evidence for all four tenets:

| Tenet | PRD section | Pass criterion |
|---|---|---|
| **Business Strategy** | Strategic context / problem statement | Value proposition declared with revenue model |
| **Value Innovation** | Differentiation / competitive context | Specific differentiation vs named competitors, not generic claims |
| **Validated User Research** | User segments / personas | Personas cite real research, not pure hypothesis |
| **Killer UX Design** | Success criteria / UX requirements | UX outcomes specified, not implied |

If any tenet lacks evidence, the PRD is "speculative" — return to upstream stage rather than ship a polished but unfounded PRD.

### 2. Persona discipline (Branson, Section 1)

The PRD's persona section must:
- Declare ONE Essential Persona per primary user role (no averaging)
- Include the full Mechanics floor (name, demographics, goals, environment, pain points, stress points)
- Use specific, named personas in feature-justification arguments — "Persona X needs Y" — not "users want Y"

### 3. Field-of-Dreams flag (Levy)

If the PRD contains no validated user research and no plan to acquire it, mark the PRD itself as "speculative." Speculative PRDs cannot be priced as execution engagements; they must precede a discovery engagement. Document the speculative-status banner at the top of the PRD.

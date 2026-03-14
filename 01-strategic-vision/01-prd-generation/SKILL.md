---
name: prd-generation
description: Generate a Product Requirements Document with market context, objectives, success metrics, and feature priority matrix per IEEE 29148 and IEEE 1233.
---

# PRD Generation Skill

## Overview

This is the second skill in Phase 01 (Strategic Vision). It builds on the Vision Statement to create a comprehensive Product Requirements Document (PRD) that bridges strategic intent and detailed requirements engineering. The PRD serves as the authoritative source for product scope, feature prioritization, and measurable objectives before downstream skills decompose features into formal SRS-level requirements.

## When to Use

- After the `03-vision-statement` skill has produced `Vision_Statement.md` in `../output/`.
- Directly after `00-meta-initialization` if the team is working without a formal vision document but has populated `vision.md` and `features.md` in `../project_context/`.

## Quick Reference

| Attribute   | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| **Inputs**  | `../project_context/vision.md`, `features.md`, `stakeholders.md`; optionally `../output/Vision_Statement.md` |
| **Output**  | `../output/PRD.md`                                                    |
| **Tone**    | Strategic-technical, data-driven, no marketing language               |
| **Standards** | IEEE 29148-2018, IEEE 1233-1998                                    |

## Input Files

| File                  | Location                        | Required | Purpose                                      |
|-----------------------|---------------------------------|----------|----------------------------------------------|
| vision.md             | `../project_context/vision.md`  | Yes      | Business goals, problem statement, constraints|
| features.md           | `../project_context/features.md`| Yes      | Feature list with descriptions                |
| stakeholders.md       | `../project_context/stakeholders.md` | Yes | User roles, personas, stakeholder groups      |
| Vision_Statement.md   | `../output/Vision_Statement.md` | No       | Enriches executive summary and market context |

## Output Files

| File    | Location             | Description                                           |
|---------|----------------------|-------------------------------------------------------|
| PRD.md  | `../output/PRD.md`   | Complete Product Requirements Document with all sections |

## Core Instructions

Follow these nine steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md`, `features.md`, and `stakeholders.md` from `../project_context/`. Optionally read `Vision_Statement.md` from `../output/`. Log every file path read. If `vision.md` or `features.md` is missing, halt execution and report the gap.

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

Write the completed document to `../output/PRD.md`. Log the total section count and feature count.

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

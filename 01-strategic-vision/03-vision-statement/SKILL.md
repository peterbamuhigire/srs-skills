---
name: "vision-statement"
description: "Generate a formal project vision document with elevator pitch, product positioning, value propositions, and success criteria per IEEE 29148 Sec 6.2."
metadata:
  use_when: "Use when the task matches 03-vision-statement skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# 03-Vision-Statement Skill

## Overview

This is the first skill to run in Phase 01: Strategic Vision. It transforms raw project context into a formal, structured vision document that establishes the strategic anchor for all downstream documentation. The output conforms to IEEE 29148-2018 Sec 6.2 and uses terminology defined by IEEE 610.12-1990.

## When to Use

- After 00-meta-initialization has produced `methodology.md` in `projects/<ProjectName>/_context/`.
- Before running 01-prd-generation or any requirements engineering skill.
- Whenever the project vision needs to be formalized or updated from raw context files.

## Quick Reference

| Field | Value |
|-------|-------|
| **Inputs** | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/stakeholders.md`, `projects/<ProjectName>/_context/glossary.md` |
| **Output** | `projects/<ProjectName>/<phase>/<document>/Vision_Statement.md` |
| **Tone** | Strategic but precise; no marketing language; active voice |
| **Standard** | IEEE 29148-2018 Sec 6.2 |

## Input Files

| File | Required | Purpose |
|------|----------|---------|
| `projects/<ProjectName>/_context/vision.md` | Yes | Problem statement, target users, business goals, constraints |
| `projects/<ProjectName>/_context/stakeholders.md` | Yes | Stakeholder roles, segments, goals, technical proficiency |
| `projects/<ProjectName>/_context/glossary.md` | Recommended | Domain terminology per IEEE 610.12-1990 |

## Output Files

| File | Description |
|------|-------------|
| `projects/<ProjectName>/<phase>/<document>/Vision_Statement.md` | Formal vision document with elevator pitch, positioning, value propositions, success criteria, and scope boundaries |

## Core Instructions

Follow these eight steps in order. Do not skip or reorder.

### Step 1: Read Context Files

Read `vision.md`, `stakeholders.md`, and `glossary.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. If `vision.md` is missing, halt execution and report the gap to the user.

### Step 2: Extract Core Elements

Extract the following from `vision.md`, capturing each verbatim before synthesis:
- Problem Statement
- Target Users
- Business Goals
- Constraints

### Step 3: Map Stakeholders to User Segments

Cross-reference `stakeholders.md` with the target users identified in Step 2. For each user segment, note the role, primary goals, and technical proficiency level.

### Step 4: Generate Elevator Pitch

Write exactly 2-3 sentences using active voice. State the problem, the solution, and the key differentiator. No superlatives or marketing language.

### Step 5: Generate Product Positioning Statement

Use Geoffrey Moore's positioning template:

> For [target users] who [statement of need], the [product name] is a [product category] that [key benefit]. Unlike [primary alternative], our product [primary differentiation].

### Step 6: Generate Value Propositions

Write 3-5 value propositions. Each shall state a measurable outcome tied to a business goal from `vision.md`. Use the format:

> [The system] shall [deliver outcome] resulting in [measurable benefit].

### Step 7: Define Success Criteria

Write success criteria using the SMART framework (Specific, Measurable, Achievable, Relevant, Time-bound). Present as a table with columns: Criterion, Metric, Baseline, Target, Timeline. If a baseline is unknown, flag it with `[BASELINE-TBD]`.

### Step 8: Define Scope Boundaries

Produce two tables:
- **In-Scope:** Item and Description.
- **Out-of-Scope:** Item and Rationale for exclusion. Every exclusion shall state why it was excluded.

## Output Format Specification

The generated `Vision_Statement.md` shall contain the following sections in order:

### Section 1: Document Header

```
# Vision Statement: [Project Name]
- **Date:** [YYYY-MM-DD]
- **Version:** [X.Y]
- **Authors:** [Names]
- **Standard:** IEEE 29148-2018 Sec 6.2
```

### Section 2: Elevator Pitch

Two to three sentences. Active voice. No superlatives.

### Section 3: Product Positioning Statement

Geoffrey Moore template as defined in Step 5.

### Section 4: Value Propositions

Numbered list. Each entry includes a measurable outcome.

### Section 5: Target Audience

Table of user segments with columns: Segment, Role, Primary Goals, Technical Proficiency.

### Section 6: Success Criteria

SMART table with columns: Criterion, Metric, Baseline, Target, Timeline.

### Section 7: Scope Boundaries

Two sub-tables: In-Scope (Item, Description) and Out-of-Scope (Item, Rationale).

### Section 8: Assumptions and Risks

- **Assumptions:** Statements taken as true without current verification.
- **Risks:** Factors that could prevent success, each with probability (High/Medium/Low) and impact (High/Medium/Low).

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in this document's directory listing the section files in the correct assembly order:

```markdown
# Document Manifest — Vision Statement
# Generated by vision-statement. Edit to reorder or exclude sections before building.
01-problem-statement.md
02-product-vision.md
03-goals.md
04-success-criteria.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Marketing language instead of engineering prose | Remove superlatives; use active voice with concrete terms |
| Unmeasurable success criteria | Apply SMART framework; every criterion needs a numeric target |
| Vague scope boundaries | Every out-of-scope item must state a rationale for exclusion |
| Missing stakeholder segments | Cross-reference stakeholders.md against vision.md target users |

## Verification Checklist

Before marking this skill as complete, confirm all of the following:

- [ ] `Vision_Statement.md` exists in `projects/<ProjectName>/<phase>/<document>/`
- [ ] Elevator pitch is 2-3 sentences with no superlatives
- [ ] Every value proposition has a measurable outcome
- [ ] All success criteria follow SMART format with Criterion, Metric, Baseline, Target, Timeline
- [ ] Scope boundaries list a rationale for each exclusion
- [ ] Document references IEEE 29148 Sec 6.2

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 00-meta-initialization | Requires `methodology.md` in `projects/<ProjectName>/_context/` |
| Downstream | 01-prd-generation | Consumes `Vision_Statement.md` to build PRD |
| Downstream | 02-requirements-engineering | Uses vision and positioning to derive requirements |

## Standards

- **IEEE 29148-2018 Sec 6.2** — Vision and scope documentation structure
- **IEEE 610.12-1990** — Terminology definitions for all domain terms

## Resources

- `logic.prompt` — Executable prompt containing the step-by-step generation logic
- `README.md` — Quick-start guide for this skill

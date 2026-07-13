---
name: 03-vision-statement
description: Use when a project needs a concise strategic north star defining target users, problem, differentiated value, success and scope boundaries; use lean-canvas to test uncertain assumptions and PRD generation to specify approved product behaviour.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# 03-Vision-Statement Skill
<!-- dual-compat-start -->
## Use When

- Stakeholders need one stable vision before a business case, PRD or SRS is drafted.

## Do Not Use When

- Do not use for feature-level requirements, financial approval or architecture decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Raw project context | `projects/<ProjectName>/_context/` | Required | Stop if the user, problem or sponsor outcome cannot be identified. |
| Stakeholder priorities | Sponsor interviews and approved decisions | Required | Record disagreements as open decisions instead of averaging them. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Vision Statement and manifest through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Vision Statement and manifest to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Vision Statement and manifest | Sponsor, product team and downstream documentation skills | A reader can identify user, problem, value, success test, in-scope boundary and exclusions without consulting hidden context. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Vision Statement and manifest draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| One user/problem/outcome is supported | Write a focused vision | Downstream teams share a north star |
| Competing visions remain | Present alternatives and request sponsor selection | Consensus wording conceals conflict |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Writing a slogan instead of a decision. Fix: name user, problem and measurable outcome.
- Listing every stakeholder as the target. Fix: identify the primary beneficiary and secondary stakeholders.
- Using motivational adjectives as differentiation. Fix: state the concrete alternative and advantage.
- Omitting exclusions to keep everyone pleased. Fix: define scope boundaries explicitly.
- Inventing success targets. Fix: use approved targets or label the metric as awaiting baseline.

## References

- [Generation logic](logic.prompt)
- [PRD generation neighbour](../01-prd-generation/SKILL.md)
- [Lean Canvas neighbour](../04-lean-canvas/SKILL.md)
<!-- dual-compat-end -->




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

## Vision-statement filter (added 2026-05-04 from Levy)

Canonical reference: `docs/ux-foundations.md` Section 2 (Top-10 Not-UX-Strategies).

Reject any vision statement that matches one of Levy's anti-patterns. Most common SRS-context failures, in order of frequency:

### #10 — The North Star
**Symptom:** "Be the [Uber / Airbnb / Stripe] of [industry]." No operational meaning. Reads like a slogan.
**Fix:** rewrite to describe the *change* the product creates in the user's life — what specifically becomes possible that wasn't before?

### #9 — The Hallmark-card affirmation
**Symptom:** "Deliver excellence, innovation, and customer delight." Too vague to act on. Cannot be operationalized into requirements.
**Fix:** name the specific user, the specific change, the specific evidence that the change has happened.

### #4 — The buzzword permutation
**Symptom:** "AI-powered Web3 platform for the metaverse." Trends concatenated. No customer in the sentence.
**Fix:** drop every buzzword that doesn't directly describe what the user does or experiences.

### #5 — Generic motivational statement
**Symptom:** "Empower every team, every day, everywhere." Could fit any product.
**Fix:** make it falsifiable — what would prove this is happening, and what would prove it isn't?

### #1 — The killer idea
**Symptom:** "Our killer idea is X." Idea-as-vision. No persona, no problem, no validation.
**Fix:** rewrite as user-problem + observable outcome.

### Procedure when a draft matches an anti-pattern

Return to the interview/discovery stage. Do not polish the prose of an anti-pattern vision statement; the underlying thinking has not happened yet. Document the rejection and the path back in the project log so the rework is auditable.

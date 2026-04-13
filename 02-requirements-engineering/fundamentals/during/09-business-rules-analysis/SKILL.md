---
name: "business-rules-analysis"
description: "Capture, classify, normalize, and validate business rules so policy, calculations, decisions, and constraints are explicit before specification and design."
metadata:
  use_when: "Use when the task matches business rules analysis and this skill's local workflow."
  do_not_use_when: "Do not use when the project has no meaningful domain logic beyond simple CRUD validation or when rules are already formalized elsewhere."
  required_inputs: "Provide business context, elicitation artifacts, process models, and any existing policies, calculations, or compliance constraints."
  workflow: "Follow the ordered discovery, classification, normalization, and validation steps before using the rules downstream."
  quality_standards: "Keep rules testable, source-attributed, exception-aware, and separated from implementation detail."
  anti_patterns: "Do not hide business rules inside prose paragraphs, user stories, or UI mockups without a catalog."
  outputs: "Produce a normalized business rules catalog with sources, classifications, examples, and downstream impacts."
  references: "Use `references/` when deeper detail is needed."
---

# Business Rules Analysis Skill

## Overview

This skill isolates the domain rules that govern decisions, calculations, constraints, eligibility, timing, and compliance. It prevents rule logic from being buried inside requirements prose or code assumptions and turns it into a reviewable catalog that can drive requirements, test cases, and design controls.

## When to Use

- When requirements depend on policy, eligibility, pricing, approval, compliance, or timing logic
- When multiple stakeholders describe the same rule differently
- When calculations, thresholds, or conditional decisions affect acceptance criteria
- Before formal SRS logic modeling or workflow design is finalized

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `../output/elicitation_log.md`, `../output/business_process_models.md` (recommended), `../project_context/business_rules.md` (optional), `vision.md` |
| **Output** | `../output/business_rules_catalog.md` |
| **Tone** | Precise, policy-aware, test-oriented |
| **Standards** | Wiegers & Beatty, Volere-style rule analysis |

## Core Instructions

### Step 1: Discover Candidate Rules

Extract candidate rules from:
- stakeholder statements
- process decisions
- compliance obligations
- calculations and thresholds
- timing or sequencing constraints
- exception handling

### Step 2: Classify the Rules

Classify each rule as one of:
- policy rule
- decision rule
- calculation rule
- validation rule
- compliance rule
- temporal rule

### Step 3: Normalize Each Rule

For each rule, capture:
- rule ID
- plain-language statement
- source or authority
- triggering condition
- action or expected outcome
- exception or override path
- example scenario

See `references/rule-catalog-pattern.md` for a normalized row structure.

### Step 4: Detect Rule Problems

Flag:
- contradictory rules
- duplicate rules
- rules without a named source
- rules with no measurable fit or test condition
- rules embedded as implementation choices rather than business intent

### Step 5: Map Rules Downstream

For each rule, identify its effect on:
- functional requirements
- non-functional constraints
- process controls
- test scenarios
- data model or audit needs

### Step 6: Write Output

Write `../output/business_rules_catalog.md` with the normalized rule catalog, issue log, and downstream mapping.

## Output Format

1. Rule inventory summary
2. Classified rule catalog
3. Contradictions and gaps
4. Downstream requirement and test impacts
5. Open questions and source gaps

## Common Pitfalls

- Mixing business policy with UI or implementation detail
- Omitting rule sources, making disputes impossible to resolve
- Recording rules without examples or exceptions
- Leaving calculations untestable or unit-less

## Verification Checklist

- [ ] Every rule has an ID and classification.
- [ ] Every rule has a source or is flagged as needing confirmation.
- [ ] Exceptions or overrides are documented where relevant.
- [ ] Contradictions and duplicates are identified.
- [ ] Downstream requirement and test impacts are mapped.

## References

- `references/rule-catalog-pattern.md` -- Normalized business rule structure and review prompts

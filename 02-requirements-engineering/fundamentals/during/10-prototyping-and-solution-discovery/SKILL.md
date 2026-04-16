---
name: "prototyping-and-solution-discovery"
description: "Generate and compare candidate solutions, prototypes, and discovery experiments to reduce uncertainty before locking requirements or design."
metadata:
  use_when: "Use when the task matches prototyping and solution discovery and this skill's local workflow."
  do_not_use_when: "Do not use when the solution is already fixed by regulation, procurement, or a non-negotiable platform decision."
  required_inputs: "Provide the problem statement, goals, stakeholder context, feature scope, and key unknowns or design risks."
  workflow: "Follow the candidate generation, prototype, comparison, and learning-loop steps before converging on the chosen approach."
  quality_standards: "Keep outputs hypothesis-driven, comparison-based, and explicit about what was learned versus what remains unproven."
  anti_patterns: "Do not treat the first idea as the only option or confuse a prototype with production-ready design."
  outputs: "Produce a solution discovery report with candidate options, prototype plan, findings, and decision rationale."
  references: "Use sibling files in this directory when deeper detail is needed."
---

# Prototyping And Solution Discovery Skill

## Overview

This skill creates structured candidate solutions and prototype-driven learning before the project commits to a detailed design. It supports sacrificial prototypes, ready-made solution evaluation, comparison matrices, and explicit learning loops so the engine reduces requirement and design risk early.

## When to Use

- When the solution space is still open or disputed
- When user workflows are hard to understand without concrete examples
- When ready-made products or platform choices must be compared
- When high-risk assumptions need to be tested before baselining requirements

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/<phase>/<document>/stakeholder_register.md` (recommended), `projects/<ProjectName>/<phase>/<document>/requirements_analysis_report.md` (optional) |
| **Output** | `projects/<ProjectName>/<phase>/<document>/solution_discovery_report.md` |
| **Tone** | Exploratory but disciplined, evidence-seeking |
| **Standards** | Volere discovery and prototype-driven requirements practices |

## Core Instructions

### Step 1: Define the Uncertainty

State:
- the problem being explored
- the assumptions most likely to be wrong
- the decision that the prototype or comparison must support

### Step 2: Generate Multiple Candidates

Produce at least three candidate solution directions when feasible:
- build custom
- configure or buy
- hybrid or phased option

For each candidate, define intended benefits, risks, and major constraints.

### Step 3: Define Prototype Strategy

Choose the smallest prototype type that can answer the question:
- paper or wireframe
- click-through UX
- workflow simulation
- proof-of-concept integration
- technical spike

### Step 4: Compare Candidates

Evaluate candidates against:
- business fit
- user fit
- technical feasibility
- implementation cost
- operational impact
- compliance or security risk

### Step 5: Record Learnings

For each prototype or experiment, document:
- hypothesis
- what was tested
- stakeholders involved
- findings
- decision impact
- follow-up work

### Step 6: Write Output

Write `projects/<ProjectName>/<phase>/<document>/solution_discovery_report.md` including candidates, prototype strategy, evaluation matrix, learnings, and recommendation.

## Common Pitfalls

- Treating a prototype as implicit approval for production implementation
- Testing visuals while leaving workflow or policy risks untouched
- Comparing options without agreed evaluation criteria
- Running discovery without recording what decision it should influence

## Verification Checklist

- [ ] The uncertainty or decision to resolve is explicit.
- [ ] More than one solution direction was considered where feasible.
- [ ] Prototype type matches the learning goal.
- [ ] Evaluation criteria include business and operational impact, not only UX.
- [ ] Findings lead to a recommendation or a clearly defined next experiment.

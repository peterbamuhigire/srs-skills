---
name: "solution-evaluation-and-transition"
description: "Plan organizational transition, go/no-go evidence, adoption readiness, and post-implementation solution evaluation after requirements and delivery artifacts exist."
metadata:
  use_when: "Use when the task matches solution evaluation and transition and this skill's local workflow."
  do_not_use_when: "Do not use when the project is still in early discovery and there is no credible implementation or release baseline to evaluate."
  required_inputs: "Provide requirements, validation, testing, deployment, stakeholder, and operational context needed to assess transition and solution performance."
  workflow: "Follow the transition, readiness, adoption, evaluation, and evidence steps before making a release or implementation recommendation."
  quality_standards: "Keep outputs evidence-based, adoption-aware, and explicit about readiness gaps, residual risk, and success measures."
  anti_patterns: "Do not equate feature completion with organizational readiness or ignore adoption and operational ownership."
  outputs: "Produce a transition and evaluation plan with readiness evidence, adoption actions, go/no-go framing, and performance measures."
  references: "Use sibling files in this directory when deeper detail is needed."
---

# Solution Evaluation And Transition Skill

## Overview

This skill closes the gap between completed requirements or delivery artifacts and real organizational adoption. It plans transition activities, readiness evidence, go/no-go framing, post-implementation evaluation, and success measurement so the engine supports actual solution rollout, not only analysis and design.

## When to Use

- When requirements, design, testing, or deployment artifacts are mature enough for rollout planning
- Before a pilot, cutover, or formal go/no-go decision
- When the project changes user behavior, operating procedures, or support responsibilities
- After early release to define solution performance evaluation criteria

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `../output/validation_report.md`, `../output/Deployment_Guide.md` (optional), `../output/Runbook.md` (optional), `../output/Test_Report.md` (optional), `../output/stakeholder_register.md` |
| **Output** | `../output/solution_evaluation_transition_plan.md` |
| **Tone** | Operational, adoption-focused, evidence-based |
| **Standards** | PMI BA transition and solution evaluation practices |

## Core Instructions

### Step 1: Assess Transition Scope

Document who must change, including:
- end users
- approvers or supervisors
- support teams
- operations teams
- downstream systems or partners

### Step 2: Define Readiness Evidence

Collect evidence required for transition:
- requirement and test coverage
- unresolved defect or risk summary
- training or enablement readiness
- support and operations readiness
- rollback and cutover preparedness

### Step 3: Plan Organizational Transition

Specify:
- training activities
- communications
- cutover sequence
- support model during hypercare
- ownership after handoff

### Step 4: Frame the Go/No-Go Decision

State:
- go criteria
- no-go triggers
- conditional-go criteria
- approvers
- evidence package required

### Step 5: Define Solution Evaluation Measures

Define post-launch evaluation measures:
- adoption
- task completion
- error or defect rate
- operational burden
- user satisfaction
- business outcome measures tied to project goals

### Step 6: Write Output

Write `../output/solution_evaluation_transition_plan.md` with transition actions, readiness gaps, decision criteria, and evaluation metrics.

## Common Pitfalls

- Launching without naming operational owners
- Treating training as optional for behavior-changing systems
- Using vague go/no-go criteria
- Measuring only delivery output instead of actual solution performance

## Verification Checklist

- [ ] Transition-affected groups are identified.
- [ ] Readiness evidence is defined and reviewed.
- [ ] Go/no-go criteria are explicit and measurable.
- [ ] Adoption, support, and hypercare plans are documented.
- [ ] Post-implementation evaluation metrics are tied to goals.

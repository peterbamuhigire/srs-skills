---
name: "business-process-modeling"
description: "Model as-is and to-be business processes, actors, handoffs, exceptions, and control points to clarify requirements before detailed specification or design."
metadata:
  use_when: "Use when the task matches business process modeling and this skill's local workflow."
  do_not_use_when: "Do not use when the project has no meaningful workflow complexity or when use-case modeling alone is sufficient."
  required_inputs: "Provide elicitation artifacts, stakeholder context, feature scope, and any known process constraints or business rules."
  workflow: "Follow the process discovery, modeling, exception, and validation steps in this file before finalizing the process model."
  quality_standards: "Keep outputs workflow-accurate, traceable to stakeholder input, and explicit about exceptions, handoffs, and control points."
  anti_patterns: "Do not flatten complex workflows into happy-path prose or confuse system functions with business process steps."
  outputs: "Produce as-is and to-be process models with narrative, actors, exceptions, and requirement implications."
  references: "Use `references/` when deeper detail is needed."
---

# Business Process Modeling Skill

## Overview

This skill turns workflow knowledge into structured process models that expose roles, handoffs, triggers, decisions, exceptions, controls, and improvement opportunities. It complements use cases and user stories by modeling the business flow itself rather than only system interactions.

## When to Use

- When the solution changes or automates existing business processes
- When handoffs, approvals, queues, or exception handling are central to the problem
- When stakeholders disagree on current-state workflow or future-state ownership
- Before detailed requirements for multi-role workflows are finalized

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `../output/elicitation_log.md`, `../output/stakeholder_register.md`, `../project_context/features.md`, `../project_context/business_rules.md` (optional) |
| **Output** | `../output/business_process_models.md` |
| **Tone** | Analytical, operational, role-aware |
| **Standards** | BPM-inspired process analysis, PMI BA practice guidance |

## Core Instructions

### Step 1: Inventory Target Processes

Identify each high-value or high-risk business process affected by the project. For each process, define:
- trigger event
- primary actor
- downstream actors
- business outcome
- business cost if the process fails

### Step 2: Model the Current State

For each process, document the current workflow:
- start trigger
- ordered activities
- actor ownership
- decisions and branching
- data created or consumed
- manual work, delays, and rework points

### Step 3: Model the Future State

Create the target workflow showing:
- what is automated
- what remains manual
- new controls or approvals
- new exception flows
- changed ownership or timing

See `references/modeling-patterns.md` for notation guidance.

### Step 4: Capture Exceptions and Negative Paths

Every process model shall include:
- alternate paths
- exception paths
- abandoned or failed flow handling
- escalation or override conditions

If the model only describes the happy path, flag it with `[PROCESS-GAP: exception handling missing]`.

### Step 5: Extract Requirement Implications

For each process step or decision point, derive:
- candidate functional requirements
- business rules that require separate capture
- interfaces or notifications
- audit or traceability needs
- metrics or SLAs implied by the process

### Step 6: Validate with Stakeholders

Record validation questions for each process:
- Is the current state accurate?
- Is the future state acceptable?
- What exceptions are still missing?
- Which controls are mandatory vs negotiable?

### Step 7: Write Output

Write `../output/business_process_models.md` containing current-state and future-state models, exception flows, and requirement implications.

## Output Format

1. Process inventory
2. As-is models
3. To-be models
4. Exceptions and control points
5. Requirement implications
6. Open questions
7. Standards traceability

## Common Pitfalls

- Modeling only screens or APIs instead of the business flow
- Ignoring manual workarounds, queues, and approvals
- Omitting exception paths and escalation rules
- Failing to connect process steps to requirements or controls

## Verification Checklist

- [ ] Every target process has a trigger, actors, and outcome.
- [ ] Current-state and future-state workflows are both documented.
- [ ] Exceptions and control points are explicit.
- [ ] Requirement implications are extracted from the models.
- [ ] Stakeholder validation questions are included.

## References

- `references/modeling-patterns.md` -- As-is/to-be workflow and exception modeling guidance

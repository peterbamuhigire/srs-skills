# Hybrid Operating Model

This repository supports Hybrid delivery, but Hybrid is not "run Agile and Waterfall side by side and hope they line up." This document defines the operating contract.

## Purpose

Use this model when a project needs formal upstream governance or regulated scope control while still delivering portions of the system iteratively.

Typical cases:

- regulated backend plus fast-moving user interface work
- contractual scope baseline plus iterative release slicing
- architecture or compliance gates that must stay stable while product details evolve

## Canonical Workspace Model

Hybrid projects still use the same canonical workspace:

- `projects/<ProjectName>/_context/`
- `projects/<ProjectName>/01-strategic-vision/...`
- `projects/<ProjectName>/02-requirements-engineering/...`
- `projects/<ProjectName>/07-agile-artifacts/...`

If a skill-local file references `../project_context/` or `../output/`, those are execution aliases into the active project workspace, not a second architecture.

## Hybrid Contract

1. **Single source of truth for business context**
   - Vision, features, stakeholders, glossary, business rules, and quality standards live under `projects/<ProjectName>/_context/`.

2. **Formal baseline for stable concerns**
   - Regulated, safety-sensitive, integration-heavy, or contractually fixed capabilities should be baselined through Phase 01 and Phase 02 before implementation.
   - These become the controlled scope boundary for Agile execution.

3. **Iterative execution for volatile concerns**
   - UX, workflow refinement, backlog slicing, release planning, and delivery sequencing can continue through Agile artifacts as long as they do not violate the controlled baseline without change control.

4. **Change-control handshake**
   - If an Agile discovery changes a baselined requirement, route the change through requirements management and traceability before accepting it into a sprint.

5. **Shared trace IDs**
   - Requirement IDs, story IDs, design IDs, and test IDs must remain linkable across both the formal and iterative tracks.

## Recommended Operating Patterns

### Pattern A: Formal Core, Agile Edge

- Use Waterfall requirements for data model, APIs, compliance, security, and reporting.
- Use Agile stories for UI flow, onboarding, dashboards, and lower-risk enhancements.

### Pattern B: Baseline Then Iterate

- Establish PRD, core SRS, architecture, and initial test strategy.
- Shift into Agile sprint planning with Definitions of Ready and Done tied back to baseline IDs.

### Pattern C: Release Train with Governance Gates

- Use Agile increments for delivery cadence.
- Use Phase 05, Phase 06, and Phase 09 gates for release approval and audit evidence.

## Minimum Artifacts for Real Hybrid Support

A project should not be described as Hybrid-ready unless these exist:

- `projects/<ProjectName>/_context/methodology.md`
- controlled scope or requirements baseline
- backlog or user story set with IDs
- traceability matrix linking baseline items to Agile execution artifacts
- definitions of ready and done that reference compliance and design constraints
- release or go-live gate evidence

## Anti-Patterns

- Calling a project Hybrid when no controlled baseline exists
- Running Agile stories that silently diverge from approved requirements
- Treating backlog priority as a substitute for change control
- Claiming auditability without a linked trace chain

## Completion Rule

Hybrid support is only "complete" for a project when the Waterfall-style governance artifacts and Agile execution artifacts are linked through shared identifiers, explicit change control, and deterministic gates.

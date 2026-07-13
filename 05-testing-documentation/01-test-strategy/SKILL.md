---
name: 01-test-strategy
description: Use when producing or updating project test strategy for risk-based test levels, test types, environments, tooling, entry criteria, and exit criteria. Use test-plan for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Test Strategy Skill

<!-- dual-compat-start -->
## Use When

- Produce or update project test strategy from approved project evidence.
- Resolve decisions about risk-based test levels, test types, environments, tooling, entry criteria, and exit criteria.
- Prepare a reviewable handoff for QA lead and delivery manager.

## Do Not Use When

- The task is primarily owned by test-plan; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Project Test Strategy | QA lead and delivery manager | Every critical requirement and quality risk maps to a test family, environment, owner, and measurable exit criterion. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose test depth from product risk and requirement criticality and produce the full artefact. | Coverage that is broad but not risk-based. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring test-plan concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every critical requirement and quality risk maps to a test family, environment, owner, and measurable exit criterion.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
> **SaaS mode:** if the project is a multi-tenant SaaS, apply `references/saas-test-strategy-addendum.md` in addition to the generic steps below.


## Overview

This is the first skill in Phase 05 (Testing Documentation). It reads the SRS and HLD to produce a comprehensive test strategy that defines test levels (Unit, Integration, System, UAT), test types (functional, performance, security, accessibility), tooling selections, environment configurations, and entry/exit criteria. The output establishes the quality assurance framework that governs all downstream testing artifacts and conforms to BS ISO/IEC/IEEE 29119-3 Section 6.

## When to Use

- After Phase 02 completes and `SRS_Draft.md` exists in `projects/<ProjectName>/<phase>/<document>/` with functional and non-functional requirements.
- After Phase 03 completes and `HLD.md` exists in `projects/<ProjectName>/<phase>/<document>/` with system architecture and component boundaries.
- When `quality_standards.md` exists in `projects/<ProjectName>/_context/` with project-specific quality targets.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/_context/quality_standards.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Test_Strategy.md` |
| **Tone**    | Prescriptive, standards-driven, QA-facing |
| **Standard** | BS ISO/IEC/IEEE 29119-3 Sec 6 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| SRS_Draft.md | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Yes | Functional and non-functional requirements driving test scope |
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes | System architecture defining component boundaries for integration testing |
| quality_standards.md | `projects/<ProjectName>/_context/quality_standards.md` | Yes | Project-specific quality targets, compliance mandates, and coverage thresholds |

### Methodology Fallback (Agile / Hybrid)

If `SRS_Draft.md` is absent, Claude shall use the following agile-compatible inputs instead:

| Agile Input | Replaces | Notes |
|---|---|---|
| `user_stories.md` | `SRS_Draft.md` | Use accepted stories as the test scope source |
| `acceptance_criteria.md` | SRS functional requirements | Given-When-Then criteria map directly to test cases |
| `tech_stack.md` | `HLD.md` | Derive architecture context from stack when HLD is absent |

**Detection logic:** At execution start, check for `SRS_Draft.md`:
- If found → proceed with standard waterfall path
- If absent → check for `user_stories.md`; if found → switch to agile path and note in the generated Test Strategy document: *"This test strategy is scoped to the agile user story backlog per IEEE 829-2008 Section 4.1 (scope flexibility)."*
- If neither exists → halt and instruct consultant to run Phase 02 first

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Test_Strategy.md | `projects/<ProjectName>/<phase>/<document>/Test_Strategy.md` | Complete test strategy with levels, types, tools, environments, and criteria |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `SRS_Draft.md` and `HLD.md` from `projects/<ProjectName>/<phase>/<document>/` and `quality_standards.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. If any required file is missing, halt execution and report the gap.

### Step 2: Define Test Levels

Define four test levels derived from the HLD component architecture: Unit (individual module logic), Integration (inter-module communication paths from HLD), System (end-to-end workflows from SRS functional requirements), and UAT (business validation against stakeholder acceptance criteria). Each level shall state its scope, responsible role, and automation expectation.

### Step 3: Define Test Types

Define test types aligned with SRS requirement categories: Functional (SRS Section 3.2 features), Performance (SRS Section 3.3 targets), Security (SRS Section 3.5 constraints), and Accessibility (WCAG or equivalent standards from quality_standards.md). Each type shall reference the specific SRS section it validates.

### Step 4: Select Testing Tools

Select testing tools and frameworks appropriate to the technology stack documented in HLD. For each tool, state its purpose, the test level it serves, and its integration method (CLI, CI pipeline plugin, IDE extension). Do not recommend tools without justifying their fit to the project stack.

### Step 5: Define Test Environments

Define test environments required for each test level: local developer environments for unit tests, staging environments for integration and system tests, and a UAT environment mirroring production configuration. Each environment shall specify infrastructure requirements and data provisioning strategy.

### Step 6: Define Entry and Exit Criteria

Define entry criteria (conditions that shall be met before testing begins at each level) and exit criteria (conditions that shall be met before testing is declared complete at each level). Entry criteria shall include build stability and prerequisite test-level completion. Exit criteria shall include pass-rate thresholds and defect-count limits from quality_standards.md.

### Step 7: Define Defect Management and Metrics

Define the defect management process: severity taxonomy (Critical, Major, Minor, Trivial), priority taxonomy (P1-P4), defect lifecycle states (Open, In Progress, Resolved, Verified, Closed), and escalation rules. Define test metrics including coverage targets, pass-rate thresholds, defect density limits, and mean-time-to-resolution targets. All thresholds shall trace to quality_standards.md.

Before writing the artifact, confirm the deterministic gate by checking `../references/29119-deterministic-checks.md`. Use it to prove each required document exists and references the relevant 29119 clause.

### Step 8: Write Output with Traceability

Write the completed document to `projects/<ProjectName>/<phase>/<document>/Test_Strategy.md`. Include a traceability section mapping each test level and test type to the SRS sections and quality_standards.md targets they validate. Log the total count of test levels, test types, and tools selected.

## Output Format

The generated `Test_Strategy.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Test Scope, 2. Test Levels, 3. Test Types, 4. Tools and Frameworks, 5. Environments, 6. Entry/Exit Criteria, 7. Defect Management, 8. Test Metrics, 9. Risks and Mitigations, Appendix A: Traceability to Quality Standards.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Test levels without clear scope boundaries | Each level shall state exactly which artifacts and components it covers |
| Tools selected without stack justification | Every tool recommendation shall reference the HLD technology stack |
| Entry/exit criteria without measurable thresholds | Every criterion shall include a numeric target or boolean condition |
| Missing defect severity definitions | The severity taxonomy shall define impact criteria for each level |

## Verification Checklist

- [ ] `Test_Strategy.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all nine sections populated.
- [ ] Four test levels are defined with scope, responsible role, and automation expectation.
- [ ] Test types reference specific SRS sections they validate.
- [ ] Tool selections cite the HLD technology stack as justification.
- [ ] Entry and exit criteria include measurable thresholds from quality_standards.md.
- [ ] Defect severity and priority taxonomies are fully defined.
- [ ] Test metrics include coverage targets and pass-rate thresholds.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 02 (Requirements Engineering) | Consumes `SRS_Draft.md` for test scope derivation |
| Upstream | Phase 03 (01-high-level-design) | Consumes `HLD.md` for architecture-driven test levels |
| Downstream | 02-test-plan | Feeds test levels, types, and criteria framework for test case generation |
| Downstream | 03-test-report | Feeds metrics definitions and criteria for report template structure |

## Standards

- **BS ISO/IEC/IEEE 29119-3** -- Current international standard for test documentation; governs the structure of organizational and project-level test strategies (Section 6).

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step test strategy generation logic.
- `README.md` -- Quick-start guide for this skill.

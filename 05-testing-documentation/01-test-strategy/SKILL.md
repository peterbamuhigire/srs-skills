---
name: "test-strategy"
description: "Generate an overall test strategy defining test levels, types, tools, environments, and entry/exit criteria per BS ISO/IEC/IEEE 29119-3 Section 6."
metadata:
  use_when: "Use when the task matches test strategy skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Test Strategy Skill

## Overview

This is the first skill in Phase 05 (Testing Documentation). It reads the SRS and HLD to produce a comprehensive test strategy that defines test levels (Unit, Integration, System, UAT), test types (functional, performance, security, accessibility), tooling selections, environment configurations, and entry/exit criteria. The output establishes the quality assurance framework that governs all downstream testing artifacts and conforms to BS ISO/IEC/IEEE 29119-3 Section 6.

## When to Use

- After Phase 02 completes and `SRS_Draft.md` exists in `../output/` with functional and non-functional requirements.
- After Phase 03 completes and `HLD.md` exists in `../output/` with system architecture and component boundaries.
- When `quality_standards.md` exists in `../project_context/` with project-specific quality targets.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/quality_standards.md` |
| **Output**  | `../output/Test_Strategy.md` |
| **Tone**    | Prescriptive, standards-driven, QA-facing |
| **Standard** | BS ISO/IEC/IEEE 29119-3 Sec 6 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| SRS_Draft.md | `../output/SRS_Draft.md` | Yes | Functional and non-functional requirements driving test scope |
| HLD.md | `../output/HLD.md` | Yes | System architecture defining component boundaries for integration testing |
| quality_standards.md | `../project_context/quality_standards.md` | Yes | Project-specific quality targets, compliance mandates, and coverage thresholds |

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
| Test_Strategy.md | `../output/Test_Strategy.md` | Complete test strategy with levels, types, tools, environments, and criteria |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `SRS_Draft.md` and `HLD.md` from `../output/` and `quality_standards.md` from `../project_context/`. Log the absolute path of each file read. If any required file is missing, halt execution and report the gap.

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

Write the completed document to `../output/Test_Strategy.md`. Include a traceability section mapping each test level and test type to the SRS sections and quality_standards.md targets they validate. Log the total count of test levels, test types, and tools selected.

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

- [ ] `Test_Strategy.md` exists in `../output/` with all nine sections populated.
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

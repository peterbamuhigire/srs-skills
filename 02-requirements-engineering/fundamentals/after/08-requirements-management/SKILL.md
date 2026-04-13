---
name: "requirements-management"
description: "Establish requirements baselines, change control processes, and version management for living requirements documents per IEEE 29148 Section 6.7."
metadata:
  use_when: "Use when the task matches requirements management skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `references/` when deeper detail is needed."
---

# Requirements Management Skill Guidance

## Overview

Run this skill after all requirements artifacts have been generated and validated. It establishes a formal baseline snapshot, defines the change control process for ongoing requirements evolution, and creates version history tracking. Every requirements document is a living artifact; this skill ensures changes are governed, traceable, and auditable.

## When to Use This Skill

- After all requirements elicitation, analysis, specification, and validation skills have completed.
- When requirements artifacts in `../output/` have reached a stable state suitable for baselining.
- Before development begins, to lock down the initial requirements baseline.
- Whenever a new baseline is needed after a controlled batch of changes.

## Quick Reference

- **Inputs:** All artifacts in `../output/`, `../project_context/vision.md`, `../project_context/stakeholder_register.md`
- **Outputs:** `../output/requirements_baseline.md`, `../output/change_control_process.md`
- **Tone:** Formal, procedural, governance-oriented

## Input Files

| File | Source | Required? |
|------|--------|-----------|
| All `*.md` artifacts | `../output/` | Yes |
| `vision.md` | `../project_context/` | Yes |
| `stakeholder_register.md` | `../project_context/` | Optional |

## Output Files

| File | Contents | Destination |
|------|----------|-------------|
| `requirements_baseline.md` | Versioned snapshot of all requirements with state tracking | `../output/` |
| `change_control_process.md` | Change request format, impact analysis, approval workflow | `../output/` |

## Core Instructions

### Step 1: Read All Output Artifacts

Read every file in `../output/` and `../project_context/vision.md`. Log each file path read. Catalog every requirement identifier found across all artifacts. If no requirement identifiers exist, halt and report `[MGMT-FAIL]: No requirement identifiers found in output artifacts`.

### Step 2: Create Requirements Inventory

Build a complete inventory of all requirements by scanning output artifacts for requirement identifiers (e.g., REQ-xxx, FR-xxx, NFR-xxx, US-xxx). For each requirement, record:

- **Requirement ID:** The unique identifier.
- **Title:** Brief descriptive title.
- **Source Artifact:** The file where the requirement is defined.
- **Current State:** One of the defined requirement states (see Step 4).
- **Priority:** As assigned by upstream skills.
- **Last Modified:** Date of last change.

### Step 3: Create Baseline Snapshot

Generate a baseline snapshot with:

- **Baseline ID:** Format `BL-[PROJECT]-[VERSION]` (e.g., `BL-SRS-1.0.0`).
- **Baseline Date:** The date of snapshot creation.
- **Version Identifier:** Semantic versioning (MAJOR.MINOR.PATCH) per the baselining guide.
- **Included Artifacts:** List of every file included in the baseline with SHA-256 hash.
- **Requirements Count:** Total requirements, grouped by type (functional, non-functional, constraint).
- **Baseline Authority:** The individual or board that approved the baseline.

Version numbering follows these rules:
- **MAJOR:** Scope change affecting project objectives or stakeholder agreements.
- **MINOR:** Addition, modification, or deletion of individual requirements within existing scope.
- **PATCH:** Corrections to wording, formatting, or metadata that do not alter requirement intent.

### Step 4: Define Requirement States

Every requirement shall transition through these states:

| State | Definition | Entry Criteria | Exit Criteria |
|-------|-----------|----------------|---------------|
| Draft | Newly elicited, not yet reviewed | Requirement identified | Submitted for review |
| Under Review | Being evaluated by stakeholders | Review initiated | Review complete |
| Approved | Accepted for implementation | Stakeholder sign-off | Allocated to baseline |
| Implemented | Coded and unit-tested | Development complete | Ready for verification |
| Verified | Passed acceptance testing | Test execution complete | All tests pass |
| Retired | No longer applicable | Retirement approved | Removed from active baseline |

State transitions shall be recorded with: timestamp, actor, previous state, new state, and justification.

### Step 5: Define Change Control Process

Document the change control process with these components:

#### 5a: Change Request Format

Each change request shall contain:

| Field | Description |
|-------|-------------|
| CR-ID | Unique change request identifier (CR-[NNN]) |
| Requester | Name and role of the person requesting the change |
| Date Submitted | Date the request was filed |
| Affected Requirements | List of requirement IDs impacted |
| Description | What the change entails |
| Rationale | Business or technical justification |
| Impact Analysis | Scope, schedule, cost, risk, and dependency impacts |
| Priority | Critical, High, Medium, Low |
| Disposition | Approved, Rejected, Deferred, Merged |

#### 5b: Impact Analysis Template

For each change request, the impact analysis shall address:

1. **Scope Impact:** Which requirements, artifacts, and baselines are affected.
2. **Schedule Impact:** Estimated effort in hours and effect on milestones.
3. **Cost Impact:** Resource and budget implications.
4. **Risk Impact:** New risks introduced or existing risks modified.
5. **Dependency Impact:** Upstream and downstream requirements affected.
6. **Test Impact:** Test cases requiring creation, modification, or retirement.

#### 5c: Approval Workflow

1. **Submission:** Requester submits CR with all mandatory fields.
2. **Triage:** Requirements Manager assigns priority and routes to Change Control Board (CCB).
3. **Analysis:** Assigned analyst completes impact analysis within 5 business days.
4. **Review:** CCB reviews CR with impact analysis and stakeholder input.
5. **Decision:** CCB records disposition (Approved/Rejected/Deferred/Merged).
6. **Implementation:** Approved changes are incorporated and baseline is updated.
7. **Verification:** Changes are verified against acceptance criteria.

#### 5d: Change Control Board Roles

| Role | Responsibility |
|------|---------------|
| CCB Chair | Convenes meetings, manages agenda, records decisions |
| Product Owner | Represents business value and stakeholder priorities |
| Technical Lead | Assesses technical feasibility and architecture impact |
| QA Lead | Evaluates test impact and verification requirements |
| Requirements Manager | Maintains baseline integrity and traceability |

### Step 6: Establish Version History Tracking

Create a version history log that records every baseline change:

| Version | Date | Author | Changes Summary | Approval Status | Linked CRs |
|---------|------|--------|-----------------|-----------------|-------------|
| 1.0.0 | [Date] | [Author] | Initial baseline | Approved | N/A |

### Step 7: Generate Output Files

Write `../output/requirements_baseline.md` and `../output/change_control_process.md` following the output format below.

## Output Format

### requirements_baseline.md

```markdown
# Requirements Baseline: [Project Name]

**Baseline ID:** BL-[PROJECT]-[VERSION]
**Created:** [Date]
**Version:** [MAJOR.MINOR.PATCH]
**Authority:** [Approver Name / CCB]
**Standards:** IEEE 29148-2018 Sec 6.7, IEEE 830-1998

---

## Baseline Summary

| Metric | Value |
|--------|-------|
| Total Requirements | N |
| Functional Requirements | N |
| Non-Functional Requirements | N |
| Constraints | N |
| Requirements in Draft | N |
| Requirements Approved | N |
| Requirements Verified | N |

---

## Requirements Inventory

| Req ID | Title | Type | State | Priority | Source Artifact |
|--------|-------|------|-------|----------|----------------|
| REQ-001 | ... | Functional | Approved | High | SRS_Draft.md |

---

## Included Artifacts

| File | SHA-256 Hash | Last Modified |
|------|-------------|---------------|
| SRS_Draft.md | [hash] | [date] |

---

## Version History

| Version | Date | Author | Changes | Status | CRs |
|---------|------|--------|---------|--------|-----|
| 1.0.0 | [Date] | [Author] | Initial baseline | Approved | N/A |
```

### change_control_process.md

```markdown
# Change Control Process: [Project Name]

**Created:** [Date]
**Standards:** IEEE 29148-2018 Sec 6.7, Wiegers Practices 15-17

---

## Change Request Template

| Field | Value |
|-------|-------|
| CR-ID | CR-[NNN] |
| Requester | [Name, Role] |
| Date Submitted | [Date] |
| Affected Requirements | [REQ-xxx, REQ-yyy] |
| Description | [What changes] |
| Rationale | [Why the change is needed] |
| Priority | [Critical/High/Medium/Low] |
| Disposition | [Pending/Approved/Rejected/Deferred] |

---

## Impact Analysis

[Scope, schedule, cost, risk, dependency, and test impact]

---

## Approval Workflow

[Seven-step workflow from submission to verification]

---

## Change Control Board

[CCB roles and responsibilities]

---

## Requirement States

[State transition table with entry/exit criteria]
```

## Common Pitfalls

- **Skipping the baseline:** Without a formal baseline, there is no reference point to measure change against. Always create the initial baseline before development starts.
- **Informal change requests:** Verbal or email-only change requests bypass impact analysis. Every change shall use the CR template.
- **State drift:** Requirements that change state without recorded transitions break audit trails. Enforce mandatory transition logging.
- **Version confusion:** Inconsistent version numbering creates ambiguity about which baseline is current. Follow semantic versioning strictly.

## Verification Checklist

- [ ] Every requirement in `../output/` has a unique identifier in the inventory.
- [ ] Baseline ID follows the `BL-[PROJECT]-[VERSION]` format.
- [ ] Version numbering uses semantic versioning (MAJOR.MINOR.PATCH).
- [ ] All six requirement states are defined with entry and exit criteria.
- [ ] Change request template contains all mandatory fields.
- [ ] Impact analysis covers scope, schedule, cost, risk, dependency, and test dimensions.
- [ ] Approval workflow defines clear CCB roles and decision process.
- [ ] Version history log is initialized with the baseline entry.

## Integration

- **Upstream:** All elicitation, specification, and validation skills
- **Downstream:** `09-traceability-engineering`, `10-requirements-metrics`

## Standards

- **IEEE Std 29148-2018** Section 6.7: Requirements management processes.
- **IEEE Std 830-1998:** Recommended practice for SRS documentation.
- **Laplante Ch.7:** Requirements management and change control.
- **Wiegers Practices 15-17:** Configuration management, change control, status tracking.
- **IEEE Std 610.12-1990:** Terminology definitions.

## Resources

- `references/change-control-process.md`: Change request template and CCB workflow.
- `references/baselining-guide.md`: Baseline creation protocol and version numbering.
- `references/version-history-template.md`: Version history log format.

---
**Last Updated:** 2026-03-07
**Skill Version:** 1.0.0

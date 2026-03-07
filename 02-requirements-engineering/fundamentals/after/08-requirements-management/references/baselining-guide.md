# Requirements Baselining Guide

**Purpose:** Define the protocol for creating, versioning, and managing requirements baselines including snapshot procedures, diff generation, and rollback.

**Standards:** IEEE 29148-2018 Sec 6.7, IEEE 828-2012

---

## What Is a Requirements Baseline?

A requirements baseline is a formally approved, time-stamped snapshot of all requirements artifacts at a specific point in the project lifecycle. Once established, a baseline serves as the official reference point against which all subsequent changes are measured. Changes to a baselined requirement shall only occur through the change control process.

---

## What to Include in a Baseline

A complete baseline shall include every artifact that defines, constrains, or validates requirements:

### Mandatory Inclusions

| Artifact Type | Examples | Rationale |
|---------------|----------|-----------|
| Requirements Specifications | SRS_Draft.md, functional requirements, NFRs | Core requirements content |
| Traceability Artifacts | traceability_matrix.md | Ensures link integrity is captured |
| Validation Artifacts | Audit_Report.md, metrics reports | Quality evidence at baseline time |
| Stakeholder Agreements | Approved scope statements, sign-off records | Authorization evidence |

### Optional Inclusions

| Artifact Type | Examples | Rationale |
|---------------|----------|-----------|
| Agile Artifacts | user_stories.md, prioritized_backlog.md | Sprint-level requirements (if Agile) |
| Interface Specifications | External/internal interface definitions | Boundary agreements |
| Data Dictionaries | Data models, entity definitions | Data requirement context |
| Glossaries | Project-specific terminology | Disambiguation reference |

### Exclusions

- Working drafts that have not completed review.
- Personal notes or informal communications.
- Source code or implementation artifacts (these belong in code configuration management).

---

## Version Numbering Scheme

Baselines shall use semantic versioning: **MAJOR.MINOR.PATCH**

### Version Increment Rules

| Level | When to Increment | Examples |
|-------|-------------------|----------|
| MAJOR | Scope change that alters project objectives, stakeholder agreements, or system boundaries | Adding a new subsystem, removing a major feature, changing target users |
| MINOR | Addition, modification, or deletion of individual requirements within the existing scope | New functional requirement, modified NFR threshold, retired requirement |
| PATCH | Corrections to wording, formatting, cross-references, or metadata that do not alter requirement intent | Typo fix, reformatted table, updated stakeholder name |

### Version Format

```
BL-[PROJECT_CODE]-[MAJOR].[MINOR].[PATCH]
```

Examples:
- `BL-SRS-1.0.0` -- Initial baseline.
- `BL-SRS-1.1.0` -- Added three new functional requirements.
- `BL-SRS-1.1.1` -- Corrected typo in REQ-005 description.
- `BL-SRS-2.0.0` -- Major scope revision after stakeholder re-negotiation.

### Pre-Release Identifiers

For baselines under review but not yet approved:

```
BL-[PROJECT_CODE]-[VERSION]-RC[N]
```

Example: `BL-SRS-1.1.0-RC1` (Release Candidate 1 for version 1.1.0).

---

## Baseline Creation Protocol

### Step 1: Pre-Baseline Verification

Before creating a baseline, verify:

- [ ] All requirements have unique identifiers.
- [ ] All requirements have an assigned state (Draft, Under Review, Approved, etc.).
- [ ] The traceability matrix has been updated.
- [ ] The quality gate (Skill 10) has been executed and passes at YELLOW or above.
- [ ] All open change requests for this release have been resolved (Approved, Rejected, or Deferred).
- [ ] Stakeholder review and sign-off has been obtained.

### Step 2: Snapshot Creation

1. Compile all artifacts listed in the "What to Include" section.
2. Generate a SHA-256 hash for each artifact file to enable tamper detection.
3. Record the following metadata for each artifact:

| Field | Value |
|-------|-------|
| File Name | [artifact filename] |
| File Path | [relative path from project root] |
| SHA-256 Hash | [computed hash] |
| Last Modified | [file modification timestamp] |
| Line Count | [number of lines] |
| Requirements Count | [number of requirement IDs in the file] |

4. Assign the baseline ID using the version numbering scheme.
5. Record the baseline date (UTC timestamp).
6. Record the baseline authority (individual or CCB that approved the baseline).

### Step 3: Baseline Manifest

Create a baseline manifest that serves as the table of contents:

```markdown
## Baseline Manifest

**Baseline ID:** BL-SRS-1.0.0
**Created:** 2026-03-07T14:30:00Z
**Authority:** [CCB Chair Name]

| # | Artifact | Hash (SHA-256) | Modified | Reqs |
|---|----------|----------------|----------|------|
| 1 | SRS_Draft.md | a1b2c3... | 2026-03-06 | 42 |
| 2 | traceability_matrix.md | d4e5f6... | 2026-03-07 | 42 |
| 3 | requirements_metrics_report.md | g7h8i9... | 2026-03-07 | 0 |
```

### Step 4: Archive

Store the baseline snapshot in a version-controlled repository. The baseline shall be immutable once approved: edits to baselined content require a new baseline version through the change control process.

---

## Diff Generation

When a new baseline is created, generate a diff report that compares it against the previous baseline.

### Diff Report Structure

```markdown
## Baseline Diff: BL-SRS-1.0.0 -> BL-SRS-1.1.0

**Previous Baseline:** BL-SRS-1.0.0 (2026-03-07)
**Current Baseline:** BL-SRS-1.1.0 (2026-03-21)

### Requirements Added (3)

| Req ID | Title | Source CR |
|--------|-------|----------|
| REQ-043 | [title] | CR-007 |
| REQ-044 | [title] | CR-007 |
| REQ-045 | [title] | CR-009 |

### Requirements Modified (2)

| Req ID | Field Changed | Previous Value | New Value | Source CR |
|--------|--------------|----------------|-----------|----------|
| REQ-012 | Priority | Medium | High | CR-008 |
| REQ-025 | Acceptance Criteria | [old] | [new] | CR-010 |

### Requirements Deleted (1)

| Req ID | Title | Rationale | Source CR |
|--------|-------|-----------|----------|
| REQ-009 | [title] | Superseded by REQ-043 | CR-007 |

### Artifacts Changed

| Artifact | Lines Added | Lines Removed | Lines Modified |
|----------|-------------|---------------|----------------|
| SRS_Draft.md | 45 | 12 | 8 |
```

---

## Rollback Procedures

If a baseline is found to contain errors that cannot be corrected through a PATCH increment, a rollback to the previous baseline may be necessary.

### Rollback Decision Criteria

A rollback shall be considered when:
- A MAJOR scope change is reversed by stakeholder decision.
- Critical defects in the baseline compromise multiple requirements.
- Regulatory compliance issues are discovered that invalidate the baseline.

### Rollback Process

1. **Authorization:** The CCB Chair shall authorize the rollback with documented justification.
2. **Notification:** All stakeholders shall be notified of the pending rollback.
3. **Restore:** The previous baseline version is restored as the active baseline.
4. **Re-version:** The rolled-back baseline receives the next MINOR version number with a rollback note (e.g., `BL-SRS-1.2.0 -- Rollback from BL-SRS-2.0.0`).
5. **Reconcile:** Any changes made between the rolled-back baseline and the current state shall be submitted as new CRs.
6. **Audit:** The rollback event is recorded in the version history with full justification.

### Rollback Constraints

- Rollback shall not skip more than one MAJOR version.
- Partial rollbacks (restoring some artifacts but not others) are prohibited. Rollback is all-or-nothing.
- The rolled-back baseline must pass the quality gate (Skill 10) before being re-activated.

---

## Baseline Lifecycle

```
[Draft Artifacts] --> [Quality Gate Pass] --> [Stakeholder Sign-off]
    --> [Baseline Created (BL-x.0.0)] --> [Change Requests]
    --> [CCB Approval] --> [Updates Applied] --> [New Baseline (BL-x.y.z)]
```

---

## References

- **IEEE Std 29148-2018** Section 6.7: Requirements baseline management.
- **IEEE Std 828-2012:** Configuration management in systems and software engineering.
- **IEEE Std 830-1998:** Baseline documentation quality characteristics.
- **Wiegers Practice 16:** Requirements baselining and configuration management.

---
**Last Updated:** 2026-03-07

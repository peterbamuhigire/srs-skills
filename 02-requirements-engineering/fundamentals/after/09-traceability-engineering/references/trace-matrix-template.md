# Traceability Matrix Template

**Purpose:** Provide a standardized template for building and maintaining a four-level requirements traceability matrix.

**Standards:** IEEE 1012-2016, IEEE 29148-2018, Laplante Ch.7.3

---

## Matrix Structure

The traceability matrix captures bidirectional links across four levels of abstraction:

```
Level 1: Business Goals (BG-xxx)
    |
Level 2: Requirements (REQ-xxx / FR-xxx / NFR-xxx / US-xxx)
    |
Level 3: Design Elements (DE-xxx)
    |
Level 4: Test Cases (TC-xxx)
```

---

## Column Definitions

| Column | ID Format | Description | Source |
|--------|-----------|-------------|--------|
| Req ID | REQ-xxx, FR-xxx, NFR-xxx, US-xxx | Unique requirement identifier | Requirements artifacts |
| Req Title | Free text | Brief descriptive title of the requirement | Requirements artifacts |
| Business Goal | BG-xxx | The business goal this requirement derives from | vision.md |
| Source Stakeholder | [Name, Role] | The stakeholder who originated or owns the requirement | stakeholder_register.md |
| Design Element | DE-xxx | The design component that satisfies this requirement | Design artifacts |
| Test Case ID | TC-xxx | The test case that verifies this requirement | Test artifacts |
| Trace Status | Complete / Partial / Orphan / Untested | Completeness of the trace chain | Computed |
| Priority | Critical / High / Medium / Low | Requirement priority | Requirements artifacts |
| Requirement State | Draft / Under Review / Approved / Implemented / Verified / Retired | Current lifecycle state | Baseline |

---

## Trace Status Definitions

| Status | Definition | Required Action |
|--------|-----------|----------------|
| Complete | Requirement has links at all four levels (BG, Req, DE, TC) | None -- fully traced |
| Partial | Requirement has some but not all trace links | Complete missing links or document justification |
| Orphan | Requirement has no upward link to a business goal | Link to BG, create new BG, or retire requirement |
| Untested | Requirement has no downward link to a test case | Create test case with verifiable acceptance criteria |

---

## Matrix Template

### Full Matrix View

| Req ID | Title | BG | Stakeholder | DE | TC | Status | Priority | State |
|--------|-------|----|-------------|----|----|--------|----------|-------|
| REQ-001 | User login authentication | BG-001 | J. Smith, PO | DE-003 | TC-001, TC-002 | Complete | Critical | Approved |
| REQ-002 | Password complexity rules | BG-001 | J. Smith, PO | DE-003 | TC-003 | Complete | High | Approved |
| REQ-003 | Dashboard performance | BG-002 | A. Lee, CTO | DE-007 | -- | Untested | High | Approved |
| REQ-004 | Report export | -- | M. Chen, Analyst | DE-010 | TC-008 | Orphan | Medium | Draft |

### Compact Matrix View (for large projects)

Use this view when the full matrix exceeds readability thresholds:

| Req ID | BG | DE | TC | Status |
|--------|----|----|----|--------|
| REQ-001 | BG-001 | DE-003 | TC-001 | Complete |
| REQ-002 | BG-001 | DE-003 | TC-003 | Complete |
| REQ-003 | BG-002 | DE-007 | -- | Untested |
| REQ-004 | -- | DE-010 | TC-008 | Orphan |

---

## Filtering Guidance

### By Trace Status

To identify gaps quickly, filter the matrix by Trace Status:

- **Filter: Orphan** -- Shows all requirements without business goal linkage. These represent potential scope creep or missing business justification.
- **Filter: Untested** -- Shows all requirements without test cases. These represent verification gaps.
- **Filter: Partial** -- Shows requirements with incomplete trace chains. These need link completion.

### By Business Goal

Filter by BG-xxx to see all requirements that support a specific business goal. This view answers: "What are we building to achieve this goal?"

If a business goal has zero requirements, it indicates an unmet goal that needs requirements elicitation.

### By Stakeholder

Filter by stakeholder to see all requirements owned by a specific individual. This view supports stakeholder review sessions and accountability tracking.

### By Priority

Filter by priority to focus review efforts on Critical and High requirements first. Lower-priority requirements with incomplete traces may be acceptable at YELLOW quality gates.

---

## Matrix Maintenance Rules

1. **Update on change:** When a requirement is added, modified, or deleted, update the matrix within the same change cycle.
2. **Verify bidirectionality:** Every forward link (Req -> TC) shall have a corresponding reverse link (TC -> Req).
3. **Re-validate on baseline:** When a new baseline is created, re-run trace analysis to confirm all links remain valid.
4. **Archive old versions:** When the matrix is updated, the previous version shall be archived with its baseline ID.
5. **Flag staleness:** If a linked artifact is modified without updating the matrix, flag the affected rows as `[STALE]`.

---

## Coverage Metrics Derivation

The following metrics are derived from the matrix:

| Metric | Formula |
|--------|---------|
| Upward Coverage | (Rows with BG populated) / (Total rows) x 100 |
| Downward Coverage | (Rows with TC populated) / (Total rows) x 100 |
| Full Coverage | (Rows with both BG and TC populated) / (Total rows) x 100 |
| Design Coverage | (Rows with DE populated) / (Total rows) x 100 |
| Orphan Count | Rows where BG is empty |
| Untested Count | Rows where TC is empty |

---

## References

- **IEEE Std 1012-2016:** Verification and validation traceability requirements.
- **IEEE Std 29148-2018:** Requirements traceability provisions.
- **Laplante Ch.7.3:** Traceability matrix construction and maintenance.
- **Wiegers Practice 18:** Requirements traceability link management.

---
**Last Updated:** 2026-03-07

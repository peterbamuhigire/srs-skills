# Trace Link Types Reference

**Purpose:** Define the taxonomy of trace link types used in requirements traceability, including bidirectional maintenance rules.

**Standards:** IEEE 1012-2016, IEEE 29148-2018

---

## Link Type Taxonomy

The following trace link types are defined for use in traceability matrices and requirements management. Each link type has a specific semantic meaning and directional convention.

---

### derives-from

| Attribute | Value |
|-----------|-------|
| Direction | Requirement -> Business Goal |
| Semantic | The requirement originates from and is justified by the business goal |
| Inverse | gives-rise-to (Business Goal -> Requirement) |
| Example | REQ-001 derives-from BG-003 ("Reduce customer churn by 20%") |

**Usage Rules:**
- Every requirement shall have at least one derives-from link to a business goal.
- A requirement with no derives-from link is classified as an Orphan.
- Multiple requirements may derive from the same business goal.
- A requirement may derive from multiple business goals (many-to-many).

**Validation:**
- If a business goal has zero derived requirements, it is an "Unmet Goal" and shall be flagged.
- If a requirement derives from a retired business goal, the requirement shall be reviewed for continued relevance.

---

### satisfies

| Attribute | Value |
|-----------|-------|
| Direction | Design Element -> Requirement |
| Semantic | The design element fulfills the intent of the requirement |
| Inverse | satisfied-by (Requirement -> Design Element) |
| Example | DE-007 satisfies REQ-015 ("The system shall display real-time inventory counts") |

**Usage Rules:**
- A design element may satisfy multiple requirements.
- A requirement may be satisfied by multiple design elements (decomposition).
- If a design element satisfies no requirement, it is classified as Gold-Plating.
- Partial satisfaction shall be documented with a note indicating which aspects remain unsatisfied.

**Validation:**
- Review all design elements with no satisfies link for potential gold-plating.
- Confirm that the design element's specification fully addresses the requirement's acceptance criteria.

---

### implements

| Attribute | Value |
|-----------|-------|
| Direction | Code Component -> Design Element |
| Semantic | The code component realizes the design element in executable form |
| Inverse | implemented-by (Design Element -> Code Component) |
| Example | `AuthController.php` implements DE-003 ("Authentication module design") |

**Usage Rules:**
- This link type is established during development, not during requirements engineering.
- It is included here for completeness of the four-level trace chain.
- Code components are identified by file path, class name, or module name.
- A design element with no implements link indicates incomplete development.

**Validation:**
- Validate during code reviews that every design element has at least one implementing component.
- Flag design elements without implementation as "Not Yet Implemented."

---

### verified-by

| Attribute | Value |
|-----------|-------|
| Direction | Requirement -> Test Case |
| Semantic | The test case validates that the requirement is correctly implemented |
| Inverse | verifies (Test Case -> Requirement) |
| Example | REQ-001 verified-by TC-001 ("Login with valid credentials returns dashboard") |

**Usage Rules:**
- Every requirement shall have at least one verified-by link to a test case.
- A requirement with no verified-by link is classified as Untested.
- Test cases shall reference the verification method: Test, Demonstration, Inspection, or Analysis.
- Multiple test cases may verify the same requirement (positive, negative, boundary cases).

**Verification Methods (IEEE 1012):**

| Method | Definition | When to Use |
|--------|-----------|-------------|
| Test | Execute the system and compare output to expected result | Functional requirements with measurable outputs |
| Demonstration | Operate the system to show capability | UI/UX requirements, workflow requirements |
| Inspection | Examine artifacts (code, documents) without execution | Coding standards, documentation completeness |
| Analysis | Use models, calculations, or simulations | Performance under extreme loads, mathematical correctness |

---

### conflicts-with

| Attribute | Value |
|-----------|-------|
| Direction | Requirement <-> Requirement (bidirectional) |
| Semantic | Two requirements specify mutually exclusive behaviors for the same system element |
| Inverse | Self-inverse (if A conflicts-with B, then B conflicts-with A) |
| Example | REQ-010 conflicts-with REQ-025 (REQ-010: "Session timeout at 15 minutes"; REQ-025: "Session persists indefinitely for premium users") |

**Usage Rules:**
- Conflicts shall be detected and flagged during traceability analysis.
- Each conflict shall include a description of the contradiction.
- Conflicts shall be resolved through the change control process before baselining.
- Unresolved conflicts are tagged with `[TRACE-GAP]`.

**Resolution Strategies:**

| Strategy | Description |
|----------|-------------|
| Prioritize | Accept one requirement and modify or retire the other |
| Merge | Combine both requirements into a single, non-contradictory requirement |
| Parameterize | Introduce a configuration variable that allows both behaviors in different contexts |
| Escalate | Submit to CCB for stakeholder decision when technical resolution is insufficient |

---

### refines

| Attribute | Value |
|-----------|-------|
| Direction | Child Requirement -> Parent Requirement |
| Semantic | The child requirement elaborates or decomposes the parent into more specific detail |
| Inverse | refined-by (Parent Requirement -> Child Requirement) |
| Example | REQ-001.1 refines REQ-001 ("REQ-001: User authentication"; REQ-001.1: "Authentication shall use bcrypt with cost factor 12") |

**Usage Rules:**
- Refinement creates a parent-child hierarchy.
- The child requirement shall not contradict the parent.
- The set of child requirements shall fully cover the parent's scope (completeness check).
- Refinement depth should not exceed 3 levels to maintain readability.

**Validation:**
- Verify that all child requirements together satisfy the parent requirement's intent.
- Flag parent requirements with no children that are too abstract to be directly testable.

---

### replaces

| Attribute | Value |
|-----------|-------|
| Direction | New Requirement -> Old Requirement |
| Semantic | The new requirement supersedes the old requirement, which shall be retired |
| Inverse | replaced-by (Old Requirement -> New Requirement) |
| Example | REQ-043 replaces REQ-009 ("REQ-009 retired; functionality superseded by REQ-043 per CR-007") |

**Usage Rules:**
- The old requirement shall transition to the Retired state.
- The replacement link shall reference the authorizing Change Request.
- All trace links from the old requirement shall be reviewed and reassigned to the new requirement where applicable.
- The old requirement shall remain in the traceability matrix with a Retired status for audit purposes.

**Validation:**
- Confirm that the new requirement covers all intent of the old requirement.
- Verify that no downstream artifacts (design, test) still reference the retired requirement.

---

## Bidirectional Link Maintenance Rules

All trace links shall be maintained bidirectionally. The following rules ensure link integrity:

### Rule 1: Simultaneous Creation

When a forward link is created (e.g., REQ-001 derives-from BG-003), the inverse link shall be created simultaneously (BG-003 gives-rise-to REQ-001).

### Rule 2: Simultaneous Deletion

When a link is deleted, the inverse link shall also be deleted. Orphaned inverse links create false trace coverage.

### Rule 3: Cascade on Retirement

When a requirement is retired, all links to and from that requirement shall be reviewed:
- derives-from links: The business goal's derived requirements list is updated.
- verified-by links: The test case is reviewed for continued relevance.
- satisfies links: The design element is checked for orphaned implementation.

### Rule 4: Change Propagation

When a requirement is modified, all linked artifacts shall be evaluated for impact:
- Does the test case still verify the modified requirement?
- Does the design element still satisfy the modified requirement?
- Is the business goal linkage still valid?

### Rule 5: Integrity Audit

The traceability matrix shall be audited for link integrity at every baseline creation. The audit shall check:
- No forward links exist without corresponding inverse links.
- No links reference retired or deleted artifacts without documentation.
- All link types use the defined taxonomy (no ad-hoc link types).

---

## Link Metadata

Each trace link shall carry the following metadata:

| Field | Description |
|-------|-------------|
| Source ID | The originating artifact identifier |
| Target ID | The linked artifact identifier |
| Link Type | One of the seven defined types |
| Created Date | When the link was established |
| Created By | Who established the link |
| Last Verified | When the link was last confirmed valid |
| Notes | Any contextual information about the link |

---

## References

- **IEEE Std 1012-2016:** Verification and validation trace link requirements.
- **IEEE Std 29148-2018:** Requirements traceability link management.
- **Laplante Ch.7.3:** Trace link types and bidirectional maintenance.
- **Wiegers Practice 18:** Link management and integrity verification.

---
**Last Updated:** 2026-03-07

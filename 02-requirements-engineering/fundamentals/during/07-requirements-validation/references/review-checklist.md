# Requirements Review Checklist

**Purpose:** Structured checklist for validating requirements against Wiegers' 7 quality attributes and IEEE 830's 8 quality criteria, with pass/fail indicators and common defect patterns.

**Standards:** IEEE 830-1998 Section 4.3, IEEE 1012-2016, Wiegers Practices 13-14

---

## 1. Per-Requirement Quality Attributes (Wiegers)

Apply these checks to **each individual requirement**.

### 1.1 Correct

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| C-01  | Does the requirement accurately reflect a documented stakeholder need? | Traces to a specific entry in `vision.md` or `features.md` | No traceable source; requirement appears invented |
| C-02  | Does the requirement describe what the system shall do (not how)? | Uses behavioral language ("shall display," "shall calculate") | Prescribes implementation ("use React," "store in MySQL") |
| C-03  | Is the requirement free from factual errors? | Technical claims are verifiable | Contains incorrect domain logic or impossible constraints |

**Common Defect Pattern:** Requirements copied from a previous project that do not apply to the current system.

### 1.2 Complete

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| CO-01 | Does the requirement contain all information needed for implementation? | Developer can implement without asking clarifying questions | Contains TBD, placeholders, or undefined references |
| CO-02 | Are error conditions and edge cases specified? | Exception handling is explicitly stated | Only the happy path is described |
| CO-03 | Are input ranges and boundary values defined? | Numeric limits, string lengths, and valid values stated | Open-ended ranges ("large number of users") |

**Common Defect Pattern:** Requirements that describe only the success scenario, omitting validation errors and exception flows.

### 1.3 Feasible

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| F-01  | Can this requirement be implemented with available technology? | TELOS Technical score >= 3 | Requires technology that does not exist or is unproven |
| F-02  | Can this requirement be implemented within budget? | TELOS Economic score >= 3 | Cost estimate exceeds allocated budget |
| F-03  | Can this requirement be delivered within the timeline? | TELOS Schedule score >= 3 | Implementation estimate exceeds remaining schedule |

**Common Defect Pattern:** Performance requirements that are physically impossible given the hardware constraints (e.g., "respond in 1ms" on a shared cloud instance).

### 1.4 Necessary

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| N-01  | Does removing this requirement degrade the product? | Traces to a business goal; removal impacts a KPI | No business goal linkage; "nice to have" without justification |
| N-02  | Is this requirement free from gold-plating? | Scope matches the business need exactly | Feature exceeds what was requested or needed |

**Common Defect Pattern:** Requirements added by developers for technical elegance that provide no user or business value.

### 1.5 Prioritized

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| P-01  | Does the requirement have an assigned priority? | MoSCoW, Kano, WSJF, or equivalent classification present | No priority assigned |
| P-02  | Is the priority justified? | Rationale references business impact or stakeholder decision | Priority assigned without explanation |

**Common Defect Pattern:** All requirements marked as "Must Have" with no differentiation.

### 1.6 Unambiguous

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| A-01  | Does the requirement have exactly one interpretation? | Two independent readers derive the same implementation | Readers disagree on meaning |
| A-02  | Is the requirement free from subjective adjectives? | No use of "fast," "intuitive," "user-friendly," "reliable" without metrics | Contains unmeasured qualitative terms |
| A-03  | Are all terms defined in the glossary? | Every domain term references `glossary.md` | Uses undefined or inconsistent terminology |

**Common Defect Pattern:** Using "appropriate" or "suitable" without defining the criteria (e.g., "display an appropriate error message").

### 1.7 Verifiable

| Check | Question | Pass Indicator | Fail Indicator |
|-------|----------|----------------|----------------|
| V-01  | Can a test case with a pass/fail criterion be written? | A deterministic test exists: given X, when Y, then Z | Outcome is subjective or non-deterministic |
| V-02  | Are acceptance criteria measurable? | Numeric thresholds, specific values, or observable behaviors stated | "The system shall perform well" |
| V-03  | Is the requirement testable within project constraints? | Test can be executed with available tools and environment | Requires testing infrastructure that does not exist |

**Common Defect Pattern:** Non-functional requirements without quantitative targets (e.g., "The system shall be scalable").

---

## 2. Set-Level Quality Criteria (IEEE 830)

Apply these checks to the **entire requirements set**.

| Criterion    | Check ID | Question | Pass Indicator | Fail Indicator |
|--------------|----------|----------|----------------|----------------|
| Correct      | S-C-01   | Does every requirement trace to a documented stakeholder need? | 100% backward traceability | Orphan requirements exist |
| Unambiguous  | S-A-01   | Are all terms used consistently across all requirements? | Glossary enforced; no synonym conflicts | Same concept uses different terms in different requirements |
| Complete     | S-CO-01  | Does every feature in `features.md` have at least one requirement? | 100% feature coverage | Features exist with no corresponding requirements |
| Complete     | S-CO-02  | Are all external interfaces defined? | Every boundary interaction specified | Interfaces referenced but not defined |
| Consistent   | S-CN-01  | Do any two requirements contradict each other? | No contradictions detected in conflict analysis | Unresolved contradictions remain |
| Ranked       | S-R-01   | Does every requirement have a priority? | 100% prioritization coverage | Requirements without priority assignments |
| Verifiable   | S-V-01   | Does every requirement have a testable criterion? | 100% of requirements have acceptance criteria | Requirements without test expectations |
| Modifiable   | S-M-01   | Does every requirement have a unique ID? | All IDs are unique; no duplicates | Duplicate IDs or missing IDs |
| Modifiable   | S-M-02   | Is the requirements set free from redundancy? | No redundant requirements detected | Redundant requirements inflate the set |
| Traceable    | S-T-01   | Does every requirement have forward and backward trace links? | Bidirectional traceability confirmed | Missing trace links in either direction |

---

## 3. Review Findings Template

For each defect found, record:

| Field              | Content                                              |
|--------------------|------------------------------------------------------|
| Finding ID         | Unique identifier (e.g., RV-001)                     |
| Requirement ID     | The affected requirement identifier                  |
| Check ID           | The checklist check that detected the defect         |
| Severity           | Critical / Major / Minor                             |
| Description        | What is wrong, stated objectively                    |
| Remediation        | Specific action to fix the defect                    |
| Tag                | `[V&V-FAIL:attribute]` per CLAUDE.md protocol        |

**Example:**
```
Finding ID: RV-003
Requirement ID: FR-015
Check ID: A-02
Severity: Major
Description: FR-015 uses the term "quickly" without a measurable threshold.
Remediation: Replace "quickly" with a specific response time target (e.g., "within 200ms at the 95th percentile").
Tag: [V&V-FAIL:AMBIGUITY]
```

---

## 4. Severity Classification Guide

| Severity | Definition                                                   | Resolution Deadline         |
|----------|--------------------------------------------------------------|-----------------------------|
| Critical | Contradicts a business goal, creates a safety or compliance risk, or makes the requirement set internally inconsistent | Before any downstream work |
| Major    | Missing information, ambiguous behavior, or untestable criterion that blocks implementation | Before baselining          |
| Minor    | Formatting, naming convention, or documentation issue that does not affect correctness | Before final release       |

---

## 5. Review Session Protocol

1. **Distribute** the checklist and requirements artifacts 48 hours before the review
2. **Prepare** individually: each reviewer applies the checklist and records findings
3. **Meet** to consolidate findings; do not solve problems during the meeting
4. **Log** all agreed-upon findings in the findings template
5. **Assign** each finding to an owner with a remediation deadline
6. **Verify** that remediation is complete before closing the finding

---

**Last Updated:** 2026-03-07

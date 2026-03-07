# Requirements Metrics Catalog

**Purpose:** Provide a complete catalog of quantitative metrics for evaluating requirements quality, including formulas, data sources, collection methods, interpretation, and industry benchmarks.

**Standards:** IEEE 29148-2018, IEEE 982.1-2005, Laplante Ch.7.4

---

## Metric 1: Volatility Index

| Attribute | Value |
|-----------|-------|
| **Name** | Volatility Index |
| **Formula** | $VI = \frac{R_{changed} + R_{added} + R_{deleted}}{R_{total}} \times 100$ |
| **Unit** | Percentage |
| **Data Source** | Version history log, baseline diffs |
| **Collection Method** | Compare current baseline against previous baseline; count added, modified, and deleted requirements |
| **Collection Frequency** | Per baseline, per sprint, or monthly |

**Interpretation:**
- 0-10%: Stable requirements. Normal for mature projects post-baseline.
- 10-25%: Moderate volatility. Acceptable during early iterations but warrants monitoring.
- 25%+: High volatility. Indicates unstable scope, insufficient elicitation, or external disruption.

**Industry Benchmarks:**
- Average enterprise project: 15-25% over full lifecycle (Wiegers).
- Well-managed project: below 10% after initial baseline.
- Agile projects: higher per-sprint volatility is expected (15-30%) but should decrease over time.

---

## Metric 2: Completeness Index

| Attribute | Value |
|-----------|-------|
| **Name** | Completeness Index |
| **Formula** | $CI = \frac{R_{complete}}{R_{total}} \times 100$ |
| **Unit** | Percentage |
| **Data Source** | Requirements artifacts, baseline inventory |
| **Collection Method** | For each requirement, verify presence of all mandatory fields: ID, description, priority, stakeholder, acceptance criteria, state |
| **Collection Frequency** | Per baseline or per quality gate execution |

**Mandatory Fields Checklist:**

| Field | Present? | Weight |
|-------|----------|--------|
| Unique identifier | Required | 1 |
| Description ("The system shall...") | Required | 1 |
| Priority (Critical/High/Medium/Low) | Required | 1 |
| Source stakeholder | Required | 1 |
| Acceptance criteria | Required | 1 |
| Requirement state | Required | 1 |

A requirement is "complete" only when all six fields are populated with meaningful content.

**Interpretation:**
- 95-100%: Production-ready. All requirements are fully specified.
- 80-94%: Needs attention. Identify and complete missing fields before development.
- Below 80%: Insufficient. Significant rework required before proceeding.

**Industry Benchmarks:**
- IEEE 830 expectation: 100% completeness at baseline.
- Practical target: 95% at initial baseline, 100% by design phase entry.

---

## Metric 3: Ambiguity Index

| Attribute | Value |
|-----------|-------|
| **Name** | Ambiguity Index |
| **Formula** | $AI = \sum \text{vague term occurrences across all requirements}$ |
| **Unit** | Count (integer) |
| **Data Source** | Requirements text across all artifacts |
| **Collection Method** | Automated text scan for prohibited terms; manual review for context-dependent ambiguity |
| **Collection Frequency** | Per baseline or per quality gate execution |

**Prohibited Terms:**

| Term | Why Prohibited | Replacement Guidance |
|------|---------------|---------------------|
| fast | No quantitative target | "within 200ms" |
| easy | Subjective | "in 3 clicks or fewer" |
| intuitive | Unmeasurable | "without training, first-time completion rate >= 90%" |
| user-friendly | Subjective | "SUS score >= 80" |
| robust | Undefined | "MTBF >= 720 hours" |
| flexible | Vague scope | "configurable via admin panel without code changes" |
| scalable | No load target | "support 10,000 concurrent users" |
| efficient | No metric | "CPU utilization <= 70% at peak load" |
| appropriate | Undefined boundary | Specify exact criterion |
| reasonable | Subjective | Specify exact threshold |
| sufficient | No threshold | Specify minimum quantity |
| adequate | Undefined level | Specify measurable standard |
| minimal | No lower bound | "at least N" or "no fewer than N" |
| maximize/minimize | No target | "achieve at least N" or "reduce to below N" |
| support | Ambiguous | "process," "generate," "transmit," or other specific verb |

**Interpretation:**
- 0: No ambiguity detected. Requirements meet IEEE 830 unambiguity criterion.
- 1-5: Minor ambiguity. Address before baselining.
- 6+: Significant ambiguity. Requirements fail IEEE 830 and must be rewritten.

---

## Metric 4: Testability Score

| Attribute | Value |
|-----------|-------|
| **Name** | Testability Score |
| **Formula** | $TS = \frac{R_{testable}}{R_{total}} \times 100$ |
| **Unit** | Percentage |
| **Data Source** | Requirements artifacts, acceptance criteria |
| **Collection Method** | Evaluate each requirement for verifiable acceptance criteria with pass/fail conditions |
| **Collection Frequency** | Per baseline or per quality gate execution |

**Testability Criteria:**

A requirement is testable when it has:
1. Acceptance criteria with explicit pass/fail conditions.
2. Quantitative thresholds where applicable (response time, accuracy, capacity).
3. No subjective terms from the Ambiguity Index prohibited list.
4. A feasible verification method (Test, Demonstration, Inspection, or Analysis).

**Interpretation:**
- 90-100%: Strong testability. Ready for test planning.
- 75-89%: Moderate testability. Some requirements need criteria refinement.
- Below 75%: Weak testability. Systematic acceptance criteria review required.

**Industry Benchmarks:**
- Best practice: 100% testability at baseline.
- Practical target: 90% at initial baseline.

---

## Metric 5: Traceability Coverage

| Attribute | Value |
|-----------|-------|
| **Name** | Traceability Coverage |
| **Formula** | $TC = \frac{R_{traced}}{R_{total}} \times 100$ |
| **Unit** | Percentage |
| **Data Source** | Traceability matrix |
| **Collection Method** | Count requirements with both upward (business goal) and downward (test case) links |
| **Collection Frequency** | Per baseline or per quality gate execution |

**Coverage Levels:**

| Level | Definition | Formula |
|-------|-----------|---------|
| Upward | Requirements linked to business goals | BG-linked / Total |
| Downward | Requirements linked to test cases | TC-linked / Total |
| Full | Requirements with both BG and TC links | Both-linked / Total |
| Design | Requirements linked to design elements | DE-linked / Total |

**Interpretation:**
- 85-100%: Strong traceability. Full audit trail established.
- 70-84%: Moderate. Gaps exist but are manageable with remediation.
- Below 70%: Weak. Significant traceability gaps compromise accountability.

---

## Metric 6: Conflict Count

| Attribute | Value |
|-----------|-------|
| **Name** | Conflict Count |
| **Formula** | $CC = \sum \text{unresolved requirement contradictions}$ |
| **Unit** | Count (integer) |
| **Data Source** | Traceability matrix, cross-requirement analysis |
| **Collection Method** | Compare requirements targeting the same system element for mutual exclusivity |
| **Collection Frequency** | Per baseline or per quality gate execution |

**Conflict Types:**

| Type | Description | Example |
|------|-------------|---------|
| Behavioral | Mutually exclusive behaviors specified | "Always encrypt" vs. "Allow plaintext for legacy" |
| Quantitative | Contradictory numeric thresholds | "Response < 100ms" vs. "Response < 500ms" for same operation |
| Priority | Same requirement given conflicting priorities by different stakeholders | Stakeholder A: Critical vs. Stakeholder B: Low |
| Temporal | Conflicting timing or sequence requirements | "Process before validation" vs. "Validate before processing" |

**Interpretation:**
- 0: No conflicts. Requirements are internally consistent.
- 1-2: Minor conflicts. Resolve through CCB before baselining.
- 3+: Significant inconsistency. Halt baselining until resolved.

---

## Metric 7: Data Quality Score

| Attribute | Value |
|-----------|-------|
| **Name** | Data Quality Score |
| **Formula** | $DQS = \frac{D_{complete} + D_{consistent}}{2 \times D_{total}} \times 100$ |
| **Unit** | Percentage |
| **Data Source** | Data requirements, data dictionaries, entity definitions |
| **Collection Method** | Evaluate each data requirement for field completeness and cross-artifact naming consistency |
| **Collection Frequency** | Per baseline |

**Data Requirement Fields:**

| Field | Required | Description |
|-------|----------|-------------|
| Data element name | Yes | Unique identifier for the data element |
| Data type | Yes | String, integer, decimal, boolean, date, etc. |
| Format | Yes | Pattern, length, encoding specification |
| Constraints | Yes | Valid ranges, allowed values, uniqueness |
| Validation rules | Yes | Business rules governing the data |
| Source | Recommended | Where the data originates |

**Interpretation:**
- 90-100%: High data quality. Data requirements are fully specified and consistent.
- 75-89%: Moderate. Some data fields lack type or constraint definitions.
- Below 75%: Low. Significant data specification gaps will cause implementation ambiguity.

---

## Metric 8: INVEST Compliance (Agile Only)

| Attribute | Value |
|-----------|-------|
| **Name** | INVEST Compliance |
| **Formula** | $IC = \frac{S_{passing}}{S_{total}} \times 100$ |
| **Unit** | Percentage |
| **Data Source** | User stories in output artifacts |
| **Collection Method** | Evaluate each user story against all six INVEST criteria |
| **Collection Frequency** | Per sprint or per quality gate execution |
| **Applicability** | Only when user stories exist in output artifacts |

**INVEST Criteria:**

| Criterion | Pass Condition |
|-----------|---------------|
| Independent | Story has no blocking dependencies or dependencies are documented |
| Negotiable | Story describes outcome, not implementation |
| Valuable | Story delivers measurable user or business value |
| Estimable | Story has a story point estimate |
| Small | Story is completable within one sprint (typically <= 8 points) |
| Testable | Story has verifiable acceptance criteria |

A story passes INVEST only when all six criteria are satisfied.

**Interpretation:**
- 90-100%: Stories are well-formed and sprint-ready.
- 75-89%: Some stories need refinement before sprint planning.
- Below 75%: Backlog requires systematic grooming.

---

## References

- **IEEE Std 982.1-2005:** Standard dictionary of measures for reliable software.
- **IEEE Std 29148-2018:** Requirements quality attributes.
- **IEEE Std 830-1998:** Eight quality characteristics for requirements.
- **Laplante Ch.7.4:** Requirements measurement and quality assessment.
- **Wiegers Practices 19-20:** Quality metrics and process improvement.

---
**Last Updated:** 2026-03-07

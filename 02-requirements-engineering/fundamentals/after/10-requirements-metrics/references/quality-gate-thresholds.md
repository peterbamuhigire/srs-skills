# Quality Gate Thresholds Configuration

**Purpose:** Define GREEN/YELLOW/RED quality gate thresholds for each requirements metric, including override justification procedures, escalation paths, and historical trend tracking.

**Standards:** IEEE 29148-2018, IEEE 982.1-2005

---

## Threshold Definitions

### Gate Verdicts

| Verdict | Meaning | Action |
|---------|---------|--------|
| GREEN | All metrics meet or exceed pass thresholds | Proceed to downstream activities without restriction |
| YELLOW | At least one metric is in the conditional range; none are RED | Proceed with documented risk acceptance and remediation plan |
| RED | At least one metric falls below conditional thresholds | Halt all downstream activities; return to upstream skills for correction |

The overall gate verdict is always the **lowest** individual metric verdict. One RED metric makes the entire gate RED.

---

## Threshold Table

| Metric | GREEN (Pass) | YELLOW (Conditional) | RED (Fail) |
|--------|-------------|---------------------|------------|
| Completeness Index | >= 95% | >= 80% and < 95% | < 80% |
| Ambiguity Index | 0 | 1-5 | > 5 |
| Testability Score | >= 90% | >= 75% and < 90% | < 75% |
| Traceability Coverage | >= 85% | >= 70% and < 85% | < 70% |
| Conflict Count | 0 | 1-2 | > 2 |
| Data Quality Score | >= 90% | >= 75% and < 90% | < 75% |
| INVEST Compliance | >= 90% | >= 75% and < 90% | < 75% |
| Volatility Index | <= 10% | > 10% and <= 25% | > 25% |

---

## Threshold Rationale

### Completeness Index: 95% GREEN

IEEE 830 mandates that every requirement be complete with all necessary information. The 95% threshold allows for minor metadata omissions in newly added requirements while ensuring the vast majority are fully specified. Requirements below 80% indicate systemic specification failures.

### Ambiguity Index: 0 GREEN

IEEE 830 requires that each requirement have exactly one interpretation. Any vague term is a potential source of misunderstanding and rework. The YELLOW band (1-5 occurrences) allows conditional passage when ambiguities are isolated and documented for resolution.

### Testability Score: 90% GREEN

Every requirement must be verifiable per IEEE 830. The 90% threshold accounts for high-level architectural requirements that may require decomposition before test cases can be written. Requirements below 75% indicate widespread absence of acceptance criteria.

### Traceability Coverage: 85% GREEN

Full traceability (business goal to test case) is the IEEE 1012 standard. The 85% threshold accommodates requirements in early lifecycle states (Draft, Under Review) that may not yet have test cases. Coverage below 70% indicates fundamental gaps in the trace chain.

### Conflict Count: 0 GREEN

No unresolved contradictions shall exist in a baselined requirement set. The YELLOW band (1-2 conflicts) allows conditional passage when conflicts are documented and under active CCB resolution. More than 2 unresolved conflicts indicate systemic analysis failure.

### Data Quality Score: 90% GREEN

Data requirements missing type, format, or constraint definitions cause implementation ambiguity. The 90% threshold allows for edge cases where data characteristics are genuinely unknown and marked for spike investigation.

### INVEST Compliance: 90% GREEN

User stories that fail INVEST criteria are not sprint-ready. The 90% threshold allows for a small number of stories undergoing active refinement. Below 75% indicates the backlog is not ready for sprint planning.

### Volatility Index: 10% GREEN

Requirements stability is essential for project predictability. Post-baseline volatility above 10% suggests scope instability. Above 25% indicates the requirements are not mature enough to support development planning.

---

## Override Justification Process

In exceptional circumstances, a YELLOW gate may be overridden to proceed as if GREEN, or a RED gate may be overridden to proceed as YELLOW. Overrides require formal justification.

### Override Authority

| Gate Status | Override Authority | Required Approvals |
|-------------|-------------------|-------------------|
| YELLOW -> GREEN | Product Owner + Technical Lead | Both must sign |
| RED -> YELLOW | CCB Chair + Product Owner + Technical Lead | All three must sign |
| RED -> GREEN | Not permitted | N/A |

A RED gate shall never be overridden directly to GREEN. The maximum override is RED to YELLOW, which still requires a remediation plan.

### Override Documentation

Every override shall be recorded with:

| Field | Description |
|-------|-------------|
| Override ID | OVR-[NNN] |
| Gate Execution Date | Date the quality gate was run |
| Metric(s) Overridden | Which metric(s) did not meet threshold |
| Actual Score(s) | The measured values |
| Justification | Detailed business or technical rationale |
| Risk Acceptance | Explicit statement of risks being accepted |
| Remediation Plan | Specific actions to bring metrics into threshold |
| Remediation Deadline | Date by which remediation must be complete |
| Approvers | Names and roles of override approvers |

### Override Constraints

- No more than 2 overrides per baseline. A third override triggers mandatory process review.
- Override remediation deadlines shall not exceed 2 sprints or 4 weeks.
- If remediation is not completed by the deadline, the gate reverts to its original status and downstream activities shall halt.

---

## Escalation Procedures

### Level 1: Metric Deficiency Detected

- **Trigger:** Any metric scores YELLOW.
- **Action:** Requirements Manager notifies the responsible skill owner.
- **SLA:** Remediation plan within 3 business days.

### Level 2: Gate Fails (RED)

- **Trigger:** Any metric scores RED.
- **Action:** Requirements Manager notifies CCB Chair and Product Owner. Downstream activities are blocked.
- **SLA:** Emergency CCB meeting within 2 business days.

### Level 3: Repeated Failure

- **Trigger:** Same metric fails RED for 2 consecutive gate executions.
- **Action:** CCB Chair escalates to project sponsor. Root cause analysis is mandatory.
- **SLA:** Root cause analysis complete within 5 business days.

### Level 4: Override Deadline Missed

- **Trigger:** Overridden metric is not remediated by the deadline.
- **Action:** Gate reverts to original status. All downstream activities halt. CCB Chair notifies project sponsor.
- **SLA:** Immediate halt; no grace period.

---

## Historical Trend Tracking

### Trend Log Template

| Date | Baseline | CI | AI | TS | TC | CC | DQS | IC | VI | Verdict |
|------|----------|----|----|----|----|----|-----|----|----|---------|
| YYYY-MM-DD | BL-x.y.z | N% | N | N% | N% | N | N% | N% | N% | GREEN |

### Trend Analysis Rules

1. **Improving trend:** Three consecutive improvements in a metric indicate process maturity. Document the practice that drove improvement.
2. **Degrading trend:** Two consecutive declines in a metric trigger a process review. Identify and address the root cause.
3. **Plateau:** If a metric remains at YELLOW for three consecutive measurements, it shall be treated as RED for escalation purposes.
4. **Benchmark comparison:** Compare current metrics against the industry benchmarks in the metrics catalog to assess relative maturity.

### Reporting Cadence

- **Per baseline:** Full metrics report with trend comparison.
- **Monthly:** Summary dashboard showing trends for all metrics.
- **Quarterly:** Management report with trend analysis, override history, and process improvement recommendations.

---

## Gate Execution Checklist

Before declaring a gate verdict:

- [ ] All eight metrics have been calculated.
- [ ] Each metric is compared against its GREEN/YELLOW/RED threshold.
- [ ] The overall verdict is set to the lowest individual metric status.
- [ ] All RED and YELLOW metrics have specific deficiency lists.
- [ ] Remediation actions are defined for all non-GREEN metrics.
- [ ] The result is recorded in the historical trend log.
- [ ] Stakeholders are notified of the verdict.

---

## References

- **IEEE Std 29148-2018:** Requirements quality evaluation.
- **IEEE Std 982.1-2005:** Standard dictionary of measures for reliable software.
- **Laplante Ch.7.4:** Quality gates and measurement-driven decision making.
- **Wiegers Practice 19:** Quality metrics thresholds and gates.

---
**Last Updated:** 2026-03-07

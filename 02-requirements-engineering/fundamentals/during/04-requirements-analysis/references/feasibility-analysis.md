# Feasibility Analysis Reference Guide (TELOS Framework)

**Purpose:** Assess requirement feasibility across five dimensions using a structured scoring rubric with go/no-go thresholds.

**Standards:** IEEE 29148-2018 Section 6.5, Laplante Ch.5

---

## 1. TELOS Framework Overview

TELOS is a five-dimensional feasibility assessment framework. Each dimension evaluates a different risk vector that could prevent successful requirement implementation.

| Dimension   | Full Name   | Core Question                                            |
|-------------|-------------|----------------------------------------------------------|
| T           | Technical   | Can this be built with available or acquirable technology?|
| E           | Economic    | Can this be built within budget constraints?              |
| L           | Legal       | Does this comply with all applicable laws and regulations?|
| O           | Operational | Can the organization operate and maintain this?           |
| S           | Schedule    | Can this be delivered within the project timeline?        |

---

## 2. Scoring Rubric

Each dimension is scored on a 1-5 scale. Scores SHALL include a one-sentence justification.

### 2.1 Technical Feasibility

| Score | Label          | Criteria                                                          |
|-------|----------------|-------------------------------------------------------------------|
| 5     | Proven         | Technology is mature, team has direct experience, no R&D needed   |
| 4     | Achievable     | Technology exists, team has related experience, minor learning curve|
| 3     | Challenging    | Technology exists but is new to the team; training or hiring needed|
| 2     | Risky          | Technology is emerging; prototype or proof-of-concept required     |
| 1     | Infeasible     | No known technology can satisfy the requirement as stated          |

### 2.2 Economic Feasibility

| Score | Label          | Criteria                                                          |
|-------|----------------|-------------------------------------------------------------------|
| 5     | Within Budget  | Estimated cost is less than 50% of allocated budget for this area |
| 4     | Affordable     | Estimated cost is 50-80% of allocated budget                      |
| 3     | Tight          | Estimated cost is 80-100% of allocated budget                     |
| 2     | Over Budget    | Estimated cost exceeds budget by up to 25%; reallocation needed   |
| 1     | Prohibitive    | Estimated cost exceeds budget by more than 25%; not viable         |

### 2.3 Legal Feasibility

| Score | Label          | Criteria                                                          |
|-------|----------------|-------------------------------------------------------------------|
| 5     | Compliant      | Fully compliant with all known regulations; no legal review needed|
| 4     | Low Risk       | Compliant with minor interpretation questions; brief legal review |
| 3     | Moderate Risk  | Compliance requires specific design accommodations                |
| 2     | High Risk      | Potential regulatory conflict; formal legal opinion required      |
| 1     | Non-Compliant  | Directly conflicts with a known regulation or statutory requirement|

### 2.4 Operational Feasibility

| Score | Label          | Criteria                                                          |
|-------|----------------|-------------------------------------------------------------------|
| 5     | Seamless       | Fits existing workflows; no process changes or retraining needed  |
| 4     | Minor Effort   | Requires minor process updates; less than 4 hours retraining      |
| 3     | Moderate Effort| Requires workflow redesign; staff retraining under 2 weeks        |
| 2     | Major Effort   | Requires significant organizational change; over 2 weeks transition|
| 1     | Disruptive     | Fundamentally incompatible with current operations                |

### 2.5 Schedule Feasibility

| Score | Label          | Criteria                                                          |
|-------|----------------|-------------------------------------------------------------------|
| 5     | Ahead          | Can be completed in less than 50% of available timeline           |
| 4     | On Track       | Can be completed within the planned timeline with buffer          |
| 3     | Tight          | Can be completed within timeline but with no buffer for delays    |
| 2     | At Risk        | Likely to exceed timeline by up to 25%; scope reduction needed    |
| 1     | Infeasible     | Cannot be completed within any reasonable extension of timeline   |

---

## 3. Composite Score Calculation

$FeasibilityScore = \frac{T + E + L + O + S}{5}$

### Weighted Variant (Optional)

If stakeholders assign different importance to each dimension:

$FeasibilityScore_{weighted} = \frac{w_T \cdot T + w_E \cdot E + w_L \cdot L + w_O \cdot O + w_S \cdot S}{w_T + w_E + w_L + w_O + w_S}$

Where $w_x$ is the stakeholder-assigned weight for dimension $x$ (default: all weights = 1).

---

## 4. Go/No-Go Thresholds

| Composite Score | Decision     | Action                                                        |
|-----------------|--------------|---------------------------------------------------------------|
| >= 4.0          | Go           | Proceed to specification. No additional risk mitigation needed. |
| 2.5 - 3.9      | Conditional  | Proceed with documented risks. Create mitigation plan for any dimension scoring below 3. |
| < 2.5           | No-Go        | Defer or remove. Flag with `[FEASIBILITY-FAIL]`. Do not include in current baseline. |

### Override Rules

- **Any single dimension scoring 1:** Automatic No-Go regardless of composite score, unless the dimension is formally waived by the executive sponsor with documented risk acceptance.
- **Legal dimension scoring 2 or below:** Mandatory legal review before proceeding, regardless of composite score.

---

## 5. Feasibility Assessment Template

| Req ID  | T | E | L | O | S | Composite | Decision    | Justification Summary                     |
|---------|---|---|---|---|---|-----------|-------------|--------------------------------------------|
| FR-001  | 5 | 4 | 5 | 4 | 4 | 4.4       | Go          | Proven tech, within budget, full compliance |
| FR-002  | 3 | 3 | 5 | 2 | 3 | 3.2       | Conditional | Operational change needed; training plan required |
| NFR-005 | 2 | 1 | 5 | 4 | 2 | 2.8       | No-Go       | Economic: exceeds budget by 40%; auto-fail on E=1 |

---

## 6. Risk Documentation for Conditional Requirements

For every requirement with a Conditional decision, document:

| Field                | Content                                                |
|----------------------|--------------------------------------------------------|
| Requirement ID       | The identifier of the conditional requirement          |
| Risk Dimension(s)    | Which TELOS dimension(s) scored below 3                |
| Risk Description     | What could go wrong and the impact                     |
| Mitigation Strategy  | Specific actions to reduce the risk                    |
| Mitigation Owner     | Person responsible for executing the mitigation        |
| Review Date          | When the mitigation status will be reassessed          |

---

## 7. Feasibility Assessment Checklist

- [ ] Every mandatory requirement has a TELOS score with per-dimension justification
- [ ] Composite scores are calculated correctly
- [ ] Go/No-Go thresholds are applied consistently
- [ ] Override rules are checked (no single dimension = 1 unless waived)
- [ ] Conditional requirements have documented risk mitigation plans
- [ ] No-Go requirements are flagged with `[FEASIBILITY-FAIL]`
- [ ] Stakeholder weights are documented if the weighted variant is used

---

**Last Updated:** 2026-03-07

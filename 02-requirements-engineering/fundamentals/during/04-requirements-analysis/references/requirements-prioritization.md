# Requirements Prioritization Reference Guide

**Purpose:** Compare four prioritization methods and provide a decision tree for selecting the most appropriate method based on project context.

**Standards:** IEEE 29148-2018, Wiegers Practice 9, Laplante Ch.5

---

## 1. Method Comparison Matrix

| Criterion              | MoSCoW            | Kano Model         | WSJF               | 100-Dollar Method   |
|------------------------|--------------------|---------------------|---------------------|---------------------|
| **Complexity**         | Low                | Medium              | Medium-High         | Low                 |
| **Stakeholder Count**  | Any                | 5+ for survey       | Requires estimators | 3-10 ideal          |
| **Quantitative**       | No (categorical)   | Semi (survey scores)| Yes (numeric ratio) | Yes (allocation)    |
| **Best For**           | MVP scoping        | Customer satisfaction| Lean/Agile backlogs | Small requirement sets |
| **Weakness**           | "Must" inflation   | Survey design effort| Estimation accuracy | Doesn't scale well  |
| **Output**             | 4 buckets          | 3 categories        | Ranked numeric list | Ranked by investment|

---

## 2. MoSCoW Method

### 2.1 Categories

| Category  | Keyword | Definition                                                         | Capacity Rule         |
|-----------|---------|--------------------------------------------------------------------|-----------------------|
| Must Have | M       | Non-negotiable for the release; the product fails without it       | Maximum 60% of effort |
| Should Have| S      | Important but not critical; workaround exists if omitted           | Typically 20% of effort|
| Could Have| C       | Desirable if resources permit; first items cut under pressure      | Typically 20% of effort|
| Won't Have| W       | Explicitly out of scope for this release; may be reconsidered later| 0% of effort          |

### 2.2 Application Process

1. Present each requirement to stakeholders with its classification context
2. Stakeholders assign one of M/S/C/W to each requirement
3. Validate Must Have set: if Must Have requirements exceed 60% of capacity, challenge each one with "What happens if we defer this?"
4. Resolve disagreements through voting or escalation to the product owner
5. Document the final MoSCoW assignment with rationale

### 2.3 Common MoSCoW Pitfalls

- **Must inflation:** Stakeholders default to "Must." Enforce the 60% cap and require justification.
- **Won't confusion:** "Won't" means "not this release," not "never." Document the deferral context.
- **Missing rationale:** Every assignment SHALL include a one-sentence justification.

---

## 3. Kano Model

### 3.1 Categories

| Category     | Also Called  | Definition                                                     | Satisfaction Curve |
|--------------|--------------|----------------------------------------------------------------|--------------------|
| Basic        | Must-Be      | Expected by default; absence causes dissatisfaction, presence does not increase satisfaction | Asymptotic negative |
| Performance  | One-Dimensional | Satisfaction increases linearly with the degree of fulfillment | Linear positive    |
| Excitement   | Attractive   | Unexpected features that delight; absence does not cause dissatisfaction | Exponential positive|

### 3.2 Classification Process

1. For each requirement, ask two questions:
   - **Functional:** "How would you feel if this feature were present?"
   - **Dysfunctional:** "How would you feel if this feature were absent?"
2. Response options: Like, Expect, Neutral, Tolerate, Dislike
3. Map response pairs to the Kano evaluation table:

| Functional \ Dysfunctional | Like    | Expect  | Neutral | Tolerate | Dislike  |
|-----------------------------|---------|---------|---------|----------|----------|
| Like                        | Q       | A       | A       | A        | O        |
| Expect                      | R       | I       | I       | I        | M        |
| Neutral                     | R       | I       | I       | I        | M        |
| Tolerate                    | R       | I       | I       | I        | M        |
| Dislike                     | R       | R       | R       | R        | Q        |

Key: M=Must-Be, O=One-Dimensional, A=Attractive, I=Indifferent, R=Reverse, Q=Questionable

### 3.3 Prioritization Rule

1. Implement all Basic (Must-Be) requirements first
2. Implement Performance requirements in order of satisfaction coefficient
3. Include Excitement requirements as capacity allows
4. Exclude Indifferent and Reverse requirements

---

## 4. WSJF (Weighted Shortest Job First)

### 4.1 Formula

$WSJF = \frac{Cost\ of\ Delay}{Job\ Size}$

Where Cost of Delay is decomposed into three components:

$Cost\ of\ Delay = User\ Value + Time\ Criticality + Risk\ Reduction$

### 4.2 Scoring Scale

Each component is scored using a modified Fibonacci scale: 1, 2, 3, 5, 8, 13, 20.

| Component        | Score 1              | Score 13             | Score 20              |
|------------------|----------------------|----------------------|-----------------------|
| User Value       | Negligible benefit   | High user benefit    | Transformative benefit|
| Time Criticality | No urgency           | Competitive window   | Regulatory deadline   |
| Risk Reduction   | No risk addressed    | Significant risk     | Existential risk      |
| Job Size         | Trivial effort       | Large effort         | Massive effort        |

### 4.3 Application Process

1. Score each requirement on all four dimensions using team consensus
2. Calculate WSJF for each requirement
3. Sort requirements in descending WSJF order
4. Higher WSJF = higher priority (maximum value per unit of effort)

### 4.4 Example

| Req ID  | User Value | Time Crit. | Risk Red. | CoD | Job Size | WSJF |
|---------|------------|------------|-----------|-----|----------|------|
| FR-001  | 8          | 13         | 5         | 26  | 3        | 8.7  |
| FR-002  | 13         | 5          | 3         | 21  | 8        | 2.6  |
| FR-003  | 5          | 8          | 8         | 21  | 2        | 10.5 |

Priority order: FR-003, FR-001, FR-002.

---

## 5. 100-Dollar Method

### 5.1 Process

1. Present stakeholders with the full list of requirements
2. Each stakeholder receives 100 hypothetical dollars to distribute
3. Stakeholders allocate dollars to requirements reflecting relative importance
4. No requirement may receive more than $50 (prevents single-item dominance)
5. Aggregate all stakeholder allocations
6. Rank requirements by total dollars received

### 5.2 Aggregation

| Req ID  | Stakeholder A | Stakeholder B | Stakeholder C | Total | Rank |
|---------|---------------|---------------|---------------|-------|------|
| FR-001  | $30           | $25           | $20           | $75   | 1    |
| FR-002  | $10           | $15           | $40           | $65   | 2    |
| FR-003  | $20           | $10           | $10           | $40   | 3    |
| FR-004  | $40           | $50           | $30           | $120  | Err  |

Note: FR-004 allocation from Stakeholder B exceeds the $50 cap. Request reallocation.

### 5.3 Limitations

- Does not scale well beyond 20-30 requirements (cognitive overload)
- Tends to favor visible features over infrastructure requirements
- Stakeholder bias toward their own domain is not controlled

---

## 6. Decision Tree: Choosing a Method

```
START
  |
  v
How many requirements?
  |
  +-- < 20 --> How many stakeholders?
  |               |
  |               +-- < 5 --> 100-Dollar Method
  |               +-- >= 5 --> MoSCoW
  |
  +-- 20-100 --> Is the team using Agile/Lean?
  |               |
  |               +-- Yes --> WSJF
  |               +-- No --> Is customer satisfaction the primary driver?
  |                           |
  |                           +-- Yes --> Kano Model
  |                           +-- No --> MoSCoW
  |
  +-- > 100 --> Split into subsystems, then apply MoSCoW or WSJF per subsystem
```

### Selection Factors Summary

| Factor                        | Recommended Method |
|-------------------------------|-------------------|
| MVP scoping with mixed stakeholders | MoSCoW       |
| Customer-facing product discovery   | Kano Model    |
| Agile backlog with capacity limits  | WSJF          |
| Small set, democratic decision      | 100-Dollar    |

---

## 7. Prioritization Checklist

- [ ] Prioritization method selected with documented rationale
- [ ] Every requirement has a priority assignment
- [ ] Stakeholder participants are identified and their roles documented
- [ ] MoSCoW: Must Have requirements do not exceed 60% of capacity
- [ ] Kano: Survey responses collected from at least 5 stakeholders
- [ ] WSJF: All four dimensions scored by team consensus
- [ ] 100-Dollar: No single requirement received more than $50 from any stakeholder
- [ ] Priority distribution analyzed for balance (no method-specific pitfalls)

---

**Last Updated:** 2026-03-07

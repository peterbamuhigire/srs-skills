# Decision Tables Reference Guide

**Purpose:** Construct, validate, and simplify decision tables for formalizing complex business logic with multiple conditions and outcomes.

**Standards:** IEEE 830-1998 Section 5.3.1, Wiegers Practice 10

---

## 1. Decision Table Anatomy

A decision table has four quadrants:

```
+---------------------+--------+--------+--------+--------+
| Conditions          | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
+---------------------+--------+--------+--------+--------+
| Condition 1         | T      | T      | F      | F      |
| Condition 2         | T      | F      | T      | F      |
+---------------------+--------+--------+--------+--------+
| Actions             |        |        |        |        |
+---------------------+--------+--------+--------+--------+
| Action A            | X      |        | X      |        |
| Action B            |        | X      |        | X      |
| Action C            | X      | X      |        |        |
+---------------------+--------+--------+--------+--------+
```

| Quadrant         | Content                                      |
|------------------|----------------------------------------------|
| Condition Stubs  | The conditions (left column)                 |
| Condition Entries| T/F values for each rule (top-right)         |
| Action Stubs     | The possible actions (left column, lower)    |
| Action Entries   | X marks indicating which actions fire (lower-right) |

---

## 2. Construction Process

### Step 1: Identify the Business Rule

Extract the business rule from `business_rules.md` that involves multiple conditions affecting different outcomes.

**Example Business Rule (BR-015):**
"The system shall calculate shipping cost based on order total, customer membership tier, and destination zone."

### Step 2: Extract Conditions

List every condition variable:
- Condition 1: Order total >= $100
- Condition 2: Customer is Premium member
- Condition 3: Destination is domestic

### Step 3: Extract Actions

List every possible outcome:
- Action A: Free shipping
- Action B: Flat rate $5.99
- Action C: Standard rate (weight-based)
- Action D: Apply 50% shipping discount

### Step 4: Calculate Required Rules

For $n$ binary conditions, the complete table requires $2^n$ rules.

| Conditions | Rules Required |
|------------|---------------|
| 2          | 4             |
| 3          | 8             |
| 4          | 16            |
| 5          | 32            |

For enumerated conditions with $k$ values, multiply: $k_1 \times k_2 \times ... \times k_n$

### Step 5: Build the Complete Table

Fill in every combination of condition values and assign the correct action(s) to each rule.

**Example (3 conditions = 8 rules):**

| Conditions / Rules      | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|-------------------------|----|----|----|----|----|----|----|----|
| Order >= $100           | T  | T  | T  | T  | F  | F  | F  | F  |
| Premium member          | T  | T  | F  | F  | T  | T  | F  | F  |
| Domestic destination    | T  | F  | T  | F  | T  | F  | T  | F  |
| **Actions**             |    |    |    |    |    |    |    |    |
| Free shipping           | X  | X  |    |    |    |    |    |    |
| Flat rate $5.99         |    |    | X  |    | X  |    |    |    |
| Standard rate           |    |    |    |    |    |    | X  |    |
| 50% shipping discount   |    |    |    | X  |    | X  |    |    |
| International surcharge |    |    |    | X  |    | X  |    | X  |

---

## 3. Completeness Checking

### 3.1 Rule Count Validation

Verify the table contains exactly $2^n$ rules for $n$ binary conditions. A table with fewer rules has implicit "don't care" conditions that must be made explicit.

### 3.2 Action Coverage Validation

For every rule column, at least one action SHALL be marked. A rule with no action indicates an undefined system behavior. Flag with `[INCOMPLETE-RULE]`.

### 3.3 Contradiction Check

No rule SHALL trigger contradictory actions. If Action A says "approve" and Action B says "reject," they cannot both be marked for the same rule.

### 3.4 Missing Combination Detection

Compare the table's condition combinations against the full truth table. Any missing combination represents an unspecified scenario.

---

## 4. Simplification Techniques

### 4.1 Dash Notation (Don't Care)

When a condition does not affect the outcome, replace T/F with a dash (-):

**Before simplification:**

| Conditions / Rules | R1 | R2 |
|---------------------|----|----|
| Order >= $100       | T  | T  |
| Premium member      | T  | F  |
| **Actions**         |    |    |
| Free shipping       | X  | X  |

**After simplification:**

| Conditions / Rules | R1 |
|---------------------|----|
| Order >= $100       | T  |
| Premium member      | -  |
| **Actions**         |    |
| Free shipping       | X  |

Premium membership does not affect the outcome when order >= $100, so it becomes a dash.

### 4.2 Merging Identical Rules

Rules with identical action entries that differ in exactly one condition can be merged using dash notation.

### 4.3 Simplification Validation

After simplification, verify that the simplified table still covers all $2^n$ original combinations. Expand the dashes mentally to confirm no combination is lost.

---

## 5. Extended-Entry Decision Tables

When conditions are not binary, use extended-entry notation:

| Conditions / Rules      | R1       | R2       | R3       | R4       |
|-------------------------|----------|----------|----------|----------|
| Membership tier         | Gold     | Silver   | Bronze   | None     |
| Order total range       | > $200   | $100-200 | $50-100  | < $50    |
| **Actions**             |          |          |          |          |
| Discount percentage     | 20%      | 10%      | 5%       | 0%       |

Extended-entry tables are more readable for enumerated conditions but require careful completeness checking since the total rule count is the product of all value counts.

---

## 6. Decision Table to Requirements Mapping

Each decision table SHALL produce one or more formal requirements:

**Template:**
```
[DT-001, Rule R3] The system shall apply a flat rate shipping charge of $5.99
when the order total is $100 or more AND the customer is not a Premium member
AND the destination is domestic.
```

Every rule in the decision table SHALL map to at least one "shall" statement. The requirement identifier SHALL reference the decision table ID and rule number.

---

## 7. Decision Table Checklist

- [ ] Business rule identified and documented
- [ ] All conditions extracted and classified (binary or enumerated)
- [ ] All actions extracted
- [ ] Complete table built with $2^n$ rules (or product for enumerated)
- [ ] Every rule has at least one action marked
- [ ] No contradictory actions within a single rule
- [ ] Simplification applied where conditions are irrelevant
- [ ] Simplified table verified against original for completeness
- [ ] Each rule mapped to a formal "shall" requirement

---

**Last Updated:** 2026-03-07

# Rule Catalog Pattern

Use this pattern when writing the business rules catalog.

| Column | Meaning |
|---|---|
| Rule ID | Stable identifier |
| Rule Type | Policy, decision, calculation, validation, compliance, temporal |
| Statement | Plain-language rule |
| Source | Policy owner, law, stakeholder, contract, or document |
| Trigger | Condition that activates the rule |
| Outcome | What must happen |
| Exception | Override or exception path |
| Example | Concrete scenario |

## Review Questions

- Is this really a business rule or an implementation preference?
- Who can change this rule?
- How would a tester prove the rule holds?
- What happens when the rule collides with another rule?

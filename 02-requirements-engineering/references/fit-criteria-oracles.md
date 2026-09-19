# Fit criteria and acceptance oracles

Use this reference to make a requirement testable before baseline. A fit
criterion may use an automated check, a human review, or both, but the method
and expected result must be explicit.

## Source and currentness

This reference is an independent synthesis of B10-A03. It does not establish a
quality threshold for a project or a jurisdiction. `NO_TIME_SENSITIVE_CLAIMS`.
The project owner must supply the baseline, target, applicable source, and
named reviewer.

## Contract

| Field | Required value |
| --- | --- |
| `criterion_id` | Stable identifier linked to `REQ-*` |
| `condition` | State or event under which the criterion applies |
| `unit` | Count, percentage, duration, rate, data value, or named review |
| `threshold_or_oracle` | Numeric threshold or exact human decision rule |
| `source` | Project source, version, and scope for the threshold |
| `verification_method` | Replay, test, inspection, observation, or approval |
| `normal_case` | Expected passing result |
| `boundary_case` | Result at or near the threshold |
| `exception_case` | Expected failure, quarantine, or escalation |
| `result_owner` | Person or role who records the result |
| `trace_links` | Requirement, event, test, and evidence identifiers |

## Synthetic fixture

```yaml
criterion_id: FIT-001
condition: a duplicate merge is authorised
unit: evidence fields present
threshold_or_oracle: source id, target id, owner, timestamp, reason, and reviewer are all present
source: project evidence schema; version and scope supplied by owner
verification_method: fixture replay plus evidence inspection
normal_case: merge is accepted and all fields are recorded
boundary_case: one required field is empty
exception_case: merge is blocked and routed to review
result_owner: requirements quality reviewer
trace_links: [REQ-001, EVT-001, TEST-001]
```

## Failure rules

| Finding | Required result |
| --- | --- |
| Adjective-only criterion such as `fast`, `secure`, or `easy` | `NOT_ASSESSED` until unit and oracle exist |
| Threshold without a project source or scope | `NOT_ASSESSED`; quarantine the claim |
| Boundary case omitted | `BLOCKED` for baseline review |
| Exception path has no owner or result | `BLOCKED` for baseline review |
| Human judgement is required but no reviewer is named | `NOT_ASSESSED` |

Keep automated evidence and human judgement in separate result fields. A human
review can satisfy an oracle only when the decision rule, reviewer role, date,
and evidence location are recorded.


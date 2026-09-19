# Event-centred requirements slice

Use this reference to turn one observable event into a bounded requirement
slice and an upward/downward trace. Keep the event model independent from an
implementation choice.

## Source and currentness

This reference is an independent synthesis of B10-A02. It carries no volatile
platform, legal, clinical, or standards claim. `NO_TIME_SENSITIVE_CLAIMS`.
Project event evidence, owners, and review dates are still required.

## Slice contract

| Field | Required value |
| --- | --- |
| `event_id` | Stable identifier and source event version |
| `trigger` | Observable event, precondition, and timestamp source |
| `actor` | Initiating actor and accountable owner |
| `intent` | User or business outcome linked to `PG-*` or `GOAL-*` |
| `system_response` | Required response and data transition, without prescribing code |
| `end_state` | Observable state and evidence that proves it |
| `exceptions` | At least one failure or denied path with owner and result |
| `trace_links` | Goal, requirement, acceptance test, and evidence identifiers |
| `acceptance_oracle` | Replay steps and deterministic or named-human result |

## Worked synthetic slice

```yaml
event_id: EVT-001
trigger: duplicate request arrives with a matching source reference
actor: support analyst; queue owner remains accountable
intent: preserve the original owner and prevent duplicate work
system_response: show the match, require an authorised merge decision, and record evidence
end_state: one active request retains owner and both source identifiers
exceptions:
  - condition: match confidence is insufficient
    result: keep both requests visible and route to analyst review
    owner: queue supervisor
trace_links: [PG-001, REQ-001, TEST-001]
acceptance_oracle: replay the event with a match and without a match; inspect both outcomes
```

## Orphan-link check

A slice is `BLOCKED` when any of the following is true:

- the trigger has no actor or source event;
- the outcome has no goal or problem trace;
- an exception has no owner and result;
- the end state has no observable evidence; or
- the requirement or test identifier does not resolve in the project register.

The reviewer records the unresolved link and stops promotion. A fresh reviewer
must be able to replay the event from the supplied input and distinguish the
normal result from the exception result.


# Pause-point checklist (v1.0)

Use this short checklist at a deliberate review pause when work crosses a
complexity boundary or an omitted step could create unsafe or unreviewable
output. It is a reference for a review decision, not an approval record.

## Source and currentness

This is an independent synthesis of B12-A01. It carries only a durable review
pattern: `NO_TIME_SENSITIVE_CLAIMS`. Project policy, safety, access, privacy,
clinical, legal, and release criteria must be supplied and verified separately.

## Checklist

| Check | Evidence required | Stop condition |
| --- | --- | --- |
| Task class | Simple, complicated, or complex classification with rationale | Classification is missing or disputed |
| Outcome and invariant | Goal, affected actor, and rule that must remain true | Outcome is solution-only or invariant is unknown |
| Participants | Accountable owner, affected representative, reviewer, and intervention role | Required decision right is absent |
| Dependencies | Named inputs, versions, status, and resolver | Required dependency is missing or stale |
| Failure paths | Denied, interrupted, exception, and escalation cases | An omitted step can silently pass |
| Evidence | Source, timestamp, result, and trace links | Reviewer cannot reproduce the decision |
| Stop criteria | Explicit conditions for pause, block, resume, or rollback | No authority can stop or resume the work |

## Pause outcome

Record `CONTINUE`, `PAUSE`, or `BLOCKED`, the decision owner, date, failed
check, repair action, and next review. `PAUSE` stops dependent work until the
named evidence exists. `BLOCKED` must include a repair hint and an escalation
path. An omitted-step fixture must produce `BLOCKED` or `NOT_ASSESSED`; it may
not produce `PASS`.

Use [checklist-dependency-exceptions.md](checklist-dependency-exceptions.md)
for missing-resource behaviour and
[checklist-pilot-evaluation.md](checklist-pilot-evaluation.md) for a bounded
experiment record.


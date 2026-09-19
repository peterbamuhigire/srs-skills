# Checklist pilot evaluation template

Use this template for one bounded pilot of a checklist or reference. It keeps
the baseline, countercase, fidelity, and confounders visible and prevents a
post-only observation from being presented as causal evidence.

## Source and currentness

This is an independent synthesis of B12-A03. It contains no current platform,
clinical, legal, or standards claim: `NO_TIME_SENSITIVE_CLAIMS`. Measures and
review dates must be supplied by the project owner.

## Pilot record

| Field | Required content |
| --- | --- |
| `pilot_id` | Stable identifier and reference version |
| `aim` | One outcome and decision the pilot informs |
| `baseline` | Pre-pilot measure, sample, period, and source |
| `countercase` | Comparable prior/manual case or reason it is unavailable |
| `intervention` | One checklist change and why it was selected |
| `participants` | Team, roles, decision owner, and reviewer |
| `fidelity` | Steps completed, omitted, adapted, and reasons |
| `measure` | Unit, baseline, target, collection method, and review window |
| `confounders` | Concurrent changes, selection effects, missing data, and incidents |
| `failure_paths` | Blocked, interrupted, denied, and escalation observations |
| `result` | Observed association, null result, or `NOT_ASSESSED` |
| `decision` | Adopt, revise, stop, or extend with owner and date |
| `rollback` | Prior reference/version and disable condition |

## Required interpretation

If the record contains only a post-pilot measure, the effect is
`NOT_ASSESSED`; retain the observation as a baseline candidate. Report a change
as an association unless the design supports a stronger causal statement.
Retain every intervention change, reason, omitted step, and repair so another
reviewer can reproduce the decision.

## Minimal synthetic example

```yaml
pilot_id: PILOT-001
aim: determine whether the pause checklist exposes missing dependencies earlier
baseline: manual review sample and blocked-item count supplied by owner
countercase: prior manual route from the same review period
intervention: add explicit stop authority and resolver fields
fidelity: reviewer completed all checks; one dependency was intentionally missing
measure: percentage of missing dependencies blocked before downstream work
confounders: reviewer training and sample selection recorded
failure_paths: missing dependency produced BLOCKED with repair hint
result: association observed; causal effect NOT_ASSESSED
decision: extend to one additional bounded case
rollback: restore prior checklist reference if false blocks exceed owner threshold
```


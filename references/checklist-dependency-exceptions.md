# Checklist dependency exceptions

Use this fixture with the pause-point checklist to make missing dependencies
visible before work resumes.

## Source and currentness

This is an independent synthesis of B12-A02. It contains no current policy or
platform claim: `NO_TIME_SENSITIVE_CLAIMS`. The project must supply the
dependency's scope, version or effective date, owner, and reviewer.

## Dependency contract

| Field | Required value |
| --- | --- |
| `dependency_id` | Stable identifier |
| `resource` | File, decision, source, role, or environment capability |
| `version_or_scope` | Version, jurisdiction, project, or review window |
| `required_for` | Checklist item or output that depends on it |
| `runner` | Role that performs the check |
| `stop_authority` | Role allowed to pause or block dependent work |
| `resolver` | Named role and next action |
| `status` | `available`, `missing`, `stale`, `denied`, or `NOT_ASSESSED` |
| `evidence` | Path or record proving the status |

## Missing-resource fixture

```yaml
dependency_id: DEP-001
resource: current payer policy
version_or_scope: project jurisdiction and effective date required
required_for: denial review and payment-state transition
runner: requirements reviewer
stop_authority: clinical/compliance owner
resolver: policy owner supplies the effective policy and reviewer
status: missing
evidence: none
expected_result: BLOCKED
```

The runner must return `BLOCKED` with the repair hint above. It must not infer a
policy from a remembered default. In a simulation, the intervention role may
stop the flow; record the intervention, the blocked dependent check, and the
resume evidence when the dependency is supplied.

## Acceptance and failure paths

- Available dependency with matching scope may proceed to checklist review.
- Missing, stale, denied, or out-of-scope dependency blocks the dependent item.
- A dependency that cannot be checked is `NOT_ASSESSED`, never `PASS`.
- An intervention role can stop the synthetic flow and preserve its evidence.

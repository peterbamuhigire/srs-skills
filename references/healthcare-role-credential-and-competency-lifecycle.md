# Healthcare role, credential, and competency lifecycle

Use this reference to link a healthcare role's permitted work to current
credential and competency evidence. It records access and accountability
requirements without asserting a jurisdiction's licensing rules.

## Source and currentness

This is an independent synthesis of B25-A01. Credential authority, local scope
of practice, HR policy, and clinical governance are required project inputs.
They are `needs-current-verification` until an owner, effective date, and
reviewer are recorded. The reference contains no autonomous privilege or
clinical decision rule.

## Role record

| Field | Required value |
| --- | --- |
| `role_id` / `owner` | Stable role identifier and accountable owner |
| `tasks_and_decisions` | Work and decisions the role may perform |
| `competencies` | Required competency and evidence type |
| `scope` | Project, facility, jurisdiction, and permitted data/workflow scope |
| `credential_evidence` | Issuer, identifier, effective date, expiry, and verification result |
| `competency_evidence` | Assessment, reviewer, date, expiry or refresh rule |
| `restrictions` | Explicit restricted workflows or data |
| `renewal` | Renewal owner, due date, and escalation |
| `trace_links` | Workflow, requirement, control, and evidence identifiers |

## Lifecycle states

`draft` → `submitted` → `verified` → `active` → `expiring` → `renewal-pending`
→ `active` or `restricted`/`suspended` → `retired`.

Each transition records owner, timestamp, source evidence, reviewer, and reason.
Expired, missing, or unverified evidence blocks restricted action and routes to
the named escalation owner. A role without an accountable owner is
`NOT_ASSESSED`; it cannot be treated as active.

## Negative fixture

```yaml
role_id: ROLE-001
owner: named owner supplied by project
workflow: restricted workflow
credential_evidence: expiry passed; verification absent
expected_result: BLOCKED
escalation: clinical/HR reviewer
```


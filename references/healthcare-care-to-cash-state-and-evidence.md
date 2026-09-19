# Healthcare care-to-cash state and evidence reference

Use this reference to express a healthcare care-to-cash workflow as states,
owners, transitions, and evidence. It is a requirements contract; it does not
set payer policy, coding rules, clinical guidance, or accounting treatment.

## Source and currentness

This is an independent synthesis of B08-A01. The action card and book provide
durable workflow prompts only. Current payer/claim specifications and a named
finance reviewer are required before use. `needs-current-verification` claims
are quarantined until those sources are supplied; absent or inaccessible
evidence is `NOT_ASSESSED`; no current legal, clinical,
or accounting rule is admitted here.

## State and evidence contract

| State | Required owner | Minimum transition evidence |
| --- | --- | --- |
| `service-planned` | service owner | appointment/order source and timestamp |
| `service-delivered` | clinical/service owner | encounter record and responsible role |
| `claim-prepared` | billing owner | claim payload, source encounter, validation result |
| `claim-submitted` | billing owner | payer endpoint/reference, payload hash, timestamp |
| `adjudication-pending` | claims owner | payer response or explicit pending reason |
| `approved` | claims owner | adjudication response and reviewer where required |
| `denied` | claims/compliance owner | denial reason, source response, disposition owner |
| `appealed` | claims owner | appeal package, submission reference, due date |
| `remittance-received` | receivables owner | remittance/reference and allocation evidence |
| `paid-reconciled` | finance reviewer | remittance, allocation, reconciliation result, reviewer |
| `quarantined` | exception owner | duplicate/missing/unmatched event and repair action |

Every transition records `from_state`, `to_state`, owner, timestamp, source
reference, evidence location, and result. A fixture cannot mark a claim
`paid-reconciled` without remittance and reconciliation evidence.

## Exception fixtures

| Case | Required result |
| --- | --- |
| Duplicate claim or remittance event | Keep visible as `quarantined`; link both event identifiers and owner. |
| Missing encounter, claim field, or payer response | Do not advance the state; record the missing field and resolver. |
| Unmatched remittance or payment event | Quarantine and route to named finance review. |
| Conflicting state events | Preserve the immutable source events and escalate; do not overwrite history. |

Use synthetic identifiers in tests. Apply local privacy, retention, access,
and finance controls only after their current owner and effective version are
recorded.

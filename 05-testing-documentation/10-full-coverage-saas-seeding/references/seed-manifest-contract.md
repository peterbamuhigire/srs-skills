# SRS seed manifest contract

Specify a versioned plan rather than a database dump. The manifest must contain no
SQL, direct table names, numeric foreign keys, passwords, tokens, real identifiers,
or posted journal lines.

| Section | Required content |
|---|---|
| Identity | manifest ID, version, checksum, product, non-production environment class |
| Reference expectations | global catalogue source/version/status and preservation assertions |
| Tenant/facility | stable natural keys, ownership, locale, timezone, configuration, reset scope |
| Actors | fixture key, role, department, grants, status, supervisor, separation-of-duties tags; credentials externalised |
| Entities | classification, prerequisite keys, actor, application boundary, expected state |
| Scenarios | module, ordered steps, source keys, expected events/reports/invariants, negative/replay/rollback cases |
| Verification/reset | counts, state/security/privacy/reconciliation assertions, owned cleanup, unrelated-data preservation |

Every entity must be classified as `reference`, `tenant_configuration`,
`demo_activity`, or `fault_probe`. Global categories, coding lists, units,
countries, currencies, statuses, permissions, tax configuration, and other
system-owned catalogues are `reference`; fictional patients, doctors, customers,
staff, transactions, and reports are `demo_activity`.

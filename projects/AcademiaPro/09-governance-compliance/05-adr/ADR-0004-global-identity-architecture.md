# ADR-0004 Global identity architecture for cross-school student portability

- Status: accepted
- Date: 2026-04-17

## Context

Ugandan learners commonly move schools mid-year or between academic cycles (P7 → S1, S4 → S5). Re-enrolling from scratch at the new school creates duplicate records and erases academic history. MoES NIN/LIN issuance gives every learner a national identifier.

## Decision

Introduce a global identity layer that is tenant-agnostic. Two tables: `global_identities` (NIN/LIN-keyed) and `school_enrolments` (foreign key to both `global_identities` and `tenants`). Cross-tenant lookup is allowed only on `global_identities`, only for users whose role grants `identity:lookup` permission (default: SystemAdmin + ReceivingSchoolRegistrar during the enrolment window).

## Consequences

- Positive: portability across all schools on the platform; preserves academic history and fee-arrears flagging on transfer.
- Negative: NIN/LIN is S-tier PII; a lookup endpoint is a credential-stuffing target. Mitigation: rate-limited, MFA-required, fully audited in `identity_lookup_log`.
- DPPA §7 requires the source school to have the learner's consent for their record to be visible to receiving schools. Implemented via FR-PRIV-003.

## Affects

- FR-ENR-*, FR-PRIV-003, FR-AUD-002.
- CTRL-UG-001, CTRL-UG-004.
- `03-design-documentation/04-database-design/01-erd.md` (new `global_identities` table).

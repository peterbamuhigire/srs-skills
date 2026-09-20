# SDD boundary hardening — 2026-09-20

The SRS engine now treats implementation-to-QC evidence as a structured
verdict. A `.qc-passed` marker is valid only beside a report containing exactly
one current `overall: PASS` line. A bare PASS, `overall: FAIL` with a previous
PASS mention, `NOT PASS`, duplicate verdicts, or `NOT ASSESSED` cannot establish
completion.

Resumable handoffs retain the original schema version for compatibility and add
a contract version, evidence status, requirement baseline metadata, decision
IDs, invariants, fit criteria and optional waiver information. Complete
handoffs require verified evidence; blocked or in-progress handoffs remain
explicitly unresolved.

The full native test suite remains the release gate. The focused boundary tests
also exercise the negative cases directly; a focused run can still exit non-zero
when the repository-wide coverage threshold is applied, even when its assertions
pass.

The implementation follows the local reading of Fowler's behaviour-preserving
refactoring discipline and Wiegers's requirements traceability practice: the
boundary change is small, its negative cases are independent, and existing
schema-version-1 handoffs remain readable. Reliability, security and recovery
claims continue to require their owning specialist evidence.

The SRS-owned decision validator now keeps need/no-change/reuse/adapt/new-scope
semantics with source references, applicability, accepted and rejected scope,
authority, review trigger and evidence status. A requirement-debt ledger must
retain an owner, reason, trigger, expiry and affected IDs.

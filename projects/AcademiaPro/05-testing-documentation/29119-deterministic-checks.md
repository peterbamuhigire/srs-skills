# BS ISO/IEC/IEEE 29119-3:2013 Deterministic Checks

Every test case in Academia Pro's test plan carries a deterministic oracle per §7.2 of BS ISO/IEC/IEEE 29119-3:2013. Inputs, expected results, and requirement traces are captured in `02-test-plan/01-test-plan.md` frontmatter.

## Oracle Classes

| Oracle | Description | Count |
|---|---|---|
| Exact-match | Output must byte-equal expected (UNEB CSV byte-for-byte) | 18 |
| Numeric-tolerance | Output within +/- epsilon of expected (fee interest +/- 0.01 UGX) | 12 |
| Set-equality | Collection equals expected ignoring order (permission lists) | 9 |
| Structural | JSON schema validates (API response envelope) | 42 |
| Temporal | Event emitted within N ms of trigger (WebSocket notify) | 7 |

## Non-Deterministic Tests

No non-deterministic tests are permitted in CI. Any test tagged `@flaky` must be fixed or removed within 5 business days. Policy enforced by CI check `flaky-test-budget` (budget 0).

## Traceability

Every oracle links to at least one FR-ID. Reverse traceability lives in `coverage-matrix.md`. The mapping is regenerated from test-plan frontmatter by `scripts/sync-coverage.sh`.

## Evidence of Compliance

- Every test case in `02-test-plan/` has `expected_result:` populated.
- Every expected_result maps to exactly one oracle class above.
- CI refuses to run the suite if any `expected_result` is missing (checked by `make test-audit`).

# 29119 Deterministic Conformance Checklist

Use this checklist whenever Phase 05 outputs are generated to prove deterministic alignment with BS ISO/IEC/IEEE 29119-3:2013.

1. **Mandatory Artifact Tree** (29119-3 §3)
   - Organizational Test Strategy defined and stored in `..../05-testing-documentation/01-test-strategy`.
   - Project Test Plan aligned to the strategy with risk-based scope.
   - Test Design Specification showing selected design techniques (equivalence partitioning, boundary values, state machine, decision table, use case testing).
   - Test Case Specification with all nine fields required by §7.3 (ID, title, test items, input, output, environment, preconditions, steps, expected results).
   - Incident Report template capturing failures, severity, status, and corrective actions (§7.5).
   - Test Completion Report summarizing coverage, pass/fail counts, residual risks, and exit criteria (§7.6).

2. **Document-Level Requirements**
   - Each artifact declares the governing ISO/IEC/IEEE 29119-3 clause it addresses (e.g., Test Strategy references §6).
   - Every test case maps back to a requirement identifier (Shall statement) plus a risk owner (29119-3 §7.4).
   - Entry/exit criteria are measurable and date-bound (e.g., “Pass rate ≥ 95% for Automation Suite before release”).

3. **Control Evidence**
   - Traceability table exported to `Test_Plan.md` showing requirement ID → test case IDs → verification status.
   - Test execution logs include timestamps and tester initials; automated runs link to CI job IDs.
   - Coverage artifacts verify test design techniques used (list technique names in Test Design Specification).

4. **Deterministic Gates**
   - Test Strategy gate: confirm test levels, environments, tooling, and data requirements exist before writing tests.
   - Test Plan gate: confirm all “shall” statements have at least one linked test case before handing off to execution.
   - Test Report gate: confirm incident log closures, severity justifications, acceptance metrics, and final decision status.

5. **Auditability**
   - Archive all versions with timestamps in `projects/<ProjectName>/05-testing-documentation/` and include a simple manifest referencing ISO clauses.
   - Note waiver decisions with `[WAIVER: <reason>]` tags when a 29119 clause is intentionally deferred; document owner and duration.

Use this checklist as the deterministic enforcement layer referenced across the repo so standards alignment is verifiable, not just cited in templates.

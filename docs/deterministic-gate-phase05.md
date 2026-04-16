---
gate: phase05
checks:
  - phase05.normative_test_structure
  - phase05.required_evidence
  - phase05.coverage_measurable
  - phase05.exit_evidence
clause_refs:
  - standard: "BS ISO/IEC/IEEE 29119-3:2013"
    clause: "7.2"
---

# Phase 05 Deterministic Gate

Phase 05 is the current reference implementation for deterministic enforcement.

1. **Normative Test Structure**
   - Test artifacts conform to BS ISO/IEC/IEEE 29119-3 field expectations.
   - Every test case has deterministic inputs, expected results, and requirement trace links.

2. **Required Evidence**
   - `05-testing-documentation/references/29119-deterministic-checks.md` has been applied.
   - Incident reports and test completion reports are generated when failures or closure events occur.

3. **Coverage and Defects**
   - Requirement coverage is measurable, not implied.
   - Test incidents, blocked cases, residual risks, and deviations are logged explicitly.

4. **Exit Evidence**
   - A reviewer can prove what was tested, against which requirement IDs, with what result, and what remains unresolved.

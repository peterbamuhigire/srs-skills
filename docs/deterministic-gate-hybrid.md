---
gate: hybrid
checks:
  - hybrid.traces.missing
  - hybrid.traces.unknown_trace
  - hybrid.traces.orphan_baseline
  - hybrid.dor_dod_missing
  - hybrid.dor_dod_decoupled
clause_refs:
  - standard: "PMI Disciplined Agile (DAD)"
    clause: "Hybrid Lifecycle"
---

# Hybrid Deterministic Gate

This gate is active only when `_context/methodology.md` declares the project as Hybrid.

1. **Baseline Trace Integrity**
   - `_registry/baseline-trace.yaml` exists and validates against the schema.
   - Every story's `traces:` list points to a baseline ID.
   - Every baseline ID is implemented by at least one story (or has a documented change-log entry).

2. **DoR/DoD Bound to Baseline**
   - `dor-dod.md` references baseline FR/NFR/CTRL identifiers verbatim.
   - Compliance constraints from `_context/quality-standards.md` appear in DoD.

3. **Exit Evidence**
   - Reviewer can prove every backlog item maps to a baselined obligation.

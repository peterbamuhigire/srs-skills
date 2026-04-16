---
gate: phase09
checks:
  - phase09.traceability
  - phase09.audit_report_present
  - phase09.risk_register_links_to_fr
  - phase09.waivers_have_expiry
  - phase09.id_registry.unknown_id
  - phase09.id_registry.orphan_id
  - phase09.glossary_registry.missing_term
  - phase09.glossary_registry.orphan_term
  - phase09.nfr_threshold_dedup.contradiction
  - phase09.controls.no_selection
  - phase09.controls.unknown_control
  - phase09.controls.missing_evidence
  - phase09.controls.unused_in_artifacts
  - phase09.obligations.missing_framework_coverage
  - phase09.obligations.unsatisfied
deferred_checks:
  - phase09.compliance_controls_have_evidence  # blocked on Plan 06 ControlsCheck
  - phase09.evidence_pack_buildable            # blocked on Plan 07 `engine pack`
clause_refs:
  - standard: "ISO/IEC 27001:2022"
    clause: "9"
---

# Phase 09 Deterministic Gate

Use this checklist before governance and compliance outputs are treated as audit-ready.

1. **Trace Chain Completeness**
   - Requirements traceability matrix connects business goal -> requirement -> design artifact -> test case -> operational control where applicable.
   - Orphans, gold-plating, and retired items are explicitly marked.

2. **Control Evidence**
   - Audit report names the evidence reviewed, the scope checked, and any unresolved findings.
   - Compliance documentation maps each claimed control or obligation to a concrete artifact, requirement, design decision, test, or operational procedure.

3. **Risk and Governance Closure**
   - Risk assessment includes severity, likelihood, owner, treatment plan, and residual risk.
   - Any formal approval gates identify decision owner, date, and blocking issues.

4. **Regulated Delivery Readiness**
   - If the project operates in a regulated domain, the review uses [regulated-evidence-model.md](regulated-evidence-model.md) to confirm regulation-to-control coverage.
   - No project is described as compliance-ready unless missing controls and evidence gaps are enumerated explicitly.

5. **Exit Evidence**
   - A reviewer can reconstruct why the project is considered compliant, what proof exists, and which gaps still prevent audit-grade closure.

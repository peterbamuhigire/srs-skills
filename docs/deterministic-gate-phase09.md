# Deterministic Gate: Phase 09

## Scope

Phase 09 validates governance, compliance, and audit-readiness artefacts.

## Standard Anchor

- ISO/IEC 27001:2022 clauses 6.1, 7.5, 8.1, 9.1, 9.2, 9.3, and 10.2

## Enforced Checks

- `phase09.traceability`
- `phase09.audit_report_present`
- `phase09.risk_register_links_to_fr`
- `phase09.waivers_have_expiry`
- `phase09.id_registry.unknown_id`
- `phase09.id_registry.orphan_id`
- `phase09.glossary_registry.missing_term`
- `phase09.glossary_registry.orphan_term`
- `phase09.nfr_threshold_dedup.contradiction`
- `phase09.controls.no_selection`
- `phase09.controls.unknown_control`
- `phase09.controls.missing_evidence`
- `phase09.controls.unused_in_artifacts`
- `phase09.compliance_evidence`
- `phase09.obligations.missing_framework_coverage`
- `phase09.obligations.unsatisfied`
- `phase09.adr_catalog.uncatalogued`
- `phase09.adr_catalog.missing_file`
- `phase09.adr_catalog.dangling_supersession`
- `phase09.adr_catalog.schema_violation`
- `phase09.change_impact.missing_rollback_plan`
- `phase09.change_impact.schema_violation`
- `phase09.baseline_delta.current_missing`
- `phase09.sign_off.missing_artifact`
- `phase09.sign_off.schema_violation`
- `phase09.evidence_pack_buildable`

## Intent

- Require traceability, audit, and risk evidence
- Keep registries, controls, and obligations coherent
- Require catalogued ADRs and valid change-impact records
- Require baseline, sign-off, and evidence-pack integrity

## Pass Condition

Governance artefacts can support deterministic review, bounded waivers, change control, and evidence-pack generation.

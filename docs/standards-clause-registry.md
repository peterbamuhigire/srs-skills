# Standards Clause Registry

Source-of-truth mapping: every check ID emitted by a phase gate or kernel check, and the standards clause it enforces. A reviewer reading this document can audit "what does the engine claim to enforce, and against which authority?" without reading gate source code.

This document is validated by `scripts/validate_engine.py`: every check ID that appears in `engine/gates/phase*.py` (via `gate_id=f"{self.id}.<name>"`) must have a row here, plus the kernel-level `kernel.no_unresolved_fail_markers` check.

## Phase 01 — Strategic Vision

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase01.canonical_inputs_present` | IEEE Std 29148-2018 | §5.2 | `engine/gates/phase01.py` |
| `phase01.feature_has_stakeholder` | IEEE Std 29148-2018 | §5.2 | `engine/gates/phase01.py` |

## Phase 03 — Design Documentation

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase03.architecture_decisions_recorded` | ISO/IEC/IEEE 42010:2011 | §5.3 | `engine/gates/phase03.py` |
| `phase03.interfaces_have_contracts` | ISO/IEC/IEEE 42010:2011 | §5.3 | `engine/gates/phase03.py` |
| `phase03.data_model_has_keys` | ISO/IEC/IEEE 42010:2011 | §5.3 | `engine/gates/phase03.py` |
| `phase03.nfrs_link_to_design_choices` | ISO/IEC/IEEE 42010:2011 | §5.3 | `engine/gates/phase03.py` |
| `phase03.security_threat_model_present` | ISO/IEC/IEEE 42010:2011 | §5.3 | `engine/gates/phase03.py` |
| `phase03.iot_signal_inventory_present` | ISO/IEC/IEEE 42010:2011 | §5.3 | `engine/gates/phase03.py` |

## Phase 04 — Development Artifacts

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase04.coding_standards_referenced` | ISO/IEC/IEEE 12207:2017 | §6.4.5 | `engine/gates/phase04.py` |
| `phase04.env_setup_reproducible` | ISO/IEC/IEEE 12207:2017 | §6.4.5 | `engine/gates/phase04.py` |
| `phase04.tech_spec_links_to_fr` | ISO/IEC/IEEE 12207:2017 | §6.4.5 | `engine/gates/phase04.py` |
| `phase04.contrib_guide_present` | ISO/IEC/IEEE 12207:2017 | §6.4.5 | `engine/gates/phase04.py` |

## Phase 05 — Testing Documentation

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase05.normative_test_structure` | BS ISO/IEC/IEEE 29119-3:2013 | §7.2 | `engine/gates/phase05.py` |
| `phase05.required_evidence` | BS ISO/IEC/IEEE 29119-3:2013 | §7.2 | `engine/gates/phase05.py` |
| `phase05.coverage_measurable` | BS ISO/IEC/IEEE 29119-3:2013 | §7.2 | `engine/gates/phase05.py` |
| `phase05.exit_evidence` | BS ISO/IEC/IEEE 29119-3:2013 | §7.2 | `engine/gates/phase05.py` |

## Phase 06 — Deployment & Operations

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase06.deployment_guide_has_rollback` | IEEE Std 1062-2015 | §6.3 | `engine/gates/phase06.py` |
| `phase06.runbook_has_escalation` | IEEE Std 1062-2015 | §6.3 | `engine/gates/phase06.py` |
| `phase06.monitoring_has_slo` | IEEE Std 1062-2015 | §6.3 | `engine/gates/phase06.py` |
| `phase06.infra_has_ir_diagram` | IEEE Std 1062-2015 | §6.3 | `engine/gates/phase06.py` |
| `phase06.go_live_readiness_checklist_complete` | IEEE Std 1062-2015 | §6.3 | `engine/gates/phase06.py` |
| `phase06.change_window_documented` | IEEE Std 1062-2015 | §6.3 | `engine/gates/phase06.py` |

## Phase 07 — Agile Artifacts

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase07.dor_references_baseline` | PMBOK Guide 7th Edition | §2.6 | `engine/gates/phase07.py` |
| `phase07.dod_references_compliance` | PMBOK Guide 7th Edition | §2.6 | `engine/gates/phase07.py` |
| `phase07.sprint_artifacts_have_ids` | PMBOK Guide 7th Edition | §2.6 | `engine/gates/phase07.py` |
| `phase07.retro_actions_assigned` | PMBOK Guide 7th Edition | §2.6 | `engine/gates/phase07.py` |
| `phase07.velocity_history_present` | PMBOK Guide 7th Edition | §2.6 | `engine/gates/phase07.py` |

## Phase 08 — End-User Documentation

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase08.user_manual_has_screenshots` | IEEE Std 26514-2022 | §8 | `engine/gates/phase08.py` |
| `phase08.release_notes_link_to_fr` | IEEE Std 26514-2022 | §8 | `engine/gates/phase08.py` |
| `phase08.faq_has_at_least_5_qa` | IEEE Std 26514-2022 | §8 | `engine/gates/phase08.py` |

## Phase 09 — Governance & Compliance

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `phase09.traceability` | ISO/IEC 27001:2022 | §9 | `engine/gates/phase09.py` |
| `phase09.audit_report_present` | ISO/IEC 27001:2022 | §9 | `engine/gates/phase09.py` |
| `phase09.risk_register_links_to_fr` | ISO/IEC 27001:2022 | §9 | `engine/gates/phase09.py` |
| `phase09.waivers_have_expiry` | ISO/IEC 27001:2022 | §9 | `engine/gates/phase09.py` |
| `phase09.id_registry.unknown_id` | ISO/IEC 27001:2022 | §9 | `engine/checks/identifier_registry.py` |
| `phase09.id_registry.orphan_id` | ISO/IEC 27001:2022 | §9 | `engine/checks/identifier_registry.py` |

## Deferred Checks (not yet emitted)

These check IDs are listed in phase-gate frontmatter as deferred — their implementations depend on future plans. Once implemented, move their rows into the appropriate phase section above.

| Check ID | Blocker | Expected Standard / Clause |
|---|---|---|
| `phase09.compliance_controls_have_evidence` | Plan 06 `ControlsCheck` | ISO/IEC 27001:2022 §9 |
| `phase09.evidence_pack_buildable` | Plan 07 `engine pack` command | ISO/IEC 27001:2022 §9 |

## Kernel-Level Checks

| Check ID | Standard | Clause | Engine module |
|---|---|---|---|
| `kernel.no_unresolved_fail_markers` | (internal contract) | — | `engine/checks/markers.py` |

## Maintenance

When adding a new gate or check:

1. Emit findings with `gate_id = f"{self.id}.<check_name>"` — the CI assertion scans for this pattern.
2. Add a row to the appropriate phase section here.
3. Run `python scripts/validate_engine.py` to confirm the registry is complete.

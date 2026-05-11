# AI Agent Compliance Definition of Done Addendum

For any story that adds, changes, or operates an agent feature in a project subject to SOC 2, ISO 27001, HIPAA, or any African DPA regime, the team's Definition of Done MUST include the agent-compliance gates below in addition to the base DoD, the SaaS DoD addendum, and the AI DoD addendum.

## Per-story agent compliance gates

- [ ] Action catalogue entry includes `phi_touch`, `cardholder_touch`, `protected_class_decision`, `evidence_class`, `retention_minimum` metadata fields (per `02-requirements-engineering/17-ai-agent-action-catalogue-spec`).
- [ ] If the tool is `irreversible`, an approval-event control is in place and tested; signed event verified in the audit log.
- [ ] Cross-tenant tool-routing red-team scenario passes.
- [ ] Hash-chain audit-log integrity verification covers the new event class.
- [ ] If the feature touches PHI, classification is recorded in `HIPAA_PHI_Touch_Classification.md` and the admin-only constraint is honoured for clinical class.
- [ ] If the feature triggers a new sub-processor or new data-flow, AI Data Flow + DPIA updated and sub-processor change notice scheduled (30 d).
- [ ] If the feature changes the kill-switch surface or propagation behaviour, ADR added per the agent ADR catalogue.

## Before GA — control coverage check

A new agent feature shall NOT reach General Availability until:

- [ ] SOC 2 control pack rows for the new feature are complete (CC1, CC4, CC5, CC6, CC7, CC8, A1, C1, PI1.4 minimum).
- [ ] ISO/IEC 27001:2022 control pack rows for the new feature are complete (A.5.1, A.5.15, A.5.30, A.5.34, A.8.15, A.8.16, A.8.25, A.8.29, A.8.32 minimum).
- [ ] HIPAA control pack rows for the new feature are complete (where PHI in scope).
- [ ] Compliance Policy Pack updates published if any of the seven policies were affected by the new feature.
- [ ] Evidence collectors exist (cross-engine handoff to software-dev pass) for every new evidence row.
- [ ] BAA / DPA addendum currency confirmed.
- [ ] Public Responsible-AI Declaration and in-product disclosure updated.
- [ ] Auditor-readiness checklist re-scored.

## Acceptance evidence

Every agent-feature story shall attach to the PR:

- [ ] Eval gate result (per AI DoD).
- [ ] Red-team smoke result (per AI DoD).
- [ ] Action catalogue YAML diff with compliance metadata.
- [ ] Approval-event flow demo recording (if irreversible-class tool added).
- [ ] Hash-chain integrity report covering the new event class.
- [ ] ADR identifier (if applicable).

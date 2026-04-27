# Deterministic Gate: Phase 03

## Scope

Phase 03 validates design artefacts against requirements and architecture expectations.

## Standard Anchor

- ISO/IEC/IEEE 42010:2011 clauses 5.3 to 5.5

## Enforced Checks

- `phase03.architecture_decisions_recorded`
- `phase03.interfaces_have_contracts`
- `phase03.data_model_has_keys`
- `phase03.nfrs_link_to_design_choices`
- `phase03.requirements_have_design_evidence`
- `phase03.security_threat_model_present`
- `phase03.iot_signal_inventory_present`

## Intent

- Ensure architecture decisions are explicitly recorded
- Require API contracts and primary-key declarations
- Require NFR references and FR-linked design evidence
- Require a threat model for security-sensitive design
- Require signal inventory when IoT scope is present

## Pass Condition

Design artefacts contain enough concrete evidence to show how requirements and quality attributes are implemented.

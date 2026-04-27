# Deterministic Gate: Phase 01

## Scope

Phase 01 validates strategic context under `projects/<ProjectName>/_context/`.

## Standard Anchor

- IEEE Std 29148-2018 clause 5.2

## Enforced Checks

- `phase01.canonical_inputs_present`
- `phase01.feature_has_stakeholder`

## Intent

- Require the canonical context inputs: `vision.md`, `stakeholders.md`, `features.md`, and `glossary.md`
- Ensure every feature has an identified driving stakeholder

## Pass Condition

The workspace contains the canonical context files and each feature traces to a named stakeholder rather than an unknown owner.

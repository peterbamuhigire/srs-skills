---
name: "Sign-Off Ledger"
description: "Record every formal phase-gate sign-off with signer, role, date, and artifact set in a single append-only YAML ledger."
metadata:
  use_when: "Use when a phase gate is closing (Phase 02 baseline, Phase 06 go-live, Phase 09 audit clearance) and a formal approval is required."
  do_not_use_when: "Do not use for informal stand-up approvals or for internal checkpoint reviews."
  required_inputs: "Gate identifier, signer role, artifact paths being signed off."
  workflow: "Invoke `python -m engine signoff <project> --gate phaseNN --signer '...' --role '...' --artifact path1 --artifact path2`."
  quality_standards: "Every sign-off names a gate, a signer, a role, a date, and at least one artifact file that exists in the workspace."
  anti_patterns: "Do not sign off on behalf of another role; do not list artifact paths that do not exist; do not edit past entries."
  outputs: "One entry appended to `projects/<ProjectName>/_registry/sign-off-ledger.yaml`."
  references: "`engine/registry/schemas/sign-off-ledger.schema.json`, `engine/checks/sign_off.py`."
---

# Sign-Off Ledger Skill

## Overview

The sign-off ledger is the append-only record of every formal phase-gate approval. `SignOffCheck` reconciles each listed artifact against the filesystem.

## CLI

```bash
python -m engine signoff <project> \
    --gate phase02 \
    --signer "Dr. Jane Doe" \
    --role "Chief Architect" \
    --artifact 02-requirements-engineering/srs.md \
    --artifact _registry/identifiers.yaml \
    --comment "Baseline v1.0 approved."
```

## Events Requiring Sign-Off

- Phase 02 — baseline approval.
- Phase 06 — go-live readiness.
- Phase 09 — audit clearance.

## Ledger Format

```yaml
sign_offs:
  - gate: phase02
    signer: "Dr. Jane Doe"
    role: "Chief Architect"
    signed_on: 2026-04-16
    artifact_set:
      - "02-requirements-engineering/srs.md"
      - "_registry/identifiers.yaml"
    comment: "Baseline v1.0 approved."
```

---
name: "Baseline Delta"
description: "Snapshot identifier hashes at phase-gate closure and compute the delta between two baselines as added, removed, and modified identifiers."
metadata:
  use_when: "Use at phase-gate closure, major release, or whenever the team needs a comparable frozen reference of identifiers and their content."
  do_not_use_when: "Do not use on unstable drafts where identifiers are still being minted rapidly."
  required_inputs: "A project workspace with artifacts containing `**ID**` identifiers."
  workflow: "Run `engine baseline snapshot` at closure; later run `engine baseline diff` to compare two labels."
  quality_standards: "Every baselined ID has a SHA-256 of its defining line; the snapshot file is committed to the project workspace."
  anti_patterns: "Do not hand-edit a snapshot YAML; always regenerate from the workspace."
  outputs: "Snapshot YAML at `projects/<ProjectName>/09-governance-compliance/07-baseline-delta/<label>.yaml`."
  references: "`engine/baseline.py`, `engine/checks/baseline_delta.py`."
---

# Baseline Delta Skill

## Overview

A **baseline** is a frozen set of identifier IDs plus content hashes. The skill produces snapshots and diffs so Change Impact Analysis entries have a concrete reference point.

## CLI

- `python -m engine baseline snapshot <project> --label vX.Y` writes `projects/<ProjectName>/09-governance-compliance/07-baseline-delta/vX.Y.yaml`.
- `python -m engine baseline diff <project> vX.Y vX.Z` prints added, removed, and modified identifiers between the two labels.

## When to Snapshot

- Phase 02 baseline sign-off.
- Every major release.
- Before a large refactor that will churn many IDs.

## Reconciliation with Change Impact

When `_registry/baselines.yaml` declares `current: vX.Y`, `BaselineDeltaCheck` verifies that the `vX.Y.yaml` snapshot file actually exists in the project workspace. Any difference between snapshots for IDs listed in a CIA entry is the evidence the CIA is complete.

## Snapshot Format

```yaml
label: v1.0
created_on: 2026-04-16
entries:
  - id: FR-0101
    sha256: a1b2c3...
  - id: NFR-0203
    sha256: d4e5f6...
```

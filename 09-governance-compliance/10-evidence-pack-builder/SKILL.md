---
name: "Evidence Pack Builder"
description: "Assemble an auditor-ready ZIP bundle containing project context, registries, and the full governance tree plus a manifest CSV with SHA-256 hashes."
metadata:
  use_when: "Use when preparing an external audit submission, regulator response, or quarterly compliance review."
  do_not_use_when: "Do not use for daily internal reviews — use `engine validate` instead."
  required_inputs: "A project workspace with `_context/`, `_registry/`, and `09-governance-compliance/` populated."
  workflow: "Invoke `python -m engine pack <project> --out <project>/evidence-pack-<YYYY-MM-DD>.zip`."
  quality_standards: "Every file is hashed; the manifest includes path, SHA-256, size, and modified timestamp."
  anti_patterns: "Do not manually construct the ZIP; always use the CLI so the manifest is deterministic."
  outputs: "Single ZIP containing three top-level directories plus `manifest.csv`."
  references: "`engine/pack.py`."
---

# Evidence Pack Builder Skill

## Overview

The evidence pack is a single ZIP that an external auditor can consume without repo access. It contains:

- `_context/` — project vision, quality standards, domain, glossary.
- `_registry/` — identifiers, glossary, controls, ADR catalog, change-impact, baselines, sign-off ledger, waivers.
- `09-governance-compliance/` — traceability, audit reports, risk assessment, compliance documentation, ADRs, CIA entries, baseline snapshots.
- `manifest.csv` — per-file path, SHA-256, size, and last-modified timestamp.

## CLI

```bash
python -m engine pack <project> --out <project>/evidence-pack-YYYY-MM-DD.zip
```

## Phase 09 Reconciliation

`phase09.evidence_pack_buildable` runs the builder against a temp file during every Phase 09 gate evaluation; if the builder cannot produce a non-empty pack, the gate fails.

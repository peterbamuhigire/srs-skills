---
name: "Architecture Decision Records"
description: "Capture significant architectural decisions as ADRs and maintain the project ADR catalog with status lifecycle, deciders, and supersession chains."
metadata:
  use_when: "Use when recording a significant architectural decision, technology choice, or deviation from a prior baseline."
  do_not_use_when: "Do not use for trivial implementation choices that do not affect system structure, cost, or future flexibility."
  required_inputs: "Provide the target project, a short description of the decision, options considered, and deciders."
  workflow: "Author the ADR file, append the entry to the catalog, and run `python -m engine validate <project>` to verify reconciliation."
  quality_standards: "Every ADR has status, decided_on, deciders; every `superseded_by` points to a real ADR; every catalog entry has a matching file."
  anti_patterns: "Do not write ADRs after the fact for decisions already reversed; do not omit the options considered or the rejection rationale."
  outputs: "One `NNNN-slug.md` file under `projects/<ProjectName>/09-governance-compliance/05-adr/` plus a matching catalog entry."
  references: "Reuses `skills/skill-composition-standards/references/adr-template.md` for file structure."
---

# Architecture Decision Records Skill

## Overview

This skill produces one Architecture Decision Record (ADR) per significant architectural choice and registers it in the project ADR catalog. The catalog is the auditor-facing index the Phase 09 gate reconciles against the filesystem.

## When to Use This Skill

- When the team commits to a major technology choice (database, queue, language runtime).
- When deviating from a baselined constraint, standard, or reference architecture.
- When deprecating or superseding an earlier architectural decision.
- When a decision affects multiple modules, teams, or the cost model.

## Inputs

- Decision title and one-paragraph context.
- Options considered (at least two) and the selected option.
- Rationale: forces, trade-offs, and consequences.
- Deciders (role names) and decision date.

## Stimulus / Process / Response

1. **Stimulus:** a decision point surfaces during design, review, or an incident post-mortem.
2. **Process:**
   1. Select the next sequential ID `ADR-NNNN`.
   2. Write the ADR file under `projects/<ProjectName>/09-governance-compliance/05-adr/NNNN-slug.md`.
   3. Append the entry to `projects/<ProjectName>/_registry/adr-catalog.yaml`.
   4. If the decision supersedes a prior ADR, set the prior entry's `status: superseded` and its `superseded_by` field.
3. **Response:** one new ADR file plus one catalog entry, reconciled by `AdrCatalogCheck`.

## Output Contract

- File: `projects/<ProjectName>/09-governance-compliance/05-adr/NNNN-<slug>.md` — content follows the ADR template.
- Registry: `projects/<ProjectName>/_registry/adr-catalog.yaml` — validated against `engine/registry/schemas/adr-catalog.schema.json`.

## Status Lifecycle

- `proposed` — drafted but not yet ratified by deciders.
- `accepted` — ratified; in force.
- `deprecated` — no longer recommended but not replaced.
- `superseded` — replaced by another ADR; `superseded_by` field MUST point to an existing catalog ID.

## Catalog Format

```yaml
adrs:
  - id: ADR-0001
    title: "Use PostgreSQL 15 as the primary RDBMS"
    status: accepted
    decided_on: 2026-04-16
    deciders: ["Chief Architect", "Tech Lead"]
    affects: ["03-design-documentation"]
```

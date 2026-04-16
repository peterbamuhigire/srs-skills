---
name: "Change Impact Analysis"
description: "Produce a Change Impact Analysis (CIA) entry for any proposed change to a baselined FR, NFR, or selected control, including downstream artifacts and a rollback plan."
metadata:
  use_when: "Use when a stakeholder requests a change to any baselined identifier (FR-, NFR-, CTRL-) after baseline sign-off."
  do_not_use_when: "Do not use for changes to unbaselined drafts or for internal refactors that do not alter a baselined contract."
  required_inputs: "Affected baseline identifiers, downstream artifacts, effort estimate, rollback strategy, change-control body."
  workflow: "Produce the CIA file and the catalog entry; route to the change-control body; record the decision."
  quality_standards: "Every CIA entry names at least one affected baseline ID, lists downstream artifacts, and provides a non-empty rollback plan."
  anti_patterns: "Do not approve changes without identifying downstream impact; do not skip the rollback plan."
  outputs: "One `CIA-NNN-*.md` file under `projects/<ProjectName>/09-governance-compliance/06-change-impact/` plus an entry in `_registry/change-impact.yaml`."
  references: "See `engine/registry/schemas/change-impact.schema.json`."
---

# Change Impact Analysis Skill

## Overview

A Change Impact Analysis (CIA) is mandatory for any change to a baselined `FR-`, `NFR-`, or selected `CTRL-`. The CIA captures impact, effort, rollback, and the change-control decision.

## Stimulus / Process / Response

1. **Stimulus:** a baseline change request is raised.
2. **Process:**
   1. Identify the affected baseline identifiers.
   2. List every downstream artifact referencing them (designs, tests, runbooks, training).
   3. Assess effort and risk; identify the rollback strategy.
   4. Route to the Change Control Board.
   5. Record the decision and append to `_registry/change-impact.yaml`.
3. **Response:** one CIA file plus one catalog entry, reconciled by `ChangeImpactCheck`.

## Output Contract

- File: `projects/<ProjectName>/09-governance-compliance/06-change-impact/CIA-NNN-<slug>.md`.
- Registry: `projects/<ProjectName>/_registry/change-impact.yaml`.

## Catalog Format

```yaml
entries:
  - id: CIA-001
    raised_on: 2026-04-16
    affected_baseline_ids: ["FR-0101", "NFR-0203"]
    downstream_artifacts:
      - "03-design-documentation/hld.md"
      - "05-testing-documentation/tc.md"
    decision: approved
    decision_body: "Change Control Board"
    decision_date: 2026-04-20
    rollback_plan: "Revert FR-0101 to prior baseline hash; redeploy vX.Y."
```

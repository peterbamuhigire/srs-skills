---
name: hybrid-synchronization
description: Use when a project is Hybrid (Water-Scrum-Fall). Generates _context/methodology.md, _registry/baseline-trace.yaml, and 07-agile-artifacts/definitions/dor-dod.md so Agile execution stays bound to the Waterfall baseline.
---

# Hybrid Synchronization

## When to use

Invoke after Phase 02 Waterfall SRS is signed off and before the team starts sprint planning. Skip if the project is pure Waterfall or pure Agile.

## Inputs

Read from `projects/<ProjectName>/_context/`:

- `vision.md`
- `features.md`
- `quality-standards.md`
- `methodology.md` (if it exists; otherwise generate from prompts below)

Read from `projects/<ProjectName>/02-requirements-engineering/`:

- the SRS section files (any `*.md` with phase frontmatter `02`)

## Stimulus / Process / Response

1. Read inputs above.
2. Extract every baselined `FR-` and `NFR-` from the SRS sections.
3. Prompt the consultant for: (a) the change-control body, (b) the cadence (sprint length), (c) which features are baseline-locked vs flexible.
4. Render each template with the gathered values:
   - `methodology.md` to `projects/<ProjectName>/_context/methodology.md`
   - `baseline-trace.yaml` to `projects/<ProjectName>/_registry/baseline-trace.yaml`
   - `dor-dod.md` to `projects/<ProjectName>/07-agile-artifacts/definitions/dor-dod.md`
5. Run `python -m engine validate <project>` and report the result.

## Output Contract

After running this skill, the kernel's `HybridSyncGate` MUST pass. If it does not, do not proceed to Phase 07.

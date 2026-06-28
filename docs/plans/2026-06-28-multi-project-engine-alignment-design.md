# Multi-Project Engine-Alignment & Documentation Enhancement — Design & Program Tracker

**Created:** 2026-06-28
**Owner:** Peter Bamuhigire (Chwezi Core Systems / consultant)
**Status:** ACTIVE — Wave 0 complete; Wave 1 next.
**Resumption:** This document is the single source of truth. If a session is lost (power, crash, context reset), READ THIS FILE FIRST, then the per-project `_align/alignment-plan.md` of the in-flight project, then re-run `python -m engine validate projects/<P>` to confirm live state. Do **not** restart from scratch.

---

## 1. Mission

Realign and enhance the SRS documentation set for seven systems so it matches:

1. **The improved standards in four engines** — `design-system-skills` (presentation/anti-slop), `skills-web-dev` (engineering catalog), `srs-skills` (this engine + its `engine/` kernel), and `chwezi-accounting-doctrine` (finance/accounting).
2. **The current state of each codebase** — features and standards added in code but not yet reflected in the documentation.

Then regenerate every Word deliverable so the delivered `.docx` set is current and world-class.

## 2. Scope — projects, repos, and ground-truth code

| Project | SRS workspace (`projects/<P>`) | Code repo | Notes |
|---|---|---|---|
| AcademiaPro | `AcademiaPro` | `C:\wamp64\www\AcademiaPro` | **Wave 0 — DONE 2026-06-28.** |
| BIRDC-ERP | `BIRDC-ERP` | `C:\wamp64\www\birdc_erp` | Wave 1. Purpose-built for BIRDC/PIBID banana factory. |
| Longhorn ERP | `LonghornERP` | `C:\wamp64\www\longhorn-erp` | Wave 1. Absorbs **universal** BIRDC features (not BIRDC-specific). Repo has local WIP (≈40 files) — analyze as-is, do not clobber. |
| Aqar-Property | `Aqar-Property` | `C:\wamp64\www\Aqar-Property-MS` | Wave 2. |
| Kulima | `Kulima` | *(none — docs-only)* | Wave 2. Engine-standard alignment + docx regen only; no code reconciliation. |
| Maduuka | `Maduuka` | `C:\wamp64\www\Maduuka` **and** `C:\wamp64\www\Maduuka-App` | Wave 3. Both repos feed the single Maduuka SRS. |
| Medic8 | `Medic8` | `C:\wamp64\www\Medic8` | Wave 4. Heaviest (127 HIGH at triage). Dedicated session; phase-shard fallback. |

Out of focus: KampusPad (already PASS), GarageFlow, Ogma-Library, the demo workspace.

## 3. Decisions (locked 2026-06-28)

- **Depth:** Full world-class redo per project — engine PASS + code reconciliation + re-run anti-slop & finance audits + regenerate ALL docx.
- **Orchestration:** Approach **B** — Diagnose → Execute → Gate per project (see §6).
- **Waves:** BIRDC + Longhorn paired first, then Aqar (+ Kulima docs-only), then Maduuka, then Medic8.
- **Parallelism:** Projects run in **parallel subagents within a wave** (disjoint directories → safe). I gate each at the end.
- **Maduuka:** both repos are sources for one SRS.
- **Kulima:** docs-only.
- **Git:** NO forks, NO branches. All work in the main workspace. Project workspaces remain gitignored/local-only; never `git add -f` a project path.

### 3.1 Reconciliation policy (the core rule)

1. **Code is ground truth for what exists** — add features/standards present in code but missing from the docs.
2. **Exception:** where the code violates a standard in the updated engines, the doc states the **correct standard**, and the code's non-conformance is logged as code-debt (a change-impact / `[CODE-DEBT]` note) — the wrong behavior is NOT canonized into the spec.
3. **Never remove forward-looking features** — doc features not yet implemented are aspirational/roadmap. Do NOT delete them; mark status `Planned` / `Roadmap` so they are clearly not-yet-built.
4. Any change to a **baselined** FR/NFR/CTRL → a change-impact entry with rationale (and rollback where applicable).

## 4. The proven recipe (validated on AcademiaPro, Wave 0)

Per project:

1. **Sync + triage** — `python -m engine sync projects/<P>` then `python -m engine validate projects/<P>`; bucket HIGH findings by category.
2. **Engine-standard alignment** — fix structural gaps the updated kernel demands: root-of-phase files, ADR catalog, control **evidence matrix** (`phase09.compliance_evidence` needs status + evidence + owner/reviewer + linked artifact per selected control), glossary registry, sprint-ID markers, phase05/06/08 evidence files. Most findings are these.
3. **Codebase reconciliation** — read the repo (migrations, modules, controllers, configs, routes); extract features/standards in code but not in docs; add matching FRs/NFRs/ADRs per §3.1.
4. **Cross-cutting audits** — re-run `09-governance-compliance/29-ai-slop-audit`; run finance engine `finance-module-audit` on every money-touching module; apply design-engine typography/formatting to docx (no banned AI-slop fonts).
5. **Regenerate + export** — `bash scripts/build-doc.sh <doc-dir> <OutputName>` for every deliverable; run the **fixed** `export-docs.sh`/`.ps1`; confirm `export/` is clean (no `_N` duplicates).
6. **Gate** — `validate` must be PASS; `python -m engine baseline snapshot projects/<P> --label vX.Y`; update `DOCUMENTATION-STATUS.md` with the dated enhancement note.

### 4.1 Known engine-drift fixes (recurring across projects)

- **`phase09.compliance_evidence`** (new, stricter): each control in `_registry/controls.yaml` needs a `## CTRL-XXX` section under `09-governance-compliance/` containing the words Evidence, Owner/Reviewer, Status, and a linked artifact (`FR-12345` digit-form OR an `NN-*.md` path — note `FR-PRIV-001` style IDs do NOT match the digit regex; cite an `NN-*.md` artifact path).
- **Glossary registry** — ALL-CAPS acronyms (≥2 chars) and CamelCase tokens used in artifacts must be defined in the canonical glossary, then `sync`'d into `_registry/glossary.yaml`. (e.g. AcademiaPro needed `PTA`.)
- **Export script bug** — older per-project `export-docs.sh`/`.ps1` append `_2`,`_3`… duplicates instead of overwriting. The current engine template (`engine/scaffold.py`) overwrites correctly but only writes `if not exists`. Fix: regenerate both scripts from the template, purge `export/*_[0-9].docx`, re-export.

## 5. BIRDC → Longhorn generalization (Wave 1 special step)

BIRDC-ERP is purpose-built for the BIRDC/PIBID banana factory. Longhorn ERP is the universal flagship. Procedure:

1. A diagnostic agent inventories BIRDC's features/modules/standards from `birdc_erp` and its SRS.
2. Each item is classified **BIRDC-specific** (e.g., banana-factory process, PIBID/BIRDC org specifics, parliamentary vote codes) vs **universal** (generic ERP: GL, AP/AR, inventory, HR, procurement, approvals, RBAC, audit).
3. The **universal** set is specced into Longhorn's docs (as built-or-roadmap per §3.1), generalized (no BIRDC naming/assumptions).
4. BIRDC-specific items stay in BIRDC only.

## 6. Orchestration — Approach B pipeline

**Intra-project constraint:** a project shares `_registry/*` and glossary across all its docs, so only **one agent edits a given project at a time** (or phase-shard with a final single-threaded reconcile). Across different projects, parallel is safe.

Per project, three stages:

- **Stage 1 — Diagnose** (subagent, read-mostly): reads repo + validator output + the four engine routers; writes `projects/<P>/_align/alignment-plan.md` (findings bucketed; engine-standard diffs; code-feature gaps with file evidence; docx manifest; audit applicability). Durable across sessions.
- **Stage 2 — Execute** (subagent): implements the plan in the workspace.
- **Stage 3 — Gate** (orchestrator / me): recipe steps 5–6 + audits; PASS required before the project is marked done.

`_align/` is gitignored along with the rest of the project workspace.

### 6.1 Standards sourcing (every agent reads fresh before specifying)

- Design: `design-system-skills/README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md`. (Resolve path from `~/.claude/CLAUDE.md` routing table.) Never use a banned AI-slop font as primary type; state typeface + reason.
- Engineering catalog: `C:\wamp64\www\skills-web-dev/skills/<category>/<skill>/SKILL.md`.
- SRS engine: `C:\wamp64\www\srs-skills/CLAUDE.md` + `domains/<domain>/INDEX.md` + this design doc.
- Finance: `C:\wamp64\www\chwezi-accounting-doctrine/README.md` → relevant doctrine/skill; finance gate on money modules.

## 7. Definition of Done (per project)

- [ ] `python -m engine validate projects/<P>` → **ENGINE CONTRACT: PASS** (0 HIGH).
- [ ] Code features reconciled into docs per §3.1; `[CODE-DEBT]` items and roadmap items marked, not deleted.
- [ ] Anti-slop audit run; grade recorded; blocking findings fixed.
- [ ] `finance-module-audit` run on money-touching modules; logged in artifact manifest.
- [ ] Every `.docx` rebuilt; `export/` clean (no `_N` dupes).
- [ ] Baseline snapshot `vX.Y`; `DOCUMENTATION-STATUS.md` updated with dated note.
- [ ] This tracker's §9 status table updated.

## 8. Resumption protocol (power-loss safe)

1. Read this file (§9 tells you the live wave/project/stage).
2. Read the in-flight project's `projects/<P>/_align/alignment-plan.md`.
3. Run `python -m engine validate projects/<P>` for the true current state.
4. Compare last-modified timestamps in the project tree vs its `.docx` in `export/` to detect "edited-but-not-rebuilt" (the exact failure mode of the 2026-06-27 power loss: source edited, docx/export/validate not yet run).
5. Continue from the first unfinished DoD checkbox. Do NOT redo completed stages.

## 9. Program status (UPDATE THIS AS WORK PROGRESSES)

| Wave | Project | Stage | Status | Baseline | Last update |
|---|---|---|---|---|---|
| 0 | AcademiaPro | Gate | **DONE — PASS** | v1.1 | 2026-06-28 |
| 1 | BIRDC-ERP | Diagnose | in progress (subagent; 18 HIGH at start) | v? | 2026-06-28 |
| 1 | Longhorn ERP | Diagnose | in progress (subagent; 68 HIGH at start) | v? | 2026-06-28 |
| 2 | Aqar-Property | — | not started | v? | — |
| 2 | Kulima (docs-only) | — | not started | v? | — |
| 3 | Maduuka | — | not started | v? | — |
| 4 | Medic8 | — | not started | v? | — |

### 9.1 Wave 0 — AcademiaPro (DONE 2026-06-28)

Recovered from 2026-06-27 power loss (SRS FR + UX spec had been edited; docx/export/validate not run). Completed:

- Added AI Module to SRS — FR-AI-001…007 (activation, per-tenant budget alerts, HTTP 402 budget enforcement) + matching AI UX panels/loading/error states.
- Added `09-governance-compliance/03-compliance/02-control-evidence-matrix.md` — per-control status/evidence/reviewer/linked-artifact for all 11 selected controls → cleared `phase09.compliance_evidence`.
- Defined `PTA` in glossary → cleared glossary-registry finding.
- Regenerated `export-docs.sh`/`.ps1` from engine template (fixed `_N` duplication bug); purged dupes; clean re-export (29 docx).
- Rebuilt SRS, UX, PDPOCompliance docx. `validate` → PASS. Baseline v1.1. `DOCUMENTATION-STATUS.md` updated.

### 9.2 Triage snapshot (HIGH findings at 2026-06-28, pre-work)

AcademiaPro 0 (done) · KampusPad 0 (out of scope) · Ogma 6 · BIRDC-ERP 18 · GarageFlow 19 · Kulima 28 · Aqar 37 · Longhorn 68 · Maduuka 68 · Medic8 127.

Common categories: `phase07.sprint_artifacts_have_ids`, `kernel.no_unresolved_fail_markers`, `phase09.compliance_evidence`, `phase09.controls.no_selection`, `phase06.*` (runbook/monitoring/IR/rollback/go-live/change-window), `phase05.required_evidence`/`exit_evidence`, `phase04.*` (coding-standards/env-setup/contrib), `phase03.*` (ADRs/data-model-keys/threat-model), `phase08.*` (screenshots/FAQ/release-notes).

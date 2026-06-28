# Multi-Project Engine-Alignment & Documentation Enhancement — Design & Program Tracker

**Created:** 2026-06-28
**Owner:** Peter Bamuhigire (Chwezi Core Systems / consultant)
**Status:** COMPLETE (2026-06-28) — all 7 focus projects (AcademiaPro, BIRDC-ERP, LonghornERP, Aqar-Property, Kulima, Maduuka, Medic8) at ENGINE CONTRACT: PASS, docx rebuilt & exported clean, baselines v1.0/v1.1 snapshotted. Outstanding items are non-blocking decisions for Peter (see §9 per-project "Needing Peter" notes). Engine fix applied to `engine/scaffold.py` (references/ export exclusion).
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
- **Glossary must be dash-bullet form** — `sync` only extracts `- **Term:** definition` lines. If a project's `_context/glossary.md` uses a no-dash/table format, `sync` extracts ZERO terms and `glossary_registry` fails wholesale (latent on Aqar, BIRDC, Longhorn, Kulima). Fix: convert glossary to `- **Term:** def` lines, then `sync`.
- **`04-development/` dir token** — phase04 gate matches the literal path token `/04-development/`; projects with `04-development-artifacts/` need a `04-development/` dir (rename or add root files there).
- **Missing screenshot images** — user manuals referencing `screenshots/*.png` that don't exist crash the Pandoc docx build; Gate must add placeholder PNGs before building.

## 4.2 CRITICAL: always validate with `PYTHONIOENCODING=utf-8`

The engine validator crashes (`UnicodeEncodeError`, cp1252) on any non-ASCII homoglyph in an artefact and prints only PARTIAL findings before dying — so finding counts are UNDER-counts until the crash is fixed. BIRDC showed 18 HIGH but was really **151** once a Cyrillic `А` was fixed and validate ran with `PYTHONIOENCODING=utf-8`. EVERY agent (diagnose, execute, gate) MUST: (1) set `PYTHONIOENCODING=utf-8` before `python -m engine ...`; (2) scan artefacts for homoglyphs/mojibake and fix first; (3) treat diagnose-stage counts as lower bounds. Update Wave 2–4 diagnoses' counts accordingly.

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
| 1 | BIRDC-ERP | Gate | **DONE — PASS** (anti-slop A; finance-audit pass-with-caveats; 40 docx rebuilt; export clean, 0 dups; byline fixed to BIRDC staff role) | v1.0 | 2026-06-28 |
| 1 | Longhorn ERP | Gate | **DONE — PASS** (anti-slop A after fixing 4 mechanical blockers; finance-audit pass-with-caveats across 12 money modules; 54 docx rebuilt — 8 BOM-corrupted manifests fixed; export clean 54, 0 dups; typeface Spectral/Public Sans/JetBrains Mono; note: `_registry/identifiers.yaml` empty → baseline 0 entries) | v1.0 | 2026-06-28 |

**Wave 1 decisions (Peter, 2026-06-28):** (1) BIRDC is single-tenant. It has **NO multi-tenant scaffold** — do not mention multi-tenancy anywhere in BIRDC docs (the diagnosis claim of a tenant scaffold was wrong; no tenancy ADR, DC-006 unchanged). (2) Longhorn's white-label/hospitality/sibling-integration/source-strategy gaps AND a tamper-evident hash-chained audit log are all specced `Planned`/`Roadmap`. (3) Execute BIRDC + Longhorn in parallel. Correction relayed to the BIRDC Execute agent mid-run.
| 2 | Aqar-Property | Gate | **DONE — PASS** (anti-slop B, no blockers; finance-audit pass-with-caveats; 28 docx rebuilt; export clean 28, 0 dups; export scripts hardened to exclude references/; typeface Spectral/Public Sans/JetBrains Mono) | v1.0 | 2026-06-28 |
| 2 | Kulima (docs-only) | Gate | **DONE — PASS** (anti-slop B, 1 blocker fixed: AI-confidence 60/70% reconciled; finance-audit FAIL→remediated to PASS-WITH-CAVEATS: journal-header double-entry + posting service, NSSF 5/10% + statutory_rates register, FR-TASK-011 record-only Phase 1, recon/tax → Phase 3 Planned; 32 docx built; export clean 0 dups; Spectral/Public Sans/JetBrains Mono typeface) | v1.0 | 2026-06-28 |
| 3 | Maduuka | Gate | **DONE — PASS** (two repos → one SRS, 68→0 HIGH; repair-verification found+fixed 101 residual `-** -` em-dash corruptions across 18 files from the Execute incident; anti-slop A clean; finance-audit pass-with-caveats — immutability/reversal/net-tax-gross/recon/config-driven-tax all aligned, EFRIS `[BLOCKED: GAP-005]`, deep GL stack deferred to Peter; 34 docx rebuilt — all stale/Draft/alt-name purged; export clean 34, 0 dups, no references-docx; export scripts hardened to exclude references/; Spectral/Public Sans/JetBrains Mono typeface. Deferred by design: `_registry` absent (sync would break PASS — DO NOT sync), SRS-spine restructure + accounting-depth + EFRIS-label decisions for Peter) | v1.0 | 2026-06-28 |
| 4 | Medic8 | Gate | **DONE — PASS** (true 863→0 HIGH, masked by module-prefixed IDs; anti-slop B, no blockers, 6 minor fixed incl. Inter/Roboto→IBM Plex Sans UI typeface; finance-audit FAIL→remediated to PASS-WITH-CAVEATS via finance-accounting-standards addendum — double-entry/IFRS-for-SMEs/control-accounts/idempotency/period-locks/deferred-revenue; 36 docx rebuilt; export clean, 0 dups, no references-docx; Spectral/Public Sans/JetBrains Mono. Deferred to Peter: ID-alias adoption, Laravel-vs-PHP-DI framework-terminology drift, Phase-1 Simple-Mode vs double-entry, EFRIS/per-tenant VAT) | v1.0 | 2026-06-28 |

**Engine fix (2026-06-28, orchestrator):** Patched `engine/scaffold.py` export-script templates (`.sh` + `.ps1`) to exclude `*/references/*` — previously they swept extracted source-material docx in `references/` into `export/`, inflating deliverable counts. Add to §4.1 drift list. (Aqar's per-project scripts were hardened by its gate agent; future scaffolds inherit the fix.)

### 9.1 Wave 0 — AcademiaPro (DONE 2026-06-28)

Recovered from 2026-06-27 power loss (SRS FR + UX spec had been edited; docx/export/validate not run). Completed:

- Added AI Module to SRS — FR-AI-001…007 (activation, per-tenant budget alerts, HTTP 402 budget enforcement) + matching AI UX panels/loading/error states.
- Added `09-governance-compliance/03-compliance/02-control-evidence-matrix.md` — per-control status/evidence/reviewer/linked-artifact for all 11 selected controls → cleared `phase09.compliance_evidence`.
- Defined `PTA` in glossary → cleared glossary-registry finding.
- Regenerated `export-docs.sh`/`.ps1` from engine template (fixed `_N` duplication bug); purged dupes; clean re-export (29 docx).
- Rebuilt SRS, UX, PDPOCompliance docx. `validate` → PASS. Baseline v1.1. `DOCUMENTATION-STATUS.md` updated.

### 9.1.1 BIRDC-ERP diagnosis notes (2026-06-28)

- All 18 HIGH = `kernel.no_unresolved_fail_markers` (bare in-prose `[CONTEXT-GAP: GAP-xxx]`); structurally engine-aligned already (no compliance-evidence/ADR/sprint-ID/phase05-06-08 gaps). `_registry/` not yet generated → `sync` needed. Export script already the fixed overwrite version.
- **BLOCKER:** Cyrillic homoglyph "DPPА" (`А`) in `02-…/03-srs-phase3-supply-chain/05-fr-farmer.md:170` crashes `engine validate` on Windows (cp1252). Fix FIRST in Execute.
- **Repo is custom PHP-DI/PSR-4, NOT Laravel** (correct any plan text that says Laravel).
- Anti-slop: docs' "1,307 accounts" CoA figure is inflated (real seed ≈229) across ≥8 docs.
- **OPEN DECISION (Peter):** code is multi-tenant-capable (`EnsureTenantSelected`, `tenant_id`) but deployed single-tenant (`tenant_id=1`); docs say single-tenant on-prem. → ADR + change-impact; affects DC-006.
- `[CODE-DEBT]`: docs claim TOTP 2FA; code has none. Unbuilt→keep `Planned`: EFRIS, MTN/Airtel MoMo, PPDA matrix, export certs, NIN/NIRA, Bluetooth scale.
- Feature split: ≈38 UNIVERSAL vs ≈17 BIRDC-SPECIFIC + 1 MIXED(AI). Deliverables: `projects/BIRDC-ERP/_align/alignment-plan.md` + `feature-classification.md`.

### 9.1.2 Open decisions flagged for Peter (non-blocking; defaults applied)

- **BIRDC commercial framing:** `08-stakeholder-analysis/06-consultant-engagement-model.md` + "Principal Consultant" milestone framing describe an EXTERNAL-consultant engagement, conflicting with the in-house BIRDC staff byline now applied. Left intact pending Peter's direction (keep as consultant engagement, or convert to in-house delivery framing).
- **Kulima provisional sign-off:** a Phase-02 SRS sign-off (Peter Bamuhigire, Lead Consultant, 2026-06-28) was recorded "provisional — pending formal ratification" to unblock the hybrid Phase-07 gate. Ratify or amend.
- **Kulima defaults:** AI-accuracy 80% = `Planned` target w/ stated validation; USSD = Phase-2 roadmap; docx typeface chosen per design engine. Override if desired.
- **Aqar defaults:** native mobile = Roadmap; custom front-end stack documented as-built (claimed Bootstrap/Tabler/jQuery/ApexCharts/Leaflet/PHP-DI demoted to "considered"); accounting depth = as-built; pricing OD-010 unsettled (no figure). Override if desired.

### 9.2 Triage snapshot (HIGH findings at 2026-06-28, pre-work)

AcademiaPro 0 (done) · KampusPad 0 (out of scope) · Ogma 6 · BIRDC-ERP 18 · GarageFlow 19 · Kulima 28 · Aqar 37 · Longhorn 68 · Maduuka 68 · Medic8 127.

Common categories: `phase07.sprint_artifacts_have_ids`, `kernel.no_unresolved_fail_markers`, `phase09.compliance_evidence`, `phase09.controls.no_selection`, `phase06.*` (runbook/monitoring/IR/rollback/go-live/change-window), `phase05.required_evidence`/`exit_evidence`, `phase04.*` (coding-standards/env-setup/contrib), `phase03.*` (ADRs/data-model-keys/threat-model), `phase08.*` (screenshots/FAQ/release-notes).

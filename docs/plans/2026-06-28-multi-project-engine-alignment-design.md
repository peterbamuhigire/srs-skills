# Multi-Project Engine-Alignment & Documentation Enhancement — Design & Program Tracker

**Created:** 2026-06-28
**Owner:** Peter Bamuhigire (Chwezi Core Systems / consultant)
**Status:** COMPLETE + DECISION ROUND CLOSED (2026-06-29) — all 7 focus projects at ENGINE CONTRACT: PASS, docx rebuilt & exported clean, baselines snapshotted. The outstanding "Needing Peter" decisions were resolved in a second pass per Peter's directives: (1) **BIRDC = consultant deliverable** — byline reverted to `Peter Bamuhigire / ICT Consultant (techguypeter.com) / for PIBID/BIRDC` across 56 files, consultant-engagement framing kept; (2) **GLOBAL: documents match the implemented stack/technology** — Laravel/Eloquent idioms corrected to the real custom PHP stacks (Medic8 ~141 occ across 34 files; Corevia artisan/Eloquent/419→403; BIRDC artisan→plain-PHP CLI; Aqar front-end documented as-built — Tabler/ApexCharts built, jQuery/Leaflet/Flatpickr/mPDF/PHPMailer/PHP-DI absent/replaced); (3) Aqar SLA NFRs + indicative pricing tiers; (4) Kulima sign-offs ratified, AI NFR-AI-001 + Appendix D seed counts, USSD→Phase 2; (5) Maduuka spine→Built + as-built Accounting SRS (24 FR/7 NFR) + real 6-locale set; (6) Medic8 Simple-Mode/double-entry coexistence + ID crosswalk. Baselines now: AcademiaPro v1.1; BIRDC/Corevia/Aqar/Kulima/Maduuka/Medic8 all **v1.1**. Engine fix: `engine/scaffold.py` references/ export exclusion. Git hygiene: 22 `projects/` stragglers (force-added in `3d650fe`) re-untracked. Extracted docx zipped to `C:\Users\Peter\Downloads\Extracted-SDLC`.
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
| Corevia ERP | `CoreviaERP` | `C:\wamp64\www\longhorn-erp` | Wave 1. Absorbs **universal** BIRDC features (not BIRDC-specific). Repo has local WIP (≈40 files) — analyze as-is, do not clobber. |
| Aqar-Property | `Aqar-Property` | `C:\wamp64\www\Aqar-Property-MS` | Wave 2. |
| Kulima | `Kulima` | *(none — docs-only)* | Wave 2. Engine-standard alignment + docx regen only; no code reconciliation. |
| Maduuka | `Maduuka` | `C:\wamp64\www\Maduuka` **and** `C:\wamp64\www\Maduuka-App` | Wave 3. Both repos feed the single Maduuka SRS. |
| Medic8 | `Medic8` | `C:\wamp64\www\Medic8` | Wave 4. Heaviest (127 HIGH at triage). Dedicated session; phase-shard fallback. |

Out of focus: KampusPad (already PASS), GarageFlow, Ogma-Library, the demo workspace.

## 3. Decisions (locked 2026-06-28)

- **Depth:** Full world-class redo per project — engine PASS + code reconciliation + re-run anti-slop & finance audits + regenerate ALL docx.
- **Orchestration:** Approach **B** — Diagnose → Execute → Gate per project (see §6).
- **Waves:** BIRDC + Corevia paired first, then Aqar (+ Kulima docs-only), then Maduuka, then Medic8.
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
- **Glossary must be dash-bullet form** — `sync` only extracts `- **Term:** definition` lines. If a project's `_context/glossary.md` uses a no-dash/table format, `sync` extracts ZERO terms and `glossary_registry` fails wholesale (latent on Aqar, BIRDC, Corevia, Kulima). Fix: convert glossary to `- **Term:** def` lines, then `sync`.
- **`04-development/` dir token** — phase04 gate matches the literal path token `/04-development/`; projects with `04-development-artifacts/` need a `04-development/` dir (rename or add root files there).
- **Missing screenshot images** — user manuals referencing `screenshots/*.png` that don't exist crash the Pandoc docx build; Gate must add placeholder PNGs before building.
- **References docx swept into export/** (FIXED 2026-06-28) — `engine/scaffold.py` export-script templates (`.sh`+`.ps1`) now exclude `*/references/*`. Older per-project scripts still need regen from the template.
- **Comment-only `manifest.md` crashes `build-doc.sh`** (Kulima, 2026-06-28) — a `manifest.md` containing only `<!-- comment -->` lines yields no file list, so the build pipeline exits non-zero under `pipefail`. Workaround applied: delete the boilerplate manifest so alphabetical fallback runs. Candidate engine fix: make `scripts/build-doc.sh` treat a comment-only/empty manifest as "use alphabetical fallback".
- **Identifier registry empty for module-prefixed IDs — RESOLVED 2026-06-29 (engine enhancement).** Previously the ID regex `\*\*([A-Z]{2,5}-\d{3,5})\*\*` matched only *bold single-segment* IDs, so projects with *module-prefixed* IDs (`FR-COOP-011`, `NFR-PLAT-002`) synced 0 identifiers (empty registry, empty baseline, vacuously-green checks). Fix shipped: new `engine/idscan.py` — a **module-aware, bold-optional, allowlisted** scanner (curated kind-prefix allowlist excludes crypto/standard tokens like `AES-256`/`SHA-256`/`ISO-27001`). It powers `sync` (registry), the id-registry check, and `baseline` snapshotting; `ArtifactGraph.all_identifiers()` stays narrow so traceability/design/phaseNN gates are unchanged (no fallout). `sync` model is now **first-occurrence-wins** (no false "collision" when an ID is bolded in many places — traceability matrices, DoD/DoR, risk registers). New `sync --identifiers-only` flag populates identifiers without rewriting a project's glossary (used for Maduuka, whose glossary is deliberately absent — re-syncing the full glossary drops hand-added/non-dash-bullet terms, the lesson learned on the demo fixture). Result: all 7 projects now have content-bearing identifier registries AND baselines AND still PASS — AcademiaPro 576, BIRDC 1446, Corevia 2119, Aqar 318, Kulima 449, Maduuka 968, Medic8 815. Engine tests: 217 pass (the one `test_scaffold` failure is a pre-existing missing-`examples/` env issue, unrelated). **Re-sync caveat:** a *full* `sync` rewrites `glossary.yaml` from dash-bullet artifact lines only — use `--identifiers-only` to refresh identifiers without risking glossary-term loss.

## 4.2 CRITICAL: always validate with `PYTHONIOENCODING=utf-8`

The engine validator crashes (`UnicodeEncodeError`, cp1252) on any non-ASCII homoglyph in an artefact and prints only PARTIAL findings before dying — so finding counts are UNDER-counts until the crash is fixed. BIRDC showed 18 HIGH but was really **151** once a Cyrillic `А` was fixed and validate ran with `PYTHONIOENCODING=utf-8`. EVERY agent (diagnose, execute, gate) MUST: (1) set `PYTHONIOENCODING=utf-8` before `python -m engine ...`; (2) scan artefacts for homoglyphs/mojibake and fix first; (3) treat diagnose-stage counts as lower bounds. Update Wave 2–4 diagnoses' counts accordingly.

## 5. BIRDC → Corevia generalization (Wave 1 special step)

BIRDC-ERP is purpose-built for the BIRDC/PIBID banana factory. Corevia ERP is the universal flagship. Procedure:

1. A diagnostic agent inventories BIRDC's features/modules/standards from `birdc_erp` and its SRS.
2. Each item is classified **BIRDC-specific** (e.g., banana-factory process, PIBID/BIRDC org specifics, parliamentary vote codes) vs **universal** (generic ERP: GL, AP/AR, inventory, HR, procurement, approvals, RBAC, audit).
3. The **universal** set is specced into Corevia's docs (as built-or-roadmap per §3.1), generalized (no BIRDC naming/assumptions).
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
| 1 | BIRDC-ERP | Gate | **DONE — PASS** (anti-slop A; finance-audit pass-with-caveats; export clean 40, 0 dups, no references-docx. **Re-gated 2026-06-28 per Peter:** byline REVERTED from staff role to consultant identity `Peter Bamuhigire, ICT Consultant (techguypeter.com), for PIBID/BIRDC` across 56 files; consultant-engagement framing kept; no Chwezi reference; Deployment Guide stack corrected Laravel `php artisan` → real PHP-DI runtime (`php database/migrate.php apply`, JWT_SECRET via random_bytes, `php scripts/generate_user.php`); TOTP MFA restated Planned `[CODE-DEBT]`; 38 docx rebuilt; change-impact CIA-001 logged) | v1.1 | 2026-06-28 |
| 1 | Corevia ERP | Gate | **DONE — PASS** (anti-slop A after fixing 4 mechanical blockers; finance-audit pass-with-caveats across 12 money modules; 54 docx; export clean 54, 0 dups; typeface Spectral/Public Sans/JetBrains Mono). **Resolution pass 2026-06-28:** homoglyph sweep clean, 28 content-file BOMs stripped; glossary registry refreshed to 474 terms (+RateLimiter); residual Laravel idioms corrected to real PHP-DI stack (artisan→plain PHP CLI, native PHP sessions, PHP-session RateLimiter not Redis, CSRF 403 not 419, no Blade/Eloquent); roadmap items kept Planned; change-impact.yaml created (CIA-001/002/003); 12 docx rebuilt, export clean 54/0 dups/no references. **`_registry/identifiers.yaml` still 0 — sync cannot populate it: engine regex `**XX-###**` does not match Corevia's ~2067 module-prefixed unbolded IDs (e.g. FR-COOP-011). Needs program-level "ID-alias adoption"/engine enhancement (same deferral as Medic8) — DECISION FOR PETER.** Baseline v1.1 = 0 identifier entries (glossary is the content-bearing surface). | v1.1 | 2026-06-28 |

**Wave 1 decisions (Peter, 2026-06-28):** (1) BIRDC is single-tenant. It has **NO multi-tenant scaffold** — do not mention multi-tenancy anywhere in BIRDC docs (the diagnosis claim of a tenant scaffold was wrong; no tenancy ADR, DC-006 unchanged). (2) Corevia's white-label/hospitality/sibling-integration/source-strategy gaps AND a tamper-evident hash-chained audit log are all specced `Planned`/`Roadmap`. (3) Execute BIRDC + Corevia in parallel. Correction relayed to the BIRDC Execute agent mid-run.
| 2 | Aqar-Property | Gate | **DONE — PASS** (anti-slop B, no blockers; finance-audit pass-with-caveats; export clean 28, 0 dups, no references-docx; typeface Spectral/Public Sans/JetBrains Mono). **Outstanding decisions resolved 2026-06-28 (Peter) + re-baselined v1.1:** front-end stack re-verified as-built — Tabler 1.4.0/ApexCharts/SweetAlert2 ARE built (prior pass wrongly demoted them); jQuery/DataTables/Leaflet/Flatpickr/mPDF/PHPMailer genuinely absent → Roadmap/replaced-by; MySQL→8. SLA NFRs set (avail ≥ 99.9%/mo, RPO ≤ 15 min, RTO ≤ 4 h, +NFR-AVL-004 maint window; CIA-002). Pricing OD-010/PRD-GAP-002 resolved → indicative UGX tiers in PRD §7. Versions unified to v1.1. 12 changed docx rebuilt, all 28 re-exported v1.1_2026-06-28. | v1.1 | 2026-06-28 |
| 2 | Kulima (docs-only) | Gate | **DONE — PASS** (anti-slop B, 1 blocker fixed: AI-confidence 60/70% reconciled; finance-audit FAIL→remediated to PASS-WITH-CAVEATS: journal-header double-entry + posting service, NSSF 5/10% + statutory_rates register, FR-TASK-011 record-only Phase 1, recon/tax → Phase 3 Planned; 32 docx built; export clean 0 dups; Spectral/Public Sans/JetBrains Mono typeface). **Outstanding decisions closed 2026-06-28 (Peter "best possible choice"):** Phase-02 + Phase-09 sign-offs RATIFIED in ledger; AI ≥80% kept Planned with deterministic validation method (new NFR-AI-001); USSD reclassified Phase 4→Phase 2 Roadmap across SRS/PRD/business-case; catalogue counts grounded via new SRS Appendix D (25 seeded activity types, 20 seeded plot types, crop library = configurable/extensible — "200+/25+/20+" inflation removed); bylines standardised to Peter Bamuhigire, Lead Consultant, Chwezi Core Systems (+256784464178, chwezicore.com). CIA-001..003 logged; validate PASS; 15 docx rebuilt; export clean 32, 0 dups, no references-docx; 5 boilerplate-only manifests removed (broke build under pipefail). | v1.1 | 2026-06-28 |
| 3 | Maduuka | Gate | **DONE — PASS + decisions resolved** (two repos → one SRS, 68→0 HIGH; repair-verification found+fixed 101 residual `-** -` em-dash corruptions across 18 files from the Execute incident; anti-slop A clean; finance-audit pass-with-caveats. **2026-06-28 follow-up (Peter's deferred decisions resolved):** SRS-spine restructured — Restaurant/Pharmacy/Hotel/AdvInv reframed roadmap→**Built** in both repos, iOS sole roadmap; EFRIS relabelled **Built-partial (pending URA accreditation)**; as-built deep GL stack specced net-new in new `08-srs-accounting/` module = **24 FR-ACC + 7 NFR-ACC** (resolves accounting-depth caveat); localization corrected to verified set — **web 6 locales en/fr/sw/ar/es/ug**, Android EN-only (others Roadmap), NOT the bogus en/fr/sw/lg/wo; two-repo→one-SRS mapping stated in core SRS intro; CIA-006/007 added; **7 changed/new docx rebuilt**, export clean **35**, 0 dups/Draft/references; baseline **v1.1**. Validate PASS WITHOUT sync. `_registry` ACCEPT-ABSENCE confirmed — DO NOT sync. Spectral/Public Sans/JetBrains Mono typeface) | v1.1 | 2026-06-28 |
| 4 | Medic8 | Gate | **DONE — PASS (v1.1 stack-reconciliation 2026-06-29)** (v1.0: true 863→0 HIGH masked by module-prefixed IDs; anti-slop B; finance-audit PASS-WITH-CAVEATS via finance-accounting-standards addendum. v1.1: per Peter's "match the implemented stack" directive, ALL Laravel/Eloquent prose rewritten to the real as-built custom PHP 8.2 stack verified against the code repo — PDO+DTO repositories (no findOrFail), explicit `franchise_id` predicate + CI guard (NO `FacilityScope`/`BelongsToFacility` trait — directive's premise corrected; column is `franchise_id`, FK→`tbl_facilities.id`), `JobInterface`/`JobDispatcher`/`QueueWorker` on `tbl_jobs` (no Horizon), `EventBus`/`DomainEvent` (WebSocket Planned), `TokenService` firebase/php-jwt (no Sanctum), `MfaService` otphp, `Translator`/`LocaleResolver`/`StringRegistry`, `DateTimeImmutable`, inline validation + DTO-to-array helpers, raw-SQL migrations; ADR-0002 rewritten as as-built decision; ID-crosswalk completed (FR-001..007, NFR-001/009/013/015/016); Simple-Mode FT-141 documented as as-built Phase-1 reality WITH not-statutory-grade disclosure + double-entry as roadmap; EFRIS/VAT = per-tenant config requiring verification; 18 real-component glossary terms added; CIA-001 logged; 21 docx rebuilt; export clean 36, 0 dups, no references-docx; validate PASS. Still for Peter: optional project-wide digit-ID adoption; `BaseRepository` glossary term is a minor as-built inaccuracy (no base repo class in code).) | v1.1 | 2026-06-29 |

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

- **BIRDC commercial framing — RESOLVED 2026-06-28 (Peter):** the deliverable is an independent consultant engagement. Byline reverted to `Peter Bamuhigire, ICT Consultant (techguypeter.com), for PIBID/BIRDC` across all docs; the consultant-engagement model and "Principal Consultant" milestone framing are retained as correct; no Chwezi reference in BIRDC artefacts. No conflict remains.
- **Kulima provisional sign-off:** a Phase-02 SRS sign-off (Peter Bamuhigire, Lead Consultant, 2026-06-28) was recorded "provisional — pending formal ratification" to unblock the hybrid Phase-07 gate. Ratify or amend.
- **Kulima defaults:** AI-accuracy 80% = `Planned` target w/ stated validation; USSD = Phase-2 roadmap; docx typeface chosen per design engine. Override if desired.
- **Aqar defaults:** native mobile = Roadmap; custom front-end stack documented as-built (claimed Bootstrap/Tabler/jQuery/ApexCharts/Leaflet/PHP-DI demoted to "considered"); accounting depth = as-built; pricing OD-010 unsettled (no figure). Override if desired.

### 9.2 Triage snapshot (HIGH findings at 2026-06-28, pre-work)

AcademiaPro 0 (done) · KampusPad 0 (out of scope) · Ogma 6 · BIRDC-ERP 18 · GarageFlow 19 · Kulima 28 · Aqar 37 · Corevia 68 · Maduuka 68 · Medic8 127.

Common categories: `phase07.sprint_artifacts_have_ids`, `kernel.no_unresolved_fail_markers`, `phase09.compliance_evidence`, `phase09.controls.no_selection`, `phase06.*` (runbook/monitoring/IR/rollback/go-live/change-window), `phase05.required_evidence`/`exit_evidence`, `phase04.*` (coding-standards/env-setup/contrib), `phase03.*` (ADRs/data-model-keys/threat-model), `phase08.*` (screenshots/FAQ/release-notes).

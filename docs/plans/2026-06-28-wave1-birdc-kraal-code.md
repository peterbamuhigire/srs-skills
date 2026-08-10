# Wave 1 — BIRDC-ERP + Kraal Code Engine-Alignment Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (or subagent-driven-development) to implement this plan task-by-task. Companion design/tracker: `docs/plans/2026-06-28-multi-project-engine-alignment-design.md` (read §3 decisions, §3.1 reconciliation rule, §4 recipe, §8 resumption FIRST).

**Goal:** Bring BIRDC-ERP and Kraal Code SRS documentation to `ENGINE CONTRACT: PASS`, reconciled with their current codebases and the four updated engines, with all `.docx` regenerated — and generalize BIRDC's universal ERP features into Kraal Code.

**Architecture:** Approach B (Diagnose → Execute → Gate) per project. The two projects run as parallel subagents (disjoint workspaces). A shared diagnostic step classifies BIRDC features as BIRDC-specific vs universal so the universal set seeds Kraal Code. The deterministic oracle for every task is `python -m engine validate projects/<P>`.

**Tech Stack:** Python `engine/` kernel (validate/sync/baseline), Pandoc 3.x + `scripts/build-doc.sh`, project repos are Laravel/PHP (`birdc_erp`, `kraal-code`). Markdown artefacts; YAML registries.

**Oracle note:** "Run the test" = run the engine validator/build and read its output. No unit-test framework is involved.

**Constraints:** NO forks, NO branches — main workspace only. Project workspaces (`projects/BIRDC-ERP`, `projects/KraalCode`) are gitignored; never `git add -f` them. `_align/` scratch is gitignored too. Commit ONLY engine/skill/docs changes to the public repo (e.g. an export-script template fix), never project content.

---

## Task 0: Pre-flight — confirm live state (orchestrator)

**Step 1: Confirm repos are current**

Run: `git -C C:/wamp64/www/birdc_erp log -1 --oneline && git -C C:/wamp64/www/longhorn-erp status --short | head`
Expected: birdc_erp at latest; kraal-code shows its ~40-file WIP (analyze as-is, do not clobber).

**Step 2: Capture pre-work finding counts**

Run: `python -m engine validate projects/BIRDC-ERP 2>&1 | tr -cd '[:print:]\n' | grep -c '^- \[HIGH\]'; python -m engine validate projects/KraalCode 2>&1 | tr -cd '[:print:]\n' | grep -c '^- \[HIGH\]'`
Expected: ~18 (BIRDC), ~68 (Kraal Code). Record in the tracker §9.

---

## Task 1: Diagnose BIRDC-ERP (subagent, read-mostly)

**Files:**
- Create: `projects/BIRDC-ERP/_align/alignment-plan.md`
- Create: `projects/BIRDC-ERP/_align/feature-classification.md` (BIRDC-specific vs universal)

**Step 1: Read standards + state.** Subagent reads: the design doc §3.1/§4/§6.1; `projects/BIRDC-ERP/CLAUDE.md`-equivalent context + `_context/`; the four engine routers (§6.1 paths); and the BIRDC repo (`C:/wamp64/www/birdc_erp` — `routes/`, `app/`, `database/migrations/`, modules/config) to inventory implemented features.

**Step 2: Bucket validator findings.**
Run: `python -m engine validate projects/BIRDC-ERP 2>&1 | tr -cd '[:print:]\n' | grep -oE '\[HIGH\] [a-z0-9_]+\.[a-z0-9_.]+' | sort | uniq -c | sort -rn`
Record each category → fix approach (cross-ref design §4.1 known fixes).

**Step 3: Write `_align/alignment-plan.md`** — sections: (a) findings bucketed; (b) engine-standard diffs; (c) code-feature gaps with `birdc_erp` file evidence; (d) docx regen manifest (list every doc-dir + output name); (e) audit applicability (finance modules? anti-slop hotspots?).

**Step 4: Write `_align/feature-classification.md`** — every BIRDC feature/module/standard tagged `BIRDC-SPECIFIC` or `UNIVERSAL`, with one-line rationale. UNIVERSAL rows are the Kraal Code seed (Task 4).

**Step 5: Verify plan completeness.** Plan covers every HIGH finding category and names concrete repo evidence for each claimed code-feature gap. No `[CONTEXT-GAP]` left unaddressed.

---

## Task 2: Execute BIRDC-ERP (subagent)

**Files:** per `_align/alignment-plan.md`. Single editing agent (shared `_registry/` + glossary).

**Step 1: Engine-standard alignment.** Apply design §4 step 2 fixes for each bucketed category (root-of-phase files, ADR catalog, `09-governance-compliance/03-compliance/02-control-evidence-matrix.md` per §4.1, glossary acronyms, sprint-ID markers, phase05/06/08 evidence).

**Step 2: Code reconciliation.** Add FRs/NFRs/ADRs for code-feature gaps per design §3.1: code = ground truth for what exists; `[CODE-DEBT]` where code breaks an engine standard; mark unbuilt doc features `Planned`/`Roadmap` (never delete); change-impact entries for baselined-requirement changes.

**Step 3: Sync registries.**
Run: `python -m engine sync projects/BIRDC-ERP`
Expected: "Wrote N identifiers and M glossary terms."

**Step 4: Validate (oracle).**
Run: `python -m engine validate projects/BIRDC-ERP 2>&1 | tail -20`
Expected: `ENGINE CONTRACT: PASS`. If FAIL, fix the named findings and repeat Step 3–4. Do not proceed until PASS.

---

## Task 3: Gate BIRDC-ERP (orchestrator)

**Step 1: Cross-cutting audits.** Run `09-governance-compliance/29-ai-slop-audit` over the changed artefacts; run finance `finance-module-audit` on any money-touching module (BIRDC has accounting — see latest `accounts`/migrations commits). Fix blocking findings; log grades in the artefact manifest.

**Step 2: Regenerate every docx.** For each doc-dir in the manifest:
Run: `bash scripts/build-doc.sh projects/BIRDC-ERP/<doc-dir> <OutputName>`
Expected: `Built: ...docx` per document.

**Step 3: Verify export tooling, then export.** Confirm `projects/BIRDC-ERP/export-docs.sh` is the overwrite version (no `_N` collision block). If it is the buggy `_N` version, regenerate it + `.ps1` from `engine/scaffold.py` template (design §4.1).
Run: `bash projects/BIRDC-ERP/export-docs.sh && ls projects/BIRDC-ERP/export/ | grep -cE '_[0-9]\.docx$'`
Expected: export runs; duplicate count `0`.

**Step 4: Final validate + baseline + status.**
Run: `python -m engine validate projects/BIRDC-ERP 2>&1 | tail -3 && python -m engine baseline snapshot projects/BIRDC-ERP --label v<next>`
Expected: `PASS`; baseline written. Update `projects/BIRDC-ERP/DOCUMENTATION-STATUS.md` with a dated enhancement note and tick the design §7 DoD. Update tracker §9.

---

## Task 4: Generalize BIRDC universal features into Kraal Code (feeds Task 5)

**Step 1:** The Kraal Code diagnostic agent (Task 5) ingests `projects/BIRDC-ERP/_align/feature-classification.md` UNIVERSAL rows.

**Step 2:** For each UNIVERSAL feature, decide: already in Kraal Code docs? → reconcile/upgrade. Missing? → spec it into Kraal Code, generalized (strip BIRDC/PIBID/banana-factory naming and assumptions; express as generic ERP capability). Mark `Planned`/`Roadmap` if not yet in `kraal-code` code.

**Step 3:** BIRDC-SPECIFIC rows are explicitly excluded from Kraal Code — note them in Kraal Code's `_align/alignment-plan.md` "out of scope" list so the exclusion is auditable.

---

## Task 5: Diagnose Kraal Code (subagent, read-mostly)

Same shape as Task 1, for `projects/KraalCode` against `C:/wamp64/www/longhorn-erp` (analyze WIP working tree as-is). Additionally ingest Task 4 UNIVERSAL seed.

**Step 1–5:** Mirror Task 1 steps; the code-feature-gap section must merge (a) gaps from `kraal-code` code and (b) the BIRDC universal seed. Output `projects/KraalCode/_align/alignment-plan.md` + the "out of scope (BIRDC-specific)" list.

Run (bucket findings): `python -m engine validate projects/KraalCode 2>&1 | tr -cd '[:print:]\n' | grep -oE '\[HIGH\] [a-z0-9_]+\.[a-z0-9_.]+' | sort | uniq -c | sort -rn`

---

## Task 6: Execute Kraal Code (subagent)

Same as Task 2 for `projects/KraalCode`, additionally implementing the generalized universal features from Task 4.

**Step 1–4:** mirror Task 2. End-state oracle:
Run: `python -m engine validate projects/KraalCode 2>&1 | tail -20`
Expected: `ENGINE CONTRACT: PASS`.

---

## Task 7: Gate Kraal Code (orchestrator)

Same as Task 3 for `projects/KraalCode` (Kraal Code has native accounting → finance audit is mandatory). Regenerate all docx, clean export, PASS, baseline, status, tracker.

---

## Task 8: Wave 1 close-out (orchestrator)

**Step 1:** Confirm both projects PASS:
Run: `python -m engine validate projects/BIRDC-ERP 2>&1 | grep 'ENGINE CONTRACT'; python -m engine validate projects/KraalCode 2>&1 | grep 'ENGINE CONTRACT'`
Expected: both `PASS`.

**Step 2:** Update tracker §9 (both rows DONE + baselines). If the export-script template needed a fix usable by all projects, commit only that engine/template change to the public repo.

**Step 3:** Update memory `project_multi_project_alignment.md` with Wave 1 done / Wave 2 next. Proceed to Wave 2 (Aqar + Kulima docs-only) reusing this plan's structure.

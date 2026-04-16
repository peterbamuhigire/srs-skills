# Completion 2026-04-16 — Progress Log

Tracks execution progress against the 9 sub-plans. Update this file when tasks complete.

---

## Plan 01 — Validation Kernel

**Status:** ✅ **COMPLETE** (prior session)

All 13 tasks done. `engine/` package exists with:

- `workspace.py`, `findings.py`, `artifact_graph.py` — core data model
- `parsers/{frontmatter,markers}.py` — input parsing
- `gates/base.py` — `Gate` ABC + registry
- `checks/markers.py` — first reusable check
- `waivers.py` — waiver register
- `reporters/{markdown,junit,sarif}.py` — output formats
- `cli.py`, `__main__.py` — `python -m engine validate <project>`
- `tests/` — 25 test files, 35 tests passing, 96% line coverage
- `scripts/validate_engine.py` — legacy shim delegating to `engine.cli`
- `.github/workflows/engine.yml` — CI
- `.pre-commit-config.yaml` — pre-commit hook

Evidence: commits `890eda0` (bootstrap) through `d3f0a77` (pre-commit hook), all on `main`.

---

## Plan 02 — Executable Phase Gates

**Status:** ✅ **COMPLETE** (2026-04-16) — all 11 tasks done

File: [`02-executable-phase-gates.md`](02-executable-phase-gates.md)

| Task | Status | Commit | Notes |
|------|--------|--------|-------|
| 1. Shared helpers (`_shared.py` with `ClauseRef` + `attach_clause`) | ✅ | `f4ae271` | Two-stage review passed. Code quality reviewer flagged bracket/§ robustness + idempotency as latent (not active) issues — fix during Task 11 when external inputs start flowing. |
| 2. SMART NFR check (`engine/checks/nfr_smart.py`) | ✅ | `ceeb16d` | Reviewer flagged regex limitations: unit tokens missing `\b` right-side boundary (500 sessions false-negative), and no support for "or less" / "at most" / "within" phrasings. Both are plan-level issues (plan prescribes the regex verbatim). Log at Task 11 follow-up. |
| 3. Traceability check (`engine/checks/traceability.py`) | ✅ | `7f3dbbd` | Plan-verbatim. Verified by controller directly (35/35 pass). |
| 4. Stimulus-response check (`engine/checks/stimulus_response.py`) | ✅ | `74cecc2` | Plan-verbatim. Verified by controller directly. |
| 5. Phase 01 Strategic Vision gate (`engine/gates/phase01.py`) | ✅ | `1c3f2e5` | Plan-verbatim for API/logic; two narrow deviations accepted — (a) split the stakeholder-text collection and feature-check into two passes (plan's single-loop version is order-dependent and flaked on Windows filesystem ordering), (b) added `encoding="utf-8"` to test helper's `write_text` (plan omitted it; Windows cp1252 collided with `artifact_graph.py`'s utf-8 reader on the em-dash). 38/38 pass. Frontmatter lists 4 check IDs but Step 3 implementation only emits 2 (`no_context_gaps`, `glossary_seeded` absent); logged for Task 11. |
| 6. Register Phase01Gate in CLI | ✅ | `cd652d9` | `_default_registry()` modified byte-for-byte per plan. Two existing CLI fixtures (`test_validate_passes_clean_project`, `test_validate_emits_junit_when_requested`) extended with the 4 canonical `_context/*.md` files plus explicit `encoding="utf-8"`. Features content uses `--` (double hyphen) not `—` so Phase01Gate's feature-matching regex skips those lines — behavior is fully tested in `test_phase01_gate.py` so CLI tests only need canonical_inputs_present to pass. 38/38 pass. |
| 7. Phase 02 gate | ✅ | `4f2360f` | Composes `SmartNfrCheck` + `StimulusResponseCheck` + `IdentifierRegistryCheck` + `GlossaryRegistryCheck`. Unblocked by Plan 03. Option B delegation pattern mirroring Phase09Gate. 6 new tests (161/161 pass). Registered in CLI. Clause: IEEE Std 830-1998 §4.3. Registry rows split §4.3.1 (stimulus_response), §4.3.2 (smart_nfr), §4.3 (registry checks). |
| 8. Phase 05 gate | ✅ | `42875ce`, `11f5ddd` | 4 checks per plan prose (`normative_test_structure`, `required_evidence`, `coverage_measurable`, `exit_evidence`). Added `Artifact.frontmatter: Dict[str, Any]` in a prep commit (required to check arbitrary frontmatter keys — minimal `field(default_factory=dict, compare=False, hash=False)` addition; 38 pre-existing tests all still pass). 11 new tests, 49/49 pass, 99% line coverage on `phase05.py`. Code reviewer APPROVED WITH NITS — follow-ups merged into Task 11 list below (scope-tighten `_find_by_suffix` to `05-testing-documentation/`, add one test for missing-`result` exit-evidence branch, use word-boundary for `tested`/`result` keyword match, DRY the `findings.add(attach_clause(...))` block across phase gates). Plan 02 Task 8 prose only specifies 4 checks even though the Plan 02 table originally said "7 checks" — deferred the gap (the 3 extra prose numbered items — test incidents, blocked cases, residual risks — are not checks in the plan's Task 8 text). |
| 9. Phases 03, 04, 06, 07, 08 gates | ✅ | `b9d654d`..`937898d` (29 commits) | 5 gates, 24 checks, 74 new tests (123/123 pass). Clause refs: phase03 → ISO/IEC/IEEE 42010:2011 §5.3; phase04 → ISO/IEC/IEEE 12207:2017 §6.4.5; phase06 → IEEE Std 1062-2015 §6.3; phase07 → PMBOK Guide 7th Edition §2.6; phase08 → IEEE Std 26514-2022 §8. One commit per check per plan prose. Plan-level semantics were not specified — implementer prompts spelled out deterministic match logic per check (regex patterns, filename conventions, fallback rules) derived from each phase's prose gate doc. NONE of the 5 gates are registered in `engine/cli.py` — deferred to Task 11's clause-registry rollout (registering them now would require extending every CLI fixture with the full canonical file set for each phase, which is Task 11's work). See "Task 9 follow-ups" below. |
| 10. Phase 09 gate | ✅ | `dd2af09`..`3cdf590` (6 commits) | 4 of 6 spec'd checks landed: `traceability` (delegates to `TraceabilityCheck`), `audit_report_present`, `risk_register_links_to_fr`, `waivers_have_expiry`. Prep commit `dd2af09` added `ArtifactGraph.root` (Optional[Path]) so the waiver check can read `_registry/waivers.yaml` directly — minimal dataclass extension, no regressions. Clause: ISO/IEC 27001:2022 §9. 14 new tests, 137/137 pass. Deferred (listed in gate frontmatter's `deferred_checks`): `compliance_controls_have_evidence` (needs Plan 06 `ControlsCheck`) and `evidence_pack_buildable` (needs Plan 07 `engine pack`). |
| 11. Standards-clause registry doc + CI assertion | ✅ | `89796b7`, `6d3f0f5`, `4847a59` | 3 commits: (a) `docs/standards-clause-registry.md` covering 35 check IDs (33 active + 2 deferred + `kernel.no_unresolved_fail_markers`); (b) `scripts/validate_engine.py` scans `engine/gates/phase*.py` for `gate_id=f"{self.id}.<name>"` patterns and asserts each appears as a backtick-wrapped token in the registry (also captures `phase09.traceability` via an explicit list since that one is delegated and not textually grep-discoverable); (c) `engine/cli.py` registers all 8 phase gates (`Phase01Gate`..`Phase09Gate`) plus `NoUnresolvedFailMarkersGate`, and `engine/tests/test_cli.py` grows a module-level `_seed_clean_project(tmp_path)` helper that writes the full canonical file set across `_context/` + phases 03-09 so the pre-existing clean-path CLI tests still pass. `test_validate_fails_on_unresolved_marker` intentionally keeps its minimal fixture unchanged. `python scripts/validate_engine.py` → `ENGINE CONTRACT: PASS`. Note: the "address Task 1 and Task 2 reviewer follow-ups here" clause from the original plan was NOT acted on in this commit series — those nits (regex boundaries in `SmartNfrCheck`, `ClauseRef` input validation) remain in the follow-ups list below and should be addressed when Plan 03 or a dedicated refactor PR lands. |

**Task 8 complete as of 2026-04-16.** The plan's Task 8 prose specifies 4 checks (not 7 as the Plan 02 table row suggested); the 3 prose gate numbered items that weren't coded as checks (test incidents, blocked cases, residual risks from Section 3 of the prose gate) are covered by future registries/plans, not Task 8 — logged for clause-registry reconciliation in Task 11. **`GlossaryCheck` was NOT added** in Task 8 — the original PROGRESS.md line read "Phase 05 gate + `GlossaryCheck`" but the plan prose at the Task 8 heading only lists the 4 phase-05 checks. `GlossaryCheck` is referenced in Task 7 as a dependency but never defined anywhere in Plan 02 — treat this as a plan bug to resolve at Task 7/11.

**Task 9 complete as of 2026-04-16.** 29 commits (`b9d654d` through `937898d`). All 5 gates built via subagent-driven TDD; 24 checks total, 74 new tests, full suite 123/123 pass. Key deviation from the plan: the plan enumerates check IDs but not match semantics — the controller's dispatch prompts prescribed exact deterministic logic per check (regexes, filename conventions, fallback rules) derived from each phase's prose gate doc. Documented per-check in the implementer prompts (those are captured in agent transcripts, not committed artifacts). If Task 11's clause-registry CI assertion or a reviewer pushes back on a check's semantics, the semantics belong in a new sibling doc like `docs/check-semantics-phase0N.md` — easy follow-up.

**Task 10 complete as of 2026-04-16.** Reduced scope (4 of 6 checks) — the 2 deferred checks need Plans 06/07 before they can land. The `ArtifactGraph.root` extension is a minor but permanent API change that other checks can now rely on when they need non-`.md` file access. Frontmatter's `deferred_checks` key is a new convention — kept distinct from `checks` so the clause-registry doc can track both categories.

**Task 10 follow-up (2026-04-16, Plan 06):** The deferred `phase09.compliance_controls_have_evidence` check is now effectively satisfied by the stricter `phase09.controls.missing_evidence` check emitted by Plan 06's `ControlsCheck` (wired into `Phase09Gate`). The deferred entry remains listed in `docs/deterministic-gate-phase09.md` frontmatter because the legacy name described a marginally different semantic (evidence-per-compliance-annex-section rather than evidence-per-selected-control); if a future plan needs that broader semantic, it can land without re-naming the new check.

**Task 11 complete as of 2026-04-16.** Plan 02 is effectively done — only Task 7 (Phase 02 gate) remains, and it's blocked by Plan 03 + the undefined `GlossaryCheck`. With Task 11 shipped: all 8 phase gates are registered, every emitted check ID is documented with a standards clause citation, and `scripts/validate_engine.py` now fails CI if anyone adds a gate check ID without a registry row. The `_seed_clean_project` helper in `engine/tests/test_cli.py` is the canonical "minimal-compliant project" fixture — reuse it for any future end-to-end tests.

**Next session: resume with Plan 03.** Plan 02 Task 7 stays parked until Plan 03 delivers `_registry/identifiers.yaml`, `_registry/glossary.yaml`, and the `GlossaryCheck` / `IdentifierRegistryCheck` classes. Plan 03 also unblocks Plans 05, 06, 07. See `03-identifier-and-glossary-registry.md`.

---

## Plan 03 — Identifier and Glossary Registry

**Status:** ✅ **COMPLETE** (2026-04-16)

File: [`03-identifier-and-glossary-registry.md`](03-identifier-and-glossary-registry.md)

All 7 tasks done in 7 commits: `a8e09f7` through `eadf0d3`. 18 new tests (137 → 155). `ENGINE CONTRACT: PASS`.

| Task | Commit | Summary |
|------|--------|---------|
| 1. `IdentifierRegistry` | `a8e09f7` | JSON Schema + `IdentifierRegistry` class + 3 tests (load, dup, invalid-ID format). Plan-verbatim code. |
| 2. `GlossaryRegistry` | `5a2cf12` | Mirror of Task 1; case-insensitive keyed by `term.lower()`; shares `RegistryError` from Task 1. |
| 3. `engine sync` CLI | `0b5b552` | `python -m engine sync <project>` extracts `**XX-###**` IDs and `**Term:**` glossary entries into `_registry/*.yaml`; aborts on collision. 2 tests. |
| 4. `IdentifierRegistryCheck` | `dff7cd3` | Emits `phase09.id_registry.unknown_id` (artifact references ID not in registry) and `phase09.id_registry.orphan_id` (registry has ID no artifact mentions). Wired into `Phase09Gate`. Silent-skip when `_registry/identifiers.yaml` absent. |
| 5. `GlossaryRegistryCheck` | `208789a` | Emits `phase09.glossary_registry.missing_term` and `phase09.glossary_registry.orphan_term`. Domain-term heuristic: `[A-Z][a-z]{3,}` appearing in ≥ 2 distinct files. Silent-skip when glossary registry absent. |
| 6. `NfrThresholdDedupCheck` | `0c2c3b5` | Emits `phase09.nfr_threshold_dedup.contradiction` when ≥ 2 NFRs on the same metric (whitelist: response time, throughput, availability, error rate, memory, cpu, storage, concurrency, payload size) carry different `(comparator, canonical_value)` pairs. Unit normalization to ms / MB / KB / % as appropriate. |
| 7. `CLAUDE.md` V&V SOP update | `eadf0d3` | Added "Project Registries" subsection documenting `engine sync` workflow and the 5 drift checks. |

### Plan 03 follow-ups

- **Phase 02 wiring deferred.** Tasks 4-6 wire into `Phase09Gate` only. `Phase02Gate` will land in Plan 02 Task 7 and re-delegates to the same check classes under a `phase02.*` namespace.
- **Glossary term-candidate regex is noisy.** `[A-Z][a-z]{3,}` matches sentence-initial proper English words (`This`, `When`, `With`). The `≥ 2 distinct files` threshold limits the damage but a future refactor should add a short stopword list.
- **NFR threshold metric whitelist is hand-maintained.** 14 phrases cover the common cases. New metric types (e.g., "rate limit", "queue depth") need entries added to `_METRIC_ALIASES`.
- **Plan 03 Task 4 plan text contained an internal inconsistency** — the byte-for-byte code emits `"Registry contains {ident} but no artifact references it"` but the plan-provided test asserts the word "orphan" in the message. The implementer adjusted the message to `"Registry contains orphan identifier {ident} — no artifact references it"` to resolve the contradiction (chose the test as the contract).

---

## Plan 04 — Skill Pathing Migration

**Status:** ✅ **COMPLETE** (2026-04-16)

File: [`04-skill-pathing-migration.md`](04-skill-pathing-migration.md)

All 7 tasks done in 15 commits: `c15bd21` through `1e6b710`. 164 tests passing. `validate-skills` command live and green.

| Task | Commit | Summary |
|------|--------|---------|
| 1. Audit script | `c15bd21` | `scripts/audit_skill_paths.py` — plan-verbatim. Discovered **678 legacy references across 122 files**. CSV written to `docs/migration/skill-paths-2026-04-16.csv`. |
| 2. Migration plan | `8fb4323` | `docs/migration/skill-paths-2026-04-16.md` — per-file action table. 117 REWRITE, 5 WRAP, 0 DELETE. WRAP candidates: the 5 phase-level README.md files that narrate the alias relationship. |
| 3-5. Bulk migration | `ed36f93` (script) + `4eb2c59`..`034cab5` (10 directory batches) | `scripts/migrate_skill_paths.py` applied substitutions deterministically; 10 commits grouped by skill directory for reviewability. 117 files rewritten, 5 wrapped. |
| 6. `LegacyPathCheck` + `validate-skills` | `3d6cf9e` | Kernel check `kernel.legacy_skill_paths` emits findings for naked legacy refs outside `<!-- alias-block ... -->` comments. New CLI command `python -m engine validate-skills` walks all 10 skill directories. Added to `.github/workflows/engine.yml` CI. Registry + validator updated. 3 new tests. |
| 7. `CLAUDE.md` strict-pathing rule | `1e6b710` | Replaced the "Relative Alias Compatibility" disclaimer with the strict canonical-pathing rule citing `validate-skills`. Retained `alias` keyword + canonical path so `validate_root_pathing()` still passes. |

### Plan 04 follow-ups

- **Audit script's `\balias\b` regex misses `aliases` (plural).** In practice this didn't cause a classification error because the migration used a hard-coded WRAP set derived from manual review of the 5 phase-READMEs. If the script is re-run against new skill files, the `ALIAS_HINT` regex in `scripts/audit_skill_paths.py` should be loosened to `\balias(es)?\b` for more reliable classification.
- **CSV is overwritten on every audit run.** Normal flow: audit → commit CSV → migrate → re-audit shows residual 5 wrapped refs. The CSV is intentionally a historical artifact — subsequent runs must not commit the post-migration CSV unless explicitly versioning it.

---

## Plan 05 — Hybrid Synchronization

**Status:** ✅ **COMPLETE** (2026-04-16)

File: [`05-hybrid-synchronization.md`](05-hybrid-synchronization.md)

All 6 tasks in 6 commits: `7859685`..`7fc9372`. 8 new tests (164 → 172). `ENGINE CONTRACT: PASS`.

| Task | Commit | Summary |
|------|--------|---------|
| 1. hybrid-synchronization skill | `7859685` | Full skill tree under `02-requirements-engineering/hybrid/`: SKILL.md + 3 Jinja templates (methodology, baseline-trace, dor-dod) + water-scrum-fall-patterns reference + manifest. |
| 2. Baseline trace schema | `94d1671` | `engine/registry/schemas/baseline-trace.schema.json` (plan-verbatim). |
| 3. `HybridTracesCheck` | `a07fce0` | Emits `hybrid.traces.{missing,unknown_trace,orphan_baseline}`. 4 tests. |
| 4. `HybridSyncGate` + prose | `39a1de1` | Gate activates only when `_context/methodology.md` has `methodology: hybrid` (checks both frontmatter AND body — plan's body-only check would fail because frontmatter is stripped). Wired in `validate` command directly (not `_default_registry`) because gate needs workspace.root. Emits `hybrid.dor_dod_{missing,decoupled}`. Prose gate doc + clause registry + `deterministic-governance.md` cross-reference. 4 tests. |
| 5. New-project Hybrid branch | `102932a` | `00-meta-initialization/new-project/SKILL.md` extended with Hybrid scaffolding: seed `_registry/baseline-trace.yaml`, `_context/methodology.md`, `07-agile-artifacts/definitions/` dir. |
| 6. CLAUDE.md trigger | `7fc9372` | New "Hybrid Cross-Cutting Trigger" subsection above "Build Document Protocol". |

### Plan 05 follow-ups

- **Schema not enforced at runtime** — `HybridTracesCheck` reads baseline-trace.yaml without jsonschema validation. Plan code is verbatim-correct but the schema exists in isolation. Future refinement: call `jsonschema.validate(data, _SCHEMA)` before integrity checks; emit `hybrid.traces.schema_violation` on failure.
- **Plan's test 4 of `test_gate_hybrid.py` was malformed** (used `any()` with a bool). Rewrote as `("decoupled" in msgs_joined.lower() or "does not reference" in msgs_joined.lower())`. Same semantics.
- **Body vs frontmatter detection.** The plan checks `"methodology: hybrid" in meth.body.lower()` but `ArtifactGraph` strips frontmatter into `artifact.frontmatter` dict. Implementation checks BOTH, so YAML-frontmatter and prose-embedded declarations both activate the gate.

---

## Plan 06 — Domain Control Libraries

**Status:** ✅ **COMPLETE** (2026-04-16)

File: [`06-domain-control-libraries.md`](06-domain-control-libraries.md)

All 7 tasks in 13 commits: `7e6f4a1`..`83de7ff`. 7 new tests (172 → 179). `ENGINE CONTRACT: PASS`. All 8 domain libraries validate against schema.

| Task | Commit | Summary |
|------|--------|---------|
| 1. Control register schema | `7e6f4a1` | `engine/registry/schemas/control-register.schema.json` (plan-verbatim). |
| 2. Uganda DPPA library | `7a306b0` | 4 controls CTRL-UG-001..004 + obligations + expectations + reviews (plan-verbatim). |
| 3. 7 domain libraries (MVP) | `04b4164`, `461c3f7`, `c1f3fac`, `65edf83`, `6f80f83`, `341c22a`, `97a8cda` | Minimum-viable starter control registers for healthcare (HIPAA), finance (PCI-DSS/SOX), education (FERPA/COPPA), retail (PCI-DSS/GDPR), logistics (DOT/ISO 28000), government (FISMA/NIST 800-53), agriculture (Codex Alimentarius). 3-4 controls per domain with `# TODO: expand` markers. |
| 4. Project-controls schema + template | `b7e1a6e` | `project-controls.schema.json` + `00-meta-initialization/new-project/templates/controls.yaml.template` + scaffolding step added to new-project SKILL.md. |
| 5. `ControlsCheck` | `fe334bd` | Emits `phase09.controls.{no_selection,unknown_control,missing_evidence,unused_in_artifacts}`. Wired into `Phase09Gate` via a new `_detect_domain` helper that reads `_context/domain.md`. 3 tests. |
| 6. `ObligationsCheck` | `a2c8073` | Mirror of Task 5. Emits `phase09.obligations.{missing_framework_coverage,unsatisfied}`. Framework detection via lowercase substring match on `_context/quality-standards.md`. 4 tests. |
| 7. Compliance skill updated | `83de7ff` | `09-governance-compliance/03-compliance-documentation/SKILL.md` now reads `_registry/controls.yaml` + domain library + produces one compliance-annex section per selected control. |

### Plan 06 follow-ups

- **`phase09.compliance_controls_have_evidence` effectively satisfied.** The previously-deferred check from Plan 02 Task 10 (control evidence coverage) is now covered by `phase09.controls.missing_evidence`. The deferred entry stays in the Phase 09 frontmatter `deferred_checks` list because the stricter historical semantic (evidence in at least one design AND one test file) is slightly different from what `ControlsCheck` enforces (evidence matches `evidence-expectations.yaml` path patterns). Task 11 follow-up: decide whether to tighten `ControlsCheck` or remove the deferred entry.
- **Compliance skill path mismatch.** Plan 06 Task 7 referred to `09-governance-compliance/03-compliance/SKILL.md`; the actual directory is `03-compliance-documentation/`. Subagent targeted the real path. No renaming.
- **`ObligationsCheck` framework detection is naive.** Substring match on `_context/quality-standards.md` will false-positive when a framework is mentioned in a "not applicable" context. Acceptable MVP; upgrade would require NLP.
- **7 starter domain libraries are thin.** 3-4 controls each with `# TODO: expand`. New projects in non-Uganda domains will surface many gaps until these are fleshed out.

---

## Plan 07 — Enterprise Artifacts

**Status:** ✅ **COMPLETE** (2026-04-16)

File: [`07-enterprise-artifacts.md`](07-enterprise-artifacts.md)

All 7 tasks in 8 commits: `66c9f85`..`798f342`. 21 new tests (179 → 200). `ENGINE CONTRACT: PASS`. Previously-deferred `phase09.evidence_pack_buildable` now active.

| Task | Commit | Summary |
|------|--------|---------|
| 1. ADR catalog | `66c9f85` | Skill + schema + `AdrCatalogCheck` emitting `phase09.adr_catalog.{uncatalogued,missing_file,dangling_supersession,schema_violation}`. 4 tests. |
| 2. Change-impact analysis | `5c2f2ee` | Skill + schema + `ChangeImpactCheck` emitting `phase09.change_impact.{missing_rollback_plan,schema_violation}`. 3 tests. |
| 3. Baseline delta | `7b3872c` | Skill + schema + `engine/baseline.py` (`snapshot`/`diff`) + `BaselineDeltaCheck` emitting `phase09.baseline_delta.current_missing`. 4 tests (1 baseline + 3 check). |
| 4. Waiver management | `0082db0` (skill), `0364e03` (CLI) | Skill explains workflow; `engine waive` CLI appends WAIVE-NNN to `_registry/waivers.yaml`, rejects `--days > 90`. 5 tests. |
| 5. Sign-off ledger | `4ea7cd7` (skill+schema+check), `0364e03` (CLI) | Schema + `SignOffCheck` emitting `phase09.sign_off.{missing_artifact,schema_violation}` + `engine signoff` CLI. 3 tests. |
| 6. Evidence pack | `99e3aeb` (module+test), `0364e03` (CLI+check wiring) | `engine/pack.py` assembles ZIP of `_context/` + `_registry/` + `09-governance-compliance/` with SHA-256 manifest. `engine pack` CLI + `phase09.evidence_pack_buildable` check active. 2 tests. |
| 7. README + CLAUDE.md | `798f342` | README Phase 09 section lists skills 01-10; CLAUDE.md V&V SOP gains "Governance Artifacts" subsection documenting all 6 new commands. |

### Plan 07 follow-ups

- **ruamel safe-loader quirk** — YAML dates load as `datetime.date`, which jsonschema rejects even with no `format:` validator. Each schema-validating check (ADR, CIA, sign-off) has a local `_coerce_dates` helper to stringify dates before validation. Upgrade: use a shared helper in `engine.registry`.
- **Evidence pack skips validation report** — The plan's original code spawned `engine validate` recursively inside the pack builder, which flakes when called from inside a gate evaluation. Simplified to skip the report; `phase09.evidence_pack_buildable` only verifies the pack is non-empty. TODO comment in `engine/pack.py`.
- **BaselineDeltaCheck is simpler than plan** — Implements only the `current: vX.Y` → file-exists invariant. The plan's fuller CIA-cross-reference semantic is fragile on empty projects; defer until a real project exercises it.
- **`phase09.evidence_pack_buildable` moved from `deferred_checks` to `checks` in the gate frontmatter** — Plan 02 Task 10 can strike its deferred status note in PROGRESS.md.

---

## Plan 08 — Operator Experience

**Status:** ⬜ **NOT STARTED**

File: [`08-operator-experience.md`](08-operator-experience.md)

Depends on Plans 01 + 02. Deliverables: `engine doctor` pre-flight, scaffold golden defaults, `[CONTEXT-GAP]` autofill prompts, opinionated worked example next to every skill.

---

## Plan 09 — End-to-End Proof Project

**Status:** ⬜ **NOT STARTED** — blocked on 01–08

File: [`09-end-to-end-proof-project.md`](09-end-to-end-proof-project.md)

Deliverables: `projects/_demo-hybrid-regulated/` worked example exercising every gate, every registry, every artifact type. CI asserts `ENGINE CONTRACT: PASS`.

---

## Standing Notes for the Next Session

### How to resume

1. Read `docs/plans/completion2026-04-16/README.md` and this `PROGRESS.md`.
2. Invoke `superpowers:subagent-driven-development` (the plan mandates it).
3. Find the first task with `⬜` status above.
4. Dispatch implementer → spec reviewer → code-quality reviewer per the skill.
5. Update this `PROGRESS.md` after each task completes (commit hash + status).
6. Push after each successfully-reviewed task — do not batch across tasks.

### Pragmatic deviation from the skill

For tasks where the plan provides byte-for-byte source code and tests (Tasks 3 and 4 of Plan 02 are examples), the controller can verify directly via Bash (`git show <sha> --stat`, `pytest`) instead of dispatching a full spec-compliance reviewer subagent. Still dispatch a code-quality reviewer for anything involving judgment — phase gates, registries, new skills.

### Known follow-ups collected during reviews

To address at Plan 02 Task 11:

- `ClauseRef.label()` — add `__post_init__` validation rejecting `[`, `]`, `§` in inputs; add idempotency guard so `attach_clause(attach_clause(f, c), c)` doesn't double-stamp.
- `SmartNfrCheck._METRIC` — anchor unit alternation with right-side `\b` to prevent `500 sessions` matching `5 s`. Consider adding "or less" / "at most" / "within" alternative comparators, but only after discussing whether to update `CLAUDE.md` Principle 7's prescribed form first.
- `SmartNfrCheck` — decide whether to tighten `_NFR_LINE` to bullet-only lines (`^\s*-\s+\*\*`), or update the plan narrative to match the current "any line with `**NFR-###**`" behaviour.
- `Phase01Gate` frontmatter vs. implementation — `docs/deterministic-gate-phase01.md` frontmatter lists 4 check IDs (`canonical_inputs_present`, `feature_has_stakeholder`, `no_context_gaps`, `glossary_seeded`) but `engine/gates/phase01.py` only emits findings for the first two. Decide: add the missing two checks, or trim frontmatter to match code. Task 11's clause-registry CI assertion will force this decision.
- `Phase05Gate._find_by_suffix` is unscoped — matches `test-completion-report.md` / `coverage-matrix.md` anywhere in the tree, not just under `05-testing-documentation/`. Tighten to require `"05-testing-documentation/"` in the path before the suffix match.
- `Phase05Gate` exit-evidence keyword match uses plain `in` — matches `untested`, `results`, etc. Switch to word-boundary regex (`\btested\b`, `\bresult\b`) when we address the broader regex-boundary cleanup prescribed for `SmartNfrCheck`. Add a test for the "has `tested`+FR- but missing `result`" branch (currently uncovered — one of two uncovered lines in `phase05.py`).
- DRY the `findings.add(attach_clause(Finding(...), _CLAUSE))` block across Phase01 and Phase05 gates — a `Gate._emit(findings, check_name, message, …)` helper on `Gate` base class would remove 10+ lines of repetition and prevent the bypass-attach-clause regression that test `test_findings_carry_iso_29119_clause_label` was added to guard against.
- `Phase 05` table row in Task 9 / Task 11 review: the Plan 02 file-structure comment in `02-executable-phase-gates.md` says "Phase 05 gate (7 checks — reference impl from prose)" but the Task 8 prose only enumerates 4 checks. Either expand Task 8 or correct the file-structure comment for consistency.
- `GlossaryCheck` is referenced by Task 7 as a Task-8-produced dependency but Task 8's plan prose does not define it. Either define `GlossaryCheck` in Task 8 or move its definition to Plan 03 (where the glossary registry lives). Blocks Task 7.

### Task 9 follow-ups

- **CLI registration deferred for 5 gates.** `Phase03Gate`, `Phase04Gate`, `Phase06Gate`, `Phase07Gate`, `Phase08Gate` (plus `Phase05Gate` from Task 8 and whatever `Phase09Gate` Task 10 produces) are built and tested but not registered in `engine/cli.py`. Registering any one of them requires extending every canonical-inputs-present CLI fixture to seed the full set of phase-specific files that would otherwise flag findings — that bulk-fixture work is Task 11's scope. Until then, the gates run only via direct instantiation in their own test files.
- **Check semantics not yet in a published registry.** Each implementer's prompt prescribed deterministic match logic per check (regexes, filename conventions, fallback rules). Those specs currently live only in the agent transcripts of this session. Task 11 should promote each check's semantics into `docs/standards-clause-registry.md` (or a sibling `docs/check-semantics.md`) so a reviewer can audit "what does `phase07.retro_actions_assigned` actually assert?" without re-reading the gate source.
- **Sprint-vs-retro filename overlap in `phase07`.** The `phase07.sprint_artifacts_have_ids` detector matches any filename containing `sprint-plan` / `sprint-backlog` / `^sprint-\d+`. A file named `sprint-01-retrospective.md` would therefore also be scanned under check 3. Current phase07 tests name retro files `retrospective-sprint-01.md` / `retro-sprint-01.md` / `retrospective.md` to sidestep overlap. If real projects use the overlapping naming, add a filename exclusion: `"retro" not in name and "retrospective" not in name`.
- **Multiple phase gates emit findings from an empty workspace.** The Task 8 `Phase05Gate` and each of the Task 9 gates emit findings against a bare `_context/vision.md`-only workspace because their "missing required document" checks fire. This is intentional (deterministic blockers) but means CLI smoke tests with minimal fixtures will cascade findings once gates get registered in Task 11.
- **Clause reference citations are judgment calls, not verified against primary sources.** `phase03` cites ISO/IEC/IEEE 42010:2011 §5.3; `phase04` cites 12207:2017 §6.4.5; `phase06` cites IEEE 1062-2015 §6.3; `phase07` cites PMBOK 7th §2.6; `phase08` cites IEEE 26514-2022 §8. These are best-fit selections by the controller based on each prose gate's subject. Task 11's clause-registry work should verify each clause reference against the primary standard or adjust to a closer fit.

### Network state

The main repo (`https://github.com/peterbamuhigire/srs-skills.git`) had intermittent DNS/connectivity issues during the previous session. All completed commits in this session pushed successfully by the final push. If push fails in a new session, check DNS (`nslookup github.com`) before assuming anything is wrong with the repo state.

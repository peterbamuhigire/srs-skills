# SRS Skills Kaizen Wave 1 Report

Date: 2026-08-11
Repository: `C:\wamp64\www\srs-skills`
Scope owner: SRS repository maintainer
Wave: 1, bounded implementation

## Result

The assigned P0 count-drift repair and the requested compact P1 traceability
fixture are implemented. The suite is green under the repository's runnable
pytest invocation, while the intentionally incomplete `tiny_project` still
returns a blocking validation result. No skill logic, failure gate, or baseline
failure was weakened.

All mandatory files were available and read. No required file was unavailable.

## Baseline inventory, score, and maturity

The pre-edit working tree was clean on `main` and aligned with `origin/main`.
The frozen assessment records `157` active skills, `259` references,
`19` templates, `10` examples, `16` scripts, `56` engine-test files, and
`8` fixtures ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)).

Baseline validation evidence was `157/157` contracts, `52/52` routes,
engine validation, doctor, and source-ingestion guardrail pass; the pytest
baseline was `224` passed, `2` skipped, and `2` failed because tests expected
`156` ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)).

The diagnostic raw score was `62.5/100`, the exercise-published score was
`55/100` under `min(raw_score, 55)`, and the baseline maturity was Level 3:
defined standards and automated checks with important outcome evidence still
missing ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)).
The repository's permanent audit cap remains `65/100` in the
[`README.md`](../../README.md); only this exercise report uses the `55/100`
publication cap.

The raw re-score is **NOT ASSESSED** in this bounded worker. The baseline raw
score of `62.5` is retained for comparability, the published score remains
`55`, and no progress toward `95` is claimed from prose or structural evidence
alone.

## Changed files

- `engine/tests/test_skill_engine_tools.py` now derives the expected active and
  template counts from `tests/skill-quality-baseline.json`, then checks both
  the filesystem inventory and the routing catalogue against that control.
- `engine/tests/fixtures/tiny_project/fixture-manifest.json` labels the
  existing incomplete project as a synthetic negative fixture and records its
  expected non-zero validation contract.
- `engine/tests/test_negative_fixture_contract.py` proves the negative label,
  expected exit code, minimum blocking findings, and selected gate IDs.
- `engine/tests/fixtures/requirements_traceability/` is a synthetic positive
  behavioural fixture covering ambiguity resolution, acceptance criteria, test
  oracles, upward/downward traceability, and approved change control with
  rollback.
- `engine/tests/test_traceability_behavioural_fixture.py` runs the existing
  phase-02 semantics, traceability, test-oracle, and change-impact checks over
  that fixture.
- `PROJECT_BRIEF.md` distinguishes the current catalogue from the historical
  v3.3 `46`-skill snapshot and records the current phase model.
- `ARCHITECTURE.md` replaces the stale `01-08` linear-pipeline description with
  the current `00-meta-initialization` plus `01`-`09` phase model and links the
  count control.
- This report records the evidence, residual risk, and re-audit controls.

## Improvement register

### P0-03 — catalogue count drift and stale suite expectations

- Gap: two tests expected `156` while the filesystem and validator reported
  `157`; this made a valid catalogue addition appear to be a regression.
- Root cause: tests duplicated a literal instead of consuming the canonical
  baseline control and checking filesystem truth.
- Exact change: added `load_baseline()`, derived `expected_count` from
  `tests/skill-quality-baseline.json`, checked active `SKILL.md` files and the
  routing catalogue, and checked the template count.
- Hypothesis: deliberate catalogue additions will either require an explicit
  baseline update or fail visibly; accidental drift will not be hidden by a
  stale test literal.
- Owner: SRS repository maintainer.
- Measure: stale-count failures reduced from `2` to `0`; active filesystem
  count, catalogue count, and baseline control all equal `157`.
- Risk: a maintainer could change both catalogue and baseline without review.
  The validator comparison and diff review remain required controls.
- Rollback: revert the focused test-file change; the original stale failures
  return without changing repository skill content.
- Acceptance evidence: full pytest, skill validator, and routing smoke results
  below; `git diff --check` is clean.
- Standardisation: keep `tests/skill-quality-baseline.json` as the expected
  catalogue control and require validator plus filesystem-drift assertions for
  future catalogue changes.
- Re-audit: 2026-08-18.

### P0 negative-fixture classification

- Gap: `tiny_project` intentionally produced multiple HIGH findings, but the
  fixture did not state that the failure was expected.
- Root cause: the negative path existed only through fixture content and was
  not governed by a machine-readable classification or CLI assertion.
- Exact change: added `fixture-manifest.json` and a test that requires the
  `negative` and `synthetic-test-only` labels, exit code `1`, at least `3`
  HIGH findings, and three stable gate identifiers.
- Hypothesis: future maintainers will not mistake an intentional negative-path
  failure for a broken test or weaken the fixture to obtain a pass.
- Owner: SRS repository maintainer.
- Measure: before classification was absent; after the manifest and test pass,
  the direct fixture validation still exits `1` and observed `28` HIGH lines.
- Risk: gate identifiers may change with intentional validator redesign.
  Update the manifest only after observing the changed failure and reviewing
  the fixture's purpose.
- Rollback: remove only the manifest and test if the fixture is retired; do not
  make the incomplete project pass merely to satisfy a positive-path gate.
- Acceptance evidence: `test_negative_fixture_contract.py` passes and the
  direct CLI result remains a documented expected failure below.
- Standardisation: all intentionally failing project fixtures should carry a
  classification manifest with expected exit semantics.
- Re-audit: 2026-08-18.

### P1 requirements traceability behaviour

- Gap: structural traceability tests existed, but no compact fixture joined
  ambiguity handling, acceptance evidence, and controlled change evidence.
- Root cause: the checks were tested in separate unit scenarios rather than a
  representative requirements slice.
- Exact change: added the synthetic `requirements_traceability` fixture and a
  test that runs existing phase-02 semantics, `TraceabilityCheck`,
  `TestOraclesCheck`, and `ChangeImpactCheck`.
- Hypothesis: a fresh agent can now observe one valid requirement slice whose
  wording is resolved, acceptance oracle is deterministic, links reach a goal
  and test, and an approved change has rollback evidence.
- Owner: SRS repository maintainer.
- Measure: the fixture test passes `5/5` targeted tests; no production gate
  implementation was changed.
- Risk: this is a small synthetic positive path and does not prove client-scale
  requirements quality or human acceptance.
- Rollback: remove the fixture and test together; existing gate tests remain.
- Acceptance evidence: targeted and full-suite commands below.
- Standardisation: retain the fixture under `engine/tests/fixtures` and extend
  it only when a recurring requirements defect has a deterministic oracle.
- Re-audit: 2026-08-25.

## Before and after measures

| Measure | Before | After | Evidence class |
| --- | --- | --- | --- |
| Active catalogue control | Tests expected `156`; filesystem reported `157` | Baseline, filesystem, and routing catalogue agree at `157` | Structural |
| Pytest | `224` passed, `2` skipped, `2` failed | `228` passed, `2` skipped, `0` failed | Behavioural/regression |
| Routing | `52/52`, top-3 precision `1.000` | `52/52`, top-3 precision `1.000` | Structural/behavioural routing |
| Skill contract validator | Pass with `157` active and `1` template | Same pass result | Structural |
| Tiny-project negative path | Multiple HIGH findings, unclassified | Exit `1`, observed `28` HIGH lines, manifest and assertion present | Behavioural failure path |
| Current catalogue documentation | `PROJECT_BRIEF.md` presented `46` as current | `157` current; `46` explicitly historical | Documentation |
| Architecture phase description | Stale `01-08` linear pipeline | `00` plus `01-09`, with Phase 02 tracks | Documentation |

## Commands and results

The plain entrypoint `python -m pytest -q` returned exit `4` before the suite
ran because local pytest configuration requests the unavailable `pytest-cov`
plugin. The repository suite was therefore run with its configured addopts
disabled; this is an environment/configuration limitation, not a test pass.

| Command | Result | Exit |
| --- | --- | ---: |
| `python -m pytest -q -o addopts=` | `228 passed, 2 skipped` | `0` |
| `python -m pytest -q -o addopts= engine/tests/test_traceability_behavioural_fixture.py engine/tests/test_negative_fixture_contract.py engine/tests/test_skill_engine_tools.py` | `5 passed` | `0` |
| `python -X utf8 scripts/validate_skill_engine.py --baseline tests/skill-quality-baseline.json` | `157` active, `1` template, no failure counts | `0` |
| `python -X utf8 scripts/routing_smoke_test.py` | `52/52`; top-3 precision `1.000`; threshold `1.000` | `0` |
| `python -X utf8 scripts/validate_engine.py` | `ENGINE CONTRACT: PASS` | `0` |
| `python -m engine doctor` | Python, Pandoc, package, and skills checks passed | `0` |
| `python -m engine validate-skills` | No legacy path references outside alias blocks | `0` |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | `0` findings | `0` |
| `python -m engine validate engine/tests/fixtures/tiny_project` | Expected `ENGINE CONTRACT: FAIL`; `28` HIGH lines observed | `1` |

## Evidence boundaries and NOT ASSESSED items

- Structural evidence is assessed by the catalogue, route, engine, doctor,
  path, and source-ingestion checks.
- Behavioural evidence is assessed by the deterministic fixture tests and the
  retained negative CLI path.
- Render evidence is **NOT ASSESSED**; this patch creates no PPTX, DOCX, PDF,
  or visual artefact.
- System and production evidence are **NOT ASSESSED**; no deployed service,
  client project, production requirements review, or external acceptance session
  was supplied.
- Human semantic acceptance of the synthetic requirement is **NOT ASSESSED**;
  the fixture proves machine checks and preserves the human-review boundary.
- Cross-model automatic instruction discovery is **NOT ASSESSED** in this run.

## Compatibility

- Claude: the existing `CLAUDE.md` remains the Claude-specific root protocol;
  no duplicated model-specific skill logic was added. Claude execution was not
  run here, so runtime discovery is **NOT ASSESSED**.
- Codex: the existing `AGENTS.md`, portable catalogue, and deterministic tests
  remain the repository-facing route. Codex-side file and test execution passed
  for this worker.
- Generic agent: the canonical fallback is explicit loading of `AGENTS.md`,
  `README.md`, the baseline, and the selected `SKILL.md`; universal automatic
  discovery is **NOT ASSESSED** and is not claimed.

## Remaining backlog and next wave

- P0: no unresolved P0 item remains within this assigned SRS repair scope.
  Portfolio P0 items for sibling repositories are outside this write scope.
- P1: add negative traceability cases for unresolved ambiguity and rejected
  change requests, then run a fresh-context review of the positive fixture.
- P1: add a small model-entry discovery smoke record for Claude, Codex, and a
  generic manual route; record unavailable runtime checks as NOT ASSESSED.
- P2: add a deterministic documentation-currentness check for current catalogue
  claims so stale counts are detected before manual review.
- P2: expand requirements fixtures only when a recurring defect has a named
  owner, deterministic oracle, rollback, and re-audit date.

The target of `95/100` remains an improvement target, not an achieved score.
The next independent review should re-run the gates above, inspect this diff,
exercise the negative and positive fixtures from a fresh context, and decide
whether any score dimension has enough evidence to move.

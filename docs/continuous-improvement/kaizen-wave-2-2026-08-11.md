# SRS Skills Kaizen Wave 2 Report

Date: 2026-08-11
Repository: `C:\wamp64\www\srs-skills`
Scope owner: SRS repository maintainer
Wave: 2, fresh-context bounded implementation
Write scope: this repository only

## Outcome

Wave 1 was re-audited from the current working tree before any edit. Its count
repair removed stale literal expectations, but the new test still compared only
the number of active entrypoints. A same-count replacement could therefore pass
if the baseline count was changed with it. The Wave 2 control now compares the
complete relative `SKILL.md` path inventory in addition to the count. The
negative control proves that a different path is rejected even when the measured
and expected counts are equal.

The Wave 1 negative fixture was also stronger than its test contract. Its report
recorded `28` HIGH findings, while the manifest required only a minimum of `3`.
Wave 2 requires the observed count to remain exactly `28`, while retaining the
expected non-zero exit and selected gate checks ([fixture manifest](../../engine/tests/fixtures/tiny_project/fixture-manifest.json),
[negative-fixture test](../../engine/tests/test_negative_fixture_contract.py)).

The traceability fixture was challenged with unrelated goal and test identifiers,
an empty `requirement_trace`, and malformed change-impact YAML. The traceability
check now requires a known business-goal identifier on a line that names the
functional requirement, and a test-phase artefact with an explicit requirement
trace or requirement identifier plus a test-case identifier. Existing positive
behaviour remains green.

The local default pytest command remains unavailable because this environment
does not have `pytest-cov`. That is retained as an explicit exit `4`, not turned
into a pass. The repository now places the `90` coverage threshold in the
default pytest configuration and documents the exact supported installation
command in [CONTRIBUTING.md](../../CONTRIBUTING.md). A coverage-enabled pass is
still **NOT ASSESSED** until the development extra is installed.

No commit, push, fetch, pull, reset, publish, sibling-repository edit, or
workspace-report edit was performed.

## Fresh re-audit findings and Wave 1 challenge

| Wave 1 assumption challenged | Malformed or independent check | Result |
| --- | --- | --- |
| A baseline count plus filesystem count prevents catalogue drift | The control was given one expected path and one different measured path while both counts remained `1` | The new baseline comparison reports both the missing approved path and the unexpected path; the negative control passes |
| A minimum HIGH threshold is sufficient for the intentional negative fixture | The manifest now requires the recorded `28` HIGH findings exactly | The direct fixture validation still exits `1`; the test rejects a count change |
| A positive traceability line proves a meaningful trace | A copied fixture was mutated to remove the goal link; a second case supplied unrelated `BG-999` and `TC-999` text | The traceability gate reports the missing upward and downward links |
| A valid positive test case remains valid when its frontmatter trace is empty | `requirement_trace` was changed to an empty list in a temporary fixture copy | The oracle check and traceability check both block the malformed input |
| A change-control file is valid if its YAML shape is not exercised | The temporary fixture's change-impact file was truncated to `entries: [` | The change-impact check reports a schema/parse violation |
| A configured coverage gate is reproducible in every checkout | Default pytest was run without the optional development extra | Exit `4` is retained as an environment limitation; the exact install command is documented and coverage is not claimed |

The first three checks attack the Wave 1 residual risks recorded in the
[Wave 1 repository report](kaizen-wave-1-2026-08-11.md) and the ecosystem
[Wave 1 report](/C:/wamp64/www/KAIZEN-WAVE-1-REPORT.md). The temporary mutation
fixtures are synthetic and are not presented as client evidence.

## Exact Wave 2 files

Wave 1 files were preserved. The Wave 2 implementation changed or added only
these repository-local files:

- `scripts/validate_skill_engine.py`
- `tests/skill-quality-baseline.json`
- `engine/tests/test_skill_engine_tools.py`
- `engine/tests/fixtures/tiny_project/fixture-manifest.json`
- `engine/tests/test_negative_fixture_contract.py`
- `engine/checks/traceability.py`
- `engine/tests/test_check_traceability.py`
- `engine/tests/test_traceability_behavioural_fixture.py`
- `pyproject.toml`
- `CONTRIBUTING.md`
- `docs/continuous-improvement/kaizen-wave-2-2026-08-11.md`

The existing Wave 1 changes in `ARCHITECTURE.md`, `PROJECT_BRIEF.md`, and the
Wave 1 fixture files were not rewritten.

## Wave 2 improvement register

### W2-P1-01: explicit active-skill path inventory

- Gap: Wave 1 derived the expected active-skill count from the baseline, but a
  simultaneous count and catalogue change could hide unauthorized growth.
- Root cause: the control represented catalogue membership as a scalar count,
  not as an explicit reviewed set of filesystem paths.
- Change: `tests/skill-quality-baseline.json` now records all `157` active
  entrypoint paths; `scripts/validate_skill_engine.py` exposes stable inventory
  functions and reports missing/unexpected paths; the engine test checks the
  path set and a same-count/different-path negative control.
- Hypothesis: accidental additions, removals, or replacement paths will fail
  visibly even when a stale or altered count happens to match.
- Owner: SRS repository maintainer.
- Measure: the active count, path inventory, routing catalogue, and template
  count agree in the validator and tests. The independent negative control
  produces a path mismatch with equal counts.
- Risk: an approved catalogue addition requires a deliberate baseline inventory
  review. A path list increases review volume compared with one number.
- Rollback: revert the validator, baseline inventory, and focused tests together;
  do not restore a literal count-only assertion.
- Acceptance: `python -X utf8 scripts/validate_skill_engine.py --baseline
  tests/skill-quality-baseline.json` exits `0`; the focused inventory tests pass;
  routing remains `52/52` with top-three precision `1.000` (observed command
  evidence below; the fixture control is [routing-fixtures.json](../../tests/routing-fixtures.json)).
- Standardisation: future catalogue changes must update the explicit path
  control and survive the validator, routing smoke test, and diff review.
- Re-audit: 2026-08-25.

### W2-P1-02: exact intentional negative-fixture contract

- Gap: the Wave 1 negative test required only `3` HIGH findings even though the
  recorded fixture result contained `28`.
- Root cause: the manifest captured a lower bound, so weakening or accidentally
  changing the fixture could remain green.
- Change: `engine/tests/fixtures/tiny_project/fixture-manifest.json` records
  `expected_high_findings: 28`; `engine/tests/test_negative_fixture_contract.py`
  asserts exact count, expected exit `1`, synthetic classification, and stable
  gate identifiers.
- Hypothesis: the intentionally incomplete fixture will remain a visible,
  deterministic failure rather than becoming a weaker proxy for failure-path
  coverage.
- Owner: SRS repository maintainer.
- Measure: direct validation observes `28` HIGH findings and exit `1`; the
  positive test suite does not treat that expected exit as a failed test.
- Risk: a deliberate validator change may alter the count or gate identifiers.
  That change must be reviewed against fixture purpose before updating the
  manifest.
- Rollback: remove only the manifest assertion and fixture contract if the
  synthetic fixture is retired; never make the incomplete workspace pass to
  satisfy a positive gate.
- Acceptance: targeted test passes; direct `python -m engine validate
  engine/tests/fixtures/tiny_project` exits `1` with exactly `28` HIGH findings.
- Standardisation: every intentional negative fixture must declare its data
  classification, expected exit, expected finding count or bounded count, and
  stable failure identifiers.
- Re-audit: 2026-08-25.

### W2-P1-03: malformed traceability and change-control tests

- Gap: the prior traceability regex could accept unrelated identifiers when
  they appeared on the same line, and the positive fixture had no malformed
  mutation cases.
- Root cause: traceability was checked against concatenated document text
  instead of requirement-level upward links and test-phase downward evidence.
- Change: `engine/checks/traceability.py` uses line-level known-goal matching and
  test-phase artefact evidence; `engine/tests/test_check_traceability.py` adds an
  unrelated-ID regression case; `engine/tests/test_traceability_behavioural_fixture.py`
  adds temporary malformed-input checks for the requirement link, test trace,
  and change-impact YAML.
- Hypothesis: fabricated adjacency, empty test traces, and malformed change
  records will be blocked while the existing positive fixture continues to
  demonstrate resolved ambiguity, acceptance evidence, and controlled change.
- Owner: SRS repository maintainer.
- Measure: the Wave 2 targeted group passes `13` tests; the malformed cases
  assert the intended gate messages rather than only a non-zero result.
- Risk: stricter association can expose older workspaces that relied on free
  text or requirement-line test IDs without test-phase evidence. That is a
  useful compatibility signal, but it may require explicit migration guidance.
- Rollback: revert the parser change while retaining the malformed regression
  tests as a documented blocker; do not remove the tests to restore a pass.
- Acceptance: `python -m pytest -q -o addopts= engine/tests/test_skill_engine_tools.py
  engine/tests/test_check_traceability.py engine/tests/test_traceability_behavioural_fixture.py
  engine/tests/test_negative_fixture_contract.py` exits `0`.
- Standardisation: traceability fixtures must include one positive chain and
  negative mutations for unresolved links, empty test traces, and malformed
  change-control evidence.
- Re-audit: 2026-08-25.

### W2-P1-04: reproducible coverage configuration

- Gap: `pyproject.toml` enabled `pytest-cov` addopts, but a checkout without the
  optional development extra failed before collection with exit `4`.
- Root cause: the coverage plugin is intentionally a development dependency,
  while the setup and contributor paths did not state that the default pytest
  command depends on installing that extra.
- Change: `pyproject.toml` keeps coverage enabled and adds
  `--cov-fail-under=90`; `CONTRIBUTING.md` documents the exact supported
  `python -m pip install -e ".[dev]"` command and says that a coverage pass must
  not be claimed when installation is unavailable.
- Hypothesis: a fresh maintainer can reproduce the configured release test after
  one explicit dependency step, while coverage policy remains a blocking gate.
- Owner: SRS repository maintainer.
- Measure: the configuration test confirms `pytest-cov`, `--cov=engine`, and
  `--cov-fail-under=90`; the local default command still exits `4` without the
  plugin, which is recorded as **NOT ASSESSED** rather than hidden.
- Risk: once installed, the threshold may reveal actual coverage below `90` and
  block the suite. That is the intended signal, not a reason to remove the
  threshold.
- Rollback: revert only the configuration/documentation change after an
  approved policy decision; retain the existing CI coverage command and do not
  replace it with a logic-only pass.
- Acceptance: the exact installation command is discoverable in
  `CONTRIBUTING.md`; no local coverage-enabled pass is claimed until the
  dependency is installed.
- Standardisation: the dev extra remains the supported source of test tooling;
  default pytest and CI must retain the coverage threshold.
- Re-audit: 2026-08-25.

## Before, Wave 1, and Wave 2 measures

| Measure | Before Wave 1 | Wave 1 | Wave 2 |
| --- | --- | --- | --- |
| Active catalogue control | Tests expected `156` while the filesystem contained `157` ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)) | Count, filesystem, and routing catalogue agreed at `157` ([Wave 1 report](/C:/wamp64/www/KAIZEN-WAVE-1-REPORT.md)) | The baseline contains an explicit `157`-path inventory and the validator rejects same-count path replacement ([baseline](../../tests/skill-quality-baseline.json), [inventory tests](../../engine/tests/test_skill_engine_tools.py)) |
| Pytest | `224` passed, `2` skipped, `2` failed on stale count assertions ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)) | `228` passed, `2` skipped, `0` unexplained failures with coverage addopts disabled ([Wave 1 report](/C:/wamp64/www/KAIZEN-WAVE-1-REPORT.md)) | `234` passed, `2` skipped, `0` failures with `-o addopts=`; configured default remains exit `4` locally because `pytest-cov` is absent (command evidence below) |
| Negative fixture | `tiny_project` was unclassified; `28` HIGH findings were observed ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)) | Manifest required a non-zero exit, at least `3` HIGH findings, and selected gate IDs ([Wave 1 repository report](kaizen-wave-1-2026-08-11.md)) | Manifest and test require exactly `28` HIGH findings and exit `1` ([fixture manifest](../../engine/tests/fixtures/tiny_project/fixture-manifest.json), [test](../../engine/tests/test_negative_fixture_contract.py)) |
| Traceability behaviour | Existing unit checks had no compact malformed-input challenge ([initial assessment](/C:/wamp64/www/KAIZEN-INITIAL-ASSESSMENT.md)) | One positive synthetic fixture covered ambiguity, acceptance, and controlled change ([Wave 1 repository report](kaizen-wave-1-2026-08-11.md)) | `13` targeted tests cover positive behaviour, unrelated IDs, empty traces, missing goal links, and malformed change-impact YAML ([targeted tests](../../engine/tests/test_traceability_behavioural_fixture.py)) |
| Coverage policy | The development extra listed `pytest-cov`, but local default availability was not established | Default pytest exited `4` on the unavailable plugin; override suite was used and the limitation was documented ([Wave 1 repository report](kaizen-wave-1-2026-08-11.md)) | `pyproject.toml` now enforces the `90` threshold; installation is documented; coverage-enabled execution remains **NOT ASSESSED** ([pyproject.toml](../../pyproject.toml), [CONTRIBUTING.md](../../CONTRIBUTING.md)) |

The Wave 1 and Wave 2 test totals are command observations from this working
tree, not production or client acceptance evidence. The exercise publication cap
remains `55/100`; the Wave 1 diagnostic raw score of `76.0` is retained for
comparability, while a fresh raw re-score is **NOT ASSESSED** because this
bounded worker has no approved scoring recalculation record ([Wave 1 report](/C:/wamp64/www/KAIZEN-WAVE-1-REPORT.md)).

## Commands and exits

| Command | Result | Exit | Evidence state |
| --- | --- | ---: | --- |
| `python -m pytest -q` | Coverage arguments were rejected because `pytest-cov` is not installed | `4` | **NOT ASSESSED**; no coverage pass claimed |
| `python -m pytest -q -o addopts=` | `234` passed, `2` skipped | `0` | Behavioural/regression evidence without coverage |
| Targeted Wave 2 pytest command listed in W2-P1-03 | `13` passed | `0` | Targeted behavioural evidence |
| `python -m engine validate engine/tests/fixtures/tiny_project` | `ENGINE CONTRACT: FAIL`, exactly `28` HIGH findings, expected negative path | `1` | Expected negative evidence, not a suite failure |
| `python -X utf8 scripts/validate_skill_engine.py --baseline tests/skill-quality-baseline.json` | `157` active skills, `1` template, zero failure counts | `0` | Structural evidence |
| `python -X utf8 scripts/routing_smoke_test.py` | `52/52` fixtures, top-three precision `1.000`, threshold `1.000` | `0` | Routing evidence |
| `python -X utf8 scripts/validate_engine.py` | `ENGINE CONTRACT: PASS` | `0` | Structural/kernel evidence |
| `python -m engine validate-skills` | No legacy path references outside alias blocks | `0` | Pathing evidence |
| `python -m engine doctor` | All reported environment checks passed | `0` | Environment/doctor evidence |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | `0` findings | `0` | Source-ingestion safety evidence |
| `git diff --check` | No whitespace errors | `0` | Diff hygiene evidence |

The coverage-enabled command is supported after:

```powershell
python -m pip install -e ".[dev]"
python -m pytest -q
```

That installation was not performed by this auditor. Coverage remains
**NOT ASSESSED** until the command is run in an environment with the optional
development dependency installed.

## Safety and anti-slop review

### Safety

Safety status: **Safe** for the changed surfaces reviewed.

Inspected surfaces were `scripts/validate_skill_engine.py`,
`engine/checks/traceability.py`, the changed tests and fixtures,
`pyproject.toml`, `CONTRIBUTING.md`, and the new report. The only subprocess
call in a changed test invokes the repository's own Python module against a
local synthetic fixture. No changed instruction or script adds a remote
installer, network call, credential request, secret collection, external upload,
privileged operation, or destructive filesystem command. The source-ingestion
guardrail returned `0` findings.

### Anti-slop

Anti-slop status: **Pass for this bounded artefact review**, with the explicit
coverage limitation retained. The report uses repository-local evidence and
prior dated reports for numeric claims, adds no current external standard claim,
and does not present synthetic fixtures as client outcomes. Unexecuted coverage,
render, system, production, human-acceptance, and vendor-runtime checks remain
visible as **NOT ASSESSED**. No direct external quote was added.

## Portability status

| Agent path | Status | Evidence and limit |
| --- | --- | --- |
| Claude | **NOT ASSESSED** at runtime | The existing [CLAUDE.md](../../CLAUDE.md) remains the vendor-specific controller; no Claude runtime was available to execute discovery. No canonical logic was moved into it. |
| Codex | Passed for local repository execution | Codex-side filesystem, Python tests, validator, routing, doctor, and source guardrail commands passed where their dependencies were available. |
| Generic agent | Explicit manual route available; automatic discovery **NOT ASSESSED** | Load `AGENTS.md`, the baseline, the selected `SKILL.md`, and [CONTRIBUTING.md](../../CONTRIBUTING.md). No universal automatic instruction discovery is claimed ([standards register](/C:/wamp64/www/KAIZEN-STANDARDS-SOURCE-REGISTER.md)). |

The canonical contract remains model-neutral in the baseline, validator, engine
check, fixtures, and tests. Vendor-specific execution remains a thin controller
concern.

## Residual P0, P1, P2, and NOT ASSESSED states

### P0

- No new P0 defect remains in the assigned Wave 2 implementation scope after
  the path-inventory, exact-negative-count, and malformed-traceability controls
  passed.
- The `28` HIGH findings are an intentional negative-fixture result, not a
  cleared requirement defect or a positive release gate.

### P1

- Coverage-enabled full pytest remains **NOT ASSESSED** until `pytest-cov` is
  installed with the documented command.
- Semantic quality of real client requirements remains outside the synthetic
  fixture evidence.
- Baseline inventory updates still require maintainer review. The new control
  makes membership changes visible; it cannot determine organisational
  authorization by itself (inference).

### P2

- No current external standards were re-verified in this local test-mechanics
  change. The existing source register remains the applicable evidence record;
  mutable claims require their stated review cycle ([standards register](/C:/wamp64/www/KAIZEN-STANDARDS-SOURCE-REGISTER.md)).
- Broader catalogue quality, retrieval cost, client-scale requirements, and
  long-term defect trends were not remeasured.

### NOT ASSESSED

- Coverage-enabled pytest and numeric coverage percentage.
- Native DOCX, PDF, or PPTX render evidence.
- Linux/system execution, deployed service behaviour, and production outcomes.
- Human semantic acceptance of the synthetic requirement slice.
- Live Claude discovery and vendor-runtime behaviour.
- Client or external acceptance of SRS deliverables.

## Re-audit decision

The Wave 2 changes are accepted for this bounded repository scope because the
new negative controls fail for the intended malformed reasons, the positive
fixture and full logic suite remain green, the expected negative exit remains
visible, and structural gates retain their prior results. The repository remains
at maturity Level 3 for this exercise: measured local contracts exist, but
render, system, production, human, and coverage-enabled evidence is incomplete
(synthesis from the retained Wave 1 evidence and this audit).

Next re-audit: 2026-08-25. Re-run the documented development installation and
coverage-enabled suite, inspect any baseline path change, repeat the malformed
fixtures from a fresh context, and keep every unavailable stage explicitly
**NOT ASSESSED**.

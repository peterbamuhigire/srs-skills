# AI Test Strategy Addendum

When the system under test includes AI features, the test strategy MUST include the following test layers in addition to the generic ones.

## New test layers

| Layer | Purpose | Skill |
|-------|---------|-------|
| Eval harness | functional gate for AI features | `05-testing-documentation/04-ai-eval-harness-spec` |
| Red-team | security gate for AI features | `05-testing-documentation/05-ai-red-team-test-plan` |
| Hallucination SLI monitoring | production gate | `06-deployment-operations/10-ai-hallucination-slo-doc` |
| Cost regression | production gate | `06-deployment-operations/12-ai-cost-runbook` |

## What the eval harness replaces

- It does NOT replace unit tests. The deterministic glue around the AI call (parser, sanitiser, tenant-claim builder, retrieval scoping) still has unit tests.
- It does NOT replace integration tests of non-AI components.
- It DOES replace assertion-on-exact-output tests for AI behaviour. Such tests are forbidden as primary acceptance because outputs are distributional.

## Required test artefacts per AI feature

- Golden set with provenance and version (eval).
- Adversarial set (red-team).
- Judge-LLM rubric with calibration evidence.
- CI gate rule (regression threshold + safety zero-tolerance).
- Scheduled regression cadence.
- A/B prompt eval procedure.

## CI gate rules

A PR touching `prompts/`, `models/`, `retrieval-config/`, `post-processors/`, or `eval-sets/` MUST:

1. Run unit tests (must pass).
2. Run integration tests (must pass).
3. Run eval harness on affected features (regression <= 2 pp).
4. Run red-team smoke on affected features (0 CRITICAL, 0 HIGH).
5. Cost regression check (per-call cost within +20% of baseline).

## Production gate rules

Post-deploy, the hallucination SLO and cost dashboards take over. Burn-rate alerts and auto-rollback triggers replace human gating.

## Definition of "test pass" for AI features

"Tests pass" for AI features means:

- Deterministic glue tests green.
- Eval harness within regression tolerance.
- Red-team smoke green (0 CRITICAL/HIGH).
- Cost regression within tolerance.

Hand-graded human judgement is not a CI gate. Humans calibrate the judge-LLM; they do not gate every PR.

## Non-determinism handling

- For deterministic glue, run with temperature 0 in tests.
- For end-to-end AI behaviour, accept distributional pass/fail (e.g. 92/100 examples pass) with statistical bounds.
- Re-run flaky eval cases on a different judge or with a larger sample; do not silently lower thresholds.

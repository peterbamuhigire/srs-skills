<!-- Source basis: Designing for AI early release chapters 1-4; XP 2026 AI-augmented engineering and regression-testing papers. -->

# AI Evaluation Release Evidence

The eval harness must test the product system, not only text similarity.

| Dimension | Test evidence |
|---|---|
| Task outcome | Goldens, holdout, edge cases, multilingual/local and low-resource cases |
| Model/system boundary | Versioned model, prompt, retrieval, tools, policy and fallback |
| Human control | Preview, correction, contest, override, undo, escalation, consent/notice |
| Safety and fairness | Abuse, privacy, subgroup, accessibility and harmful-action cases |
| Operations | Cost, latency percentiles, availability, errors, drift and alert response |
| Release decision | Baseline comparison, guardrail result, owner, cohort, duration, rollback |

Refresh the dataset after incidents, user corrections, model changes, data
changes, or policy changes. Never use the same generated data for tuning and
final gating without a leakage check. A failed or unavailable test is retained
as `fail` or `not assessed`, never silently omitted.

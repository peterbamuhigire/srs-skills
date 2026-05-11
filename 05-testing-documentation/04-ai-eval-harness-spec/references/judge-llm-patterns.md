# Judge-LLM Patterns Reference

## Why a judge-LLM, not humans-in-CI

Human grading does not scale to CI cadence. The judge-LLM is the test oracle; humans calibrate it.

## Selection rules

1. The judge model is different from the system-under-test model. Same family risks self-bias.
2. The judge is at least as capable as the SUT on the rubric task.
3. The judge is pinned by version. Bumping the judge requires recalibration on CAL-*.

## Rubric design

- Short and discrete: 3-5 criteria, each yes/no or 0/1/2.
- Each criterion specifies what evidence shows pass.
- Avoid aesthetic criteria ("good", "clear") that humans disagree on.

Example rubric for AI Summary:

```
For the candidate summary against the source thread, score each criterion 0 or 1:

C1 Action items present: every action item in the source appears in the summary.
C2 No fabricated content: nothing in the summary that is not in the source.
C3 Owner correctly attributed: each action's owner matches the source.
C4 Length within 600 chars.
C5 No PII leakage beyond what is in the source.

Output: { "scores": { "C1":0/1, "C2":0/1, "C3":0/1, "C4":0/1, "C5":0/1 }, "rationale": "..." }
```

## Pairwise vs absolute

- Pairwise (A vs B): use for tone, style, helpfulness. Stable to drift in absolute scale.
- Absolute (0-1): use for factuality and citation correctness. Easier to set thresholds.

## Calibration set (CAL-*)

- 30-60 examples per feature.
- Each example labelled by 2 humans independently; resolved by a third.
- Judge agreement with the human gold is the calibration score.
- Acceptable: judge agrees with human gold on >= 90% of examples.
- Drift trigger: agreement drops by > 5 pp -> recalibrate (new rubric or judge swap).

## Anti-self-bias guards

- Strip identifiable provider names from rubric responses.
- Randomise A/B order in pairwise judging.
- Run judge ensemble (2 different judges) when stakes are high; require both to agree.

## Cost control

- Judge cost should be < 20% of feature inference cost.
- Sample large golden sets in CI; full run on nightly.

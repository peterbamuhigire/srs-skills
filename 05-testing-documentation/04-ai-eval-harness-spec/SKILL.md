---
name: "ai-eval-harness-spec"
description: "Generate the AI Eval Harness Spec: golden datasets per feature, regression criteria, A/B prompt eval, judge-LLM patterns, CI gate definition, scheduled regression, and the operational ownership of eval as a production system."
metadata:
  use_when: "Use for any AI feature in production or being prepared for production. Mandatory for every AI feature in the AI Feature PRD Spec."
  do_not_use_when: "Do not use for one-shot research prototypes with no commercial commitment."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Architecture_Spec.md, Prompt_And_System_Message_Spec.md, AI_Data_And_Knowledge_Base_Spec.md."
  workflow: "Inventory eval suites per feature, define golden and adversarial sets, define metrics and pass thresholds, define judge-LLM patterns, define CI gate and scheduled regression, define ownership and review cadence, write the spec."
  quality_standards: "Every AI feature shall have a golden set with a documented sampling provenance, a pass threshold, and a CI gate. Every metric shall have a numeric threshold and an alerting rule on drift."
  anti_patterns: "Do not use the eval set to train. Do not let any AI feature go to prod without an attached eval suite. Do not let humans hand-grade in CI; use a judge-LLM with calibration evidence."
  outputs: "AI_Eval_Harness_Spec.md and eval-set seed files."
  references: "Use references/ai-eval-harness-spec-template.md and references/judge-llm-patterns.md."
---

# AI Eval Harness Spec Skill

## Overview

The eval harness is to AI features what unit + integration + load tests are to deterministic software: the test layer the team owns and the CI runs. This skill produces the spec.

## Core Instructions

### Step 1: Inventory eval suites per AI feature

For every AI FR, declare:

- Golden set (success behaviour).
- Adversarial / red-team set (failure modes; cross-link to red-team plan).
- Judge-LLM rubric.
- Calibration set (held-out examples scored by humans to verify the judge).

### Step 2: Golden set construction

Provenance rule: golden examples come from production traffic snapshots, design-partner samples, or expert authorship. Each example is labelled by a named labeller. Class balance is documented. Sets are versioned.

For each example: input, expected output (or expected shape + acceptance rubric), category tag, locale, sensitivity flag.

### Step 3: Metrics and thresholds

Per feature, choose metrics from:

| Metric | Formula | Typical threshold |
|--------|---------|--------------------|
| Pass rate | passed / total | >= 90% |
| Factuality | judge-graded factual claims correct / total | >= 0.92 |
| Citation rate (RAG) | cited claims / claims | >= 0.90 |
| Citation accuracy | cited spans matching source / cited | >= 0.95 |
| Abstention precision | correct abstains / abstains | >= 0.80 |
| Abstention recall | correct abstains / should-abstain | >= 0.70 |
| Toxicity / safety violation rate | violations / total | 0 (zero-tolerance) |
| Latency P95 | telemetry | per AI FR clause |
| Cost / call | telemetry | per AI FR clause |

### Step 4: Judge-LLM patterns

The judge is a different model from the system under test. Rubric is short and discrete; pairwise judging beats absolute judging for noisy criteria. The judge is itself calibrated against human labels on a small set; drift in judge scoring triggers re-calibration.

### Step 5: CI gate

State the gate rule: a PR cannot merge if the regression on the affected feature's golden set drops > N percentage points (typical N = 2 pp) or if any toxicity / safety metric becomes non-zero.

### Step 6: Scheduled regression

Nightly golden run; weekly full red-team run. Score history is plotted; drops trigger SEV3.

### Step 7: A/B prompt eval

For prompt changes that pass CI, run side-by-side eval across both prompts on the golden + production-snapshot set; require the new prompt to win on the primary metric without regressing the safety metric.

### Step 8: Operational ownership

The eval harness is owned by the AI lead with a named back-up. Dataset versioning, judge model + version, and rubric versions are tracked. Eval-set changes go through PR with sign-off.

### Step 9: Write the spec

`AI_Eval_Harness_Spec.md` sections: 1) Per-feature Suite Inventory, 2) Golden Set Construction, 3) Metrics & Thresholds, 4) Judge-LLM Patterns, 5) CI Gate, 6) Scheduled Regression, 7) A/B Prompt Eval, 8) Operational Ownership, 9) Traceability.

## Standards

- OpenAI Evals
- promptfoo / Anthropic eval guide
- NIST AI RMF MEASURE
- ISO/IEC 42001 Clause 9 (performance evaluation)

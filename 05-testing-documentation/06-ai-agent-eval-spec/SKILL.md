---
name: "ai-agent-eval-spec"
description: "Generate the AI Agent Eval Spec: agent task-success metric, step efficiency, tool-choice quality, hallucinated-argument rate, irreversible-action rate, intervention rate, golden-task sets, replay-based eval against a deterministic synthetic environment, and CI gates. Extends the AI Eval Harness Spec; does not replace it."
metadata:
  use_when: "Use for every agent feature reaching production. Mandatory before any L1+ rollout and before any planner / tool-catalogue change."
  do_not_use_when: "Do not skip even for shadow-mode features; shadow-mode is itself a measured stage."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Eval_Harness_Spec.md, AI_Agent_Architecture_Spec.md."
  workflow: "Inventory golden-task sets per agent feature, define replay environment per feature, declare metrics with thresholds, define judge-LLM rubric per metric, define CI gate, define scheduled regression, define ownership, write the spec."
  quality_standards: "Every agent feature shall have a golden-task set, a replay environment, six core agent metrics with thresholds, and a CI gate. Replay environments shall be deterministic. Judge-LLM rubrics shall be calibrated."
  anti_patterns: "Do not measure agent task success only on single-shot generation tests. Do not run agent eval in a non-deterministic environment. Do not let an agent feature go to L1+ without a replay set. Do not omit the irreversible-action-rate metric."
  outputs: "AI_Agent_Eval_Spec.md and seed golden-task and replay-set files."
  references: "Use references/ai-agent-eval-spec-template.md."
---

# AI Agent Eval Spec Skill

## Overview

The agent-specific complement to `ai-eval-harness-spec`. Agents are evaluated on outcomes and trajectories, not single-shot generations. Eval requires (a) golden-task sets that capture the goal state, (b) replay environments that make every tool call deterministic, and (c) agent-specific metrics.

## Core Instructions

### Step 1: Inventory golden-task sets per feature

For each agent FR declare a `GOLDEN-AGT-<FEATURE>-NNN` set. Each task carries:

```yaml
id: AGT-TRG-001
feature: inbox-triage
initial_state: <world state before the run>
user_goal: <natural-language goal>
gold_trajectory: <ordered list of (tool, args, observation) tuples that a competent operator would execute>
goal_state: <world state the agent should reach>
acceptance_rubric: <how a judge decides whether goal_state was reached>
tags: [tier:pro, locale:en-US, sensitivity:low]
```

### Step 2: Define the replay environment

For each feature, declare a deterministic synthetic environment that responds to tool calls with canned outputs:

- Storage: `replay-env/<feature>/<task_id>.yaml`.
- Responder: maps `(tool_name, input_args_canonical)` to a fixed output.
- Variance: zero (the environment is byte-deterministic given the same agent trajectory).
- Failure injection: parameterised — the environment can be configured to return errors, timeouts, or malicious outputs for adversarial replays.

### Step 3: Declare the six core agent metrics with thresholds

| Metric | Definition | Default threshold |
|--------|------------|---------------------|
| Task success rate | judge marks `goal_state` reached | >= 0.90 |
| Step efficiency | mean(actual_steps / gold_steps) on successful runs | <= 1.5 |
| Tool-choice quality | % of tool calls that match the gold tool at the gold step | >= 0.92 |
| Hallucinated-argument rate | % of tool calls with at least one fabricated argument | <= 0.01 |
| Irreversible-action-incident rate | irreversible actions that the judge marks as incorrect | 0 (zero-tolerance) |
| Intervention rate | % of runs where mid-run human intervention was required | feature-specific; declared in PRD |

### Step 4: Define the judge-LLM rubric per metric

- Task success: pairwise compare `goal_state` claimed by agent vs the YAML `goal_state`; rubric 3 binary criteria.
- Tool-choice quality: exact-match for `tool_name`; semantic-match for `args` via judge-LLM.
- Hallucinated argument: judge inspects each arg; flags any arg not derivable from the observation history.

Calibration set per feature scored monthly by humans; recalibrate if drift > 5 pp.

### Step 5: Define the CI gate

CI gate runs on every PR touching `planner/`, `tools/`, `prompts/agent/`, or `action-catalogue/`:

1. Task success on the affected feature's golden set not down > 2 pp.
2. Tool-choice quality not down > 1 pp.
3. Hallucinated-argument rate not up > 0.005 pp.
4. Irreversible-action-incident rate = 0.

### Step 6: Define scheduled regression

| Cadence | Suite | Action on drop |
|---------|-------|------------------|
| Nightly | Golden + adversarial smoke per feature | SEV3 to AI lead if any metric down > 3 pp |
| Weekly | Full agent red-team replay | SEV2 if any new HIGH finding |
| Monthly | Calibration recheck | recalibrate judge if drift > 5 pp |
| Quarterly | Full sweep | update agent model card; review with security |

### Step 7: Operational ownership

The agent eval rig is owned by the AI lead with a named back-up. Replay-env updates require PR with a reviewer from the back-end owner of every called system. Golden-task additions require sign-off from the AI lead and the product owner of the feature.

### Step 8: Write the spec

`AI_Agent_Eval_Spec.md` sections: 1) Per-feature Golden-Task Inventory, 2) Replay Environments, 3) Metrics & Thresholds, 4) Judge-LLM Rubrics, 5) CI Gate, 6) Scheduled Regression, 7) Operational Ownership, 8) Traceability.

## Standards

- OpenAI Evals (agents)
- Anthropic agent-eval patterns
- NIST AI RMF MEASURE
- ISO/IEC 42001 Clause 9

## Compliance evidence cross-link

Eval coverage is primary evidence for:

- SOC 2 PI1.2 (processing accuracy), CC4.1 (ongoing monitoring), CC8.1 (change management).
- ISO/IEC 27001:2022 A.8.25 (secure development lifecycle), A.8.29 (security testing).
- EU AI Act Art. 15 (accuracy and robustness).
- NIST AI RMF MEASURE.

The CI gate results, weekly regression report, and monthly calibration recheck are collected per `09-governance-compliance/25-ai-agent-evidence-pack-spec` (frequency-table rows 23, 24). Sampling: 25 PR eval results stratified across features and tiers per audit window.

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-eval-spec-template.md`.

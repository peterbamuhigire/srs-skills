# Agent Eval Cross-Link

The AI Eval Harness Spec covers the golden-set rig for AI features in general. For agent features (L0..L4), the harness is augmented by the **AI Agent Eval Spec** (`05-testing-documentation/06-ai-agent-eval-spec`).

## Why agent eval needs more

The golden-set rig measures input → output for a single shot. Agent runs are *trajectories*, not single shots. Eval must measure:

- Task success rate (judge-LLM marks goal-state reached).
- Step efficiency (steps vs gold).
- Tool-choice quality (tool match at each step).
- Hallucinated-argument rate (args not derivable from observations).
- Irreversible-action-incident rate (zero-tolerance).
- Intervention rate.

## Replay environments

For agent features, golden-task examples are paired with deterministic replay environments under `replay-env/<feature>/`. The responder maps `(tool_name, input_args_canonical)` to a fixed output so the agent's trajectory is reproducible.

## CI gate alignment

The agent eval rig defines its own CI gate triggered by PRs to `planner/`, `tools/`, `prompts/agent/`, `action-catalogue/`. The generic eval harness CI gate continues to apply to non-agent paths.

## Judge calibration

The judge-LLM patterns from `judge-llm-patterns.md` apply; the agent eval rig adds tool-choice and hallucinated-arg judging rubrics with their own calibration sets.

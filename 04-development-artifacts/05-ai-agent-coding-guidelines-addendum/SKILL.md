---
name: "ai-agent-coding-guidelines-addendum"
description: "Generate the AI Agent Coding Guidelines Addendum: tool-schema discipline, irreversibility annotations, blast-radius caps, deterministic state, idempotency keys for tool calls, error and timeout policy, and the test contract for agent-runtime code."
metadata:
  use_when: "Use whenever a team is writing or modifying agent-runtime code, planner code, dispatcher code, tool wrappers, or HITL hook code. Addendum to the generic coding guidelines."
  do_not_use_when: "Do not use for non-agent code paths; cover those with the generic `coding-guidelines` skill."
  required_inputs: "Coding_Guidelines.md, AI_Agent_Architecture_Spec.md, Action_Catalogue_Spec.md."
  workflow: "Codify the tool-schema discipline, irreversibility annotation rule, blast-radius caps, deterministic-state rule, idempotency-key rule, error/timeout policy, and the test contract; write the addendum."
  quality_standards: "Every tool wrapper shall be schema-validated at the boundary. Every state mutation shall be deterministic given its inputs. Every tool call shall carry an idempotency key. Every irreversible tool call shall route through the HITL hook."
  anti_patterns: "Do not put untyped dicts on the planner/dispatcher boundary. Do not silently retry on tool errors that are not idempotent. Do not store agent run state in process memory only. Do not write tool wrappers without timeout."
  outputs: "Coding_Guidelines_Agent_Addendum.md."
  references: "Use references/ai-agent-coding-guidelines-addendum-template.md."
---

# AI Agent Coding Guidelines Addendum Skill

## Core Instructions

### Step 1: Codify tool-schema discipline

- Every tool wrapper validates inputs against the catalogue schema at the function boundary; the planner's free-form output is never trusted.
- Outputs from external systems are parsed against the declared output schema and rejected on mismatch.
- Schema validation libraries are pinned and CI-tested.

### Step 2: Codify irreversibility annotations

- Every tool function carries a decorator or attribute that names its `reversibility_class`.
- A static-analysis check fails CI if a tool function exists in the codebase without an irreversibility annotation.
- The dispatcher reads the annotation at runtime; mismatch between code annotation and catalogue YAML fails startup.

### Step 3: Codify blast-radius caps

- Every tool call inside a single agent run has a per-tool cap (e.g. `email.send` capped at 5 per run).
- Caps are enforced at the dispatcher; the planner does not enforce.
- Per-run caps are loaded from the action catalogue at run start.

### Step 4: Codify deterministic state

- Agent run state is `(plan, observations, scratchpad, cumulative_cost)`. State mutations are pure functions of `(previous_state, transition_event)`.
- No tool wrapper is allowed to mutate run state directly; it returns a `ToolResult` that the orchestrator applies to state.
- Replay = re-applying transitions to the initial state in order.

### Step 5: Codify idempotency keys

- Every tool call carries `idempotency_key = sha256(agent_run_id + ':' + step_index)`.
- Tool wrappers pass the key to the underlying API where supported.
- Retries reuse the same key. Different idempotency keys on retry are a bug.

### Step 6: Codify error and timeout policy

- Every tool wrapper has a default timeout from the catalogue YAML.
- Errors are classified `retryable | non-retryable | safety`.
- `retryable` errors back off (1s, 4s, 16s) with the same idempotency key.
- `non-retryable` errors fail the step; orchestrator decides whether to abstain or re-plan.
- `safety` errors (content-filter trip, kill-switch hit, schema fail) terminate the run; no retry.

### Step 7: Codify the test contract

- Every tool wrapper has unit tests against (a) happy path, (b) schema-fail input, (c) timeout, (d) non-retryable error, (e) safety error.
- Every planner change ships with an agent-eval rig run on the affected feature's golden-task set.
- Coverage on agent-runtime code: 90% line coverage; 100% on the dispatcher hot path.

### Step 8: Write the addendum

`Coding_Guidelines_Agent_Addendum.md` sections: 1) Tool-Schema Discipline, 2) Irreversibility Annotations, 3) Blast-Radius Caps, 4) Deterministic State, 5) Idempotency Keys, 6) Error & Timeout Policy, 7) Test Contract, 8) Static-Analysis & CI Hooks, 9) Style Examples.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- Anthropic agent-engineering patterns
- Google production-LLM playbooks
- IEEE 1016-2009 §5 (Design viewpoints)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-coding-guidelines-addendum-template.md`.

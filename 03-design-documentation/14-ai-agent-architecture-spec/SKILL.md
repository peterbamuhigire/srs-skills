---
name: "ai-agent-architecture-spec"
description: "Generate the AI Agent Architecture Spec: agent runtime loop, state machine, memory tiers (scratchpad, episodic, long-term), planner, tool dispatcher, supervisor (for multi-agent), durability and resumability, kill-switch wiring, and per-tenant isolation. Sits alongside the AI Architecture Spec and is mandatory for any product shipping an agent."
metadata:
  use_when: "Use whenever one or more features are classified as agents (L0..L4) in the AI Agent Strategy Doc. Required alongside the AI Architecture Spec."
  do_not_use_when: "Do not use for products that ship only direct-LLM or RAG features without tool-using planners."
  required_inputs: "AI_Architecture_Spec.md, AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, Multi_Tenancy_Architecture_Spec.md, tech_stack.md."
  workflow: "Read inputs, declare the agent runtime decomposition, spec the loop and state machine, spec memory tiers, spec the planner, spec the tool dispatcher with audit-log integration, spec the supervisor (if multi-agent), spec durability and resumability, spec kill-switch wiring, spec per-tenant isolation, emit ADR seeds, write AI_Agent_Architecture_Spec.md."
  quality_standards: "Every agent run shall have a durable state. Every tool call shall route through the dispatcher. The kill-switch shall halt every running agent within a documented bound. Per-tenant isolation shall be enforced at the planner, dispatcher, and memory layers."
  anti_patterns: "Do not let agent code call the model gateway directly without dispatcher mediation. Do not store scratchpads across tenants in a shared namespace. Do not omit the resumability contract. Do not omit the kill-switch wiring diagram."
  outputs: "AI_Agent_Architecture_Spec.md plus ADR seeds in `adr-seeds/`."
  references: "Use references/ai-agent-architecture-spec-template.md."
---

# AI Agent Architecture Spec Skill

## Overview

The agent-distinctive architecture artefact. Sits alongside the AI Architecture Spec and the multi-tenancy spec. Captures the runtime loop, the state machine, the memory tiers, the planner, the dispatcher (the gate that enforces the action catalogue, the audit log, the rate limits, and the kill-switch), the supervisor (for multi-agent topologies), and the per-tenant isolation contract.

## Core Instructions

### Step 1: Read context

Read the AI architecture spec, the agent feature PRD, the action catalogue, the multi-tenancy spec. Identify in-scope agent features, autonomy levels, and the action catalogue scope per feature.

### Step 2: Declare the agent runtime decomposition

The agent runtime sits inside the AI plane and contains:

- **Agent Orchestrator** — the per-run controller that hosts the loop and state machine.
- **Planner** — the LLM call(s) that produce or revise the plan.
- **Tool Dispatcher** — single point of egress for every tool call; consults the action catalogue, enforces rate limits, applies kill-switch, emits the audit-log event, and gates irreversible actions through the HITL hook.
- **Memory Tiers** — scratchpad (per-run, ephemeral), episodic (per-user / per-tenant, time-windowed), long-term (per-tenant, opted-in only).
- **Supervisor** (optional, multi-agent only) — coordinates worker agents.
- **Durable State Store** — agent-run-state at every step for resumability.
- **HITL Hook** — the bridge to the human-approval UI and the inbox of approver-role queues.
- **Audit Log Pipeline** — append-only sink for every tool call event.
- **Kill-switch Controller** — operator surface; flips global, per-tenant, or per-feature switches; propagates to all dispatchers within the SLA.

Diagram in Mermaid; place every service.

### Step 3: Spec the loop and state machine

Standard loop: `observe → plan → act → observe → ...` until terminal state. State machine states: `pending`, `planning`, `awaiting-approval`, `executing-tool`, `awaiting-tool-result`, `intervened`, `aborted`, `completed-success`, `completed-abstain`, `completed-failed`. Define transitions and the durability point at every transition.

### Step 4: Spec memory tiers

For each tier:

- **Scratchpad** — in-process; lifespan = agent run; isolation key = `(tenant_id, agent_run_id)`; never crosses run boundaries.
- **Episodic** — durable; lifespan = TTL (e.g. 30 d); isolation key = `(tenant_id, user_id)`; access requires tenant claim.
- **Long-term** — durable; lifespan = unbounded; isolation key = `(tenant_id)`; access requires both the tenant claim and the per-tenant opt-in flag.

State the encryption posture, key management, and the redaction rule at write time.

### Step 5: Spec the planner

State whether the planner is `ReAct`, `Plan-and-execute`, `Tree-of-thought`, `Function-calling-loop`, or custom. State the prompt template source (prompt registry). State the budget hooks — the planner shall halt when max-step or max-cost is reached. State the abstain payload — the planner emits a structured abstain when no plan satisfies the policy envelope.

### Step 6: Spec the tool dispatcher

The dispatcher is the gate. For every tool call:

1. Look up tool in the action catalogue; refuse if absent.
2. Validate input against the tool schema; refuse on schema failure.
3. Re-validate tenant claim and tier availability.
4. Consult kill-switch state (global, per-tenant, per-feature); refuse with the configured message.
5. Consult rate-limit class; throttle if exhausted.
6. If reversibility=irreversible or above-threshold, invoke the HITL hook and block until approved or timed-out.
7. Execute the underlying API call.
8. Sanitise tool output (strip embedded instructions; truncate; redact PII).
9. Emit the audit-log event.
10. Return the sanitised output to the orchestrator.

### Step 7: Spec the supervisor (multi-agent only)

If multi-agent, cross-link to `15-ai-agent-multi-agent-coordination-spec` and place the supervisor in the diagram. State the supervision policy (review-before-act / review-after-act / sample-review).

### Step 8: Spec durability and resumability

The orchestrator persists state at every transition. After a process crash or planned restart, the orchestrator shall resume in-flight runs from the last durable state. State the storage technology, the serialisation format, and the resume SLA (e.g. < 30 s after restart). State the idempotency contract — every tool call carries an idempotency key derived from `(agent_run_id, step_index)`.

### Step 9: Spec kill-switch wiring

State the kill-switch surface (operator API + ops console UI). State the propagation SLA — global kill-switch shall halt every dispatcher within 5 seconds. State the rehearsal cadence — kill-switch is rehearsed monthly in staging.

### Step 10: Spec per-tenant isolation

State the enforcement points: planner (no cross-tenant retrieval), dispatcher (tenant claim re-validated per call), memory tiers (isolation keys above), audit log (per-tenant partitioning).

### Step 11: Emit ADR seeds

ADR seeds: planner choice per feature, memory store technology, durable state store, supervisor topology, kill-switch propagation SLA, irreversibility-gating policy, tool-call audit log retention.

### Step 12: Write the spec

`AI_Agent_Architecture_Spec.md` sections: 1) Agent Runtime Diagram, 2) Loop & State Machine, 3) Memory Tiers, 4) Planner, 5) Tool Dispatcher, 6) Supervisor (if applicable), 7) Durability & Resumability, 8) Kill-switch Wiring, 9) Per-Tenant Isolation, 10) ADR Seed Index, 11) Traceability.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- NIST AI RMF MAP / MEASURE / MANAGE
- ISO/IEC 42001 Clause 8
- AWS Well-Architected ML/AI Lens

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-architecture-spec-template.md`.

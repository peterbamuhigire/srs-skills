---
name: "ai-agent-multi-agent-coordination-spec"
description: "Generate the Multi-Agent Coordination Spec: topology choice (single-agent / supervisor-worker / debate / handoff chain), scratchpad isolation between agents, supervision policy, message-bus contract, and failure-mode handling specific to multi-agent systems."
metadata:
  use_when: "Use when more than one agent participates in a single user task: supervisor-worker, debate, handoff chains, or any topology where one agent's output feeds another agent's plan."
  do_not_use_when: "Do not use for single-agent features. Cover those with `ai-agent-architecture-spec` only."
  required_inputs: "AI_Agent_Architecture_Spec.md, AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md."
  workflow: "Declare the topology, declare the agent inventory and roles, declare the scratchpad isolation rule, declare the supervision policy, declare the message-bus contract, declare failure-mode handling, write the Multi_Agent_Coordination_Spec.md."
  quality_standards: "Every multi-agent feature shall declare exactly one topology. Every agent role shall have a bounded action-catalogue subset. Scratchpads shall not be shared across agent roles unless the topology explicitly declares the sharing rule. The supervisor shall be the sole authority for handoff."
  anti_patterns: "Do not allow worker agents to spawn sub-agents without supervisor approval. Do not share scratchpads across agents that have different policy envelopes. Do not run an unbounded debate; cap rounds."
  outputs: "Multi_Agent_Coordination_Spec.md."
  references: "Use references/ai-agent-multi-agent-coordination-spec-template.md."
---

# AI Agent Multi-Agent Coordination Spec Skill

## Core Instructions

### Step 1: Declare the topology

Pick exactly one per feature:

| Topology | When | Trade-off |
|----------|------|-----------|
| Single-agent | task fits one role | simplest; least observability cost |
| Supervisor-worker | task decomposes into specialist sub-tasks | strong observability; supervisor is the bottleneck and the source of policy |
| Debate (N-agent) | task benefits from adversarial cross-check | improves factuality; cost scales with N and rounds |
| Handoff chain | sequential phases (retrieve → draft → verify) | clear ownership; brittle to mid-chain failure |

### Step 2: Declare the agent inventory and roles

Per agent role, declare:

- Role name.
- Bounded action-catalogue subset (the role may not call tools outside this subset).
- Memory access (which tiers, which keys).
- Planner template.
- Termination criteria for the role.

### Step 3: Declare the scratchpad isolation rule

Default: each agent role has its own scratchpad keyed by `(tenant_id, agent_run_id, agent_role)`. Cross-role sharing is permitted only via explicit handoff messages on the message bus, not via shared memory.

### Step 4: Declare the supervision policy

For supervisor-worker:

- **Review-before-act** — supervisor approves every worker plan before any tool execution.
- **Review-after-act** — supervisor reviews after each worker step.
- **Sample-review** — supervisor samples N% of worker outputs.

State which policy applies at which autonomy level. Irreversible tools always require review-before-act regardless of overall policy.

### Step 5: Declare the message-bus contract

Inter-agent messages carry: `from_role`, `to_role`, `agent_run_id`, `payload_schema`, `handoff_token`. The supervisor is the sole authority that issues `handoff_token`. Messages without a valid token are refused.

### Step 6: Declare failure-mode handling

| Failure | Handling |
|---------|----------|
| Worker exceeds budget | supervisor aborts the worker; the run continues with reduced scope or terminates |
| Worker emits malformed handoff | supervisor rejects; one retry; then abort |
| Debate fails to converge in N rounds | terminate; emit abstain payload |
| Supervisor crashes | orchestrator re-elects supervisor from the durable state |
| Worker proposes irreversible tool without approval | dispatcher refuses; supervisor reviews; the worker is paused |

### Step 7: Write the spec

`Multi_Agent_Coordination_Spec.md` sections: 1) Topology Verdict, 2) Agent Inventory & Roles, 3) Scratchpad Isolation, 4) Supervision Policy, 5) Message-Bus Contract, 6) Failure-Mode Handling, 7) ADR Seeds, 8) Traceability.

## Standards

- OWASP LLM Top 10 (agentic addendum)
- Anthropic agent-engineering patterns
- AutoGen / CrewAI post-mortems
- ISO/IEC 42001 Clause 8

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-multi-agent-coordination-spec-template.md`.

# Agent Runtime Cross-Link

When the feature-to-pattern map in the AI Architecture Spec includes any `Agent` row, the AI Architecture Spec is incomplete on its own. The product MUST also produce the **AI Agent Architecture Spec** (`03-design-documentation/14-ai-agent-architecture-spec`).

## What the agent runtime spec adds

The AI Architecture Spec covers the AI plane: model gateway, vector store, prompt registry, eval harness, observability bus, security boundaries. It does **not** specify:

- The agent runtime loop and state machine.
- Memory tiers (scratchpad / episodic / long-term).
- The planner pattern and budget hooks.
- The tool dispatcher (which is the single egress for every tool call, distinct from the model gateway).
- The supervisor for multi-agent topologies.
- Durability and resumability for agent runs.
- Kill-switch wiring and propagation SLA.

These are the responsibility of the agent architecture spec.

## Feature-to-pattern row template for agent features

| Feature | Pattern | Drivers | Rejected alternatives | Cross-link |
|---------|---------|---------|------------------------|--------------|
| Inbox Triage | agent (L2) | multi-step, tool-using | direct (no tool surface), RAG (no action surface) | `14-ai-agent-architecture-spec` |

## Dispatcher vs Model Gateway

The Model Gateway is the single egress for **model-provider calls**.
The Tool Dispatcher is the single egress for **tool calls**.

These are different services. The dispatcher consults the catalogue, the kill-switch, the rate limits, and the HITL hook. The gateway consults the prompt registry, the content filter, the cost meter, and the fallback router. In the agent runtime, the orchestrator uses both.

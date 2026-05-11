# Agent ADR Slots Cross-Link

The AI ADR Catalogue covers 17 required ADR slots for AI-feature SaaS. When the product ships agent features, the **AI Agent ADR Catalogue** (`09-governance-compliance/19-ai-agent-adr-catalogue`) is the canonical home for the 14 agent-specific ADR slots.

## Agent ADR slots (canonical home: `19-ai-agent-adr-catalogue`)

1. Autonomy Level per Feature
2. Irreversibility-gating Policy
3. Planner Choice per Feature
4. Memory Store Technology and Tiering
5. Tool-call Audit-log Retention by Event Class
6. Multi-agent Topology per Feature
7. Supervision Policy
8. Kill-switch Propagation SLA
9. Action Catalogue Change-control Protocol
10. Replay Environment Source-of-truth
11. Agent-task Quarantine Policy
12. Agent Cost Envelope per Feature
13. Plan-approval UI Authority
14. Long-term Memory Opt-in Mechanism

## Relationship to AI ADR slots

The AI ADR catalogue retains its 17 slots. The agent ADR catalogue is a *separate* register that an agent-feature SaaS additionally maintains. The central `09-governance-compliance/05-architecture-decision-records` register indexes both.

## Where agent decisions overlap AI decisions

- ADR-AI-001 (Model Gateway as Sole Egress) remains in the AI register. The dispatcher is the *tool-call* analogue; it sits in the agent register as part of the architecture spec, not as a standalone ADR (unless deviation from the spec is proposed).
- ADR-AI-013 (Cross-Tenant Retrieval Prohibition) extends in the agent register via ADR-AGT (cross-tenant tool routing prohibition + enforcement at the dispatcher).
- ADR-AI-011 (Conversation Log Retention) and ADR-AGT-005 (Tool-call Audit-log Retention) are distinct but adjacent; both required.

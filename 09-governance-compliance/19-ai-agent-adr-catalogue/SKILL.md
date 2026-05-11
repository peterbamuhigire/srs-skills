---
name: "ai-agent-adr-catalogue"
description: "Generate the AI Agent ADR Catalogue: the required architecture decision records for an agent-feature SaaS — autonomy level per feature, irreversibility-gating policy, planner choice, memory store, tool-call audit-log retention, multi-agent topology, supervision policy, kill-switch SLA, and the agent change-control protocol."
metadata:
  use_when: "Use as soon as the AI Agent Architecture Spec is drafted. Each agent feature shipping to production shall have its ADR catalogue completed."
  do_not_use_when: "Do not use for projects without agent features."
  required_inputs: "AI_Agent_Architecture_Spec.md, AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_SLO_Doc.md, AI_Agent_Responsible_AI_Addendum.md."
  workflow: "Inventory required agent ADR slots, fill each ADR with context / decision / consequences / alternatives / evidence, index them in the agent ADR register, link to the central ADR catalogue and the AI ADR catalogue, write the catalogue doc."
  quality_standards: "Every required agent ADR slot shall be filled or explicitly waived with an ADR-style waiver. Every decision shall cite its alternatives and the evidence that drove the choice."
  anti_patterns: "Do not record decisions without alternatives. Do not let agent ADRs lag behind production changes. Do not omit the irreversibility-gating policy ADR."
  outputs: "AI_Agent_ADR_Catalogue.md and ADR-AGT-NNNN-<slug>.md files."
  references: "Use references/ai-agent-adr-templates.md."
---

# AI Agent ADR Catalogue Skill

## Required ADR slots

Every agent-feature SaaS shall have ADRs for the following decisions. Missing ADRs are blockers for any L1+ rollout.

1. **Autonomy Level per Feature** — L0..L4 placement with drivers and rejected alternatives.
2. **Irreversibility-gating Policy** — the rule for when human approval is required for irreversible tool calls; per-feature deviations.
3. **Planner Choice per Feature** — ReAct / Plan-and-execute / Tree-of-thought / Function-calling-loop / custom.
4. **Memory Store Technology and Tiering** — scratchpad, episodic, long-term: storage choice, isolation keys, retention.
5. **Tool-call Audit-log Retention by Event Class** — hot / cold per event class.
6. **Multi-agent Topology per Feature** — single-agent / supervisor-worker / debate / handoff chain.
7. **Supervision Policy** — review-before-act / review-after-act / sample-review.
8. **Kill-switch Propagation SLA** — default 5 s; per-feature exception only with ADR.
9. **Action Catalogue Change-control Protocol** — PR + ADR + red-team smoke + sign-off rules.
10. **Replay Environment Source-of-truth** — where the deterministic replay env lives; update protocol.
11. **Agent-task Quarantine Policy** — when to quarantine; tenant notification SLA.
12. **Agent Cost Envelope per Feature** — max-cost per run + per-tenant per-day budget.
13. **Plan-approval UI Authority** — what is shown at the approval moment; what can be hidden; signing of the approval event.
14. **Long-term Memory Opt-in Mechanism** — per-tenant flag; revocation behaviour.

## Workflow

1. Read inputs.
2. For each ADR slot, generate `ADR-AGT-NNNN-<slug>.md` using `references/ai-agent-adr-templates.md`.
3. Index in `AI_Agent_ADR_Catalogue.md`.
4. Link from the central `09-governance-compliance/05-architecture-decision-records` register and from `09-governance-compliance/17-ai-adr-catalogue`.
5. Sign-off per ADR: AI Lead + Architect + (DPO for compliance-touching ADRs; Security for kill-switch and supervision ADRs).

## Compliance-relevant ADR slots (additions)

In addition to the slots above, the following ADRs are required when the SaaS is in scope of SOC 2, ISO 27001, or HIPAA:

15. **SOC 2 Control-Ownership ADR** — names the role accountable for each agent-specific TSC control row; required before SOC 2 Type II window opens.
16. **HIPAA Admin-Only-PHI-Agent ADR** — confirms the admin-only constraint for clinical PHI agents; lists L0/L1 boundaries; required before any BAA execution.
17. **Audit-Log Integrity ADR** — hash-chain or WORM choice; daily integrity-check job; alerting on chain break.
18. **Auditor Portal Access ADR** — time-bound, named-recipient, logged-access policy; portal-access expiry default.
19. **Cross-Regime Evidence Reuse ADR** — declares the one-evidence-many-regimes posture; cross-link to `27-ai-agent-regulator-overlap-mapping`.

Each compliance ADR is signed by AI Lead + CISO + DPO and added to the agent ADR register before any audit window opens.

## Standards

- ADR pattern (Nygard)
- ISO/IEC 42001 Clause 8
- IEEE 1016-2009 §5
- EU AI Act Art. 14 (for the human-final-decision ADRs)
- AICPA TSP 100 (for SOC 2 control-ownership ADR)
- HIPAA §164.308 (for admin-only ADR)

# AI Agent / Multi-Agent Products SDLC-Docs Skills Audit — May 2026

This audit extends the AI-on-SaaS pass (see `ai-on-saas-srs-audit-2026.md`) with the documentation stack required when a SaaS product ships **agentic AI features** — LLM-driven systems that *plan*, *call tools*, *act on behalf of a user or tenant*, and may operate across multiple turns or even unattended. It contrasts the engine against the deliverables an enterprise agent-buying customer, an AI auditor (EU AI Act high-risk tier, US sectoral, emerging African AI guidance), and an internal Responsible-AI committee will demand of an agent product, and emits the new skill stack.

Convention: skill IDs follow the existing numbered pattern inside each phase. New skill numbering continues from the next free slot per phase. All new skills are prefixed with `ai-agent-` so they are discoverable as the agent family alongside the existing `ai-*` family.

## Summary of new artefacts created this session

- **New skills (13):** see "New skills" table below — one per phase gap for the agent family.
- **Enhanced skills (12):** agent addenda added to AI feature PRD, AI architecture, AI eval harness, AI red-team, AI hallucination SLO, AI feature rollout runbook, AI cost runbook, AI responsible-AI declaration, AI Act compliance, AI data flow / DPIA, AI ADR catalogue, and a placeholder for the planned SaaS rate-limiting skill.
- **Cross-cutting templates (12):** agent feature PRD, action catalogue, agent architecture, agent eval spec, agent red-team plan, agent SLO, agent runbook, agent rollout runbook, agent user disclosure, agent responsible-AI addendum, agent ADR pack, reversibility classification rubric.

---

## Why this is a separate pass from the AI-on-SaaS pass

The AI-on-SaaS pass intentionally treated agents as one of five architecture patterns (direct LLM call / RAG / agent / fine-tune / classical ML). Agents demand far more SDLC surface than any other pattern because the agent is not just a generator — it is an **actor**:

1. **Multi-step planning with tool use** — agents call tools, write to systems, send emails, charge cards, post to ticketing systems, modify files. The blast radius of a single agent run is fundamentally larger than a single LLM completion.
2. **Action accountability** — every action must be auditable to a (tenant, user, agent-run, plan-step, tool-call) tuple. A generic AI audit log is insufficient.
3. **Irreversibility classes** — some actions are idempotent (read, look-up), some are compensable (issue refund → reverse refund), some are irreversible (sent email, deleted file, executed trade). Different classes need different gates.
4. **Indirect prompt injection via tool output** — a malicious document, ticket comment, or web page fetched by the agent can inject instructions. This is a strictly larger attack surface than the RAG-injection class.
5. **Recursive self-modification** — agents that can edit their own memory, write to their own scratchpad, or spawn sub-agents present a topology-level supervision problem the existing red-team plan does not cover.
6. **Wall-clock / step / cost budgets** — an agent without a max-step or max-cost cap can run indefinitely or spend unboundedly. Cost runaway becomes a safety incident, not a FinOps incident.
7. **Human-in-the-loop placement is decisional** — for irreversible actions, the law (EU AI Act Art. 14) and the buyer both want explicit human approval. The PRD and the runtime must show *where* the human sits.
8. **Multi-agent coordination** — supervisor / worker, debate, handoff, scratchpad isolation. Coordination is its own architecture concern.
9. **Kill-switch and force-pause** — operations needs the ability to stop *all running agent runs for a tenant* (or globally) within seconds. This is a runbook the generic AI rollout runbook does not provide.
10. **Replay-based evaluation** — agent eval needs deterministic replay of (plan, tools, tool-outputs) to measure tool-choice quality, hallucinated-arg rate, and intervention rate — a strictly larger eval rig than the golden-set rig in the existing eval harness.

The AI-on-SaaS pass produced the generic AI architecture, eval harness, red-team plan, hallucination SLO, rollout runbook, responsible-AI declaration, and AI ADR catalogue. This pass layers agent-distinctive viewpoints on top.

---

## Phase 01 — Strategic Vision

### Gaps the agent reality reveals

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent vs workflow decision framework — when does a feature need an agent at all, vs a deterministic workflow or a single LLM call | Anthropic agentic-AI guidance; OpenAI agents SDK |
| 2 | No agent capability ladder by tier — what autonomy level ships at Free / Pro / Enterprise | Industry practice; vertical-AI buyer interviews |
| 3 | No agent moat asset declaration distinct from generic AI moat — proprietary action catalogue, tool-call telemetry, eval-set | Wardley mapping; agent-product post-mortems |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `14-ai-agent-strategy-doc` | `01-strategic-vision/14-ai-agent-strategy-doc/` | Agent vs workflow decision; agent capability ladder by tier; autonomy levels (suggest / approve-each / approve-batch / autonomous); agent moat |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `13-ai-feature-strategy-doc` | Cross-link to agent strategy doc when any feature is agentic; autonomy-by-tier note |

---

## Phase 02 — Requirements Engineering

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent-feature PRD spec — task scope, autonomy level, action catalogue summary, intervention triggers, budgets, abstain criteria, irreversible-action gates are not captured by the AI feature PRD | EU AI Act Art. 14; NIST AI RMF MAP |
| 2 | No formal action-catalogue specification — every tool with schema, side-effect class, reversibility class, per-tier availability, audit fields, rate-limit class, kill-switch behaviour | OWASP LLM Top 10 (agentic addendum); Anthropic tool-use guide |
| 3 | No multi-step plan approval document — plans of irreversible actions need a structured human-approval artefact | EU AI Act Art. 14; sectoral medical / financial guidance |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `16-ai-agent-feature-prd-spec` | `02-requirements-engineering/16-ai-agent-feature-prd-spec/` | Agent-feature PRD addendum: task scope, autonomy level, action-catalogue summary, intervention triggers, success metrics, max-step / max-cost / wallclock budgets, abstain criteria, irreversible-action gates |
| `17-ai-agent-action-catalogue-spec` | `02-requirements-engineering/17-ai-agent-action-catalogue-spec/` | Every tool the agent may call: name, schema, side-effect class, reversibility class, per-tier availability, audit fields, rate-limit class, kill-switch behaviour |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `14-ai-feature-prd-spec` | Cross-link to `16-ai-agent-feature-prd-spec` when the feature is agentic |

---

## Phase 03 — Design Documentation

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent runtime architecture spec — loop, state machine, memory tiers, planner, tool dispatcher, supervisor, durability, resumability, isolation per tenant | LangGraph / OpenAI Agents / Anthropic agent patterns |
| 2 | No multi-agent coordination spec — supervisor / worker, debate, handoff, scratchpad isolation | AutoGen, CrewAI, MetaGPT post-mortems |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `14-ai-agent-architecture-spec` | `03-design-documentation/14-ai-agent-architecture-spec/` | Agent runtime spec: loop, state machine, memory tiers, planner, tool dispatcher, supervisor for multi-agent, durability/resumability, per-tenant isolation |
| `15-ai-agent-multi-agent-coordination-spec` | `03-design-documentation/15-ai-agent-multi-agent-coordination-spec/` | Supervisor/worker, debate, handoffs, scratchpad isolation, topology choice |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `11-ai-architecture-spec` | Cross-link to agent runtime spec when any feature is agentic; agent-runtime row in the feature-to-pattern map |

---

## Phase 04 — Development Artefacts

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent-coding guidelines addendum — tool-schema discipline, irreversibility annotations, blast-radius caps, deterministic state, idempotency keys for tool calls, error/timeout policy | OWASP LLM Top 10; Anthropic agent-engineering guide |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `05-ai-agent-coding-guidelines-addendum` | `04-development-artifacts/05-ai-agent-coding-guidelines-addendum/` | Coding rules for agent-runtime code: tool-schema discipline, irreversibility annotations, blast-radius caps, deterministic state, idempotency keys, error/timeout policy |

---

## Phase 05 — Testing Documentation

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent eval spec — task success, step efficiency, tool-choice quality, hallucinated-arg rate, irreversible-action rate, intervention rate, golden tasks, replay-based eval, CI gates | OpenAI Evals (agents); Anthropic agent evals |
| 2 | No agent-specific red-team plan — indirect prompt injection via tool output, action escalation, tenant data exfil, recursive self-modify, jailbreak via memory, agent vs supervisor confusion | OWASP LLM Top 10 v2 (agentic); MITRE ATLAS |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `06-ai-agent-eval-spec` | `05-testing-documentation/06-ai-agent-eval-spec/` | Agent eval: task success, step efficiency, tool-choice quality, hallucinated-arg rate, irreversible-action rate, intervention rate, golden-task sets, replay-based eval, CI gates |
| `07-ai-agent-red-team-test-plan` | `05-testing-documentation/07-ai-agent-red-team-test-plan/` | Agent-specific adversarial scenarios: indirect prompt injection via tool output, action escalation, tenant data exfil, recursive self-modify, jailbreak via memory, agent vs supervisor confusion |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `04-ai-eval-harness-spec` | Cross-link to agent eval; note that agent features add agent-eval suites beyond the golden-set rig |
| `05-ai-red-team-test-plan` | Cross-link to agent red-team plan; note agent-specific attack classes |

---

## Phase 06 — Deployment & Operations

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent SLO doc — task success SLO, intervention SLO, irreversible-action-incident SLO, error budgets | Google SRE applied to agents |
| 2 | No agent runbook — kill-switch, force-pause, force-resume, agent-task quarantine, audit-log review cadence, agent-incident handling | Operations practice; agent-product incident reviews |
| 3 | No agent rollout runbook — shadow-mode pattern (agent suggests, human acts) needs explicit staging beyond canary | Anthropic / OpenAI agentic-launch playbooks |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `13-ai-agent-slo-doc` | `06-deployment-operations/13-ai-agent-slo-doc/` | Task success SLO, intervention SLO, irreversible-action-incident SLO, error budgets, burn-rate alerts |
| `14-ai-agent-runbook` | `06-deployment-operations/14-ai-agent-runbook/` | Kill-switch, force-pause, force-resume, agent-task quarantine, audit-log review cadence, agent-incident handling |
| `15-ai-agent-rollout-runbook` | `06-deployment-operations/15-ai-agent-rollout-runbook/` | Agent rollout stages: Internal → Dogfood → Shadow → Canary → Tier → GA; shadow-mode pattern (agent suggests, human acts) |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `10-ai-hallucination-slo-doc` | Agent-action-incident SLO row added |
| `11-ai-feature-rollout-runbook` | Shadow-mode stage inserted between dogfood and canary for agent features |
| `12-ai-cost-runbook` | Agent-cost dimensions (steps + tools + LLM + external) added |

---

## Phase 08 — End-User Documentation

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent user-disclosure pack — what the agent does / does not, where it has authority, how to override, undo/revert language, "agent worked on your behalf" notification design | EU AI Act Art. 13; CMA / FTC AI-disclosure guidance |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `09-ai-agent-user-disclosure-pack` | `08-end-user-documentation/09-ai-agent-user-disclosure-pack/` | User-facing disclosures: scope, authority, override, undo/revert, "agent worked on your behalf" notifications, tone and copy |

---

## Phase 09 — Governance & Compliance

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No agent-specific responsible-AI addendum — action accountability, audit-log retention, contestability of agent actions, human-final-decision principle for irreversible actions | EU AI Act Art. 14; NIST AI RMF GOVERN-3; ISO/IEC 42001 |
| 2 | No agent ADR family — required ADRs for autonomy level, irreversibility gating policy, planner choice, memory store, tool-call audit log retention, multi-agent topology, supervision policy | ADR pattern (Nygard) |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `18-ai-agent-responsible-ai-addendum` | `09-governance-compliance/18-ai-agent-responsible-ai-addendum/` | Agent-specific RAI: action accountability, audit-log retention, contestability of agent actions, human-final-decision principle for irreversible actions |
| `19-ai-agent-adr-catalogue` | `09-governance-compliance/19-ai-agent-adr-catalogue/` | Required agent ADRs: autonomy level, irreversibility gating policy, planner choice, memory store, tool-call audit log retention, multi-agent topology, supervision policy |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `14-ai-responsible-ai-declaration` | Agent paragraphs in the per-feature template; "agent worked on your behalf" disclosure pattern |
| `15-ai-act-and-regulatory-compliance-doc` | Agent tier under EU AI Act (high-risk classification triggers when irreversible / decisional) |
| `16-ai-data-flow-and-dpia` | Agent tool-call → external-service data flow added to DPIA template |
| `17-ai-adr-catalogue` | Agent ADR slots cross-linked; `19-ai-agent-adr-catalogue` flagged as the canonical agent ADR register |

---

## Cross-engine notes

- The placeholder skill `saas-rate-limiting-and-quotas` is referenced in the brief but does not yet exist in the engine. Recommend creating it in a follow-up session and giving it an agent-quota addendum (per-tenant max concurrent agent runs, per-tenant agent step rate, per-tenant agent cost-per-day cap).
- The agent ADR catalogue must be cross-linked from the central `09-governance-compliance/05-architecture-decision-records` register.
- Agent eval-set and red-team registries should sit alongside the existing AI eval-set and red-team registries; do not merge.

---

## Open gaps after this pass

1. **Agent observability spec** — agent-distinct telemetry (plan tree, tool-call span, intervention events) is referenced in the runtime spec but does not have its own skill. Candidate for a follow-up session.
2. **Agent simulator and synthetic-environment spec** — replay-based eval depends on a deterministic synthetic environment that we have specified at the eval-spec level only. A dedicated simulator-design skill may be warranted.
3. **Agent fine-tuning / distillation skill** — for teams that train action-policy heads on top of a base model.
4. **Multi-agent coordination ADRs** — partially covered in the agent ADR catalogue; may warrant a standalone catalogue when multi-agent topologies grow.

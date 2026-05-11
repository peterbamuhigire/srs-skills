# AI Agent ADR Templates (seed ADRs)

Each ADR follows:

```
# ADR-AGT-NNNN: <Decision title>

Status: { proposed | accepted | superseded by ADR-AGT-MMMM | deprecated }
Date: YYYY-MM-DD
Owners: <AI Lead, Architect, DPO if applicable, Security if applicable>

## Context
<why we are deciding this; constraints; risk class>

## Decision
<the choice>

## Consequences
<positive, negative, neutral>

## Alternatives Considered
- Option A: <why rejected>
- Option B: <why rejected>

## Evidence
- <pointers to eval, red-team, model card, SLO doc, agent runbook drill, regulatory requirement>

## Sign-off
- AI Lead: <name, date>
- Architect: <name, date>
- DPO (if applicable): <name, date>
- Security (if applicable): <name, date>
```

## Seed: ADR-AGT-001 — Autonomy Level for Inbox Triage

- Decision: L2 — approve plan, single approval per inbox-batch.
- Drivers: irreversible tools excluded from feature catalogue; admin trust gathered through 30 d shadow mode; latency budget incompatible with L1 per-step approval.
- Alternatives: L1 per-step (rejected: latency, UX friction); L3 autonomous (rejected: no executive trust signal yet).
- Evidence: GOLDEN-AGT-TRG-200 task success 0.94 in shadow; intervention rate 11% in shadow; zero irreversible incidents.

## Seed: ADR-AGT-002 — Irreversibility-gating Policy

- Decision: every tool with `reversibility_class=irreversible` requires per-call human approval at the named human role. Compensable tools above a per-tool threshold also require per-call approval. No bypass without a waiver and an ADR.
- Drivers: EU AI Act Art. 14; product-trust capital; observed agent-failure cost in adjacent products.
- Alternatives: plan-approval-only for irreversible (rejected: argument-mutation risk between approval and execution); fully autonomous with audit (rejected: no contestability).
- Evidence: RT-AGT-ESC-001 catches argument mutation; agent SLO irreversible-action-incident SLI zero-budget.

## Seed: ADR-AGT-003 — Planner Choice for Inbox Triage

- Decision: Plan-and-execute primary; ReAct fallback when plan adherence fails twice.
- Drivers: clearer audit trail; better human-approval UI; lower step variance.
- Alternatives: pure ReAct (rejected: step variance too high for budget caps); Tree-of-thought (rejected: cost).
- Evidence: comparison eval EVAL-AGT-TRG-200 across planner variants.

## Seed: ADR-AGT-004 — Memory Store Technology and Tiering

- Decision: Scratchpad in-process + durable in Postgres `agent_run_state` (keyed by `(tenant_id, agent_run_id)`); episodic in per-tenant Postgres table TTL 30 d; long-term in per-tenant Postgres + pgvector, opt-in flag.
- Drivers: tenant isolation primacy; existing operational competence with Postgres; replay-friendly serialisation.
- Alternatives: shared multi-tenant vector store with metadata filter (rejected: metadata-only isolation insufficient); Redis-only scratchpad (rejected: not durable enough for resume).
- Evidence: ADR-AI-004 (vector store) consistent; data-isolation evidence pack.

## Seed: ADR-AGT-005 — Tool-call Audit-log Retention

- Decision: per the table in the agent responsible-AI addendum; irreversible / billing / external-write events retained 7 years cold.
- Drivers: EU AI Act + sectoral regulation + dispute resolution.
- Alternatives: 13 months minimum (rejected: insufficient for financial dispute window).
- Evidence: DPA template clause; sub-processor list; storage cost runbook.

## Seed: ADR-AGT-006 — Multi-agent Topology for Research-and-summarise

- Decision: supervisor-worker with workers `Retriever`, `Drafter`, `Verifier`.
- Drivers: factuality below threshold without verifier; clear role bounding; observability.
- Alternatives: single-agent (rejected: factuality miss); debate (rejected: cost without measurable factuality lift in pilot).
- Evidence: pilot eval comparison; ADR-AGT-MA-001 cross-link.

## Seed: ADR-AGT-007 — Supervision Policy

- Decision: review-after-act with 20% sample-review for non-irreversible workers; review-before-act for any worker plan containing an irreversible tool.
- Drivers: throughput vs safety trade-off; irreversible-action incident rate zero-budget.
- Alternatives: full review-before-act (rejected: cost); sample-only (rejected: irreversible exposure).
- Evidence: SLO irreversible-action-incident = 0; agent runbook quarantine playbook.

## Seed: ADR-AGT-008 — Kill-switch Propagation SLA

- Decision: 5 seconds from operator flip to last dispatcher.
- Drivers: incident-containment requirements; monthly drill achievable.
- Alternatives: 30 s (rejected: too slow for mass-incident containment); 1 s (rejected: infra cost prohibitive at current scale).
- Evidence: monthly chaos drill `agent-killswitch-chaos`.

## Seed: ADR-AGT-009 — Action Catalogue Change-control Protocol

- Decision: PR + back-end-owner reviewer + AI Lead + Security; red-team smoke targeting new tool category; ADR if class / tier / approval requirement changes; sign-off via `python -m engine signoff`.
- Drivers: catalogue is the security boundary.
- Alternatives: PR-only (rejected: bypasses red-team); ADR-always (rejected: friction for additive read tools).
- Evidence: red-team registry; PR history.

## Seed: ADR-AGT-010 — Replay Environment Source-of-truth

- Decision: per-feature directories under `replay-env/<feature>/`; YAML format; PR reviewer = back-end owner of every referenced system.
- Drivers: deterministic eval; team-shared.
- Alternatives: per-developer local fixtures (rejected: drift); central DB (rejected: review friction).
- Evidence: agent eval rig dependency.

## Seed: ADR-AGT-011 — Agent-task Quarantine Policy

- Decision: per the agent runbook §4; tenant admin notified within 24 h.
- Drivers: contestability + regulatory.
- Alternatives: silent quarantine (rejected: bad faith); immediate purge (rejected: loses forensic evidence).
- Evidence: agent runbook drill records.

## Seed: ADR-AGT-012 — Agent Cost Envelope

- Decision: per-feature max-cost per run + per-tenant per-day budget; per the agent feature PRD.
- Drivers: cost runaway is a safety incident.
- Alternatives: no per-tenant cap (rejected: SaaS-financial risk); single global cap (rejected: blocks legitimate Enterprise usage).
- Evidence: agent cost runbook simulation.

## Seed: ADR-AGT-013 — Plan-approval UI Authority

- Decision: the plan-approval surface shows full plan, full tool args, full justification; signs the approval event with the human's identity; events are immutable.
- Drivers: contestability; argument-mutation prevention.
- Alternatives: summarised plan in UI (rejected: deception risk per RT-AGT-PLAN-SE class).
- Evidence: red-team plan-approval social-engineering scenarios.

## Seed: ADR-AGT-014 — Long-term Memory Opt-in Mechanism

- Decision: per-tenant opt-in flag; default off; revocation purges within 30 d; agent feature degrades gracefully when off.
- Drivers: data-protection minimisation; tenant autonomy.
- Alternatives: default on (rejected: data-protection); per-user opt-in only (rejected: admin-scope governance preferred).
- Evidence: DPIA addendum.

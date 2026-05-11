# AI Agent Strategy Doc Template

## 1. Agent-vs-Workflow Verdicts

| Candidate feature | Multi-step? | Tool use beyond retrieval? | Outcome-shaped success? | Variable step count? | Verdict |
|--------------------|-------------|-----------------------------|--------------------------|-----------------------|---------|
| Inbox Triage | yes | yes (label, archive, draft-reply) | yes | yes | AGENT |
| Daily Reconciliation | yes | yes (ledger writes) | yes | yes | AGENT |
| Subject-line Generator | no | no | no | no | DIRECT-LLM |
| Document Summary | no | no | partly | no | DIRECT-LLM |

A "yes" count of three or four is required to classify as an agent.

## 2. Autonomy Ladder Placement

| Agent feature | Level | Justification |
|----------------|-------|----------------|
| Inbox Triage | L2 — approve plan | irreversible "send draft" is gated by approval of the full plan |
| Daily Reconciliation | L3 — autonomous within envelope | runs nightly within $50/day and within the read-write scope of `finance.ledger.*` tools |
| Support Triage | L1 — approve each step | each ticket action requires admin click; trust not yet earned |

## 3. Tier Placement

| Agent feature | Tier | Notes |
|----------------|------|-------|
| Inbox Triage | Pro | idempotent + compensable actions only |
| Daily Reconciliation | Enterprise | irreversible writes; needs policy envelope + audit |
| Support Triage | Pro | no irreversible actions |

## 4. Moat Declaration

| Agent feature | Moat asset | Notes |
|----------------|-------------|-------|
| Inbox Triage | Action telemetry + eval-set | 6 months of labelled triage traces; competitors lack data |
| Daily Reconciliation | Proprietary action catalogue (ledger tools) | deep integration with the internal ERP; partner-exclusive API |
| Support Triage | Integration depth | Zendesk + Salesforce native; competitors require manual config |

## 5. Sequencing Roadmap

| Quarter | Feature | Dependency |
|---------|---------|-------------|
| Q2 2026 | Inbox Triage L0 (suggest only) | agent runtime, action catalogue v1, eval rig |
| Q3 2026 | Inbox Triage L1 → L2 | audit log, human-approval UI, kill-switch |
| Q4 2026 | Support Triage L1 | red-team for tool injection |
| Q1 2027 | Daily Reconciliation L3 | full audit + DPIA + EU AI Act high-risk classification |

## 6. Risk & Dependency Register

| Risk | Mitigation | Owner |
|------|-------------|-------|
| Irreversible action without human gate | reversibility-classification rubric enforced at action-catalogue PR | AI Lead |
| Indirect prompt injection via tool output | tool-output sanitiser in dispatcher; red-team coverage | Security Lead |
| Cross-tenant action via misrouted tool call | tenant-claim re-validation at every tool dispatch | Platform Lead |
| Supervision-cost runaway at L3 | max-cost-per-day cap; pause on overshoot | Ops Lead |
| EU AI Act high-risk classification surprise | early regulatory tier review per feature | DPO |

## 7. Glossary

- **Agent** — LLM-driven system that plans, calls tools, and acts across multiple steps.
- **Autonomy level (L0..L4)** — see Step 2 of the skill.
- **Action catalogue** — the enumerated set of tools the agent may call.
- **Policy envelope** — the constraints (budget, scope, time-window) within which an L3 agent acts unattended.
- **Shadow mode** — production stage in which the agent proposes actions but a human acts; used to gather evidence before promoting to L1+.

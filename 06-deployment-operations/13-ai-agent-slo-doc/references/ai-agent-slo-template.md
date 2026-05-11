# AI Agent SLO Doc Template

## 1. Agent SLI Inventory

| SLI | Definition | Source |
|-----|------------|--------|
| Task success | runs where judge marks goal-state reached / runs sampled | nightly production replay + judge-LLM |
| Step efficiency | mean(steps_actual / steps_gold) on successful runs | orchestrator metrics |
| Intervention | % of runs with mid-run human intervention | orchestrator metrics |
| Irreversible-action incident | irreversible actions later flagged as wrong per million runs | user flag + admin review |
| Agent-task availability | % of starts reaching terminal state within max-wallclock without infra failure | orchestrator metrics |
| Agent-cost-per-run | mean and P95 USD cost / run | dispatcher cost meter |
| Tool-error rate | % of tool calls returning non-retryable or safety errors | dispatcher metrics |

## 2. Measurement Procedure

| SLI | Sample / window | Cadence |
|-----|------------------|----------|
| Task success | 200 production runs per feature per night | nightly |
| Intervention | all runs | real-time |
| Irreversible incident | all flagged + all admin-reviewed | real-time + weekly audit |
| Availability | all runs | real-time |
| Cost-per-run | all runs | real-time |
| Tool-error rate | all tool calls | real-time |

## 3. Per-feature SLO Targets

### Inbox Triage (Pro)

| SLI | Target |
|-----|--------|
| Task success | >= 0.90 |
| Intervention | <= 20% |
| Irreversible incident | 0 |
| Availability | >= 0.99 |
| Cost-per-run | mean <= $0.20; P95 <= $0.40 |
| Tool-error rate | <= 1% |

### Daily Reconciliation (Enterprise)

| SLI | Target |
|-----|--------|
| Task success | >= 0.95 |
| Intervention | <= 10% |
| Irreversible incident | 0 |
| Availability | >= 0.995 |
| Cost-per-run | mean <= $40; P95 <= $50 |
| Tool-error rate | <= 0.5% |

## 4. Error Budgets

| SLI | Window | Budget |
|-----|--------|--------|
| Task success (Pro 0.90) | monthly | 10% of runs |
| Intervention (Pro 20%) | monthly | 20% of runs |
| Irreversible incident | always | 0 |
| Availability (Pro 0.99) | monthly | 1% of starts |

## 5. Burn-Rate Alerts

| Alert | Burn | Window | Threshold |
|-------|------|--------|-----------|
| Fast burn — task success | 14x | 1 h | 2% of monthly |
| Medium burn — task success | 6x | 6 h | 5% |
| Slow burn — task success | 1x | 3 d | 10% |
| Intervention surge | 3x baseline | 1 h | any feature |
| Irreversible incident | n/a | 0 | any |
| Cost overshoot per tenant | 200% of envelope | 1 h | throttle then pause |

## 6. Freeze & Pause Rules

- Task-success budget exhausted: planner and catalogue changes frozen; further model bumps require executive sign-off.
- Intervention rate up > 50% in 7 d: rollback last planner/prompt change; SEV2.
- Irreversible incident: per-tenant feature kill-switch; SEV1; postmortem within 5 working days; admin notification within 24 h.
- Cost overshoot: per-tenant throttle; if persists 1 h, per-tenant pause; SEV2.

## 7. Customer-Facing Commitments

| Tier | Commitment |
|------|-------------|
| Pro | Agent-task availability >= 99.0% monthly. Notification of any irreversible-action incident within 24 h. UI marking on every agent-performed action. Right to disable an agent feature per workspace. |
| Enterprise | Availability >= 99.5%. Same notification standard. Right to require per-call human approval for any tool class. Quarterly agent-quality review with the customer's RAI representative. |

## 8. Review Cadence

- Monthly: SLI dashboard reviewed with AI lead, SRE, and product.
- Quarterly: customer-facing commitments reviewed with legal.
- After any SEV1 or SEV2: review the relevant SLOs for tightening.

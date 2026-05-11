# Agent Shadow-Mode Stage Cross-Link

The AI Feature Rollout Runbook defines five stages: internal → design partners → opt-in beta → percentage cohort → GA. For agent features, the **AI Agent Rollout Runbook** (`06-deployment-operations/15-ai-agent-rollout-runbook`) inserts **shadow mode** between internal and canary, and replaces "opt-in beta" with explicit autonomy-level promotion.

## Shadow mode

The agent runs end-to-end and proposes actions; *humans actually execute*. The agent's plan and proposed actions are recorded and judged offline. No customer-visible change to outcomes.

Shadow mode is mandatory between dogfood and canary for any feature that includes write or external tools.

## Promotion gates additional to the generic runbook

| From → To | Additional gate |
|------------|------------------|
| Dogfood → Shadow | agent runbook drills (kill-switch, replay, quarantine) executed |
| Shadow → Canary L1 | shadow agreement rate >= 0.85; zero CRITICAL/HIGH agent-red-team; irreversible-incident rate = 0 on shadow trajectories |
| Canary → Tier | irreversible-incident rate = 0 during canary bake (>= 14 d) |
| Tier → GA | full agent SLO targets met for 30 d; responsible-AI addendum updated |

## Auto-rollback addition

Add: irreversible-action incident → per-feature kill-switch + SEV1 (in addition to the existing safety-violation pause).

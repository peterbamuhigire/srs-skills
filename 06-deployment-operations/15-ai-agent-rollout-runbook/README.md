## Objective

Produce the AI Agent Rollout Runbook: stages (Internal → Dogfood → Shadow → Canary → Tier → GA), promotion gates, auto-rollback triggers, comms plan, opt-in/out by region, post-launch monitoring window, roles and sign-off ledger.

## Execution Steps

1. Verify `AI_Agent_Feature_PRD_Spec.md`, `AI_Agent_Eval_Spec.md`, `AI_Agent_Red_Team_Test_Plan.md`, `AI_Agent_SLO_Doc.md`, `AI_Agent_Runbook.md`, `Tenant_Lifecycle_Runbook.md` exist.
2. Invoke `logic.prompt`.
3. Review with AI lead, SRE lead, customer success, and legal.

## Standards

- Google production-launch checklists
- Anthropic / OpenAI agent-launch playbooks
- ISO/IEC 42001
- EU AI Act Art. 13

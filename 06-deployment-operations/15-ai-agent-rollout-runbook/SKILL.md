---
name: "ai-agent-rollout-runbook"
description: "Generate the AI Agent Rollout Runbook: staged rollout (Internal → Dogfood → Shadow → Canary → Tier → GA), the shadow-mode pattern (agent proposes; human acts), promotion gates tied to agent eval + agent red-team + agent SLO, auto-rollback triggers, comms plan, opt-in/out per region, and the post-launch monitoring window."
metadata:
  use_when: "Use before any agent feature reaches GA, before any L1+ promotion, and before any change to planner / action catalogue / supervisor / memory store policy."
  do_not_use_when: "Do not use for purely internal experiments with no customer exposure; cover those with the generic AI feature rollout runbook."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, Tenant_Lifecycle_Runbook.md."
  workflow: "Define rollout stages including shadow-mode, set promotion gates per stage, define auto-rollback triggers, write comms plan per stage, define opt-in / opt-out by region, define post-launch monitoring window, write the runbook."
  quality_standards: "Every agent feature shall pass through shadow mode before any execution stage. Every stage shall have promotion gates tied to agent eval, agent red-team, and agent SLO. Every customer-visible change shall have a comms artefact."
  anti_patterns: "Do not promote past shadow mode without bake-period evidence. Do not promote past canary without irreversible-action audit at zero. Do not omit opt-in posture in regulated regions (EEA default off for L2+)."
  outputs: "AI_Agent_Rollout_Runbook.md."
  references: "Use references/ai-agent-rollout-runbook-template.md."
---

# AI Agent Rollout Runbook Skill

## Core Instructions

### Step 1: Rollout stages

Standard stages for an agent feature:

1. **Internal staff (dogfood)** — engineering and ops use the feature in our own workspace.
2. **Shadow mode** — the agent runs end-to-end and proposes actions; *humans actually execute*. The agent's plan and proposed actions are recorded and judged offline. No customer-visible change to outcomes.
3. **Canary at L1** — small named cohort opted in; the agent acts with per-call human approval; bake period.
4. **Tier rollout** — promoted to the target tier (Pro or Enterprise) with the target autonomy level; percentage cohort within tier (e.g. 5% → 25% → 50% → 100%).
5. **GA** — feature documented in trust center, sales enablement, customer commitments.

Shadow mode is mandatory between dogfood and canary for any feature that includes write or external tools. Shadow mode is the cheapest stage to collect human-judged trajectory evidence without exposing customers to agent execution risk.

### Step 2: Promotion gates

Per stage, all gates must pass for the bake duration:

| From → To | Gates |
|------------|-------|
| Dogfood → Shadow | agent eval green; red-team smoke green; runbook drills complete |
| Shadow → Canary L1 | shadow agreement rate >= 0.85 (judge-LLM agrees with human action); zero CRITICAL / HIGH red-team open; irreversible-action-incident rate = 0 on shadow trajectories |
| Canary L1 → Tier rollout | task success >= SLO target; intervention rate <= SLO target; irreversible-action incidents = 0 during canary bake (minimum 14 d) |
| Tier rollout (cohort %) | per cohort: SLOs met for 7 d; no SEV1/SEV2 attributable |
| Tier rollout → GA | full SLO targets met for 30 d; trust-center entry approved; legal review of disclosures complete |

### Step 3: Auto-rollback triggers

Wired to the feature-flag and dispatcher state:

- Irreversible-action incident → per-feature kill-switch + SEV1.
- Task success drop > 5 pp in 24 h → auto-rollback planner / prompt tag.
- Intervention rate up > 50% in 24 h → auto-rollback last planner / prompt change.
- Cost-per-run P95 > 200% of ceiling for 1 h → throttle then pause.
- Red-team CI regression on next PR → block merge.

### Step 4: Comms plan

- Internal (dogfood and shadow): launch readiness review, run-of-show, ops channel watch list.
- Canary cohort: per-customer kickoff call; daily check-in for first 7 d; success-team owner.
- Percentage cohort: in-product modal disclosing agent feature + scope + revert path; help-centre article.
- GA: blog post; customer email; sales enablement; trust-center update.

### Step 5: Opt-in / opt-out by region

- Default state per region: EEA defaults to off for L2+ features. UK / US / CA default on at L1 with disclosure.
- Workspace admin can disable per workspace at any stage.
- End user disclosure on first agent action ("This task was performed by the X agent on your behalf").
- Privacy notice for consent capture where the agent processes special-category personal data.

### Step 6: Post-launch monitoring window

First 30 days post-GA: heightened monitoring; daily agent-quality stand-up; immediate review of every irreversible-action audit event; weekly review of cost-per-tenant; bi-weekly review of customer flags.

### Step 7: Write the runbook

`AI_Agent_Rollout_Runbook.md` sections: 1) Rollout Stages, 2) Promotion Gates, 3) Auto-Rollback Triggers, 4) Comms Plan, 5) Opt-in / Opt-out, 6) Post-Launch Monitoring Window, 7) Roles & Sign-off Ledger.

## Standards

- Google production-launch checklists
- Anthropic / OpenAI agent-launch playbooks
- ISO/IEC 42001 Clause 8
- EU AI Act Art. 13 (transparency) for disclosures

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-rollout-runbook-template.md`.

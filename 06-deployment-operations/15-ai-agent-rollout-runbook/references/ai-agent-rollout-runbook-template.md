# AI Agent Rollout Runbook Template

## 1. Rollout Stages

| Stage | Audience | Autonomy | Duration |
|-------|----------|----------|----------|
| Dogfood | Internal staff | L0 → L1 | 7 d minimum |
| Shadow | All target users, opt-in | L0-equivalent (proposes; human acts) | 14-30 d |
| Canary L1 | Named design partners | L1 (per-call HITL) | 14 d minimum |
| Tier rollout | Pro or Enterprise cohort at % | target autonomy | 5% → 25% → 50% → 100%, each step 7 d |
| GA | Full availability per tier | target autonomy | ongoing |

## 2. Promotion Gates

### Dogfood → Shadow

- Agent eval green on golden-task set.
- Red-team smoke green: zero CRITICAL / HIGH open.
- Agent runbook drills (kill-switch, replay, quarantine) executed.
- Coding-guideline static checks passing.

### Shadow → Canary L1

- Shadow agreement rate >= 0.85 (judge-LLM agrees with the human action that was taken).
- Zero CRITICAL / HIGH red-team open.
- Irreversible-action-incident rate = 0 on shadow trajectories (counted as: had the agent's plan been executed, would the action have been incorrect).
- Bake duration met (14-30 d).

### Canary L1 → Tier rollout

- Task success >= SLO target for the feature/tier.
- Intervention rate <= SLO target.
- Irreversible-action incidents = 0 during canary bake (minimum 14 d).
- Customer success qualitative sign-off.

### Tier rollout cohort progression

- Each cohort step: SLOs met for 7 d; no SEV1/SEV2 attributable.
- Cost-per-run within ceiling for the tier.

### Tier rollout → GA

- Full SLO targets met for 30 d.
- Trust-center entry approved.
- Legal review of disclosures complete.
- Responsible-AI addendum updated.
- Customer comms artefacts prepared.

## 3. Auto-Rollback Triggers

| Trigger | Action |
|---------|--------|
| Irreversible-action incident | per-feature kill-switch + SEV1 |
| Task success drop > 5 pp in 24 h | auto-rollback to last green planner / prompt tag |
| Intervention rate up > 50% in 24 h | auto-rollback last planner / prompt change |
| Cost-per-run P95 > 200% of ceiling for 1 h | throttle; if persists, pause |
| Red-team CI regression on next PR | block merge |

## 4. Comms Plan

| Stage | Internal | External |
|-------|----------|----------|
| Dogfood | launch readiness review; ops channel | none |
| Shadow | weekly status; ops on-call | enrolled tenants receive "shadow-running" notice; no UI change |
| Canary L1 | kickoff with design partners; daily check-in first 7 d | per-customer kickoff call |
| Tier rollout 5%-50% | per-cohort review | in-product modal disclosing the agent + scope + revert; help-centre article |
| GA | sales / CS enablement | blog post; customer email; trust-center update |

## 5. Opt-in / Opt-out

| Region | Default state | Override |
|--------|---------------|----------|
| EEA | off for L2+; off for any feature processing special-category personal data | workspace admin opt-in |
| UK | on at L1 with disclosure; admin opt-out | admin per workspace |
| US / CA | on at L1 with disclosure; admin opt-out | admin per workspace |
| LATAM / APAC | on at L1 with disclosure; admin opt-out | admin per workspace |
| Africa (uganda etc) | per local DPA; default on at L1 with disclosure; opt-out admin | admin per workspace |

First-action disclosure copy: "This task was performed by the <feature> agent on your behalf. <Undo / Review> | <How agents work>".

## 6. Post-Launch Monitoring Window

First 30 days post-GA:

- Daily agent-quality stand-up (AI Lead + SRE + Customer Success).
- Daily review of every irreversible-action audit event.
- Weekly cost-per-tenant review.
- Bi-weekly customer flag review.
- Weekly red-team smoke re-run.

## 7. Roles & Sign-off Ledger

| Stage | Signer roles | Artefact |
|-------|---------------|----------|
| Dogfood → Shadow | AI Lead, Architect | `signoff/agent-<feature>-shadow.md` |
| Shadow → Canary | AI Lead, Security, DPO if applicable | `signoff/agent-<feature>-canary.md` |
| Canary → Tier | AI Lead, Customer Success, SRE | `signoff/agent-<feature>-tier.md` |
| Tier → GA | AI Lead, Legal, CTO | `signoff/agent-<feature>-ga.md` |

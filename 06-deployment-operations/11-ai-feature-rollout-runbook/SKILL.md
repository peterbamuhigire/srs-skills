---
name: "ai-feature-rollout-runbook"
description: "Generate the AI Feature Rollout Runbook: staged rollout (internal -> design partners -> opt-in beta -> percentage cohort -> GA), canary cohort definition, auto-rollback triggers tied to eval and SLO, comms plan, opt-in/out handling, and the post-launch monitoring window."
metadata:
  use_when: "Use before any AI feature reaches GA or before any model / prompt change is promoted to production."
  do_not_use_when: "Do not use for purely internal AI experiments with no customer exposure."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Eval_Harness_Spec.md, AI_Red_Team_Test_Plan.md, AI_Hallucination_SLO_Doc.md, Tenant_Lifecycle_Runbook.md."
  workflow: "Define rollout stages, set promotion gates per stage, define auto-rollback triggers, write comms plan per stage, define opt-in/out handling, define post-launch monitoring window, write the runbook."
  quality_standards: "Every stage shall have a promotion gate tied to eval + red-team + SLO. Every stage shall have an auto-rollback trigger. Every customer-visible change shall have a comms artefact."
  anti_patterns: "Do not promote on calendar deadlines without gate evidence. Do not promote past beta without an attached rollback rehearsal. Do not omit the opt-in posture for regulated regions."
  outputs: "AI_Feature_Rollout_Runbook.md."
  references: "Use references/ai-rollout-runbook-template.md."
---

# AI Feature Rollout Runbook Skill

## Core Instructions

### Step 1: Rollout stage definition

Standard stages for an AI feature:

1. Internal staff (dogfood).
2. Design partners (named cohort, opt-in, single-digit count).
3. Opt-in beta (workspace-admin opt-in).
4. Percentage cohort (e.g. 5% -> 25% -> 50% -> 100%).
5. GA.

### Step 2: Promotion gates

Each stage to the next requires:

- Eval harness green on the golden set for the bake duration.
- Red-team smoke green; zero CRITICAL or HIGH open.
- Hallucination SLO met for the bake duration.
- Cost-per-call within ceiling.
- Customer success sign-off (qualitative feedback from current stage).

### Step 3: Auto-rollback triggers

Wire concrete triggers to the gateway / feature-flag system:

- Citation accuracy drop > 5 pp in 24 h -> auto-rollback prompt tag.
- Safety violation -> pause feature.
- Cost overshoot per-tenant 200% of ceiling for 1 h -> throttle then pause.
- Eval CI regression on next prompt PR -> block merge.

### Step 4: Comms plan

- Internal: launch readiness review, run-of-show, channel watch list.
- Design partners: pre-rollout email, daily check-in for first 7 d.
- Opt-in beta: in-product modal, help-centre article.
- Percentage cohort: status-page entry, release notes draft.
- GA: blog post, customer email, sales enablement update, trust-center update.

### Step 5: Opt-in / opt-out handling

- Default state per region (EEA defaults to off for high-risk features).
- Workspace admin can disable per workspace.
- End user disclosure on first use.
- Privacy notice for consent capture.

### Step 6: Post-launch monitoring window

First 14 days post-GA: heightened monitoring; daily AI-quality stand-up; immediate review of flagged outputs; review of cost-per-tenant.

### Step 7: Write the runbook

`AI_Feature_Rollout_Runbook.md` sections: 1) Rollout Stages, 2) Promotion Gates, 3) Auto-Rollback Triggers, 4) Comms Plan, 5) Opt-in / Opt-out, 6) Post-Launch Monitoring, 7) Roles & Sign-off Ledger.

## Standards

- Google production-launch checklists
- Anthropic / OpenAI production-LLM playbooks
- ISO/IEC 42001 Clause 8 (operation)

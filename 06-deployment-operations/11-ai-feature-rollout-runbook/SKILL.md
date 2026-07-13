---
name: 11-ai-feature-rollout-runbook
description: Use when rolling out a non-agentic AI feature through offline, shadow, limited, and wider exposure with evaluation gates, bake periods, rollback triggers, and owners; use ai-agent-rollout-runbook for autonomy changes.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Feature Rollout Runbook Skill

<!-- dual-compat-start -->
## Use When

- Produce or update controlled AI rollout runbook from approved project evidence.
- Resolve decisions about staged exposure, promotion gates, bake periods, rollback triggers, and authority.
- Prepare a reviewable handoff for AI release and operations teams.

## Do Not Use When

- The task is primarily owned by go-live-readiness; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Controlled AI Rollout Runbook | AI release and operations teams | Every stage has an eligible cohort, measurable gate, minimum observation period, rollback trigger, and named approver. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Inspection is read-only by default. Create or edit the named project document only when explicitly authorised. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose promotion from observed stage evidence and produce the full artefact. | Scaling harm before it is measurable. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring go-live-readiness concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every stage has an eligible cohort, measurable gate, minimum observation period, rollback trigger, and named approver.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
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

---
name: 12-ai-cost-runbook
description: Use when producing or updating AI cost operations runbook for cost signals, budgets, attribution, anomaly response, containment, and current price evidence. Use slo-and-error-budget for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# AI Cost Runbook Skill

<!-- dual-compat-start -->
## Use When

- Produce or update AI cost operations runbook from approved project evidence.
- Resolve decisions about cost signals, budgets, attribution, anomaly response, containment, and current price evidence.
- Prepare a reviewable handoff for FinOps, AI operations, and product owners.

## Do Not Use When

- The task is primarily owned by slo-and-error-budget; route there and use this skill only for its named output.
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
| AI Cost Operations Runbook | FinOps, AI operations, and product owners | Cost decisions use versioned usage evidence and current verified provider prices; anomalies have containment and reconciliation steps. |
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
| Evidence is complete and authority is explicit | Choose containment from verified spend variance and customer impact and produce the full artefact. | Stale-price decisions or uncontrolled spend. |
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
- Mixing the neighbouring slo-and-error-budget concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when cost decisions use versioned usage evidence and current verified provider prices; anomalies have containment and reconciliation steps.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Core Instructions

### Step 1: Cost-generating component inventory

For each AI feature list every cost-bearing component: model calls (provider $/M tokens), embedding calls, vector ops (per-query, per-storage), reranker, judge-LLM, content-filter, agent tool invocations (third-party APIs), egress.

### Step 2: Per-call and per-tenant ceilings

Set per-(feature, tenant, day) and per-(feature, tenant, month) ceilings. Ceilings are tier-defaulted; admins can request higher.

### Step 3: Spend anomaly detection

Per-tenant baseline computed over the last 14 d. Alert at 2x baseline within 1 h; 3x within 5 min for Enterprise tier.

### Step 4: Throttle / pause / fallback rules

- 100% of ceiling: throttle (slow path, larger batch sizes, smaller model).
- 150% of ceiling: hard throttle (queue, with user-visible message).
- 200% of ceiling: pause feature for the tenant; CSM contact within 15 min.
- Cost > 130% of per-call ceiling: route to cheaper model (state which model).
- Anomaly above 5x baseline: pause and SEV1; possible abuse / misconfig.

### Step 5: Model-fallback policy

Define the fallback ladder per feature: primary -> cheaper-but-comparable -> abstain.

### Step 6: FinOps cadence

- Daily: cost dashboards reviewed by FinOps + AI lead.
- Weekly: per-feature, per-tier cost-per-call trend.
- Monthly: per-tenant top spenders + outliers; renewal-risk flags to CSM.
- Quarterly: cost-vs-pricing-tier reconciliation.

### Step 7: Billing-event reconciliation

Every cost-bearing AI call emits a billing event (cross-link `02-requirements-engineering/13-saas-billing-and-metering-spec` AI usage-metering events). The reconciliation job matches gateway logs against billing-event store nightly; missing events trigger a SEV3.

### Step 8: Write the runbook

`AI_Cost_Runbook.md` sections: 1) Cost-Generating Components, 2) Per-Tenant & Per-Feature Ceilings, 3) Spend Anomaly Detection, 4) Throttle / Pause / Fallback Rules, 5) Model-Fallback Policy, 6) FinOps Cadence, 7) Billing-Event Reconciliation, 8) On-Call Procedure.

## Standards

- FinOps Foundation framework
- Provider FinOps playbooks (OpenAI, Anthropic enterprise)
- ISO/IEC 42001 Clause 8 (operation)

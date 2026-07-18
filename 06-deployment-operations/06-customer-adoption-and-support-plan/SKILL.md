---
name: 06-customer-adoption-and-support-plan
description: Use when producing or updating customer adoption and support plan for onboarding, training, support readiness, feedback, escalation, and adoption measures. Use go-live-readiness for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Customer Adoption And Support Plan

<!-- dual-compat-start -->
## Use When

- Produce or update customer adoption and support plan from approved project evidence.
- Resolve decisions about onboarding, training, support readiness, feedback, escalation, and adoption measures.
- Prepare a reviewable handoff for Customer-success and support teams.

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
| Customer Adoption And Support Plan | Customer-success and support teams | Named user cohorts have onboarding, support ownership, measurable adoption outcomes, and escalation paths. |
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
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose rollout support by user risk and change impact and produce the full artefact. | A launch plan with no adoption evidence. |
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

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when named user cohorts have onboarding, support ownership, measurable adoption outcomes, and escalation paths.

## References

- [Repository router](../../README.md) - project pathing, phase sequence, and delivery rules.
<!-- dual-compat-end -->

## Use When

- A release needs user adoption, training, launch communication, support scripts, hypercare, maintenance, or customer recovery.
- Go-live readiness has support, service, or organisational transition gaps.
- SaaS, AI, website, mobile, public-sector, or premium systems require rollout beyond technical deployment.

## Do Not Use When

- The release is purely internal and has no user, customer, support, training, or maintenance impact.
- Deployment has no confirmed scope, audience, owner, or launch window.
- Support commitments cannot be approved by the delivery or operations owner.

## Required Inputs

- Release scope, stakeholder register, user roles, deployment guide, runbook, monitoring setup, UX/user documentation, known risks, service levels, and maintenance model.
- Existing go-live readiness report or solution transition plan when available.

## Workflow

1. Segment adopters, buyers, users, support agents, administrators, and executive stakeholders.
2. Define adoption outcomes and behavioural success metrics.
3. Build launch communications by audience and channel.
4. Define training plan, enablement materials, and proof-of-understanding checks.
5. Define support model, scripts, escalation, customer recovery, and hypercare cadence.
6. Define maintenance expectations, renewal/review cadence, and feedback-to-backlog loop.
7. Use `references/rollout-support-and-customer-service-scripts.md` before finalising.

## Quality Standards

- Adoption must be measured by user behaviour and operational outcomes, not announcement delivery.
- Every support script must include acknowledgement, diagnosis, action, expectation, and follow-up.
- Support and maintenance commitments must align with monitoring, runbook, SLA, and commercial promises.

## Anti-Patterns

- Launching with documentation but no training, support ownership, or recovery language.
- Treating customer service as generic friendliness rather than a controlled operational process.
- Making premium promises that the support model cannot deliver.

## Outputs

- Customer adoption and support plan.
- Audience communication matrix.
- Training and enablement plan.
- Service desk scripts, escalation paths, and customer recovery playbook.
- Maintenance and feedback loop.

## References

- `references/rollout-support-and-customer-service-scripts.md`


## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/Customer_Adoption_And_Support_Plan.md` with rollout audiences, adoption metrics, communications, training, support scripts, escalation, hypercare, and maintenance expectations.


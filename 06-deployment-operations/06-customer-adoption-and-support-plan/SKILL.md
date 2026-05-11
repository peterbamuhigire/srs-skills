---
name: 06-customer-adoption-and-support-plan
description: Generate customer adoption, training, rollout communication, service desk, escalation, recovery, maintenance, and post-launch support plans for SDLC deliverables. Use before pilots, go-live, SaaS rollout, public-sector launch, website launch, AI system adoption, or premium client handover.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Customer Adoption And Support Plan

<!-- dual-compat-start -->
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
<!-- dual-compat-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/Customer_Adoption_And_Support_Plan.md` with rollout audiences, adoption metrics, communications, training, support scripts, escalation, hypercare, and maintenance expectations.


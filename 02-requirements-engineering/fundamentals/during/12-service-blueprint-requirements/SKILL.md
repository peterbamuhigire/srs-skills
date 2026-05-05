---
name: 12-service-blueprint-requirements
description: Convert service blueprints into requirements for frontstage UX, backstage operations, support, evidence, handoffs, failures, recovery, implementation, rollout, maintenance, and governance. Use for SaaS, websites, mobile apps, public-sector services, AI systems, and service-heavy products where delivery depends on people, process, policy, and technology working together.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Service Blueprint Requirements

<!-- dual-compat-start -->
## Use When

- A system has frontstage user interactions and backstage staff, automation, operations, or partner work.
- Requirements must cover handoffs, support, failure recovery, evidence, service desk scripts, governance, or rollout.
- Public-sector, SaaS, enterprise, AI, website, or mobile products need a service blueprint before SRS, UX, deployment, or support planning.

## Do Not Use When

- The product is a simple self-contained feature with no operational or service dependency.
- Only a user journey is needed; use `11-experience-mapping-requirements`.
- The team cannot identify actors, channels, support roles, systems, or handoff points.

## Required Inputs

- Stakeholder register, process map, journey map, support model, current procedures, incident/support logs, and project context.
- PRD, SRS, HLD, deployment guide, runbook, or go-live plan when available.
- Regulatory, evidence, audit, or public-sector service obligations where relevant.

## Workflow

1. Define the service scenario, actors, channel, start/end event, and desired outcome.
2. Build the blueprint lanes: customer actions, frontstage interactions, backstage actions, support systems, policies, evidence, metrics, and failure/recovery.
3. Mark lines of interaction, visibility, internal action, and governance accountability.
4. Convert each handoff, wait state, failure point, evidence object, and backstage action into requirements.
5. Classify requirements as product, UX/content, workflow, support, data, security, deployment, training, maintenance, or governance.
6. Define failure recovery scripts and operational acceptance criteria.
7. Produce a service-blueprint requirement checklist and trace matrix.
8. Use `references/service-blueprint-requirement-checklist.md` before finalising.

## Quality Standards

- Every frontstage promise must have backstage ownership, support-system capability, and failure recovery.
- Requirements must specify who acts, what evidence is produced, what system state changes, and what metric proves success.
- Avoid approving a digital workflow that cannot be staffed, monitored, supported, or audited.

## Anti-Patterns

- Documenting only screens while ignoring operations and service recovery.
- Treating support scripts as optional afterthoughts.
- Omitting the physical, policy, or document evidence users rely on.

## Outputs

- Service blueprint requirements document.
- Blueprint-to-requirement trace matrix.
- Failure and recovery requirement list.
- Handoff to UX specification, HLD, deployment, runbook, go-live readiness, and evidence pack.

## References

- `references/service-blueprint-requirement-checklist.md`
<!-- dual-compat-end -->

## Output Shape

Write `projects/<ProjectName>/<phase>/<document>/service_blueprint_requirements.md` with:

1. Service scenario and blueprint scope.
2. Blueprint lane table.
3. Handoff, evidence, and failure analysis.
4. Derived requirements by type.
5. Operational acceptance and recovery scripts.
6. Trace matrix and unresolved service risks.


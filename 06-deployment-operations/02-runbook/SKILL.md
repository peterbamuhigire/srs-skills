---
name: 02-runbook
description: Use when producing or updating service operations runbook for diagnosis, mitigation, recovery, escalation, verification, and evidence. Use deployment-guide for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Runbook Skill

<!-- dual-compat-start -->
## Use When

- Produce or update service operations runbook from approved project evidence.
- Resolve decisions about diagnosis, mitigation, recovery, escalation, verification, and evidence.
- Prepare a reviewable handoff for On-call operators and service owners.

## Do Not Use When

- The task is primarily owned by deployment-guide; route there and use this skill only for its named output.
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
| Service Operations Runbook | On-call operators and service owners | Each procedure starts from an observable symptom and ends with verified recovery or an explicit escalation. |
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
| Evidence is complete and authority is explicit | Choose the procedure from measured symptoms and blast radius and produce the full artefact. | Guess-driven production changes. |
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
- Mixing the neighbouring deployment-guide concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when each procedure starts from an observable symptom and ends with verified recovery or an explicit escalation.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

This is the second skill in Phase 06 (Deployment & Operations). It produces an operational runbook that defines service overview, incident severity levels, incident response procedures, alert response playbooks, escalation matrices, troubleshooting recipes, and maintenance procedures. The output follows SRE best practices (Google SRE Book) and serves as the primary on-call reference for operations teams during incidents and routine maintenance.

## When to Use

- After 01-deployment-guide completes and `Deployment_Guide.md` exists in `projects/<ProjectName>/<phase>/<document>/`.
- When `HLD.md` exists in `projects/<ProjectName>/<phase>/<document>/` with system architecture and component dependencies.
- When `tech_stack.md` is present in `projects/<ProjectName>/_context/` with technology choices and runtime details.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/_context/tech_stack.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Runbook.md` |
| **Tone**    | Procedural, actionable, on-call-facing |
| **Standard** | SRE Best Practices (Google SRE Book) |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes | System architecture, component dependencies, service boundaries |
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes | Technology choices, runtime details, infrastructure tooling |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Runbook.md | `projects/<ProjectName>/<phase>/<document>/Runbook.md` | Complete operational runbook with incident response, playbooks, and maintenance procedures |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `projects/<ProjectName>/<phase>/<document>/` and `tech_stack.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define Service Overview

Document the operational profile of each service component:
- Component name, purpose, and owner
- Dependencies (upstream and downstream services)
- SLAs and SLOs (reference `quality_standards.md` if available)
- Critical data flows and failure domains

### Step 3: Define Incident Severity Levels

Establish severity classifications with response time targets:
- **SEV1:** Complete service outage or data loss -- response within 15 minutes
- **SEV2:** Major feature degradation affecting most users -- response within 30 minutes
- **SEV3:** Minor feature degradation affecting some users -- response within 2 hours
- **SEV4:** Cosmetic issues or minor bugs -- response within 1 business day

### Step 4: Define Incident Response Procedure

Document the five-phase incident lifecycle:
- **Detect:** How the incident is identified (monitoring alert, user report, automated check)
- **Triage:** Severity classification, impact assessment, initial communication
- **Mitigate:** Immediate actions to reduce impact (failover, rollback, feature flag toggle)
- **Resolve:** Root cause identification and permanent fix
- **Postmortem:** Blameless review, timeline reconstruction, action items

### Step 5: Define Alert Response Playbooks

For each critical metric, define an alert response playbook:
- CPU utilization (warning at 70%, critical at 90%)
- Memory utilization (warning at 75%, critical at 90%)
- Disk utilization (warning at 80%, critical at 95%)
- Response time (warning at 2x baseline, critical at 5x baseline)
- Error rate (warning at 1%, critical at 5%)
- Each playbook shall include diagnostic commands and remediation steps

### Step 6: Define Escalation Matrix

Document who to contact per severity level:
- On-call engineer (SEV1-SEV4 first responder)
- Team lead (SEV1-SEV2 escalation)
- Engineering manager (SEV1 escalation after 30 minutes)
- VP Engineering / CTO (SEV1 escalation after 1 hour)
- Include contact methods (Slack channel, phone, PagerDuty)

### Step 7: Define Troubleshooting Recipes and Maintenance Procedures

Document common troubleshooting scenarios:
- Database connection pool exhaustion
- Out-of-memory errors
- Deployment failure recovery
- Certificate expiration
Document routine maintenance:
- Planned downtime procedures
- Certificate rotation
- Log rotation and archival
- Database maintenance (vacuum, reindex)

### Step 8: Write Output

Write the completed document to `projects/<ProjectName>/<phase>/<document>/Runbook.md`. Include a contact list appendix. Log the total count of playbooks, troubleshooting recipes, and maintenance procedures.

## Output Format

The generated `Runbook.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Service Overview, 2. Incident Severity Levels, 3. Incident Response Procedure, 4. Alert Response Playbooks, 5. Escalation Matrix, 6. Troubleshooting Recipes, 7. Maintenance Procedures, 8. Contact List.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Playbooks without diagnostic commands | Every alert playbook shall include at least one diagnostic command |
| Missing escalation timelines | Every severity level shall define a maximum response time |
| Troubleshooting recipes without resolution steps | Every recipe shall end with a verified resolution action |
| No postmortem template | Incident response shall include a postmortem process with action items |

## Verification Checklist

- [ ] `Runbook.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all eight sections populated.
- [ ] Service overview lists all components from HLD with dependencies.
- [ ] Incident severity levels define SEV1 through SEV4 with response time targets.
- [ ] Alert response playbooks exist for CPU, memory, disk, response time, and error rate.
- [ ] Escalation matrix defines contacts for every severity level.
- [ ] Troubleshooting recipes cover database, memory, deployment, and certificate issues.
- [ ] Maintenance procedures cover planned downtime, log rotation, and certificate rotation.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 01-deployment-guide | Consumes deployment context for rollback procedures |
| Upstream | Phase 03 (01-high-level-design) | Consumes `HLD.md` for component topology |
| Parallel | 03-monitoring-setup | Alert definitions inform playbook thresholds |
| Downstream | 04-infrastructure-docs | Feeds operational context into infrastructure documentation |

## Standards

- **SRE Best Practices** -- Google Site Reliability Engineering. Governs incident response, SLOs, error budgets, and operational procedures.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step runbook generation logic.
- `README.md` -- Quick-start guide for this skill.

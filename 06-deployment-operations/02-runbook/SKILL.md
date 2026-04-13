---
name: "runbook"
description: "Generate an operational runbook with incident response procedures, monitoring alert responses, escalation paths, and common fix recipes following SRE best practices."
metadata:
  use_when: "Use when the task matches runbook skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Runbook Skill

## Overview

This is the second skill in Phase 06 (Deployment & Operations). It produces an operational runbook that defines service overview, incident severity levels, incident response procedures, alert response playbooks, escalation matrices, troubleshooting recipes, and maintenance procedures. The output follows SRE best practices (Google SRE Book) and serves as the primary on-call reference for operations teams during incidents and routine maintenance.

## When to Use

- After 01-deployment-guide completes and `Deployment_Guide.md` exists in `../output/`.
- When `HLD.md` exists in `../output/` with system architecture and component dependencies.
- When `tech_stack.md` is present in `../project_context/` with technology choices and runtime details.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/HLD.md`, `../project_context/tech_stack.md` |
| **Output**  | `../output/Runbook.md` |
| **Tone**    | Procedural, actionable, on-call-facing |
| **Standard** | SRE Best Practices (Google SRE Book) |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `../output/HLD.md` | Yes | System architecture, component dependencies, service boundaries |
| tech_stack.md | `../project_context/tech_stack.md` | Yes | Technology choices, runtime details, infrastructure tooling |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Runbook.md | `../output/Runbook.md` | Complete operational runbook with incident response, playbooks, and maintenance procedures |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `../output/` and `tech_stack.md` from `../project_context/`. Log the absolute path of each file read. Halt if any required file is missing.

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

Write the completed document to `../output/Runbook.md`. Include a contact list appendix. Log the total count of playbooks, troubleshooting recipes, and maintenance procedures.

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

- [ ] `Runbook.md` exists in `../output/` with all eight sections populated.
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

---
name: 03-monitoring-setup
description: Use when producing or updating monitoring and alerting specification for service indicators, dashboards, alerts, ownership, and runbook links. Use slo-and-error-budget for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Monitoring Setup Skill

<!-- dual-compat-start -->
## Use When

- Produce or update monitoring and alerting specification from approved project evidence.
- Resolve decisions about service indicators, dashboards, alerts, ownership, and runbook links.
- Prepare a reviewable handoff for SRE and service owners.

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
| Monitoring And Alerting Specification | SRE and service owners | Each user-impacting failure has a measurable signal, actionable alert, owner, threshold rationale, and runbook. |
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
| Evidence is complete and authority is explicit | Choose alerts from user impact and SLO burn, not raw metric availability and produce the full artefact. | Noisy alerts without an operator action. |
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

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when each user-impacting failure has a measurable signal, actionable alert, owner, threshold rationale, and runbook.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
> **SaaS mode:** if the project is a multi-tenant SaaS, apply `references/saas-monitoring-addendum.md` in addition to the generic steps below.


## Overview

This is the third skill in Phase 06 (Deployment & Operations). It produces monitoring and alerting design documentation that defines a metrics catalog, alert thresholds tied to SLAs, dashboard specifications, health check endpoints, log aggregation strategy, and on-call notification rules. The output conforms to ISO/IEC 25010 (Reliability, Performance Efficiency) and ensures the system is observable in production.

## When to Use

- After 01-deployment-guide completes and the deployment topology is established.
- When `HLD.md` exists in `projects/<ProjectName>/<phase>/<document>/` with component architecture for per-component metric definition.
- When `quality_standards.md` is present in `projects/<ProjectName>/_context/` with SLAs and quality targets.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/_context/quality_standards.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Monitoring_Setup.md` |
| **Tone**    | Technical, observability-focused, SRE-facing |
| **Standard** | ISO/IEC 25010 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes | Component architecture for per-component metric definition |
| quality_standards.md | `projects/<ProjectName>/_context/quality_standards.md` | Yes | SLAs, SLOs, and quality targets for alert threshold derivation |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Monitoring_Setup.md | `projects/<ProjectName>/<phase>/<document>/Monitoring_Setup.md` | Complete monitoring design with metrics, alerts, dashboards, and health checks |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `projects/<ProjectName>/<phase>/<document>/` and `quality_standards.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define Key Metrics per Component

For each component in HLD.md, define the metrics to collect:
- **Infrastructure metrics:** CPU utilization, memory utilization, disk I/O, network throughput
- **Application metrics:** Request rate, error rate, response latency (p50, p95, p99)
- **Business metrics:** Active users, transaction volume, conversion rate
- Each metric shall specify name, type (counter, gauge, histogram), unit, and collection interval
- **Delivery metrics:** deployment frequency, change lead time, change failure rate, mean time to restore, release marker visibility
- **Queue and worker metrics:** queue depth, job age, failed jobs, retry rate, dead-letter count where asynchronous processing exists

### Step 3: Define Alert Thresholds

For each metric, define warning and critical thresholds derived from `quality_standards.md` SLAs:
- Warning threshold: early indicator requiring attention
- Critical threshold: breach of SLA requiring immediate action
- Each alert shall specify evaluation window, aggregation method, and notification channel
- Thresholds shall align with SLOs defined in quality_standards.md
- Classify every alert as page, ticket, or dashboard-only. Page only when there is a clear operator action or customer-impact risk.

### Step 4: Define Dashboard Specifications

Design monitoring dashboards for different audiences:
- **Executive dashboard:** SLA compliance, uptime, error budget remaining
- **Operations dashboard:** Real-time system health, active alerts, resource utilization
- **Service dashboard:** Per-service request rate, latency, error rate (RED metrics)
- Each dashboard shall specify panels, data sources, refresh interval, and layout

### Step 5: Define Health Check Endpoints

For each service component, define health check endpoints:
- Endpoint path (e.g., `/health`, `/ready`, `/live`)
- Check type (liveness, readiness, startup)
- Expected response format and status codes
- Check interval and timeout values
- Dependency checks (database connectivity, external service availability)

### Step 6: Define Log Aggregation Strategy

Document the log collection and analysis approach:
- Log format standard (structured JSON with timestamp, level, service, trace ID)
- Log collection pipeline (agent, aggregator, storage)
- Log retention policy per environment
- Log-based alerting rules for error patterns

### Step 7: Define Notification Rules and Write Output

Document on-call notification configuration:
- Notification channels per alert severity (Slack, PagerDuty, email, SMS)
- Notification routing rules (which team receives which alerts)
- Notification deduplication and suppression rules
- Escalation timers for unacknowledged alerts
Write the completed document to `projects/<ProjectName>/<phase>/<document>/Monitoring_Setup.md`. Log the total count of metrics, alerts, and dashboard panels.

## Output Format

The generated `Monitoring_Setup.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Metrics Catalog, 2. Alert Definitions, 3. Dashboard Specifications, 4. Health Checks, 5. Log Aggregation, 6. Notification Rules.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Metrics without units or collection intervals | Every metric shall specify unit and collection interval |
| Alert thresholds not tied to SLAs | Every critical threshold shall reference a specific SLA or SLO |
| Noisy alerts with no owner | Every paging alert shall have an owner, action, runbook link, and escalation path |
| Dashboards without refresh intervals | Every dashboard shall specify its refresh interval |
| Health checks without timeout values | Every health check shall define check interval and timeout |

## Verification Checklist

- [ ] `Monitoring_Setup.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all six sections populated.
- [ ] Metrics catalog covers infrastructure, application, and business metrics per component.
- [ ] Alert definitions include warning and critical thresholds tied to SLAs.
- [ ] Dashboard specifications define panels with data sources and refresh intervals.
- [ ] Health check endpoints exist for every service with liveness and readiness checks.
- [ ] Log aggregation defines format standard, pipeline, and retention policy.
- [ ] Notification rules map alert severity to notification channels.
- [ ] Alerts distinguish page-worthy customer impact from ticket or dashboard-only signals.
- [ ] Dashboards include release markers and delivery-system metrics where production deployment is in scope.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 01-deployment-guide | Consumes deployment topology for monitoring scope |
| Upstream | Phase 03 (01-high-level-design) | Consumes `HLD.md` for component architecture |
| Parallel | 02-runbook | Alert definitions inform runbook playbook thresholds |
| Downstream | 04-infrastructure-docs | Feeds monitoring architecture into infrastructure documentation |

## Standards

- **ISO/IEC 25010** -- Systems and Software Quality Requirements and Evaluation. Governs reliability and performance efficiency quality characteristics used for metric and threshold definition.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step monitoring setup generation logic.
- `README.md` -- Quick-start guide for this skill.

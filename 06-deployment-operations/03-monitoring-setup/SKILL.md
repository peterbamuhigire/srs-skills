---
name: "monitoring-setup"
description: "Generate monitoring and alerting design documentation with metrics definitions, alert thresholds, dashboard specifications, and health check endpoints per ISO/IEC 25010."
metadata:
  use_when: "Use when the task matches monitoring setup skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Monitoring Setup Skill

## Overview

This is the third skill in Phase 06 (Deployment & Operations). It produces monitoring and alerting design documentation that defines a metrics catalog, alert thresholds tied to SLAs, dashboard specifications, health check endpoints, log aggregation strategy, and on-call notification rules. The output conforms to ISO/IEC 25010 (Reliability, Performance Efficiency) and ensures the system is observable in production.

## When to Use

- After 01-deployment-guide completes and the deployment topology is established.
- When `HLD.md` exists in `../output/` with component architecture for per-component metric definition.
- When `quality_standards.md` is present in `../project_context/` with SLAs and quality targets.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/HLD.md`, `../project_context/quality_standards.md` |
| **Output**  | `../output/Monitoring_Setup.md` |
| **Tone**    | Technical, observability-focused, SRE-facing |
| **Standard** | ISO/IEC 25010 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `../output/HLD.md` | Yes | Component architecture for per-component metric definition |
| quality_standards.md | `../project_context/quality_standards.md` | Yes | SLAs, SLOs, and quality targets for alert threshold derivation |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Monitoring_Setup.md | `../output/Monitoring_Setup.md` | Complete monitoring design with metrics, alerts, dashboards, and health checks |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `../output/` and `quality_standards.md` from `../project_context/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define Key Metrics per Component

For each component in HLD.md, define the metrics to collect:
- **Infrastructure metrics:** CPU utilization, memory utilization, disk I/O, network throughput
- **Application metrics:** Request rate, error rate, response latency (p50, p95, p99)
- **Business metrics:** Active users, transaction volume, conversion rate
- Each metric shall specify name, type (counter, gauge, histogram), unit, and collection interval

### Step 3: Define Alert Thresholds

For each metric, define warning and critical thresholds derived from `quality_standards.md` SLAs:
- Warning threshold: early indicator requiring attention
- Critical threshold: breach of SLA requiring immediate action
- Each alert shall specify evaluation window, aggregation method, and notification channel
- Thresholds shall align with SLOs defined in quality_standards.md

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
Write the completed document to `../output/Monitoring_Setup.md`. Log the total count of metrics, alerts, and dashboard panels.

## Output Format

The generated `Monitoring_Setup.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Metrics Catalog, 2. Alert Definitions, 3. Dashboard Specifications, 4. Health Checks, 5. Log Aggregation, 6. Notification Rules.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Metrics without units or collection intervals | Every metric shall specify unit and collection interval |
| Alert thresholds not tied to SLAs | Every critical threshold shall reference a specific SLA or SLO |
| Dashboards without refresh intervals | Every dashboard shall specify its refresh interval |
| Health checks without timeout values | Every health check shall define check interval and timeout |

## Verification Checklist

- [ ] `Monitoring_Setup.md` exists in `../output/` with all six sections populated.
- [ ] Metrics catalog covers infrastructure, application, and business metrics per component.
- [ ] Alert definitions include warning and critical thresholds tied to SLAs.
- [ ] Dashboard specifications define panels with data sources and refresh intervals.
- [ ] Health check endpoints exist for every service with liveness and readiness checks.
- [ ] Log aggregation defines format standard, pipeline, and retention policy.
- [ ] Notification rules map alert severity to notification channels.

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

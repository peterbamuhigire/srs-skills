# 03-Monitoring-Setup Skill

## Objective

This skill produces monitoring and alerting design documentation that defines a metrics catalog, alert thresholds tied to SLAs, dashboard specifications, health check endpoints, log aggregation strategy, and notification rules. It ensures the system is observable in production per ISO/IEC 25010.

## Execution Steps

1. Verify `../output/HLD.md` and `../project_context/quality_standards.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates metrics catalog, alert definitions, dashboard specs, health checks, log aggregation, and notification rules, then writes `../output/Monitoring_Setup.md`.
3. Review alert thresholds to confirm each critical threshold references a specific SLA or SLO from quality_standards.md.
4. This skill runs in parallel with `02-runbook`. Once both complete, proceed to `04-infrastructure-docs`.

## Quality Reminder

Every metric shall specify name, type, unit, and collection interval. Every critical alert threshold shall reference a documented SLA or SLO. Every dashboard shall specify panels with data sources and refresh intervals. Every health check shall define liveness and readiness endpoints with timeout values. Flag monitoring gaps rather than fabricating observability details.

## Standards

- ISO/IEC 25010 (Reliability, Performance Efficiency)

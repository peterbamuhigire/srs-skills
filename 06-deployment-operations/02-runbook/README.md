# 02-Runbook Skill

## Objective

This skill produces an operational runbook that defines incident response procedures, alert response playbooks, escalation matrices, troubleshooting recipes, and maintenance procedures. It serves as the primary on-call reference for operations teams during incidents and routine maintenance, following SRE best practices.

## Execution Steps

1. Verify `projects/<ProjectName>/<phase>/<document>/HLD.md` and `projects/<ProjectName>/_context/tech_stack.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates service overview, incident severity levels, alert playbooks, escalation matrix, troubleshooting recipes, and maintenance procedures, then writes `projects/<ProjectName>/<phase>/<document>/Runbook.md`.
3. Review alert response playbooks to confirm each playbook includes diagnostic commands and remediation steps.
4. This skill runs in parallel with `03-monitoring-setup`. Once both complete, proceed to `04-infrastructure-docs`.

## Quality Reminder

Every alert playbook shall include diagnostic commands and verified remediation steps. Every severity level shall define response time targets. Troubleshooting recipes shall cover database, memory, deployment, and certificate scenarios. Flag operational gaps rather than fabricating incident procedures.

## Standards

- SRE Best Practices (Google SRE Book)

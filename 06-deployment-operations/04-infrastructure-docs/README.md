# 04-Infrastructure-Docs Skill

## Objective

This skill produces infrastructure documentation that defines architecture diagrams, compute resource specifications, network topology, storage architecture, IaC references, and backup/disaster recovery procedures. It serves as the authoritative infrastructure reference for DevOps and platform engineering teams per IEEE 1016-2009.

## Execution Steps

1. Verify `../output/HLD.md` and `../project_context/tech_stack.md` exist. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates infrastructure architecture diagram, compute resources, network topology, storage architecture, IaC references, backup/DR, and cost estimates, then writes `../output/Infrastructure_Docs.md`.
3. Review the Mermaid infrastructure diagram to confirm it renders valid syntax with directional data flows.
4. This is the final skill in Phase 06. Once complete, Phase 08 (User Documentation) can consume the infrastructure documentation.

## Quality Reminder

Every infrastructure diagram shall show directional connectivity between components. Every production compute resource shall define a scaling policy. Network topology shall include security group rules for every subnet. Backup and DR shall define RPO and RTO targets explicitly. Flag infrastructure gaps rather than fabricating resource specifications.

## Standards

- IEEE 1016-2009 (Software Design Descriptions)

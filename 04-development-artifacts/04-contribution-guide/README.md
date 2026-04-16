# 04-Contribution-Guide Skill

## Objective

This skill produces a contribution guide that standardizes the development workflow with branching strategy, commit conventions, pull request process, and code review checklist. It ensures every contribution follows a predictable, auditable process per IEEE 1074.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/tech_stack.md` exists. Halt if it is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill reads VCS and CI/CD details, generates workflow standards, and writes `projects/<ProjectName>/<phase>/<document>/Contribution_Guide.md`.
3. Review that the Getting Started section references `Dev_Environment_Setup.md` and `Coding_Guidelines.md` from prior skills in this phase.
4. This skill runs after `02-coding-guidelines` and `03-dev-environment-setup` complete, as it references their outputs.

## Quality Reminder

Every branch type shall have a naming convention with examples. Every commit type shall include a concrete example message. The PR process shall define maximum change size to prevent unreviewable contributions. CI/CD expectations shall specify numeric thresholds for coverage and quality gates.

## Standards

- IEEE 1074 (Software Life Cycle Processes)

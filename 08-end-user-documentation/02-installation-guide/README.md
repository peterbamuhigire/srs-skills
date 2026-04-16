# 02-Installation-Guide Skill

## Objective

This skill produces a comprehensive installation guide that walks end users and system administrators through system requirements, prerequisites, step-by-step installation procedures, configuration, verification, upgrading, and uninstallation. It serves as the authoritative installation reference per ISO 26514.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/tech_stack.md` exists. Optionally check for `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md`. Halt if the required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates system requirements, prerequisites, installation steps, configuration, verification, and troubleshooting, then writes `projects/<ProjectName>/<phase>/<document>/Installation_Guide.md`.
3. Review the installation steps to confirm each step includes exact commands, expected output, and platform-specific variations.
4. Proceed to other Phase 08 skills or downstream phases.

## Quality Reminder

Every installation step shall include the exact command to execute with expected console output. Every dependency shall specify a minimum version number. The guide shall include post-installation verification with at least one functional test. Flag installation gaps rather than fabricating platform-specific details.

## Standards

- ISO 26514 (User Documentation)

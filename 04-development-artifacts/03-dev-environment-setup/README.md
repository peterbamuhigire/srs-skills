# 03-Dev-Environment-Setup Skill

## Objective

This skill produces a development environment setup guide that enables any developer to establish a working local environment from scratch with numbered installation steps, configuration templates, and verification commands. It serves as the primary onboarding document for new team members per IEEE 1074.

## Execution Steps

1. Verify `../project_context/tech_stack.md` exists. Optionally check for `../output/HLD.md` to derive infrastructure dependencies.
2. Invoke `logic.prompt` or trigger the skill. The skill reads toolchain details, generates platform-specific setup steps, and writes `../output/Dev_Environment_Setup.md`.
3. Run the verification commands in the Verification Checklist section to confirm the setup guide produces a working environment.
4. This skill can run in parallel with `02-coding-guidelines`. Once both complete, proceed to `04-contribution-guide`.

## Quality Reminder

Every prerequisite shall specify an exact or minimum version number. Every installation command shall state which platform it targets. Every environment variable shall include an example value and a description. Include a Troubleshooting section that addresses at least three common setup failures.

## Standards

- IEEE 1074 (Software Life Cycle Processes)

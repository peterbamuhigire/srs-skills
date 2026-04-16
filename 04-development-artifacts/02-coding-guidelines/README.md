# 02-Coding-Guidelines Skill

## Objective

This skill produces a coding standards document that defines language-specific naming conventions, code structure patterns, anti-patterns to avoid, and quality metrics. It ensures consistent, maintainable code across the development team per IEEE 730.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/tech_stack.md` exists. Optionally check for `projects/<ProjectName>/<phase>/<document>/HLD.md` to align conventions with architectural decisions.
2. Invoke `logic.prompt` or trigger the skill. The skill detects languages and frameworks, generates conventions for each, and writes `projects/<ProjectName>/<phase>/<document>/Coding_Guidelines.md`.
3. Review that every naming convention includes compliant and non-compliant examples, and that anti-patterns include recommended alternatives.
4. This skill can run in parallel with `03-dev-environment-setup`. Once both complete, proceed to `04-contribution-guide`.

## Quality Reminder

Every naming convention shall include a concrete compliant and non-compliant example. Every anti-pattern shall name the recommended alternative. Security practices shall address injection prevention, credential handling, and data sanitization. Flag ambiguous conventions rather than leaving them open to interpretation.

## Standards

- IEEE 730 (Software Quality Assurance Plans)

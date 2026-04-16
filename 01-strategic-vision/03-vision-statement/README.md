# 03-Vision-Statement Skill

## Objective

This skill transforms raw project context (vision.md, stakeholders.md) into a formal, IEEE 29148-compliant vision document. It establishes the elevator pitch, product positioning, value propositions, and success criteria that anchor all downstream requirements and design documentation.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/vision.md` and `projects/<ProjectName>/_context/stakeholders.md` exist and are populated. Halt if vision.md is missing.
2. Invoke `logic.prompt` or trigger the skill through your runner. The skill reads context files, synthesizes strategic sections, and writes `projects/<ProjectName>/<phase>/<document>/Vision_Statement.md`.
3. Review the generated Vision_Statement.md to confirm elevator pitch uses active voice, value propositions have measurable outcomes, and success criteria follow SMART format.
4. Proceed to `01-prd-generation` to build the Product Requirements Document from this vision.

## Quality Reminder

Every statement shall be grounded in the project context files. Avoid marketing language, superlatives, and unquantified claims. If a metric or baseline is unknown, flag it explicitly rather than fabricating a value.

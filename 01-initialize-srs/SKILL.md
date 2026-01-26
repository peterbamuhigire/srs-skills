---
name: initialize-srs
description: Set up IEEE Std 830-1998 and US ISO/IEC 25051 compliant project context files so downstream SRS skills can operate with stakeholder data, quality criteria, and definitions.
---

# Initialize-SRS Skill Guidance

## Overview
Use this skill to bootstrap the parent project with industrial templates that capture vision, features, technology constraints, business rules, quality standards, and glossary definitions before running any other SRS skills. The skill provides an automation script plus template guidance so Claude can reliably seed `../project_context/` and `../output/`.

## Quick Reference
- Initialize or refresh `../project_context/` with six templates (vision, features, tech stack, business rules, quality standards, glossary).
- Ensure `../output/` exists before downstream IEEE/ISO skills execute.
- Use Maintenance Mode when existing content must stay untouched; use Clean mode only when a fresh baseline is required.

## Core Instructions
1. Run `python init_skill.py` from this directory or call the `logic.prompt` via your skill runner.
2. The automation checks for `../project_context/`. Offer Maintenance Mode (add missing templates) or Clean (delete and reseed). Maintenance Mode must never overwrite user edits.
3. After provisioning, create `../output/` if missing so downstream skills always find a writeable folder.
4. Copy templates from `templates/`. Each template embeds Expert Guidance comments, SHALL/MUST phrasing, and aligned Markdown tables. Log every directory action and template copy/skip with explicit paths (e.g., `../project_context/vision.md`).
5. After completion, echo: “The quality of the final SRS depends entirely on the technical density of these files. Avoid vague language; provide specific numbers and models.”

## Resources
- `README.md`: Skill description, ISO/IEC alignment, template list, and references.
- `init_skill.py`: Python automation that handles directory checks, Maintenance/Clean mode, template copying, and logging.
- `logic.prompt`: LLM instructions describing the desired behavior, standards references, and logging needs.
- `templates/`: Six industrial templates (`vision.md`, `features.md`, `tech_stack.md`, `business_rules.md`, `quality_standards.md`, `glossary.md`). Each contains Expert Guidance comments and placeholders for measurable data.

## Common Pitfalls
- Re-running the skill without choosing Maintenance Mode can delete effort; prefer Clean only when templates must reset.
- Skipping template population leaves downstream skills without verifiable inputs; ensure the vision, quality, and business rule files contain measurable targets before proceeding.
- Omitting the role-specific acceptance criteria in `quality_standards.md` or glossary definitions undermines ISO/IEC alignment; keep those sections updated with traceable references.

# 01-User-Manual Skill

## Objective

This skill produces a comprehensive user manual that guides end users through every feature of the software product with step-by-step procedures, screenshot placeholders, navigation overviews, and role-based workflow instructions. It serves as the primary reference for end users adopting the system per ISO 26514.

## Execution Steps

1. Verify `projects/<ProjectName>/_context/vision.md` and `projects/<ProjectName>/_context/features.md` exist. Optionally check for `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` and `projects/<ProjectName>/<phase>/<document>/user_stories.md`. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates getting started content, navigation overview, per-feature guides, role-based workflows, troubleshooting, and glossary, then writes `projects/<ProjectName>/<phase>/<document>/User_Manual.md`.
3. Review the feature guides to confirm each feature has numbered steps, screenshot placeholders, and expected results.
4. Proceed to `03-faq` which can reference the user manual for cross-linking.

## Quality Reminder

Every feature in `features.md` shall have a corresponding feature guide with numbered steps and screenshot placeholders. Role-based workflows shall cover every identified user role. The glossary shall define every acronym and technical term. Flag documentation gaps rather than fabricating user-facing instructions.

## Standards

- ISO 26514 (User Documentation)

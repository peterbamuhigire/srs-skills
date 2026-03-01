# 03-FAQ Skill

## Objective

This skill produces a structured Frequently Asked Questions document organized by category with clear question-answer pairs, cross-references to the user manual and installation guide, and search-friendly formatting. It serves as a quick-reference resource that reduces support burden by addressing common user inquiries proactively per ISO 26514.

## Execution Steps

1. Verify `../project_context/vision.md` and `../project_context/features.md` exist. Optionally check for `../output/User_Manual.md`. Halt if any required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates categorized question-answer pairs covering general, installation, feature-specific, account, troubleshooting, and security topics, then writes `../output/FAQ.md`.
3. Review the FAQ entries to confirm each answer is concise, actionable, and cross-references detailed documentation where applicable.
4. Iterate if feature coverage is incomplete or answers lack specificity.

## Quality Reminder

Every answer shall provide a concrete action or fact within three to five sentences. Answers describing procedures shall cross-reference the relevant User Manual or Installation Guide section. Questions shall be derived from actual product features and documented scope, not fabricated. Flag gaps in source material rather than inventing answers.

## Standards

- ISO 26514 (User Documentation)

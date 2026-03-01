# 04-Release-Notes Skill

## Objective

This skill produces a reusable release notes template that standardizes how version changes are communicated to end users, including release highlights, new features, improvements, bug fixes, breaking changes, migration instructions, known issues, and a compatibility matrix. It provides a repeatable format the development team can populate for each release cycle per IEEE 830.

## Execution Steps

1. Verify `../project_context/vision.md` exists. Optionally check for `../output/SRS_Draft.md`. Halt if the required file is missing.
2. Invoke `logic.prompt` or trigger the skill. The skill generates a release notes template with all standard sections, authoring guidance, and a pre-publish checklist, then writes `../output/Release_Notes_Template.md`.
3. Review the template to confirm each section includes entry format guidance and placeholder examples.
4. Distribute the template to the development team for use in upcoming release cycles.

## Quality Reminder

Release notes entries shall describe user-facing impact, not implementation details or code changes. Every breaking change shall include a concrete migration action the user must take. Known issues shall include severity classification and workarounds where available. Flag gaps in versioning context rather than fabricating release details.

## Standards

- IEEE 830 (Software Requirements Specifications)

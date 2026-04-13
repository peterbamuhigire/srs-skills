---
name: "release-notes"
description: "Generate a release notes template with version tracking, new features, bug fixes, breaking changes, migration instructions, and known issues per IEEE 830."
metadata:
  use_when: "Use when the task matches release notes skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Release Notes Skill

## Overview

This is the fourth skill in Phase 08 (End-User Documentation). It produces a release notes template that standardizes how version changes are communicated to end users, including release highlights, new features, improvements, bug fixes, breaking changes, migration instructions, and known issues. The output conforms to IEEE 830 and provides a reusable template that the development team can populate for each release cycle.

## When to Use This Skill

- After `vision.md` exists in `../project_context/` to establish the product identity and versioning context.
- When the project requires a standardized format for communicating changes to end users.
- Optionally after `SRS_Draft.md` exists in `../output/` for tracing features to requirements.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `../project_context/vision.md`, `../output/SRS_Draft.md` (optional) |
| **Output**   | `../output/Release_Notes_Template.md` |
| **Tone**     | Professional, concise, user-facing |
| **Standard** | IEEE 830 |
| **Time**     | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `../project_context/vision.md` | Yes | Product name, versioning scheme, release cadence context |
| SRS_Draft.md | `../output/SRS_Draft.md` | No | Functional requirements for tracing features to specifications |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Release_Notes_Template.md | `../output/Release_Notes_Template.md` | Reusable release notes template with all standard sections and placeholder guidance |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `../project_context/`. Optionally read `SRS_Draft.md` from `../output/`. Log the absolute path of each file read. Halt if the required file is missing.

### Step 2: Define Version and Date Header

Produce a header template with:
- Product name and version number placeholder (e.g., `v[MAJOR].[MINOR].[PATCH]`)
- Release date placeholder
- Release type classification (Major, Minor, Patch, Hotfix)
- Semantic versioning guidance for the development team

### Step 3: Generate Release Highlights Section

Define a template section for release highlights:
- Two to three sentence executive summary of the release
- Guidance that highlights SHALL focus on user-facing impact, not implementation details
- Placeholder format for highlight bullet points

### Step 4: Generate New Features Section

Define a template section for new features:
- Per-feature entry format: feature name, description, user benefit, related requirement ID (if SRS exists)
- Screenshot or demo link placeholder per feature
- Guidance that each feature entry SHALL describe what the user can now do, not how it was implemented

### Step 5: Generate Improvements and Bug Fixes Sections

Define template sections for improvements and bug fixes:
- Improvement entry format: area of improvement, description of change, user impact
- Bug fix entry format: issue ID (if applicable), description of the bug, resolution, affected versions
- Guidance that bug fix descriptions SHALL describe the symptom the user experienced, not the code change

### Step 6: Generate Breaking Changes and Migration Guide Sections

Define template sections for breaking changes and migration:
- Breaking change entry format: what changed, why, migration action required
- Migration guide format: numbered steps to transition from previous version
- Guidance that every breaking change SHALL include a concrete migration action
- Deprecation notices with timeline for removal

### Step 7: Generate Known Issues and Compatibility Matrix

Define template sections for known issues and compatibility:
- Known issue entry format: description, severity, workaround (if available), expected fix version
- Compatibility matrix template: OS versions, browser versions, dependency versions tested
- Guidance that known issues SHALL include severity classification (Critical, High, Medium, Low)

### Step 8: Assemble Template and Write Output

Assemble all sections into the final template with authoring instructions embedded as comments. Include a checklist at the end for release managers to verify completeness before publishing. Write the completed template to `../output/Release_Notes_Template.md`. Log completion.

## Output Format Specification

The generated `Release_Notes_Template.md` SHALL contain these sections in order:

1. **Version & Date** -- Product name, version, release date, release type
2. **Release Highlights** -- Executive summary of the release
3. **New Features** -- Per-feature entries with descriptions and user benefit
4. **Improvements** -- Enhancements to existing functionality
5. **Bug Fixes** -- Resolved issues with symptom descriptions
6. **Breaking Changes** -- Changes that require user action
7. **Migration Guide** -- Step-by-step transition instructions
8. **Known Issues** -- Unresolved issues with severity and workarounds
9. **Deprecation Notices** -- Features scheduled for future removal
10. **Compatibility Matrix** -- Tested platform and dependency versions

## Common Pitfalls

- **Implementation-focused language:** Entries SHALL describe user-facing impact, not code changes or internal refactoring.
- **Missing migration actions:** Every breaking change SHALL include a concrete step the user must take.
- **No severity on known issues:** Every known issue SHALL include a severity classification.
- **Missing version context:** The template SHALL include semantic versioning guidance for consistent version numbering.
- **No completeness checklist:** The template SHALL include a pre-publish checklist for release managers.

## Verification Checklist

1. `Release_Notes_Template.md` exists in `../output/` with all ten sections.
2. Version header includes semantic versioning guidance and release type classification.
3. New Features section template includes user benefit and requirement traceability fields.
4. Breaking Changes section template requires a migration action for each entry.
5. Known Issues section template includes severity classification.
6. Compatibility matrix template covers OS, browser, and dependency versions.
7. Pre-publish checklist is present at the end of the template.
8. Authoring guidance comments are embedded in each section.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 02 (Requirements Engineering) | Consumes `vision.md` for product identity and versioning context |
| Upstream | Phase 02 (SRS Draft) | Optionally consumes `SRS_Draft.md` for requirement traceability |
| Downstream | Phase 09 (Compliance) | Release notes feed compliance documentation for change tracking |

## Standards Compliance

- **IEEE 830** -- Recommended Practice for Software Requirements Specifications. Governs traceability of features to requirements and structured documentation of changes.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step release notes template generation logic.
- `README.md` -- Quick-start guide for this skill.

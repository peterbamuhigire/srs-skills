---
name: user-manual
description: Generate a comprehensive user manual covering all features with step-by-step procedures, navigation guides, and role-based usage instructions per ISO 26514.
---

# User Manual Skill

## Overview

This is the first skill in Phase 08 (End-User Documentation). It produces a comprehensive user manual that guides end users through every feature of the software product with step-by-step procedures, screenshot placeholders, navigation overviews, and role-based workflow instructions. The output conforms to ISO 26514 (User Documentation) and serves as the primary reference for end users adopting the system.

## When to Use This Skill

- After Phase 02 completes and `vision.md` and `features.md` exist in `../project_context/`.
- When end users require a structured guide to learn and operate the software product.
- Optionally after Phase 05 when `user_stories.md` exists in `../output/` for richer workflow context.
- Optionally after Phase 02 when `SRS_Draft.md` exists in `../output/` for detailed functional reference.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `../project_context/vision.md`, `../project_context/features.md`, `../output/SRS_Draft.md` (optional), `../output/user_stories.md` (optional) |
| **Output**   | `../output/User_Manual.md` |
| **Tone**     | Instructional, user-facing, task-oriented |
| **Standard** | ISO 26514 |
| **Time**     | 15-25 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `../project_context/vision.md` | Yes | Product purpose, target audience, high-level goals |
| features.md | `../project_context/features.md` | Yes | Feature list with descriptions for per-feature guide generation |
| SRS_Draft.md | `../output/SRS_Draft.md` | No | Detailed functional requirements for precise procedure steps |
| user_stories.md | `../output/user_stories.md` | No | User stories and personas for role-based workflow generation |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| User_Manual.md | `../output/User_Manual.md` | Complete user manual with getting started, feature guides, role-based workflows, troubleshooting, and glossary |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` and `features.md` from `../project_context/`. Optionally read `SRS_Draft.md` and `user_stories.md` from `../output/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define Getting Started Section

Document the onboarding experience for a first-time user:
- System access procedures (login, registration, initial setup)
- First-run configuration or wizard steps
- Orientation to the primary interface layout
- Quick-start task that demonstrates core value within five minutes

### Step 3: Generate Navigation Overview

Produce a navigation map of the application:
- Primary navigation elements (menus, sidebars, toolbars) with screenshot placeholders
- Page-by-page or screen-by-screen summary with purpose description
- Navigation shortcuts and keyboard accelerators if applicable

### Step 4: Generate Feature Guides

For each feature in `features.md`, produce a dedicated section:
- Feature purpose and user benefit (one to two sentences)
- Step-by-step procedure with numbered instructions
- Screenshot placeholders formatted as `![Feature Name - Step N](screenshots/feature-name-step-n.png)`
- Expected results after each critical step
- Edge cases and limitations the user should be aware of

### Step 5: Generate Role-Based Workflows

If `user_stories.md` is present, define workflows per user role:
- Identify distinct user roles from stories or personas
- Map each role to its permitted features and typical task sequences
- Produce end-to-end workflow walkthroughs for each role
- If no user stories exist, generate workflows based on features.md feature groupings

### Step 6: Generate Troubleshooting Section

Document common user-facing issues and resolutions:
- Error message catalog with plain-language explanations and resolution steps
- Frequently encountered obstacles during onboarding
- Performance or display issues with recommended actions
- Escalation path for unresolved issues (support contact, ticket system)

### Step 7: Generate Glossary

Compile a glossary of domain-specific and product-specific terms:
- Every acronym and abbreviation used in the manual SHALL be expanded
- Technical terms SHALL include user-friendly definitions
- Terms SHALL be sorted alphabetically

### Step 8: Assemble and Write Output

Assemble all sections into the final document with a table of contents. Write the completed document to `../output/User_Manual.md`. Log the total count of feature guides and role-based workflows generated.

## Output Format Specification

The generated `User_Manual.md` SHALL contain these sections in order:

1. **Document Header** -- Product name, version, date, audience, standards reference
2. **Table of Contents** -- Auto-navigable section links
3. **Getting Started** -- First-time user onboarding and quick-start
4. **Navigation Overview** -- Interface map with screenshot placeholders
5. **Feature Guides** -- Per-feature step-by-step procedures
6. **Role-Based Workflows** -- End-to-end task sequences per user role
7. **Troubleshooting** -- Error catalog and resolution steps
8. **Glossary** -- Alphabetical term definitions
9. **Support & Contact** -- Escalation paths and contact information

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in this document's directory listing the section files in the correct assembly order:

```markdown
# Document Manifest — User Manual
# Generated by user-manual. Edit to reorder or exclude sections before building.
01-getting-started.md
02-navigation-overview.md
03-feature-guides.md
04-role-based-workflows.md
05-troubleshooting.md
06-glossary.md
07-support.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Common Pitfalls

- **Jargon without definition:** Every technical term SHALL appear in the glossary with a user-friendly definition.
- **Missing screenshot placeholders:** Every multi-step procedure SHALL include at least one screenshot placeholder per critical step.
- **Role-agnostic instructions:** Workflows SHALL be segmented by user role when multiple roles exist.
- **Assumed prior knowledge:** The Getting Started section SHALL assume zero familiarity with the product.
- **Missing error guidance:** Every known error state SHALL have a documented resolution path.

## Verification Checklist

1. `User_Manual.md` exists in `../output/` with all nine sections populated.
2. Getting Started section assumes zero prior knowledge and includes a quick-start task.
3. Every feature in `features.md` has a corresponding feature guide section.
4. Screenshot placeholders follow the `![Name - Step](screenshots/...)` format.
5. Role-based workflows cover every identified user role.
6. Troubleshooting section includes error messages with resolution steps.
7. Glossary contains every acronym and technical term used in the manual.
8. Table of contents links match actual section headings.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 02 (Requirements Engineering) | Consumes `vision.md` and `features.md` for product scope |
| Upstream | Phase 05 (Testing Documentation) | Consumes `user_stories.md` for role-based workflows |
| Downstream | 03-faq | FAQ generation references the user manual for cross-linking |
| Downstream | Phase 09 (Compliance) | User manual feeds compliance documentation traceability |

## Standards Compliance

- **ISO 26514** -- Systems and Software Engineering -- Requirements for Designers and Developers of User Documentation. Governs structure, completeness, and audience-appropriateness of user-facing documentation.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step user manual generation logic.
- `README.md` -- Quick-start guide for this skill.

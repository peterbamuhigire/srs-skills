# Phase 08: End-User Documentation

## Purpose

Generate user-facing documentation that enables end users to install, operate, troubleshoot, and stay informed about the software product per ISO 26514 and IEEE 830 standards.

## Skills in This Phase

| Order | Skill | Output | Standard |
|-------|-------|--------|----------|
| 1 | 01-user-manual | User_Manual.md | ISO 26514 |
| 2 | 02-installation-guide | Installation_Guide.md | ISO 26514 |
| 3 | 03-faq | FAQ.md | ISO 26514 |
| 4 | 04-release-notes | Release_Notes_Template.md | IEEE 830 |

## Execution Order

Skills 01-04 are independent. User manual and installation guide are typically generated first as they are most critical for end users.

## Dependencies

- **Upstream:** Phase 03 (Design Documentation) provides architectural context for installation guides. Phase 06 (Deployment & Operations) provides `Deployment_Guide.md` for installation procedures and operational context.
- **Downstream:** Phase 09 (Compliance Documentation) consumes release notes and user-facing docs for regulatory traceability.

## I/O

All skills read from `../output/` (SRS_Draft.md, Deployment_Guide.md, user_stories.md) and `../project_context/` (vision.md, features.md, tech_stack.md). All skills write to `../output/`.

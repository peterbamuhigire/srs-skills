---
name: descriptive-modeling
description: Build Section 2.0 by analyzing tech_stack.md, features.md, and quality_standards.md to describe product perspective, functions, users, constraints, and dependencies with ISO/IEEE rigor.
---

# Descriptive Modeling Skill Guidance

## Overview
Invoke this skill after initializing the project context and generating Section 1.0. It reads the technology stack, feature set, and quality standards to produce Section 2.0 (Descriptive Modeling) with technical realism, block diagram descriptions, and constraint traceability.

## Quick Reference
- Inputs: `../project_context/tech_stack.md`, `../project_context/features.md`, `../project_context/quality_standards.md`
- Output: `../output/SRS_Draft.md` (Section 2.0 only)
- Tone: Engineering prose using SHALL statements; System Block Diagram descriptions must mention actual infrastructure components (OCI, HP Z440, MySQL 8.0, etc.).

## Core Instructions
1. Run `python descriptive_modeling.py` from this directory or trigger `logic.prompt` through your skill runner.
2. The script analyzes the tech stack keywords, groups features into Major Capability buckets, reads quality constraints, and writes Section 2.0 with subsections 2.1–2.5.
3. Ensure the script replaces any existing Section 2.0 block in `../output/SRS_Draft.md` and leaves the rest of the document untouched.
4. Verify the new section includes System Interfaces, User Interfaces, Hardware Interfaces, Memory Constraints, Product Functions, User Characteristics, Constraints (including ISO/IEC 25051 and Uganda environmental factors), and Assumptions/Dependencies.
5. Confirm Section 2.0 references the governance standards and maintains traceability back to vision-derived stakeholder needs.

## Resources
- `README.md`: Skill intent, environmental mapping, and quality reminders.
- `descriptive_modeling.py`: Automation script that synthesizes Section 2.0.
- `logic.prompt`: Meta instructions for language models to orchestrate the process with the required tone and logging.

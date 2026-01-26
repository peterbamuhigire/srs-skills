---
name: context-engineering
description: Synthesize Section 1.0 (Introduction) by reading vision.md and glossary.md, and write a standardized SRS Draft that captures purpose, scope, definitions, references, and overview with ISO/IEEE rigor.
---

# Context Engineering Skill Guidance

## Overview
Use this skill once the project context templates have been populated. It turns `vision.md` and `glossary.md` into Section 1.0 of the SRS, emphasizing the legal/technical boundaries, definitions, and governing standards before downstream requirements are generated.

## Quick Reference
- Input files: `../project_context/vision.md`, `../project_context/glossary.md`
- Output file: `../output/SRS_Draft.md` (Section 1.0 only)
- Tone: Standardized Document Header + active engineering prose; avoid conversational phrases.
- Traceability: Each scope bullet must refer back to a Stakeholder Need entry in `vision.md`.

## Core Instructions
1. Run `python context_engineering.py` from within this directory or trigger the `logic.prompt` via your skill runner.
2. The script reads the problem statement, stakeholder needs, and system constraints to separate Business Intent from Technical Scope, then builds Section 1.0 with the required subsections.
3. The glossary table drives Section 1.3 (Definitions, Acronyms, and Abbreviations) so that IEEE 610.12 and ISO/IEC 15504-1 terms are standardized and unambiguous.
4. References include the required IEEE and ISO/IEC standards plus the project context files used for traceability.
5. Always keep the Standardized Document Header in place; do not allow the section to drift into conversational or promotional language.
6. Validate that `../output/SRS_Draft.md` exists and contains the new introduction before closing the skill run.

## Resources
- `README.md`: Provides the synthesis intent for this skill.
- `context_engineering.py`: The automation script that performs the extraction, synthesis, and file writing described above.
- `logic.prompt`: Instructions for Claude to orchestrate this skill with the required tone, standards, and logging.

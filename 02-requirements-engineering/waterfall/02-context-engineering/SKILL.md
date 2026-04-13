---
name: "context-engineering"
description: "Synthesize Section 1.0 (Introduction) by reading vision.md and glossary.md, and write a standardized SRS Draft that captures purpose, scope, definitions, references, and overview with ISO/IEEE rigor."
metadata:
  use_when: "Use when the task matches context engineering skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt`, local scripts when deeper detail is needed."
---

> **[MISSING FILE FALLBACK]**
> This skill references auxiliary files (`logic.prompt`, Python scripts) for automated execution.
> **If those files are unavailable in your environment**, Claude can execute this skill directly:
> 1. Read all files in `projects/<ProjectName>/_context/`
> 2. Follow the step-by-step instructions in the **Manual Execution** section below (or ask Claude to generate the relevant SRS section by describing the context inline)
> 3. Write output to `projects/<ProjectName>/02-requirements-engineering/01-srs/<section-file>.md`
>
> _This skill is fully executable without Python or logic.prompt by providing context directly to Claude._

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

### Out of Scope

The following items are explicitly **excluded** from this project's scope. Listing exclusions prevents false assumptions and scope creep.

| # | Out-of-Scope Item | Reason / Notes |
|---|-------------------|----------------|
| 1 | [Item] | [Why excluded or deferred] |

**Generation rule:** For every major feature area mentioned in the project description, explicitly state whether it is IN or OUT of scope. If something a stakeholder might reasonably expect is not being built, list it here. A blank Out of Scope table is a red flag — revisit with stakeholders.

**Audit tag:** If this section is empty or absent, Skill 08 (Semantic Auditing) shall flag `[CONTEXT-GAP: Out of Scope not defined]`.

## Resources
- `README.md`: Provides the synthesis intent for this skill.
- `context_engineering.py`: The automation script that performs the extraction, synthesis, and file writing described above.
- `logic.prompt`: Instructions for Claude to orchestrate this skill with the required tone, standards, and logging.

---
name: "initialize-srs"
description: "Set up IEEE Std 830-1998 and US ISO/IEC 25051 compliant project context files so downstream SRS skills can operate with stakeholder data, quality criteria, and definitions."
metadata:
  use_when: "Use when the task matches initialize-srs skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `templates/`, local scripts when deeper detail is needed."
---

> **[MISSING FILE FALLBACK]**
> This skill references auxiliary files (`logic.prompt`, Python scripts) for automated execution.
> **If those files are unavailable in your environment**, Claude can execute this skill directly:
> 1. Read all files in `projects/<ProjectName>/_context/`
> 2. Follow the step-by-step instructions in the **Manual Execution** section below (or ask Claude to generate the relevant SRS section by describing the context inline)
> 3. Write output to `projects/<ProjectName>/02-requirements-engineering/01-srs/<section-file>.md`
>
> _This skill is fully executable without Python or logic.prompt by providing context directly to Claude._

## Royce's 5 Critical Steps (IEEE WESCON 1970)

> Royce's original paper explicitly states the basic sequential waterfall (analysis → design → coding → testing) **"is risky and invites failure."** His real contribution was five corrective steps that all must be present for waterfall to succeed. Consultants must verify all five are planned before proceeding.

| Step | Requirement | Status Check |
|------|-------------|--------------|
| **1. Design First** | Preliminary program design (storage, timing, interfaces) must exist BEFORE analysis begins | `_context/` must include architecture constraints in `tech_stack.md` |
| **2. Document Everything** | Documentation IS the design. "If the documentation does not yet exist there is as yet no design." | All 6 Royce canonical docs must be planned |
| **3. Do It Twice** | Build a pilot/prototype first. Delivered version should be the second version | Pilot plan should exist in `01-strategic-vision/` |
| **4. Plan Testing Early** | Test planning starts at Program Design phase, not at the testing phase | Test Strategy should be initiated during Phase 03 Design |
| **5. Involve the Customer** | Three formal review gates: PSR (after prelim design), CSR (during design), FSAR (after testing) | Review gate dates must be in project schedule |

**Royce's 6 Canonical Documents (all must exist at delivery):**
1. Software Requirements → `SRS_Draft.docx` (this pipeline)
2. Preliminary Design Spec → `HLD.docx` (Phase 03)
3. Interface Design Spec → `APISpec.docx` + `DatabaseDesign.docx` (Phase 03)
4. Final Design Spec (As-Built) → `LLD.docx` updated after coding (Phase 03/04)
5. Test Plan + Test Results → `TestPlan.docx` + `TestReport.docx` (Phase 05)
6. Operating Instructions → `UserManual.docx` + `DeploymentGuide.docx` (Phase 06/08)

# Initialize-SRS Skill Guidance

## Overview
Use this skill to bootstrap the parent project with industrial templates that capture vision, features, technology constraints, business rules, quality standards, and glossary definitions before running any other SRS skills. The skill provides an automation script plus template guidance so Claude can reliably seed `../project_context/` and `../output/`.

## Quick Reference
- Initialize or refresh `../project_context/` with six templates (vision, features, tech stack, business rules, quality standards, glossary).
- Ensure `../output/` exists before downstream IEEE/ISO skills execute.
- Use Maintenance Mode when existing content must stay untouched; use Clean mode only when a fresh baseline is required.

## Anti-Hallucination Guard

> **CRITICAL:** Do NOT generate, invent, or assume any requirements, stakeholder names, features, or system behaviors that are not explicitly present in the `_context/` files. If a context file is empty or a required field is missing, **halt and prompt the consultant to fill it in** rather than making assumptions. Flag every gap with `[CONTEXT-GAP: <file> is missing <field>]`. This engine is a grounding tool, not a generation tool — all content must trace to stakeholder-provided context. *(Derived from hallucination mitigation guidance: Kodukula & Vinueza, 2024)*

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

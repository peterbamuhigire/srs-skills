---
name: "feature-decomposition"
description: "Convert features.md into IEEE 830 Section 3.2 (Functional Requirements) using a Functional Decomposition Tree with stimulus/response pairs and verifiable \"shall\" clauses."
metadata:
  use_when: "Use when the task matches feature decomposition skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt`, local scripts when deeper detail is needed."
---

# Feature Decomposition Skill Guidance

## Overview
Use this skill after Sections 1.0, 2.0, and 3.1 are generated. It transforms the feature set and quality standards into Section 3.2 (Feature Decomposition), ensuring every functional requirement follows a stimulus/response pattern with a single verifiable "shall" per clause per IEEE 830 Clause 5.3.1.

> **WBS Alignment:** The output of this skill forms the **requirements baseline** equivalent to a WBS Work Package layer (per PMBOK Guide, 7th Ed.): it decomposes scope from Features (Epic level) → Subfunctions (Story level) → Verifiable Requirements (task-level acceptance criteria). Project managers familiar with WBS methodology can use this output directly to populate their WBS dictionary for the requirements scope baseline.

## Quick Reference
- Inputs: `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/_context/quality_standards.md`
- Output: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (Section 3.2 only)
- Tone: Technical, precise, employing SHALL statements; avoid subjective adjectives and reference ISO/IEC 25010 Functional Suitability.

## Functional Requirement Template

Every SHALL requirement must include an inline GWT (Given-When-Then) acceptance stub immediately after the requirement statement:

```
**FR-[ID]: [Requirement Title]**
The system shall [verb] [object] when [condition].

**Acceptance:**
- **Given** [precondition — system state before the action]
- **When** [trigger action — exactly one]
- **Then** [observable outcome — externally verifiable]

*Priority: [Must/Should/Could/Won't] | Audience: [End User / Admin / Developer] | Precondition: [System state required before this requirement applies, or "None"]*
```

**GWT Rules (Adzic, 2023):**
- Exactly ONE `When` clause per stub. Two Whens = two requirements.
- `Then` must describe an externally observable state change, not an internal variable.
- `Given` uses past tense (preconditions that existed before the action).
- If the expected result requires judgment to determine pass/fail → tag `[VERIFIABILITY-FAIL: expected result is not a test oracle]`.

**Checklist:**
- [ ] Every SHALL requirement has an inline GWT stub with exactly one When clause
- [ ] Every FR has a Precondition clause (even if "None")
- [ ] Every FR has an [AUDIENCE] tag

## Core Instructions
1. Run `python feature_decomposition.py` from this directory or invoke the `logic.prompt` through your skill runner.
2. Parse each feature entry from `features.md`, extract user story triggers, and build a Functional Decomposition Tree with numbered subsections (3.2.x.1 Description/Priority, 3.2.x.2 Stimulus/Response Sequences, 3.2.x.3 Functional Requirements).
3. Write exactly one "shall" per clause; pair every stimulus with a deterministic response. For each feature, include ALL IEEE 830 §5.3.2 sub-items:
   - Validity checks on inputs (data type, range, format)
   - Exact sequence of operations (numbered processing steps)
   - Responses to abnormal situations (overflow, communication failure, error recovery)
   - Effect of parameters (how configuration alters behavior)
   - Input/output relationships and formulas (LaTeX where applicable)
   - Error handling requirements (independently verifiable)
4. Every requirement MUST have an importance ranking (Essential/Conditional/Optional) per IEEE 830 §4.3.5 and a backward traceability reference `[Source: features.md > Feature Name]` per IEEE 830 §4.3.8.
5. Confirm Section 3.2 references ISO/IEC 25010 Functional Suitability and that each requirement is traceable back to a feature in `features.md`.
6. Reference `../ieee-830-compliance-checklist.md` (ID IEEE830-5.3.2) for compliance verification.
5. Validate that the updated `SRS_Draft.md` retains Sections 1.0, 2.0, and 3.1 content while replacing or appending Section 3.2.

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in the SRS document directory (`projects/<ProjectName>/<phase>/<document>/01-srs/`) listing the section files in the correct assembly order:

```markdown
# Document Manifest — SRS Feature Decomposition
# Generated by feature-decomposition. Edit to reorder or exclude sections before building.
01-introduction.md
02-overall-description.md
03-functional-requirements.md
04-nfr.md
05-external-interfaces.md
06-constraints.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Resources
- `README.md`: Explains the intent and quality expectation for this skill.
- `feature_decomposition.py`: Automation script that performs parsing, decomposition, and writing of Section 3.2.
- `logic.prompt`: Provides meta instructions for Claude to orchestrate the process.

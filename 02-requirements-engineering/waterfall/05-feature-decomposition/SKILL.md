---
name: feature-decomposition
description: Convert features.md into IEEE 830 Section 3.2 (Functional Requirements) using a Functional Decomposition Tree with stimulus/response pairs and verifiable "shall" clauses.
---

# Feature Decomposition Skill Guidance

## Overview
Use this skill after Sections 1.0, 2.0, and 3.1 are generated. It transforms the feature set and quality standards into Section 3.2 (Feature Decomposition), ensuring every functional requirement follows a stimulus/response pattern with a single verifiable "shall" per clause per IEEE 830 Clause 5.3.1.

## Quick Reference
- Inputs: `../project_context/features.md`, `../project_context/quality_standards.md`
- Output: `../output/SRS_Draft.md` (Section 3.2 only)
- Tone: Technical, precise, employing SHALL statements; avoid subjective adjectives and reference ISO/IEC 25010 Functional Suitability.

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

## Resources
- `README.md`: Explains the intent and quality expectation for this skill.
- `feature_decomposition.py`: Automation script that performs parsing, decomposition, and writing of Section 3.2.
- `logic.prompt`: Provides meta instructions for Claude to orchestrate the process.

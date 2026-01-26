---
name: semantic-auditing
description: Validate the full SRS and create a Requirements Traceability Matrix plus audit report following IEEE 1012 and IEEE 830.
---

# Semantic Auditing Skill Guidance

## Overview
Run this skill after Sections 1.0–3.5 have been generated so it can audit the entire SRS and the project context before verification activities begin.

## Quick Reference
- Inputs: `../output/SRS_Draft.md`, every file within `../project_context/`
- Output: `Audit_Report.md` containing the Requirements Audit, RTM, Ambiguity & Weak Word Report, Gap Analysis, and Standard Conformance Statement.
- Tone: Ruthless, technical, PASS/FAIL oriented; avoid filler.

## Core Instructions
1. Execute `python semantic_auditing.py` from this directory or trigger via `logic.prompt`. The script logs all reads, forces unique requirement IDs, and generates the audit report as a stand-alone artifact so the SRS remains unchanged.
2. The Requirements Audit section reviews IEEE 830’s eight qualities and calls out any failures (duplicate text, missing measurements, orphan requirements, etc.). Use the audit findings to fix requirements before moving to test planning.
3. The RTM ties each requirement ID to its feature, goal, ISO/IEC 25010 quality characteristic, and verification method; keep verification methods grounded in Test/Demo/Inspection vocabulary.
4. Ambiguity & Weak Word Report flags sentences containing weak verbs or missing metrics; each flag is labeled `FAIL`. Gap Analysis lists Orphan Requirements (no matching feature goal) and Unmet Goals (features without requirements).
5. The Standard Conformance Statement explicitly states how this artifact meets US ISO/IEC 25010 and IEEE 830.

## Resources
- `README.md`: Execution steps and precision reminders.
- `semantic_auditing.py`: Automation that reads the SRS/context files, audits requirements, and writes `Audit_Report.md`.
- `logic.prompt`: LLM instructions that describe the auditing steps, traceability expectations, and critical tone.
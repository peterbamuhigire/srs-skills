---
name: "semantic-auditing"
description: "Validate the full SRS and create a Requirements Traceability Matrix plus audit report following IEEE 1012 and IEEE 830."
metadata:
  use_when: "Use when the task matches semantic auditing skill guidance and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt`, local scripts when deeper detail is needed."
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
2. Load `../ieee-830-compliance-checklist.md` and use its checklist IDs (IEEE830-4.3.1 through IEEE830-5.4.3) when reporting all findings.
3. The Requirements Audit section reviews ALL eight IEEE 830 quality attributes with enhanced checks:
   - **Ranking completeness** (IEEE830-4.3.5): every requirement must have Essential/Conditional/Optional priority
   - **TBD protocol** (IEEE830-4.3.3.1): every TBD must include condition, resolution, owner, deadline
   - **Modifiability** (IEEE830-4.3.7): no redundancy, single-shall-per-clause, cross-references present
   - **Backward traceability** (IEEE830-4.3.8): every requirement references its source document
4. **SRS Structure Verification**: confirm presence of ALL required IEEE 830 sections including 2.1.1–2.1.8 sub-items, Section 2.6 (Apportioning), Section 3.5.5 (Standards Compliance), Section 3.6 (Other Requirements), and Table of Contents.
5. The RTM ties each requirement ID to its feature, goal, ISO/IEC 25010 quality characteristic, verification method, and backward traceability reference.
6. Gap Analysis covers: orphan requirements, unmet goals, missing SRS sections, non-compliant TBDs, and unranked requirements.
7. The Standard Conformance Statement provides a clause-by-clause compliance summary with overall verdict: COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT.

### Glossary Audit

For every domain-specific term, acronym, or project-specific phrase used in the SRS output:
1. Check whether it is defined in `_context/glossary.md`
2. If undefined, tag the occurrence as `[GLOSSARY-GAP: <term>]`
3. List all GLOSSARY-GAP findings in the audit report under a "Terminology Gaps" section
4. The SRS is not considered complete until all GLOSSARY-GAP tags are resolved or explicitly accepted by the consultant

**Acceptance criteria:** Zero unresolved [GLOSSARY-GAP] tags before Skill 08 closure.

**Checklist:**
- [ ] Zero [GLOSSARY-GAP] tags unresolved

## Resources
- `README.md`: Execution steps and precision reminders.
- `semantic_auditing.py`: Automation that reads the SRS/context files, audits requirements, and writes `Audit_Report.md`.
- `logic.prompt`: LLM instructions that describe the auditing steps, traceability expectations, and critical tone.
# 08-Semantic-Auditing Skill

## Objective

This skill performs a ruthless audit of `../output/SRS_Draft.md` plus every file in `../project_context/`, validates the eight IEEE 830 qualities, and emits a traceability matrix plus verification artifacts aligned with IEEE 1012.

## Execution Steps

1. Run `python semantic_auditing.py` from this directory. The script reads each context file, the current SRS draft, and generates a standalone `Audit_Report.md` at the workspace root while logging every file access.
2. Inspect `Audit_Report.md` for the Requirements Audit (IEEE 830), the Requirements Traceability Matrix (RTM), Ambiguity & Weak Word Report, Gap Analysis, and the Standard Conformance Statement. Each section uses traceable IDs, identifies PASS/FAIL status, and flags any missing measurements.
3. Use the audit results to tighten requirements (eliminate weak words, add measurable targets, map each requirement to a goal) before progressing to validation or implementation chapters.

## Engineering Rigor: The Traceability Matrix

- RTM rows follow the format `[Req ID] | [Feature Name] | [Source/Vision Goal] | [ISO/IEC 25010 Quality Tag] | [Verification Method]` with unique IDs such as `R-REQ-001`.
- Ambiguity findings are marked as `FAIL` with precise citations; any requirement that lacks a measurable target or uses weak terminology is highlighted.
- Gap Analysis lists Orphan Requirements and Unmet Goals so the audit links to IEEE 1012 (Verification & Validation) while staying grounded in IEEE 830.
- Standard Conformance Statement references both IEEE 830 and US ISO/IEC 25010, emphasizing traceability and measurability.

## Quality Reminder

Stay critical, avoid filler, and keep the tone technical. The audit must feel like a forensic report: precise, comparative, and unwaveringly human. Every requirement needs a measurable target, a mapped goal, and a verification method.

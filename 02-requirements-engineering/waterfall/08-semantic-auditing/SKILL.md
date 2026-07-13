---
name: 08-semantic-auditing
description: "Use when performing a read-only semantic audit for ambiguity, contradiction, undefined terms, weak modals, and inconsistent requirement language; use requirements-validation for the full multidisciplinary gate."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Semantic Auditing Skill Guidance

<!-- local-contract-start -->
<!-- dual-compat-start -->
## Use When

- performing a read-only semantic audit for ambiguity, contradiction, undefined terms, weak modals, and inconsistent requirement language; use requirements-validation for the full multidisciplinary gate.
- Use this procedure when the required source artefacts are available and `Semantic audit findings` is the next lifecycle deliverable.

## Do Not Use When

- Use `requirements-validation` when that neighbouring route owns the decision or deliverable.
- Do not invent missing project evidence, standards clauses, thresholds, or stakeholder decisions.

## Required Inputs

| Artefact | Source or provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Draft SRS, glossary, controlled vocabulary, quality rules, and source evidence | Requirements owner and domain glossary | Yes | Stop the affected step, name the missing source, and return only a qualified gap record. |

## Workflow

1. Inspect the required inputs and log the exact sources, versions, and unresolved assumptions.
2. Apply this skill's existing domain workflow and decision rules to produce `Semantic audit findings`.
3. Stop when a required source, accountable decision owner, or deterministic test oracle is absent.
4. Recover by preserving valid work, marking the blocked scope, and returning the narrowest qualified artefact plus the next evidence needed.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Semantic audit findings | Requirements authors, reviewers, and quality gate | Required sections are populated, source links resolve, and every material requirement or decision has an observable review or test oracle. |

## Evidence Produced

| Evidence | Reviewer | Acceptance condition |
| --- | --- | --- |
| Source, decision, trace, and validation record for `Semantic audit findings` | Requirements quality reviewer | Inputs used, decisions made, checks run, failures, and unassessed items are explicit. |

## Capability and permission boundaries

Read and search are required. This procedure is read-only by default. Editing the reviewed artefact, publishing, production mutation, destructive action, spending, or certification requires explicit authority.

## Degraded mode

Fallback: if a required file, reviewer, standard source, network check, renderer, or execution capability is unavailable, return the narrowest useful qualified result and mark the affected check `not assessed`; never convert an unassessed check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A term or modal changes meaning across requirements | Issue an evidence-linked finding and withhold a clean verdict. | Misinterpretation masked by syntactic correctness. |
| Required inputs and test oracles are complete | Continue through the existing workflow and record evidence. | A deliverable whose acceptance cannot be reproduced. |
| A mandatory source or owner is missing | Stop the affected branch and issue a qualified gap record. | Fabricated context or unauthorised decisions. |

## Quality Standards

- Preserve stable identifiers and bidirectional traceability from project evidence to `Semantic audit findings` and its acceptance checks.
- Apply ISO/IEEE measures only with a named metric, method, threshold, evidence source, and responsible reviewer; run the anti-slop gate before release.

## Anti-Patterns

- Producing `Semantic audit findings` from assumed context. Fix: cite the project source or mark the scope blocked.
- Accepting a material requirement without a deterministic oracle. Fix: add a measurable result, boundary, and verification method.
- Crossing into `requirements-validation` without routing the decision. Fix: hand off the named input and preserve trace links.
- Treating an unavailable check as passed. Fix: mark it `not assessed` and state the release consequence.
- Claiming standards, statutory, or stakeholder approval without evidence. Fix: cite the source and reviewer or qualify the claim.

## References

- [Skill authoring and release standard](../../../docs/skill-authoring-standard.md)
- [Skill guidance](README.md)
- [Executable generation logic](logic.prompt)
<!-- dual-compat-end -->
<!-- local-contract-end -->

## Overview
Run this skill after Sections 1.0–3.5 have been generated so it can audit the entire SRS and the project context before verification activities begin.

## Quick Reference
- Inputs: `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, every file within `projects/<ProjectName>/_context/`
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

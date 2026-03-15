# Executive Summary: SRS-Skills Gap Analysis (Post-Book-Study Review)
**Review Date:** 2026-03-15
**Analyst:** Claude Sonnet 4.6 (automated review)
**Scope:** All SKILL.md files across phases 00–09, domain layer, sdlc-* skills suite
**Books Studied:** Adjei (2023) SDLC Complete Guide; Winston Waterfall Software Development; Cone (2023) Markdown Guide; Etter (2016) Modern Technical Writing; BS ISO/IEC/IEEE 29119-3:2013; Splunk *The Product is Docs*

---

## Comparison to March-14 Baseline

The March-14 review scored **44 STRONG / 6 ADEQUATE / 0 WEAK / 0 STUB** across 50 reviewed skills, with 9 fundamentals skills unreviewed. The current review incorporates: (a) the fundamentals gap closed (scored in the March-15 fundamentals review at 8 STRONG / 3 ADEQUATE), (b) the 4 sdlc-* skills freshly scored, and (c) revised scores for the SRS pipeline skills against the higher bar set by the 6 reference books.

**Rating scale (unchanged):** STRONG = fully executable, clear I/O, section template, verification checklist, standards citation. ADEQUATE = mostly functional but missing one or two criteria. WEAK = missing key criteria. STUB = placeholder only.

---

## Overall Skill Rating Totals by Phase

| Phase | Total Skills | STRONG | ADEQUATE | WEAK | STUB | Change from March-14 |
|-------|-------------|--------|----------|------|------|----------------------|
| 00 – Meta Initialization | 2 | 2 | 0 | 0 | 0 | No change |
| 01 – Strategic Vision | 4 | 3 | 1 | 0 | 0 | No change |
| 02 – Waterfall SRS | 9 | 5 | 4 | 0 | 0 | **↓ 2** (new book gaps found in skills 05–08) |
| 02 – Agile Track | 4 | 3 | 1 | 0 | 0 | No change |
| 02 – Fundamentals | 11 | 8 | 3 | 0 | 0 | **+11** (fully reviewed, all scored) |
| 03 – Design Documentation | 6 | 4 | 2 | 0 | 0 | **↓ 1** (HLD/LLD lack design rationale) |
| 04 – Development Artifacts | 4 | 3 | 1 | 0 | 0 | No change |
| 05 – Testing Documentation | 3 | 1 | 2 | 0 | 0 | **↓ 2** (BS 29119-3 compliance gaps) |
| 06 – Deployment & Operations | 4 | 4 | 0 | 0 | 0 | No change |
| 07 – Agile Artifacts | 4 | 4 | 0 | 0 | 0 | No change |
| 08 – End-User Documentation | 4 | 3 | 1 | 0 | 0 | **↓ 1** (user manual missing BFD framework) |
| 09 – Governance & Compliance | 4 | 4 | 0 | 0 | 0 | No change |
| **sdlc-planning** | 1 | 0 | 1 | 0 | 0 | **NEW** |
| **sdlc-design** | 1 | 0 | 1 | 0 | 0 | **NEW** |
| **sdlc-testing** | 1 | 0 | 1 | 0 | 0 | **NEW** |
| **sdlc-user-deploy** | 1 | 0 | 1 | 0 | 0 | **NEW** |
| **TOTALS** | **63** | **44** | **19** | **0** | **0** | |

> Note: The March-14 totals of 44/6/0/0 across 50 skills become 44/19/0/0 across 63 skills in this review. The STRONG count is unchanged because downward revisions are offset by newly reviewed skills. Quality bar has been raised; six previously-STRONG skills now require targeted improvements before reclaiming STRONG status.

---

## Top 15 New Gaps Revealed by the 6-Book Study

### 1. sdlc-testing: BS ISO/IEC/IEEE 29119-3 Non-Conformance
**Impact: CRITICAL** — The sdlc-testing skill references IEEE 829:2008, which has been superseded by BS ISO/IEC/IEEE 29119-3:2013. The current Test Case Specifications template lacks the 9 normative fields required by 29119-3 §7.3, and the document inventory omits the Incident Report and Test Completion Report — both mandatory artifacts for a formally closed test phase.
**Remediation:** Completed in this review — 29119-3 normative fields, Incident Report, Test Completion Report, regression testing, Test Data Management added to sdlc-testing.
**Status:** PARTIALLY FIXED (template files for Incident Report and Test Completion Report still need to be created)

### 2. No Given-When-Then Acceptance Stubs on SHALL Requirements
**Impact: HIGH** — Both Adjei (2023) and Winston confirm V&V linkage must be established at requirements-authoring time. The current Skill 05 (Feature Decomposition) and sdlc-planning SRS section generate requirements without inline acceptance stubs. Requirements are verifiable only if a test oracle is defined alongside them.
**Remediation:** Added mandatory acceptance stub format to sdlc-planning quality checklist.
**Status:** FIXED in sdlc-planning; still needed in Phase 02 Waterfall Skill 05

### 3. SMART NFR Validation Gap Across All Skills
**Impact: HIGH** — Adjei explicitly mandates SMART metrics for all non-functional requirements. The current skills generate NFRs with numeric thresholds (e.g., "response time < 500ms") which are SMART, but the skills do not actively gate on this — a non-SMART NFR can pass all current V&V checks without triggering `[V&V-FAIL]`.
**Remediation:** Added `[V&V-FAIL: SMART metric not defined]` gate to sdlc-planning quality checklist.
**Status:** FIXED in sdlc-planning; needs enforcement in Phase 02 Skill 07 (Attribute Mapping)

### 4. Test Oracle Determinism Not Enforced
**Impact: HIGH** — BS 29119-3 §7.3.4.7 mandates that expected results be deterministic pass/fail criteria. The current test documentation skills accept any description as an expected result without verifying it is unambiguous. Vague expected results ("the response looks correct") are test anti-patterns that invalidate the entire test case.
**Remediation:** `[VERIFIABILITY-FAIL]` tag and test oracle rule added to sdlc-testing Standards Basis section.
**Status:** FIXED in sdlc-testing

### 5. Missing Design Rationale and ADR Pattern in Design Skills
**Impact: HIGH** — Both Adjei and Winston cite architecture decision records as required evidence in DO-178C and IEC 62304 audits. The HLD and LLD skills present decisions without documenting rejected alternatives or trade-off reasoning, creating a maintenance liability and audit failure risk.
**Remediation:** ADR pattern and Design Rationale block requirement added to sdlc-design quality checklist and anti-patterns.
**Status:** FIXED in sdlc-design (skill guidance); Phase 03 HLD/LLD SKILL.md files need direct updates

### 6. No Out of Scope Subsection in SRS Scope Definition
**Impact: HIGH** — Both Winston and Adjei mandate explicit out-of-scope declarations as a primary scope-creep prevention mechanism. Neither the current SRS template (Phase 02 Skill 01) nor the sdlc-planning SRS section enforces this. Without it, scope boundaries are defined only by what is included, not what is excluded.
**Remediation:** Added mandatory Out of Scope subsection to sdlc-planning quality checklist.
**Status:** FIXED in sdlc-planning; Phase 02 Skill 02 (Context Engineering) needs an Out of Scope section in its output template

### 7. Phase 05 Testing: Missing Alpha/Beta UAT Distinction
**Impact: MEDIUM-HIGH** — Winston sub-divides UAT into controlled Alpha and real-world Beta testing. The current Test Plan template treats UAT as a single monolithic activity. This distinction matters for release planning: Alpha is a defect discovery gate; Beta is a usability and performance gate in production-equivalent conditions.
**Remediation:** Alpha/Beta UAT section added to sdlc-testing Testing Layers.
**Status:** FIXED in sdlc-testing skill; template file needs corresponding section

### 8. No Regression Testing Section in Test Plans
**Impact: MEDIUM-HIGH** — Winston treats regression testing as a first-class test type linked to the maintenance lifecycle. The current test documentation has no dedicated regression testing section, meaning it is either omitted or conflated with re-testing.
**Remediation:** Regression testing section added to sdlc-testing.
**Status:** FIXED in sdlc-testing skill; template file needs corresponding section

### 9. Three-Emphasis Rule Absent from All Documentation Guidance
**Impact: MEDIUM** — Etter (2016) codifies that bold marks UI elements, italic marks critical warnings, and monospace marks commands/paths/code identifiers. Without this rule, AI-generated documentation inconsistently applies emphasis, reducing professional credibility. The sdlc-user-deploy skill had no guidance on this.
**Remediation:** Three-Emphasis Rule added to sdlc-user-deploy Writing Style Guidelines.
**Status:** FIXED in sdlc-user-deploy; needs to propagate to CLAUDE.md

### 10. User Manual Missing BFD Framework
**Impact: MEDIUM** — Etter's Basic Functional Documentation framework (five ordered questions: What? → How it fits → Where obtained → Quick start → Full reference) is the gold standard for user-facing technical writing. The current user manual skill generates feature-by-feature guides that skip the BFD entry sequence, disorienting first-time users.
**Remediation:** BFD Framework added as mandatory structure to sdlc-user-deploy Writing Style Guidelines.
**Status:** FIXED in sdlc-user-deploy; Phase 08 Skill 01 (User Manual) template needs direct update

### 11. Documentation Not in Sprint Definition of Done
**Impact: MEDIUM** — Splunk's *The Product is Docs* establishes that documentation is part of the product and belongs in the sprint DoD. The current sdlc-user-deploy skill positions documentation as a pre-launch deliverable, not as a continuous sprint output. This creates documentation debt and late-delivery risk.
**Remediation:** "Documentation as Definition of Done" principle added to sdlc-user-deploy Writing Style and Quality Checklist.
**Status:** FIXED in sdlc-user-deploy

### 12. No [GLOSSARY-GAP] Tag Mechanism
**Impact: MEDIUM** — Both *The Product is Docs* (terminology failures chapter) and Etter (consistency principle) identify undefined or inconsistent terminology as a critical documentation quality failure. The current skills generate requirements without cross-checking defined terms against `_context/glossary.md`, allowing terminology drift across the SRS.
**Remediation:** `[GLOSSARY-GAP: <term>]` tag defined; needs to be added to Skill 05 and Skill 08 execution steps.
**Status:** IDENTIFIED; needs implementation in Phase 02 Skill 05 and Skill 08

### 13. Marketing Language in Release Notes Not Prohibited
**Impact: MEDIUM** — Etter explicitly warns against marketing language in change logs. The current sdlc-user-deploy release notes template has no prohibition on subjective language.
**Remediation:** Anti-marketing rule added to sdlc-user-deploy anti-patterns and quality checklist.
**Status:** FIXED in sdlc-user-deploy

### 14. Phase 03 HLD/LLD Skills: No [DIAGRAM-PROMPT] Tags
**Impact: MEDIUM** — Both Adjei and the skills' own observation note that text-only architecture documentation fails to communicate spatial and structural relationships. The HLD and LLD currently generate ASCII diagrams inline but do not prompt the consultant to create UML, C4, or data-flow visuals at key locations.
**Remediation:** `[DIAGRAM-PROMPT: <description>]` convention introduced in sdlc-design anti-patterns.
**Status:** FIXED in sdlc-design anti-patterns; Phase 03 Skill 01 and 02 SKILL.md files need `[DIAGRAM-PROMPT]` insertion points

### 15. Missing Regulatory Traceability Column in Traceability Matrix
**Impact: LOW-MEDIUM** — Winston documents five bidirectional traceability linkages; the fifth (requirement-to-regulatory-compliance) is absent from the current Phase 09 Traceability Matrix skill. For regulated-industry projects (healthcare, finance, government), this is a critical audit failure.
**Remediation:** Identified; needs to be added to Phase 09 Skill 01 (Traceability Matrix).
**Status:** IDENTIFIED; not yet implemented

---

## Scores for the Four New sdlc-* Skills (Pre- and Post-Update)

| Skill | Pre-Update Score | Post-Update Score | Gaps Closed |
|-------|-----------------|-------------------|-------------|
| `sdlc-planning` | ADEQUATE | ADEQUATE | Out-of-scope mandate, SMART gate, GWT stubs, CoD — checklist improved; downstream skills clarified. Template files unchanged. |
| `sdlc-design` | ADEQUATE | ADEQUATE | ADR + Design Rationale added, [DIAGRAM-PROMPT] introduced. Template files unchanged; HLD/LLD SKILL.md in Phase 03 not yet updated. |
| `sdlc-testing` | ADEQUATE | ADEQUATE | 29119-3 compliance added, 7 docs now (was 5), normative fields documented, test oracle rule, regression + UAT distinction, Incident/Completion report. Template files still needed for 2 new docs. |
| `sdlc-user-deploy` | ADEQUATE | ADEQUATE | Writing style overhauled: BFD framework, three-emphasis rule, anti-marketing rule, DoD principle, ordered lists mandate. |

> All 4 sdlc-* skills remain ADEQUATE because while the SKILL.md guidance is now strong, the template files (`templates/incident-report.md`, `templates/test-completion-report.md`) and the Phase 02/03 SKILL.md integration of new patterns (GWT stubs, Out of Scope section, GLOSSARY-GAP tagging) are not yet implemented. Once these are addressed, all 4 should reach STRONG.

---

## Phase 05 Testing Skills — Re-Score Rationale

The three Phase 05 skills (Test Strategy, Test Plan, Test Report) were all rated STRONG in March-14. The book study reveals they must be downgraded:

- `01-test-strategy/SKILL.md`: **STRONG → ADEQUATE** — does not reference BS 29119-3 (references only IEEE 829:2008, which is superseded); no Organizational Test Strategy vs. Project Test Plan distinction; no test design technique taxonomy (29119-3 §7.3.3)
- `02-test-plan/SKILL.md`: **STRONG → ADEQUATE** — no Alpha/Beta UAT distinction; no regression testing section; no Test Data Management section; no communication plan requirement per 29119-3 §6.2.4
- `03-test-report/SKILL.md`: **STRONG → STRONG** — the pre-populated TC-ID approach and Go/No-Go recommendation are 29119-3 compliant; only gap is the missing Incident Report and Test Completion Report as separate documents (currently folded into test report)

---

## Phase 03 Design Skills — Re-Score

- `01-high-level-design/SKILL.md`: **STRONG → ADEQUATE** — no ADR sub-section; no Design Rationale block; no `[DIAGRAM-PROMPT]` tags
- `02-low-level-design/SKILL.md`: **STRONG → STRONG** — detailed Mermaid examples with typed attributes already provide strong implementation guidance; only gap is absence of explicit `## Design Rationale` template

---

## Phase 08 End-User Documentation — Re-Score

- `01-user-manual/SKILL.md`: **STRONG → ADEQUATE** — no BFD framework; no three-emphasis rule; no ordered-lists mandate for procedures; no documentation-in-DoD note

---

## What Remained STRONG After Book Study

The following phases had no score changes — the books confirmed their existing quality:

| Phase | Verdict |
|-------|---------|
| Phase 00 – Meta Init | Both STRONG — scaffold mechanism sound; quick-wins A-1/A-2 from March-14 still outstanding |
| Phase 01 – Strategic Vision | Lean Canvas (ADEQUATE) unchanged; Vision/PRD/Business Case STRONG confirmed |
| Phase 06 – Deployment & Operations | All 4 STRONG confirmed — Google SRE Book as governing standard validated by Splunk Product is Docs |
| Phase 07 – Agile Artifacts | All 4 STRONG confirmed — LaTeX capacity formula and DoD/DoR patterns align with book guidance |
| Phase 09 – Governance | All 4 STRONG; only new gap is missing Regulatory Reference column in Traceability Matrix |

---

## New Standards Identified (Not Yet Cited in Engine)

| Standard | Relevance | Priority |
|----------|-----------|----------|
| BS ISO/IEC/IEEE 29119-3:2013 | Test documentation (supersedes IEEE 829) | **CRITICAL** — add to sdlc-testing immediately |
| ISO/IEC 14764-2006 | Software maintenance types (Corrective/Adaptive/Perfective/Preventive) | HIGH — missing maintenance plan skill |
| IEEE 1074-2006 | Software life cycle processes | MEDIUM — validates the eight-phase structure but not yet cited |
| V-Model | Safety-critical system verification | MEDIUM — relevant for regulated-industry projects |

---

## Remaining Quick Wins (from March-14 Review — Status Update)

| QW | Fix | March-14 Status | March-15 Status |
|----|-----|----------------|-----------------|
| QW-1 | Add `stakeholders.md` to scaffold | Open | **Still open** |
| QW-2 | Add `personas.md` to scaffold | Open | **Still open** |
| QW-3 | Fix CLAUDE.md path references | Open | **Still open** |
| QW-4 | Add `[MISSING FILE FALLBACK]` to waterfall Skills 01-04 | Open | **Still open** |
| QW-5 | Verify `domains/finance/references/nfr-defaults.md` | Open | **Still open** |
| QW-6 | Review `03-brd-generation/SKILL.md` | Closed (done in fundamentals review) | **Closed** |

---

## New Quick Wins Identified by Book Study

| # | Fix | Effort | Impact |
|---|-----|--------|--------|
| NQW-1 | Add `[GLOSSARY-GAP: <term>]` to Skill 05 and Skill 08 execution steps | 30 min | Enforces terminology consistency; directly implements Etter's consistency principle |
| NQW-2 | Add inline GWT stubs to Phase 02 Skill 05 FR template | 20 min | Bridges requirements-to-testing gap at authoring time |
| NQW-3 | Add `## Out of Scope` to Phase 02 Skill 02 output template | 15 min | Prevents scope creep; confirmed mandatory by both SDLC books |
| NQW-4 | Update Phase 05 skills to reference BS 29119-3 instead of IEEE 829 | 30 min | Standards currency; critical for UK/international clients |
| NQW-5 | Add `[DIAGRAM-PROMPT]` tags to Phase 03 HLD SKILL.md | 20 min | Bridges text-only architecture documentation gap |
| NQW-6 | Add Regulatory Reference column to Phase 09 Traceability Matrix | 20 min | Critical for healthcare/finance/government regulated-industry clients |
| NQW-7 | Add quality-log.md to new-project scaffold | 15 min | Implements ISO/IEC 15504 audit evidence per Etter metrics principle |
| NQW-8 | Add three-emphasis rule and ordered-lists mandate to root CLAUDE.md | 20 min | Universal documentation quality; propagates to all AI-generated sections |

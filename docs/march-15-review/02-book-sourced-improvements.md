# Book-Sourced Improvements Applied and Pending
**Review Date:** 2026-03-15

This document tracks every improvement identified from the 6-book study, its source, implementation status, and target location.

---

## Book 1 & 2: Adjei (2023) + Winston — SDLC & Waterfall

| # | Improvement | Status | Target |
|---|-------------|--------|--------|
| W-01 | Add explicit `## Out of Scope` subsection to SRS Section 1.2 | ✅ Checklist | sdlc-planning; Phase 02 Skill 02 template pending |
| W-02 | SMART NFR validation gate `[V&V-FAIL: SMART metric not defined]` | ✅ Checklist | sdlc-planning; Phase 02 Skill 07 pending |
| W-03 | Inline Given-When-Then acceptance stubs on every SHALL requirement | ✅ Checklist | sdlc-planning; Phase 02 Skill 05 template pending |
| W-04 | MoSCoW priority column in functional requirements table | ✅ Referenced | sdlc-planning checklist — always existed; now reinforced |
| W-05 | Cost of Delay (CoD) prioritization for time-sensitive features | ✅ Anti-patterns | sdlc-planning |
| W-06 | Alpha/Beta UAT distinction in test plan | ✅ New section | sdlc-testing |
| W-07 | Regression testing as first-class test type | ✅ New section | sdlc-testing |
| W-08 | Test Data Management section in test plan | ✅ New section | sdlc-testing |
| W-09 | Six-step defect resolution protocol in test report | ❌ Pending | Phase 05 Skill 03 template |
| W-10 | ADR (Architecture Decision Record) pattern | ✅ Anti-patterns, checklist | sdlc-design |
| W-11 | Design Rationale block (chosen + rejected + trade-offs) | ✅ Anti-patterns, checklist | sdlc-design |
| W-12 | [DIAGRAM-PROMPT] tags at key visual-aid points | ✅ Anti-patterns, checklist | sdlc-design; Phase 03 pending |
| W-13 | Stakeholder Register + Communication Plan (upgraded) | ❌ Pending | Phase 02 Fundamentals Skill 01 |
| W-14 | Regulatory Reference column in Traceability Matrix | ❌ Pending | Phase 09 Skill 01 |
| W-15 | Software Maintenance Plan skill (ISO/IEC 14764-2006) | ❌ Identified only | New skill needed |
| W-16 | Post-Deployment Evaluation Report skill | ❌ Identified only | New skill needed |
| W-17 | CCB Charter sub-skill | ❌ Identified only | Phase 09 addition |
| W-18 | Water-Scrum-Fall hybrid detection in meta-initialization | ❌ Identified only | Phase 00 |
| W-19 | 3 missing elicitation techniques (Contextual Inquiry, Benchmarking, Data Gathering) | ❌ Pending | Phase 02 Fundamentals Skill 02 |
| W-20 | Update Phase 05 testing standard reference to BS 29119-3 | ✅ sdlc-testing | Phase 05 SKILL.md files pending |

---

## Book 3 & 4: Cone (2023) + Etter (2016) — Markdown & Technical Writing

| # | Improvement | Status | Target |
|---|-------------|--------|--------|
| M-01 | Three-emphasis rule: bold=UI, italic=warning, mono=commands | ✅ sdlc-user-deploy | CLAUDE.md pending |
| M-02 | Fenced code blocks with explicit language IDs in all technical skills | ✅ sdlc-user-deploy admin docs section | Phase 06 Skill 01/02, Phase 04 Skill 01 pending |
| M-03 | Audience metadata (End User / Administrator / Developer) per document | ✅ sdlc-user-deploy | All Phase skills pending |
| M-04 | Ordered lists mandatory for all sequential procedures | ✅ sdlc-user-deploy | CLAUDE.md pending |
| M-05 | Blank-line linter for block-level elements (pre-Pandoc) | ❌ Pending | scripts/build-doc.sh or new scripts/lint-md.sh |
| M-06 | quality-log.md added to `_context/` scaffold | ❌ Pending | Phase 00 new-project SKILL.md |
| M-07 | projects/<ProjectName>/README.md scaffolded at project creation | ❌ Pending | Phase 00 new-project SKILL.md |
| M-08 | Minimum-length directive: only content needed for verifiability | ❌ Pending | CLAUDE.md Skill Execution Workflow |
| M-09 | glossary.md as active terminology guard per skill invocation | ❌ Pending | CLAUDE.md Skill Execution Workflow |
| M-10 | BFD five-question framework for user manual and deployment guide | ✅ sdlc-user-deploy | Phase 08 Skill 01 template pending |
| M-11 | Footnotes for IEEE standards citations (cleaner requirement clauses) | ❌ Pending | CLAUDE.md + generated templates |
| M-12 | Anti-marketing language rule in release notes | ✅ sdlc-user-deploy anti-patterns + checklist | Phase 08 Skill 04 pending |
| M-13 | `---` alternate heading syntax banned (conflicts with Pandoc) | ❌ Pending | CLAUDE.md |
| M-14 | No nested lists/blockquotes inside table cells | ❌ Pending | CLAUDE.md |
| M-15 | Use `-` consistently for unordered lists (not `*` or `+`) | ❌ Pending | CLAUDE.md |

---

## Book 5 & 6: BS 29119-3 + Product is Docs (Splunk)

| # | Improvement | Status | Target |
|---|-------------|--------|--------|
| B-01 | Upgrade sdlc-testing to BS ISO/IEC/IEEE 29119-3:2013 | ✅ Standards Basis section | Phase 05 SKILL.md files pending |
| B-02 | 9-field normative test case anatomy (ID, objective, priority, traceability, preconditions, input, expected result, actual result, test result) | ✅ Standards Basis section, checklist | Template file pending |
| B-03 | Test oracle rule: expected results must be deterministic | ✅ [VERIFIABILITY-FAIL] tag defined | Phase 05 Skill 02 template pending |
| B-04 | Traceability requirement: every FR → ≥1 test case | ✅ Checklist | Phase 09 RTM needs column |
| B-05 | Phase Gate exit criteria per skill output | ❌ Pending | All Phase skills |
| B-06 | [GLOSSARY-GAP: <term>] tag for undefined domain terms | ❌ Pending | Phase 02 Skill 05, Skill 08 |
| B-07 | [AUDIENCE: role] tags on requirements | ❌ Pending | Phase 02 Skill 05 |
| B-08 | Test Data Readiness Report and Test Environment Readiness Report | ❌ Pending | Phase 05 new template files |
| B-09 | Incident Report with 8 normative fields | ✅ Document inventory | Template file pending |
| B-10 | Test Completion Report with 9 mandatory sections | ✅ Document inventory | Template file pending |
| B-11 | metrics.md in `_context/` scaffold | ❌ Pending | Phase 00 new-project SKILL.md |
| B-12 | Runbook as SaaS deployment prerequisite | ✅ sdlc-user-deploy admin section | Phase 06 Skill 02 confirmation pending |
| B-13 | Precondition clause in FR template (self-contained requirements) | ❌ Pending | Phase 02 Skill 05 template |
| B-14 | QA walkthrough of documented procedures | ✅ sdlc-user-deploy anti-patterns | Phase 08 Skill 01 pending |
| B-15 | Documentation in sprint Definition of Done | ✅ sdlc-user-deploy | Sprint planning skill, feature-planning pending |

---

## Implementation Priority Summary

### Done in This Pass (15 improvements)
W-01 through W-08, W-10, W-11, W-12, W-20, M-01, M-02, M-03, M-04, M-10, M-12, B-01 through B-04, B-09, B-10, B-12, B-14, B-15

### Highest-Priority Remaining (next session)

| Priority | ID | Fix | Effort |
|----------|----|-----|--------|
| 1 | B-06 | Add [GLOSSARY-GAP] to Skill 05 and Skill 08 | 30 min |
| 2 | W-03 | Add GWT stubs to Phase 02 Skill 05 FR template | 20 min |
| 3 | W-01 | Add Out of Scope to Phase 02 Skill 02 output template | 15 min |
| 4 | M-08 | Minimum-length directive in CLAUDE.md | 10 min |
| 5 | M-09 | Glossary guard in CLAUDE.md Skill Execution Workflow | 10 min |
| 6 | NQW-8 | Three-emphasis rule + ordered-lists in CLAUDE.md | 15 min |
| 7 | B-05 | Phase Gate exit criteria added to each skill | 60 min |
| 8 | W-14 | Regulatory Reference column in Phase 09 Traceability Matrix | 20 min |
| 9 | M-06 | quality-log.md to new-project scaffold | 15 min |
| 10 | B-03 | [VERIFIABILITY-FAIL] in Phase 05 Skill 02 template | 20 min |

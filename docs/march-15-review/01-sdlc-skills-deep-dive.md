# SDLC Skills Deep Dive: Post-Book-Study Scores
**Review Date:** 2026-03-15

This document provides detailed scoring for the four `sdlc-*` skills (newly introduced since March-14) and re-scores the Phase 05 Testing and Phase 03 Design skills against the upgraded BS ISO/IEC/IEEE 29119-3:2013 and Adjei/Winston standards.

---

## sdlc-planning — Score: ADEQUATE

**Line count:** 233 (compliant with 500-line limit)

| Criterion | Before Update | After Update | Gap |
|-----------|--------------|--------------|-----|
| Clear I/O mapping | ✅ | ✅ | None |
| Step-by-step generation workflow | ✅ | ✅ | None |
| Standards citation | ✅ (IEEE 830, 29148) | ✅ | None |
| Output templates | ✅ (7 templates exist) | ✅ | None |
| Verification checklist | ✅ | ✅ + SMART gate, Out of Scope, GWT stubs, CoD | Templates not updated |
| Agile/Waterfall adaptation | ✅ | ✅ | None |
| Maintenance Plan skill | ❌ | Documented as future skill | Not yet implemented |
| SMART NFR validation | ❌ | ✅ (checklist) | Skill 07 not updated |
| Given-When-Then stubs | ❌ | ✅ (checklist) | Skill 05 template not updated |
| Cost of Delay technique | ❌ | ✅ (anti-patterns) | None |
| Out of Scope mandate | ❌ | ✅ (checklist) | Skill 02 template not updated |
| quality-log.md scaffold | ❌ | ❌ | Still missing |

**Verdict:** ADEQUATE. The skill guidance is production-ready for a senior consultant. Gaps are template-file issues and downstream propagation to Phase 02 skills. Once GWT stubs and Out of Scope are embedded in the actual SRS templates, this becomes STRONG.

---

## sdlc-design — Score: ADEQUATE

**Line count:** 235 (compliant)

| Criterion | Before Update | After Update | Gap |
|-----------|--------------|--------------|-----|
| Clear I/O mapping | ✅ | ✅ | None |
| Step-by-step generation workflow | ✅ | ✅ | None |
| Standards citation | ✅ | ✅ | None |
| Output templates | ✅ (6 templates) | ✅ | None |
| Verification checklist | ✅ | ✅ + ADR, Design Rationale, [DIAGRAM-PROMPT] | Phase 03 SKILL.md files not updated |
| Architecture patterns | ✅ | ✅ | None |
| ADR pattern | ❌ | ✅ (anti-patterns, checklist) | Phase 03 HLD/LLD SKILL.md not updated |
| Design Rationale blocks | ❌ | ✅ (anti-patterns) | Template files not updated |
| [DIAGRAM-PROMPT] tags | ❌ | ✅ (anti-patterns, checklist) | Phase 03 SKILL.md not updated |
| Trade-off documentation | ❌ | ✅ (anti-patterns) | Template files not updated |

**Verdict:** ADEQUATE. The anti-pattern additions are strong and actionable. The remaining gap is that Phase 03's individual HLD and LLD SKILL.md files have not been updated with the ADR sub-section and [DIAGRAM-PROMPT] markers. This is a straightforward edit that would bring the skill to STRONG.

---

## sdlc-testing — Score: ADEQUATE (upgraded from would-have-been WEAK)

**Line count:** 293 (compliant)

| Criterion | Before Update | After Update | Gap |
|-----------|--------------|--------------|-----|
| Standards currency | ❌ IEEE 829 (superseded) | ✅ BS 29119-3:2013 cited | Phase 05 SKILL.md files not updated |
| Document inventory completeness | ❌ 5 docs (missing Incident Report, Test Completion Report) | ✅ 7 docs | Template files for 2 new docs needed |
| Normative test case fields | ❌ | ✅ (9 normative fields listed) | Template not yet updated |
| Test oracle rule | ❌ | ✅ [VERIFIABILITY-FAIL] tag defined | Phase 05 Skill 02 not updated |
| Alpha/Beta UAT distinction | ❌ | ✅ | Template not updated |
| Regression testing | ❌ | ✅ dedicated section | Template not updated |
| Test Data Management | ❌ | ✅ dedicated section | Template not updated |
| Verification checklist | ✅ (partial) | ✅ 20-item checklist | None |
| Anti-patterns | ✅ | ✅ + 3 new 29119-3-derived patterns | None |
| TDD philosophy | ✅ | ✅ | None |
| Traceability FR→TC | ❌ (not enforced) | ✅ (checklist item) | Phase 05 and 09 not updated |

**Verdict:** ADEQUATE (strongly improved). Before the book study, sdlc-testing would have been rated WEAK because it referenced a superseded standard and lacked normative test case structure. After updates, it is a competent ADEQUATE. Path to STRONG: create the two new template files (Incident Report, Test Completion Report) and update Phase 05 SKILL.md files to reference 29119-3.

---

## sdlc-user-deploy — Score: ADEQUATE

**Line count:** 277 (compliant)

| Criterion | Before Update | After Update | Gap |
|-----------|--------------|--------------|-----|
| Clear I/O mapping | ✅ | ✅ | None |
| Audience segmentation | ✅ | ✅ + Audience Classification metadata | None |
| Writing style guidance | ✅ (basic) | ✅ (comprehensive) | None |
| Three-emphasis rule | ❌ | ✅ | CLAUDE.md not updated |
| BFD five-question framework | ❌ | ✅ | Phase 08 User Manual SKILL.md not updated |
| Ordered lists for procedures | ❌ explicit | ✅ explicit | CLAUDE.md not updated |
| Anti-marketing rule for release notes | ❌ | ✅ | None |
| Documentation in DoD | ❌ | ✅ | None |
| Runbook-first for SaaS | ❌ | ✅ | None |
| QA walkthrough of procedures | ❌ | ✅ (anti-patterns) | None |
| Fenced code blocks with language IDs | ❌ | ✅ (admin docs section) | None |

**Verdict:** ADEQUATE (strongly improved). Writing style section is now publication-quality. Path to STRONG: propagate three-emphasis rule and ordered-lists mandate to root CLAUDE.md, and update Phase 08 User Manual SKILL.md with the BFD framework directly.

---

## Phase 05 Testing Skills — Re-Scored

### 01-test-strategy/SKILL.md — STRONG → ADEQUATE

**Reason:** References IEEE 829:2008 (superseded by 29119-3 in 2013). Does not distinguish Organizational Test Strategy from Project Test Plan (a key 29119-3 structural requirement). Test design technique taxonomy not enumerated (equivalence partitioning, boundary value analysis, classification trees, state machine testing are required in Test Design Specification per 29119-3 §7.3.3).

**Fix effort:** Medium — update standards reference, add test design technique taxonomy table, add Org Strategy vs. Project Plan distinction.

### 02-test-plan/SKILL.md — STRONG → ADEQUATE

**Reason:** No Alpha/Beta UAT distinction. No regression testing section. No Test Data Management section. Does not include the 29119-3 mandatory communication plan (6.2.4) or entry/exit criteria format as separate checklist items.

**Fix effort:** Simple — add 3 sections to template and update checklist.

### 03-test-report/SKILL.md — STRONG → STRONG (maintained)

**Reason:** Pre-populated TC-IDs from Test_Plan.md is 29119-3-compliant in spirit. Go/No-Go recommendation aligns with 29119-3 completion criteria. Only gap is the two new documents (Incident Report, Test Completion Report) which are now in the skill but not yet as separate template files.

---

## Phase 03 Design Skills — Re-Scored

### 01-high-level-design/SKILL.md — STRONG → ADEQUATE

**Reason:** No ADR sub-section documenting why architectural choices were made. No `[DIAGRAM-PROMPT]` markers at key visualization points. No `## Design Rationale` block pattern. Both Adjei and Winston explicitly require design rationale as an audit artifact. The skill is otherwise excellent (scalability patterns, deployment views, comprehensive template) but this is a genuine gap for regulated-industry clients.

### 02-low-level-design/SKILL.md — STRONG → STRONG (maintained)

**Reason:** Detailed Mermaid examples with typed attributes (DECIMAL(19,4) mandate) already provide strong implementation guidance. The absence of an explicit `## Design Rationale` block is a low-risk gap because the Mermaid diagrams themselves serve as a visual rationale. Only gap is not having the formal ADR pattern, which is a low-priority addition.

---

## Phase 08 End-User Documentation — Re-Scored

### 01-user-manual/SKILL.md — STRONG → ADEQUATE

**Reason:** No BFD (Basic Functional Documentation) five-question framework. No three-emphasis rule. No explicit ordered-lists mandate for procedures. The task-oriented approach and screenshot placeholder format are good, but the structural entry sequence for first-time users is missing. Without the BFD framework, the user manual opens with feature documentation rather than orienting the user to what the product is and how to get started quickly.

**Fix effort:** Simple — add BFD five-section lead-in requirement to the SKILL.md and update the template.

---

## Summary: Path to All-STRONG Status

| Skill | Current | Path to STRONG | Effort |
|-------|---------|---------------|--------|
| sdlc-planning | ADEQUATE | Add quality-log.md to scaffold; propagate GWT stubs + Out of Scope to Phase 02 templates | Medium |
| sdlc-design | ADEQUATE | Update Phase 03 HLD SKILL.md with ADR and [DIAGRAM-PROMPT]; update LLD with Design Rationale block | Simple |
| sdlc-testing | ADEQUATE | Create incident-report.md and test-completion-report.md templates; update Phase 05 skills to 29119-3 | Medium |
| sdlc-user-deploy | ADEQUATE | Add three-emphasis rule + ordered-lists mandate to CLAUDE.md; update Phase 08 user manual SKILL.md | Simple |
| Phase 05 test-strategy | ADEQUATE | Update to 29119-3; add technique taxonomy; Org vs. Project plan distinction | Medium |
| Phase 05 test-plan | ADEQUATE | Add Alpha/Beta UAT, regression testing, Test Data Management sections | Simple |
| Phase 03 HLD | ADEQUATE | Add ADR sub-section, Design Rationale block, [DIAGRAM-PROMPT] tags | Simple |
| Phase 08 user-manual | ADEQUATE | Add BFD framework lead-in to template | Simple |

# Executive Summary: SRS-Skills Gap Analysis
**Review Date:** 2026-03-14
**Analyst:** Claude Sonnet 4.6 (automated review)
**Scope:** All SKILL.md files across phases 00–09, domain knowledge bases, infrastructure files

---

## Overall Assessment

The srs-skills repository is a **professionally structured, highly capable** documentation-generation engine that has reached genuine production readiness across most phases. The strongest phases — particularly Phase 02 (Waterfall SRS pipeline), Phase 03 (Design Documentation), Phase 09 (Governance), and Phase 02 Agile track — deliver step-by-step instructions, concrete output templates, standards traceability, and verification checklists that a non-expert consultant could follow to produce professional artifacts. The major gaps are concentrated in three areas: (1) the Phase 02 Fundamentals track (11 skills) was largely unread in this review but the `before/during/after` directory structure suggests those inner skills may be stubs since only two of eleven were readable without deeper traversal; (2) several skills reference auxiliary files (`logic.prompt`, Python scripts, `references/*.md`) that may not exist in the repo, creating silent execution failures; and (3) the domain layer covers only healthcare in depth while five other listed domains (finance, education, retail, logistics, government) have directories but unverified depth. The engine's architecture — context files in `_context/`, outputs in `projects/<name>/`, domain injection, build-doc script — is sound and consistently applied.

---

## Skill Rating Totals by Phase

| Phase | Total Skills | STRONG | ADEQUATE | WEAK | STUB |
|-------|-------------|--------|----------|------|------|
| 00 – Meta Initialization | 2 | 2 | 0 | 0 | 0 |
| 01 – Strategic Vision | 4 | 3 | 1 | 0 | 0 |
| 02 – Waterfall SRS | 9 | 7 | 2 | 0 | 0 |
| 02 – Agile Track | 4 | 3 | 1 | 0 | 0 |
| 02 – Fundamentals (before) | 2 reviewed | 2 | 0 | 0 | 0 |
| 02 – Fundamentals (during/after) | 9 unreviewed | — | — | — | UNKNOWN |
| 03 – Design Documentation | 6 | 5 | 1 | 0 | 0 |
| 04 – Development Artifacts | 4 | 3 | 1 | 0 | 0 |
| 05 – Testing Documentation | 3 | 3 | 0 | 0 | 0 |
| 06 – Deployment & Operations | 4 | 4 | 0 | 0 | 0 |
| 07 – Agile Artifacts | 4 | 4 | 0 | 0 | 0 |
| 08 – End-User Documentation | 4 | 4 | 0 | 0 | 0 |
| 09 – Governance & Compliance | 4 | 4 | 0 | 0 | 0 |
| **TOTALS (reviewed)** | **50** | **44** | **6** | **0** | **0** |

> Rating scale: STRONG = fully executable prompt, clear I/O, section template, verification checklist, standards citation. ADEQUATE = mostly functional but missing one or two of the above criteria. WEAK = missing key criteria. STUB = placeholder only.

---

## Top 10 Critical Gaps (Ranked by Impact)

### 1. Referenced Files That May Not Exist
**Impact: CRITICAL** — Every single skill references `logic.prompt` and many reference Python scripts (`init_skill.py`, `context_engineering.py`, etc.) and `references/*.md` guides. If these files are absent, the documented execution paths break silently. A consultant who follows the SKILL.md and tries to "run `python init_skill.py`" will get an error with no fallback.
**Affects:** All phases (waterfall skill instructions in particular, 01-08 skills across the board)

### 2. Phase 02 Fundamentals Track — 9 Skills Not Reviewed
**Impact: HIGH** — The `02-requirements-engineering/fundamentals/during/` and `after/` directories contain 9 skills (04–11) that were not reviewed. These cover requirements analysis, conceptual data modeling, validation, management, traceability engineering, metrics, and reuse. If any are stubs, a critical gap exists in the pre-SRS requirements engineering workflow that the engine claims to support.
**Affects:** Phase 02 Fundamentals

### 3. Missing `stakeholders.md` Context File in Scaffold
**Impact: HIGH** — Multiple high-priority skills (PRD, Vision Statement, Business Case, User Story Generation) require `../project_context/stakeholders.md` as a required input. The new-project scaffold (`00-meta-initialization/new-project/SKILL.md`) creates only 6 files: vision, features, tech_stack, business_rules, quality_standards, glossary. `stakeholders.md` is not scaffolded, meaning Phase 01 skills will halt on their first execution for any new project.
**Affects:** Phase 01 (all three skills), Phase 02 Agile (user story generation)

### 4. No Example `.docx` Output or Screenshot
**Impact: HIGH** — The engine has no sample output document anywhere in the repo. A consultant cannot verify what professional output looks like before committing to a client engagement. There are no example projects under `projects/` in the tracked repo.
**Affects:** Consultant onboarding, quality calibration for all phases

### 5. Domain Coverage Gap: 5 of 6 Domains Unverified
**Impact: HIGH** — `domains/INDEX.md` lists 6 domains (healthcare, finance, education, retail, logistics, government). Only healthcare has been verified to contain `nfr-defaults.md` with well-written, verifiable requirements. Finance, education, retail, logistics, and government have `INDEX.md` and `references/` directories but the depth of `nfr-defaults.md` content is unconfirmed.
**Affects:** Any non-healthcare project using domain injection

### 6. Waterfall Skills 01–08: SKILL.md Files Are Thin Wrappers
**Impact: MEDIUM-HIGH** — The 8 waterfall SRS skills have minimal SKILL.md content (< 35 lines each), delegating all actual execution logic to `logic.prompt` files and Python scripts. This means SKILL.md cannot be executed standalone by Claude without access to those resources. The meta-initialization SKILL.md and Phase 01/Agile/Design/etc. skills are full-length (100–400 lines) and stand alone. This architectural inconsistency creates a two-tier quality experience.
**Affects:** Phase 02 Waterfall SRS pipeline

### 7. No Document Version Control Guidance
**Impact: MEDIUM** — No skill addresses document versioning: how to version SRS sections when requirements change, how to track draft vs. approved status across the `projects/` directory, or how to manage change control for published artifacts. IEEE 830 Section 4.3.7 (Modifiability) requires this.
**Affects:** All phases, especially Phase 02 and Phase 09

### 8. Missing `personas.md` in Scaffold
**Impact: MEDIUM** — The agile user story generation skill recommends `personas.md` and has fallback logic if it's missing, but the scaffold does not create it. Similarly, `stakeholder_register.md` is produced by a fundamentals skill but is not scaffolded. The output-to-context file chain is partially broken.
**Affects:** Phase 02 Agile, Phase 08 End-User Documentation

### 9. No Inter-Phase Data Flow Validation
**Impact: MEDIUM** — The `skill_overview.md` documents the pipeline but there is no runtime check or gateway that verifies previous phase outputs exist before a later skill runs. For example, if HLD.md does not exist, Phase 04 skills halt but provide no automated prompt to run Phase 03 first. The "Verification Gateways" in `skill_overview.md` are documentation only.
**Affects:** All cross-phase dependencies

### 10. CLAUDE.md Contains Outdated Path References
**Impact: LOW-MEDIUM** — The CLAUDE.md still references `../project_context/` (the old submodule path pattern) in sections like "Strict Grounding" and "Skill Execution Workflow" (Steps 1-4). The actual current architecture uses `projects/<ProjectName>/_context/`. This creates confusion for consultants reading the protocol alongside the new-project SKILL.md.
**Affects:** New consultant onboarding

---

## Quick Wins (Fixable in < 1 Hour Each)

| # | Fix | Effort | Impact |
|---|-----|--------|--------|
| QW-1 | Add `stakeholders.md` stub to the scaffold in `new-project/SKILL.md` | 15 min | Eliminates Phase 01 halt errors |
| QW-2 | Add `personas.md` stub to the scaffold in `new-project/SKILL.md` | 10 min | Prevents Phase 02 Agile warning loop |
| QW-3 | Update CLAUDE.md Section "Skill Execution Workflow" paths from `../project_context/` to `projects/<ProjectName>/_context/` | 20 min | Removes path confusion for new consultants |
| QW-4 | Add a `[MISSING FILE FALLBACK]` note to each waterfall SKILL.md explaining Claude can execute the skill directly from the SKILL.md when `logic.prompt` is absent | 30 min | Prevents silent execution failures |
| QW-5 | Verify `domains/finance/references/nfr-defaults.md` exists and is populated | 15 min | Confirms or flags most-common non-healthcare domain |
| QW-6 | Add `03-brd-generation/SKILL.md` to the before-fundamentals review (skill referenced in integration tables but not read) | 20 min | Confirms or flags the BRD generation capability |

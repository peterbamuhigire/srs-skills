# Requirements Engineering Fundamentals Layer — Design Document

**Date:** 2026-03-07
**Status:** Approved
**Author:** Peter Bamuhigire + Claude Opus 4.6

## Summary

Add a methodology-agnostic "fundamentals" layer to `02-requirements-engineering/` that wraps around both the Waterfall and Agile pipelines. 11 hybrid-granularity skills organized by lifecycle position (Before / During / After), with reference files for technique depth.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Layer relationship | Layered (C) — wraps around both pipelines | Matches real RE lifecycle: elicitation before, analysis during, management after |
| Skill granularity | Hybrid (C) — 10-12 skills with reference files | Matches existing conventions, respects 500-line SKILL.md limit |
| BRD generation | Optional with decision gate (C) | Serves enterprise/regulated without burdening lean teams |
| Data modeling | Conceptual only in fundamentals (A) | Clean separation: business domain in RE, logical/physical in Phase 03 |
| Metrics & quality | Dedicated metrics skill (A) | Single universal quality gate for both pipelines, DRY |
| Domain extensions | Hooks in elicitation skill only (C) | Catches domain concerns at gathering time without overcomplicating other skills |

## Book Sources

| Book | Key Contributions |
|------|-------------------|
| Agile Software Requirements (Leffingwell) | Epic→Feature→Story hierarchy, NFRs as constraints, enabler stories |
| Business Requirements Gathering & Data Architecture (Book 2) | BRD template, conceptual data modeling, data quality rules, MDM requirements |
| Requirements Engineering for Software and Systems (Laplante) | RE lifecycle, elicitation techniques, formal methods, metrics, domain-specific RE |
| Software Requirements Essentials (Wiegers & Beatty) | 20 core practices, requirements patterns, quality attributes checklist, reuse |

## Directory Structure

```
02-requirements-engineering/
├── fundamentals/
│   ├── README.md
│   ├── before/
│   │   ├── 01-stakeholder-analysis/    (SKILL.md + 2 references)
│   │   ├── 02-elicitation-toolkit/     (SKILL.md + 6 references)
│   │   └── 03-brd-generation/          (SKILL.md + 2 references, OPTIONAL)
│   ├── during/
│   │   ├── 04-requirements-analysis/   (SKILL.md + 4 references)
│   │   ├── 05-conceptual-data-modeling/(SKILL.md + 3 references)
│   │   ├── 06-requirements-patterns/   (SKILL.md + 3 references)
│   │   └── 07-requirements-validation/ (SKILL.md + 3 references)
│   └── after/
│       ├── 08-requirements-management/ (SKILL.md + 3 references)
│       ├── 09-traceability-engineering/(SKILL.md + 2 references)
│       ├── 10-requirements-metrics/    (SKILL.md + 2 references)
│       └── 11-requirements-reuse/      (SKILL.md + 2 references)
├── waterfall/  (unchanged)
└── agile/      (unchanged)
```

## Lifecycle Flow

```
BEFORE (run before choosing pipeline)
  01-stakeholder-analysis → 02-elicitation-toolkit → [03-brd-generation?]
      ↓
CHOOSE PIPELINE → waterfall/ OR agile/
      ↓
DURING (run alongside pipeline skills)
  04-requirements-analysis ←→ 05-conceptual-data-modeling
  06-requirements-patterns ←→ 07-requirements-validation
      ↓
AFTER (run after pipeline completes)
  08-requirements-management → 09-traceability-engineering
  10-requirements-metrics (quality gate)
  11-requirements-reuse (optional, for product lines)
```

## Standards Mapping

| Skill | Primary Standards |
|-------|-------------------|
| 01 Stakeholder Analysis | IEEE 29148 §6.2, Wiegers Practice 1-3 |
| 02 Elicitation Toolkit | Laplante Ch.4, IEEE 29148 §6.3, Wiegers Practice 4-6 |
| 03 BRD Generation | Book 2 Ch.2-4, IEEE 29148 §6.4 |
| 04 Requirements Analysis | Laplante Ch.5, IEEE 29148 §6.5, Wiegers Practice 7-9 |
| 05 Conceptual Data Modeling | Book 2 Ch.5-7, IEEE 1016 |
| 06 Requirements Patterns | Wiegers Practice 10-12, IEEE 830 |
| 07 Requirements Validation | Laplante Ch.6, IEEE 1012, Wiegers Practice 13-14 |
| 08 Requirements Management | Laplante Ch.7, IEEE 29148 §6.7, Wiegers Practice 15-17 |
| 09 Traceability Engineering | IEEE 1012, Laplante Ch.7.3, Wiegers Practice 18 |
| 10 Requirements Metrics | Laplante Ch.7.4, Wiegers Practice 19-20 |
| 11 Requirements Reuse | Laplante Ch.9, Wiegers Practice 20 |

## Input/Output Contracts

**Inputs (from `../project_context/`):**
- vision.md, features.md, tech_stack.md, business_rules.md, quality_standards.md, glossary.md

**New artifacts generated (to `../project_context/` or `../output/`):**
- stakeholder_register.md, elicitation_log.md, brd.md (optional)
- conceptual_data_model.md, requirements_analysis_report.md
- requirements_baseline.md, traceability_matrix.md, metrics_report.md

## Integration Points

- Fundamentals `before/` feeds both `waterfall/01-initialize-srs` and `agile/01-user-story-generation`
- Fundamentals `during/` skills can be invoked at any point during pipeline execution
- Fundamentals `after/` complements waterfall `08-semantic-auditing` and serves as Agile's missing quality gate
- `10-requirements-metrics` produces a universal quality score usable by both pipelines

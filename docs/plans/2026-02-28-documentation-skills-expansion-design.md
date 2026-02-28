# Design: Documentation Skills Expansion (Phases 01-03 + Phase 02 Fixes)

**Date:** 2026-02-28
**Author:** Peter Bamuhigire (with AI assistance)
**Version:** 1.0.0
**Status:** Approved

## Objective

Build 11 new documentation skills across three phases, plus fix existing gaps in Phase 02. This brings the SDLC-Docs-Engine from ~23% to ~50% implementation coverage.

## Scope

### Phase 02 Fixes (4 items)

| Item | Type | Directory |
|------|------|-----------|
| `05-feature-decomposition/SKILL.md` | Missing file | `02-requirements-engineering/waterfall/05-feature-decomposition/` |
| `02-acceptance-criteria` | New sub-phase | `02-requirements-engineering/agile/02-acceptance-criteria/` |
| `03-story-mapping` | New sub-phase | `02-requirements-engineering/agile/03-story-mapping/` |
| `04-backlog-prioritization` | New sub-phase | `02-requirements-engineering/agile/04-backlog-prioritization/` |

### Phase 01: Strategic Vision (3 sub-skills)

| Sub-skill | Directory |
|-----------|-----------|
| `01-prd-generation` | `01-strategic-vision/01-prd-generation/` |
| `02-business-case` | `01-strategic-vision/02-business-case/` |
| `03-vision-statement` | `01-strategic-vision/03-vision-statement/` |

### Phase 03: Design Documentation (4 sub-skills)

| Sub-skill | Directory |
|-----------|-----------|
| `01-high-level-design` | `03-design-documentation/01-high-level-design/` |
| `02-low-level-design` | `03-design-documentation/02-low-level-design/` |
| `03-api-specification` | `03-design-documentation/03-api-specification/` |
| `04-database-design` | `03-design-documentation/04-database-design/` |

## File Structure Per Skill

```
XX-skill-name/
├── SKILL.md        # Frontmatter (name, description) + full instructions
├── logic.prompt    # LLM execution instructions for Claude
└── README.md       # Detailed guidance, examples, anti-patterns
```

## Skill Specifications

### Phase 02 Fix: `05-feature-decomposition/SKILL.md`

- **Standard:** IEEE 830 Clause 5.3.1
- **Input:** `features.md`, `quality_standards.md`
- **Output:** `SRS_Draft.md` Section 3.2
- **Pattern:** Stimulus/response pairs with verifiable "shall" clauses
- **References:** Existing `feature_decomposition.py` and `logic.prompt`

### Phase 02 Agile: `02-acceptance-criteria`

- **Standard:** IEEE 29148 Sec 6.4.5
- **Input:** `../output/user_stories.md`
- **Output:** `../output/acceptance_criteria.md`
- **Pattern:** Gherkin Given-When-Then format
- **Key rule:** 3-5 criteria per story, each with deterministic pass/fail

### Phase 02 Agile: `03-story-mapping`

- **Standard:** IEEE 29148, Jeff Patton Story Mapping (2014)
- **Input:** `../output/user_stories.md`, `../output/epic_breakdown.md`
- **Output:** `../output/story_map.md`, `../output/story_map.mmd`
- **Pattern:** Backbone (user activities) → Walking Skeleton → Release slices

### Phase 02 Agile: `04-backlog-prioritization`

- **Standard:** IEEE 29148 Sec 6.4.6
- **Input:** `../output/user_stories.md`, `../project_context/vision.md`
- **Output:** `../output/prioritized_backlog.md`, `../output/release_plan.md`
- **Pattern:** MoSCoW classification + WSJF scoring + sprint allocation

### Phase 01: `01-prd-generation`

- **Standard:** IEEE 29148, IEEE 1233
- **Input:** `vision.md`, `features.md`, `stakeholders.md`
- **Output:** `../output/PRD.md`
- **Sections:** Market context, objectives, success metrics, feature priority matrix, constraints, assumptions

### Phase 01: `02-business-case`

- **Standard:** IEEE 1058
- **Input:** `vision.md`, `stakeholders.md`
- **Output:** `../output/Business_Case.md`
- **Sections:** Problem statement, proposed solution, cost-benefit analysis, ROI projection, risk assessment, go/no-go criteria

### Phase 01: `03-vision-statement`

- **Standard:** IEEE 29148 Sec 6.2
- **Input:** `vision.md`, `stakeholders.md`, `glossary.md`
- **Output:** `../output/Vision_Statement.md`
- **Sections:** Elevator pitch, product positioning, value propositions, target audience, success criteria, scope boundaries

### Phase 03: `01-high-level-design`

- **Standard:** IEEE 1016-2009 Sec 5
- **Input:** `../output/SRS_Draft.md`, `../project_context/tech_stack.md`
- **Output:** `../output/HLD.md`
- **Sections:** Architecture overview, component diagram, deployment diagram, data flow, technology decisions, integration points

### Phase 03: `02-low-level-design`

- **Standard:** IEEE 1016-2009 Sec 6
- **Input:** `../output/HLD.md`, `../output/SRS_Draft.md`, `../project_context/business_rules.md`
- **Output:** `../output/LLD.md`
- **Sections:** Module specifications, class diagrams, sequence diagrams, state machines, algorithm detail, error handling

### Phase 03: `03-api-specification`

- **Standard:** OpenAPI 3.0, IEEE 29148
- **Input:** `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/tech_stack.md`
- **Output:** `../output/API_Specification.md`, `../output/openapi.yaml`
- **Sections:** Endpoints, request/response schemas, authentication, error codes, rate limits, versioning

### Phase 03: `04-database-design`

- **Standard:** IEEE 1016 Sec 6.7
- **Input:** `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/business_rules.md`
- **Output:** `../output/Database_Design.md`, `../output/erd.mmd`
- **Sections:** ERD, normalization analysis, table definitions, indexes, constraints, migration strategy, data dictionary
- **Mandatory skill:** Must reference `skills/mysql-best-practices/`

## Execution Order

### Build Sequence

```
1. Phase 02 fixes (dependency: none)
   a. 05-feature-decomposition SKILL.md
   b. 02-acceptance-criteria
   c. 03-story-mapping
   d. 04-backlog-prioritization

2. Phase 01 (dependency: none, but logically first in pipeline)
   a. 03-vision-statement
   b. 01-prd-generation
   c. 02-business-case

3. Phase 03 (dependency: Phase 02 SRS outputs)
   a. 01-high-level-design
   b. 02-low-level-design
   c. 03-api-specification
   d. 04-database-design
```

### Runtime Dependency Chain

```
Phase 01: 03-vision → 01-prd → 02-business-case
Phase 02 Waterfall: 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08
Phase 02 Agile: 01 → 02 → 03 → 04
Phase 03: 01-hld → 02-lld, 03-api-spec, 04-db-design
```

## Quality Standards

- All skills reference IEEE/ISO clause numbers
- All SKILL.md files follow existing frontmatter + section pattern
- All logic.prompt files use "shall" language and active voice
- No subjective adjectives without measurable metrics
- 500-line hard limit on all .md files
- LaTeX for mathematical expressions where applicable

## Post-Build Updates

After building all skills:
1. Update `skill_overview.md` with new I/O mappings
2. Update `docs/CHANGELOG.md` with v3.2 entry
3. Update `README.md` roadmap to reflect completed phases
4. Update `PROJECT_BRIEF.md` with new capabilities

## Deliverables

- 11 new skill directories (33 files total: 11 SKILL.md + 11 logic.prompt + 11 README.md)
- 1 fixed SKILL.md (feature-decomposition)
- Updated documentation (skill_overview, CHANGELOG, README, PROJECT_BRIEF)

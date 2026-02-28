# Documentation Skills Expansion Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build 11 new documentation skills across Phases 01-03 and fix Phase 02 gaps, bringing the SDLC-Docs-Engine from ~23% to ~50% implementation coverage.

**Architecture:** Each skill consists of 3 files: `SKILL.md` (frontmatter + structured guidance following waterfall pattern), `logic.prompt` (direct AI execution instructions with numbered steps), and `README.md` (human-readable objective, execution steps, quality reminders). All skills read from `../project_context/` and write to `../output/`. Stateless design — no project data stored in submodule.

**Tech Stack:** Markdown, Mermaid diagrams, IEEE/ISO standards (830, 1012, 1016, 1233, 29148, 25010, 25023, 610.12), OpenAPI 3.0 for API specification skill.

---

## Group A: Phase 02 Fixes

### Task 1: Create `05-feature-decomposition/SKILL.md`

**Files:**
- Create: `02-requirements-engineering/waterfall/05-feature-decomposition/SKILL.md`

**Step 1: Write the SKILL.md**

Follow the exact pattern from `04-interface-specification/SKILL.md` (short metadata-focused format). Reference the existing `feature_decomposition.py` and `logic.prompt`.

```markdown
---
name: feature-decomposition
description: Convert features.md into IEEE 830 Section 3.2 (Functional Requirements) using a Functional Decomposition Tree with stimulus/response pairs and verifiable "shall" clauses.
---

# Feature Decomposition Skill Guidance

## Overview
Use this skill after Sections 1.0–3.1 are generated. It transforms the feature catalog into Section 3.2 of the SRS, ensuring each feature is decomposed into description/priority, stimulus/response sequences, and atomic functional requirements with a single "shall" per clause.

## Quick Reference
- Inputs: `../project_context/features.md`, `../project_context/quality_standards.md`
- Output: `../output/SRS_Draft.md` (Section 3.2 only)
- Tone: Precise, atomic, stimulus/response oriented. Each requirement uses exactly one "shall" and references ISO/IEC 25010 Functional Suitability where applicable.

## Core Instructions
1. Run `python feature_decomposition.py` from this directory or invoke the `logic.prompt` through your skill runner.
2. Read each feature from `features.md` and decompose it into subsections numbered 3.2.x containing: 3.2.x.1 Description and Priority (Essential/Conditional/Optional with ISO/IEC 25010 linkage), 3.2.x.2 Stimulus/Response Sequences (numbered pairs derived from user stories), and 3.2.x.3 Functional Requirements (behavior + error handling, one "shall" per clause).
3. Reference ISO/IEC 25010 Functional Suitability guidance from `quality_standards.md` when writing feature descriptions. Avoid subjective qualifiers.
4. Replace only Section 3.2 in `../output/SRS_Draft.md` with the new content, preserving all other sections.
5. Validate that every requirement is atomic and verifiable — a deterministic test case must exist for each "shall" clause.

## Resources
- `README.md`: Explains the Functional Decomposition Tree intent and quality expectations.
- `feature_decomposition.py`: Automation script that reads features, builds the decomposition tree, and writes Section 3.2.
- `logic.prompt`: LLM instructions for orchestrating the decomposition with ISO/IEC traceability and anti-filler enforcement.
```

**Step 2: Verify file consistency**

Confirm `SKILL.md` references match existing files in the directory (`feature_decomposition.py`, `logic.prompt`, `README.md`).

**Step 3: Commit**

```bash
git add 02-requirements-engineering/waterfall/05-feature-decomposition/SKILL.md
git commit -m "fix: Add missing SKILL.md for feature-decomposition (waterfall phase 05)"
```

---

### Task 2: Create `02-acceptance-criteria` Agile Sub-phase

**Files:**
- Create: `02-requirements-engineering/agile/02-acceptance-criteria/SKILL.md`
- Create: `02-requirements-engineering/agile/02-acceptance-criteria/logic.prompt`
- Create: `02-requirements-engineering/agile/02-acceptance-criteria/README.md`

**Step 1: Create directory**

```bash
mkdir -p 02-requirements-engineering/agile/02-acceptance-criteria
```

**Step 2: Write SKILL.md**

Frontmatter pattern matching waterfall skills. Content covers:
- Name: `acceptance-criteria`
- Description: Formalize Given-When-Then acceptance criteria for user stories per IEEE 29148
- Standard: IEEE 29148 Sec 6.4.5
- Inputs: `../output/user_stories.md`, `../project_context/quality_standards.md` (optional for NFR criteria)
- Output: `../output/acceptance_criteria.md`
- Pattern: Gherkin Given-When-Then, 3-5 criteria per story, deterministic pass/fail
- Sections: Overview, Quick Reference, When to Use, Input Files table, Output Files table, Process Workflow (Mermaid), Core Instructions (6 steps), Output Format Specification, Common Pitfalls, Verification Checklist, Integration with Other Phases, Standards Compliance
- Integration: Upstream = `01-user-story-generation`, Downstream = `05-testing-documentation/`, `03-story-mapping`

**Step 3: Write logic.prompt**

Numbered steps following waterfall pattern:
1. Read `../output/user_stories.md`, log file path
2. For each user story (US-XXX), extract the "As a / I want / So that" triad
3. Generate 3-5 acceptance criteria per story in Gherkin format: `Given [precondition], When [action], Then [expected result]`
4. If `quality_standards.md` exists, append NFR acceptance criteria (performance, security thresholds)
5. Validate each criterion is deterministic (binary pass/fail, no subjective language)
6. Flag stories with `[AC-FAIL]` if criteria cannot be made testable
7. Write `../output/acceptance_criteria.md` with story cross-references
8. Log count of stories processed, criteria generated, and any failures

**Step 4: Write README.md**

Follow waterfall README pattern:
- Objective: 2-3 sentences
- Execution Steps: 3-4 numbered steps
- Quality Reminder: 2-3 sentences on Gherkin precision

**Step 5: Commit**

```bash
git add 02-requirements-engineering/agile/02-acceptance-criteria/
git commit -m "feat: Add acceptance-criteria skill (agile phase 02)"
```

---

### Task 3: Create `03-story-mapping` Agile Sub-phase

**Files:**
- Create: `02-requirements-engineering/agile/03-story-mapping/SKILL.md`
- Create: `02-requirements-engineering/agile/03-story-mapping/logic.prompt`
- Create: `02-requirements-engineering/agile/03-story-mapping/README.md`

**Step 1: Create directory**

```bash
mkdir -p 02-requirements-engineering/agile/03-story-mapping
```

**Step 2: Write SKILL.md**

- Name: `story-mapping`
- Description: Build Jeff Patton story maps with backbone activities, walking skeleton, and release slices per IEEE 29148
- Standard: IEEE 29148, Jeff Patton Story Mapping (2014)
- Inputs: `../output/user_stories.md`, `../output/epic_breakdown.md`
- Output: `../output/story_map.md`, `../output/story_map.mmd` (Mermaid)
- Sections: Overview, Quick Reference, Core Instructions (map user activities to backbone, identify walking skeleton/MVP slice, assign stories to release slices, generate Mermaid diagram), Output Format (story_map.md with narrative + story_map.mmd with visual), Verification Checklist, Integration

**Step 3: Write logic.prompt**

1. Read `../output/user_stories.md` and `../output/epic_breakdown.md`
2. Identify user activities (backbone) from epic groupings
3. Map stories under their activity columns, ordered by priority
4. Define Walking Skeleton (minimal end-to-end flow) from Critical priority stories
5. Slice remaining stories into Release 1 (MVP), Release 2, Release 3
6. Generate `story_map.md` with narrative tables showing activities × releases
7. Generate `story_map.mmd` Mermaid diagram with subgraphs per activity and release slice markers
8. Log activities identified, stories mapped, and release slice counts

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 02-requirements-engineering/agile/03-story-mapping/
git commit -m "feat: Add story-mapping skill (agile phase 03)"
```

---

### Task 4: Create `04-backlog-prioritization` Agile Sub-phase

**Files:**
- Create: `02-requirements-engineering/agile/04-backlog-prioritization/SKILL.md`
- Create: `02-requirements-engineering/agile/04-backlog-prioritization/logic.prompt`
- Create: `02-requirements-engineering/agile/04-backlog-prioritization/README.md`

**Step 1: Create directory**

```bash
mkdir -p 02-requirements-engineering/agile/04-backlog-prioritization
```

**Step 2: Write SKILL.md**

- Name: `backlog-prioritization`
- Description: Prioritize the product backlog using MoSCoW classification and WSJF scoring, then allocate stories to sprints with a release plan per IEEE 29148
- Standard: IEEE 29148 Sec 6.4.6, SAFe WSJF
- Inputs: `../output/user_stories.md`, `../project_context/vision.md`, `../output/story_map.md` (optional)
- Output: `../output/prioritized_backlog.md`, `../output/release_plan.md`
- Core Instructions: MoSCoW classification (Must/Should/Could/Won't), WSJF scoring (Business Value / Time Criticality / Risk Reduction / Job Size), sprint capacity allocation, dependency sequencing, release plan generation
- Verification: Every Must-have story assigned to a sprint, WSJF scores calculated, no circular dependencies

**Step 3: Write logic.prompt**

1. Read `../output/user_stories.md` and `../project_context/vision.md`
2. Classify each story using MoSCoW: Must Have (blocks MVP), Should Have (significant value), Could Have (nice-to-have), Won't Have (future)
3. Calculate WSJF score for each story: `WSJF = (Business Value + Time Criticality + Risk Reduction) / Job Size`
4. Sort stories by WSJF within each MoSCoW category
5. Allocate to sprints using assumed velocity (20 points/sprint default, adjustable)
6. Check dependency ordering — move blockers earlier
7. Generate `prioritized_backlog.md` with MoSCoW table + WSJF scores
8. Generate `release_plan.md` with sprint-by-sprint allocation and milestone dates
9. Log classification counts, velocity assumption, sprint count

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 02-requirements-engineering/agile/04-backlog-prioritization/
git commit -m "feat: Add backlog-prioritization skill (agile phase 04)"
```

---

## Group B: Phase 01 — Strategic Vision

### Task 5: Create Phase 01 directory and `03-vision-statement`

**Files:**
- Create: `01-strategic-vision/README.md`
- Create: `01-strategic-vision/03-vision-statement/SKILL.md`
- Create: `01-strategic-vision/03-vision-statement/logic.prompt`
- Create: `01-strategic-vision/03-vision-statement/README.md`

**Step 1: Create directories**

```bash
mkdir -p 01-strategic-vision/03-vision-statement
```

**Step 2: Write Phase 01 README.md**

Brief phase-level README explaining the 3 sub-skills and execution order: Vision Statement → PRD → Business Case.

**Step 3: Write 03-vision-statement/SKILL.md**

- Name: `vision-statement`
- Description: Generate a formal project vision document with elevator pitch, product positioning, value propositions, and success criteria per IEEE 29148 Sec 6.2
- Standard: IEEE 29148-2018 Sec 6.2 (Stakeholder Requirements Definition)
- Inputs: `../project_context/vision.md`, `../project_context/stakeholders.md`, `../project_context/glossary.md`
- Output: `../output/Vision_Statement.md`
- Sections produced in output:
  1. Elevator Pitch (2-3 sentences)
  2. Product Positioning Statement (For [target], Who [need], The [product] is a [category], That [key benefit], Unlike [alternative], Our product [differentiator])
  3. Value Propositions (3-5 measurable propositions)
  4. Target Audience (from stakeholders.md, with user segments)
  5. Success Criteria (SMART: Specific, Measurable, Achievable, Relevant, Time-bound)
  6. Scope Boundaries (In-scope vs Out-of-scope, with rationale)
  7. Key Assumptions and Risks

**Step 4: Write logic.prompt**

1. Read `../project_context/vision.md`, `stakeholders.md`, `glossary.md`. Log paths.
2. Extract Problem Statement, Target Users, Business Goals, Constraints from vision.md
3. Map stakeholders to user segments from stakeholders.md
4. Generate Elevator Pitch: 2-3 sentences, active voice, no marketing fluff
5. Generate Product Positioning using Geoffrey Moore's template
6. Generate 3-5 Value Propositions with measurable outcomes
7. Define Success Criteria using SMART framework, each with metric and timeline
8. Define Scope Boundaries: explicit In/Out with rationale for exclusions
9. List Assumptions (things taken as true) and Risks (things that could derail)
10. Write to `../output/Vision_Statement.md`, log sections generated

**Step 5: Write README.md**

**Step 6: Commit**

```bash
git add 01-strategic-vision/
git commit -m "feat: Add vision-statement skill (strategic vision phase 01.03)"
```

---

### Task 6: Create `01-prd-generation`

**Files:**
- Create: `01-strategic-vision/01-prd-generation/SKILL.md`
- Create: `01-strategic-vision/01-prd-generation/logic.prompt`
- Create: `01-strategic-vision/01-prd-generation/README.md`

**Step 1: Create directory**

```bash
mkdir -p 01-strategic-vision/01-prd-generation
```

**Step 2: Write SKILL.md**

- Name: `prd-generation`
- Description: Generate a Product Requirements Document with market context, objectives, success metrics, and feature priority matrix per IEEE 29148 and IEEE 1233
- Standard: IEEE 29148-2018, IEEE 1233-1998
- Inputs: `../project_context/vision.md`, `../project_context/features.md`, `../project_context/stakeholders.md`, `../output/Vision_Statement.md` (if exists)
- Output: `../output/PRD.md`
- Sections produced:
  1. Document Header (project name, version, date, authors)
  2. Executive Summary
  3. Market Context (problem space, market landscape, competitive analysis)
  4. Product Objectives (SMART goals aligned with vision)
  5. Target Users and Personas (from stakeholders)
  6. Feature Priority Matrix (table: Feature | Priority | Effort | Value | MoSCoW)
  7. Success Metrics (KPIs with baselines and targets)
  8. Constraints and Dependencies
  9. Release Strategy (phased rollout or MVP approach)
  10. Appendix: Standards Traceability (IEEE 29148, IEEE 1233 clause mapping)

**Step 3: Write logic.prompt**

1. Read vision.md, features.md, stakeholders.md. Optionally read Vision_Statement.md if exists. Log paths.
2. Generate Executive Summary: 1 paragraph distilling the product purpose and key value
3. Generate Market Context: problem space from vision.md Problem Statement, competitive landscape (infer from domain)
4. Generate Product Objectives: align each objective with a business goal from vision.md, use SMART format
5. Generate Feature Priority Matrix: table with all features from features.md, assign Priority (Critical/High/Medium/Low), Effort (S/M/L/XL), Value (High/Medium/Low), MoSCoW classification
6. Generate Success Metrics: 3-5 KPIs with baseline (current state) and target (desired state) and timeline
7. List Constraints from vision.md Constraints section, add Dependencies (external systems, APIs, third-party)
8. Generate Release Strategy: map features to releases/sprints based on priority
9. Write to `../output/PRD.md`. Log section count and feature count.

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 01-strategic-vision/01-prd-generation/
git commit -m "feat: Add PRD generation skill (strategic vision phase 01.01)"
```

---

### Task 7: Create `02-business-case`

**Files:**
- Create: `01-strategic-vision/02-business-case/SKILL.md`
- Create: `01-strategic-vision/02-business-case/logic.prompt`
- Create: `01-strategic-vision/02-business-case/README.md`

**Step 1: Create directory**

```bash
mkdir -p 01-strategic-vision/02-business-case
```

**Step 2: Write SKILL.md**

- Name: `business-case`
- Description: Generate a business case document with problem analysis, cost-benefit analysis, ROI projection, risk assessment, and go/no-go criteria per IEEE 1058
- Standard: IEEE 1058-1998 (Software Project Management Plans)
- Inputs: `../project_context/vision.md`, `../project_context/stakeholders.md`, `../output/PRD.md` (if exists)
- Output: `../output/Business_Case.md`
- Sections produced:
  1. Executive Summary
  2. Problem Statement (current state, pain points, quantified impact)
  3. Proposed Solution (high-level approach, key capabilities)
  4. Cost-Benefit Analysis (development costs, operational costs, revenue/savings projections, using LaTeX for formulas)
  5. ROI Projection ($ROI = \frac{Net Benefits - Costs}{Costs} \times 100$)
  6. Risk Assessment (risk matrix: Probability × Impact, mitigation strategies)
  7. Timeline and Milestones
  8. Go/No-Go Criteria (decision gates with measurable thresholds)
  9. Recommendation

**Step 3: Write logic.prompt**

1. Read vision.md, stakeholders.md. Optionally read PRD.md. Log paths.
2. Generate Problem Statement: extract from vision.md, quantify impact where possible
3. Generate Proposed Solution: summarize from vision.md or PRD.md
4. Generate Cost-Benefit Analysis: use LaTeX for financial formulas. Flag where actual costs are unknown with "[COST-TBD: Requires stakeholder input]"
5. Calculate ROI projection with formula. Flag assumptions.
6. Generate Risk Assessment: 3x3 matrix (Low/Medium/High for Probability and Impact), list top 5 risks with mitigation
7. Generate Timeline: align with PRD release strategy if available
8. Define Go/No-Go Criteria: 3-5 measurable gates (e.g., "MVP demonstrates 80% feature completion within budget")
9. Write to `../output/Business_Case.md`. Log section count.

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 01-strategic-vision/02-business-case/
git commit -m "feat: Add business-case skill (strategic vision phase 01.02)"
```

---

## Group C: Phase 03 — Design Documentation

### Task 8: Create Phase 03 directory and `01-high-level-design`

**Files:**
- Create: `03-design-documentation/README.md`
- Create: `03-design-documentation/01-high-level-design/SKILL.md`
- Create: `03-design-documentation/01-high-level-design/logic.prompt`
- Create: `03-design-documentation/01-high-level-design/README.md`

**Step 1: Create directories**

```bash
mkdir -p 03-design-documentation/01-high-level-design
```

**Step 2: Write Phase 03 README.md**

Phase-level README explaining 4 sub-skills and execution order: HLD → LLD → API Spec + DB Design (parallel).

**Step 3: Write 01-high-level-design/SKILL.md**

- Name: `high-level-design`
- Description: Generate a High-Level Design document with system architecture, component diagrams, deployment topology, data flow, and technology decisions per IEEE 1016-2009
- Standard: IEEE 1016-2009 Sec 5 (Design Viewpoints)
- Inputs: `../output/SRS_Draft.md`, `../project_context/tech_stack.md`, `../output/PRD.md` (optional)
- Output: `../output/HLD.md`
- Sections produced:
  1. Document Header and Design Overview
  2. Architectural Style (monolith, microservices, serverless, etc. — inferred from tech_stack.md)
  3. System Context Diagram (Mermaid: system + external actors/systems)
  4. Component Architecture (Mermaid: internal components and their responsibilities)
  5. Deployment Topology (Mermaid: servers, containers, cloud services, networks)
  6. Data Flow Diagrams (Mermaid: how data moves between components)
  7. Technology Decisions (table: Decision | Options Considered | Choice | Rationale)
  8. Integration Points (external APIs, third-party services, protocols)
  9. Cross-Cutting Concerns (authentication, logging, error handling, caching)
  10. Design Constraints (from SRS Section 3.4)
  11. Traceability to SRS (table: HLD Component → SRS Section → Requirement IDs)

**Step 4: Write logic.prompt**

1. Read `../output/SRS_Draft.md` (all sections), `../project_context/tech_stack.md`. Optionally read `../output/PRD.md`. Log paths.
2. Infer architectural style from tech_stack.md (frameworks, deployment config, database choices)
3. Generate System Context Diagram as Mermaid C4 Context: identify system boundary, external actors (users, systems), and data exchanges
4. Generate Component Architecture as Mermaid diagram: decompose system into layers (presentation, business logic, data access, infrastructure). Each component has: name, responsibility (1 sentence), interfaces (what it exposes)
5. Generate Deployment Topology as Mermaid diagram: map components to infrastructure (servers, containers, cloud services). Include ports, protocols, TLS requirements from SRS Section 3.1
6. Generate Data Flow Diagrams: show how data enters, transforms, and exits the system
7. Generate Technology Decisions table: for each major decision (language, framework, database, hosting), list options considered, choice made, and rationale citing SRS constraints
8. Document Integration Points: external APIs, webhooks, message queues, with protocols and authentication methods
9. Document Cross-Cutting Concerns: auth (from SRS 3.5.3), logging, error handling, caching strategies
10. Generate Traceability table: map each HLD component to SRS sections and requirement IDs
11. Write to `../output/HLD.md`. Log component count, diagram count.

**Step 5: Write README.md**

**Step 6: Commit**

```bash
git add 03-design-documentation/
git commit -m "feat: Add high-level-design skill (design documentation phase 03.01)"
```

---

### Task 9: Create `02-low-level-design`

**Files:**
- Create: `03-design-documentation/02-low-level-design/SKILL.md`
- Create: `03-design-documentation/02-low-level-design/logic.prompt`
- Create: `03-design-documentation/02-low-level-design/README.md`

**Step 1: Create directory**

```bash
mkdir -p 03-design-documentation/02-low-level-design
```

**Step 2: Write SKILL.md**

- Name: `low-level-design`
- Description: Generate a Low-Level Design document with module specifications, class diagrams, sequence diagrams, state machines, and algorithm detail per IEEE 1016-2009
- Standard: IEEE 1016-2009 Sec 6 (Design Elements)
- Inputs: `../output/HLD.md`, `../output/SRS_Draft.md`, `../project_context/business_rules.md`
- Output: `../output/LLD.md`
- Sections produced:
  1. Module Specifications (for each HLD component: classes, functions, data structures)
  2. Class Diagrams (Mermaid classDiagram: attributes, methods, relationships)
  3. Sequence Diagrams (Mermaid sequenceDiagram: key workflows from SRS functional requirements)
  4. State Machine Diagrams (Mermaid stateDiagram: for entities with lifecycle states)
  5. Algorithm Detail (pseudocode or structured English for complex business rules from business_rules.md, LaTeX for formulas)
  6. Error Handling Design (error codes, exception hierarchy, recovery strategies)
  7. Data Validation Rules (input validation per SRS Section 3.1, referencing ISO/IEC 25062)
  8. Traceability to HLD (table: LLD Module → HLD Component → SRS Requirement)

**Step 3: Write logic.prompt**

1. Read `../output/HLD.md`, `../output/SRS_Draft.md`, `../project_context/business_rules.md`. Log paths.
2. For each component in HLD, decompose into modules/classes with responsibilities
3. Generate class diagrams: classes with attributes (typed), methods (parameterized), relationships (inheritance, composition, dependency)
4. Generate sequence diagrams for the 5-8 most critical workflows (derived from SRS Section 3.2 stimulus/response pairs)
5. Generate state machine diagrams for entities with lifecycle (e.g., Order: Created → Confirmed → Shipped → Delivered → Completed)
6. Formalize complex business rules from business_rules.md as structured pseudocode with LaTeX for calculations
7. Design error handling: enumerate error codes, define exception hierarchy, specify recovery behavior
8. Define data validation rules: input constraints, format validation, range checks per ISO/IEC 25062
9. Generate traceability table: LLD Module → HLD Component → SRS Requirement IDs
10. Write to `../output/LLD.md`. Log module count, diagram count, business rules formalized.

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 03-design-documentation/02-low-level-design/
git commit -m "feat: Add low-level-design skill (design documentation phase 03.02)"
```

---

### Task 10: Create `03-api-specification`

**Files:**
- Create: `03-design-documentation/03-api-specification/SKILL.md`
- Create: `03-design-documentation/03-api-specification/logic.prompt`
- Create: `03-design-documentation/03-api-specification/README.md`

**Step 1: Create directory**

```bash
mkdir -p 03-design-documentation/03-api-specification
```

**Step 2: Write SKILL.md**

- Name: `api-specification`
- Description: Generate API specification with endpoint definitions, request/response schemas, authentication, error codes, and an OpenAPI 3.0 YAML artifact per IEEE 29148 and OpenAPI 3.0
- Standard: OpenAPI 3.0 Specification, IEEE 29148-2018
- Inputs: `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/tech_stack.md`
- Output: `../output/API_Specification.md`, `../output/openapi.yaml`
- Sections in API_Specification.md:
  1. API Overview (base URL, versioning strategy, content types)
  2. Authentication and Authorization (from SRS 3.5.3, reference `dual-auth-rbac` skill if applicable)
  3. Endpoint Reference (grouped by resource: Method, Path, Description, Request Body, Response, Status Codes)
  4. Request/Response Schemas (JSON Schema definitions with types, constraints, examples)
  5. Error Response Format (standardized error object, reference `api-error-handling` skill)
  6. Rate Limiting and Throttling (from SRS 3.3 Performance Requirements)
  7. Pagination (reference `api-pagination` skill pattern)
  8. Versioning Strategy (URL path vs header vs query parameter)
  9. CORS and Security Headers
  10. Traceability (Endpoint → SRS Requirement → HLD Component)
- openapi.yaml: Valid OpenAPI 3.0 document generated from the specification

**Step 3: Write logic.prompt**

1. Read `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/tech_stack.md`. Log paths.
2. Extract entities and operations from SRS Section 3.2 (functional requirements) to identify API resources
3. Map CRUD operations to HTTP methods: Create=POST, Read=GET, Update=PUT/PATCH, Delete=DELETE
4. Define authentication scheme from SRS Section 3.5.3 (JWT Bearer, Session, API Key)
5. For each endpoint: define path parameters, query parameters, request body schema (JSON), response schema (JSON), status codes (200, 201, 400, 401, 403, 404, 422, 500)
6. Define standardized error response: `{ "success": false, "error": { "code": "string", "message": "string", "details": [] } }`
7. Define rate limits from SRS 3.3 performance requirements
8. Define pagination format: cursor-based or offset-based with `page`, `per_page`, `total`, `data[]`
9. Generate `../output/API_Specification.md` with all sections
10. Generate `../output/openapi.yaml` as valid OpenAPI 3.0 YAML
11. Log endpoint count, schema count, resource count.

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 03-design-documentation/03-api-specification/
git commit -m "feat: Add API specification skill (design documentation phase 03.03)"
```

---

### Task 11: Create `04-database-design`

**Files:**
- Create: `03-design-documentation/04-database-design/SKILL.md`
- Create: `03-design-documentation/04-database-design/logic.prompt`
- Create: `03-design-documentation/04-database-design/README.md`

**Step 1: Create directory**

```bash
mkdir -p 03-design-documentation/04-database-design
```

**Step 2: Write SKILL.md**

- Name: `database-design`
- Description: Generate a database design document with ERD, normalization analysis, table definitions, indexes, constraints, migration strategy, and data dictionary per IEEE 1016 Sec 6.7 with mandatory mysql-best-practices integration
- Standard: IEEE 1016-2009 Sec 6.7 (Interface Design), ISO/IEC 25010
- Mandatory skill reference: `skills/mysql-best-practices/` (per CLAUDE.md requirement)
- Inputs: `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/business_rules.md`, `../project_context/tech_stack.md`
- Output: `../output/Database_Design.md`, `../output/erd.mmd` (Mermaid ERD)
- Sections produced:
  1. Database Overview (RDBMS choice, version, charset, collation from tech_stack.md)
  2. Entity-Relationship Diagram (Mermaid erDiagram with cardinality)
  3. Normalization Analysis (1NF → 2NF → 3NF verification, denormalization justification where needed)
  4. Table Definitions (for each table: columns with type, nullable, default, constraints, indexes)
  5. Relationships and Foreign Keys (cascade rules, referential integrity)
  6. Indexing Strategy (primary, unique, composite, full-text — with rationale)
  7. Data Dictionary (table: Field | Type | Description | Constraints | Example)
  8. Migration Strategy (versioned migrations, rollback procedures)
  9. Multi-Tenancy Considerations (if applicable, from SRS/HLD)
  10. Performance Considerations (query optimization, partitioning, caching)
  11. Traceability (Table → SRS Entity → HLD Component)

**Step 3: Write logic.prompt**

1. Read `../output/SRS_Draft.md`, `../output/HLD.md`, `../project_context/business_rules.md`, `../project_context/tech_stack.md`. Log paths.
2. Determine database platform from tech_stack.md (MySQL 8.x vs PostgreSQL). Apply `skills/mysql-best-practices/` rules if MySQL.
3. Extract entities from SRS Section 3.2 (functional requirements) and Section 2.0 (data objects)
4. Generate ERD as Mermaid erDiagram: entities with attributes and typed fields, relationships with cardinality (one-to-one, one-to-many, many-to-many with junction tables)
5. Verify normalization: check 1NF (atomic values), 2NF (no partial dependencies), 3NF (no transitive dependencies). Document any intentional denormalization with rationale.
6. Generate table definitions: column name, data type (use DECIMAL(19,4) for monetary values per logic-modeling skill), nullable, default value, constraints (PK, FK, UNIQUE, CHECK)
7. Define indexes: primary key (every table), unique indexes (natural keys), composite indexes (common query patterns), full-text indexes (search fields)
8. Generate Data Dictionary: every field across all tables with type, description, constraints, example value
9. Define migration strategy: numbered migration files, up/down procedures, data seeding
10. If multi-tenant: define tenant isolation strategy (shared DB with tenant_id, separate schemas, or separate DBs)
11. Write `../output/Database_Design.md` and `../output/erd.mmd`. Log table count, column count, relationship count.

**Step 4: Write README.md**

**Step 5: Commit**

```bash
git add 03-design-documentation/04-database-design/
git commit -m "feat: Add database-design skill (design documentation phase 03.04)"
```

---

## Group D: Post-Build Updates

### Task 12: Update skill_overview.md

**Files:**
- Modify: `skill_overview.md`

**Step 1: Add new rows to the pipeline registry table**

Add entries for all 11 new skills (3 agile sub-phases, 3 strategic vision, 4 design documentation) with their Inputs, Process Logic, Governing Standard, and Primary Output columns.

Add a new section for Phase 01 and Phase 03 entries.

**Step 2: Commit**

```bash
git add skill_overview.md
git commit -m "docs: Update skill pipeline registry with phases 01-03 skills"
```

---

### Task 13: Update documentation files

**Files:**
- Modify: `docs/CHANGELOG.md`
- Modify: `README.md`
- Modify: `PROJECT_BRIEF.md`

**Step 1: Update CHANGELOG.md**

Add v3.2.0 entry with all new skills listed, grouped by phase. Include date and change descriptions.

**Step 2: Update README.md**

Update the roadmap section to mark v3.2 items as complete. Update the repository structure section to reflect new phase directories.

**Step 3: Update PROJECT_BRIEF.md**

Add Phase 01 and Phase 03 to the "What Can It Generate" section. Update completion statistics.

**Step 4: Commit**

```bash
git add docs/CHANGELOG.md README.md PROJECT_BRIEF.md
git commit -m "docs: Update documentation for v3.2 release (phases 01-03)"
```

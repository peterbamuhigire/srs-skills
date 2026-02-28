# Skill Pipeline Registry

This registry documents the inputs, process logic, governing standards, and outputs for each skill in the SRS-Skills pipeline. It is formatted as an Engineering Interface Control Document to ensure compliance with ISO/IEC 15504 and IEEE 1002 taxonomy requirements.

| Skill ID & Name | Inputs | Process Logic | Governing Standard | Primary Output |
|-----------------|--------|----------------|-------------------|----------------|
| 01-initialize-srs | User input, existing context, project anchors | Populate ../project_context/ with IEEE/ISO-driven templates, ensuring baseline artifacts and seeds exist | ISO/IEC 15504 – Process Assessment Framework; IEEE 1074 – Software Life Cycle Process | Seeded templates in ../project_context/ (vision.md, tech_stack.md, features.md, business_rules.md, quality_standards.md, glossary.md) |
| 02-context-engineering | ../project_context/vision.md, glossary.md | Synthesize Introduction, Purpose, and Definition sections guided by stakeholder vision and terminology | IEEE 830 Clause 5.1 – Introduction | ../output/SRS_Draft.md Section 1.0 (Purpose, Scope, Definitions) |
| 03-descriptive-modeling | ../project_context/tech_stack.md, features.md | Map environment, constraints, and capability descriptions, aligning system context with feature candidates | IEEE 830 Clause 5.2 – Overall Description | ../output/SRS_Draft.md Section 2.0 (Overall Description, System Overview) |
| 04-interface-specification | ../project_context/tech_stack.md | Conduct connectivity and interface audit versus infrastructure stack, documenting protocols and interoperability controls | IEEE 1233 – System Requirements Development; ISO/IEC 25051 – Software Product Quality Requirements | ../output/SRS_Draft.md Section 3.1 (External Interfaces) |
| 05-feature-decomposition | ../project_context/features.md | Break down functional capabilities into stimulus/response pairs with verifiable SHALL statements | IEEE 830 Clause 5.3.1 – Functional Requirements (Feature-Based) | ../output/SRS_Draft.md Section 3.2 (Functional Requirements) |
| 06-logic-modeling | ../project_context/business_rules.md | Formalize algorithms, formulas, and decision tables (LaTeX where appropriate), capturing logic invariants for requirements | IEEE 1016 – Standards for Software Design Descriptions (Logic Mapping) | ../output/SRS_Draft.md Sections 3.2.x (Data/Logic Details) |
| 07-attribute-mapping | ../project_context/quality_standards.md | Enforce NFR metrics, describing performance, security, reliability, and other quality attributes with traceable targets | ISO/IEC 25010 – Software Product Quality | ../output/SRS_Draft.md Sections 3.3–3.6 (Attribute-based Requirements) |
| 08-semantic-auditing | ../output/SRS_Draft.md (full draft) | Validate completeness, consistency, and traceability; generate audit report and requirements traceability matrix | IEEE 1012 – Verification & Validation | ../output/Traceability_Matrix.md and Audit_Report.md (plus updated SRS draft sections) |

## Phase 01: Strategic Vision

| Skill ID & Name | Inputs | Process Logic | Governing Standard | Primary Output |
|-----------------|--------|----------------|-------------------|----------------|
| 03-vision-statement | ../project_context/vision.md, stakeholders.md, glossary.md | Generate formal vision document with elevator pitch, product positioning (Geoffrey Moore template), value propositions, and SMART success criteria | IEEE 29148-2018 Sec 6.2 – Stakeholder Requirements Definition | ../output/Vision_Statement.md |
| 01-prd-generation | ../project_context/vision.md, features.md, stakeholders.md; optionally ../output/Vision_Statement.md | Generate Product Requirements Document with market context, SMART objectives, feature priority matrix (MoSCoW), and success metrics | IEEE 29148-2018; IEEE 1233-1998 – System Requirements Development | ../output/PRD.md |
| 02-business-case | ../project_context/vision.md, stakeholders.md; optionally ../output/PRD.md | Generate business case with cost-benefit analysis (NPV), ROI projection, risk assessment matrix, and go/no-go criteria | IEEE 1058-1998 – Software Project Management Plans | ../output/Business_Case.md |

## Phase 02: Agile Requirements Track

| Skill ID & Name | Inputs | Process Logic | Governing Standard | Primary Output |
|-----------------|--------|----------------|-------------------|----------------|
| 01-user-story-generation | ../project_context/vision.md, features.md, personas.md | Transform features into INVEST-compliant user stories with acceptance criteria, story points, and epic breakdown | IEEE 29148-2018 Sec 6.4; INVEST Criteria | ../output/user_stories.md, epic_breakdown.md, backlog_summary.md |
| 02-acceptance-criteria | ../output/user_stories.md; optionally ../project_context/quality_standards.md | Formalize Given-When-Then acceptance criteria per story with NFR criteria and testability validation | IEEE 29148-2018 Sec 6.4.5 – Requirements Specification | ../output/acceptance_criteria.md |
| 03-story-mapping | ../output/user_stories.md, epic_breakdown.md | Build Jeff Patton story maps with backbone activities, walking skeleton, and release slices | IEEE 29148-2018; Jeff Patton Story Mapping (2014) | ../output/story_map.md, story_map.mmd |
| 04-backlog-prioritization | ../output/user_stories.md, ../project_context/vision.md | Prioritize backlog using MoSCoW classification and WSJF scoring, allocate stories to sprints | IEEE 29148-2018 Sec 6.4.6; SAFe WSJF | ../output/prioritized_backlog.md, release_plan.md |

## Phase 03: Design Documentation

| Skill ID & Name | Inputs | Process Logic | Governing Standard | Primary Output |
|-----------------|--------|----------------|-------------------|----------------|
| 01-high-level-design | ../output/SRS_Draft.md, ../project_context/tech_stack.md | Generate system architecture with component, deployment, and data flow diagrams (Mermaid), technology decisions, and traceability | IEEE 1016-2009 Sec 5 – Design Viewpoints | ../output/HLD.md |
| 02-low-level-design | ../output/HLD.md, SRS_Draft.md, ../project_context/business_rules.md | Decompose HLD into module specs with class, sequence, and state diagrams (Mermaid), algorithm formalization (LaTeX), error handling design | IEEE 1016-2009 Sec 6 – Design Elements | ../output/LLD.md |
| 03-api-specification | ../output/SRS_Draft.md, HLD.md, ../project_context/tech_stack.md | Generate REST API endpoint definitions, schemas, auth, error format, and machine-readable OpenAPI 3.0 YAML | OpenAPI 3.0; IEEE 29148-2018; RFC 7231 | ../output/API_Specification.md, openapi.yaml |
| 04-database-design | ../output/SRS_Draft.md, HLD.md, ../project_context/business_rules.md, tech_stack.md | Generate ERD (Mermaid), normalized table definitions, indexing strategy, data dictionary, migration strategy. MANDATORY: mysql-best-practices for MySQL | IEEE 1016-2009 Sec 6.7; ISO/IEC 25010 | ../output/Database_Design.md, erd.mmd |

## Verification Gateways

1. Each skill ingests the output of the preceding phase as its baseline artifact (e.g., Skill 02 uses the vision/glossary created by Skill 01). This ensures traceability of inputs back to original templates.
2. Skill 05 requires the Feature catalog generated by Skills 01–03; Skill 06 and Skill 07 enforce data/logic and quality attributes flowing from Skill 05 definitions.
3. Skill 08 performs the terminal verification gate: it reads the entire SRS draft produced by Skills 02–07, confirms compliance with the cited standards, and emits the traceability matrix plus audit report. Passing Skill 08 is mandatory before any new iteration of Skill 01 to preserve integrity across the pipeline.
4. Phase 01 (Strategic Vision) produces Vision_Statement.md and PRD.md that feed into Phase 02 as upstream context. Business_Case.md provides the go/no-go decision gate.
5. Phase 02 Agile track skills execute sequentially: user stories → acceptance criteria → story mapping → backlog prioritization. Each consumes the prior skill's output.
6. Phase 03 (Design Documentation) requires Phase 02 outputs (SRS_Draft.md or user_stories.md). HLD runs first; LLD, API Spec, and Database Design can run in parallel after HLD completes. Each design artifact traces back to SRS requirements.

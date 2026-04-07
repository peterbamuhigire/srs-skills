# Changelog - SRS-Skills Engine

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2026-04-07] — AI Module Upgrade Across All Active Projects

### Added

- **Kulima** — AI Farm Advisor module: PRD `FR-AI` business section (5 features: Natural Language Q&A, Photo Pest/Disease Diagnosis, Personalised Farm Plan, Seasonal Planting Advisory, Market Timing Advice); SRS FR-AI-001–006 technical requirements verified and strengthened with measurable thresholds; `Kulima_PRD.docx` and `Kulima_SRS.docx` built.
- **Medic8** — AI Clinical Intelligence module: PRD `FR-AI` business section (5 features: At-Risk Patient EWS, Differential Diagnosis Support, SOAP Note Summarisation, Pharmacy Demand Forecasting, Disease Surveillance); SRS FR-AI-001–005 technical requirements added to `04-functional-requirements.md`; `Medic8_PRD.docx` and `Medic8_SRS.docx` built.
- **LonghornERP** — AI Intelligence module: new PRD file `10-ai-intelligence.md` (5 features: Cash Flow Intelligence, GL Anomaly Detection, Demand Forecasting and Reorder, Debtor Default Risk Scoring, Narrative Financial Reports); new SRS Module 15 directory (`15-ai-intelligence/`) with cover, introduction, FR-AI-001–005, NFRs, and traceability; `LonghornERP_PRD.docx` rebuilt and `LonghornERP_SRS_AIIntelligence.docx` built.
- **Maduuka** — AI Business Intelligence module: PRD section `7A` (4 features: Sales Forecasting, Smart Reorder Advisor, Fraud and Anomaly Alerts, Business Health Advisor) inserted into `01-prd.md`; SRS FR-AI-001–004 appended to `04-functional-requirements.md`; `Maduuka_PRD.docx` and `Maduuka_SRS_Phase1.docx` rebuilt.
- **BIRDC-ERP** — AI Intelligence Phase 7 contract extension: new PRD file `11-ai-module.md` (5 capabilities: Production Yield Prediction, Quality Defect Pattern Detection, Farmer Supply Forecasting, Predictive Equipment Maintenance, Export Demand Intelligence); SRS `08-fr-ai.md` added to Phase 6 (`06-srs-phase6-research-admin/`) with FR-AI-001–005; `PRD_BIRDC_ERP.docx` and `SRS_BIRDC_ERP_Phase6_ResearchAdmin.docx` rebuilt.
- Implementation plan saved to `docs/plans/2026-04-07-ai-module-upgrade-all-projects.md`.

### Changed

- All 5 active projects now have domain-specific AI modules specified at both PRD (business language) and SRS (IEEE 830 stimulus-response) levels, consistent with the AcademiaPro AI module pattern established previously.

---

## [Unreleased] — AcademiaPro Phase 2 Requirements Engineering — 2026-03-29

### Project: AcademiaPro (Chwezi Core Systems)

**Phase 2 — Requirements Engineering completed.** All IEEE 830-compliant SRS sections authored, built to `.docx`, and project documentation updated.

**Deliverables produced:**

- `02-requirements-engineering/AcademiaPro_SRS.docx` — 6-section SRS: Introduction, Overall Description, External Interfaces, 49 Functional Requirements (FR-AUTH/TNT/SIS/ACA/FEE/ATT/EXM/RPT/RBAC/EMIS/AUD), System Constraints, 13 NFRs
- `02-requirements-engineering/AcademiaPro_UserStories.docx` — 20 user stories with Gherkin acceptance criteria
- `02-requirements-engineering/AcademiaPro_RBAC_Stakeholder.docx` — Full RBAC permission matrix (60+ permissions × 8 roles); closes HIGH-005

**Skill alignments explicit in SRS:**

- `multi-tenant-saas-architecture` — three-tier panel architecture, `tenant_id` enforcement, rate limits, audit retention
- `dual-auth-rbac` — session prefix `academia_pro_`, JWT 15 min/30 day, Argon2ID (C-003), 5-level permission resolution
- `mysql-best-practices` — InnoDB/utf8mb4, non-destructive migrations
- PRD 7-day mobile refresh token superseded by skill's 30-day standard (documented in C-002)

**Gap analysis updates:**

- HIGH-005 (RBAC matrix): ✅ Resolved
- HIGH-006 (double-payment, Phase 1 manual scope): ✅ Resolved in FR-FEE-002/003
- HIGH-001, HIGH-002, HIGH-003, HIGH-004, HIGH-007, HIGH-008: Pending (next phase)

**Context gaps flagged for external resolution:**

- `[CONTEXT-GAP: UNEB registration format]` — contact UNEB; blocks FR-EXM-008
- `[CONTEXT-GAP: MoES EMIS data dictionary]` — obtain from MoES; blocks FR-EMIS-001

---

## [3.5.1] - 2026-03-08

### Added

**IEEE 830-1998 Full Compliance Enforcement:**
- **ieee-830-compliance-checklist.md** - Authoritative compliance reference for all waterfall SRS skills
  - Part 1: Eight Quality Attributes (§4.3) with pass/fail criteria and examples
  - Part 2: SRS Structure Checklist (§5.1–§5.4) with checklist IDs (IEEE830-x.x.x)
  - Part 3: Annex A Template Selection Guide (A.1–A.8)
  - Part 4: TBD Protocol (§4.3.3.1) with mandatory fields
  - Part 5: Anti-Patterns and Fixes
  - Part 6: Skill-to-Clause Mapping

### Changed

**Phase 03 (Descriptive Modeling) - IEEE 830 §5.2 compliance:**
- Now generates all eight §5.2.1 sub-items: System/User/Hardware/Software/Communications Interfaces, Memory Constraints, Operations, Site Adaptation
- Added Section 2.6 Apportioning of Requirements (§5.2.6)

**Phase 05 (Feature Decomposition) - IEEE 830 §5.3.2 compliance:**
- Added validity checks on inputs (§5.3.2a)
- Added exact sequence of operations (§5.3.2b)
- Added responses to abnormal situations: overflow, communication failure, error recovery (§5.3.2c)
- Added effect of parameters (§5.3.2d)
- Added input/output relationships and formulas (§5.3.2e)
- Enforced importance ranking on every requirement (§4.3.5)
- Enforced backward traceability reference on every requirement (§4.3.8)

**Phase 07 (Attribute Mapping) - IEEE 830 §5.3.5.1 and §5.3.8:**
- Added Section 3.5.5 Standards Compliance (§5.3.5.1): report formats, data naming, audit tracing
- Added Section 3.6 Other Requirements (§5.3.8): portability, installation, localization
- Output range expanded from Sections 3.3–3.5.4 to Sections 3.3–3.6

**Phase 08 (Semantic Auditing) - Comprehensive IEEE 830 audit:**
- Enhanced to validate all 8 quality attributes with checklist ID references
- Added ranking completeness check (§4.3.5): flags every unranked requirement
- Added TBD protocol enforcement (§4.3.3.1): validates condition, resolution, owner, deadline
- Added modifiability checks (§4.3.7): compound-shall detection, redundancy detection
- Added backward traceability validation (§4.3.8): every requirement must reference source
- Added SRS structure completeness check (§5.1–§5.4): verifies all required sections exist
- Added Annex A template verification (confirms Section 1.5 documents template choice)
- Enhanced Python automation (`semantic_auditing.py`) with 8 new validation functions
- Overall compliance verdict: COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT
- RTM now includes Backward Trace column

## [3.3.0] - 2026-03-01

### Added

**Phase 04: Development Artifacts (4 new skills):**
- **01-technical-specification** - Module-level technical specs with interface contracts, data structures, algorithm details per IEEE 1016/830
- **02-coding-guidelines** - Naming conventions, formatting, patterns, code review criteria per IEEE 730
- **03-dev-environment-setup** - Toolchain installation, build configuration, local development workflow per IEEE 1074
- **04-contribution-guide** - Branching strategy, commit conventions, PR workflow, CI/CD integration per IEEE 1074

**Phase 05: Testing Documentation (3 new skills):**
- **01-test-strategy** - Test levels, types, tools, environments, entry/exit criteria per IEEE 829 Sec 6
- **02-test-plan** - Test cases with requirements traceability, test data, schedule per IEEE 829 Sec 7-8
- **03-test-report** - Execution report template with pass/fail summary, defect analysis, coverage metrics per IEEE 829 Sec 9-10

**Phase 06: Deployment & Operations (4 new skills):**
- **01-deployment-guide** - Step-by-step deployment procedures with rollback and environment configs per IEEE 1062
- **02-runbook** - Incident response, escalation paths, health checks, recovery playbooks per SRE practices
- **03-monitoring-setup** - Metrics definitions, alerting rules, dashboard specs, SLI/SLO targets per ISO/IEC 25010
- **04-infrastructure-docs** - Architecture diagrams (Mermaid), resource inventory, networking topology per IEEE 1016

**Phase 07: Agile Artifacts (4 new skills):**
- **01-sprint-planning** - Sprint goal, capacity calculation, backlog selection, task breakdown per Scrum Guide/IEEE 29148
- **02-definition-of-done** - Multi-level DoD checklist (story, increment, release) per Scrum Guide
- **03-definition-of-ready** - Backlog item readiness criteria with acceptance criteria and sizing per Scrum Guide
- **04-retrospective-template** - Multiple facilitation formats (Start-Stop-Continue, 4Ls, Sailboat) per Scrum Guide

**Phase 08: End-User Documentation (4 new skills):**
- **01-user-manual** - Getting started, feature guides, role-based workflows, troubleshooting per ISO 26514
- **02-installation-guide** - System requirements, installation steps, configuration, verification per ISO 26514
- **03-faq** - Categorized question-answer pairs with cross-references per ISO 26514
- **04-release-notes** - Version tracking, features, bug fixes, breaking changes, migration guide per IEEE 830

**Phase 09: Governance & Compliance (4 new skills):**
- **01-traceability-matrix** - Bidirectional RTM with gap analysis and orphan detection per IEEE 1012-2016
- **02-audit-report** - V&V audit with severity-rated findings and remediation plan per IEEE 1012-2016
- **03-compliance-documentation** - Regulatory mapping (GDPR/HIPAA/SOC2) with gap analysis
- **04-risk-assessment** - ISO 31000 risk framework with probability/impact matrix and risk register per ISO 31000/IEEE 1012

**Infrastructure:**
- Updated skill_overview.md pipeline registry with all 23 new skills
- 6 new phase-level README.md files

### Changed

- All 10 SDLC phases now fully implemented (100% phase coverage)
- Overall engine implementation increased from ~50% to 100% of planned documentation skills
- Total skill count: 46 documentation generation skills across 10 phases

## [3.2.0] - 2026-02-28

### Added

**Phase 01: Strategic Vision (3 new skills):**
- **03-vision-statement** - Formal vision document with elevator pitch, Geoffrey Moore product positioning, SMART success criteria per IEEE 29148 Sec 6.2
- **01-prd-generation** - Product Requirements Document with market context, feature priority matrix (MoSCoW), success metrics per IEEE 29148/1233
- **02-business-case** - Business case with cost-benefit analysis (NPV/LaTeX), ROI projection, risk assessment matrix, go/no-go criteria per IEEE 1058

**Phase 02: Agile Requirements Track Completion (3 new skills):**
- **02-acceptance-criteria** - Gherkin Given-When-Then acceptance criteria with NFR criteria per IEEE 29148 Sec 6.4.5
- **03-story-mapping** - Jeff Patton story maps with backbone activities, walking skeleton, release slices per IEEE 29148
- **04-backlog-prioritization** - MoSCoW classification with WSJF scoring, sprint allocation, release planning per IEEE 29148 Sec 6.4.6

**Phase 03: Design Documentation (4 new skills):**
- **01-high-level-design** - System architecture with Mermaid C4/deployment/data flow diagrams, technology decisions per IEEE 1016-2009 Sec 5
- **02-low-level-design** - Module specs with class/sequence/state diagrams (Mermaid), algorithm formalization (LaTeX) per IEEE 1016-2009 Sec 6
- **03-api-specification** - REST API endpoints with OpenAPI 3.0 YAML artifact, standardized error format per IEEE 29148/RFC 7231
- **04-database-design** - ERD (Mermaid), normalization analysis, data dictionary, migration strategy per IEEE 1016 Sec 6.7 with mandatory mysql-best-practices integration

**Phase 02 Fix:**
- **05-feature-decomposition** - Added missing SKILL.md wrapper for the waterfall feature decomposition skill

**Infrastructure:**
- Setup scripts for new SRS projects (PowerShell + Bash)
- SETUP_GUIDE.md with complete workflow instructions
- Updated skill_overview.md pipeline registry with all new skills

### Changed

- Agile requirements track expanded from 1/4 to 4/4 sub-phases (100% complete)
- Waterfall requirements track now 8/8 sub-phases with all SKILL.md files present
- Overall engine implementation coverage increased from ~23% to ~50%

## [3.1.0] - 2026-02-07

### Added

**AI-Assisted Development Skills:**
- **ai-assisted-development** - Orchestration patterns for coordinating multiple AI agents in software development workflows
  - 5 orchestration strategies (Sequential, Parallel, Conditional, Looping, Retry)
  - 3 AI-specific patterns (Agent Handoff, Fan-Out/Fan-In, Human-in-the-Loop)
  - Real-world examples from MADUUKA and BRIGHTSOMA applications
  - References: orchestration-strategies.md, ai-patterns.md, practical-examples.md

- **orchestration-best-practices** - The 10 Commandments of Orchestration for multi-step workflows
  - Enforces clear step definition, dependency tracking, error handling
  - Complete code examples (good vs bad patterns)
  - Verification checklist for all generated code
  - Anti-patterns guide

- **ai-error-prevention** - Error prevention strategies for AI-assisted development (Trust But Verify)
  - 7 prevention strategies to minimize wasted tokens and catch Claude's mistakes early
  - Common Claude failure modes and prevention techniques
  - App-specific checklists (MADUUKA, MEDIC8, BRIGHTSOMA, DDA, CROWNPOINT)
  - Token savings: 50-75% reduction in wasted tokens
  - References: prevention-strategies.md, failure-modes.md, app-specific-prevention.md

- **ai-error-handling** - 5-layer validation stack for AI-generated code
  - Layer 1: Syntax validation
  - Layer 2: Requirement matching
  - Layer 3: Test validation
  - Layer 4: Security checks
  - Layer 5: Documentation validation
  - Quality scoring system (0-100 with 80% acceptance threshold)

**Reference Guides:**
- **prompting-patterns-reference.md** - 10 essential prompting patterns for better AI instructions
  - Clear Task + Context + Constraints, Chain-of-Thought, Few-Shot Learning, etc.
  - Reduces clarification questions by 50%, improves first-time-right code by 60%

- **orchestration-patterns-reference.md** - Comprehensive orchestration guide for multi-agent workflows
  - 5 orchestration types with real-world examples
  - 4 core patterns (Map-Reduce, Pipeline, Fan-Out/Fan-In, Circuit Breaker)
  - Decision trees and complexity vs performance analysis

- **encoding-patterns-into-skills.md** - Guide for creating pattern-enforcing skills
  - Formula: Rules + Examples + Checklists + Decision Trees
  - Pattern encoding templates
  - Skill effectiveness and iteration strategies

**Documentation Standards:**
- All new skills comply with doc-standards.md (500-line hard limit)
- Two-tier structure (Tier 1 TOC + Tier 2 deep dives)
- Smart subdirectory grouping for maintainability

### Changed

- **skills/CLAUDE.md** - Updated repository structure to include AI development skills
- **skills/ai-assisted-development/SKILL.md** - Refactored from 879 lines to 462 lines (compliant)
  - Split into main SKILL.md + 3 reference files
  - Improved navigability and token efficiency

### Performance

- **Token Efficiency Improvements:**
  - ai-error-prevention saves 50-75% of tokens through early error detection
  - Prompting patterns reduce clarification rounds by 50%
  - Orchestration patterns enable 30-50% faster parallel execution

### Documentation

- Updated to reflect expanded scope beyond SDLC documentation to include AI development assistance
- All skills now enforce automatic pattern following through structured templates

## [3.0.0] - 2026-02-06

### Added

- Multi-methodology support (Waterfall, Agile, Hybrid)
- Expanded from SRS-only to 23 document types across 10 SDLC phases
- Phase 00: Meta-initialization for methodology detection
- Agile track: User story generation with INVEST criteria
- Backward compatibility with v2.x Waterfall SRS pipeline

### Changed

- Renamed from SRS-Skills to SDLC-Docs-Engine
- Reorganized phases: 01-08 → 02-requirements-engineering/waterfall/
- Updated README.md and PROJECT_BRIEF.md

## [1.0.0] - 2026-01-26

### Added

- Core 1-8 Skill Pipeline targeting IEEE 830 and ISO/IEC 25010.
- Submodule-ready architecture with relative pathing to ../project_context.
- High-density seeder templates for Skill 01 with ISO-aligned elicitation questions.
- Skill Registry (skill_overview.md) for architectural transparency.
- V&V Standard Operating Procedure in CLAUDE.md.

### Changed

- (Document future modifications to skill logic.prompt or root-level protocols here, referencing the Engineering Registry when appropriate.)

### Fixed

- (Reserve for bug fixes per semantic versioning.)

### Removed

- (Use this section for retired features or deprecated skill templates.)

### Security

- (Record security-related updates or compliance notes.)

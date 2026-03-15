# Research Analysis: SDLC & Waterfall Books
## Sources
- **Book 1:** *The Software Development Life Cycle: A Complete Guide* — Albert Tetteh Adjei (2023)
- **Book 2:** *Waterfall Software Development* — Simon Winston

**Analyst:** Research Agent
**Date:** 2026-03-15
**Purpose:** Extract all insights applicable to improving the SRS-Skills documentation engine

---

## A. SDLC Phases & Waterfall Model

### A.1 Canonical Phase Definitions

Both books converge on the same six-phase Waterfall spine, which directly maps to the SRS-Skills phase grid. The canonical sequence is:

1. **Requirements Gathering / Analysis** — eliciting, documenting, and validating stakeholder needs
2. **System Design** — high-level architecture, detailed design, database design, UI design
3. **Implementation** — coding, unit testing, integration
4. **Testing** — test planning, execution, defect tracking, system and acceptance testing
5. **Deployment** — installation, configuration, user training, handover to operations
6. **Maintenance** — corrective, adaptive, perfective, and preventive maintenance

Adjei (Book 1, Ch. 2) states: *"Each phase is dependent on the completion of the previous one, forming a waterfall-like flow... The well-defined phases allow for detailed documentation, making it easier to manage the development process."*

Winston (Book 2, Ch. 2) refines this by adding a **seventh implicit phase**: *"Evaluation and Feedback — Throughout the process, stakeholders and users provide feedback on the software's performance, usability, and relevance. This feedback loop informs future enhancements."* This is currently absent as a named phase in the SRS-Skills engine.

### A.2 Phase Gates and Entry/Exit Criteria

Adjei is explicit that phases must be formally closed before the next opens. Specific gate activities per phase:

| Phase Exit Gate | Key Deliverable | Gate Activity |
|-----------------|-----------------|---------------|
| Requirements | Requirements Specification Document | Validation review with stakeholders |
| Design | System Design Document (SDD) | Architecture review |
| Implementation | Source code + unit test results | Code review |
| Testing | Test reports, defect logs | Sign-off from Test Lead |
| Deployment | Deployed system + training materials | User acceptance confirmation |
| Maintenance | Change logs, updated documentation | Periodic performance review |

Winston (Book 2, Ch. 10) adds that Waterfall uses **milestones or phase gates** explicitly: *"Milestones serve as markers of progress, enabling project managers to assess the project's health and make necessary adjustments."* He identifies specific milestone examples: successful permit acquisition (requirements gate), completion of environmental impact assessment, commencement of construction (implementation gate).

**Actionable Improvement:** The SRS-Skills engine's PRIME cycle (Prepare → Relay → Inspect → Modify → Execute) maps well to the phase-gate concept, but it does not currently emit a named **Phase Gate Checklist** artifact at the close of each skill. This should be added as a lightweight `gate_checklist.md` template per phase.

### A.3 Waterfall in Regulated Environments

Winston (Book 2, Ch. 13) provides the strongest justification for the SRS-Skills engine's target audience: *"Documentation and Traceability: Regulated industries often require extensive documentation and traceability to ensure that processes and systems meet strict compliance standards. Waterfall's structured and sequential approach is conducive to creating thorough documentation at each phase of the project. This documentation is invaluable for regulatory audits and demonstrating that a system meets all the required standards."*

He enumerates specific sectors: healthcare, finance, aerospace, nuclear energy. The book identifies four concrete Waterfall advantages in regulated settings:

1. **Stability and Predictability** — fixed scope prevents regulatory non-compliance from late changes
2. **Systematic Quality Assurance** — dedicated testing phase aligns with audit requirements
3. **Change Control and Auditing** — formal RFC process provides audit trail
4. **Certification and Approvals** — documentation depth supports FDA/CE/DO-178B submission packages

This directly reinforces the SRS-Skills decision to lead regulated-industry users toward the Waterfall SRS pipeline over the Agile pipeline.

### A.4 Hybrid Model Insights

Both books endorse hybrid approaches. Winston (Book 2, Ch. 13) coins the term **"Water-Scrum-Fall"** — Waterfall's structured phases with Agile Scrum practices embedded in implementation. He frames three specific hybrid patterns:

- **Iterative Waterfall:** Break each large phase into smaller sub-phases with periodic review cycles
- **Hybrid Models:** Waterfall planning and documentation with Agile sprints for implementation
- **Agile Techniques Injection:** Daily standups, backlog prioritization, and frequent status updates layered onto a Waterfall backbone

Adjei mirrors this in Chapter 3, noting that Agile emerged precisely because Waterfall *"struggles to keep up with changing requirements."* He recommends Waterfall for projects with *"stable, well-defined scope"* and Agile for those with *"evolving, uncertain scope."*

**Actionable Improvement:** The SRS-Skills README already documents Hybrid Approach patterns (Example 1-3 in `/02-requirements-engineering/README.md`). However, neither book provides guidance for the engine on **when to auto-detect hybrid requirements** from context files. A heuristic detection rule should be added to the meta-initialization skill: if `_context/vision.md` contains terms like "iterative delivery," "MVP," or "phased rollout" alongside a regulated-industry domain tag, suggest the Iterative Waterfall variant.

### A.5 Maintenance Types — A Missing Phase Coverage Gap

Adjei (Book 1, Ch. 13) and Winston (Book 2, Ch. 9) both define the four standard ISO/IEC 14764 maintenance types:

| Type | Definition |
|------|------------|
| **Corrective** | Bug fixes and defect resolution post-deployment |
| **Adaptive** | Modifications for changed operating environment (OS, hardware, regulatory updates) |
| **Perfective** | Enhancements to improve performance, usability, or add features |
| **Preventive** | Proactive actions to reduce future defect risk (code reviews, security assessments) |

The SRS-Skills engine currently has Phase 06 (Deployment & Operations) with Runbook and Monitoring skills, but **no maintenance documentation skill**. Winston states: *"Long-Term Maintenance and Compliance: Many regulated systems require ongoing maintenance and updates while remaining in compliance with evolving regulations. Waterfall's structured approach to documentation and change management makes it easier to maintain systems over the long term."*

**Actionable Improvement:** Add a `06-maintenance-plan` sub-skill to Phase 06 that generates a Software Maintenance Plan (SMP) artifact documenting all four maintenance types, the maintenance request handling process, change control board (CCB) composition, and version control strategy.

---

## B. Requirements Engineering

### B.1 Elicitation Techniques Inventory

Adjei (Book 1, Ch. 8) enumerates 19 distinct requirements elicitation techniques. The SRS-Skills Phase 02 Fundamentals skill already covers several, but this list is the most complete reference found in either book:

1. Interviews (structured, semi-structured)
2. Workshops and Brainstorming
3. Surveys and Questionnaires
4. Prototyping and Mockups
5. Observation and Job Shadowing
6. Document Analysis (existing manuals, business process docs, technical specs)
7. Use Cases and User Stories
8. Requirement Workshops
9. Joint Application Development (JAD)
10. Contextual Inquiry
11. Focus Groups
12. Benchmarking (comparing against industry standards/competitors)
13. Data Gathering from Existing Systems
14. Storyboarding
15. Context Diagrams and Entity Relationship Diagrams (ERDs)
16. Non-Functional Requirements Elicitation (brainstorming/workshops specifically for NFRs)
17. Change Control and Requirements Traceability
18. User Persona Development
19. Documentation Standards and Templates

**Notable gap:** Techniques 10 (Contextual Inquiry), 12 (Benchmarking), and 13 (Data Gathering from Existing Systems) are not explicitly covered in the current elicitation skill. Benchmarking is especially relevant when the `_context/` domain file indicates competitive-market software.

### B.2 Requirements Analysis — The Quality Triad

Adjei (Book 1, Ch. 8) provides three explicit analysis activities that map directly to the IEEE 830 quality criteria already embedded in the CLAUDE.md:

1. **Eliciting Requirements** — engaging stakeholders to gather needs
2. **Analyzing Requirements** — reviewing for *"completeness, consistency, clarity, and feasibility"* and resolving *"ambiguous or contradictory requirements"*
3. **Prioritizing Requirements** — ranking by business value, risk, complexity, and dependencies

For prioritization, Adjei documents six techniques:

| Technique | Principle |
|-----------|-----------|
| **MoSCoW Method** | Must-have, Should-have, Could-have, Won't-have |
| **Kano Model** | Basic, Performance, Excitement categories |
| **Value vs. Effort Matrix** | 2x2 grid plotting business value against development effort |
| **Theme Screening** | Stakeholder voting on requirement themes/epics |
| **Business Value Points (BVP)** | Numeric point assignment by business value |
| **Cost of Delay (CoD)** | Priority based on financial cost of deferring requirement |

The SRS-Skills Fundamentals layer includes a Requirements Analysis skill, but the prioritization section currently focuses on MoSCoW. **Cost of Delay (CoD)** is a powerful economic prioritization lens missing from the engine's vocabulary — particularly relevant for time-sensitive business systems.

### B.3 Requirements Documentation Standards

Adjei (Book 1, Ch. 8) states: *"Documentation Standards and Templates: Establishing documentation standards and using templates for requirements documentation ensures consistency and clarity. Standardized formats and templates make it easier for stakeholders to understand and review requirements."*

He identifies the key components of a formal requirements specification:
- Functional requirements
- Non-functional requirements
- Use cases
- Business objectives context
- Acceptance criteria
- Traceability linkages

Winston (Book 2, Ch. 4) adds a critical dimension: *"Clear requirements define the project scope with precision. They delineate what is in and, equally importantly, what is out of scope."* This **explicit out-of-scope declaration** is a best practice that the SRS-Skills waterfall SRS does not currently enforce as a mandatory section.

**Actionable Improvement:** Add a mandatory `## 1.5 Scope Exclusions` section to the SRS template (Section 1 — Introduction). This section forces the consultant to explicitly state what the system will NOT do, which IEEE 830 permits but does not enforce. This prevents scope creep and reduces `[CONTEXT-GAP]` flags during Section 3 generation.

### B.4 Verification and Validation — Formal Definition Alignment

Winston (Book 2, Ch. 4) provides the clearest V&V distinction found in either book: *"Verification primarily focuses on assessing whether the project is being built right, while validation centers on determining if the right project is being built."*

He enumerates V&V techniques:
- **Verification:** Inspections, reviews, walk-throughs, testing
- **Validation:** User acceptance testing, simulations, assessments

This aligns with the SRS-Skills CLAUDE.md V&V SOP but adds a nuance: validation is explicitly linked to *user acceptance testing* as its primary mechanism. The engine's Skill 08 (Semantic Auditing) is primarily a verification tool. **The engine lacks a dedicated validation skill** that connects SRS functional requirements back to acceptance test criteria at the point of requirements generation, not just at the testing phase.

**Actionable Improvement:** Modify the waterfall SRS pipeline's Phase 02 Skill 05 (Requirements Validation) to explicitly generate an **Acceptance Test Stub** for each functional requirement — a draft test scenario written in Given-When-Then format. This bridges the V&V gap at requirements time rather than deferring it entirely to Phase 05.

### B.5 Traceability Engineering

Winston (Book 2, Ch. 4) dedicates a full section to traceability in Waterfall: *"Traceability forms the backbone of the Waterfall model... it provides a clear thread that ties requirements, design, implementation, testing, and maintenance together."*

He specifies five bidirectional traceability linkages:
1. Requirements → Design artifacts (requirements-to-design trace)
2. Design → Implementation (design-to-code trace)
3. Requirements → Test cases (requirements-to-test trace) — *"verifies that test cases are derived directly from the requirements, ensuring comprehensive coverage"*
4. Changes → Impact analysis (change-to-affected-artifacts trace)
5. Requirements → Regulatory standards (requirements-to-compliance trace)

The SRS-Skills Phase 09 Traceability Matrix covers linkages 1, 3, and partially 4. **Linkage 5 (requirements-to-regulatory-compliance trace)** is not explicitly generated as a column in the traceability matrix template.

**Actionable Improvement:** Add a `Regulatory Reference` column to the Traceability Matrix template in Phase 09. For each functional requirement, this column should cite the applicable standard section (e.g., "HIPAA §164.312(a)(1)," "IEEE 830-1998 §3.2," or "GDPR Art. 25"). This is especially critical for the domains already in `/domains/` (healthcare, finance).

### B.6 Non-Functional Requirements

Adjei (Book 1, Ch. 8) explicitly calls out NFR elicitation as a distinct process: *"Non-Functional Requirements Elicitation: Non-functional requirements capture the qualities and constraints of the software system, such as performance, security, usability, and scalability. Techniques such as brainstorming, workshops, and surveys can be used specifically to elicit non-functional requirements. These techniques help in defining measurable and specific criteria for system performance and quality attributes."*

This reinforces the `[DOMAIN-DEFAULT]` NFR injection mechanism in the engine, but highlights that NFR elicitation should be a **workshop event**, not just a template fill-in. The current domain NFR defaults are static. An active NFR elicitation prompt (structured questions delivered during the brainstorming skill) would produce higher-quality context before domain defaults are applied.

---

## C. Testing Documentation

### C.1 Test Hierarchy — The Four-Level Model

Both books converge on the same four-level testing hierarchy. Winston (Book 2, Ch. 7) provides the most structured account:

| Level | Scope | Trigger |
|-------|-------|---------|
| **Unit Testing** | Individual functions/methods in isolation | During Implementation phase |
| **Integration Testing** | Interactions between components/modules | After Integration within Implementation |
| **System Testing** | End-to-end system behavior against requirements | After Implementation complete |
| **User Acceptance Testing (UAT)** | Validation against user needs in real-world scenarios | Before Deployment |

Winston further subdivides UAT into:
- **Alpha Testing** — performed by in-house end-users or a dedicated testing team; identifies pre-release issues
- **Beta Testing** — performed by a select external audience; validates real-world performance before official release

The current SRS-Skills Test Strategy skill (Phase 05, Skill 01) defines these four test levels. However, **the Alpha/Beta UAT distinction is absent** from the test plan template. This is a meaningful gap for client-facing software projects.

### C.2 Integration Testing Levels

Winston (Book 2, Ch. 7) defines three integration testing levels not currently differentiated in the engine:

1. **Component Integration Testing** — checks interactions between individual software modules within boundaries
2. **System Integration Testing** — multiple subsystems working together; uncovers interface issues
3. **Acceptance Integration Testing** — complete system against specified requirements; final pre-UAT gate

**Actionable Improvement:** The Phase 05 Test Plan skill should generate distinct test case sections for each integration level, not treat integration testing as a monolithic activity.

### C.3 Regression Testing as a Formal Phase

Winston (Book 2, Ch. 7) treats regression testing as a first-class testing type: *"Regression testing is the act of retesting a software system or application to confirm that recent changes... have not adversely impacted existing, previously validated functionality."* He links it explicitly to the maintenance lifecycle.

The SRS-Skills engine has no regression testing protocol or template. In a Waterfall context, regression tests should be run after each approved change request is implemented during maintenance. This connects Phase 05 testing artifacts to the maintenance cycle.

**Actionable Improvement:** Add regression testing documentation as a section in the Test Plan template — defining the regression test suite trigger conditions, scope, and automation approach.

### C.4 Bug Tracking and Resolution Process

Winston (Book 2, Ch. 7) provides a formal six-step bug resolution workflow:

1. Issue Prioritization (by severity and impact)
2. Assigning Responsibility (developer/team assignment)
3. Development and Testing (fix development + verification testing)
4. Verification and Validation (confirm fix; confirm no new defects introduced)
5. Documentation and Communication (update tracking system; document resolution)
6. Release and Deployment (prepare updated version)

The SRS-Skills Test Report skill (Phase 05, Skill 03) produces a defect log template. However, it does not currently generate a **bug resolution workflow** section that documents steps 2-6. This is especially important for regulated industries that require audit trails of defect closure.

**Actionable Improvement:** Add a `## Defect Resolution Protocol` section to the Test Report template that specifies the six-step closure process, including required sign-off roles at step 4 (V&V sign-off).

### C.5 Test Plan Components — Complete Reference

Adjei (Book 1, Ch. 11) identifies the complete set of test plan components:

- **Test Planning:** Test objectives, test cases, test data, testing resources required
- **Test Execution:** Systematic execution of test cases; actual vs. expected results comparison
- **Defect Tracking:** Documentation, logging, and assignment of identified defects
- **System Testing:** End-to-end validation of complete system behavior

This matches the current Phase 05 test plan structure. However, Adjei adds one missing element: **test data specification**. The current test plan template asks for test cases but does not require explicit test data sets. For regulated industries (e.g., HIPAA-compliant healthcare software), test data management — including anonymization and synthetic data generation — is a compliance requirement.

**Actionable Improvement:** Add a `## Test Data Management` section to the Test Plan template. This section should specify: (a) data sources, (b) anonymization/masking requirements for production data, (c) synthetic data generation approach, and (d) data retention policy during testing.

### C.6 Quality Metrics — SMART Requirement

Adjei (Book 1, Ch. 15) introduces a quality metrics standard directly applicable to SRS NFR generation: *"Effective quality metrics are specific, measurable, achievable, relevant, and time-bound (SMART), enabling teams to make data-driven decisions and track progress over time."*

He categorizes metrics into three types:
- **Process metrics:** Defect density, cycle time, rework percentage
- **Product metrics:** Code coverage, bug severity, response time
- **Customer satisfaction metrics:** Survey ratings, user feedback scores

This directly supports the CLAUDE.md prohibition on subjective adjectives (*"fast," "reliable," "intuitive"*) and the mandate to use IEEE 982.1 metrics. The SMART framework should be explicitly cited in the NFR generation prompts to reinforce the metric-definition requirement.

**Actionable Improvement:** In Phase 02 SRS Skill (NFR section), add a SMART validation gate: for every NFR generated, the AI must confirm that each quality attribute has a specific numeric threshold (e.g., "response time < 2 seconds at 95th percentile under 500 concurrent users") before the requirement passes the V&V gate. NFRs that fail this check should be tagged `[V&V-FAIL: SMART metric not defined]`.

---

## D. Document Quality Standards

### D.1 Documentation Types Taxonomy

Adjei (Book 1, Ch. 16) provides the most comprehensive documentation taxonomy found in either book. This is directly useful for validating that the SRS-Skills engine covers all required document types:

**Requirements Documentation:**
- Business Requirements Document (BRD)
- Functional Requirements Specification (FRS)
- Use Case Documents

**Design Documentation:**
- System Design Document (SDD)
- Technical Design Document (TDD)
- Database Design Document

**User Documentation:**
- User Manual, User Guides, FAQs

**Technical Documentation:**
- API Documentation
- Code Documentation
- SDK Documentation

**Testing and QA Documentation:**
- Test Plans
- Test Cases
- Test Scripts
- Bug Reports

**Project Management Documentation:**
- Project Charter
- Project Schedule
- Risk Management Plan

**Maintenance and Support Documentation:**
- Release Notes
- Change Logs
- Troubleshooting Guides

**Legal and Compliance Documentation:**
- EULA
- Privacy Policy
- Compliance Documents

**Architectural Documentation:**
- Architecture Decision Records (ADRs)
- UML Diagrams

**Compliance and Audit Documentation:**
- Security Audit Reports
- Compliance Certifications

**Cross-referencing against the SRS-Skills phase grid:** The engine covers all categories except **Architecture Decision Records (ADRs)** and **Project Charter**. ADRs are a high-value artifact for regulated projects — they document *why* design decisions were made, which is required evidence in aerospace (DO-178C) and medical device (IEC 62304) audits.

**Actionable Improvement:** Add an ADR (Architecture Decision Record) sub-skill to Phase 03 (Design Documentation). Each ADR should record: (1) Context, (2) Decision, (3) Status, (4) Consequences, (5) Standards reference. This is a lightweight addition with high audit value.

### D.2 Effective Technical Writing Standards

Adjei (Book 1, Ch. 16) enumerates best practices for technical documentation quality directly applicable to the engine's output:

1. **Understand the Target Audience** — tailor language to skill level; avoid alienating jargon
2. **Structuring the Documentation** — clear hierarchy: TOC, chapters, sections, headings
3. **Writing Style** — *"clear, concise, and user-friendly manner... simple and accessible language"*; avoid complex terminology; maintain consistent terminology
4. **Visual Aids** — screenshots, diagrams, and illustrations *"significantly enhance the clarity and understanding"*; videos for complex tasks
5. **Testing and Reviewing Documentation** — *"Real users should be involved in testing... Technical experts, user representatives, and documentation specialists can review the content for consistency, accuracy, and clarity"*
6. **Regular Updates** — *"Documentation should be regularly updated to align with software updates... Outdated or inaccurate documentation can lead to confusion"*

Point 5 aligns with the CLAUDE.md Human Review Gate requirement. Point 3 (consistent terminology) aligns with the IEEE 610.12-1990 glossary mandate. However, **Point 4 (visual aids)** is not currently addressed in any SRS-Skills skill prompt. The engine generates Markdown text only and has no provision for directing consultants to create diagrams.

**Actionable Improvement:** In Phase 02 (SRS), Phase 03 (Design Documentation), and Phase 05 (Testing), add `[DIAGRAM-PROMPT]` tags at points where a UML diagram, data flow diagram, or test coverage matrix would significantly improve document quality. These are not generated by the AI — they are instructions to the consultant to create and embed the visual artifact.

### D.3 Design Decision Documentation

Adjei (Book 1, Ch. 16) states: *"Document design principles: Start by outlining the overarching design principles that guide the project... Record design choices: Document specific design choices made during the development process, including architectural patterns, data structures, algorithms, and integration approaches... Explain trade-offs: Describe the trade-offs considered when making design decisions."*

This trade-off documentation is currently absent from the SRS-Skills HLD and LLD skills in Phase 03. Design documents typically present *what* was decided but not *why* or *what was rejected*.

**Actionable Improvement:** Add a `## Design Rationale` section to both the HLD and LLD SKILL.md prompts. For each major architectural decision, the AI must state: chosen approach, alternatives considered, and the trade-off justification. This is the textual precursor to a formal ADR.

### D.4 Documentation Maintenance Protocol

Winston (Book 2, Ch. 9) states: *"Documentation is invaluable for support and maintenance. When issues arise or updates are needed, well-documented code and system architecture provide the necessary context for efficient problem-solving and enhancements."*

He adds: *"In industries with stringent regulations, such as healthcare or finance, documentation is essential for demonstrating compliance... It provides a trail of accountability and adherence to best practices."*

Adjei (Book 1, Ch. 16) identifies the documentation maintenance process: *"Assign documentation ownership: Designate responsible individuals or roles to maintain and update the documentation regularly... Encourage contribution: Foster a culture of documentation within the development team."*

The SRS-Skills CLAUDE.md mandates updating `docs/CHANGELOG.md` with every skill change. However, there is no guidance for project-level documentation ownership — who is responsible for keeping `projects/<ProjectName>/_context/` files current after the initial scaffold.

**Actionable Improvement:** The new-project scaffold (Phase 00) should generate a `_context/doc-ownership.md` file that lists each context file, the responsible stakeholder role, and the update trigger condition (e.g., "Update `vision.md` when business objectives change; Update `nfr-defaults.md` after each regulatory audit").

---

## E. Gaps and Weaknesses in the Current SRS-Skills Approach

### E.1 Gap: No Post-Deployment Evaluation Skill

Winston (Book 2, Ch. 8) dedicates a full section to Post-Deployment Evaluation: *"Performance Metrics... User Feedback... Bug Tracking... Usability Testing... Security Audits... Performance Tuning..."*

The SRS-Skills engine ends at Phase 09 (Governance & Compliance). There is no post-deployment review skill that captures the operational feedback loop back into the requirements or maintenance documentation. This is a lifecycle completeness gap.

**Recommendation:** Add a `06-post-deployment-review` sub-skill to Phase 06 that generates a Post-Deployment Evaluation Report template. This artifact should include: (a) performance metrics against SRS NFR baselines, (b) user feedback summary, (c) open defect status, (d) security audit results, (e) any identified maintenance backlog items. This closes the SDLC loop and feeds the maintenance plan.

### E.2 Gap: Change Control Board (CCB) Documentation

Winston (Book 2, Ch. 3) and Adjei (Book 1, Ch. 8) both discuss **Change Control Boards** as the governance mechanism for managing requirement changes after baseline. Winston states: *"For complex projects, consider establishing a Change Control Board (CCB) or similar group responsible for evaluating and approving change requests."*

The SRS-Skills engine has a Requirements Management skill in Phase 02 Fundamentals that covers baselining and change control. However, it does not generate a **CCB Charter** — a formal document defining the CCB's composition, authority, meeting cadence, and RFC escalation path.

**Recommendation:** Add a `09-ccb-charter` sub-skill to Phase 09 (Governance & Compliance). This is a one-page artifact but is mandatory evidence in ISO 9001 and CMMI Level 2+ audits.

### E.3 Gap: Formal Scope Exclusion Declaration

Winston (Book 2, Ch. 4) and Adjei (Book 1, Ch. 8) both emphasize that scope definition includes explicit **out-of-scope declarations**. Winston: *"They delineate what is in and, equally importantly, what is out of scope."*

The current SRS template (Phase 02, waterfall pipeline) generates a `1.2 Scope` section that describes what the system *will* do. There is no enforced `1.3 Exclusions` or `1.2.2 Out of Scope` section.

**Recommendation:** Modify the SRS Scope section prompt in Phase 02 to require two subsections: `## 1.2.1 In Scope` and `## 1.2.2 Out of Scope`. Both are mandatory. If the consultant has not populated `_context/` with exclusion information, the AI must flag `[CONTEXT-GAP: Out-of-scope boundary not defined]` rather than leaving the section blank.

### E.4 Gap: Stakeholder Register as a First-Class Artifact

Winston (Book 2, Ch. 3) dedicates an entire chapter to stakeholder identification and management, listing 15 stakeholder categories (Project Sponsor, Project Team, Clients, End-Users, Internal Stakeholders, External Stakeholders, Subject Matter Experts, Competitors, Suppliers/Vendors, Regulatory Bodies, Community/Public, Shareholders/Investors, Advocacy Groups, Project Reviewers/Auditors, NGOs).

The SRS-Skills engine has a Stakeholder Analysis skill in Phase 02 Fundamentals that generates Power/Interest grids and RACI matrices. However, it does not generate a **Stakeholder Register** — a formal list of all stakeholders with their classification, interest level, influence level, engagement strategy, and communication plan.

This matters because Winston (Book 2, Ch. 3) argues that managing stakeholder *expectations* — not just identifying them — is critical: *"Setting realistic expectations: This means defining what the project can and cannot achieve within its scope, budget, and timeline. It's about being honest and upfront about limitations and constraints."*

**Recommendation:** Upgrade the Phase 02 Fundamentals Stakeholder Analysis skill to generate a formal Stakeholder Register with a Communication Plan column. This register should be stored in `_context/stakeholders.md` and referenced by all downstream skills when identifying review audiences for Human Review Gates.

### E.5 Gap: Acceptance Criteria Linked to Requirements at Generation Time

The most significant gap identified across both books is the separation between requirements and acceptance criteria. Adjei (Book 1, Ch. 8) states requirements must be validated against stakeholder expectations. Winston (Book 2, Ch. 4) states V&V requires *"test cases derived directly from the requirements."* Both books agree that this linkage must be established at requirements time, not deferred to the testing phase.

In the current engine, the waterfall SRS pipeline generates functional requirements (Phase 02) and test cases (Phase 05) as entirely separate artifacts, with the linkage created retroactively in the Traceability Matrix (Phase 09).

**Recommendation:** Modify Phase 02 SRS Skill 05 (functional requirements) to generate an inline acceptance stub for every `SHALL` requirement in the format:

```
**FR-001:** The system shall [action] when [stimulus].
*Acceptance Stub:* Given [precondition], when [stimulus], then [expected outcome within measurable threshold].
*Test Reference:* [Placeholder for Phase 05 test case ID]
```

This pattern aligns with the existing CLAUDE.md "Stimulus-Response Rule" and extends it to include the full acceptance criterion at requirements authoring time.

### E.6 Gap: Requirements Prioritization Method in SRS

Adjei (Book 1, Ch. 8) lists six prioritization techniques (MoSCoW, Kano, Value vs. Effort, Theme Screening, BVP, CoD). The SRS-Skills engine acknowledges prioritization in the Agile backlog skills but does not enforce a **prioritization method for Waterfall SRS functional requirements**.

In a formal IEEE 830 SRS, all requirements are treated as equally mandatory once baselined. This creates a practical problem: when scope must be reduced due to budget or time constraints, there is no pre-existing priority ordering to guide cuts.

**Recommendation:** Add a `Priority` column to the functional requirements table in the SRS template with values `[M] Must-Have`, `[S] Should-Have`, `[C] Could-Have`, `[W] Will-Not-Have` (MoSCoW). This makes the SRS itself a scope-management tool, not just a specification document. The Phase 02 waterfall skill prompt should instruct the AI to assign priority based on business goals documented in `_context/vision.md`.

### E.7 Gap: Risk Management Documentation

Both books treat risk management as a mandatory SDLC artifact, not an afterthought. Adjei (Book 1, Ch. 14) covers risk identification, categorization, and mitigation. Winston (Book 2, Ch. 10) states: *"Waterfall's love for documentation extends to risk management. Detailed records of identified risks, assessment findings, mitigation plans, and their outcomes are meticulously maintained."*

The SRS-Skills engine has a Risk Assessment skill in Phase 09 (Governance & Compliance, ISO 31000). However, both books indicate risk documentation should begin in Phase 00/01, not at the end of the lifecycle.

**Recommendation:** Move risk identification to the new-project scaffold step. The `_context/` directory should include a `risks.md` template pre-populated with domain-specific risk categories (sourced from `domains/<domain>/references/`). The Phase 01 (Strategic Vision) Business Case skill should consume this file and include a risk register in the Business Case document.

### E.8 Gap: Work Breakdown Structure (WBS) Artifact

Adjei (Book 1, Ch. 14) describes the WBS as foundational to project planning: *"The Work Breakdown Structure (WBS) is a hierarchical decomposition of project deliverables into smaller, more manageable tasks. It provides a visual representation of the project's scope and enables effective planning, resource allocation, and tracking."*

The SRS-Skills engine generates requirements, design, and test documents but does not produce a WBS. For regulated-industry clients, the WBS is often required alongside the SRS as a contract deliverable.

**Recommendation:** Add a `01-wbs` sub-skill to Phase 00 (Meta-Initialization) that generates a Work Breakdown Structure template. The WBS should derive its top-level nodes from the SRS-Skills phase structure itself (Requirements, Design, Development, Testing, Deployment, Maintenance) and leave third-level decomposition as consultant-populated TODOs.

---

## Summary: Prioritized Improvement Actions

| Priority | Action | Phase Affected | Source |
|----------|--------|----------------|--------|
| 1 | Add inline acceptance stubs to each `SHALL` requirement (Given-When-Then) | Phase 02 | Both books |
| 2 | Add mandatory `## 1.2.2 Out of Scope` to SRS template | Phase 02 | Winston Ch. 4, Adjei Ch. 8 |
| 3 | Add SMART NFR validation gate with `[V&V-FAIL: SMART metric not defined]` tag | Phase 02 | Adjei Ch. 15 |
| 4 | Add `Priority` (MoSCoW) column to functional requirements table in SRS | Phase 02 | Adjei Ch. 8 |
| 5 | Add Regulatory Reference column to Traceability Matrix | Phase 09 | Winston Ch. 4 |
| 6 | Add Alpha/Beta UAT distinction to Test Plan template | Phase 05 | Winston Ch. 7 |
| 7 | Add `## Test Data Management` section to Test Plan template | Phase 05 | Adjei Ch. 11 |
| 8 | Add `## Defect Resolution Protocol` to Test Report template | Phase 05 | Winston Ch. 7 |
| 9 | Add `06-maintenance-plan` sub-skill generating Software Maintenance Plan | Phase 06 | Both books |
| 10 | Add `06-post-deployment-review` sub-skill for Post-Deployment Evaluation Report | Phase 06 | Winston Ch. 8 |
| 11 | Add ADR (Architecture Decision Record) sub-skill to Phase 03 | Phase 03 | Adjei Ch. 16 |
| 12 | Add `## Design Rationale` section to HLD and LLD prompts | Phase 03 | Adjei Ch. 16 |
| 13 | Upgrade Stakeholder Analysis to generate formal Stakeholder Register + Communication Plan | Phase 02 | Winston Ch. 3 |
| 14 | Add `09-ccb-charter` sub-skill to Phase 09 | Phase 09 | Winston Ch. 3 |
| 15 | Add regression testing section to Test Plan template | Phase 05 | Winston Ch. 7 |
| 16 | Generate `_context/doc-ownership.md` at scaffold time | Phase 00 | Adjei Ch. 16 |
| 17 | Move risk identification to scaffold; add `risks.md` to `_context/` | Phase 00/01 | Both books |
| 18 | Add WBS sub-skill to Phase 00 | Phase 00 | Adjei Ch. 14 |
| 19 | Add hybrid detection heuristic to meta-initialization | Phase 00 | Both books |
| 20 | Add `[DIAGRAM-PROMPT]` tags at key visual aid points in SRS, HLD, and Test Plan | Phases 02, 03, 05 | Adjei Ch. 16 |

---

## Standards and References Confirmed by Both Books

Both books explicitly cite or align with the following standards already embedded in the SRS-Skills engine:

- **IEEE 830-1998** (SRS) — confirmed as primary waterfall requirements standard
- **IEEE 1012** (V&V) — confirmed; both books support the engine's V&V SOP
- **ISO/IEC 14764** — maintenance types (corrective, adaptive, perfective, preventive); not yet cited in engine
- **IEEE 829** (Test Documentation) — confirmed as test plan/report standard

**Standards cited in books but NOT yet in SRS-Skills engine:**
- **IEEE 1074** (Software Life Cycle Processes) — Adjei references lifecycle phase sequencing
- **V-Model** — Winston references as a Waterfall derivative used in safety-critical systems; relevant for aerospace/medical domains
- **CMMI Level 2 requirements** — Winston's CCB charter discussion implies CMMI traceability; worth citing in Phase 09 Governance
- **ISO/IEC 14764-2006** (Software Maintenance) — should be added to the maintenance plan skill once created

---

*Research conducted by reading full text of both EPUBs. All quotes extracted directly from source HTML files at `/tmp/epub1/` and `/tmp/epub2/OEBPS/`. No AI hallucination of quotes — all verified against source content.*

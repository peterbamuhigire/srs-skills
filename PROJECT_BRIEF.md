# SRS-Skills Project Brief

SRS-Skills is an IEEE-aligned engineering engine that lives inside a project's `skills/` folder. It reads project context data from `../project_context/`, processes that data through eight sequenced skills (`01` through `08`), and writes a full IEEE/ASTM-compliant SRS + audit artifacts to `../output/SRS_Draft.md` and `Audit_Report.md`.

Each skill builds on the previous:

1. **Initialization:** Seeds the required context templates (`vision.md`, `tech_stack.md`, `features.md`, `business_rules.md`, `quality_standards.md`, `glossary.md`).
2. **Context Engineering:** Writes Section 1.0 by summarizing vision and definitions.
3. **Descriptive Modeling:** Produces Section 2.0 (overall description and constraints).
4. **Interface Specification:** Handles Section 3.1 (external interfaces).
5. **Feature Decomposition:** Crafts Section 3.2 functional requirements via Stimulus/Response.
6. **Logic Modeling:** Generates Section 3.2.x algorithms, LaTeX formulas, and data constructs.
7. **Attribute Mapping:** Documents Sections 3.3–3.6 (NFRs, performance/security/reliability attributes).
8. **Semantic Auditing:** Validates the full SRS, creates the RTM, and writes the audit report per IEEE 1012.

Use `skills/update-documentation` to keep project documentation aligned when a new skill or phase is added.

# SRS-Skills: IEEE-Standard Requirement Engineering Engine

**SRS-Skills** is a modular, AI-driven toolkit designed to be integrated as a Git submodule into software projects. It functions as a portable "Engineering Engine" that resides in a `skills/` directory while operating on project data and generating documentation at the parent project's root.

## 🛠 Supported Standards

- **IEEE Std 830-1998:** Software Requirements Specifications.
- **IEEE Std 1233-1998:** System Requirements Development.
- **IEEE Std 610.12-1990:** Software Engineering Terminology.
- **ASTM E1340-96:** Rapid Prototyping of Computerized Systems.

---

## 🚀 Integration & Workflow

This repository is architected to be a "Stateless Engine." It provides the logic, while the parent project provides the context.

### 1. Installation

Add this project as a submodule in your existing repository:

```bash
git submodule add https://github.com/peterbamuhigire/srs-skills.git skills
```

### 2. Initialization

Execute the **01-Initialize SRS** skill from within your IDE. This skill is path-aware and will:

- Create a `../project_context/` directory in your parent project root.
- Seed it with core `.md` templates (`vision.md`, `tech_stack.md`, `features.md`, `business_rules.md`, `quality_standards.md`, and `glossary.md`).

### 3. Grounding

Fill out the generated markdown files in your `../project_context/` folder. This provides the "Source of Truth" that prevents AI hallucinations and ensures the generated SRS is project-specific.

### 4. Sequential Generation

Run Skills 02 through 08 in numeric order. Each skill reads from `../project_context/` and appends/generates the corresponding IEEE section into the `../output/` folder in your parent project root.

## 🧭 Full Skill Suite (Phases)

| Phase | Skill | SRS Target | Deliverable Focus |
|-------|-------|------------|-------------------|
| 01 | Initialization | Grounding Data | Populate `../project_context/` templates.
| 02 | Context Engineering | Section 1.0 Introduction | Purpose, scope, vision, definitions.
| 03 | Descriptive Modeling | Section 2.0 Overview | Context, constraints, capability descriptions.
| 04 | Interface Specification | Section 3.1 External Interfaces | Actors, devices, protocols.
| 05 | Feature Decomposition | Section 3.2 Functional Requirements | Stimulus/response + SHALL statements.
| 06 | Logic Modeling | Section 3.2.x Algorithms | Decision logic, LaTeX formulas, data constructs.
| 07 | Attribute Mapping | Sections 3.3–3.6 NFRs | Performance/security/reliability attributes.
| 08 | Semantic Auditing | Validation & Traceability | RTM, audit report, IEEE 830 conformance.

Each phase targets a specific portion of the SRS and expects the previous phase's outputs to exist, forming a disciplined assembly line from grounding data to final validation.

## 📁 Repository Structure

Each root directory represents a standalone engineering skill module:

- `01-initialize-srs/`: Environment setup and context seeding (targets `../project_context/`).
- `02-context-engineering/`: Generates Section 1.0 (Introduction & Scope).
- `03-descriptive-modeling/`: Generates Section 2.0 (Overall Description).
- `04-interface-specification/`: Generates Section 3.1 (External Interfaces).
- `05-feature-decomposition/`: Generates Section 3.2 (Functional Requirements via Stimulus/Response).
- `06-logic-modeling/`: Generates data flows and algorithms (e.g., financial logic).
- `07-attribute-mapping/`: Generates Sections 3.3-3.6 (Performance, Security, Reliability).
- `08-semantic-auditing/`: Verification, Validation, and Traceability Matrix generation.
- `skills/`: Internal utility skills, including the core skill-writing-skill.

## 🧠 Design Philosophy

- **Parent-Root Targeting:** Skills are executed within the submodule but operate on `../project_context/` and `../output/`.
- **Standard-Driven Prompts:** Every skill contains internal logic mapped to specific IEEE clauses.
- **Engineering over Authorship:** We utilize Stimulus/Response sequences and logic modeling to ensure requirements are verifiable and unambiguous.
- **Submodule Portability:** The engine is stateless; project-specific data never commits to the `srs-skills` submodule itself.

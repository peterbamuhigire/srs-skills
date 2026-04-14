# Phase 2: Requirements Engineering & Documentation Engine

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Master the complete IEEE/ASTM-compliant SDLC documentation engine — from initial
requirements gathering through full SRS, PRD, design docs, test plans, and maintenance records.

**Architecture:** The `srs-skills` submodule at `C:\wamp64\www\srs-skills\` IS this phase.
It delivers an 8-skill SRS generation suite, professional Word output, Uganda DPPA compliance,
and a structured workspace per project. This phase is already world-class — the work is to
practise the full workflow on live projects.

**Skills library path:** `C:\Users\Peter\.claude\skills\` + `C:\wamp64\www\srs-skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Produce IEEE 830-compliant Software Requirements Specifications for any client project
- Generate professional Word (`.docx`) documents via Pandoc from structured Markdown
- Conduct Uganda DPPA 2019 compliance analysis on any personal data processing system
- Generate DPIA (Data Protection Impact Assessment) documents for high-risk processing
- Write and maintain PRDs, design documents, test plans, and user deployment guides
- Audit requirements for correctness, completeness, consistency, and verifiability
- Deliver ISO-compliant documentation that passes grant reviewer scrutiny
- Maintain living documentation through system lifecycle using the PRIME methodology

This is a **rare competitive differentiator.** Most ICT consultancies produce no formal
documentation. ISO-compliant SRS documents command client trust and justify premium rates.

---

## Current Strengths — Skills Already Built

### SRS Generation Suite (8-Phase Workflow in srs-skills)
- `sdlc-design` — Phase 1: Project initialisation, context seeding, directory scaffold
- `spec-architect` — Phase 2: System purpose, scope, product perspective, constraints
- `doc-architect` — Phase 3: System overview, product functions, user characteristics
- `system-architecture-design` — Phase 4: External interfaces (UI, hardware, software, communications)
- `ai-integration-section` — Phase 5 extension: AI module requirements specification
- `project-requirements` — Phase 5: Functional requirements (stimulus-response pattern)
- `database-design-engineering` — Phase 6: Logic modeling, data flow diagrams
- `sdlc-planning` — Phase 7: Attribute mapping (reliability, performance, security NFRs)
- `implementation-status-auditor` — Phase 8: Semantic audit, V&V, traceability matrix

### Compliance & Legal Skills
- `uganda-dppa-compliance` — DPPA 2019 PII inventory, consent FRs, data subject rights, breach SLA
- `dpia-generator` — Regulation 12-compliant DPIA for high-risk processing operations

### Document Production
- `professional-word-output` — Pandoc pipeline: Markdown → styled `.docx` with reference template
- `report-print-pdf` — PDF generation, print-ready formatting
- `markdown-lint-cleanup` — Markdown standards enforcement, linting

### SDLC Lifecycle Documentation
- `sdlc-planning` — Planning phase: project charter, WBS, risk register
- `sdlc-design` — Design phase: architecture documents, data models
- `sdlc-testing` — Testing phase: test plans, test cases, UAT sign-off
- `sdlc-user-deploy` — Deployment phase: deployment plan, user training materials
- `sdlc-maintenance` — Maintenance phase: change management, SLA documentation
- `sdlc-post-deployment` — Post-deployment: lessons learned, system handover

### Standards Compliance
- IEEE 830 — Software Requirements Specification
- IEEE 1233 — Guide for Developing System Requirements Specifications
- IEEE 610.12-1990 — Glossary of Software Engineering Terminology
- ASTM E1340 — Standard Guide for Rapid Prototyping
- Uganda DPPA 2019 — Data Protection and Privacy Act

---

## Build Tasks

**None required.** This phase is already world-class.

### Recommended Practice Workflow

Execute the full 8-phase SRS workflow on the next live engagement:

1. **Initialise** — run `sdlc-design` to scaffold `projects/<ClientName>/`
2. **Interview** — populate `_context/` files with client data
3. **Generate Section 1** — run `spec-architect` for System Purpose and Scope
4. **Generate Section 2** — run `doc-architect` for Overview and Functions
5. **Generate Section 3.1** — run `system-architecture-design` for Interfaces
6. **Generate Section 3.2** — run `project-requirements` for Functional Requirements
7. **Uganda check** — run `uganda-dppa-compliance` if any personal data is processed
8. **Logic model** — run `database-design-engineering` for data flow and ER diagrams
9. **NFR mapping** — run `sdlc-planning` for performance, reliability, security attributes
10. **Audit** — run `implementation-status-auditor` for V&V, traceability, glossary gaps
11. **Build** — run `bash scripts/build-doc.sh` to produce the final `.docx`

---

## Phase Completion Checklist

- [ ] Full 8-phase SRS has been generated for at least one live project
- [ ] Professional `.docx` output produced using `scripts/build-doc.sh`
- [ ] Uganda DPPA compliance annex generated for any personal data module
- [ ] All V&V fail tags and context gaps resolved before final delivery
- [ ] Client received the SRS and signed off — this is your quality benchmark
- [ ] Glossary in `_context/glossary.md` contains every domain-specific term used

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Software Requirements* (3rd ed.) | Karl Wiegers & Joy Beatty | Microsoft Press | ~$50 | The authoritative requirements engineering reference. Every elicitation technique, specification pattern, and validation method in one book. |
| 2 | *Writing Effective Use Cases* | Alistair Cockburn | Addison-Wesley | ~$40 | The definitive guide to use case writing — directly applicable to FR generation in Phase 5 of the SRS workflow. |
| 3 | *Documenting Software Architectures* (2nd ed.) | Clements, Bachmann, Bass et al. | Addison-Wesley | ~$60 | How to document architecture decisions in SRS Section 3.4 — views, styles, rationale. |
| 4 | *User Stories Applied* | Mike Cohn | Addison-Wesley | ~$40 | Agile requirements — bridges user stories to IEEE-formal requirements for hybrid methodology projects. |
| 5 | *Practical Model-Driven Enterprise Architecture* | Carsten Lemker | Springer | ~$60 | Data flow and logic modeling for Phase 6 of the SRS workflow. |

### Free Resources

- IEEE 830-1998 (Software Requirements Specification) — free via university library proxy
- IEEE 1233-1998 (System Requirements Specifications) — free via university library proxy
- Uganda DPPA 2019 full text — free at `ulii.org`
- Uganda NITA-U guidelines — free at `nita.go.ug`
- Pandoc documentation — `pandoc.org/MANUAL.html` — master the build pipeline
- RAGAS framework documentation — `docs.ragas.io` — AI output evaluation (relevant to Phase 8 of SRS)

---

*Next phase: [Phase 3 — Architecture, Design & Data Modeling](phase-03.md)*

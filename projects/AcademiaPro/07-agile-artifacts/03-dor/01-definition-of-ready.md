# Definition of Ready — Academia Pro

**Project:** Academia Pro
**Methodology:** Hybrid (Water-Scrum-Fall)
**Owner:** Chwezi Core Systems
**Effective Date:** 2026-04-03
**Standard:** Scrum Guide (2020) adapted for solo-developer context

This document defines the criteria that every Product Backlog Item (PBI) SHALL satisfy before it is selected into a Sprint. A PBI that fails any criterion below is not Ready and SHALL NOT enter Sprint Planning.

## 0 Baseline Traceability

A story is NOT Ready unless it references at least one baselined identifier from the v1.0 baseline (`_registry/baselines.yaml`):

- A functional requirement `FR-###` or module-prefixed form `FR-<MOD>-###` (`FR-ENR-001`, `FR-FEE-003`).
- A non-functional requirement `NFR-<CATEGORY>-###` (`NFR-PERF-001`, `NFR-SEC-002`).
- A business goal `BG-###` (`BG-001`).
- A control `CTRL-<FRAMEWORK>-###` (`CTRL-UG-001`, `CTRL-ISO-A9`).

Example story title: *"FR-ENR-003: validate NIN format on enrolment form"*. The reference must appear in the story description, the acceptance criteria, or the branch name (`feature/FR-<id>-short-name`). Hybrid-mode traces are recorded in `_registry/baseline-trace.yaml`.

## 1 Story Completeness Criteria

- SC-01: The PBI SHALL have a unique identifier (e.g., `PBI-0042`) assigned in the backlog tracker.
- SC-02: The PBI SHALL be expressed in user story format: "As a [role], I want [capability] so that [business value]."
- SC-03: The PBI SHALL state its business value in terms traceable to a project goal in `_context/vision.md`.
- SC-04: The PBI SHALL identify the primary user role from the stakeholder register in `_context/stakeholders.md`.
- SC-05: The PBI SHALL specify the module(s) it affects (e.g., Gradebook, Fees, Attendance).

## 2 Acceptance Criteria Requirements

- AC-01: The PBI SHALL have at least one acceptance criterion written in Given-When-Then format.
- AC-02: The acceptance criteria SHALL cover the success path (happy path) for the primary use case.
- AC-03: The acceptance criteria SHALL cover at least one error path (invalid input, unauthorised access, network failure) relevant to the story.
- AC-04: The acceptance criteria SHALL cover edge cases identified during refinement (e.g., boundary values, empty states, concurrent access).
- AC-05: Each acceptance criterion SHALL be independently verifiable with a deterministic pass/fail outcome.
- AC-06: The developer SHALL confirm agreement with the acceptance criteria during self-refinement (see Section 6) before the PBI enters Sprint Planning.

## 3 Sizing and Estimation Criteria

- SZ-01: The PBI SHALL have a story point estimate assigned during refinement.
- SZ-02: The PBI SHALL fit within a single Sprint. If the estimate exceeds 8 story points, the PBI SHALL be split into smaller items before it is considered Ready.
- SZ-03: Each split item SHALL be independently deliverable and testable.
- SZ-04: The estimation SHALL account for testing, documentation, and deployment effort — not just implementation.

## 4 Dependency Resolution Criteria

- DR-01: All external dependencies (third-party APIs, partner integrations, infrastructure provisioning) SHALL be identified and listed on the PBI.
- DR-02: Each external dependency SHALL have a confirmed resolution date that falls before or within the target Sprint.
- DR-03: API contracts for external integrations (e.g., SchoolPay, MTN MoMo, EMIS) SHALL be finalised and documented before the PBI enters Sprint Planning.
- DR-04: Internal dependencies on other PBIs SHALL be resolved or scheduled in a prior Sprint.
- DR-05: Required test data, sample files, or access credentials SHALL be available before Sprint start.

## 5 Design Clarity Criteria

- DS-01: User-facing PBIs SHALL have UI mockups or wireframes attached, specifying layout, field labels, and interaction states.
- DS-02: Data model changes (new tables, column additions, relationship changes) SHALL be identified and documented with a migration sketch.
- DS-03: The technical approach SHALL be agreed upon during refinement, including:
  - Framework components to use or extend
  - Affected API endpoints (new or modified)
  - Tenant isolation strategy for the feature
- DS-04: Non-functional requirements applicable to the PBI SHALL be specified with measurable thresholds drawn from `_context/quality_standards.md`. Examples:
  - API response time: P95 ≤500 ms
  - Accessibility: zero Axe violations
  - Security: zero OWASP Top 10 critical/high findings
- DS-05: If the PBI introduces a new algorithm or business rule (e.g., UNEB grading formula, fee penalty calculation), the rule SHALL be documented with input/output examples before Sprint entry.

## 6 Refinement Process

Context: Academia Pro is developed by a solo developer. Traditional team-based refinement ceremonies are replaced by a structured self-refinement discipline.

- RF-01: The developer SHALL conduct a weekly self-refinement session (minimum 30 minutes) to review and refine the top 10 backlog items by priority.
- RF-02: Each refinement session SHALL verify every candidate PBI against Sections 1 through 5 of this document.
- RF-03: PBIs that fail any criterion SHALL be tagged `[NOT-READY: <reason>]` and returned to the backlog with a note describing the missing element.
- RF-04: Blocked PBIs (awaiting external input, partner API access, or stakeholder decision) SHALL be escalated by:
  1. Logging the blocker in the backlog tracker with a due date.
  2. Sending a follow-up communication to the blocking party.
  3. Reviewing the blocker status at each subsequent refinement session.
- RF-05: The developer SHALL not select a PBI into Sprint Planning until all criteria in this document are satisfied and the `[NOT-READY]` tag is removed.
- RF-06: Refinement notes (decisions, assumptions, open questions resolved) SHALL be recorded on the PBI as comments for audit traceability.

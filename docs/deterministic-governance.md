# Deterministic Governance Checklist

To reach the repository's deterministic-governance target, every phase needs a clause-level gate document similar to the Phase 05 testing checklist. Start by applying the per-phase checks below before marking a phase complete.

## Phase 02 – Requirements Engineering

1. **Inputs Ready**
   - `projects/<ProjectName>/_context/vision.md`, `features.md`, `business_rules.md`, `glossary.md`, `quality_standards.md` exist with no `<!-- TODO -->`.
2. **Clause-Level Coverage**
   - Each SRS section (IEEE 29148 Clauses 5.1–5.6) lists the governing clause numbers.
   - All “shall” statements cite a standard or regulatory clause (IEEE 29148, ISO 25010, GDPR, etc.).
3. **Traceability Gate**
   - Traceability matrix links every requirement to a business goal and at least one test case.
4. **Enforcement Check**
   - Run `02-requirements-engineering/fundamentals/after/10-requirements-metrics` and confirm metric thresholds (completeness, ambiguity) meet the universal quality gate.

## Phase 03 – Design Documentation

1. **Architecture Statements**
   - HLD identifies each design viewpoint per IEEE 1016: Component, Data, Deployment, Behavior.
   - Every design decision cites a clause (IEEE 1016, ISO 42010, OWASP, etc.).
2. **Design Rationale Gate**
   - LLD documents rejected alternatives and ADR IDs referencing standards or regulatory constraints.
3. **Implementation Readiness**
   - API, Database, UX specs enumerate trace links to requirements and state technology choices/constraints per `tech_stack.md`.

## Phase 05 – Testing (done)

- Already enforced via the BS ISO/IEC/IEEE 29119-3 checklist, incident report, and test completion templates.

## Phase 06 – Deployment & Operations

1. **Operational Gate**
   - Deployment guide lists rollback steps, pre/post checks, and SLA-driven thresholds (per IEEE 1062 + ISO 27001 controls).
   - Runbook defines incident escalation, alert thresholds, and mitigation actions with trace links to monitoring alerts.
   - Infrastructure docs cite reliability/resilience clauses (IEEE 1016, ISO 27001) and include manifest of IaC artifacts.
2. **Go-Live Readiness**
   - Go-Live Readiness skill documents decision gates (product, technical, operational, compliance, organizational) referencing the checklist and capturing blockers with owners.

Use this checklist as the deterministic enforcement pattern for other phases until every phase has an analogous gate/tracing reference.

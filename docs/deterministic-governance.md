# Deterministic Governance Checklist

To reach the repository's deterministic-governance target, every phase needs a clause-level gate document similar to Phase 05's ISO/IEC/IEEE 29119-3 checklist. Apply the phase-specific references below before marking a phase complete.

## Phase 02 – Requirements Engineering

1. **Inputs Ready**
   - `projects/<ProjectName>/_context/vision.md`, `features.md`, `business_rules.md`, `glossary.md`, `quality_standards.md` exist with no `<!-- TODO -->`.
2. **Clause-Level Coverage**
   - Each SRS section (IEEE 29148 Clauses 5.1–5.6) lists the governing clauses.
   - Every “shall” statement cites a standard or regulatory clause (IEEE 29148, ISO 25010, GDPR, etc.).
3. **Traceability Gate**
   - Traceability matrix links every requirement to a business goal and at least one test case, annotating ISO/IEC/IEEE 29148 trace links.
4. **Enforcement Check**
   - Run `02-requirements-engineering/fundamentals/after/10-requirements-metrics` and confirm metric thresholds (completeness ≥95%, ambiguity ≤5, traceability ≥85%) pass; log failures with `[METRIC-GAP]`.

See `docs/deterministic-gate-phase02.md` for the runnable worksheet.

## Phase 03 – Design Documentation

1. **Architecture Statements**
   - HLD documents each IEEE 1016 viewpoint with clause citations (component, data, deployment, behavior).
   - Decisions reference IEEE 1016, ISO 42010, OWASP, or analogous standards.
2. **Design Rationale Gate**
   - LLD includes ADR references and rejected alternatives linked to clause numbers.
3. **Implementation Readiness**
   - API, database, and UX specs each include traceability appendices referencing SRS IDs and tech constraints from `tech_stack.md`.

Run `docs/deterministic-gate-phase03.md` for the phase-specific checklist before moving to testing.

## Phase 05 – Testing (done)

- Already covered by the BS ISO/IEC/IEEE 29119-3 checklist, incident report, and test completion templates plus the deterministic enforcement checklist in `05-testing-documentation/references/29119-deterministic-checks.md`.

## Phase 06 – Deployment & Operations

1. **Operational Gate**
   - Deployment guide lists rollback steps, pre/post checks, and SLA thresholds (IEEE 1062, ISO/IEC 27001).
   - Runbook defines escalation/alert thresholds with traceable metrics (ISO/IEC 27035/25010).
   - Infrastructure docs cite reliability/resilience clauses (IEEE 1016, ISO/IEC 27001) and manifest IaC artifacts.
2. **Go-Live Readiness**
   - Go-Live Readiness skill documents product, technical, operational, compliance, and organizational gates with owner-backed blockers.

Use `docs/deterministic-gate-phase06.md` for the deployment-specific gate and evidence log.

Use this checklist as the deterministic enforcement pattern until every phase has an analogous clause-level verification reference.

# Deterministic Governance Checklist

Use this document as the repo-level index for deterministic phase gates. The goal is to move the engine from narrative quality claims toward repeatable, reviewable closure checks across the full lifecycle.

## Phase 01 – Strategic Vision

1. **Input Integrity**
   - `projects/<ProjectName>/_context/vision.md`, `stakeholders.md`, `features.md`, and `glossary.md` exist with no unresolved `<!-- TODO -->`.
2. **Strategic Traceability**
   - Vision goals, PRD scope items, and business-case assertions are uniquely identifiable so they can be traced into Phase 02.
3. **Closure Discipline**
   - No unresolved `[CONTEXT-GAP]`, `[GLOSSARY-GAP]`, or `[V&V-FAIL]` markers remain without owner and action.

Use `docs/deterministic-gate-phase01.md` for the phase-specific worksheet.

## Phase 02 – Requirements Engineering

1. **Inputs Ready**
   - `projects/<ProjectName>/_context/vision.md`, `features.md`, `business_rules.md`, `glossary.md`, and `quality_standards.md` exist with no `<!-- TODO -->`.
2. **Clause-Level Coverage**
   - Each SRS section (IEEE 29148 Clauses 5.1-5.6) lists the governing clauses.
   - Every "shall" statement cites a standard or regulatory clause where the statement is normative.
3. **Traceability Gate**
   - Traceability matrix links every requirement to a business goal and at least one test case.
4. **Enforcement Check**
   - Run `02-requirements-engineering/fundamentals/after/10-requirements-metrics` and confirm thresholds pass; log failures with `[METRIC-GAP]`.

Use `docs/deterministic-gate-phase02.md` for the runnable worksheet.

## Phase 03 – Design Documentation

1. **Architecture Statements**
   - HLD documents each IEEE 1016 viewpoint with clause citations.
   - Decisions reference IEEE 1016, ISO 42010, OWASP, or analogous standards.
2. **Design Rationale Gate**
   - LLD includes ADR references and rejected alternatives linked to clause numbers.
3. **Implementation Readiness**
   - API, database, and UX specs each include traceability appendices referencing SRS IDs and tech constraints from `tech_stack.md`.

Use `docs/deterministic-gate-phase03.md` before moving to testing.

## Phase 04 – Development Artifacts

1. **Specification Readiness**
   - Technical specs, coding guidelines, environment setup, and contribution rules are traceable back to requirement and design IDs.
2. **Executable Rules**
   - Coding conventions, review gates, and environment setup are deterministic enough for implementation teams to follow consistently.

Use `docs/deterministic-gate-phase04.md` for the implementation-readiness gate.

## Phase 05 – Testing

1. **Normative Test Structure**
   - Test artifacts conform to BS ISO/IEC/IEEE 29119-3 field expectations.
2. **Required Evidence**
   - Apply `05-testing-documentation/references/29119-deterministic-checks.md` plus incident and completion reporting.

Use `docs/deterministic-gate-phase05.md` as the phase-level entry point.

## Phase 06 – Deployment & Operations

1. **Operational Gate**
   - Deployment guide lists rollback steps, pre/post checks, and SLA thresholds.
   - Runbook defines escalation and alert thresholds with traceable metrics.
   - Infrastructure docs cite reliability and resilience clauses and manifest IaC artifacts.
2. **Go-Live Readiness**
   - Go-Live Readiness documents product, technical, operational, compliance, and organizational gates with owner-backed blockers.

Use `docs/deterministic-gate-phase06.md` for the deployment-specific gate and evidence log.

## Phase 07 – Agile Artifacts

1. **Sprint Gate Integrity**
   - Ready and Done rules are explicit, reviewable, and connected to upstream requirements or stories.
2. **Hybrid Compatibility**
   - Hybrid projects carry compliance and architecture constraints from the baselined track into sprint execution.

Use `docs/deterministic-gate-phase07.md` before sprint commitment or sprint closure.

## Phase 08 – End-User Documentation

1. **Behavioral Accuracy**
   - User-facing guidance is checked against current design, testing, and deployment evidence.
2. **Operational Usability**
   - Installation, troubleshooting, and release notes are actionable without hidden tribal knowledge.

Use `docs/deterministic-gate-phase08.md` for the publication gate.

## Phase 09 – Governance & Compliance

1. **Audit-Ready Trace Chain**
   - Governance outputs prove business-goal-to-control traceability rather than documenting intention only.
2. **Regulated Evidence Depth**
   - Regulated projects must satisfy the evidence chain defined in `docs/regulated-evidence-model.md`.

Use `docs/deterministic-gate-phase09.md` as the audit-readiness gate.

## Hybrid Synchronization (cross-cutting)

1. **Baseline Trace Integrity**
   - `_registry/baseline-trace.yaml` exists, stories trace to baseline IDs, and every baseline ID is implemented by at least one story.
2. **DoR/DoD Bound to Baseline**
   - `dor-dod.md` references baseline FR/NFR/CTRL identifiers verbatim so Agile execution cannot silently diverge from the Waterfall baseline.

The gate is active only when `_context/methodology.md` declares `methodology: hybrid`. Use `docs/deterministic-gate-hybrid.md` as the cross-cutting worksheet.

Use this checklist as the deterministic enforcement pattern across the full engine, not just selected phases.

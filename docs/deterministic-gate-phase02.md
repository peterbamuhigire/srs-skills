# Phase 02 Deterministic Gate

Use this checklist before declaring requirements complete to ensure BS ISO/IEC/IEEE 29148, ISO/IEC 25010, and applicable regulatory clauses are enforced.

1. **Context Coverage**
   - `projects/<ProjectName>/_context/vision.md`, `features.md`, `business_rules.md`, `quality_standards.md`, and `glossary.md` exist with no `<!-- TODO -->` placeholders.
   - Each file references the governing standard (IEEE 29148 section or regulation) for its content (e.g., security rules cite ISO/IEC 27001 controls, privacy rules cite GDPR articles).

2. **Clause-Tagged Sections**
   - Section 1.0 intro references IEEE 29148 Sec. 5.1 clauses.
   - Section 2.0 overall description tags Clause 5.2 viewpoints.
   - Functional requirements (3.2) tag the applicable clause(s) (IEEE 29148 5.3.1 or IEEE 29148, ISO 29119 for testability).
   - Non-functional sections cite ISO/IEC 25010 characteristics and any domain-specific clauses (IEEE 1016, ISO 29119 for traceability/testability).

3. **Deterministic Metrics**
   - Run `02-requirements-engineering/fundamentals/after/10-requirements-metrics` and confirm thresholds (completeness ≥95%, ambiguity ≤5, traceability ≥85%) pass; log failures as `[METRIC-GAP]`.

4. **Traceability Gate**
   - Traceability matrix links every SRS requirement to a business goal, design artifact, and at least one test case (ISO 29148 traceability graph).
   - Flag any unmatched items with `[TRACE-GAP: <REQ-ID>]` before closure.

5. **Governance Evidence**
   - Business Analysis Plan (`before/04-business-analysis-planning`) documents stakeholder engagement, decision authority, and governance clauses (PMI BA Practice Guide sections). Capture unresolved governance gaps as `[GOV-GAP]`.

Record this checklist outcome in the deterministic governance manifest before moving to Phase 03.

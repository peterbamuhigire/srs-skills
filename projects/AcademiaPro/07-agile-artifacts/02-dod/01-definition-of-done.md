# Definition of Done — Academia Pro

**Project:** Academia Pro
**Methodology:** Hybrid (Water-Scrum-Fall)
**Owner:** Chwezi Core Systems
**Effective Date:** 2026-04-03
**Standard:** Scrum Guide (2020) adapted for solo-developer context

This document defines the quality criteria that every Product Backlog Item (PBI), Increment, and Release SHALL satisfy before it is considered Done. A PBI that fails any criterion below is not Done and SHALL NOT be included in the Increment.

## 1 Code Quality Criteria

- CQ-01: The CI build SHALL pass with zero errors on the `main` branch before merge.
- CQ-02: `PHPStan` level 8 analysis SHALL report zero errors.
- CQ-03: `PHP CS Fixer` (PSR-12 ruleset) SHALL report zero violations.
- CQ-04: `ESLint` and `Prettier` SHALL report zero violations on all TypeScript files.
- CQ-05: `composer audit` and `npm audit` SHALL report zero critical or high vulnerabilities in production dependencies.
- CQ-06: No `TODO`, `FIXME`, or `HACK` comments SHALL remain in committed code unless tracked by a backlog item with a unique identifier.
- CQ-07: All new PHP classes and methods SHALL declare strict types (`declare(strict_types=1)`).

## 2 Testing Criteria

- TS-01: All new and modified code SHALL have accompanying unit tests that pass.
- TS-02: Backend test coverage SHALL be ≥80% line coverage as measured by PHPUnit with Xdebug/PCOV.
- TS-03: UNEB grading engine and fee calculation logic SHALL maintain 100% line coverage.
- TS-04: Frontend component coverage SHALL be ≥70% as measured by Vitest.
- TS-05: All critical user flows (admission, fee payment, mark entry, report card generation) SHALL pass their Playwright end-to-end tests.
- TS-06: No existing test SHALL regress. A regression is defined as a previously passing test that now fails.
- TS-07: Edge cases identified in `_context/` files and acceptance criteria SHALL have corresponding test cases.
- TS-08: Fee payment idempotency tests SHALL confirm zero duplicate receipts per 10,000 simulated payment events.

## 3 Documentation Criteria

- DC-01: Non-obvious logic (algorithms, business rules, workarounds) SHALL have inline comments explaining the rationale.
- DC-02: New or modified API endpoints SHALL have updated OpenAPI documentation before merge.
- DC-03: A changelog entry SHALL be added to `CHANGELOG.md` describing the change, its category (added, changed, fixed, removed), and the related backlog item identifier.
- DC-04: Database migration files SHALL include a comment block describing the schema change and its rollback procedure.

## 4 Review Criteria

- RV-01: The developer SHALL complete the self-review checklist (Appendix A) before marking a PBI as Done.
- RV-02: For architectural changes (new module, schema redesign, new external integration), the developer SHALL document the decision in an Architecture Decision Record (ADR) and review it against the Design Covenant in `_context/vision.md` before merge.
- RV-03: The developer SHALL verify that all `[CONTEXT-GAP]`, `[GLOSSARY-GAP]`, and `[V&V-FAIL]` tags are resolved before marking as Done.

## 5 Deployment Criteria

- DP-01: The full CI/CD pipeline SHALL complete with a green status on the staging environment.
- DP-02: The PBI SHALL be verified on the staging environment against its acceptance criteria before promotion to production.
- DP-03: The rollback procedure for the deployment SHALL be documented and tested on staging.
- DP-04: Database migrations SHALL be verified as reversible on staging before production deployment.

## 6 Increment-Level Definition of Done

An Increment (the sum of all PBIs completed in a Sprint) SHALL satisfy:

- IN-01: Every PBI in the Increment SHALL meet all item-level criteria (Sections 1 through 5).
- IN-02: The Sprint Goal SHALL be validated by verifying that the Increment delivers the intended capability.
- IN-03: Zero critical or high-severity defects SHALL remain open against the Increment.
- IN-04: Cross-module integration tests SHALL pass when the Increment includes changes spanning multiple modules.
- IN-05: API response time (P95) SHALL remain ≤500 ms under 200 concurrent requests as measured by `k6` load test on staging.

## 7 Release-Level Definition of Done

A Release (promoted to production) SHALL satisfy:

- RL-01: All Increments included in the Release SHALL meet the Increment-level DoD (Section 6).
- RL-02: Release notes SHALL be complete, listing all changes by category with backlog item identifiers.
- RL-03: Performance benchmarks SHALL meet or exceed the targets in `_context/quality_standards.md`:
  - Page load (P95) ≤2,000 ms on 3G simulation
  - API response time (P95) ≤500 ms
  - UNEB grade computation (500 students) ≤5 seconds
  - Bulk report card generation (200 students) ≤120 seconds
- RL-04: Zero OWASP Top 10 critical or high findings SHALL be present as verified by the security scan.
- RL-05: WCAG 2.1 AA compliance SHALL show zero Axe violations on all web portal pages.
- RL-06: Phase gate sign-off SHALL be obtained before the Release enters production, per the Water-Scrum-Fall methodology.
- RL-07: Backup and recovery procedures SHALL be verified (RTO ≤4 hours, RPO ≤1 hour).

## Appendix A: Solo Developer Self-Review Checklist

Before marking any PBI as Done, verify each item:

- [ ] I have re-read the acceptance criteria and confirmed the implementation satisfies every condition.
- [ ] I have run `php artisan test` locally with zero failures.
- [ ] I have run `PHPStan` level 8 with zero errors.
- [ ] I have run `PHP CS Fixer` and `ESLint`/`Prettier` with zero violations.
- [ ] I have checked for hardcoded secrets, credentials, or tenant-specific data.
- [ ] I have verified tenant isolation — no query leaks data across tenants.
- [ ] I have tested the feature on a 360 x 800 px viewport (budget Android phone).
- [ ] I have reviewed the diff for unnecessary changes, debug statements, and commented-out code.
- [ ] I have updated the changelog and API documentation where applicable.

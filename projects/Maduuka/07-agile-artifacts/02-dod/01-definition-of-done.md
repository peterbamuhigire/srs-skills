---
title: "Definition of Done — Maduuka Phase 1"
version: "1.0"
date: "2026-04-05"
status: "Approved"
owner: "Peter Bamuhigire"
---

# Definition of Done — Maduuka Phase 1

A task or user story is *Done* only when ALL of the following criteria are true. A story that satisfies only a subset of these criteria is not Done and must not be closed or counted in the sprint velocity.

## Code Quality

- [ ] Code follows the Coding Guidelines documented in `CodingGuidelines_Maduuka.docx`.
- [ ] No hardcoded currency symbols, tenant IDs, or API keys appear in the committed code.
- [ ] PHPStan level 8 passes with no ignored errors (backend).
- [ ] SwiftLint passes with no warnings (iOS); ktlint passes with no warnings (Android).
- [ ] No `TODO` or `FIXME` comments are committed without an associated issue number.

## Security

- [ ] Every new API endpoint has RBAC middleware applied.
- [ ] Every new state-changing web form has CSRF protection.
- [ ] All user input is validated and sanitised before database writes.
- [ ] No new SQL injection vectors are introduced; parameterised queries are used exclusively.
- [ ] Sensitive data (PII, credentials, salary figures) is not written to application logs.

## Testing

- [ ] Unit tests are written and passing for all new service methods.
- [ ] Integration tests are written for all new API endpoints, covering: response code, response schema, and RBAC enforcement.
- [ ] The test case(s) from `TestPlan_Maduuka_Phase1.docx` corresponding to this story are passing.
- [ ] No regression: the full test suite passes, not only the new tests.

## Multi-tenancy

- [ ] Every new database query is scoped to `franchise_id`.
- [ ] Cross-tenant data leak test: a user authenticated as Tenant A cannot access Tenant B's data via this feature. Result documented in the PR.

## Documentation

- [ ] The API endpoint is documented in the API specification, or the existing API spec is updated if behaviour changed.
- [ ] The Traceability Matrix is updated if a new functional requirement has been implemented.

## Deployment

- [ ] The feature works identically on Web AND Android (DC-001 parity), confirmed by manual test on both platforms before the PR is raised.
- [ ] The feature functions in offline mode if it is a POS or inventory feature (DC-003).
- [ ] The feature is verified on a low-end test device (DC-004: UGX 250,000-class Android handset).
- [ ] The PR has been reviewed and approved by at least 1 other team member.
- [ ] The story is merged to the staging branch and smoke-tested on the staging environment.

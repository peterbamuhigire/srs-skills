# Contributing to Academia Pro

Thank you for contributing to Academia Pro. This project follows a hybrid Water-Scrum-Fall methodology (see `_context/methodology.md`). Every code change must trace to a baselined requirement.

## Branch Model

- `main` — production-ready; protected.
- `develop` — integration branch; protected.
- `feature/FR-<id>-short-name` — one feature branch per FR story.
- `bugfix/BUG-<id>-short-name` — one branch per production defect.

## Commit Messages

Conventional Commits. Every commit body references at least one baselined identifier.

```
feat(enrolment): add NIN validation on enrolment form

Implements FR-ENR-003. Unit tests in tests/Feature/EnrolmentTest.php.
Closes #142.
```

## Pull Requests

- Link the Jira/Linear story (auto-populated from branch name).
- Tick the DoD checklist in `07-agile-artifacts/02-dod/01-definition-of-done.md`.
- At least one reviewer from the code-owning team. Two reviewers if the PR touches tenant isolation (ADR-0003), global identity (ADR-0004), or the PII scrubber (ADR-0005).
- CI must pass: unit + feature tests, PHPStan level 7, ESLint, detekt, SwiftLint, axe-core (WCAG 2.1 AA), and the tenant-leakage integration test.

## Code of Conduct

See `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1). Violations reported to `peter.bamuhigire@gmail.com`.

## Security Issues

Do NOT open a public issue for security vulnerabilities. Email `peter.bamuhigire@gmail.com` with subject `SECURITY: <short summary>` and PGP-encrypted body if possible. Responsible-disclosure window: 90 days.

## Further Reading

- Coding standards: `projects/AcademiaPro/04-development/coding-standards.md`
- Developer setup: `projects/AcademiaPro/04-development/env-setup.md`
- Architecture decisions: `projects/AcademiaPro/09-governance-compliance/05-adr/`

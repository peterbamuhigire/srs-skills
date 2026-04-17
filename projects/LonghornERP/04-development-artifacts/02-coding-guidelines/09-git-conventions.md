# Git Workflow Conventions

## Commit Message Format

All commit messages shall follow the format:

```
type: short description
```

The short description shall not exceed 50 characters. The type prefix shall be lowercase. A blank line followed by a body paragraph is permitted for commits that require additional context, but the subject line must stand alone as a complete summary.

## Commit Types

| Type | Use When |
|---|---|
| `feat` | A new feature or user-visible behaviour is added |
| `fix` | A defect is corrected |
| `refactor` | Code is restructured without changing behaviour |
| `test` | Tests are added or corrected with no production code change |
| `docs` | Documentation files only are modified |
| `chore` | Build scripts, dependency updates, config changes |

## Requirement ID References

Where a commit directly implements or closes a functional requirement, developers shall append the requirement ID in parentheses at the end of the subject line.

```
feat: add invoice approval workflow (FR-SALES-015)
fix: correct VAT rounding on credit notes (FR-SALES-022)
test: add tenant isolation test for PayslipService (FR-PAY-008)
```

## Branch Naming

All work shall be performed on a named branch. The branch name shall identify the module and a brief description of the change.

- New features: `feature/[module]-[description]`
- Bug fixes: `fix/[module]-[description]`

Examples:
- `feature/sales-invoice-approval`
- `feature/payroll-payslip-pdf-export`
- `fix/inventory-negative-stock-guard`
- `fix/auth-session-timeout`

Spaces and uppercase letters are prohibited in branch names. Hyphens shall be used as word separators.

## Branch Protection

Direct commits to the `main` branch are prohibited. All changes shall be delivered via a pull request from a feature or fix branch. The `main` branch shall be protected with the following required status checks:

1. PHPStan analysis at level 8 — zero errors.
2. PHP CS Fixer check — no unformatted files.
3. PHPUnit test suite — no failures or errors.

A pull request that fails any of these checks shall not be merged.

## Pull Request Requirements

Every pull request shall satisfy all of the following before a reviewer approves it:

1. PHPStan reports zero errors at level 8.
2. PHP CS Fixer reports a clean codebase (no changes needed).
3. PHPUnit reports all tests passing with no failures, errors, or risky tests.
4. The PR description references the requirement IDs addressed (where applicable).
5. Any new service class has a corresponding test file with ≥ 80% line coverage.

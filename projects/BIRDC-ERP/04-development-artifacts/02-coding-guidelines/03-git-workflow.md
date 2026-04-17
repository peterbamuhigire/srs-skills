# 3. Git Workflow

## 3.1 Branch Strategy

| Branch | Purpose | Protection Rules |
|---|---|---|
| `main` | Production-ready code. Deployed to production after manual approval. | No direct commits. PR required. 1 approval required. CI must pass. |
| `develop` | Integration branch. All feature branches merge here. Deployed to staging automatically. | No direct commits. PR required. 1 approval required. CI must pass. |
| `feature/<description>` | New features. One branch per feature. Branches off `develop`. | No restrictions. Developer's working branch. |
| `hotfix/<description>` | Urgent production fixes. Branches off `main`. Merged to both `main` and `develop`. | No direct commits to `main` even for hotfixes — PR required. |
| `release/<version>` | Release preparation. Branches off `develop`. Minor bug fixes only. | No new features. Merges to `main` and back to `develop`. |

**Branch naming examples:**

- `feature/agent-remittance-fifo-allocation`
- `feature/farmer-contribution-stage3-ui`
- `feature/efris-retry-queue`
- `hotfix/payer-nssf-calculation-rounding`
- `release/1.2.0`

No developer commits directly to `main` or `develop`. The CI pipeline blocks direct pushes to protected branches.

## 3.2 Commit Message Format (Conventional Commits)

All commit messages follow the Conventional Commits specification (conventionalcommits.org):

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

**Types:**

| Type | When to use |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or updating tests |
| `docs` | Documentation changes only |
| `chore` | Build tooling, dependency updates, CI changes |
| `perf` | Performance improvements |
| `security` | Security fixes — always use this type for security-related changes |

**Scopes (BIRDC ERP modules):**

`sales`, `pos`, `inventory`, `agents`, `finance`, `gl`, `payroll`, `procurement`, `farmers`, `production`, `qc`, `hr`, `efris`, `auth`, `admin`, `android-agent`, `android-farmer`, `android-warehouse`, `android-exec`, `android-hr`, `android-factory`

**Examples:**

```
feat(agents): implement FIFO remittance allocation via sp_apply_remittance_to_invoices

Enforces BR-002. The stored procedure allocates remittances to outstanding invoices
in oldest-first order. Partial allocation is supported when remittance < oldest invoice.

Closes #42
```

```
fix(payroll): correct PAYE calculation for employees earning exactly the band boundary

PAYE band boundary values were being taxed at the higher rate due to an off-by-one
error in the tax band comparison. Fixed to use >= for lower bound and < for upper bound.

Fixes #89
```

```
security(auth): enforce account lockout after 5 failed login attempts

Implements rate limiting middleware that tracks failed attempts per username
in tbl_login_attempts. Lockout duration is configurable (default 15 minutes).
IT Administrator receives email alert on each lockout event.
```

**Short description rules:**

- Imperative mood: "add", "fix", "implement" — not "added", "fixed", "implementing".
- Maximum 72 characters.
- No full stop at the end.
- Does not repeat the type: `feat(pos): add barcode scanning` not `feat(pos): added barcode scanning feature`.

## 3.3 Pull Request Template

Every pull request must complete the following template. PRs with incomplete templates are not reviewed.

```markdown
## Summary

<!-- 2–4 bullet points describing what this PR does. -->

- 
- 

## Business Rule Reference

<!-- List every BR affected or enforced by this change. -->

| Rule | How enforced in this PR |
|---|---|
| BR-XXX | |

## Testing Done

<!-- What tests were run? What was the result? -->

- [ ] PHPUnit / unit tests pass locally
- [ ] Relevant integration tests pass
- [ ] Manual test: [describe what was tested and the result]

## Security Checklist

<!-- Complete every item. Check the box or explain N/A. -->

- [ ] No raw SQL — all queries use PDO prepared statements
- [ ] All user output escaped with `htmlspecialchars()` (web) or Compose text binding (Android)
- [ ] CSRF token present on all new state-changing forms
- [ ] RBAC permission check on every new API endpoint
- [ ] Audit log entry added for every new financial transaction type
- [ ] No credentials, API keys, or secrets in code or config files
- [ ] No hardcoded business rules — all configurable values use configuration tables (DC-002)
- [ ] `declare(strict_types=1)` on every new PHP file

## Reviewer Notes

<!-- Anything specific the reviewer should check or pay attention to. -->
```

## 3.4 Merge Rules

- **Squash merge** from `feature/*` into `develop` — keeps `develop` history clean.
- **Merge commit** (no squash) from `develop` into `main` — preserves the full feature history in production.
- **No force push** to `main` or `develop`. Force push to feature branches is permitted but discouraged.
- **Delete branch** after merge — the remote feature branch is deleted automatically after the PR is merged.
- **Rebase instead of merge** on feature branches to keep the branch up to date with `develop` before raising a PR.

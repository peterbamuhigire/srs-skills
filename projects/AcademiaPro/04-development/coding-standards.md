# Coding Standards — Academia Pro

The authoritative coding standards document is `02-coding-guidelines/01-coding-guidelines.md`. This file is the top-of-phase index required by `phase04.coding_standards_referenced` and summarises the rules the engine treats as canonical.

## Languages

- PHP 8.2+ — backend. Laravel 11. PSR-12 formatting enforced by `php-cs-fixer`. PHPStan level 7 required on every merge.
- TypeScript 5.x — web frontend. React 18. `strict: true` in `tsconfig.json`. ESLint with `airbnb-typescript`.
- Kotlin 1.9 — Android. Jetpack Compose. `detekt` and `ktlint` on every build.
- Swift 5.9 — iOS. SwiftUI. SwiftLint on every build.
- SQL — MySQL 8 dialect. Every migration reversible. No destructive `DROP COLUMN` without a two-release deprecation window.

## Mandatory Practices

- TDD — every FR implementation begins with a failing test, referenced in the commit message.
- Every PR references at least one baselined identifier (FR-, NFR-, BR-, CTRL-). Enforced by PR template and CI check.
- TenantScope tests — any new tenant-scoped model ships with a cross-tenant leakage test.
- PIIScrubber coverage — any new AI call ships with a scrubber unit test per ADR-0005.

## Style, Naming, Error Handling

See `02-coding-guidelines/01-coding-guidelines.md §3, §4, §5` for the full rules including variable naming, error wrapping, logging levels, and API response envelopes.

## Traces to Requirements

- NFR-MAINT-001 (maintainability) — requires static analysis pass rate ≥ 95%.
- NFR-SEC-006 (secure coding) — OWASP Top 10 checklist referenced in review.

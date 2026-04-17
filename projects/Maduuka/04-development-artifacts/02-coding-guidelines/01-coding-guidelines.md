---
title: "Maduuka -- Coding Guidelines"
version: "1.0"
date: "2026-04-05"
status: "Draft"
owner: "Peter Bamuhigire -- Chwezi Core Systems"
---

# Maduuka -- Coding Guidelines

**Project:** Maduuka
**Version:** 1.0
**Date:** 2026-04-05
**Status:** Draft
**Owner:** Peter Bamuhigire -- Chwezi Core Systems

---

## 1. Purpose and Scope

These guidelines are mandatory for all contributors to the Maduuka codebase. Pull requests (PRs) that violate these standards are rejected at review without exception. The guidelines cover the PHP backend, Android (Kotlin), and iOS (Swift) platforms, plus universal rules that apply across all platforms.

---

## 2. Universal Rules (All Platforms)

The following rules apply to every file in every platform:

- **No hardcoded locale data.** Currency symbols, country codes, phone number prefixes, and tax rates must come from the application configuration or database -- never from source code literals.
- **No hardcoded `franchise_id`.** Every data access operation must derive `franchise_id` from the authenticated user's session or token. A tenant identifier must never appear as a literal value in source code.
- **No secrets in source files.** API keys, credentials, database passwords, and connection strings must be stored in environment variables. They must never appear in source files, committed configuration files, or version control history.
- **Internationalisation (i18n) required.** All user-facing text must support localisation. Phase 1 targets English and Swahili. Strings must be externalised to the appropriate resource file for each platform (`strings.xml` on Android, Localizable strings on iOS, language files on PHP/web).
- **Audit log on every write.** Every create, update, delete, void, and adjustment operation must write a corresponding entry to the audit log before the operation is considered complete. An operation without an audit entry is considered incomplete.
- **Actionable error messages.** Error messages shown to the end user must be specific and actionable. Stack traces, database error messages, and internal exception details must never be exposed to the end user.

---

## 3. PHP Backend Standards

### 3.1 Language and Type Safety

- PHP 8.3+ with `declare(strict_types=1)` at the top of every file.
- Named arguments are required for all function calls with 3 or more parameters.
- Use PHP 8.1+ enums for all status values. Example: `OrderStatus::PENDING`, not the string literal `'pending'`.

### 3.2 Code Style and Static Analysis

- PSR-12 code style, enforced by PHP_CodeSniffer in the CI pipeline. Zero violations are required.
- PHPStan at level 8. Suppressing an error with `@phpstan-ignore` requires a documented justification comment on the same line. Undocumented suppressions are a CI failure.

### 3.3 Architecture

- Service layer pattern is mandatory: controllers call service classes, not Eloquent models or database queries directly.
- Every public method on a service class has a corresponding unit test.

### 3.4 Security

- **SQL injection prevention:** Parameterised queries only. String concatenation inside any SQL query is a blocking PR defect.
- **CSRF protection:** `csrf_token()` validation is applied in middleware to every `POST`, `PUT`, `PATCH`, and `DELETE` request. Controller-level CSRF checks are not a substitute for middleware enforcement.
- **Password hashing:** `password_hash()` with `PASSWORD_BCRYPT` and a cost factor of 12 or higher. `MD5`, `SHA-1`, and unsalted hashes are prohibited.
- **Log hygiene:** Personally Identifiable Information (PII), passwords, and tokens must never appear in application log output. Mask or omit these values before passing them to any logger.

---

## 4. Android (Kotlin) Standards

### 4.1 Language Idioms

Use idiomatic Kotlin throughout:

- Data classes for all data-transfer and domain model types.
- Sealed classes for representing finite sets of states (e.g., UI state, network result).
- Extension functions to add behaviour to existing types rather than creating utility classes.
- Coroutines over callbacks for all asynchronous operations.

### 4.2 Jetpack Compose

- Stateless composables are preferred. State is hoisted to the ViewModel.
- Composables must not directly access Room Data Access Objects (DAOs) or Retrofit service interfaces.

### 4.3 Architecture

- Repository pattern is mandatory. ViewModels call Repository interfaces; they must not access Room DAOs or Retrofit service interfaces directly.
- `franchise_id` is injected as an explicit parameter into every Repository method. It must never be stored as a global variable, singleton, or companion object property.

### 4.4 Threading

No blocking calls on the main thread. All database and network I/O runs on `Dispatchers.IO`. All UI state updates run on `Dispatchers.Main`.

### 4.5 Error Handling

A sealed `Result<T, E>` type is used throughout the Domain and Data layers. Raw exceptions must not propagate into ViewModels. Every error case is represented as a typed value.

### 4.6 Resource Files

- All user-facing strings are defined in `strings.xml`. No string literals in Kotlin source files.
- All dimension values are defined in `dimens.xml` or as Compose `dp` / `sp` constants. No hardcoded pixel values.

### 4.7 Tests

- Every ViewModel class has a corresponding unit test class.
- Every Repository class has a corresponding unit test class using a fake or mock data source.
- Every Room DAO has a corresponding instrumented test running against an in-memory database.

---

## 5. iOS (Swift) Standards

### 5.1 Language and Concurrency

- Swift 5.9+ with strict concurrency enabled.
- `@MainActor` applied to all ViewModel and UI-bound classes.
- `async/await` is mandatory for all asynchronous operations. Completion handler callbacks are prohibited in new code.
- All types crossing actor boundaries must conform to `Sendable`.

### 5.2 SwiftUI Architecture

- ViewModels are `@Observable` (iOS 17+) or `ObservableObject` (iOS 16 fallback for the minimum deployment target).
- Views must not access Core Data managed object contexts directly. All data access goes through a Repository interface.

### 5.3 Repository Pattern

- Repository pattern is mandatory, identical in intent to the Android requirement.
- `franchiseId` is passed as an explicit parameter to every repository call. Singleton or global storage of `franchiseId` is prohibited.

### 5.4 Error Handling

- Typed errors using `Result<T, AppError>` throughout Domain and Data layers.
- Force unwraps (`!`) are prohibited in production code. Every optional must be unwrapped safely with `if let`, `guard let`, or `??`.

### 5.5 Secure Storage

- All tokens and sensitive data are stored via a `KeychainWrapper` abstraction.
- Storage in `UserDefaults` for any sensitive value is prohibited.

### 5.6 Memory Management

- `[weak self]` is required in all closures that capture `self` to avoid retain cycles.
- Instruments (Leaks and Allocations) must be run before every release build. Unresolved memory leaks block release.

### 5.7 Tests

- Every ViewModel class has a corresponding unit test class.
- Every Repository class has a corresponding unit test class using a mock or in-memory data source.
- The Core Data stack has integration tests verifying the migration path from version N to version N+1 before any schema migration is merged.

---

## 6. Git Workflow

### 6.1 Branch Naming

| Branch type | Format |
|---|---|
| Feature | `feature/TASK-ID-short-description` |
| Bug fix | `fix/TASK-ID-short-description` |
| Chore / maintenance | `chore/short-description` |

### 6.2 Commit Message Format

Commits follow the Conventional Commits specification:

```
<type>(<module>): <description>
```

Permitted types: `feat`, `fix`, `test`, `refactor`, `chore`, `docs`, `style`, `ci`.

Examples:

- `feat(pos): add mobile money payment flow`
- `fix(inventory): correct stock deduction on split sale`
- `test(auth): add refresh token expiry unit tests`

### 6.3 Pull Request Requirements

Every PR must include:

1. A description of what changed and why.
2. Test evidence -- a screenshot of the passing test output or a screen recording of the UI behaviour.
3. Reviewer assignment -- at least 1 reviewer must approve before merge.

Self-merge is prohibited. Force-push to `main` or `staging` is prohibited.

---

## 7. Security Checklist (Per PR)

The following checklist must be completed by the PR author before requesting review. Reviewers verify completion.

- [ ] No hardcoded credentials or API keys in any file.
- [ ] All user input is validated (type, length, format) and sanitised before use.
- [ ] SQL injection: parameterised queries used throughout -- no string concatenation in queries.
- [ ] CSRF protection is active on all state-changing web forms.
- [ ] The API endpoint introduced or modified has RBAC middleware applied.
- [ ] No sensitive data (PII, tokens, passwords) appears in application log output.
- [ ] No `franchise_id` bypass is possible -- tenant scoping is enforced at the service or repository layer.

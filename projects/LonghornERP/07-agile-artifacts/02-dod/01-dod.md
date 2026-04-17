# Definition of Done — Longhorn ERP

A feature is *Done* when ALL of the following criteria are met. Each criterion is a binary, verifiable gate — pass or fail, with no room for judgment.

## Code Quality

1. All FR-*-* requirements for the feature are implemented and match the SRS exactly.
2. PHPStan reports zero errors at level 8 for all files touched by the feature.
3. PHP CS Fixer reports zero violations for all files touched by the feature.
4. No `var_dump()`, `print_r()`, `dd()`, or commented-out code exists in any committed file.

## Testing

5. PHPUnit unit tests exist for the service class and all public methods have at least 1 test.
6. PHPUnit test suite passes 100% — no skipped tests for this feature.
7. Unit test line coverage ≥ 80% for the feature's service class(es).
8. Integration test confirms: every state-changing operation writes an audit log record.
9. Tenant isolation test passes: cross-tenant access attempt returns HTTP 404.

## Security

10. `RequirePermission` middleware is applied to all new endpoints; missing permission returns HTTP 403.
11. All new SQL queries use PDO prepared statements — no string concatenation in SQL.
12. All user input is validated before use; no raw `$_GET` or `$_POST` without validation.
13. `tenant_id` in all new queries comes from `SessionService::getTenantId()` — never from request input.

## Integration and GL

14. All financial transactions post correct double-entry GL entries, verified by integration test: `sum(debit) = sum(credit)`.
15. All stock-moving operations write a stock ledger entry, verified by integration test.

## Documentation

16. All new domain terms are added to `_context/glossary.md`.
17. Open `[CONTEXT-GAP]`, `[V&V-FAIL]`, or `[TRACE-GAP]` flags in the SRS for this feature are resolved or formally accepted by the product owner.
18. API endpoint(s) for the feature are documented in the API Specification.

## UX

19. Feature reviewed against UX Specification: layout, navigation, component usage, and error handling match the spec.
20. All confirmation dialogs for destructive actions use the SweetAlert2 confirmation pattern.
21. WCAG 2.1 AA: colour contrast checked; all form fields have accessible labels.

## Acceptance

22. Product owner has reviewed and approved the feature against the acceptance criteria in the SRS.
23. No Critical or High severity defects are open against this feature.

---

## DoD Checklist — Copy into PR Description

```markdown
### Definition of Done Checklist

**Code Quality**
- [ ] All FR-*-* requirements for the feature are implemented and match the SRS exactly.
- [ ] PHPStan reports zero errors at level 8 for all files touched by the feature.
- [ ] PHP CS Fixer reports zero violations for all files touched by the feature.
- [ ] No `var_dump()`, `print_r()`, `dd()`, or commented-out code in any committed file.

**Testing**
- [ ] PHPUnit unit tests exist for the service class and all public methods have at least 1 test.
- [ ] PHPUnit test suite passes 100% — no skipped tests for this feature.
- [ ] Unit test line coverage ≥ 80% for the feature's service class(es).
- [ ] Integration test confirms: every state-changing operation writes an audit log record.
- [ ] Tenant isolation test passes: cross-tenant access attempt returns HTTP 404.

**Security**
- [ ] `RequirePermission` middleware is applied to all new endpoints; missing permission returns HTTP 403.
- [ ] All new SQL queries use PDO prepared statements — no string concatenation in SQL.
- [ ] All user input is validated before use; no raw `$_GET` or `$_POST` without validation.
- [ ] `tenant_id` in all new queries comes from `SessionService::getTenantId()` — never from request input.

**Integration and GL**
- [ ] All financial transactions post correct double-entry GL entries (integration test: sum(debit) = sum(credit)).
- [ ] All stock-moving operations write a stock ledger entry (integration test).

**Documentation**
- [ ] All new domain terms added to `_context/glossary.md`.
- [ ] Open `[CONTEXT-GAP]`, `[V&V-FAIL]`, or `[TRACE-GAP]` flags resolved or formally accepted by product owner.
- [ ] API endpoint(s) documented in the API Specification.

**UX**
- [ ] Feature reviewed against UX Specification: layout, navigation, component usage, and error handling match.
- [ ] All confirmation dialogs for destructive actions use SweetAlert2 confirmation pattern.
- [ ] WCAG 2.1 AA: colour contrast checked; all form fields have accessible labels.

**Acceptance**
- [ ] Product owner has reviewed and approved the feature against SRS acceptance criteria.
- [ ] No Critical or High severity defects open against this feature.
```

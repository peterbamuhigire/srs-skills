# Definition of Ready — Longhorn ERP

A feature is *Ready* to develop when ALL of the following pre-conditions are met. Each criterion is a binary gate — the feature does not enter the sprint until every condition passes.

## Requirements

1. The SRS section for this feature exists and has no open `[CONTEXT-GAP]` flags.
2. All FR-*-* identifiers for this feature are present in the SRS with stimulus-response format.
3. All NFR-*-* requirements affecting this feature have measurable thresholds — no `[SMART-FAIL]` flags.
4. No `[V&V-FAIL]` tags remain unresolved in this feature's SRS section.

## Design

5. Database schema for the feature is defined: table names, column names, data types, and FK relationships are specified.
6. API endpoint(s) for the feature are specified in the API Specification: method, path, request schema, and response schema are present.
7. All new UI screens are described in the UX Specification: layout, components, and interaction patterns are documented.

## Traceability

8. Every FR-*-* for this feature links to at least 1 business goal — no `[TRACE-GAP-BG]` flags.
9. Every FR-*-* for this feature has at least 1 planned test case in the Test Plan — no `[TRACE-GAP-TC]` flags.

## Dependencies

10. All module dependencies are resolved: if this feature requires another module (e.g., Manufacturing requires Advanced Inventory), that module's feature is already Done or will be Done in the same sprint.
11. Any external API dependency (EFRIS, MoMo) either has confirmed credentials or is explicitly stubbed with a `[CONTEXT-GAP]` accepted by the product owner.

## Glossary

12. All new domain terms introduced by this feature are defined in `_context/glossary.md`.

## Estimation

13. The feature has been sized by the developer in story points or hours.
14. The feature can be completed in a single sprint — if not, it must be split into smaller features before it is considered Ready.

---

## DoR Checklist — Copy into Sprint Planning Board

```markdown
### Definition of Ready Checklist

**Requirements**
- [ ] SRS section for this feature exists with no open `[CONTEXT-GAP]` flags.
- [ ] All FR-*-* identifiers are present in the SRS with stimulus-response format.
- [ ] All NFR-*-* requirements have measurable thresholds — no `[SMART-FAIL]` flags.
- [ ] No `[V&V-FAIL]` tags remain unresolved in this feature's SRS section.

**Design**
- [ ] Database schema defined: table names, column names, data types, FK relationships.
- [ ] API endpoint(s) specified in API Specification: method, path, request/response schema.
- [ ] All new UI screens described in UX Specification: layout, components, interaction patterns.

**Traceability**
- [ ] Every FR-*-* links to at least 1 business goal — no `[TRACE-GAP-BG]` flags.
- [ ] Every FR-*-* has at least 1 planned test case in the Test Plan — no `[TRACE-GAP-TC]` flags.

**Dependencies**
- [ ] All module dependencies resolved — dependent features are Done or in-sprint.
- [ ] External API dependencies have confirmed credentials or are formally stubbed.

**Glossary**
- [ ] All new domain terms defined in `_context/glossary.md`.

**Estimation**
- [ ] Feature sized by developer (story points or hours).
- [ ] Feature fits in a single sprint, or has been split.
```

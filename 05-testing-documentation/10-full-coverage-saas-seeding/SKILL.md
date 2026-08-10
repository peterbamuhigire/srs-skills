---
name: 10-full-coverage-saas-seeding
description: Use when specifying, planning, tracing, or reviewing realistic synthetic SaaS demo data and application-workflow test coverage for an SRS, PRD, test plan, release gate, or go-live evidence pack.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Full-Coverage SaaS Seeding

<!-- dual-compat-start -->
## Use When

- An SRS or test programme must define a coherent demo tenant and a complete,
  repeatable fixture for testing every supported SaaS module.
- Product, QA, engineering, and demo teams need traceable data journeys from
  onboarding through operations, reporting, administration, and reset.
- Requirements must specify that writes go through the product's authenticated UI,
  supported APIs, application services, commands, workflow handlers, posting
  services, or event/outbox boundaries.

## Do Not Use When

- The work is only permanent reference-data installation, migrations, or template
  bootstrap; route to the relevant architecture/database/bootstrap skill.
- The requester asks the SRS engine to mutate a tenant, database, production system,
  external integration, or live communications. This skill specifies and verifies;
  implementation execution routes to skills-web-dev's matching skill.
- A capability is assumed from a menu, schema, or migration without an executable
  application boundary. Record a blocker or `NOT_ASSESSED` status.

## Core distinction: default/reference data versus demo data

Every specification must separate these layers:

| Layer | Examples | Requirement |
|---|---|---|
| Default/reference data | System-owned global categories, coding/ICD lists, medicine or laboratory lists, UOMs, countries, currencies, statuses, permissions, tax configuration, and other standard catalogues | Version, source, bootstrap owner, availability, and preservation check; never count as tenant demo activity or delete on reset |
| Tenant configuration | Fictional organisation/facility, departments, settings, fiscal periods, roles, grants, prices, policies, and test adapters | Define tenant owner, scope, lifecycle, and reset boundary |
| Demo activity | Fictional patients, doctors, staff, members, customers, suppliers, products, appointments, orders, encounters, invoices, payments, reports, and audit activity | Define stable keys, realistic journeys, volumes, actor permissions, downstream effects, and disposable ownership |
| Fault probes | Invalid, duplicate, replay, forbidden, timeout, partial-failure, rollback, privacy, and isolation cases | Keep isolated, tagged, expected outcome, and evidence location; never disguise a fault as a happy-path demo |

For a hospital, patients and doctors are demo activity; ICD, medicine, laboratory,
units, statuses, global categories, permissions, and other system-owned catalogues
are default/reference data. The patient may select an ICD item through the product,
but the fixture must not create a replacement ICD catalogue or treat it as demo data.
Apply the same rule to any other SaaS domain.

## Required Inputs

| Artefact | Source/provider | Required | Purpose | If absent |
|---|---|---:|---|---|
| Approved PRD/SRS, architecture, module list, business rules, target environment, and risk scope | Product and engineering sources | Yes | Define traceable coverage | Stop the affected branch |
| Routes/screens, API/service contracts, permissions, state machines, reports, integrations, tests, and existing fixtures | Repository and deployed product | Yes when assessing implementation | Discover real boundaries and gaps | Mark `NOT_ASSESSED` |
| Product owner, engineering owner, QA owner, demo operator, tenant/facility scope, retention, reset authority | Accountable delivery owners | Yes | Assign accountability and safe target | Return an authority gap |
| Finance/accounting doctrine and jurisdictional source register | Chwezi and current source registers | When applicable | Preserve financial and current-source controls | Route or mark blocked |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Discovery and capability matrix | Product, engineering, QA, demo, and release owners | Every applicable capability has evidence, boundary, status, owner, and blocker reason |
| Seed manifest, scenario catalogue, and classification register | Engineering and QA | Stable keys, default/demo separation, prerequisites, actors, states, negative cases, and invariants are explicit |
| Execution, verification, reset, defect, and evidence contracts | Engineering, QA, and release owner | Replay, isolation, privacy, reconciliation, rollback, and preservation checks are reproducible |
| Release verdict | Accountable release owner | Verdict is `PASS`, `PASS_WITH_CAVEATS`, `BLOCKED`, or `FAIL` with evidence and limitations |

1. Discovery report and capability matrix with evidence, boundary, roles,
   preconditions, states, negative cases, and `SUPPORTED`/`PARTIAL`/`BLOCKED`/
   `NOT_ASSESSED` status.
2. Data classification and reference-data preservation register.
3. Versioned manifest contract with stable natural keys, cohorts, dependencies,
   actors, expected states, invariants, negative cases, checksum, and no SQL,
   passwords, tokens, numeric foreign keys, or real regulated data.
4. Per-tenant/facility roster with hard minimum and target counts.
5. Module scenario catalogue covering happy, failure, permission, duplicate,
   replay, boundary, rollback, isolation, reporting, and audit journeys.
6. Application execution plan naming the UI/API/service boundary and actor for each
   write; a missing boundary becomes `BLOCKED_CAPABILITY`.
7. Verification/reconciliation plan, defect loop, reset/replay runbook, evidence
   pack, contract tests, known limitations, and release verdict.

## Workflow

1. Establish authority, named non-production target, data retention, reset boundary,
   secret mechanism, test adapters, no-real-side-effect rule, and ownership. Refuse
   production or an ambiguous target; stop when authority or target safety is unclear.
2. Inspect the repository and product. Build the capability matrix from routes,
   services, contracts, permissions, states, reports, integrations, tests,
   bootstrap/reference paths, and existing fixture violations. Do not infer a
   module from a table or menu.
3. Classify default/reference data, tenant configuration, demo activity, and fault
   probes. Specify source/version and preservation checks for global catalogues.
4. Define measurable volumes per tenant/facility and diverse cohorts: new/returning,
   active/inactive, complete/incomplete, normal/exception, privacy-restricted, and
   other domain-relevant variants. Link every later workflow to an actor and source.
5. Define fictional identities, roles, departments, supervisors, facility grants,
   account states, and preparer/approver separation for purchasing, refunds,
   payroll, inventory, results, and close. Test suspension/offboarding attribution.
6. Specify chained module journeys. For every supported module record prerequisites,
   boundary, actor, input, state transitions, entities, audit events, downstream
   effects, reports, duplicate/replay, partial failure, rollback, and negative cases.
7. Specify an execution adapter that carries tenant, actor, scenario, idempotency,
   correlation, and manifest checksum. Prohibit SQL/DML, direct database handles,
   table-name fixtures, arbitrary repository calls, and private persistence paths.
8. Specify preflight and dry-run checks: schema, tenant/facility codes, actor
   compatibility, references, dates/timezones, amounts/quantities, collisions,
   dependency order, target safety, and expected counts/invariants. Dry-run writes
   zero business data.
9. Specify dependency-order execution, run/entity ledgers, fault and security
   probes, and test adapters for payments, notifications, webhooks, and integrations.
10. Specify verification of counts, states, permissions, idempotency, audit,
    isolation, privacy, reports, lineage, stock, payroll, AP/AR, cash/bank/mobile
    money, and accounting invariants where applicable.
11. Link each failure to scenario, actor, tenant/facility, route/service, evidence,
    severity, owner, fix, and retest. Repair application code/configuration, recover
    safely where supported, not seeded rows; preserve failed evidence.
12. Specify replay, owned-activity reset, default/reference-data preservation,
    unrelated-tenant preservation, second-clean-target reproduction, handoff, and
    final verdict: `PASS`, `PASS_WITH_CAVEATS`, `BLOCKED`, or `FAIL`.

## Finance, privacy, and release rules

When applicable, require canonical accounting doctrine, source events, balanced
immutable idempotent journals, period controls, reversals/compensation, subledger
tie-outs, controlled stock variance/expiry, payroll separation, and current source
registers. Never specify hard-coded statutory rates or direct journal creation.
Require synthetic identities, encrypted sensitive test data, no reusable secrets,
no real outbound effects, and explicit cross-tenant refusal evidence.

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Capability, classification, and traceability records | Markdown tables and project registers | Every supported or blocked decision names inspected evidence and an owner |
| Execution, verification, and defect results | Run ledger, test report, logs, screenshots where useful | Another reviewer can reproduce the result and distinguish unassessed from passed |
| Reset, replay, preservation, and release record | Evidence pack and sign-off | No duplicate effects; default/reference and unrelated tenant data are proven unchanged |

## Capability and permission boundaries

Read and search are required for specification work. This skill is read-only by
default and may author the named SRS/test artefacts only when explicitly requested
by the accountable authority.
It must not mutate a tenant, database, live integration, or production system.
Route implementation and non-production execution to the software-engineering
companion skill; route finance controls to Chwezi and current claims to Digital
Research where applicable.

## Degraded mode

If repository, runtime, routes, services, references, target, reviewer, or evidence
are unavailable, produce the narrowest qualified specification, mark affected
checks `not assessed`,
preserve the intended oracle, and name the unblock owner.
Never convert an unavailable application boundary into a pass.

## Decision Rules

| Condition | Action | Risk avoided |
|---|---|---|
| A required capability has no supported application boundary | Record `BLOCKED_CAPABILITY` and stop that branch | Direct-write bypass |
| Data is system-owned global/reference data | Preserve source/version and exclude it from demo counts and reset | Catalogue loss or false demo coverage |
| Evidence is partial or unexecuted | Mark `NOT_ASSESSED` and retain the oracle | False readiness |
| A change passes its traceability, safety, and evidence gates | Standardise the contract and schedule re-audit | Repeated fixture drift |

## Quality Standards

- Every requirement and scenario has a deterministic acceptance oracle.
- Default/reference data, tenant configuration, demo activity, and fault probes are visibly distinct.
- No evidence claim is based on a populated screen alone.
- Security, privacy, tenant isolation, finance, rollback, idempotency, and reset boundaries remain explicit.
- Use British English, preserve project terminology, and keep unsupported claims qualified.

## Anti-Patterns

- Treating global categories or standard catalogues as demo rows. Fix: classify and preserve them as `reference` data.
- Planning a seed from tables or menus alone. Fix: name and verify the application boundary.
- Replacing a blocked service with SQL. Fix: return `BLOCKED_CAPABILITY`.
- Omitting failed, duplicate, replay, or isolation cases. Fix: add scenario-specific oracles and evidence.
- Calling a document or fixture complete without execution proof. Fix: retain the gap and assign the verifier.

## Acceptance and handoff

The SRS/test artefacts must expose target safety, capability status, classification,
manifest/version/checksum, scenario order, planned counts, application boundary,
actor/permission, positive and negative results, replay/reset evidence, defects,
limitations, exact verification methods, and the release verdict. A screenshot or
populated screen cannot prove balances, isolation, privacy, rollback, idempotency,
or complete module coverage.

## References

- [Seed manifest contract](references/seed-manifest-contract.md) — required manifest and classification fields.
- [Module coverage matrix](references/module-coverage-matrix.md) — module journey and evidence prompts.
- [Contract test matrix](references/contract-test-matrix.md) — skill routing and refusal cases.
- `05-testing-documentation/02-test-plan` — consume this skill's scenarios and data requirements.
- `skills-web-dev/skills/saas/full-coverage-saas-seeding` — implementation/execution companion; resolve via the global routing table.
- `09-governance-compliance/11-saas-data-isolation-evidence-pack` — tenant isolation evidence.
- `09-governance-compliance/31-kaizen-engine-and-product-improvement` — apply the 65-to-95 improvement gate to this skill and each product fixture.
<!-- dual-compat-end -->

---
name: 08-accounting-engine-test-plan
description: Use when producing or updating accounting-engine test plan for ledger invariants, posting, reversal, period control, reconciliation, migration, and audit evidence. Use test-plan for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Accounting Engine Test Plan

<!-- dual-compat-start -->
## Use When

- Produce or update accounting-engine test plan from approved project evidence.
- Resolve decisions about ledger invariants, posting, reversal, period control, reconciliation, migration, and audit evidence.
- Prepare a reviewable handoff for Finance controller, QA, and engineering.

## Do Not Use When

- The task is primarily owned by test-plan; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, architecture, and implemented posting rules | Project owner, engineering, and finance controller | Required | Stop; do not infer ledger behaviour, balances, rates, or authority. |
| Current finance doctrine and applicable source evidence | chwezi-accounting-doctrine router, finance controller, and verified current sources | Required | Mark the gate unassessed and block any finance pass or release claim. |
| Environment, tenant, period state, and operation authority | Service owner and finance controller | Required for execution | Stay read-only and return the missing-authority checklist. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Accounting-engine Test Plan | Finance controller, QA, and engineering | Every finance flow proves balanced immutable postings, tenant isolation, idempotency, period control, reconciliation, and traceable evidence. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.
- Run and record the finance and accounting quality gate before accepting the artefact. Preserve double-entry balance, journal immutability, idempotency, tenant isolation, period locks, source-document traceability, and reconciliation invariants; never invent statutory rates.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose tests from finance doctrine and the implemented posting rules and produce the full artefact. | A UI-only pass that misses ledger corruption. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring test-plan concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every finance flow proves balanced immutable postings, tenant isolation, idempotency, period control, reconciliation, and traceable evidence.

## References

- [Repository router](../../README.md) - project pathing, phase sequence, and delivery rules.
<!-- dual-compat-end -->
## Use When

- The system has an embedded ledger, billing, inventory valuation, payroll, tax, grants, or financial statements.
- A release can affect posted journals, balances, accounting periods, or reports.

## Mandatory Test Suites

1. Balanced journal tests: every journal entry has equal debits and credits.
2. Posting service tests: all writes pass through `LedgerPostingService`; direct table writes fail review/CI checks.
3. Idempotency tests: duplicate source event with same key does not double-post.
4. Period tests: open periods allow posting; closed/locked periods reject posting unless approved workflow exists.
5. Reversal tests: corrections create linked reversing journals; original lines remain unchanged.
6. Subledger tests: AR/AP/customer/supplier balances equal control accounts.
7. Inventory tests: GL inventory equals stock-on-hand value by item/location/cost layer; sale posts COGS.
8. Fixed asset tests: asset register equals GL cost and accumulated depreciation; disposal gain/loss is correct.
9. Payroll tests: gross pay, employer cost, employee deductions, liabilities, net pay, and remittances reconcile.
10. FX tests: transaction-date rates, settlement differences, and month-end revaluation post realised/unrealised gains/losses correctly.
11. Report tests: trial balance, income statement, statement of financial position, cash flow, and equity/net-asset reports regenerate from journal lines.
12. Tenant isolation tests: one tenant cannot read or post to another tenant's accounts, mappings, periods, or journals.

## Acceptance Criteria Pattern

```text
Given a locked accounting period
When a business module attempts to post a sale dated in that period
Then the posting service rejects the entry
And no journal header or line is inserted
And the rejection names the locked period and source document.
```

## Outputs

- Accounting test plan.
- Invariant matrix.
- Test data scenarios.
- Release-blocking acceptance criteria.

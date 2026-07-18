---
name: 21-accounting-operations-runbook
description: Use when producing or updating accounting operations runbook for opening balances, close, ledger integrity, reconciliation incidents, rebuilds, controls, and audit evidence. Use runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Accounting Operations Runbook

<!-- dual-compat-start -->
## Use When

- Produce or update accounting operations runbook from approved project evidence.
- Resolve decisions about opening balances, close, ledger integrity, reconciliation incidents, rebuilds, controls, and audit evidence.
- Prepare a reviewable handoff for Finance controller, operations, and audit.

## Do Not Use When

- The task is primarily owned by runbook; route there and use this skill only for its named output.
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
| Accounting Operations Runbook | Finance controller, operations, and audit | Every accounting operation preserves balanced immutable journals, period controls, source evidence, tenant isolation, and approved recovery. |
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
- Inspection is read-only by default. Create or edit the named project document only when explicitly authorised. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.
- Run and record the finance and accounting quality gate before accepting the artefact. Preserve double-entry balance, journal immutability, idempotency, tenant isolation, period locks, source-document traceability, and reconciliation invariants; never invent statutory rates.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose actions from finance doctrine, ledger state, and named authority and produce the full artefact. | Silent financial-statement corruption. |
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
- Mixing the neighbouring runbook concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when every accounting operation preserves balanced immutable journals, period controls, source evidence, tenant isolation, and approved recovery.

## References

- [Repository router](../../README.md) - project pathing, phase sequence, and delivery rules.
<!-- dual-compat-end -->
## Use When

- Deploying, operating, migrating, or supporting a system with an embedded ledger.
- Planning go-live, month-end close, audit support, or incident response for accounting data.

## Required Runbook Sections

1. Opening balance migration and sign-off.
2. Posting queue monitoring and retry policy.
3. Nightly per-tenant integrity job and alert routing.
4. Period close checklist.
5. Locked-period exception workflow.
6. Duplicate posting incident procedure.
7. Missing posting incident procedure.
8. Subledger reconciliation failure procedure.
9. Inventory, payroll, fixed asset, tax, and bank/mobile-money reconciliation procedures.
10. Materialized balance and report rebuild command.
11. Audit evidence export pack.
12. First month-end close support plan.

## Safety Rules

- NEVER fix accounting incidents by editing journal lines.
- NEVER unlock a period without named approval, reason, timestamp, and post-close recheck.
- MUST take a backup before migration, opening-balance import, report-cache rebuild, or bulk mapping change.
- MUST preserve source documents and posting-rule versions used at the time of posting.

## Outputs

- Accounting operations runbook.
- Close checklist.
- Incident playbooks.
- Audit evidence checklist.

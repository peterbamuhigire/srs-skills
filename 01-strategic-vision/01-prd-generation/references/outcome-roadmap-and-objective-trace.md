# Outcome Roadmap and Objective-to-Requirement Trace

Parent skill: [PRD generation](../SKILL.md), Step 9 (Release Strategy). Also
consumed by [traceability matrix](../../../09-governance-compliance/01-traceability-matrix/SKILL.md)
for the strategic (forward) half of the RTM.

Use this reference when the PRD needs a release strategy, when a sponsor asks
for a roadmap, or when an RTM must show that every requirement serves a funded
objective. It replaces the "features by quarter" table with a roadmap that
commits to outcomes and an explicit trace chain that an auditor or an AI agent
can walk in both directions.

## 1. The trace chain

Every baselined requirement sits on one unbroken chain:

```text
OBJ  business objective (funded, owned, dated)
 └─ OUT  outcome: a change in actor behaviour or business result, with metric, baseline, target, window
     └─ OPP  opportunity: the problem or unmet need that, if solved, moves the outcome (Opportunity Record O1)
         └─ RSK  product-risk evidence row (value, usability, feasibility, viability)
             └─ REQ  functional or non-functional requirement (stimulus-response, fit criterion)
                 └─ ACC  acceptance test or named review
                     └─ TEL  telemetry event or report that measures OUT in production
```

Identifier rules:

- `OBJ-nn` comes from `vision.md` business goals (the RTM's `BG-nnn` maps
  one-to-one; keep one scheme per project and record the alias).
- `OUT-nn` belongs to exactly one `OBJ`. An outcome serving two objectives is
  split or the objectives are merged.
- `REQ` may link to several `OPP` rows; it must link to at least one.
- `TEL` names the event, its owner, and the report or dashboard where the
  outcome is read. "Analytics" is not an answer.

### Orphan and dead-end checks

| Check | Rule | Tag on failure |
|---|---|---|
| Orphan requirement | `REQ` with no path to an `OBJ` | `[TRACE-ORPHAN]`: remove, or record the objective it silently serves |
| Unserved objective | `OBJ` with no `REQ` beneath it | `[TRACE-GAP]`: the objective is unfunded in scope; tell the sponsor |
| Unmeasured outcome | `OUT` with no `TEL` | `[TRACE-BLIND]`: the release cannot be judged; add the instrumentation requirement |
| Untested requirement | `REQ` with no `ACC` | `[V&V-FAIL]` |
| Evidence-free requirement | `REQ` whose `RSK` rows are `OPEN` at E0 | `[DRAFT]` until evidence arrives |
| Platform and compliance work | Security, audit, statutory and operability requirements | Trace to an explicit enabling objective (for example "OBJ-05 Pass URA e-invoicing certification"), never left orphaned |

## 2. Outcome roadmap format

A roadmap commits to problems and outcomes in order, and to dates only where
a date is genuinely fixed (contract, regulation, season, event).

| Horizon | Outcome (OUT) | Opportunity (OPP) | Confidence | Evidence rung | Candidate scope | Date type |
|---|---|---|---|---|---|---|
| Now (committed) | ... | ... | High | E4 or above | Validated minimal product | Committed date |
| Next (shaping) | ... | ... | Medium | E2 to E3 | Options under test | Target window |
| Later (exploring) | ... | ... | Low | E0 to E1 | None; problem statement only | None |

Rules:

- Only the `Now` horizon carries feature scope and a committed date. `Next`
  carries options and a window. `Later` carries problems only.
- A date in `Next` or `Later` that a customer contract depends on is promoted
  to a fixed-date item with its own risk row; do not hide it in a horizon.
- Moving an item from `Next` to `Now` requires the value and usability rows to
  reach `RETIRED` or `ACCEPTED`. This is the roadmap's entry gate.
- Each horizon review records which outcomes moved, by how much, and the
  decision taken: continue, change approach, or stop.

## 3. Release-change requirements for existing users

When a release changes a workflow people already depend on, disruption is a
product risk. The PRD states how change reaches users, as requirements:

| Concern | Requirement pattern | Verification |
|---|---|---|
| Advance notice | The system shall notify affected users of workflow changes no less than N days before activation, in-product and by the channel the user registered | Notification log shows every affected account notified by T-N |
| Choice of timing | For changes to a core daily workflow, the system shall let users opt in early and remain on the previous flow until a published cut-off date | Feature-flag state per account; cut-off enforced on the date |
| Data compatibility | Records created in the previous version shall remain readable and editable after the change | Regression suite on a snapshot of production-shaped data |
| Staged exposure | The release shall reach a named cohort first (region, branch, tenant tier) and widen only when stated guardrail metrics hold for a stated period | Rollout log with guardrail readings at each stage |
| Retirement | The previous flow's retirement date shall be announced no less than N days in advance | Communication record and retirement date in release notes |
| Rapid correction | A defect that blocks a core task in the new flow shall have a stated restore target (rollback or fix) | Incident timeline against the restore target |

N and the guardrails come from project context (user base, contract terms,
support capacity). Never invent them; flag `[CONTEXT-GAP]`.

## 4. Worked example (original)

A Ugandan private-school group commissions a fees and parent-communication
platform.

- `OBJ-01` Reduce fees receivable older than 60 days from 18% to 8% of billed
  fees by the end of Term 3, 2027.
- `OUT-01` Share of parents paying the termly invoice within 14 days of issue,
  baseline 41% (bursar ledger, Term 1 2026), target 65%.
- `OPP-01` Parents do not know the exact balance or the accepted payment
  references, so mobile-money payments arrive unmatched.
- `REQ-FEE-012` When an invoice is issued, the system shall send the parent a
  message containing the balance, the due date, and a payment reference unique
  to the learner, within 5 minutes.
- `ACC-FEE-012` Issue 500 invoices in staging; 100% of messages delivered to the
  test gateway within 5 minutes, each with a unique reference.
- `TEL-01` Event `invoice_paid` with `days_from_issue`; the bursar's weekly
  collection report shows OUT-01 by campus.

Roadmap: `Now` holds OUT-01 with the validated invoice-message and
auto-matching scope. `Next` holds OUT-02 (reduce bursar reconciliation time)
with two options under test. `Later` holds "parents cannot see academic
progress alongside fees" as a problem statement only.

## 5. Premium versus generic output

| Generic output | Premium output |
|---|---|
| Quarterly feature list with dates to Q4 next year | Committed `Now`, shaped `Next`, problems-only `Later` |
| "Improve collections" | Objective with baseline, target, date, and ledger source |
| RTM starting at the requirement | RTM starting at the funded objective and ending at a production metric |
| Release notes after the fact | Notice, opt-in window, staged cohorts and retirement dates as testable requirements |

## Evidence and currentness

- `NO_TIME_SENSITIVE_CLAIMS`. Worked-example figures are illustrative.
- Access date for this synthesis: 2026-09-24.

Sources: Cagan, M. (2008) *Inspired: How to Create Products Customers Love*
(opportunity-first planning, staged deployment of change); Ximenes, F. (2024)
*Strategic Software Engineering* (incremental delivery as risk control);
engine synthesis with IEEE 29148 traceability practice already used by the
parent skills.

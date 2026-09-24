# Data Contract and Data Dictionary Requirements

Parent skill: [05-conceptual-data-modeling](../SKILL.md).

Load when the conceptual model contains data that another team, system, report,
regulator, or AI feature will consume, and the SRS must state what that data
interface guarantees. This file specifies *what* the interface must achieve and
how acceptance is verified. *How* to implement it (contract files, CI gates,
publishing patterns) belongs to the engineering engine:
`chwezi-dev-engine/skills/backend-databases/database-design-engineering/references/data-contracts-and-schema-evolution.md`.

Related references: [data-quality-nfr-catalogue.md](data-quality-nfr-catalogue.md)
for measurable quality NFRs; [data-governance-catalog-lineage-requirements.md](data-governance-catalog-lineage-requirements.md)
for ownership, classification, catalog, and lineage requirements;
[fit-criteria-oracles.md](../../../../references/fit-criteria-oracles.md) for the fit-criterion record.

## Inputs and Stop Conditions

| Input | Source | Missing-input behaviour |
| --- | --- | --- |
| Entity catalog and grain for each shared dataset | This skill's Steps 2 to 4 | Stop; a data interface without grain cannot be specified. |
| Named consumers and the decision each makes with the data | `_context/stakeholders.md`, `_context/features.md` | Flag `[CONTEXT-GAP: consumer for <dataset>]`; do not invent consumers. |
| Freshness, completeness, and availability needs per consumer | Elicitation log, business rules | Flag `[CONTEXT-GAP]`; do not insert a default threshold. |
| Personal-data and confidentiality classification | Data protection officer, `_context/quality-standards.md` | Flag `[DPPA-FAIL: no consent mechanism]` or `[CONTEXT-GAP]` as applicable. |
| Retention obligations | Legal or records schedule, domain regulations | Flag `[CONTEXT-GAP: retention for <dataset>]`. |

## Data Dictionary Template

The data dictionary is the field-level specification the SRS baselines. The
glossary defines business concepts; the dictionary defines each field that
carries them. One row per attribute per shared dataset.

| Column | Content rule |
| --- | --- |
| `DD-ID` | Stable identifier, for example `DD-REPAY-004`. |
| Dataset and grain | Dataset name and one sentence stating what one record represents. |
| Business name | Term from `_context/glossary.md`; `[GLOSSARY-GAP]` if absent. |
| Definition | What the value means, including inclusions and exclusions. |
| Logical type and unit | Text, integer, decimal, date-time, enumeration, identifier; unit or currency; time zone for date-times. No physical column types. |
| Allowed values or pattern | Enumeration members, range, or format reference with its authority. |
| Required | Yes or no, and the condition when conditional. |
| Identifier role | Business key, foreign reference, or none. |
| Classification | Confidentiality level and sensitivity (non-personal, personal, special personal). |
| Quality rule | `DQ-*` identifier from the data quality NFR catalogue. |
| Source of record | The system or actor that creates the value. |
| Retention | Period and the obligation that sets it. |
| Owner and steward | Roles, not personal names, unless the client supplies them. |
| Trace links | `BR-*`, `FR-*`, `ENT-*`, `TC-*`. |

Rules:

- A derived field states its derivation in business terms, for example "Days past
  due = reporting date minus the earliest unpaid instalment due date".
- Codes reference an authority and a version: an ISO code list, a regulator's
  published list, or a client-controlled reference table named in the SRS.
- Personal-data fields state the lawful basis reference and the erasure or
  anonymisation outcome required at end of retention.

## Data Contract Requirements Template

Write one Data Interface Requirement (`DIR-*`) block for every dataset shared
across a team or system boundary. Each block is a requirement set, not a design.

| Clause | Requirement pattern | Verification |
| --- | --- | --- |
| Purpose | The `<dataset>` interface shall provide `<grain>` to `<consumers>` for `<decision>`. | Inspection against the stakeholder register |
| Ownership | The `<producing role>` shall own the interface and shall be the first responder when any clause in this block is breached. | Inspection of the RACI and on-call record |
| Structure | The interface shall conform to data dictionary entries `<DD-IDs>`. | Automated schema comparison |
| Quality | The interface shall meet `<DQ-IDs>`. | Automated checks per the NFR catalogue |
| Service levels | The interface shall meet `<NFR-IDs>` for latency, freshness, completeness, and availability. | Monitoring report over the stated window |
| Change control | A change that removes, renames, retypes, or redefines a field, changes grain, or loosens a service level shall be announced to every registered consumer at least `<N>` business days before release, and the prior version shall remain available for at least `<M>` business days after release. | Change record, notification log, and parallel-run evidence |
| Deprecation | A deprecated interface version shall be removed only after lineage shows zero reads for `<period>`. | Lineage query result attached to the removal approval |
| Governance | Every field shall carry a classification, and every personal-data field shall carry an erasure outcome, before the interface is released. | Automated metadata completeness check |
| Discoverability | The interface, its owner, and its current version shall be discoverable in the organisation's data catalog within `<N>` hours of release. | Catalog query |

`<N>`, `<M>`, and `<period>` come from the consumers' tolerance and the release
calendar in `_context/`. If the context does not supply them, leave the
placeholder and raise `[CONTEXT-GAP]`; do not choose a number on the client's behalf.

## Worked Example: Repayment Feed for a Savings and Credit Cooperative Platform

Context (illustrative): a lending platform serving savings and credit
cooperatives publishes repayments to three consumers: the credit committee's
portfolio-at-risk report, a credit-scoring model, and month-end reconciliation.

**DIR-REPAY-01 Purpose.** The Loan Repayment interface shall provide one record
per repayment credited to a member loan to the Credit Committee Report, the
Credit Scoring Service, and the Finance Reconciliation process.

**DIR-REPAY-05 Service levels.** The Loan Repayment interface shall make 95% of
repayments settled through MTN MoMo or Airtel Money available to consumers
within 15 minutes of provider settlement, measured weekly from provider
settlement time to interface publish time.

- Fit criterion: weekly monitoring report shows the 95th percentile of
  (publish time minus settlement time) at or below 15 minutes.
- Boundary case: a week at exactly 15 minutes passes.
- Exception case: branch cash receipts are excluded and are governed by
  **DIR-REPAY-06** (4-hour threshold) because branches may operate offline.

**DIR-REPAY-07 Change control.** A breaking change to the Loan Repayment
interface shall be announced to every registered consumer at least 20 business
days before release, and the prior version shall remain available for at least
one month-end close after release.

The thresholds above are the example's stakeholder decisions, not defaults for
other projects.

## Acceptance Checklist

- [ ] Every dataset crossing a team or system boundary has a `DIR-*` block.
- [ ] Every `DIR-*` names its consumers and the decision each makes.
- [ ] Every field in scope has a data dictionary row with classification and quality rule.
- [ ] Every service level has a metric, window, measurement points, threshold, and owner.
- [ ] Change control states notice period and parallel-availability period.
- [ ] No implementation terms (table names, column types, tools) appear in requirement text.

## Failure Modes

- Consumers write the contract and producers never accept it. Fix: the `DIR-*`
  names the producing role as owner and requires its sign-off at baseline.
- "The data shall be accurate and up to date." Fix: replace with `DQ-*` and
  service-level NFRs that carry metric, window, and threshold.
- Contract clauses copied into every dataset regardless of use. Fix: derive each
  threshold from a named consumer's need.
- Breaking-change policy missing, so a field rename ships silently. Fix: include
  the change-control clause in every `DIR-*`.

## Evidence/currentness

Access date: 2026-09-24. The clauses map onto the Open Data Contract Standard
(ODCS) v3.2.0 (released 2026-09-08; bitol-io/open-data-contract-standard), so an
engineering team can implement them without translation. The standard is an
implementation format; the SRS remains format-neutral. Uganda-specific data
protection obligations are maintained in `domains/uganda/references/regulations.md`.

Sources: Jones (2023) *Driving Data Quality with Data Contracts*; Bitol project,
ODCS v3.2.0 (2026); ISO/IEC/IEEE 29148:2018.

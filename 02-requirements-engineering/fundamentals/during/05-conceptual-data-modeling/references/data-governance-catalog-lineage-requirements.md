# Data Governance, Catalog, and Lineage Requirements

Parent skill: [05-conceptual-data-modeling](../SKILL.md).

Load when the SRS must specify who owns and decides about data, how data is
classified, how people and AI features find and understand it, and how its
movement is traced for impact analysis, audits, and erasure. Use alongside
[mdm-requirements.md](mdm-requirements.md) (golden records and stewardship for
master data) and [data-contract-and-dictionary-requirements.md](data-contract-and-dictionary-requirements.md)
(interface guarantees). Engineering design of the catalog and lineage belongs
to `chwezi-dev-engine/skills/backend-databases/database-design-engineering/references/metadata-catalog-and-lineage-design.md`.

## Inputs and Stop Conditions

| Input | Source | Missing-input behaviour |
| --- | --- | --- |
| Organisational capability or process map | Client enterprise architecture or quality management system | Use the feature list as a provisional map and flag `[CONTEXT-GAP: capability map]`. |
| Classification policy (confidentiality levels) | Client security policy | Flag `[CONTEXT-GAP]`; do not invent level names. |
| Personal-data definitions and special categories | Applicable law via the domain pack | Stop the sensitivity requirements until the jurisdiction is confirmed. |
| Retention schedule | Legal or records owner | Flag `[CONTEXT-GAP: retention]`. |
| Named decision owners for data | `_context/stakeholders.md` | Use roles, flag `[CONTEXT-GAP: owner for <domain>]`. |

## Governance Operating Model Requirements

Governance is federated: a central council sets policy and standards; producing
teams make local decisions within them and are supported by tooling. Specify
roles and decision rights, not committees for their own sake.

| ID pattern | Requirement pattern | Verification |
| --- | --- | --- |
| `GOV-01` | Each data domain shall have one accountable domain owner and at least one steward, recorded in the data catalog. | Catalog query: domains without owner = 0 |
| `GOV-02` | Each shared dataset shall have an owner in the producing team, who approves its interface changes. | Inspection of the approval record for each release |
| `GOV-03` | A data governance council with representation from each producing and consuming area, legal or privacy, and security shall approve classification levels, retention rules, and access policy. | Council terms of reference and minutes |
| `GOV-04` | Classification of a new field shall be decided by its producing team using the approved policy, without waiting for central review, and shall be sampled by the privacy role at least `<frequency>`. | Sample review log |
| `GOV-05` | Access to data classified `<level>` or above shall be granted by rule derived from the classification, and each grant shall carry an expiry date. | Access register inspection |

## Classification Requirements

Specify three independent axes. A single combined label produces wrong access
and handling decisions.

| Axis | Requirement | Decided by |
| --- | --- | --- |
| Content | Every asset shall carry a content code identifying its capability or process and subject. | Domain owner |
| Confidentiality | Every asset and field shall carry one of the client's approved confidentiality levels. | Security owner |
| Sensitivity | Every field shall be marked non-personal, personal, or special personal as defined by the applicable law. | Data protection officer |

For Uganda-scoped systems, the sensitivity axis uses the definitions of the Data
Protection and Privacy Act, 2019, including special personal data (section 9),
and triggers the tags `[DPPA-FAIL: ...]` and `[DPIA-REQUIRED: ...]` defined in the
root protocol. Detailed obligations live in `domains/uganda/references/regulations.md`.

## Catalog Requirements

State what the catalog must let each user group achieve, with measurable fit criteria.

| ID pattern | Requirement pattern | Fit criterion |
| --- | --- | --- |
| `CAT-01` | The catalog shall register every dataset in scope for `<domains>`, exposing metadata only and no data values. | Registered in-scope assets divided by the in-scope inventory is at least `<target>`% at each quarterly review |
| `CAT-02` | Each registered asset shall carry an owner, a description stating primary and secondary use, at least one approved glossary term, and all three classifications. | Curated assets divided by registered assets is at least `<target>`% |
| `CAT-03` | A user new to a domain shall locate the authoritative dataset for a scripted business question and identify its owner within `<N>` minutes. | Moderated test with at least `<n>` participants; `<target>`% succeed |
| `CAT-04` | Glossary terms shall follow a draft, review, approved, replaced or deleted lifecycle, and replaced or deleted terms shall remain searchable. | Inspection of term history |
| `CAT-05` | Harvested field names that disclose personal or confidential information shall be hidden from catalog-wide view until reviewed. | Review queue inspection |
| `CAT-06` | A catalog query shall return all assets of a given confidentiality level within a given capability, to support system decommissioning and audits. | Demonstration against a seeded test set |

## Lineage Requirements

| ID pattern | Requirement pattern | Fit criterion |
| --- | --- | --- |
| `LIN-01` | The system shall record dataset-level lineage for every scheduled and event-driven job that reads or writes an in-scope dataset, captured from job execution and not drawn manually. | Jobs emitting a start and a terminal lineage event, divided by jobs executed, is 100% in a weekly sample |
| `LIN-02` | For tier 1 regulated or financial data, lineage shall be recorded at field level from source to each report or submission. | Trace from three sampled report figures to source fields succeeds |
| `LIN-03` | Before any breaking interface change, the owner shall obtain from lineage the list of consumers read within the last `<period>`. | Change record contains the lineage query result |
| `LIN-04` | For an erasure request, the system shall identify every downstream dataset, model feature store, and search index holding the subject's personal data. | Erasure test on a seeded subject reaches 100% of seeded copies |
| `LIN-05` | Lineage events shall contain no personal data values. | Automated scan of lineage payloads finds 0 personal data values |

## Metadata Requirements for AI Features

When an AI assistant, retrieval-augmented generation feature, text-to-SQL tool,
or agent uses catalog or contract metadata, add these requirements and trace them
to `02-requirements-engineering/15-ai-data-and-knowledge-base-spec`.

| ID pattern | Requirement pattern | Fit criterion |
| --- | --- | --- |
| `AIM-01` | The AI feature shall retrieve only metadata and documents the requesting user is authorised to see, applying classification filters before ranking. | Red-team test set: 0 unauthorised items returned |
| `AIM-02` | Each dataset exposed to an AI feature shall carry usage instructions, prohibited uses, and a set of verified question-and-answer pairs approved by its owner. | Inspection; evaluation pass rate on verified pairs is at least `<target>`% |
| `AIM-03` | Each AI answer about organisational data shall cite the asset identifiers and interface versions it used. | Sampled answers with citations divided by sampled answers is 100% |
| `AIM-04` | Deprecated and retired interfaces shall be excluded from default AI retrieval. | Seeded deprecated asset never appears in a scripted test run |
| `AIM-05` | Retrieval logs shall record, for each AI answer, which metadata items were retrieved, for at least `<retention>`. | Log inspection for sampled answers |

## Worked Example (Illustrative)

A district health information system shares facility visit data with a national
reporting platform and an AI assistant that answers programme managers'
questions. **CAT-03** is instantiated as: "A programme officer new to the maternal
health domain shall locate the authoritative antenatal visit dataset and identify
its steward within 5 minutes." **LIN-04** is instantiated for patient records so
that a correction or erasure decision reaches the reporting extract and the
assistant's index. **AIM-01** prevents the assistant from surfacing field names
from restricted HIV programme datasets to users without access. All thresholds
are the example's stakeholder decisions.

## Acceptance Checklist

- [ ] Every domain has an owner and steward requirement; every shared dataset has an owner.
- [ ] Classification is specified on three axes with named deciders.
- [ ] Catalog requirements carry coverage, curation, and findability fit criteria.
- [ ] Lineage requirements cover impact analysis, regulated field-level trace, and erasure reach.
- [ ] AI features using metadata have access-filtering, citation, and deprecation-exclusion requirements.
- [ ] No vendor or tool name appears in requirement text.

## Failure Modes

- "The organisation shall implement a data catalog." Fix: state what users must
  achieve with it and how that is measured.
- Governance specified as a central approval gate for every change. Fix: federated
  decision rights with sampled review.
- Lineage required only for the data warehouse. Fix: require it for every job that
  touches in-scope data, including exports to spreadsheets and AI indexes.
- One classification field. Fix: content, confidentiality, and sensitivity.

## Evidence/currentness

Access date: 2026-09-24.

- Uganda Data Protection and Privacy Act, 2019 (Act 9 of 2019): section 9
  (special personal data), section 18 (retention of records), section 23
  (notification of data security breaches), Part V (rights of data subjects),
  checked against the Laws.Africa/ULII text as at 2019-05-03. A consolidated
  version dated 2023-12-31 is listed by Laws.Africa; its numbering is `NOT_ASSESSED`.
  The Data Protection and Privacy Regulations, 2021 and the Personal Data
  Protection Office as regulator are reported by practitioner sources; the
  pdpo.go.ug pages did not render for automated review, so direct confirmation is `NOT_ASSESSED`.
- ODCS v3.2.0 `context` block (instructions, constraints, verified statements)
  underpins `AIM-02`; checked at bitol-io.github.io/open-data-contract-standard/latest/context.
- OpenLineage event model (start plus exactly one terminal event per run)
  underpins the `LIN-01` fit criterion; spec schema 2-0-2, release 1.53.0 (2026-09-01).
- DAMA-DMBOK 3.0 is unpublished and in development (dama.org); do not cite it as a standard.

Sources: Olesen-Bagneux (2023) *The Enterprise Data Catalog*; Olesen-Bagneux
(n.d., 2nd ed. early release) *The Enterprise Data Catalog*; Jones (2023)
*Driving Data Quality with Data Contracts*; Uganda Data Protection and Privacy Act, 2019.

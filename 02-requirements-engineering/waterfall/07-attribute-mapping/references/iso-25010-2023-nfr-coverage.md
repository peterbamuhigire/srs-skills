# ISO/IEC 25010:2023 NFR Coverage Map

Parent skill: [07-attribute-mapping](../SKILL.md). Load it when writing SRS
Sections 3.3 to 3.6, when `_context/quality_standards.md` still uses the
2011 vocabulary (usability, portability, maturity), or when a reviewer asks
whether every relevant quality characteristic was considered. It keeps the
existing IEEE 830-style section layout used by `scripts/build-doc.sh` and
`08-semantic-auditing`; only the coverage and vocabulary change.

## 1. Coverage procedure

1. For each of the nine characteristics below, decide Relevant, Not relevant
   (with a one-line reason) or `[CONTEXT-GAP]`. Record the decision in the
   attribute register; silence is not a decision.
2. For each relevant subcharacteristic, write at least one requirement in the
   section shown, using a quality-attribute scenario: source, stimulus,
   environment, artefact, response, response measure.
3. Give every measure a unit, threshold, load or context condition,
   measurement method (ISO/IEC 25023 measure where one fits) and owner.
4. Check the set for contradictions (two thresholds for one metric) before
   running `python -m engine validate`.

## 2. Characteristic-to-section map

| Characteristic (2023) | Subcharacteristics | SRS section | Typical response measure |
|---|---|---|---|
| Functional suitability | Functional completeness, functional correctness, functional appropriateness | 3.2 (verified through FR acceptance criteria) | Percentage of specified tasks completable; calculation accuracy to stated precision |
| Performance efficiency | Time behaviour, resource utilization, capacity | 3.3 | P95 latency under named load; throughput; maximum concurrent users or records |
| Compatibility | Co-existence, interoperability | 3.1 interfaces; residual items in 3.6 | Successful exchange rate with named external systems and versions |
| Interaction capability (formerly usability) | Appropriateness recognizability, learnability, operability, user error protection, user engagement, inclusivity, user assistance, self-descriptiveness | 3.1.1 user interfaces; measurable targets in 3.6 | First-task success rate; error recovery rate; WCAG 2.2 AA conformance for web content |
| Reliability | Faultlessness (formerly maturity), availability, fault tolerance, recoverability | 3.5.1 and 3.5.2 | Failure rate per 1,000 transactions; availability % per calendar month; RPO and RTO |
| Security | Confidentiality, integrity, non-repudiation, accountability, authenticity, resistance | 3.5.3 | Access-control test pass rate; audit-trail completeness; time to detect and contain a defined attack |
| Maintainability | Modularity, reusability, analysability, modifiability, testability | 3.5.4 | Mean time to diagnose; change lead time for a defined change class; automated test coverage of critical rules |
| Flexibility (formerly portability) | Adaptability, scalability, installability, replaceability | 3.6 (scalability limits also in 3.3 capacity) | Time to install on a clean target; load growth supported without redesign |
| Safety (new in 2023) | Operational constraint, risk identification, fail safe, hazard warning, safe integration | 3.6, cross-referenced to the risk register | Hazard detected and warned within stated time; safe state reached on defined failures |

Write availability as a sub-requirement of reliability, not as a separate
top-level characteristic. Accessibility is expressed through inclusivity and
user assistance plus the WCAG conformance requirement.

## 3. Quality in use belongs to validation

ISO/IEC 25019:2023 defines quality in use as beneficialness, freedom from
risk and acceptability. State these as outcome targets for critical journeys
in the PRD or validation plan, not as product requirements in Section 3.
Do not cite effectiveness, efficiency and satisfaction as ISO/IEC 25019:2023
characteristics; that set comes from the replaced 2011 model.

## 4. Example (Uganda SACCO core system)

- 3.3: "When 300 tellers post deposits concurrently across 12 branches, the
  system shall confirm each posting within 1.5 s at P95 over the branch WAN."
- 3.5.2: "The member-facing USSD channel shall be available at least 99.5% of
  each calendar month, excluding a maintenance window of Sundays 01:00 to
  04:00 EAT announced 72 hours in advance."
- 3.6 Safety: "When a loan disbursement exceeds the approved amount, the
  system shall block the disbursement and alert the branch manager within
  60 s."

## Quality gate

- All nine characteristics carry a relevance decision.
- No 2011-only terms (usability, portability, maturity, user interface
  aesthetics) remain as characteristic names, except when quoting a
  client's legacy document.
- Every requirement has unit, threshold, condition, method and owner.

## Sources and currentness

Evidence/currentness (accessed 2026-09-24):
- ISO/IEC 25010:2023 (second edition) cancels and replaces the 2011 edition;
  foreword confirms safety added, usability and portability replaced by
  interaction capability and flexibility, maturity and user interface
  aesthetics replaced by faultlessness and user engagement, accessibility
  split into inclusivity and user assistance; subclauses 3.1 to 3.4.4
  confirmed from the ISO preview text. Remaining subcharacteristic names were
  confirmed against secondary summaries (arc42 quality model, Sonar) only;
  primary clause text beyond the preview is `NOT_ASSESSED`.
- ISO/IEC 25019:2023 quality-in-use characteristics as recorded by the
  `01-high-level-design` reference of this engine (ISO OBP).
- WCAG 2.2 is the current W3C Recommendation (w3.org/TR/WCAG22, 12 Dec 2024).
- ISO/IEC 25023 measure applicability to the 2023 model was not re-verified:
  `NOT_ASSESSED`.

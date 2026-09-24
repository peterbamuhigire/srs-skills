# API Interface Requirements and API NFRs

Parent skill: [`04-interface-specification`](../SKILL.md). Load this reference
when Section 3.1 must state requirements for software or communication
interfaces exposed as APIs (HTTP, events, webhooks, streaming, AI-agent tools)
or when API quality attributes (latency, availability, limits, compatibility,
security) must become verifiable SHALL statements.

Boundary: the SRS states WHAT an interface must guarantee and how it will be
verified. The choice of REST vs GraphQL vs gRPC, the envelope, and the
OpenAPI document are design decisions owned by `03-api-specification` and the
engineering catalog (`chwezi-dev-engine`, skill `api-design-first`). Name a
style in the SRS only when it is a genuine constraint (a partner mandates it,
a regulator prescribes it, an existing system fixes it) and cite that source.

## Inputs

| Input | Source | If missing |
| --- | --- | --- |
| External actors and systems, direction of each exchange | `_context/features.md`, context diagram | Stop; record a gap |
| Data concepts exchanged and their classification | Data dictionary, privacy assessment | Block security and retention requirements |
| Latency, throughput, freshness, and availability targets | `_context/quality_standards.md`, stakeholders | Record `TBD-owner` with an owner and date; do not invent numbers |
| Partner or regulator interface mandates | Contracts, regulations | State "none known" explicitly |
| Consumer types (browser, mobile on constrained network, partner server, AI agent, analyst) | Stakeholder analysis | Mark consumer-specific requirements `NOT_ASSESSED` |

## Procedure

1. Enumerate interfaces as `IF-<nn>`: provider, consumer, direction, trigger,
   data concept, classification.
2. For each interface write requirements in the categories below. Every
   requirement has an ID, a SHALL statement, a measurable threshold or
   observable behaviour, a verification method (Test, Demonstration,
   Inspection, Analysis), and a source.
3. Trace each requirement to a business need or constraint and forward to a
   test case ID placeholder.
4. Remove any requirement that prescribes internal implementation without a
   stated constraint; move it to design notes.

## Requirement categories and verifiable patterns

| Category | Pattern (fill the brackets) | Verification |
| --- | --- | --- |
| Contract | The system SHALL publish a machine-readable contract for IF-[nn] in [OpenAPI 3.1+/AsyncAPI 3.x/protobuf] and SHALL reject requests that do not conform to it with an error identifying the non-conforming field. | Test: contract-conformance suite; send a request with an unknown field |
| Error semantics | IF-[nn] SHALL return errors in a single documented machine-readable format (RFC 9457 problem details for HTTP interfaces) with a stable error type identifier per error condition. | Inspection of catalogue; Test: each documented error condition |
| Latency | IF-[nn] [operation] SHALL respond within [p95 X ms] and [p99 Y ms] at [N requests/second] measured at the service boundary over [window]. | Test: load test report with percentile table |
| Availability | IF-[nn] SHALL be available [99.x percent] per calendar month excluding announced maintenance of at most [H] hours, measured by [external probe]. | Analysis of monitoring data |
| Freshness | Data served by IF-[nn] SHALL reflect source changes within [T minutes]; each response SHALL state the as-of time. | Test: change source, poll, measure |
| Limits | IF-[nn] SHALL enforce [R requests per minute per client] and [B KB maximum request body] and SHALL signal limit breaches with HTTP 429 or 413 and a retry hint. | Test: exceed each limit |
| Idempotency | Operations of IF-[nn] that create financial, stock, or notification side effects SHALL produce exactly one effect when the same request is retried with the same idempotency key within [24 h]. | Test: duplicate submission under simulated network loss |
| Compatibility | Changes to IF-[nn] SHALL NOT remove or change the meaning of published fields within a major version; retiring a version SHALL be announced at least [D days] in advance with Deprecation and Sunset signals. | Inspection of change log; Test: contract diff in CI |
| Authorisation | IF-[nn] SHALL return a record only to callers entitled to that record's [tenant/owner]; a request for another tenant's record SHALL be indistinguishable from a request for a non-existent record. | Test: cross-tenant ID substitution |
| Security baseline | IF-[nn] SHALL be assessed against the OWASP API Security Top 10 (2023) before release, with each risk recorded as passed with evidence, not applicable with reason, or not assessed. | Inspection of assessment record |
| Delivery (events/webhooks) | Events on IF-[nn] SHALL be delivered at least once, signed, carry a unique event ID, and be retried for at least [H hours]; consumers SHALL be able to request redelivery for [D days]. | Test: receiver offline for [H] hours |
| AI-agent consumers | Operations of IF-[nn] exposed to AI agents SHALL declare input and output schemas, SHALL separate read from write operations, and irreversible or spending operations SHALL require a human approval recorded in the audit log before execution. | Inspection; Test: agent attempt without approval is refused |
| Data consumers | IF-[nn] SHALL provide a bulk export of [dataset] refreshed [daily] with a data dictionary whose field definitions match the API. | Inspection; Test: sample reconciliation |

## Localised worked example (Uganda)

IF-04: School management system to mobile-money aggregator.

- REQ-IF-04-01: The system SHALL submit each fee collection request to the
  aggregator with a unique idempotency key and SHALL record exactly one
  receipt per successful payment when the same request is retried up to
  3 times within 24 hours. Verification: Test (simulated timeout after
  aggregator debit). Source: bursar interview, 2026-09-10 (example).
- REQ-IF-04-02: The system SHALL accept payment-result callbacks only when
  the callback signature verifies and the callback timestamp is within
  5 minutes of receipt; rejected callbacks SHALL be logged with reason.
  Verification: Test (tampered body, stale timestamp).
- REQ-IF-04-03: Amounts on IF-04 SHALL be exchanged in UGX as whole numbers
  (ISO 4217 minor unit 0). Verification: Inspection of contract; Test with a
  fractional amount.

## Premium vs generic output

| Generic output | Specification-grade output |
| --- | --- |
| "The API shall be fast and secure." | p95/p99 at a stated load, window, and measuring point; OWASP API Top 10 assessment record |
| "The system shall use REST." with no source | Style left to design unless a cited constraint mandates it |
| "The API shall handle errors gracefully." | One documented error format with a stable type per condition and a test per condition |
| Numbers invented to fill the template | `TBD-owner` with a named owner and due date |

## Quality gate

- [ ] Every IF has contract, error, limits, authorisation, and compatibility requirements, or a recorded reason for omission.
- [ ] Every threshold has a source; none invented.
- [ ] Every requirement has a verification method and a traceable test placeholder.
- [ ] No implementation choice stated without a cited constraint.

## Evidence and currentness

Accessed 2026-09-24: OWASP API Security Top 10 current edition is 2023 (api-security.owasp.org); RFC 9457 (July 2023) obsoletes RFC 7807; RFC 9745 (March 2025) defines the Deprecation header, used with Sunset (RFC 8594); OpenAPI latest patches 3.1.2 and 3.2.1 (spec.openapis.org); AsyncAPI latest 3.1.0; ISO 4217 List One gives UGX minor unit 0. Consumer-specific targets for any given project are `NOT_ASSESSED` until stakeholders supply them.

Sources: Dynowski and Dulak (2025) *Learning API Styles*; Johnson (2025) *Practical JSON Design and Usage*; Day (2024, early release) *Hands-On APIs for AI and Data Science*; IEEE 29148 interface requirement practice as applied in this engine.

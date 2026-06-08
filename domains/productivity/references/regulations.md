# Productivity — Regulations & Compliance Baseline

This is product-design compliance guidance, not legal advice. A local-first productivity application that holds only the *user's own* documents, notes, and research carries a **low regulatory burden** by default: there is no third-party data subject whose rights the vendor is custodian of, no regulated PII baseline, and no mandatory sector certification. The compliance surface appears at exactly one boundary — the moment an optional feature transmits user content or metadata **off-device**. The table-driven baseline below defines what an application MUST be able to satisfy as a configurable capability; products enable the subset applicable to their feature set and the user's jurisdiction.

## When Privacy Law Engages

| State | Regulatory posture |
|---|---|
| Fully local / offline operation | Low burden. The user processes their own data on their own device. No vendor-side data processing, no transfer, no controller/processor relationship is created. |
| Local model only (on-device AI) | Low burden. Inference occurs on-device; no user content leaves the machine. Treated as local operation. |
| Opt-in cloud AI / metadata provider | GDPR and jurisdictional Data Protection Act principles engage for the off-device payload. The vendor and the chosen provider become accountable for that processing under the user's chosen lawful basis. |

The dividing line is **off-device transmission of user content or metadata**, not the mere presence of an AI feature.

## GDPR / Data Protection Act Principles for Off-Device Transmission

When an optional feature sends user content or metadata off-device, the following principles MUST be honoured by design.

| Principle | Control | Verifiability |
|---|---|---|
| Lawful basis (consent) | Off-device transmission MUST be on an explicit, freely given, specific, informed opt-in. Consent is captured per privacy tier and per provider, never bundled into general app acceptance. The default state is no transmission. | A transmission attempt with no recorded matching consent is blocked and logged; the consent record names the tier, provider, and timestamp. |
| Purpose limitation | The consented purpose (for example, metadata lookup, summarisation, semantic indexing) MUST bound what payload is sent and how the response is used. Re-use for a new purpose requires fresh consent. | Each off-device call carries a purpose tag matched against the consent record; a mismatch is refused. |
| Data minimisation | The payload MUST be reduced to the minimum needed for the consented purpose, and the user MUST be shown a preview of the exact payload before it leaves the device. | Payload-preview test asserts the transmitted field set equals the previewed and minimised set. |
| Transparency | The active privacy tier, the destination provider, and what each tier transmits MUST be legible in the UI at the point of action, not buried in a policy document. | A walkthrough confirms tier and destination are shown at the moment of any off-device action. |
| Right to erasure | The user MUST be able to delete AI query history and embeddings derived from their content, and the app MUST surface or invoke the provider's deletion path for any data sent off-device. | Scoped-erasure test confirms removal of local vectors, cached responses, and exposure of the provider deletion mechanism. |
| Data portability | The user MUST be able to export their catalogue, annotations, and metadata in documented open formats sufficient to move to another tool. | Round-trip export/import test confirms no loss of organisation. |
| No training on user data | User content MUST NOT be used to train any model without a separate, distinct, explicit opt-in that is independent of the consent to use the feature. The default MUST be opt-out of training. | Provider configuration asserts the no-training flag by default; enabling training requires a separate recorded consent. |
| Cross-border transfer awareness | Where a chosen provider processes data outside the user's jurisdiction, the app SHOULD surface the processing location so the user can make an informed choice; the app MUST NOT silently route user content across borders. | Provider metadata includes processing region; the region is shown before first use of that provider. |

## Accessibility as a Legal Expectation

Digital accessibility is a legal expectation in many jurisdictions, not merely a quality preference. Conformance to **WCAG 2.2 Level AA** is the baseline target; **EN 301 549** (European accessibility requirements for ICT, which incorporates WCAG) and **Section 508** (United States federal procurement) are the conceptual reference frameworks that most accessibility law maps onto. Productivity applications SHOULD treat WCAG 2.2 AA conformance as a release gate (see `nfr-defaults.md` NFR-PROD-007 and NFR-PROD-008) so the product remains usable by keyboard-only and screen-reader users and procurable in regulated contexts.

## Privacy Impact Screening

Before shipping any feature that transmits user content or metadata off-device, the team SHOULD run a Data Protection Impact Assessment screening covering: the data categories in the payload, the purpose, the lawful basis, the chosen provider's processing location and retention, the user's erasure path, and the residual risk. A full DPIA is warranted where the processing is systematic, large-scale, or involves content the user is likely to consider sensitive. This screening is a design artifact, not a certification, and replaces no jurisdiction-specific legal review.

## What This Domain Does NOT Carry by Default

- No regulated third-party PII custody — the data subject is the user themselves.
- No sector certification baseline (no HIPAA, PCI-DSS, SOX equivalence) unless a specific product feature introduces regulated data, in which case the relevant sector domain applies in addition.
- No breach-notification custodial obligation for local-only operation, because the vendor processes no user data; obligations arise only for data the vendor or its chosen provider actually processes off-device.

## Standards References

- GDPR (Regulation (EU) 2016/679) and jurisdictional Data Protection Acts
- WCAG 2.2 Level AA (W3C)
- EN 301 549 (ICT accessibility, conceptual)
- Section 508 of the Rehabilitation Act (conceptual)
- ISO/IEC 25010:2023 (systems and software quality model)
- ISO/IEC 27001 (information security management, used as local-hygiene reference)
- IEEE 830, IEEE 1012, IEEE 1233, IEEE 610.12, ASTM E1340

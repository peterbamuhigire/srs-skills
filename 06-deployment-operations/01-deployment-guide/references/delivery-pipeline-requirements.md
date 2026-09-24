# Delivery Pipeline Requirements

Load this when a Deployment Guide, SRS non-functional section, or go-live
readiness pack must state verifiable requirements for how releases are built,
promoted, secured, rolled back, and measured. It states WHAT must be true and
how an auditor checks it. HOW to build the pipeline belongs to the engineering
engine (`chwezi-dev-engine`: `cicd-pipelines`, `deployment-release-engineering`,
`infrastructure-as-code`).

## 1. Requirement-writing rules

- Each requirement uses "shall", names one measurable property, and carries a verification method (Inspection, Demonstration, Test, Analysis) and an evidence artefact.
- Thresholds come from the client's risk decision, a measured baseline, or a contract; never from "industry standard". Where no basis exists, write `[THRESHOLD: owner to set]` and list it in the gap register.
- Do not name a CI product, cloud, or tool unless the client has contractually fixed it. Say "the build platform", "the secret store".
- Separate deployment (artifact reaches an environment) from release (users see behaviour). Requirements for each are distinct.

## 2. Requirement catalogue (adapt, do not paste)

Identifiers are placeholders; renumber to the project scheme.

| ID | Requirement pattern | Verification | Evidence |
|---|---|---|---|
| DP-01 Artifact identity | Every production deployment shall reference the release artifact by cryptographic digest, and the digest deployed to production shall equal the digest that passed acceptance testing. | Inspection of three consecutive deployment records | Deployment records with digests and test-run links |
| DP-02 Build origin | Release artifacts shall be built only on the hosted build platform from a commit on a protected branch; artifacts built elsewhere shall be rejected by the production deploy step. | Demonstration: attempt to deploy a locally built artifact | Rejection log |
| DP-03 Provenance | Each release artifact shall carry signed build provenance meeting SLSA Build Level [2 or 3], verified by the deploy step before deployment. | Test on a tampered artifact | Verification output; SLSA level named in release plan |
| DP-04 Credentials | The pipeline shall hold no long-lived cloud credentials; production access shall use credentials that expire within [THRESHOLD] minutes and are scoped to one environment. | Inspection of secret store and identity trust policies | Secret inventory; trust policy export |
| DP-05 Separation of duty | A production deployment shall require approval by a person other than its requester. | Demonstration | Approval audit log |
| DP-06 Pipeline change control | Changes to pipeline definitions shall require review by a designated platform owner. | Inspection of repository rules | Ruleset / code-owner configuration |
| DP-07 Rollout strategy | For each release class, the Deployment Guide shall name the core deployment strategy, any exposure limits (canary, toggle, promotion), and the reason. | Inspection | Release plan section |
| DP-08 Abort criteria | Each production rollout shall define numeric abort thresholds on error rate and latency and an observation window of at least [THRESHOLD] minutes. | Inspection; drill | Release plan; drill record |
| DP-09 Reversal time | The system shall be restorable to the previous release within [THRESHOLD] minutes of an abort decision, for releases classified reversible. | Test in staging each quarter | Timed rollback drill record |
| DP-10 Irreversible changes | Releases containing contract-phase schema changes or external side effects shall be classified forward-fix-only and shall include a compensating-action procedure approved before release. | Inspection | Migration classification register |
| DP-11 Infrastructure changes | Infrastructure changes shall be applied only by the pipeline from a reviewed plan; destroy or replace actions on stateful resources shall require a named recovery plan. | Inspection of apply logs vs reviewed plans | Plan and apply records |
| DP-12 Drift | Deviation between declared and actual infrastructure shall be detected within [THRESHOLD] hours and assigned to an owner. | Demonstration: introduce a controlled drift in staging | Drift ticket |
| DP-13 Delivery measurement | The delivery system shall report, per service and per [window], deployment frequency, change lead time, change fail rate, failed deployment recovery time, and deployment rework rate as defined by DORA. | Analysis of the metrics report against raw deployment records | Metrics report; definitions sheet |
| DP-14 Release markers | Every production deployment shall emit a version marker visible in logs, metrics, and traces within [THRESHOLD] minutes. | Demonstration | Dashboard screenshot with marker |

## 3. DORA definitions to cite (current)

As published in the DORA metrics guide (updated 2026-01-05): throughput is
measured by change lead time (commit to production), deployment frequency, and
failed deployment recovery time; instability by change fail rate (deployments
needing immediate intervention) and deployment rework rate (unplanned
deployments caused by a production incident). Failed deployment recovery time
replaced the older generic MTTR. State the counting rules (what counts as a
deployment, a failure, the window) inside the SRS, because the definitions
leave these to the adopter.

## 4. Quality gate for this section

- [ ] Every DP requirement has a verification method and evidence artefact.
- [ ] No threshold is invented; each is sourced or listed as a gap with an owner.
- [ ] Reversible and forward-fix-only release classes are both covered.
- [ ] Requirements are tool-neutral unless the contract fixes the tool.
- [ ] DORA metrics use current names; MTTR is not used as a synonym for failed deployment recovery time.

Senior output reads like an audit protocol: an independent reviewer could
fail the vendor against it. Generic output ("the system shall support CI/CD and
zero-downtime deployments") cannot be failed and is rejected.

Worked example (original): for a Uganda Revenue Authority-integrated invoicing
product, DP-10 classifies the release that changes EFRIS submission payloads as
forward-fix-only because submitted fiscal documents cannot be withdrawn; the
compensating procedure (credit-note flow) is approved by the client's finance
lead before the release date. Tax substance routes to the finance engine.

## Evidence and currentness

Accessed 2026-09-24. DORA metrics guide (dora.dev/guides/dora-metrics/,
updated 2026-01-05); SLSA specification v1.2 Build track
(slsa.dev/spec/v1.2/build-requirements). Freshness class: DORA and SLSA
definitions stable within a year; re-verify each Kaizen cycle.
`NOT_ASSESSED`: whether a given client's regulator mandates specific
retention periods for deployment evidence.

Sources: Brikman (2025) *Fundamentals of DevOps and Software Delivery*; DORA
and SLSA primary documentation.

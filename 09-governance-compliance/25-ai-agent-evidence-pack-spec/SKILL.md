---
name: 25-ai-agent-evidence-pack-spec
description: Use when defining AI-agent compliance evidence items, sources, collection, sampling, integrity, chain of custody, retention, redaction, presentation, and auditor access. Use evidence-pack-builder to assemble a specific pack and control packs to define obligations.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent Evidence Pack Spec Skill

<!-- dual-compat-start -->

## Use When

- Use when defining AI-agent compliance evidence items, sources, collection, sampling, integrity, chain of custody, retention, redaction, presentation, and auditor access. Use evidence-pack-builder to assemble a specific pack and control packs to define obligations.

## Do Not Use When

- Do not use as the incident evidence pack spec — this is the steady-state compliance evidence pack; the incident pack is a superset for SEV3+ events. Cross-link to `06-deployment-operations/17-ai-incident-evidence-pack-spec`.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md (where applicable), AI_Agent_HIPAA_Control_Pack.md (where applicable), AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Architecture_Spec.md, AI_Agent_Runbook.md, AI Incident Evidence Pack Spec, parent evidence-pack builder skill. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Provenance, integrity, period, or control mapping is absent | Quarantine the item and record the gap | Misleading or tampered evidence |
| Evidence meets scope, integrity, and traceability checks | Index it for the named consumer | Unreviewable evidence dumps |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI Agent Evidence Pack Spec | Accountable reviewer, control owner, auditor, or release authority | Every control row in every control pack shall map to one or more evidence items. Every evidence item shall name source system, collector, capture method, frequency, retention, sampling, redaction, presentation. Chain-of-custody shall be tamper-evident. Auditor portal access shall be time-bound, logged, and named-recipient. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent Evidence Pack Spec evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every control row in every control pack shall map to one or more evidence items. Every evidence item shall name source system, collector, capture method, frequency, retention, sampling, redaction, presentation. Chain-of-custody shall be tamper-evident. Auditor portal access shall be time-bound, logged, and named-recipient.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent Evidence Pack Spec from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if provenance, integrity, period, or control mapping is absent, quarantine the item and record the gap. Record the evidence and result in the validation record; this avoids misleading or tampered evidence.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

The evidence pack is the auditor's reading set. The SOC 2 / ISO / HIPAA control packs name what evidence is required; this spec defines **how it is collected, where it lives, how it is sampled, how it is redacted, how it is presented, and how the auditor accesses it**. The software-dev pass owns the collectors; this spec defines the contract.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | SOC 2 / ISO / HIPAA control packs, Policy Pack, Agent Architecture, Runbook, Incident Evidence Pack Spec, parent evidence-pack builder |
| **Output** | `AI_Agent_Evidence_Pack_Spec.md` + Template + Frequency Table |
| **Standards** | AICPA TSP 100; ISO/IEC 27007; ISO/IEC 17021; HHS OCR audit protocol |

## Core Instructions

### Step 1: Evidence items per control class

Enumerate evidence per control class (governance, access, monitoring, change, incident, supplier, privacy, integrity, availability, confidentiality, processing integrity, BAA). Each item carries:

- Artefact name and format.
- Source system (e.g., orchestrator, dispatcher, IAM provider, observability platform).
- Collector (cross-link software-dev pass collector name).
- Capture method (automated push, scheduled job, sign-off-ledger entry).
- Frequency (continuous, daily, weekly, monthly, quarterly, annual, on-event).
- Retention (per evidence-pack retention schedule).
- Sampling (full population, 25 stratified, 5% sample, etc.).
- Redaction class.
- Presentation format (CSV, signed JSON, PDF, screenshot, log export).

### Step 2: Pack layout

```
evidence-pack-<window>/
  manifest.json
  policies/
    agent-action-governance-policy.pdf
    ...
  controls/
    soc2/
      CC1-1.md
      CC6-1/
        access-review-Q1.csv
        access-review-Q2.csv
        ...
    iso27001/
      A-8-15.md
      ...
    hipaa/
      164-312-b.md
      ...
  evidence/
    audit-log-integrity-reports/
    kill-switch-drill-reports/
    approval-events-sample-25.csv
    daily-review-tickets-sample-25.csv
    pr-sample-25.csv
    sub-processor-list.json
    baa-ledger.csv
    dpa-ledger.csv
  incidents/
    SEV1/
    SEV2/
  signed-zip.zip
  signed-zip.zip.sha256
```

### Step 3: Sampling protocol

| Population | Sample |
|-------------|--------|
| Approval events | 25 stratified across features and severity |
| Daily-review tickets | 25 stratified across the window |
| PR changes (planner/catalogue/supervisor) | 25 stratified |
| Access reviews | full population |
| Kill-switch drills | full population |
| Erasure events | full population |
| SEV1 / SEV2 incidents | full population |
| SEV3 incidents | 25 stratified |
| Anomaly tickets | 25 stratified |
| External tool calls (PHI-touching) | 25 per quarter, stratified |

Sampling rationale follows AICPA AT-C 205 and ISO/IEC 17021 sampling guidance. Stratification keys: feature, tier, severity, tenant size, time-of-window quintile.

### Step 4: Chain-of-custody

- Each artefact captured to immutable storage with content hash (SHA-256 default).
- Capture event names: source system, time window, capture operator or job id, hash, storage URI.
- Modifying a captured artefact is impossible by design; corrections create a derived artefact with back-link.
- All captures listed in `manifest.json` with their hashes; the manifest itself is signed at pack close.

### Step 5: Retention

Per the Audit-Log Retention Policy and per the SOC 2 / ISO / HIPAA retention requirements:

| Class | Retention |
|-------|-----------|
| Policy pack versions | 7 years |
| Control packs and SoA versions | 7 years |
| Audit-log samples | per audit-log retention policy |
| Kill-switch drill reports | 7 years |
| Incident packs (SEV1) | 7 years |
| Sign-off ledger entries | 7 years |
| Sub-processor change records | 7 years |
| BAA and DPA addenda | 7 years from termination |
| Auditor portal access logs | 7 years |

HIPAA minimum: 6 years from creation or last effective date. SOC 2: typical 5 years; bias toward 7. ISO: as policy.

### Step 6: Redaction policy

Same redaction classes as the incident evidence pack spec:

- Other tenants' data: redact by default; not overridable.
- User PII fields: redact unless regulator requires unredacted under order.
- Provider-confidential under NDA: redact unless provider authorises.
- Internal pricing: redact for customer view; exec sign-off for unredacted to auditor.

Redaction events appended to the manifest.

### Step 7: Presentation format

- Markdown for narrative artefacts (policies, control narratives, SoA, walkthrough scripts).
- CSV or signed JSON for tabular evidence (access reviews, approval events, tickets, drill reports).
- PDF for signed documents (policies, sign-off ledger, BAAs).
- Screenshots / video for in-product disclosures, drills, demos.
- Signed zip for the bundle as a whole.

### Step 8: Auditor portal access governance

- Access is time-bound (default: audit window + 14 days).
- Named-recipient only; no shared accounts.
- Every access is logged with name, IP, time, artefact viewed.
- Download events recorded with hash of downloaded artefact.
- Portal access revoked on day +1 after final report.

### Step 9: Write the spec

`AI_Agent_Evidence_Pack_Spec.md` sections: 1) Evidence items per control class, 2) Pack layout, 3) Sampling protocol, 4) Chain-of-custody, 5) Retention, 6) Redaction policy, 7) Presentation format, 8) Auditor portal access governance, 9) Cross-refs, 10) Sign-off.

## Standards

- AICPA TSP 100; AICPA AT-C 205
- ISO/IEC 27007 (auditing guidelines)
- ISO/IEC 17021 (certification body process)
- HIPAA §164.316(b) (documentation retention)
- HHS OCR audit protocol

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-attestation-evidence-pack-template.md`, `references/ai-agent-evidence-frequency-table.md`.

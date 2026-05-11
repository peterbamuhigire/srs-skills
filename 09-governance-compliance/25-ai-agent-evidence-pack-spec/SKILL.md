---
name: "ai-agent-evidence-pack-spec"
description: "Generate the AI Agent Evidence Pack Spec: what evidence the auditor expects per control class; evidence-pack file layout; sampling protocol; chain-of-custody; retention; redaction policy; presentation format; auditor portal access governance. Defines the contract the software-dev pass's collectors must satisfy."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features at L1+ and prepares for SOC 2, ISO, HIPAA, or covered-entity audit. Mandatory before the audit window opens and refreshed annually."
  do_not_use_when: "Do not use as the incident evidence pack spec — this is the steady-state compliance evidence pack; the incident pack is a superset for SEV3+ events. Cross-link to `06-deployment-operations/17-ai-incident-evidence-pack-spec`."
  required_inputs: "AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md (where applicable), AI_Agent_HIPAA_Control_Pack.md (where applicable), AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Architecture_Spec.md, AI_Agent_Runbook.md, AI Incident Evidence Pack Spec, parent evidence-pack builder skill."
  workflow: "Enumerate evidence items by control class; define pack layout; define sampling protocol; define chain-of-custody; define retention; define redaction policy; define presentation format; define auditor portal access governance; write the spec."
  quality_standards: "Every control row in every control pack shall map to one or more evidence items. Every evidence item shall name source system, collector, capture method, frequency, retention, sampling, redaction, presentation. Chain-of-custody shall be tamper-evident. Auditor portal access shall be time-bound, logged, and named-recipient."
  anti_patterns: "Do not produce evidence ad hoc per audit; the pack shall be continuous. Do not skip the chain-of-custody manifest. Do not put raw customer data in the auditor portal; redact per the redaction policy. Do not let evidence cadence be 'continuous' without naming the collector."
  outputs: "AI_Agent_Evidence_Pack_Spec.md, AI_Agent_Attestation_Evidence_Pack_Template.md, AI_Agent_Evidence_Frequency_Table.md."
  references: "Use references/ai-agent-attestation-evidence-pack-template.md and references/ai-agent-evidence-frequency-table.md."
---

# AI Agent Evidence Pack Spec Skill

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

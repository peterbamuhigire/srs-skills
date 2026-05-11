---
name: "ai-incident-evidence-pack-spec"
description: "Generate the AI Incident Evidence Pack Spec: what evidence to preserve when an AI incident occurs — trace bundle, prompt + model + tool versions at the time of the incident, retrieval set, eval output at the time of the incident, customer-affected list, action audit log, reproduce script, model-price-table snapshot. Defines chain-of-custody, retention, redaction policy, and the regulator-handover format."
metadata:
  use_when: "Use as the data-preservation contract for every AI incident at SEV3 and above. Mandatory before GA. Evidence preservation is what makes regulator handover possible later."
  do_not_use_when: "Do not use as the general logging spec; this is for incident preservation specifically and assumes the parent logging / tracing system exists."
  required_inputs: "AI_Incident_Severity_Matrix.md, AI_Incident_Response_Runbook.md, AI_Architecture_Spec.md, AI_Hallucination_SLO_Doc.md, AI_Cost_Runbook.md, AI_Model_Card.md, AI_Act_And_Regulatory_Compliance_Doc.md, Multi_Tenancy_Architecture_Spec.md."
  workflow: "Enumerate evidence items, define chain-of-custody, define retention per severity, define redaction policy, define regulator-handover packaging, write the spec."
  quality_standards: "Every evidence item shall name source system, capture method, retention period, and access policy. Every SEV1 evidence pack shall be regulator-handover-ready within 24 h of incident closure. Every evidence pack shall include a reproduce script."
  anti_patterns: "Do not rely on ad-hoc screenshots. Do not preserve raw customer data without tenant-isolation. Do not retain beyond the stated period."
  outputs: "AI_Incident_Evidence_Pack_Spec.md."
  references: "Use references/ai-incident-evidence-pack-spec-template.md."
---

# AI Incident Evidence Pack Spec Skill

## Overview

An AI incident produces a unique evidence surface: the prompt, the model version, the tool calls, the retrieval set, and the eval output at the moment of failure must be preserved together. Without that bundle, the postmortem cannot reach a defensible root cause and the regulator handover cannot be assembled within the EU AI Act Art. 73 or GDPR Art. 33 windows.

This skill produces the spec. The software-dev engine pass owns the implementation (evidence-bundle exporter, reproduce-script generator, price-table snapshotter); this spec is the contract.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Severity Matrix, Response Runbook, AI Architecture, Hallucination SLO, Cost Runbook, Model Card, AI Act doc, Tenancy Spec |
| **Output** | `AI_Incident_Evidence_Pack_Spec.md` |
| **Standards** | EU AI Act Art. 12 (logs); Art. 20 (corrective actions); GDPR Art. 30 (records); ISO/IEC 42001 Clause 9.1 |

## Core Instructions

### Step 1: Evidence items

The pack carries at minimum the following items per incident:

1. **Trace bundle** — every model call, tool call, and gateway decision affected by the incident; full request/response with prompt id, model id, tool id, tenant id; time-bounded.
2. **Prompt + model + tool versions at T** — snapshot of the prompt registry, model gateway routing config, agent tool registry at the incident start time.
3. **Retrieval set** — for RAG incidents, the documents retrieved per affected request; index id and snapshot id.
4. **Eval output at T** — the most recent eval run before the incident; the run that gated the latest release; calibration-set scores.
5. **Customer-affected list** — tenant ids, user ids (subject to data-protection scope), affected request count, autonomous-action count per tenant.
6. **Action audit log** — for agent-action incidents: every tool call that succeeded, every record mutated, every recipient contacted.
7. **Reproduce script** — a deterministic script that re-runs the failing request against the pinned configuration and reproduces the failure (best-effort for non-deterministic models; expected to surface the regression).
8. **Model-price-table snapshot** — provider price list at T (for cost-runaway incidents and for postmortem cost calculation).
9. **Containment-action log** — every containment mode invoked, time, operator id, verification outcome.
10. **Customer comms artefacts** — outgoing emails, status-page snapshots, tenant-notifications.

### Step 2: Chain-of-custody

- Each item is captured to immutable storage (write-once-read-many, or content-addressed with append-only audit log).
- Capture is automatic on incident declaration; the IC may extend the time window during the incident.
- Each capture event names: source system, time window, capture operator (or job id), hash of the captured artefact, storage location.
- Modifying a captured item is impossible by design; redaction creates a derived artefact with a back-link.

### Step 3: Retention per severity

| Severity | Retention | Justification |
|----------|-----------|---------------|
| SEV1 | 7 years | EU AI Act Art. 12 + audit timeline; potential litigation |
| SEV2 | 3 years | postmortem cycle + audit timeline |
| SEV3 | 1 year | learning + trend analysis |
| SEV4 | 90 d | minor noise window |

Override per tenant DPA if longer is contractually required. Adhere to "right to erasure" exceptions (GDPR Art. 17(3)(b), Art. 17(3)(e)) for incident records.

### Step 4: Redaction policy

For external handover (regulator or affected-tenant):

- Other tenants' data redacted by default.
- User-identifying fields redacted unless required by the receiving authority.
- Provider-confidential information (model architecture details under NDA) redacted.
- Redaction log appended to the pack; redacted-vs-unredacted is auditable.

### Step 5: Regulator-handover packaging

For Art. 73 / Art. 33 / state-level / African regulators:

- The pack is exported as a sealed bundle (signed zip or equivalent).
- Index manifest names every artefact, its hash, its capture provenance, and any redactions.
- Cross-reference to the regulator-notification template (`09-governance-compliance/18-ai-regulator-incident-notification-doc`).
- DPO/legal sign-off recorded in the manifest before handover.

### Step 6: Access policy

- Read access in normal operation: AI lead, SRE on-call, security, DPO, legal, exec sponsor — by role.
- Read access for customer-distribution: redacted view only.
- Read access for regulator handover: time-bound, logged, named recipient.

### Step 7: Write the spec

`AI_Incident_Evidence_Pack_Spec.md` sections: 1) Evidence Items, 2) Chain-of-Custody, 3) Retention, 4) Redaction Policy, 5) Regulator-Handover Packaging, 6) Access Policy, 7) Capture Tooling (cross-link to software-dev pass), 8) Cross-Refs.

## Standards

- EU Reg 2024/1689 Art. 12 (record-keeping), Art. 20 (corrective actions)
- EU Reg 2016/679 Art. 30 (records of processing)
- ISO/IEC 42001 Clause 9.1 (monitoring)
- NIST AI RMF MEASURE-3 (record of decisions)

## Relationship to the compliance evidence pack

The incident evidence pack is a **superset** of the compliance evidence pack for the affected control rows during the incident window:

- Trace bundle, action audit log, reproduce script, and price-table snapshot all feed back into the SOC 2 PI1.4, ISO A.8.15/A.8.24, and HIPAA §164.312(b)/(c) evidence rows for the audit window.
- The incident pack chain-of-custody and redaction rules apply unchanged when those artefacts are referenced by the compliance pack.
- The compliance pack manifest cross-references each incident pack by `incident_id` and inherits its hash.

See `09-governance-compliance/25-ai-agent-evidence-pack-spec` for the steady-state pack and the auditor portal contract; this spec governs the per-incident superset.

## Resources

- `logic.prompt`, `README.md`, `references/ai-incident-evidence-pack-spec-template.md`.

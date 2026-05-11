---
name: "saas-dpa-and-privacy-doc-set"
description: "Generate the SaaS DPA + Privacy doc set: Data Processing Addendum (controller-processor terms, SCCs, sub-processor list, audit rights), Records of Processing Activity (ROPA Art.30), retention & destruction schedule, breach-notification procedure, DSAR handling procedure."
metadata:
  use_when: "Use when the SaaS processes personal data on behalf of customers (almost always for B2B SaaS) under GDPR / POPIA / DPPA / CCPA."
  do_not_use_when: "Do not use when no personal data is processed (rare)."
  required_inputs: "Compliance_Docs.md, Multi_Tenancy_Architecture_Spec.md (for regions), sub-processor list, retention obligations, Risk_Assessment.md."
  workflow: "Draft DPA template, draft ROPA, draft retention schedule, draft breach-notification procedure, draft DSAR procedure, attach SCCs, write the index."
  quality_standards: "DPA shall include SCCs (current EU version) for cross-border transfer. ROPA shall list every processing activity. Breach SLA shall be ≤ 72 hours."
  anti_patterns: "Do not write 'we take privacy seriously' without specific obligations. Do not omit cross-border transfer mechanism."
  outputs: "DPA.md, ROPA.md, Retention_Schedule.md, Breach_Notification_Procedure.md, DSAR_Procedure.md, index DPA_And_Privacy_Pack.md."
  references: "references/saas-dpa-and-privacy-doc-templates.md"
---

# SaaS DPA & Privacy Doc Set Skill

## Overview

Generates the document set that GDPR / POPIA / DPPA / CCPA expect a SaaS processor to publish or hold ready: DPA template, ROPA, retention schedule, breach-notification procedure, DSAR procedure.

## Core Instructions

### Step 1: Draft the DPA

Sections: parties; subject matter; duration; nature & purpose; type of personal data; categories of data subjects; obligations of processor (process only on documented instructions; confidentiality; security; sub-processors with notice and consent; assistance with rights requests; assistance with DPIAs; deletion or return at end; audit rights with notice); obligations of controller; international transfers (Standard Contractual Clauses Annex); liability; term & termination.

### Step 2: Draft the ROPA (Art.30 record)

| Processing activity | Purpose | Categories of data subjects | Categories of personal data | Recipients | International transfers | Retention | Security measures |
|--------------------|---------|----------------------------|----------------------------|------------|------------------------|-----------|-------------------|

Every product feature that processes personal data appears as a row.

### Step 3: Retention & destruction schedule

| Data class | Retention | Destruction method | Verification | Owner |
|------------|-----------|--------------------|--------------|-------|
| Account / billing PII | life of contract + 7 y tax | hard delete after retention | verification query + certificate | privacy officer |
| Operational data | per contract | hard delete on offboarding +30 d grace | verification query | privacy officer |
| Telemetry raw | 13 months | rotate-out | retention policy on bus | platform team |
| Logs | 13 months | rotate-out | retention policy on log store | platform team |
| Backups | per backup retention (e.g. 35 d) | encrypted rotate-out + key destruction | backup audit | platform team |

### Step 4: Breach-notification procedure

- Detection sources: monitoring, audit log, customer report, third-party advisory.
- Confirmation: incident commander confirms within 24 h.
- Risk assessment: scope (tenants, data classes, volume), severity.
- Notify supervisory authority: within 72 h of confirmation (GDPR Art.33) with the prescribed content.
- Notify affected data subjects: where high-risk to rights, without undue delay (Art.34).
- Notify customer (controllers): per DPA SLA — recommend within 24 h of confirmation.
- Record-keeping: every breach logged, regardless of notifiability.

### Step 5: DSAR procedure

- Channels: in-product, support email, postal.
- Authentication: verify identity per published procedure.
- Statutory windows: GDPR 30 d (extendable +60); POPIA reasonable time; CCPA 45 d (+45).
- Right of access: machine-readable export.
- Right to erasure: trigger hard-delete via lifecycle runbook.
- Right to portability: standard JSON/CSV export.
- Right to rectification: in-product UI + audit.
- Right to object / restrict: feature-flag approach.

### Step 6: SCCs

Attach EU Standard Contractual Clauses (Module 2 controller-processor, current version) as an Annex to the DPA where cross-border transfer applies. Note alternative frameworks (UK IDTA, Swiss FDPIC, EU-US Data Privacy Framework).

### Step 7: Write the pack

`DPA_And_Privacy_Pack.md` indexes the docs above.

## Standards

- GDPR (Regulation 2016/679) Articles 28, 30, 32, 33, 34, 35, 44.
- POPIA (South Africa) sections 19, 22, 23.
- DPPA 2019 (Uganda) sections on processor obligations, breach notification, DSAR.
- CCPA / CPRA (California).

## Resources

- `logic.prompt`, `README.md`, `references/saas-dpa-and-privacy-doc-templates.md`.

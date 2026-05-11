---
name: "saas-trust-center-document-pack"
description: "Generate a public Trust Center document pack: security overview, compliance attestations, sub-processor list, DPA template availability, status-page commitment, vulnerability-disclosure policy, and customer-data handling summary."
metadata:
  use_when: "Use when a SaaS sells to enterprise buyers, must answer security questionnaires, or wants to publish a buyer-facing trust page."
  do_not_use_when: "Do not use for internal-only tools."
  required_inputs: "Compliance_Docs.md, Data_Isolation_Evidence_Pack.md, Risk_Assessment.md, DPA, sub-processor list."
  workflow: "Inventory attestations, write public-facing security overview, publish sub-processor list, link DPA, publish vulnerability-disclosure policy, write the Trust Center index."
  quality_standards: "Every claim shall be backed by an attestation, an evidence pack, or a documented control. Marketing language is prohibited."
  anti_patterns: "Do not claim certifications you do not hold. Do not list controls without naming the evidence."
  outputs: "Trust_Center_Document_Pack.md plus public-facing markdown pages."
  references: "references/saas-trust-center-document-pack-template.md"
---

# SaaS Trust Center Document Pack Skill

## Overview

Produces the buyer-facing trust document pack. Designed for enterprise procurement, security questionnaires (SIG, CAIQ, SIG Lite), and the public trust-center page that mature SaaS vendors host.

## Core Instructions

### Step 1: Security overview

Public summary covering: encryption at rest, encryption in transit, authentication (SSO, MFA), authorization (RBAC, scoped tokens), tenant isolation summary, vulnerability management, secure-SDLC, third-party penetration testing cadence, incident response approach, data-residency options.

### Step 2: Compliance attestations index

| Attestation | Status | Period | Auditor | Report request |
|-------------|--------|--------|---------|----------------|
| SOC 2 Type II | held / in progress / planned | YYYY-MM to YYYY-MM | | request form URL |
| ISO/IEC 27001 | | | | |
| ISO/IEC 27017 | | | | |
| ISO/IEC 27018 | | | | |
| PCI-DSS | | | | |
| HIPAA BAA | | | | |
| GDPR alignment | | | | |
| CSA STAR | | | | |
| Cyber Essentials | | | | |

### Step 3: Sub-processor list

Public table: name, purpose, region, data-classes processed, certifications. Notification commitment for new sub-processors (typical: 30 days advance notice with right of objection).

### Step 4: DPA & privacy

Link to the published DPA, the privacy policy, the cookie policy, the data-residency options, the breach-notification commitment (typical: within 72 hours of confirmation).

### Step 5: Vulnerability disclosure policy

How to report (security@), safe-harbour scope, response SLA, hall-of-fame or bounty (if applicable).

### Step 6: Status page commitment

Link to the public status page, incident-comms protocol, postmortem-publication commitment.

### Step 7: Customer-data handling summary

What classes of data the product processes, retention defaults, deletion options, export options (GDPR portability), data-residency options, encryption posture per class.

### Step 8: Write the pack

`Trust_Center_Document_Pack.md` indexes the public pages. Generate public-facing markdown for each section under `public/trust/`.

## Standards

- SOC 2 / ISO 27001 / ISO 27017 / ISO 27018
- GDPR, POPIA, DPPA
- CSA CAIQ v4 / SIG Core / SIG Lite

## Resources

- `logic.prompt`, `README.md`, `references/saas-trust-center-document-pack-template.md`.

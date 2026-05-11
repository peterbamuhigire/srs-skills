---
name: "saas-incident-response-and-postmortem"
description: "Generate a SaaS-tuned Incident Response & Postmortem documentation pack: severity matrix that distinguishes tenant-scope vs platform-scope, blast-radius reporting, customer-comms templates per severity, status-page protocol, and the blameless postmortem template."
metadata:
  use_when: "Use for any multi-tenant SaaS that must operate an on-call rotation and communicate incidents to customers."
  do_not_use_when: "Do not use for internal-only tools without customer SLAs."
  required_inputs: "Multi_Tenancy_Architecture_Spec.md, SLO_And_Error_Budget_Doc.md, Runbook.md, pricing & packaging spec."
  workflow: "Define SaaS severity matrix (with tenant-scope dimension), define detection sources, define IR phases, define customer-comms templates per severity, define status-page protocol, define blameless postmortem structure, write the IR_and_Postmortem.md doc."
  quality_standards: "Every severity row shall include tenant-scope dimension. Every severity shall have a customer-comms template. Every postmortem shall be blameless and tracked to action items with owners and dates."
  anti_patterns: "Do not collapse severity to a single dimension. Do not omit blast-radius reporting. Do not allow postmortem action items without owners."
  outputs: "IR_and_Postmortem.md plus customer-comms templates."
  references: "references/saas-incident-response-and-postmortem-template.md"
---

# SaaS Incident Response & Postmortem Skill

## Overview

Produces the SaaS-tuned Incident Response & Postmortem doc pack. The generic runbook covers severity tiers and escalation, but SaaS adds a critical dimension: **tenant scope**. A SEV1 affecting one Enterprise tenant is operationally different from a SEV1 affecting all tenants. This skill captures that.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Multi_Tenancy_Architecture_Spec.md, SLO_And_Error_Budget_Doc.md, Runbook.md, pricing spec |
| **Output** | `IR_and_Postmortem.md` + `templates/customer-comms-<sev>.md` |
| **Standard** | Google SRE; FCC / NIST incident-comms norms |

## Core Instructions

### Step 1: Define the two-dimensional severity matrix

| Severity × Scope | Single tenant | Tenant cohort | Platform-wide |
|------------------|---------------|---------------|---------------|
| SEV1 | Tier-Enterprise customer down or data-impacting incident | Pod or region down | All-tenant outage / data corruption |
| SEV2 | Tier-Gold customer down | Multiple Gold tenants degraded | Significant feature degraded for most |
| SEV3 | Single Silver/Bronze customer down | Cohort degraded | Minor feature degraded for some |
| SEV4 | Cosmetic | Cosmetic | Cosmetic |

Override the matrix per project but the two dimensions are mandatory.

### Step 2: Define detection sources

Monitoring alerts (linked to SLO burn-rate), customer support tickets, status-page subscriber reports, partner/SDK error reports, security telemetry.

### Step 3: Define IR phases

Detect → Triage → Contain → Mitigate → Resolve → Postmortem. State the time targets per severity (SEV1: triage in 5 min, customer-comms in 15 min; SEV2: triage in 15 min, comms in 30 min).

### Step 4: Customer-comms templates per severity

For SEV1 and SEV2 produce:

- Initial acknowledgement (within X min of detection).
- Status updates (cadence: every 30 min for SEV1, every hour for SEV2).
- Resolution announcement.
- Postmortem publication (within 5 business days for SEV1, 10 for SEV2).

Each template carries: subject line, in-app banner copy, status-page entry, dedicated email to affected tenants. Include placeholder for tenant scope (`{affected_tenants}` or "all tenants in the EU region").

### Step 5: Status-page protocol

Define when to post (any SEV1, any SEV2 lasting > 15 min, any maintenance). Define who can post (on-call + comms-on-call). Define the components mapped (per-region per-service). Define subscriber notification.

### Step 6: Blameless postmortem template

Sections: timeline, impact (tenants affected, duration, error-budget burn, financial impact estimate, support load), root cause (5 whys), what went well, what went poorly, contributing factors, action items (with owner, severity, due date, status), lessons learned.

### Step 7: Action-item tracking

State the system where action items are tracked (ticketing tool) and the review cadence (weekly action-item burn-down meeting). Postmortem closure is independent of incident closure.

### Step 8: Write IR_and_Postmortem.md

Sections: 1) Severity Matrix, 2) Detection Sources, 3) IR Phases & Time Targets, 4) Customer-Comms Protocol, 5) Status-Page Protocol, 6) Blameless Postmortem Template, 7) Action-Item Tracking, 8) Tenant-Impact Reporting, 9) Cross-Refs (runbook, SLO doc, lifecycle runbook).

## Standards

- Google SRE — blameless postmortems.
- NIST SP 800-61 — incident handling guide (adapted for SaaS-customer reporting).

## Resources

- `logic.prompt`, `README.md`, `references/saas-incident-response-and-postmortem-template.md`.

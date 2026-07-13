---
name: 12-saas-trust-center-document-pack
description: Use when preparing verified customer-facing security, privacy, availability, subprocessor, and compliance material for a SaaS trust centre. Use evidence-pack-builder for internal proof and DPA/privacy-doc-set for contractual privacy documents.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Trust Center Document Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when preparing verified customer-facing security, privacy, availability, subprocessor, and compliance material for a SaaS trust centre. Use evidence-pack-builder for internal proof and DPA/privacy-doc-set for contractual privacy documents.

## Do Not Use When

- Do not use for internal-only tools.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: Compliance_Docs.md, Data_Isolation_Evidence_Pack.md, Risk_Assessment.md, DPA, sub-processor list. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A required source, owner, obligation, or acceptance condition is missing | Stop the affected claim and record the gap | Unsupported governance artefact |
| Evidence satisfies the declared acceptance condition | Record the decision and hand off to the named consumer | Ambiguous approval or release |

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
| SaaS Trust Center Document Pack | Accountable reviewer, control owner, auditor, or release authority | Every claim shall be backed by an attestation, an evidence pack, or a documented control. Marketing language is prohibited. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Trust Center Document Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every claim shall be backed by an attestation, an evidence pack, or a documented control. Marketing language is prohibited.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Trust Center Document Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a required source, owner, obligation, or acceptance condition is missing, stop the affected claim and record the gap. Record the evidence and result in the validation record; this avoids unsupported governance artefact.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

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

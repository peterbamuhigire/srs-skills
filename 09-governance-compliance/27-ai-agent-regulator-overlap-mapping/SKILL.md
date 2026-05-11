---
name: "ai-agent-regulator-overlap-mapping"
description: "Generate the AI Agent Regulator Overlap Mapping: the multi-regime crosswalk that shows how a single piece of agent-compliance evidence satisfies multiple frameworks at once — SOC 2 × ISO 27001 × HIPAA × EU AI Act × NIST AI RMF × Kenya DPA × Nigeria NDP Act × South Africa POPIA × Uganda DPPA × Rwanda DP Law. Enables 'one piece of evidence, multiple regimes' reuse and surfaces where regimes diverge so distinct evidence is needed."
metadata:
  use_when: "Use whenever an agentic SaaS operates across two or more jurisdictions or framework scopes. Mandatory before multi-region launch. Refreshed annually and when any framework is updated."
  do_not_use_when: "Do not use as the sole reference for any one regime — use it alongside the per-regime control pack. Do not treat the overlap as automatic; gaps shall be identified explicitly per row."
  required_inputs: "AI_Agent_SOC2_Control_Pack.md, AI_Agent_ISO27001_Control_Pack.md, AI_Agent_HIPAA_Control_Pack.md, AI_Act_And_Regulatory_Compliance_Doc.md, NIST AI RMF mapping, AI_Data_Flow_And_DPIA.md, BAA/DPA addendum templates, regional regulator guidance documents (KE ODPC AI guidance 2024; NG NDPC advisory 2024; ZA POPIA s.71; UG DPPA 2019; RW DP Law 2021)."
  workflow: "Build the regime list; build the canonical control area list; for each control area, map to each regime's specific clause; identify shared evidence and divergent evidence; produce the overlap matrix; write the mapping doc."
  quality_standards: "Every control area shall map to every applicable regime. Shared-evidence cells shall name the evidence artefact. Divergent-evidence cells shall name the additional requirement. EU AI Act high-risk and prohibited classifications shall be cross-linked. Updates triggered by framework change shall be timestamped."
  anti_patterns: "Do not collapse regimes into 'equivalent' without per-clause verification. Do not assume EU AI Act and GDPR have the same scope for agent processing. Do not skip African DPA divergence — they differ materially on notification timelines and residency expectations."
  outputs: "AI_Agent_Regulator_Overlap_Mapping.md, AI_Agent_Regulator_Overlap_Matrix.md."
  references: "Use references/ai-agent-regulator-overlap-matrix.md."
---

# AI Agent Regulator Overlap Mapping Skill

## Overview

A single audit-log retention configuration can satisfy SOC 2 CC7.2, ISO 27001 A.8.15, HIPAA §164.312(b), EU AI Act Art. 12, and NIST AI RMF MEASURE-3. The auditor wants to know which evidence is shared, which is unique, and where regimes diverge. This skill produces the crosswalk.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | SOC 2 / ISO / HIPAA control packs, AI Act doc, NIST AI RMF mapping, DPIA, BAA/DPA templates, regional regulator guidance |
| **Output** | `AI_Agent_Regulator_Overlap_Mapping.md` + `AI_Agent_Regulator_Overlap_Matrix.md` |
| **Standards** | All listed regimes |

## Core Instructions

### Step 1: Regimes in scope

- **SOC 2** (AICPA TSP 100; TSC 2017 / 2022 revisions).
- **ISO/IEC 27001:2022** + ISO/IEC 42001:2023 overlay.
- **HIPAA Security Rule** (45 CFR §164.302–§164.318) + Breach Notification (§164.400–§164.414).
- **EU AI Act** (Regulation 2024/1689).
- **NIST AI RMF 1.0** (2023) and updates.
- **Kenya DPA 2019** + ODPC AI guidance (2024).
- **Nigeria NDP Act 2023** + NDPC AI advisory (2024).
- **South Africa POPIA 2013** + Information Regulator guidance.
- **Uganda DPPA 2019**.
- **Rwanda DP Law 2021**.

### Step 2: Canonical control areas

| Area | Description |
|------|-------------|
| Action governance | What actions an agent may perform; authorisation model |
| Audit logging | Record-keeping for tool calls and approval events |
| Audit-log integrity | Tamper-evidence (hash-chain, WORM) |
| Access control | Identity, scope, least privilege |
| Approval and supervision | Human-in-the-loop placement |
| Kill-switch and containment | Emergency stop; force-pause |
| Incident management | Detection, response, postmortem |
| Breach notification | Timeline, recipient, content |
| Sub-processor management | Disclosure, change notice |
| Data subject rights | Access, erasure, objection, explanation |
| Transparency and disclosure | User/tenant disclosure of agent involvement |
| Cross-border transfer | Mechanism per direction |
| DPIA / impact assessment | When required; assistance |
| Bias and protected-class outcomes | Review cadence; remediation |
| Training-data exclusion | Provider commitment; evidence |
| Memory and erasure | Tiered memory; erasure SLA |
| Red-team and adversarial testing | Cadence; severity |
| Change management | CAB; ADR; gate |
| Monitoring and SLI | Burn-rate alerts; intervention |
| Documentation retention | Years per regime |

### Step 3: For each area, map to each regime

For each (area × regime) cell:

- The specific clause / criterion / standard ID.
- The shared evidence artefact (if any) — name and frequency.
- Divergent evidence required — name and rationale.
- Risk if the area is treated as fully overlapping without divergent evidence.

Produce the matrix in `references/ai-agent-regulator-overlap-matrix.md`.

### Step 4: Identify EU AI Act tier per feature

Cross-link the EU AI Act classification from `ai-act-and-regulatory-compliance-doc`:

- Prohibited (Art. 5) — block.
- High-risk (Annex III) — full Annex IV technical documentation, conformity assessment, post-market monitoring, registration.
- Limited-risk (Art. 50) — transparency obligations.
- Minimal-risk — voluntary codes.

Per area declare additional AI Act obligations.

### Step 5: One-evidence-multiple-regimes reuse table

Produce a concrete reuse table:

| Evidence artefact | SOC 2 | ISO | HIPAA | EU AI Act | NIST | KE | NG | ZA | UG | RW |
|---------------------|--------|-----|--------|------------|------|-----|-----|-----|-----|-----|
| Hash-chain integrity report | CC7.2, PI1.4 | A.8.15, A.8.24 | 164.312.b, .c | Art. 12 | MEASURE-3 | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Kill-switch drill report | CC7.4, A1.3 | A.5.30 | 164.308.a.7 | n/a (operational) | MANAGE | s.41 | Art. 32 | s.19 | s.19 | Art. 25 |
| Approval event sample | CC5.1, PI1.4 | A.5.15, A.8.2 | 164.312.d | Art. 14 | MEASURE | s.40 | Art. 29 | s.71 | s.24 | Art. 26 |
| DPIA addendum | P3 | A.5.34 | 164.502 | Art. 27 | MAP | s.31 | Art. 28 | s.71 | s.21 | Art. 22 |
| Sub-processor list + change log | CC9.1, P6 | A.5.19, A.5.20 | 164.308.b.1 | (provider chain) | GOVERN | s.40 | Art. 29 | s.20 | s.24 | Art. 26 |

### Step 6: Write the mapping doc

`AI_Agent_Regulator_Overlap_Mapping.md` sections: 1) Regimes in Scope, 2) Canonical Control Areas, 3) Per-area Regime Crosswalk, 4) EU AI Act Tier per Feature, 5) Evidence Reuse Table, 6) Divergent Evidence Required per Regime, 7) Update Triggers, 8) Sign-off.

## Standards

- All regimes listed in Step 1.

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-regulator-overlap-matrix.md`.

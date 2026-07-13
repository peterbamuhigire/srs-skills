---
name: 20-ai-agent-soc2-control-pack
description: Use when mapping an L1+ AI agent to SOC 2 trust-services controls, implementation evidence, sampling, testing, exceptions, and owners. Use ISO 27001 or HIPAA control packs for those frameworks and evidence-pack-spec for collection rules.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent SOC 2 Control Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when mapping an L1+ AI agent to SOC 2 trust-services controls, implementation evidence, sampling, testing, exceptions, and owners. Use ISO 27001 or HIPAA control packs for those frameworks and evidence-pack-spec for collection rules.

## Do Not Use When

- Do not use for L0 suggest-only AI features with no tool-call surface; the parent SaaS SOC 2 control pack is sufficient. Do not use as the sole control mapping for HIPAA or ISO; use the parallel HIPAA and ISO control packs.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_Evidence_Pack_Spec.md, parent SOC 2 control matrix (if exists). | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A control is applicable but evidence or test procedure is absent | Record a gap; do not claim control effectiveness | Unsupported assurance |
| Control, owner, evidence, sampling, and test all align | Mark the row ready for independent assessment | Framework checkbox compliance |

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
| AI Agent SOC 2 Control Pack | Accountable reviewer, control owner, auditor, or release authority | Every applicable TSC criterion shall have an agent-specific implementation requirement, an evidence row, an evidence-frequency value, and a test procedure. Every irreversible-action-class control shall name the human-final-decision evidence. Every monitoring criterion shall name the SLI from the agent SLO doc. Every control narrative shall be readable by an AICPA auditor in under three minutes. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent SOC 2 Control Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every applicable TSC criterion shall have an agent-specific implementation requirement, an evidence row, an evidence-frequency value, and a test procedure. Every irreversible-action-class control shall name the human-final-decision evidence. Every monitoring criterion shall name the SLI from the agent SLO doc. Every control narrative shall be readable by an AICPA auditor in under three minutes.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent SOC 2 Control Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a control is applicable but evidence or test procedure is absent, record a gap; do not claim control effectiveness. Record the evidence and result in the validation record; this avoids unsupported assurance.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

The SOC 2 auditor walks the Trust Services Criteria row by row. For an agentic SaaS, the parent SaaS control narrative is insufficient because every TSC row has agent-specific implementation depth the auditor will ask about: the agent service principal's access (CC6), agent action monitoring (CC7), agent change management (CC8), agent availability SLI (A1), processing integrity of agent output (PI1), confidentiality of tool-output (C1), and privacy of agent-handled personal data (P1–P8).

This skill produces the control pack: one row per applicable TSC criterion, naming the agent-specific implementation, the evidence the auditor will accept, the frequency, the test procedure, and the auditor walkthrough script. The software-dev pass owns the **collector** that produces the evidence; this pack defines what the collector must produce and the format the auditor will read.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Agent PRD, Action Catalogue, Agent Architecture, Agent SLO, Agent Runbook, Agent Eval, Agent Red-Team, Responsible-AI Addendum, ADR Catalogue, Policy Pack, Evidence Pack Spec |
| **Output** | `AI_Agent_SOC2_Control_Pack.md` + `soc2-controls/*.md` |
| **Standards** | AICPA TSP 100 (2017, 2022 revisions); SOC 2 Type II attest engagement |

## Core Instructions

### Step 1: Confirm scope

For each TSC category, declare in-scope or out-of-scope with reasoning:

- **Security (CC1–CC9)** — always in-scope for any agent feature.
- **Availability (A1)** — in-scope if a customer-facing SLA names agent-task availability.
- **Confidentiality (C1)** — in-scope if customer-confidential data is processed by the agent (almost always).
- **Processing Integrity (PI1)** — in-scope if the agent performs transactional or financial actions (billing, ledger, contracts, regulated reporting).
- **Privacy (P1–P8)** — in-scope if the agent processes personal data; mandatory if any feature is subject to GDPR, CCPA, or an African DPA.

### Step 2: Agent-specific control extensions

Walk every applicable criterion and declare the agent-specific implementation. Default treatment:

| TSC | Agent-specific extension |
|-----|---------------------------|
| CC1 Control Environment | Agent governance owner named; policy pack signed; ADR catalogue current |
| CC2 Communication | Agent disclosures (user, tenant admin); Responsible-AI public paragraph |
| CC3 Risk Assessment | Agent-feature risk register row per feature; reversibility classification rubric applied |
| CC4 Monitoring | Agent SLI burn-rate alerts active; intervention rate trended; quarterly audit-log review |
| CC5 Control Activities | Approval-event control; kill-switch control; supervision-policy control |
| CC6 Logical Access | Agent service-principal access reviewed quarterly; per-tenant scope verified; tool allow-list enforced |
| CC7 System Operations | Agent-incident playbooks; anomaly detection on irreversible-action rate, intervention rate, cost-per-run, cross-tenant tool routing |
| CC8 Change Management | Planner / catalogue / supervisor / kill-switch changes through CAB; red-team smoke required; ADR required |
| CC9 Risk Mitigation | Agent insurance / vendor risk; provider sub-processor change protocol |
| A1 Availability | Agent-task availability SLI; capacity for peak agent runs; failover for orchestrator |
| C1 Confidentiality | Tool-output isolation; cross-tenant routing prevention; memory tier confidentiality; redaction in audit log |
| PI1 Processing Integrity | Action audit log integrity (hash-chain); reproduce-script evidence; eval coverage |
| P1–P8 Privacy | DPIA addendum; consent capture for agent processing; right-to-erasure on agent memory; sub-processor notice for model provider |

### Step 3: Declare evidence per criterion

For each criterion, declare:

- **Evidence artefact name** (e.g., `agent_access_review_Qn.csv`).
- **Source system** (e.g., IAM provider, agent orchestrator, audit log).
- **Capture method** (automated collector, scheduled job, sign-off ledger).
- **Frequency** (continuous, daily, weekly, monthly, quarterly, annual, on-event).
- **Retention** (per evidence-pack spec).
- **Sampling protocol** (full population, statistical sample with stated confidence, judgemental sample with stated size).

Refer to `references/ai-agent-soc2-control-matrix-template.md` for the canonical evidence table.

### Step 4: Declare the test procedure per criterion

For each criterion, declare the auditor's test:

- **Inquiry** (question the auditor will ask, and the role who answers).
- **Inspection** (artefact the auditor will inspect, and the system of record).
- **Observation** (walkthrough the auditor will observe — e.g., kill-switch drill).
- **Reperformance** (action the auditor will reperform — e.g., approve an irreversible action, then verify the audit-log row).

### Step 5: Declare the sampling protocol

| Population | Default sample |
|-------------|----------------|
| Approval events (irreversible actions) | 25 events stratified across features, or full population if < 25 |
| Kill-switch drills | full population (typically quarterly = 4) |
| Action-catalogue change PRs | 25 PRs stratified across features, or full population |
| Access reviews | 1 review per quarter, full population of agent service principals |
| Memory-erasure requests | full population |
| Red-team CRITICAL findings | full population; HIGH/MEDIUM by sample |
| Eval gate failures | full population during the audit window |
| Incident postmortems (SEV1/SEV2) | full population |

### Step 6: Auditor walkthrough script

Write a 1-page walkthrough script per major area: agent governance, action audit log, kill-switch drill, approval-event flow, evidence-pack assembly. Each script names the demoer role, the system, the click path, and the artefact the auditor will leave with.

### Step 7: Write the pack

`AI_Agent_SOC2_Control_Pack.md` sections: 1) Scope, 2) Agent-Specific Control Extensions, 3) Evidence Inventory, 4) Test Procedures, 5) Sampling Protocols, 6) Auditor Walkthrough Scripts, 7) Cross-Refs (to policy pack, evidence pack spec, runbook), 8) Sign-off Ledger.

## Standards

- AICPA TSP 100 (Trust Services Criteria)
- AICPA AT-C Section 205 (Attest Engagements)
- ISO/IEC 42001 Clause 9 (cross-link)
- NIST AI RMF MEASURE / MANAGE (cross-link)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-soc2-control-matrix-template.md`.

---
name: 23-ai-agent-compliance-policy-pack
description: Use when producing signed, auditor-readable policies for agent actions, audit logs, approval, supervision, kill switch, memory erasure, red-team work, evidence, and attestation. Use control packs for framework mappings and evidence-pack-spec for proof.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent Compliance Policy Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when producing signed, auditor-readable policies for agent actions, audit logs, approval, supervision, kill switch, memory erasure, red-team work, evidence, and attestation. Use control packs for framework mappings and evidence-pack-spec for proof.

## Do Not Use When

- Do not use as a substitute for the parent SaaS information security policy set; pair with it. Do not use marketing language; auditor-grade plain English only.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Evidence_Pack_Spec.md, parent information security policy set. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| AI Agent Compliance Policy Pack | Accountable reviewer, control owner, auditor, or release authority | Every policy shall have scope, definitions, statements, roles, exceptions, review cadence, signature block. Every policy shall name the controls (SOC2/ISO/HIPAA IDs) it supports. Every statement shall be prescriptive (uses 'shall'). Review cadence shall be annual minimum. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent Compliance Policy Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every policy shall have scope, definitions, statements, roles, exceptions, review cadence, signature block. Every policy shall name the controls (SOC2/ISO/HIPAA IDs) it supports. Every statement shall be prescriptive (uses 'shall'). Review cadence shall be annual minimum.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent Compliance Policy Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

Seven written policies an agentic SaaS shall maintain to pass SOC 2 (CC1 Control Environment, CC5 Control Activities), ISO 27001 (A.5.1 Policies), and HIPAA (§164.316(a) Policies and procedures). The pack is the textual evidence the auditor expects to see signed, dated, and current.

## Policies in the pack

1. **Agent Action Governance Policy** — what agent actions are permitted, who governs, classification of actions, autonomy levels, irreversibility gates.
2. **Agent Audit-Log Retention Policy** — retention periods per event class, hash-chain integrity, access policy.
3. **Agent Approval and Supervision Policy** — when human approval is required, how supervision is recorded, sampling for review-after-act.
4. **Agent Kill-Switch and Drill Policy** — kill-switch surfaces, two-person rule, propagation SLA, drill cadence.
5. **Agent Memory Erasure Policy** — memory tiers, erasure triggers, verification, certificate of erasure.
6. **Agent Red-Team and Safety Policy** — adversarial test cadence, severity matrix, sign-off rules.
7. **Agent Compliance Evidence and Attestation Policy** — what evidence is collected, where it lives, how attestation is produced.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Agent PRD, Action Catalogue, Agent Architecture, SLO, Runbook, Eval, Red-Team, Responsible-AI Addendum, ADR Catalogue, Evidence Pack Spec, parent ISP set |
| **Output** | `AI_Agent_Compliance_Policy_Pack.md` + 7 files in `policies/` |
| **Standards** | SOC 2 CC1 / CC5 / CC8; ISO/IEC 27001 A.5.1; HIPAA §164.316; ISO/IEC 42001 Clause 5.2 |

## Core Instructions

### Step 1: Common structure per policy

| Section | Content |
|---------|---------|
| 1. Purpose | One-paragraph purpose statement |
| 2. Scope | Features, environments, roles in scope |
| 3. Definitions | Terms used in the policy (cross-link glossary) |
| 4. Policy statements | Numbered prescriptive statements ("shall" language) |
| 5. Roles and responsibilities | Named roles; accountability matrix |
| 6. Exceptions and waivers | When an exception is allowed; who approves; max duration |
| 7. Review cadence | Annual minimum; trigger events for off-cycle review |
| 8. Related controls | SOC2 / ISO / HIPAA control IDs supported |
| 9. Related documents | Cross-refs |
| 10. Sign-off | Role, name, signature, date, policy version |

### Step 2: Policy 1 — Agent Action Governance

Declare:

- Permitted action classes (read / write-internal / write-external / billing).
- Reversibility classification rubric.
- Autonomy levels (L0 suggest-only, L1 approve-each, L2 approve-batch, L3 autonomous, L4 cross-domain).
- Irreversibility gates: every irreversible-class tool requires a named human approval at the moment of execution.
- Catalogue change-control: PR + ADR + red-team smoke + sign-off.

### Step 3: Policy 2 — Agent Audit-Log Retention

Reproduce the retention table from the Responsible-AI Addendum; bind it as policy. Declare hash-chain integrity, daily review, access policy.

### Step 4: Policy 3 — Agent Approval and Supervision

Declare:

- Review-before-act: required for L1, irreversible-class, PHI-touching actions.
- Review-after-act: permitted for L2 compensable actions; sampling rate per feature.
- Sample-review: permitted for L3 read-only actions; minimum 5% sample.
- Approval evidence: signed event with approver role, time, plan id.

### Step 5: Policy 4 — Agent Kill-Switch and Drill

Declare:

- Three kill-switch surfaces: global, per-tenant, per-feature.
- Two-person rule for global kill-switch.
- Propagation SLA (default 5 s).
- Drill cadence: quarterly in staging; annual in production with notification.
- Drill evidence: drill report; audit-log entry.

### Step 6: Policy 5 — Agent Memory Erasure

Declare:

- Memory tiers: scratchpad (ephemeral per run), episodic (per session), long-term (opt-in per tenant).
- Erasure triggers: tenant deletion, user DSAR, contractual expiry, regulatory order, opt-out toggle.
- Erasure procedure: verifier job; certificate of erasure produced.
- Retention exceptions: legal hold, incident evidence pack (within retention window).

### Step 7: Policy 6 — Agent Red-Team and Safety

Declare:

- Red-team CI smoke on every relevant PR.
- Weekly full red-team replay.
- Quarterly external red-team.
- Sign-off rules: zero CRITICAL, zero HIGH open findings before L1+ rollout.
- New scenario intake within 7 days of advisory.

### Step 8: Policy 7 — Agent Compliance Evidence and Attestation

Declare:

- Evidence inventory per control class.
- Collector ownership (software-dev pass).
- Retention per evidence-pack spec.
- Attestation cadence: SOC 2 Type II annual; ISO surveillance annual; HIPAA annual.
- Auditor portal access governance.

### Step 9: Assemble the pack and sign

Bundle into `AI_Agent_Compliance_Policy_Pack.md` with a cover page listing all seven policies, their owners, version numbers, signature dates. Each policy file lives in `policies/`. Sign-off ledger records every signature.

## Standards

- SOC 2 TSP 100 CC1.1, CC5.1
- ISO/IEC 27001:2022 A.5.1
- ISO/IEC 27002:2022 §5.1
- HIPAA §164.316(a) and §164.316(b)
- ISO/IEC 42001 Clause 5.2 (policy)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-compliance-policy-pack-template.md`.

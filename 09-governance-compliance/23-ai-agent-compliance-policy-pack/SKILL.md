---
name: "ai-agent-compliance-policy-pack"
description: "Generate the AI Agent Compliance Policy Pack: seven bundled, signed, auditor-readable policies — agent action governance, agent audit-log retention, agent approval and supervision, agent kill-switch and drill, agent memory erasure, agent red-team and safety, agent compliance evidence and attestation. Each policy carries scope, definitions, statements, roles, exceptions, review cadence, and the signature block."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features at L1+ and must demonstrate written policies to SOC 2, ISO 27001, HIPAA, or a covered-entity / enterprise procurement review. Mandatory before any external audit, BAA execution, or enterprise sales review."
  do_not_use_when: "Do not use as a substitute for the parent SaaS information security policy set; pair with it. Do not use marketing language; auditor-grade plain English only."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Evidence_Pack_Spec.md, parent information security policy set."
  workflow: "For each of the seven policies, declare scope, definitions, policy statements, roles and responsibilities, exceptions and waivers, review cadence, and the signature block; assemble the pack; ledger sign-off; publish."
  quality_standards: "Every policy shall have scope, definitions, statements, roles, exceptions, review cadence, signature block. Every policy shall name the controls (SOC2/ISO/HIPAA IDs) it supports. Every statement shall be prescriptive (uses 'shall'). Review cadence shall be annual minimum."
  anti_patterns: "Do not write 'best practices' language; use 'shall'. Do not omit the exceptions section — auditors expect to see how exceptions are governed. Do not skip the signature block; an unsigned policy is not evidence. Do not let the same person sign all seven policies; spread accountability across AI Lead, CTO, CEO, DPO, CISO."
  outputs: "AI_Agent_Compliance_Policy_Pack.md (bundle) and seven standalone policy files under `policies/`."
  references: "Use references/ai-agent-compliance-policy-pack-template.md."
---

# AI Agent Compliance Policy Pack Skill

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

---
name: "ai-agent-hipaa-control-pack"
description: "Generate the AI Agent HIPAA Security Rule Control Pack: per-standard treatment for §164.308 Administrative, §164.310 Physical, §164.312 Technical safeguards; agent-specific implementation for access controls, audit controls, integrity controls, transmission security, contingency; admin-only constraint for clinical PHI agents; BAA implications; minimum-necessary application to agent service principals."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features that may process Protected Health Information (PHI) — clinical, payer, life-sciences, employer-health, behavioural-health, or wellness with regulated overlap. Mandatory before HIPAA-regulated tenants are onboarded. Refreshed annually and after any change to the planner, action catalogue, supervisor, kill-switch SLA, or BAA list."
  do_not_use_when: "Do not use for AI features that demonstrably do not touch PHI (synthetic-data demos, non-PHI workflows, marketing analytics on de-identified Safe-Harbor data). Do not use as the sole pack if EU patients are in-scope — pair with the AI Act and GDPR coverage. Do not relax the admin-only constraint for clinical PHI agents."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md (with phi_touch metadata), AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_BAA_Addendum.md, AI Data Flow and DPIA, existing BAA with covered entity (if any)."
  workflow: "Classify every agent feature by PHI touch (none / limited / clinical); apply the admin-only constraint to clinical PHI agents; declare the agent-specific treatment per HIPAA standard and implementation specification; declare BAA implications; declare evidence and audit procedure; write the pack."
  quality_standards: "Every PHI-touching feature shall have a Security Rule treatment per standard and implementation specification (required/addressable). Clinical PHI agents shall be admin-only with no autonomous L1+ external-write tools touching PHI. Every audit control row shall reference the hash-chain action audit log. BAA addendum language shall be cited."
  anti_patterns: "Do not run a clinical PHI agent at L1+ for irreversible external-write tools. Do not skip the addressable implementation specifications (HHS expects a documented reason if not implemented). Do not omit minimum-necessary application to the agent service principal. Do not log raw PHI fields in audit metadata — log identifiers and redacted references."
  outputs: "AI_Agent_HIPAA_Control_Pack.md, per-standard entries in `hipaa-controls/<id>.md`, and HIPAA_PHI_Touch_Classification.md."
  references: "Use references/ai-agent-hipaa-control-matrix-template.md."
---

# AI Agent HIPAA Security Rule Control Pack Skill

## Overview

The HIPAA Security Rule (45 CFR §164.302–§164.318) is the auditable control framework for PHI confidentiality, integrity, and availability. For an agentic SaaS, the rule's "workforce" concept extends to the agent service principal; the audit-control standard maps onto the agent action audit log; the integrity standard maps onto hash-chain or WORM; and the technical access-control standard maps onto per-tenant scope at the dispatcher.

The defining policy decision for clinical PHI agents is **admin-only**: a clinical PHI agent shall not act autonomously on external systems containing PHI. Every irreversible external-write tool touching PHI shall be gated by a named clinician approval event. This is the operationalisation of §164.312(a)(1) (Access Control) and §164.312(b) (Audit Controls) for agent systems handling clinical PHI.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Agent PRD, Action Catalogue (with phi_touch), Agent Architecture, Agent SLO, Agent Runbook, Agent Eval, Agent Red-Team, Responsible-AI Addendum, ADR Catalogue, Policy Pack, BAA Addendum, AI Data Flow + DPIA, existing BAA |
| **Output** | `AI_Agent_HIPAA_Control_Pack.md` + `hipaa-controls/*.md` + `HIPAA_PHI_Touch_Classification.md` |
| **Standards** | 45 CFR §164.302–§164.318; HHS OCR audit protocol; HITRUST CSF (cross-link); NIST 800-66 Rev. 2 |

## Core Instructions

### Step 1: Classify every feature by PHI touch

| Class | Definition | Allowed autonomy |
|-------|-------------|--------------------|
| `none` | Agent feature does not access PHI; covered-entity tenant uses for non-clinical workflows | L0–L3 per parent policy |
| `limited` | Agent reads PHI but does not write; outputs are summaries, drafts, classifications | L0, L1 with human approval per call |
| `clinical` | Agent reads PHI and produces clinical-decision-relevant output, or writes back to a clinical system | L0 only with admin role; L1 only with named clinician approval; no L2+; no autonomous external-write |

Record the classification in `HIPAA_PHI_Touch_Classification.md` and reflect it in the action catalogue's `phi_touch` metadata field.

### Step 2: §164.308 Administrative safeguards

| Standard | Implementation spec | Agent treatment |
|----------|---------------------|------------------|
| §164.308(a)(1) Security management process | Risk analysis (R); risk management (R); sanction policy (R); IS activity review (R) | Agent risk register; agent activity review = daily irreversible-action audit-log review |
| §164.308(a)(2) Assigned security responsibility | (R) | AI Lead + Security Officer named in policy pack |
| §164.308(a)(3) Workforce security | Authorisation (A); termination (A) | Agent service principal provisioning and deprovisioning; per-tenant scope |
| §164.308(a)(4) Information access management | Access authorisation (A); access establishment and modification (A); isolating clearinghouse functions (R) | Tool allow-list per service principal; per-tenant scope at dispatcher; quarterly review |
| §164.308(a)(5) Security awareness and training | (A; security reminders, malware, login monitoring, password) | Agent on-call training; tool-output poisoning awareness training |
| §164.308(a)(6) Security incident procedures | (R) | Agent incident playbooks; HHS notification path for PHI incidents |
| §164.308(a)(7) Contingency plan | Data backup (R); disaster recovery (R); emergency mode (R); testing (A); criticality analysis (A) | Kill-switch operations; replay-a-run drill; agent-task quarantine |
| §164.308(a)(8) Evaluation | (R) | Annual HIPAA evaluation including agent controls |
| §164.308(b)(1) BAA | (R) | BAA addendum for agent processing; model provider BAA where required |

### Step 3: §164.310 Physical safeguards

Inherited from parent if no dedicated agent infrastructure. Cite inheritance.

### Step 4: §164.312 Technical safeguards

| Standard | Implementation spec | Agent treatment |
|----------|---------------------|------------------|
| §164.312(a)(1) Access control | Unique user ID (R); emergency access (R); automatic logoff (A); encryption/decryption (A) | Unique agent service-principal ID; emergency operator access via kill-switch console; automatic session expiry on the operator console; tool-call payload encryption in transit and at rest |
| §164.312(b) Audit controls | (R) | Action audit log per Responsible-AI Addendum retention; hash-chain integrity; daily review |
| §164.312(c)(1) Integrity | Mechanism to authenticate ePHI (A) | Hash-chain audit log; signed approval events; reproduce-script preservation |
| §164.312(d) Person or entity authentication | (R) | Approver identity verified at the approval moment; signed event |
| §164.312(e)(1) Transmission security | Integrity controls (A); encryption (A) | TLS 1.2+ enforced; signed claim on tenant identity to provider |

### Step 5: §164.316 Policies, procedures, and documentation

| Standard | Agent treatment |
|----------|------------------|
| §164.316(a) Policies and procedures | Compliance Policy Pack signed and reviewed annually |
| §164.316(b)(1) Documentation | All agent control documents retained 6 years from creation or last effective date |

### Step 6: Minimum-necessary application

The minimum-necessary rule (§164.502(b)) applies to the agent service principal:

- The agent shall not request PHI beyond what is required for the current task.
- The retrieval set returned to the agent shall be minimised by query-scoped filter and per-tenant scope.
- Audit log records the PHI fields touched per tool call.
- Quarterly review samples tool calls and verifies minimum-necessary compliance.

### Step 7: BAA implications

- BAA addendum language for agent processing (see `26-ai-agent-baa-and-data-processing-language`).
- Model provider BAA required if the provider processes PHI; alternatives:
  1. De-identify before model call (Safe Harbor or Expert Determination).
  2. Use provider with executed BAA and zero-retention configuration.
  3. Run model on-premise / on-tenant infrastructure within the covered entity's boundary.

### Step 8: Breach notification

- §164.408 PHI breach notification: ≤ 60 days to affected individuals; immediate to HHS for ≥ 500 individuals.
- Agent breach scenarios: cross-tenant retrieval leak, prompt-injection-driven disclosure, audit-log integrity compromise, memory-tier leak.

### Step 9: Write the pack

`AI_Agent_HIPAA_Control_Pack.md` sections: 1) PHI Touch Classification per Feature, 2) Admin-Only Constraint Statement, 3) Administrative Safeguards (§164.308), 4) Physical Safeguards (§164.310), 5) Technical Safeguards (§164.312), 6) Policies and Documentation (§164.316), 7) Minimum-Necessary Application, 8) BAA Implications, 9) Breach Notification Procedure, 10) Evidence and Audit Procedure, 11) Cross-Refs, 12) Sign-off Ledger.

## Standards

- 45 CFR §164.302–§164.318 (HIPAA Security Rule)
- 45 CFR §164.400–§164.414 (Breach Notification Rule)
- 45 CFR §164.500–§164.534 (Privacy Rule, where the agent processes PHI for treatment, payment, operations)
- NIST SP 800-66 Rev. 2 (HIPAA Security Rule implementation)
- HHS OCR audit protocol
- HITRUST CSF (cross-link)

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-hipaa-control-matrix-template.md`.

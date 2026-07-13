---
name: 22-ai-agent-hipaa-control-pack
description: Use when mapping a PHI-touching AI agent to HIPAA Security Rule safeguards, minimum-necessary access, BAA duties, evidence, testing, and breach handling. Use ISO 27001 or SOC 2 packs for those frameworks.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# AI Agent HIPAA Security Rule Control Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when mapping a PHI-touching AI agent to HIPAA Security Rule safeguards, minimum-necessary access, BAA duties, evidence, testing, and breach handling. Use ISO 27001 or SOC 2 packs for those frameworks.

## Do Not Use When

- Do not use for AI features that demonstrably do not touch PHI (synthetic-data demos, non-PHI workflows, marketing analytics on de-identified Safe-Harbor data). Do not use as the sole pack if EU patients are in-scope — pair with the AI Act and GDPR coverage. Do not relax the admin-only constraint for clinical PHI agents.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md (with phi_touch metadata), AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_Runbook.md, AI_Agent_Eval_Spec.md, AI_Agent_Red_Team_Test_Plan.md, AI_Agent_Responsible_AI_Addendum.md, AI_Agent_ADR_Catalogue.md, AI_Agent_Compliance_Policy_Pack.md, AI_Agent_BAA_Addendum.md, AI Data Flow and DPIA, existing BAA with covered entity (if any). | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
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
| AI Agent HIPAA Security Rule Control Pack | Accountable reviewer, control owner, auditor, or release authority | Every PHI-touching feature shall have a Security Rule treatment per standard and implementation specification (required/addressable). Clinical PHI agents shall be admin-only with no autonomous L1+ external-write tools touching PHI. Every audit control row shall reference the hash-chain action audit log. BAA addendum language shall be cited. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| AI Agent HIPAA Security Rule Control Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every PHI-touching feature shall have a Security Rule treatment per standard and implementation specification (required/addressable). Clinical PHI agents shall be admin-only with no autonomous L1+ external-write tools touching PHI. Every audit control row shall reference the hash-chain action audit log. BAA addendum language shall be cited.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing AI Agent HIPAA Security Rule Control Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
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

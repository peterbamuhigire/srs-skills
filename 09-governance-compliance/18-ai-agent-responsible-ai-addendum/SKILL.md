---
name: "ai-agent-responsible-ai-addendum"
description: "Generate the AI Agent Responsible-AI Addendum: action accountability (who is responsible for an agent action), audit-log retention by event class, contestability of agent actions, human-final-decision principle for irreversible actions, agent-specific bias and harm reviews, and the cross-link to the public Responsible AI Declaration."
metadata:
  use_when: "Use whenever a SaaS ships one or more agent features to external users. Required alongside the parent Responsible AI Declaration. Updated quarterly."
  do_not_use_when: "Do not use for AI features that do not call tools or act on the user's behalf. Cover those under the parent Responsible AI Declaration."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Architecture_Spec.md, AI_Agent_SLO_Doc.md, AI_Agent_User_Disclosure_Pack.md, Responsible_AI_Declaration.md, AI_Act_Regulatory_Compliance_Doc.md."
  workflow: "Declare action accountability per feature, declare audit-log retention by event class, declare the contestability mechanism, declare the human-final-decision principle for irreversible actions, declare bias and harm reviews, cross-link the public declaration, write the addendum."
  quality_standards: "Every irreversible-action class shall have a named human-final-decision principle. Every agent feature shall have a contestability path. Audit-log retention shall meet or exceed regulatory minima. Every paragraph in the public declaration that mentions agents shall trace back to an internal evidence row in the addendum."
  anti_patterns: "Do not claim 'human-in-the-loop' without stating where the human sits in the loop. Do not retain less than 13 months of irreversible-action audit log. Do not omit the bias review for any feature that affects a protected-class outcome."
  outputs: "AI_Agent_Responsible_AI_Addendum.md (internal evidence pack) and Responsible_AI_Declaration_Agent_Section.md (public)."
  references: "Use references/ai-agent-responsible-ai-addendum-template.md."
---

# AI Agent Responsible-AI Addendum Skill

## Core Instructions

### Step 1: Action accountability per feature

For each agent feature, declare:

- The accountable role for an agent action (typically the workspace admin who enabled the feature).
- The responsible party for the agent's design and operation (us).
- The named human approver role for any irreversible-action call.
- The audit retention path that supports each accountability claim.

### Step 2: Audit-log retention by event class

| Event class | Hot | Cold | Justification |
|--------------|-----|------|----------------|
| Tool call (read) | 90 d | 13 months | operational debugging |
| Tool call (write-internal) | 13 months | 3 years | tenant audit + dispute resolution |
| Tool call (write-external, billing, irreversible) | 13 months | 7 years | regulatory + dispute |
| Plan + approval events | 13 months | 7 years | regulatory + dispute |
| Kill-switch events | 13 months | 7 years | safety audit |
| Human-approval events | 13 months | 7 years | regulatory |

Retention shall meet or exceed regulatory minima per region (EU, UK, US sectoral, African DPAs).

### Step 3: Contestability mechanism

State the user-facing contestation path; the internal review SLA; the evidence assembly procedure; the escalation path; the postmortem trigger for confirmed wrong actions.

### Step 4: Human-final-decision principle

For every tool class with `reversibility_class=irreversible`, state in plain language:

- The named human role that takes the final decision.
- The moment in the flow the decision is taken.
- The information shown at that moment.
- The bypass policy (no bypass; documented exceptions only with ADR and waiver).

This is the operationalisation of EU AI Act Art. 14 for the product.

### Step 5: Bias and harm reviews

For every agent feature whose actions affect protected-class outcomes (hiring, lending, housing, healthcare, education), declare:

- The bias review cadence.
- The reviewers (named individuals; include external reviewers where regulation requires).
- The metrics tracked.
- The remediation path.

### Step 6: Cross-link the public declaration

The public Responsible AI Declaration carries plain-language paragraphs. The internal addendum is the evidence trail. Every public paragraph that mentions agents shall trace to an internal evidence row.

### Step 7: Write both documents

- `AI_Agent_Responsible_AI_Addendum.md` (internal) — the evidence trail.
- `Responsible_AI_Declaration_Agent_Section.md` (public) — the plain-language paragraphs to slot into the parent declaration.

Sections (internal): 1) Action Accountability per Feature, 2) Audit-Log Retention, 3) Contestability Mechanism, 4) Human-Final-Decision Principle, 5) Bias and Harm Reviews, 6) Public-Declaration Cross-link Table, 7) Review Cadence.

## Standards

- EU AI Act Art. 13 (transparency), Art. 14 (human oversight)
- NIST AI RMF GOVERN-3
- ISO/IEC 42001 Clause 7.4 (communication)
- Google AI Principles
- Anthropic AUP / RSP

## Compliance evidence cross-link

The addendum is a primary evidence artefact for the following control rows:

- SOC 2 CC1.1, CC2.3 — public Responsible-AI Declaration and tenant-admin disclosure.
- SOC 2 CC5.1, PI1.4 — irreversibility gates and approval-event evidence.
- ISO/IEC 27001:2022 A.5.1, A.5.34 — policy authority and PII protection.
- HIPAA §164.308(a)(4) and §164.312(d) — approval-event evidence (where PHI in scope).
- EU AI Act Art. 13 (transparency) and Art. 14 (human oversight).
- NIST AI RMF GOVERN-3.

Each Addendum section maps to one or more rows in `09-governance-compliance/25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md` (rows 25, 26, 39, 40). The Addendum is signed annually as part of the Compliance Policy Pack (`09-governance-compliance/23-ai-agent-compliance-policy-pack`).

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-responsible-ai-addendum-template.md`.

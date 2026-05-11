---
name: "ai-agent-user-disclosure-pack"
description: "Generate the AI Agent User Disclosure Pack: end-user-facing copy explaining what the agent does and does not, where it has authority, how the user overrides, undo / revert language, the 'agent worked on your behalf' notification design, and the contestation path. Plain-language, layperson-reviewable, regionalised where required."
metadata:
  use_when: "Use before any agent feature is exposed to end users at any autonomy level above L0 dogfood; required at every public stage of the agent rollout runbook."
  do_not_use_when: "Do not use for internal-only agents with no end-user exposure."
  required_inputs: "AI_Agent_Feature_PRD_Spec.md, Action_Catalogue_Spec.md, AI_Agent_Rollout_Runbook.md, Responsible_AI_Declaration.md, Trust Center doc pack."
  workflow: "Author the per-feature does-and-does-not paragraph; author the authority statement; author the override and undo copy; design the 'agent worked on your behalf' notification; author the contestation path; localise per region; write the pack."
  quality_standards: "Every agent feature shall have a does / does-not / authority / override / undo / contestation block in plain language. Copy shall be reviewable by a layperson and shall not use marketing language. Regional disclosures shall meet EU AI Act Art. 13 and local DPA requirements."
  anti_patterns: "Do not write marketing copy. Do not omit the undo / revert path. Do not bury the agent-attribution notification. Do not gate the contestation path behind authentication a user cannot reach when locked out."
  outputs: "AI_Agent_User_Disclosure_Pack.md and per-locale UI copy strings."
  references: "Use references/ai-agent-user-disclosure-pack-template.md."
---

# AI Agent User Disclosure Pack Skill

## Core Instructions

### Step 1: Per-feature does and does not

For each agent feature, write a paragraph with two bullets:

- What the agent does. Plain language. One sentence.
- What the agent does not do. Plain language. One sentence.

### Step 2: Authority statement

Per feature, state in plain language:

- Whose authority the agent acts under (the workspace, the user).
- Which actions the agent is allowed to take.
- Which actions it is not allowed to take.
- Any per-call human approval required.

### Step 3: Override and undo copy

For each agent feature:

- How to disable the feature (admin path).
- How to undo a specific action (per-action path).
- How to cancel a run in progress.
- What is not reversible (the explicit, plain-language list).

### Step 4: 'Agent worked on your behalf' notification

Design pattern for the notification that surfaces when an agent acted:

- When it shows (after every agent action with a user-visible side-effect).
- Where it shows (inbox, banner, dedicated audit drawer).
- What it shows (action verb + target + timestamp + agent name + revert button if applicable + 'how this worked' link).
- How the user dismisses it (acknowledge; do not auto-dismiss).

### Step 5: Contestation path

Per feature:

- How a user reports a wrong action (form, email, in-product flag).
- Expected response time.
- What evidence is gathered (audit log excerpt for that user / run).
- Escalation path to a human reviewer.

### Step 6: Regional disclosures

- EEA: prominent EU AI Act Art. 13 transparency notice; opt-in default for L2+; reference to the responsible-AI declaration.
- UK ICO: AI accountability statement reference.
- US: state-specific disclosures where applicable (CO AI Act 2026; NYC bias audits for employment-related agents).
- Africa: per local DPA (Uganda DPPA, Ghana DPA, Nigeria NDPR).

### Step 7: Write the pack

`AI_Agent_User_Disclosure_Pack.md` sections: 1) Per-feature Disclosure Blocks, 2) Notification Design, 3) Contestation Path, 4) Regional Disclosures, 5) Copy String Tables (per locale), 6) Review Cadence.

## Standards

- EU AI Act Art. 13 (transparency)
- ICO AI auditing guidance
- WCAG 2.2 AA (copy and contrast)
- Plain Language Act / GOV.UK content style
- Anthropic / OpenAI agent-disclosure patterns

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-user-disclosure-pack-template.md`.

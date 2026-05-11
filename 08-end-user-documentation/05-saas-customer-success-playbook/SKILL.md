---
name: "saas-customer-success-playbook"
description: "Generate a SaaS Customer Success Playbook: customer-health-score spec, segmented intervention plays at each lifecycle stage (onboarding, adoption, renewal, at-risk, expansion, churned), QBR template, dunning recovery, escalation matrix."
metadata:
  use_when: "Use for any SaaS that operates a customer success function — i.e. every B2B SaaS and most B2C SaaS at scale."
  do_not_use_when: "Do not use for tools without a CS function (rare)."
  required_inputs: "PRD.md, Pricing_And_Packaging_Spec.md, Onboarding_Journey_Spec.md (if available), churn data, contract types."
  workflow: "Define health score, segment customers, write per-stage plays, write QBR template, write dunning recovery, write escalation matrix, write the playbook."
  quality_standards: "Every play shall have trigger, owner, action, measurement of success, escalation rule."
  anti_patterns: "Do not write plays without triggers. Do not omit health-score definition. Do not skip dunning recovery."
  outputs: "Customer_Success_Playbook.md."
  references: "references/saas-customer-success-playbook-template.md"
---

# SaaS Customer Success Playbook Skill

## Overview

Produces the playbook that operationalises churn-control and expansion. Sourced from Cotton (Essay 9: churn is the quiet killer) and Garbugli (lifecycle email tactics).

## Core Instructions

### Step 1: Customer Health Score spec

Composite of (usage depth, breadth, engagement frequency, support sentiment, NPS, contract age, expansion signal). State weights, scoring formula, refresh cadence (weekly), bands (Green / Yellow / Red), action per band.

### Step 2: Segment customers

By tier (Bronze/Silver/Gold/Enterprise) × stage (onboarding 0-90 d / adoption 90-365 d / renewal-window / at-risk / churned-recoverable). Different plays per segment.

### Step 3: Per-stage plays

For each (segment, stage) pair produce a play:

```
### Play: <name>
- Trigger:
- Owner: (CSM / CS-Ops / automation)
- Action:
- Channels (in-app / email / call):
- Frequency:
- Success measurement:
- Escalation rule:
```

Required plays (minimum):

- **Onboarding kickoff** (Day 0)
- **First-value milestone check** (Day 7)
- **30-day health review**
- **At-risk intervention** (health → Red)
- **Renewal forecast** (T-90, T-60, T-30)
- **Renewal at-risk save**
- **Expansion / upsell** (health → Green + signal)
- **Dunning recovery** (payment-failure)
- **Churned recoverable** (re-engagement)

### Step 4: QBR template

Quarterly Business Review template: business objectives, usage review, value delivered, support summary, expansion opportunities, action items.

### Step 5: Escalation matrix

When does an account escalate from CSM to CS Lead, to CRO, to executive sponsor? Triggers (health, ARR, contract anniversary, executive contact change, integration partner change).

### Step 6: Write the playbook

`Customer_Success_Playbook.md` with sections: 1) Health Score Spec, 2) Segmentation, 3) Per-Stage Plays, 4) QBR Template, 5) Dunning Recovery, 6) Escalation Matrix, 7) Tooling & Source-of-Truth, 8) Cadence & Review.

## Standards

- Cotton (2020) Essay 9.
- Pulse / TSIA customer-success frameworks.
- IEEE 29148-2018 (service-level requirements).

## Resources

- `logic.prompt`, `README.md`, `references/saas-customer-success-playbook-template.md`.

---
name: "saas-moat-and-defensibility-plan"
description: "Generate a Moat & Defensibility Plan: which moat types apply (integrations / brand / owned channels / switching costs / data / network effect), which are false moats to avoid, milestones, and the roadmap to harden each."
metadata:
  use_when: "Use for any SaaS that wants explicit defensibility rather than counting on feature velocity."
  do_not_use_when: "Do not use if the product is purely tactical / commodity."
  required_inputs: "vision.md, competitive scan, PRD.md, customer-interview notes."
  workflow: "Inventory moat candidates, score current strength, identify false moats, build per-moat hardening roadmap, write the plan."
  quality_standards: "Every moat shall have a current-strength score and a hardening plan with owner and date."
  anti_patterns: "Do not treat 'unique features' as a moat. Do not list more than three primary moats — focus."
  outputs: "Moat_And_Defensibility_Plan.md."
  references: "references/saas-moat-and-defensibility-template.md"
---

# SaaS Moat & Defensibility Plan Skill

## Overview

Anchored in Walling's moat taxonomy. Forces explicit identification of real vs false moats and a hardening roadmap.

## Core Instructions

### Step 1: Moat candidates inventory

| Moat type | Description | Current strength (1-5) | Trend |
|-----------|-------------|-----------------------|-------|
| Integrations / network effect | depth of integrations into customer workflow | | |
| Brand | recognised authority in segment | | |
| Owned traffic channels | direct audience (newsletter, podcast, community) | | |
| Switching costs | data, workflows, integrations make leaving expensive | | |
| Data network effect | usage produces data that improves the product | | |
| Marketplace / two-sided | supply + demand both onboard | | |
| Regulatory / certifications | hard-won attestations | | |
| Geographic / vertical specialisation | depth in narrow segment | | |

### Step 2: False-moat watch

Per Walling, "unique features" is the false moat — competitors can copy in months. Flag the false moats currently being relied on.

### Step 3: Pick the 1-3 primary moats

Focus is more valuable than breadth. Choose at most three primary moats; the rest are "passive" (maintained, not invested).

### Step 4: Per-moat hardening plan

For each primary moat:

| Moat | Current state | Target state (12 mo) | Owner | Milestones | Investment |
|------|---------------|----------------------|-------|------------|------------|
| | | | | quarterly | $/headcount |

### Step 5: Anti-moats to avoid

- Underpricing.
- Translating product before product-market fit.
- White-labelling at small scale.
- Adding verticals too early.

### Step 6: Write the plan

`Moat_And_Defensibility_Plan.md` with: 1) Inventory, 2) False moats identified, 3) Primary moats chosen, 4) Per-moat hardening plan, 5) Anti-moats to avoid, 6) Quarterly review schedule.

## Standards

- Walling (2022).
- IEEE 29148-2018 (strategic requirements).

## Resources

- `logic.prompt`, `README.md`, `references/saas-moat-and-defensibility-template.md`.

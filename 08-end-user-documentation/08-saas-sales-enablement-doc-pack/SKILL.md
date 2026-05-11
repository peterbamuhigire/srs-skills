---
name: "saas-sales-enablement-doc-pack"
description: "Generate the SaaS Sales Enablement Doc Pack: ICP / target persona, sales-methodology selection (transactional / solution / consultative / provocative), 8-step discovery meeting script (SPI + TALKER), two-part demo script, competitive battlecards, closing playbook, MEDDIC qualification."
metadata:
  use_when: "Use for any SaaS that operates a sales motion (not pure self-serve)."
  do_not_use_when: "Do not use for pure-self-serve products with no sales rep."
  required_inputs: "PRD.md, Pricing_And_Packaging_Spec.md, competitive scan, target ICP, GTM Segment Profile (if available)."
  workflow: "Define ICP, pick methodology, write 8-step meeting script, write demo script, write battlecards, write closing playbook, write the index."
  quality_standards: "Every doc shall be product-specific (no generic templates pasted). Every discovery question shall be a tested formulation."
  anti_patterns: "Do not write generic discovery questions. Do not write demos without the two-part shape (demonstrate / integrate)."
  outputs: "Sales_Enablement_Doc_Pack.md and per-document files."
  references: "references/saas-sales-enablement-doc-pack-template.md, references/saas-value-quantification-worksheet.md"
---

# SaaS Sales Enablement Doc Pack Skill

## Overview

Sourced from Winning by Design's *SaaS Sales Method Fundamentals* and *for Account Executives*. Produces the AE-facing doc pack that operationalises discovery, demo, and closing.

## Core Instructions

### Step 1: ICP & target persona

For each segment in scope, produce: firmographics, technographics, trigger events, buying-committee map, common objections, vocabulary.

### Step 2: Sales-methodology selection

Per product line:

| Methodology | When | ACV band | Sales cycle | Deals / mo / AE |
|-------------|------|----------|-------------|-----------------|
| Transactional | high-volume inbound | < $1k | < 30d | 10-20 |
| Solution | inbound/outbound mid | $5k | ~30d | 5-10 |
| Consultative | platform sale | $20-100k | 6-18 mo | 1-3 |
| Provocative | innovation, CEO-level | $250k+ | 6-9 mo | 1-2 |

Pick one; state the team-shape implication.

### Step 3: 8-step discovery meeting script

Per Winning by Design AE method:

1. Prepare for the meeting.
2. Open the conversation.
3. ACE the start (Acknowledge, Connect, Empathise).
4. Set the agenda.
5. Diagnose situation + pain (S + P questions).
6. Summarize the conversation.
7. Provide a 3rd-party reference.
8. Identify value via impact (I) questions.

For each step write: goal, recommended phrases, common mistakes, the standard SPI questions tailored to the ICP.

### Step 4: Demo script (two-part)

- **Part 1 — Demonstrate the product.** Show the 3-5 narrative beats that show the customer's pain being solved. Use the customer's tone words from discovery.
- **Part 2 — Integrate into the call.** Tie each demo beat back to a stated customer pain. End on impact and next step.

State the demo length budget (30 min for solution sale; 60 for consultative).

### Step 5: Competitive battlecards

One per main competitor. Sections: positioning, differentiation, where they win, where we win, traps to avoid, objection responses, proof points (named customers).

### Step 6: Closing playbook

- Trade / Commit / Go Dark signals and responses.
- MEDDIC qualification (Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion).
- Mutual action plan template.
- Procurement / legal / security review playbook (DPA, security questionnaire, MSA negotiation).

### Step 7: Value quantification worksheet

Cost / Experience / Revenue impact (Reduce / Improve / Increase). Tied to discovery findings.

### Step 8: Write the pack

`Sales_Enablement_Doc_Pack.md` indexes:

- `ICP.md`
- `Sales_Methodology.md`
- `Discovery_Meeting_Script.md`
- `Demo_Script.md`
- `Battlecards/<competitor>.md`
- `Closing_Playbook.md`
- `Value_Quantification_Worksheet.md`
- `Pricing_Cheatsheet.md` (derived from Pricing & Packaging Spec)

## Standards

- IEEE 29148 (stakeholder requirements).
- Winning by Design *SaaS Sales Method* fundamentals + AE volumes.

## Resources

- `logic.prompt`, `README.md`, `references/saas-sales-enablement-doc-pack-template.md`, `references/saas-value-quantification-worksheet.md`.

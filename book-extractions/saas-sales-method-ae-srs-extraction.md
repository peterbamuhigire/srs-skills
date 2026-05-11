# The SaaS Sales Method for Account Executives — SRS-Engine Extraction

**Source:** Winning by Design, *The SaaS Sales Method for Account Executives: How to Win Customers.*

**Lens:** Which AE-facing, demo-facing, and customer-winning documents must the engine output?

## One-line takeaway

The AE method standardises **sales methodology selection (transactional / solution / consultative / provocative), a structured 8-step customer meeting, a demo "Part 1 demonstrate, Part 2 integrate" pattern, and an impact-journey map** — each of these becomes a documented artefact.

## Distinctive documentation surface

### 1. Sales-methodology selection doc

Transactional vs. solution vs. consultative vs. provocative — chosen per product based on ACV, sales-cycle, and decision-maker count. The engine should produce a **Sales Methodology Selection Document** with the chosen archetype and its operational implications (rep ramp, cycle length, deals/month/AE, expected ACV).

### 2. ICP & targeting doc

Relevance-based account targeting; the engine should output an **Ideal Customer Profile (ICP) Spec** with firmographics, technographics, trigger events, and a target-account list template.

### 3. 8-step meeting script

Prepare → Open → ACE start → Set agenda → Diagnose (SPI) → Summarize → 3rd-party reference → Identify value. The engine should produce a **Discovery Meeting Script** template per product.

### 4. Demo script (two-part pattern)

"Part 1 Demonstrate your product, Part 2 Integrate the demonstration into the call." The engine should produce a **Demo Script Spec** with the two-part structure and product-specific narrative beats.

### 5. Impact journey map

Cost / Experience / Revenue impact across the customer journey. Each impact gets quantified value & timing.

### 6. Battlecards

Implicit but essential — competitor responses, differentiation cards. The engine should produce a **Competitive Battlecard** template.

### 7. Next-step / commit / go-dark playbook

Trade / Commit / Go Dark — what to do at each customer signal. A **Closing Playbook** doc.

## Documentation patterns

- Methodology before tactics — pick the sales methodology first, then build artefacts to fit.
- The meeting is scripted as 8 named steps; the doc captures each step's goal.
- Demo isn't ad-lib; it has a documented two-part shape.

## Implications for the SDLC-Docs-Engine

1. Add Phase 08 skill **`07-saas-sales-enablement-doc-pack`** producing: ICP, methodology selection, discovery meeting script, demo script, battlecards, closing playbook.
2. Add cross-cutting template **`saas-sales-enablement-doc-pack-template.md`**.

## Source mapping

- Ch.1 (Sales methodology comparison table) → Sales Methodology Selection Document.
- Targeting / Relevance exercise → ICP Spec.
- ACE start + 8-step meeting → Discovery Meeting Script template.
- Part 1/Part 2 demo → Demo Script Spec.
- Impact journey → Value Quantification across Cost/Experience/Revenue.

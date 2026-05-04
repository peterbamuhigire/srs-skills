# SRS-Skills UX/UI Phase 2 Upgrade — Design Spec
**Date:** 2026-05-04
**Author:** Claude (with peter.bamuhigire@gmail.com)
**Status:** Approved
**Phase:** 2 of 3

## Context

Phase 1 produced 5 UX/UI book extractions. This spec defines the srs-skills changes that translate them into skill upgrades for the SDLC documentation engine.

## Scope

5 target SKILL.md files + 1 new shared doc. Total: **6 file edits**, 1 commit.

**Targets:**
1. `docs/ux-foundations.md` — new shared doc
2. `03-design-documentation/05-ux-specification/SKILL.md`
3. `01-strategic-vision/01-prd-generation/SKILL.md`
4. `01-strategic-vision/03-vision-statement/SKILL.md`
5. `01-strategic-vision/04-lean-canvas/SKILL.md`
6. `01-strategic-vision/07-premium-product-positioning/SKILL.md`

## Approach

Hybrid (per user choice "D"): one shared doc holds cross-cutting UX foundations referenced by multiple skills; each skill gets a focused inline append. Mirrors the social-media-skills Phase 2 pattern.

**Note on `skills/ux-standards.md`:** This existing file is a SaaS implementation-patterns doc (Select2 dropdowns, etc.), not a UX-philosophy doc. It is **not modified** by this spec. The new `docs/ux-foundations.md` lives at a different layer (philosophy + process) and references the canonical extractions in `book-extractions/`.

**Note on `book-extractions/`:** SRS does NOT have a local `book-extractions/` folder (per Phase 1 spec — SRS references the canonical at `C:\Users\BIRDC\.claude\skills\book-extractions\`). The new doc cites that canonical path.

## New shared doc — `docs/ux-foundations.md`

Six sections (broader than social-media's 4-section version because SRS spans more disciplines):

### Section 1 — Branson Persona Discipline
Stories at the centre, Edge cases, Designing-for-themselves trap, Choosing the Essential Persona, Mechanics, "Clingy" personas. Source: `branson-ux-ui-design-extraction.md` Section 4.

### Section 2 — Levy Four Tenets + Top-10 Anti-Patterns + Business Model Canvas (9 blocks)
Adds the BMC because Lean Canvas is a direct descendant. The 9 blocks: customer segments, value propositions, channels, customer relationships, revenue streams, key resources, key activities, key partnerships, cost structure. Note: UX strategy intersects most strongly with **customer segments + value propositions**. Source: `levy-ux-strategy-extraction.md` Parts I–III.

### Section 3 — Synechron 5 Outcomes + 5-Level UX Maturity Checklist
- Outcomes (Useful, Easy, Efficient, Pleasing, Accessible) as a launch gate
- Maturity (Levels 0–4) as a process gate — premium claims require Level 3 minimum
- Activity-by-Level matrix as a checklist
Source: `enterprise-ux-financial-insurance-extraction.md` Parts I, VIII, IX.

### Section 4 — Branson Working Memory + 4-Stage Cognitive Affordance
- Miller's 7±2 + chunking + stacking + cognitive load (Sweller) — used as NFR templates
- 4-stage affordance: Presence → Visibility → Recognizability → Intelligibility — used as UX-spec rules
Source: `branson-ux-ui-design-extraction.md` Sections 5 + 6.

### Section 5 — Deacon 3 Levels of UX Scope
Single Interaction / Journey / Relationship — required declaration in every PRD/vision artifact. Source: `deacon-ux-ui-strategy-extraction.md` Section 2.

### Section 6 — Cross-References
Canonical extractions paths + skill consumption map.

## Per-skill inline edits

### 1. `03-design-documentation/05-ux-specification/SKILL.md`

**Append:** "UX foundations integration (added 2026-05-04)"
- Cite all 6 sections of the shared doc as required reading
- Specific rules for the UX specification document:
  - **Required NFR templates** drawn from Section 4: list-length cap (Miller), form-field-per-step cap, cognitive-load minimization
  - **Required affordance audit** drawn from Section 4: every primary CTA must pass Presence/Visibility/Recognizability/Intelligibility
  - **Required scope declaration** drawn from Section 5: which of the 3 Deacon levels does the spec target?
  - **Required maturity declaration** drawn from Section 3: at what UX maturity level does this spec aim to operate?
- Note: existing references (`design-handoff.md`, `design-system-guide.md`, `information-architecture.md`, `premium-ui-ux-specification.md`, `usability-testing.md`, `wireframing-standards.md`) remain untouched; the new section augments them.

### 2. `01-strategic-vision/01-prd-generation/SKILL.md`

**Append:** "Strategic foundations check (Levy + Branson)"
- Four Tenets check before PRD work — verify upstream artifacts contain Business Strategy + Value Innovation + Validated User Research + Killer UX Design evidence
- Persona discipline applied to PRD's persona section: cite Section 1; require Essential Persona declaration
- Field-of-Dreams flag: PRDs without validated user research input are marked "speculative"

### 3. `01-strategic-vision/03-vision-statement/SKILL.md`

**Append:** "Vision-statement filter (Levy Top-10)"
- Reject vision statements that match any of Levy's Top-10 Not-UX-Strategies anti-patterns
- Specifically call out the most common SRS-context failures:
  - **#10 (North Star)** — vision statements that read as "be the X of Y" without operational meaning
  - **#9 (Hallmark-card affirmation)** — "deliver excellence and innovation" — too vague to act on
  - **#4 (buzzword permutation)** — "AI-powered Web3 platform for the metaverse"
- If a draft vision matches any anti-pattern, return to interview stage rather than polish the prose

### 4. `01-strategic-vision/04-lean-canvas/SKILL.md`

**Append:** "Lean Canvas ↔ Business Model Canvas mapping (Levy)"
- Explicit mapping between Lean Canvas blocks and Osterwalder's BMC blocks
- Highlight where Levy says UX strategy intersects: customer segments + value propositions = the bolded BMC blocks
- Note: this is an additive mapping, not a replacement for the existing Lean Canvas methodology — both canvases coexist; BMC is referenced for the strategic-segment depth

### 5. `01-strategic-vision/07-premium-product-positioning/SKILL.md`

**Append:** "Premium positioning gate (Synechron 5 outcomes + maturity)"
- Premium-pricing claims require ALL 5 outcomes documented (Useful + Easy + Efficient + Pleasing + Accessible)
- 4-of-5 disqualifies premium pricing — drop to standard tier
- Plus: premium claims require Level 3 (UX Design) minimum on the Synechron maturity scale; Level 4 (Experience Design) for top-tier
- Tie-in to other engines: cite `website-skills/skills/design-quality-score/` Category 8 for parallel scoring

## Out of Scope

- `02-requirements-engineering/` cluster — separate spec if desired
- `04-development-artifacts/` through `09-governance-compliance/` — too far downstream
- Modifying `skills/ux-standards.md` (SaaS implementation patterns)
- Touching `engine/`, `domains/`, `templates/`, `projects/`
- Modifying any of the existing references in `05-ux-specification/references/`
- Creating new skills

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Shared doc duplicates social-media's `docs/ux-foundations.md` | Engine-local copies are simpler to maintain than cross-engine imports. SRS version is broader (6 sections vs 4) — adds BMC, maturity, working memory, affordance, scope levels |
| `04-lean-canvas` already has its own conventions | Append-only mapping; do not overwrite Lean Canvas methodology |
| `05-ux-specification` may already cover some material | New section augments existing references; doesn't replace any of the 6 reference files |
| `07-premium-product-positioning` may conflict with website-skills' premium-ui-ux-design | Cross-reference website-skills' Category 8 explicitly; both engines apply the same gate, scored independently per artifact |

## Success Criteria

- Shared doc created with 6 sections at `docs/ux-foundations.md`
- 5 SKILL.md files contain "added 2026-05-04" sections
- Each new section cites the appropriate sections of the shared doc
- Existing `references/` content in `05-ux-specification/` untouched
- One commit on `main` covers all 6 file edits

## Approval

Approved by user 2026-05-04 ("yes" after design presentation).

## Next Step

Invoke `superpowers:writing-plans` to create the implementation plan.

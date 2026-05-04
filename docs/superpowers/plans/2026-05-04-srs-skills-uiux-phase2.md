# SRS-Skills UX/UI Phase 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 1 shared UX-foundations doc + 5 inline SKILL.md appends across the UX-specification + Strategic-vision clusters of the srs-skills engine, integrating Branson persona discipline + working-memory + 4-stage affordance, Levy's Four Tenets + Top-10 anti-patterns + Business Model Canvas, Synechron's 5 outcomes + 5-level UX maturity, and Deacon's 3 levels of UX scope.

**Architecture:** Documentation/skill upgrade — markdown only. Each task creates or extends a markdown file. Verification = file exists, expected line count, grep markers pass. One commit at end.

**Tech Stack:** Markdown only. Sources at `C:\Users\BIRDC\.claude\skills\book-extractions\` (read-only). Targets at `C:\wamp64\www\srs-skills\`.

**Spec:** `C:\wamp64\www\srs-skills\docs\superpowers\specs\2026-05-04-srs-skills-uiux-phase2-design.md`

**Repo state:** `C:\wamp64\www\srs-skills` is a git repo on `main`.

---

## File Map

```
srs-skills/
├── docs/
│   └── ux-foundations.md                                                (create)
├── 01-strategic-vision/
│   ├── 01-prd-generation/SKILL.md                                       (extend)
│   ├── 03-vision-statement/SKILL.md                                     (extend)
│   ├── 04-lean-canvas/SKILL.md                                          (extend)
│   └── 07-premium-product-positioning/SKILL.md                          (extend)
└── 03-design-documentation/
    └── 05-ux-specification/SKILL.md                                     (extend)
```

**6 file edits: 1 new + 5 extended.**

---

## Conventions

- Each SKILL.md append marks itself: `## <Section Title> (added 2026-05-04 from <book>)`
- Shared doc starts with provenance citing canonical extractions at `C:\Users\BIRDC\.claude\skills\book-extractions\`
- Do NOT modify existing frontmatter; do NOT introduce emojis
- Append at end-of-file with leading blank line

---

## Task 1: Create `docs/ux-foundations.md`

**Files:**
- Create: `C:\wamp64\www\srs-skills\docs\ux-foundations.md`

- [ ] **Step 1: Write the file with this EXACT content:**

```markdown
# UX Foundations — srs-skills
**Source:** Distilled from canonical extractions at `C:\Users\BIRDC\.claude\skills\book-extractions\` (Phase 1 deliverable, 2026-05-04).
**Used by:** 03-design-documentation/05-ux-specification, 01-strategic-vision/01-prd-generation, 01-strategic-vision/03-vision-statement, 01-strategic-vision/04-lean-canvas, 01-strategic-vision/07-premium-product-positioning.

---

## Section 1 — Branson Persona Discipline

Source: `branson-ux-ui-design-extraction.md` Section 4.

### Stories at the centre
Personas are people, not stick figures. "You can't recount to a very remarkable anecdote about a stick figure." Every persona must include a name, a setting, and a quotable problem statement.

### Edge cases — the "edge-cased to death" rule
Cooper: better to have a much smaller percentage be elated than the entire public half-satisfied. Use the persona to defuse feature creep:
- "Sorry, but Noah won't need X."
- "But somebody might."
- "Maybe, but we are designing for Noah, not 'somebody.'"

### The "designing for themselves" trap
Designers (and AI) substitute themselves into the persona's seat. Specific, richly characterized personas prevent this.

### Choosing the Essential Persona
- The Essential Persona's design must at least work for the others.
- A design specifically for any other persona may not work for the Essential.
- Don't average users — averaging produces a Mr. Potato Head.

### Mechanics — required attributes
- First and last name (fictional)
- Photograph (volunteer match or stock)
- Demographics: age, education, ethnicity
- Goals & motivations
- Social, technical, physical environment
- Pain points & stress points
- Short biography: work role, main tasks, use stories, problems, concerns, biggest obstacles

### "Clingy" personas
Personas need visibility across the team — not just the design team. Tactics: posters, trading cards, T-shirts, coffee cups, screen wallpapers, full-size cardboard cutouts. Cisco-style action-figure dolls posed in work settings.

---

## Section 2 — Levy Four Tenets + Top-10 Anti-Patterns + Business Model Canvas

Source: `levy-ux-strategy-extraction.md` Parts I–III.

### The formula
> **UX Strategy = Business Strategy + Value Innovation + Validated User Research + Killer UX Design**

Simultaneously-spinning plates, not phases.

### Four misinterpretations to reject at kickoff
1. "UX strategy is a North Star" — agile/iterative, not fixed
2. "UX strategy is a strategic way to do UX design" — strategy ≠ design
3. "UX strategy is just product strategy" — spans ecosystems
4. "UX strategy is closely tied to brand strategy" — UX trumps brand

### Top-10 Not-UX-Strategies (anti-patterns)
1. A killer idea
2. A laundry list of features
3. A thoroughly researched plan with no need for customer feedback
4. Permutation of trending buzzwords
5. Generic motivational statements
6. Arrogant statement from an expert
7. Hypothesis with non-validated risky assumptions
8. Grandiose vision misaligned with capabilities
9. Vague Hallmark-card affirmation
10. The North Star

### Business Model Canvas — 9 building blocks (Osterwalder & Pigneur)

**UX strategy intersects most strongly with the bolded blocks:**

1. **Customer segments** — Who are the customers? Behaviors? Needs? Goals?
2. **Value propositions** — What value do we promise to deliver?
3. Channels — How do we reach the segment? Online or offline?
4. Customer relationships — How do we acquire and retain?
5. Revenue streams — How does the business earn revenue?
6. Key resources — Strategic assets (content, capital, patents)
7. Key activities — What unique things does the business do?
8. Key partnerships — Suppliers/partners required
9. Cost structure — Fixed vs variable; cutting frills vs premium

A premium project's BMC must explicitly answer blocks 1 + 2 with evidence (validated personas + tested value props), not just hypothesis.

---

## Section 3 — Synechron 5 Outcomes + 5-Level UX Maturity Checklist

Source: `enterprise-ux-financial-insurance-extraction.md` Parts I, VIII, IX.

### Five mandatory outcomes (launch gate)

| # | Outcome | Verification |
|---|---|---|
| 1 | **Useful** | Built for target audience; addresses real needs |
| 2 | **Easy to use** | Minimal/no training; first-task success without coaching |
| 3 | **Efficient** | Fast access; task time benchmarked |
| 4 | **Pleasing** | Right aesthetics; ≥ 4/5 first-impression rating |
| 5 | **Accessible** | ADA / Section 508 / WCAG 2.1 AA verified |

**Rule:** All 5 must hit. 4-of-5 disqualifies premium pricing. One No = no launch.

### Five maturity levels (process gate)

- **Level 0 — No Design:** ignored entirely
- **Level 1 — Uninformed UI Styling:** cosmetic only
- **Level 2 — Style & Color (Problem Solving):** UX approach defined; goals integrated
- **Level 3 — UX Design:** flow drives behavior; problems solved effectively
- **Level 4 — Experience Design (Innovation):** wow factor; design thinking process

**Premium-pricing gate:** Level 3 minimum required for premium claims; Level 4 for top-tier.

### Activity-by-Level matrix (which activities required at which level)

Activities required at Level 3 (UX Design) and above:
- Problem Definition & Business Objective
- Stakeholder Discussions / Interviews
- Success Criteria
- User Research (qualitative + quantitative)
- Competitor Analysis
- User Interviews
- Personas
- User Journeys
- Information Architecture
- Navigation Flow
- Task Flows
- Wireframes (low-fi + high-fi)
- Clickable Prototype
- Visual Design Mockups
- Heuristic / Expert Evaluation

Required at Level 4 (Experience Design) additionally:
- Experience Maps
- Mood Boards
- Usability Testing
- Test Cases & Scenarios

Required at all levels:
- Design Templates & Style Guides
- ADA / Section 508 Compliance

---

## Section 4 — Branson Working Memory + 4-Stage Cognitive Affordance

Source: `branson-ux-ui-design-extraction.md` Sections 5 + 6.

### Working memory laws (use as NFR templates)

**Miller's 7 ± 2 (1956):** working memory holds about 7 chunks (often less), for ~30 seconds. Practice can extend; interruption shrinks fast.

**Web/app implications (NFR templates):**
- Primary navigation: ≤ 7 items
- Visible form fields per step: ≤ 7
- Numeric strings (phone, account): chunked at 3-3-4 or 4-3
- Avoid stacking: don't ask the user to remember earlier-page values mid-flow

**Sweller's cognitive load theory:** the load on working memory at a moment in time. Cascading menus and long flows risk overload. Plot working-memory load over time; whenever it reaches zero = task closure. Drive frequent closure.

**Stacking:** when one task interrupts another, current context goes on a memory stack. Stacks are small, short, defective. Save state automatically; surface a clear "back to where you were" affordance after interruption.

**Recognition over recall:** computers are better at memory; humans at pattern recognition. Let the user choose from a list rather than recall from memory. For experienced users, provide keyboard shortcuts (Ctrl-S etc.) as physical-affordance bypasses.

### 4-stage cognitive affordance discipline (use as UX-spec rules)

For every important interactive element, walk through 4 stages. Failure at any stage breaks the chain.

#### Stage 1: Presence
Does the affordance exist at all? Show which UI object to manipulate, how to manipulate, active defaults, system state, modes. Avoid "clueless consent" — user proceeds without understanding consequences.

#### Stage 2: Visibility / Perceivability
Can it be seen at all? Is it actually rendered? Occluded? Small/peripheral/lost in clutter?

**Anti-pattern (must fail design review):** "Where the hell is the sign in?" — small indistinct sign-in box mixed with other items.

#### Stage 3: Recognizability
Once visible, can it be detected/identified without searching? Location within central focus of attention; contrast, size, layout complexity; separation from background.

**Anti-pattern:** status lines / message lines at the very top or very bottom — notoriously unnoticed.

#### Stage 4: Intelligibility
Once recognized, is the content understandable? Legibility (font, size, weight, color, contrast); meaning of the words once read.

### Use as a design-review heuristic
Walk every primary CTA through Presence → Visibility → Recognizability → Intelligibility. Any missing stage = redesign required before launch.

---

## Section 5 — Deacon 3 Levels of UX Scope

Source: `deacon-ux-ui-strategy-extraction.md` Section 2.

Every PRD, vision statement, and UX spec must declare which level the engagement targets:

### Level 1: Single Interaction
One product/device for one specific task. Examples: receiving help on phone, filing a claim on insurance website, completing a checkout. **Most engagements live here (~80%).**

### Level 2: Journey
Multiple interactive channels/devices to achieve a goal over time. Examples: email confirmation → check mail → log in → text reminder → return to site. **Opt-in upgrade**, requires multi-channel/automation work.

### Level 3: Relationship
Overall experience with the organization (customer experience level). Examples: research → buy → use → renew → recommend. **Rare**; requires brand + service design + customer success integration. Treat as a separate engagement bundle.

### The scoping rule
**Declare the level explicitly in every PRD/vision/spec.** Mismatched expectations between client (Relationship-level) and team (Single-Interaction-level) cause most "scope creep" problems.

---

## Section 6 — Cross-References

### Canonical extractions (source-of-truth)
- `branson-ux-ui-design-extraction.md`
- `levy-ux-strategy-extraction.md`
- `enterprise-ux-financial-insurance-extraction.md`
- `deacon-ux-ui-strategy-extraction.md`
- `fekeshazi-pm-ux-guide-extraction.md`

All located at `C:\Users\BIRDC\.claude\skills\book-extractions\`.

### Skill consumption map
- `03-design-documentation/05-ux-specification/` — uses Sections 1, 3, 4, 5 (deepest integration)
- `01-strategic-vision/01-prd-generation/` — uses Sections 1 + 2 (personas + tenets check)
- `01-strategic-vision/03-vision-statement/` — uses Section 2 (Top-10 anti-pattern filter)
- `01-strategic-vision/04-lean-canvas/` — uses Section 2 (Lean Canvas ↔ BMC mapping)
- `01-strategic-vision/07-premium-product-positioning/` — uses Section 3 (5 outcomes + maturity gate)

### Phase 2 spec
This document was created as part of the Phase 2 upgrade described in `docs/superpowers/specs/2026-05-04-srs-skills-uiux-phase2-design.md`.

### Cross-engine references
- `website-skills/skills/design-quality-score/` — Category 8 (UX Maturity scoring) parallels Section 3
- `social-media-skills/docs/ux-foundations.md` — same shape, narrower scope
```

- [ ] **Step 2: Verify**

Run: `wc -l "C:/wamp64/www/srs-skills/docs/ux-foundations.md"`
Expected: ≥ 200 lines.

Run: `grep -c "^## Section " "C:/wamp64/www/srs-skills/docs/ux-foundations.md"`
Expected: 6.

---

## Task 2: Append to `03-design-documentation/05-ux-specification/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\srs-skills\03-design-documentation\05-ux-specification\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/srs-skills/03-design-documentation/05-ux-specification/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## UX foundations integration (added 2026-05-04 from Branson + Synechron + Deacon)

Canonical reference: `docs/ux-foundations.md` (engine-local, 6 sections).

This skill consumes the broadest portion of the foundations doc. Required reading before producing a UX specification:

- **Section 1 (Branson personas)** — every UX spec's persona section must declare an Essential Persona and pass the Mechanics floor (name, demographics, goals, environment, pain points, stress points)
- **Section 3 (Synechron 5 outcomes + maturity)** — every UX spec must declare which maturity level (Level 3 minimum for premium) and document the 5 outcomes as launch criteria
- **Section 4 (working memory + 4-stage affordance)** — used as NFR templates and design-review heuristics
- **Section 5 (Deacon 3 levels of scope)** — every UX spec declares which scope level it targets

### Required NFR templates (drawn from Section 4)

The UX spec's non-functional-requirements section must include, where applicable:

- **List-length cap** — primary navigation, dropdowns, and primary action lists ≤ 7 items (Miller). If more required, chunk into groups.
- **Form-field-per-step cap** — ≤ 7 visible fields per step. Longer forms split into multi-step flows with explicit progress and saved state.
- **Cognitive-load minimization** — plot working-memory load across the primary user task; identify task-closure points; redesign if load never reaches zero across the flow.
- **Stacking-safe interruption recovery** — every multi-step flow auto-saves state; every page that can be interrupted has a "back to where you were" affordance.

### Required affordance audit (drawn from Section 4)

For every primary CTA listed in the UX spec, document Yes/No on each of:
- **Presence** — does the affordance exist?
- **Visibility/Perceivability** — can it be seen at first glance?
- **Recognizability** — can it be detected without searching?
- **Intelligibility** — is the meaning clear once read?

Any No = redesign required before launch.

### Required scope declaration (drawn from Section 5)

The UX spec opens with one sentence: "This specification targets [Single Interaction / Journey / Relationship] level UX scope, per Deacon's 3-level model."

### Required maturity declaration (drawn from Section 3)

The UX spec opens with one sentence: "This specification operates at UX Maturity Level [3 / 4], per the Synechron 5-level model. Premium-pricing claims require Level 3 minimum."

### Existing references unchanged

This section augments — does not replace — the existing references in `references/`: `design-handoff.md`, `design-system-guide.md`, `information-architecture.md`, `premium-ui-ux-specification.md`, `usability-testing.md`, `wireframing-standards.md`. Use them as before; the new section adds upstream discipline.
```

- [ ] **Step 3: Verify**

Run: `grep -c "UX foundations integration (added 2026-05-04" "C:/wamp64/www/srs-skills/03-design-documentation/05-ux-specification/SKILL.md"`
Expected: 1.

Run: `grep -c "Required NFR templates\|Required affordance audit\|Required scope declaration\|Required maturity declaration" "C:/wamp64/www/srs-skills/03-design-documentation/05-ux-specification/SKILL.md"`
Expected: ≥ 4.

---

## Task 3: Append to `01-strategic-vision/01-prd-generation/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\srs-skills\01-strategic-vision\01-prd-generation\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/srs-skills/01-strategic-vision/01-prd-generation/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Strategic foundations check (added 2026-05-04 from Levy + Branson)

Canonical reference: `docs/ux-foundations.md` Sections 1 and 2.

Three checks before producing or finalizing the PRD:

### 1. Four Tenets check (Levy)

Verify the upstream artifacts and PRD scope contain evidence for all four tenets:

| Tenet | PRD section | Pass criterion |
|---|---|---|
| **Business Strategy** | Strategic context / problem statement | Value proposition declared with revenue model |
| **Value Innovation** | Differentiation / competitive context | Specific differentiation vs named competitors, not generic claims |
| **Validated User Research** | User segments / personas | Personas cite real research, not pure hypothesis |
| **Killer UX Design** | Success criteria / UX requirements | UX outcomes specified, not implied |

If any tenet lacks evidence, the PRD is "speculative" — return to upstream stage rather than ship a polished but unfounded PRD.

### 2. Persona discipline (Branson, Section 1)

The PRD's persona section must:
- Declare ONE Essential Persona per primary user role (no averaging)
- Include the full Mechanics floor (name, demographics, goals, environment, pain points, stress points)
- Use specific, named personas in feature-justification arguments — "Persona X needs Y" — not "users want Y"

### 3. Field-of-Dreams flag (Levy)

If the PRD contains no validated user research and no plan to acquire it, mark the PRD itself as "speculative." Speculative PRDs cannot be priced as execution engagements; they must precede a discovery engagement. Document the speculative-status banner at the top of the PRD.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Strategic foundations check (added 2026-05-04" "C:/wamp64/www/srs-skills/01-strategic-vision/01-prd-generation/SKILL.md"`
Expected: 1.

Run: `grep -c "Four Tenets check\|Persona discipline\|Field-of-Dreams flag" "C:/wamp64/www/srs-skills/01-strategic-vision/01-prd-generation/SKILL.md"`
Expected: ≥ 3.

---

## Task 4: Append to `01-strategic-vision/03-vision-statement/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\srs-skills\01-strategic-vision\03-vision-statement\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/srs-skills/01-strategic-vision/03-vision-statement/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Vision-statement filter (added 2026-05-04 from Levy)

Canonical reference: `docs/ux-foundations.md` Section 2 (Top-10 Not-UX-Strategies).

Reject any vision statement that matches one of Levy's anti-patterns. Most common SRS-context failures, in order of frequency:

### #10 — The North Star
**Symptom:** "Be the [Uber / Airbnb / Stripe] of [industry]." No operational meaning. Reads like a slogan.
**Fix:** rewrite to describe the *change* the product creates in the user's life — what specifically becomes possible that wasn't before?

### #9 — The Hallmark-card affirmation
**Symptom:** "Deliver excellence, innovation, and customer delight." Too vague to act on. Cannot be operationalized into requirements.
**Fix:** name the specific user, the specific change, the specific evidence that the change has happened.

### #4 — The buzzword permutation
**Symptom:** "AI-powered Web3 platform for the metaverse." Trends concatenated. No customer in the sentence.
**Fix:** drop every buzzword that doesn't directly describe what the user does or experiences.

### #5 — Generic motivational statement
**Symptom:** "Empower every team, every day, everywhere." Could fit any product.
**Fix:** make it falsifiable — what would prove this is happening, and what would prove it isn't?

### #1 — The killer idea
**Symptom:** "Our killer idea is X." Idea-as-vision. No persona, no problem, no validation.
**Fix:** rewrite as user-problem + observable outcome.

### Procedure when a draft matches an anti-pattern

Return to the interview/discovery stage. Do not polish the prose of an anti-pattern vision statement; the underlying thinking has not happened yet. Document the rejection and the path back in the project log so the rework is auditable.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Vision-statement filter (added 2026-05-04" "C:/wamp64/www/srs-skills/01-strategic-vision/03-vision-statement/SKILL.md"`
Expected: 1.

Run: `grep -c "North Star\|Hallmark-card\|buzzword permutation" "C:/wamp64/www/srs-skills/01-strategic-vision/03-vision-statement/SKILL.md"`
Expected: ≥ 3.

---

## Task 5: Append to `01-strategic-vision/04-lean-canvas/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\srs-skills\01-strategic-vision\04-lean-canvas\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/srs-skills/01-strategic-vision/04-lean-canvas/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Lean Canvas ↔ Business Model Canvas mapping (added 2026-05-04 from Levy)

Canonical reference: `docs/ux-foundations.md` Section 2 (Business Model Canvas — 9 building blocks).

This is an **additive mapping** — it does not replace the existing Lean Canvas methodology in this skill. Lean Canvas (Maurya) and Osterwalder's BMC are complementary tools; both have their place.

### Block-by-block mapping

| Lean Canvas | Business Model Canvas | UX-strategy intersection |
|---|---|---|
| Problem | (covered indirectly by Customer Segments + Value Propositions) | Where personas' pain points live |
| Customer Segments | **Customer Segments** | **Bolded — UX strategy primary intersection** |
| Unique Value Proposition | **Value Propositions** | **Bolded — UX strategy primary intersection** |
| Solution | (BMC has no direct equivalent — implicit in Value Propositions + Key Activities) | Where UX-design tenet 4 (Killer UX Design) lives |
| Channels | Channels | Where omni-channel UX questions live |
| Revenue Streams | Revenue Streams | — |
| Cost Structure | Cost Structure | — |
| Key Metrics | (BMC has no direct equivalent) | Where Levy's Funnel Matrix metrics fit |
| Unfair Advantage | (covered in Key Resources + Key Partnerships) | Where Value Innovation differentiation lives |
| (no equivalent) | Customer Relationships | How acquisition + retention happen |
| (no equivalent) | Key Resources | Strategic assets — content, capital, patents |
| (no equivalent) | Key Activities | What unique things the business does |
| (no equivalent) | Key Partnerships | Suppliers and partners |

### When to use which

- **Lean Canvas:** early-stage startup, validating problem-solution fit
- **Business Model Canvas:** established product, articulating full operating model for strategic alignment
- **Both:** premium engagements where the team wants both fast-validation framing AND complete strategic articulation

### UX-strategy implication (per Levy)

UX strategy intersects most strongly with Customer Segments + Value Propositions on the BMC — exactly the same blocks where Lean Canvas places Customer Segments + Unique Value Proposition. Whichever canvas you use, those two blocks are where validated user research must produce evidence, not hypothesis.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Lean Canvas ↔ Business Model Canvas mapping" "C:/wamp64/www/srs-skills/01-strategic-vision/04-lean-canvas/SKILL.md"`
Expected: 1.

Run: `grep -c "Customer Segments\|Value Propositions\|UX-strategy intersection" "C:/wamp64/www/srs-skills/01-strategic-vision/04-lean-canvas/SKILL.md"`
Expected: ≥ 3.

---

## Task 6: Append to `01-strategic-vision/07-premium-product-positioning/SKILL.md`

**Files:**
- Modify: `C:\wamp64\www\srs-skills\01-strategic-vision\07-premium-product-positioning\SKILL.md`

- [ ] **Step 1: Inspect end of file**

Run: `tail -5 "C:/wamp64/www/srs-skills/01-strategic-vision/07-premium-product-positioning/SKILL.md"`

- [ ] **Step 2: Append exactly this content (with leading blank line)**

```markdown

## Premium positioning gate (added 2026-05-04 from Synechron Enterprise UX)

Canonical reference: `docs/ux-foundations.md` Section 3 (5 outcomes + 5-level UX maturity).

Premium-pricing claims must pass two gates: outcomes (launch gate) and maturity (process gate). Both are required; neither alone is sufficient.

### Gate 1 — Five Outcomes (launch gate)

A premium positioning document must declare evidence-based pass on ALL FIVE outcomes:

| Outcome | Evidence required |
|---|---|
| **Useful** | Persona-validated; tested against documented goals |
| **Easy to use** | First-task success in usability test without coaching |
| **Efficient** | Task time benchmarked against competitor or prior baseline |
| **Pleasing** | Subjective rating ≥ 4/5 on initial-impression test |
| **Accessible** | ADA / Section 508 / WCAG 2.1 AA verified |

**4-of-5 disqualifies premium pricing.** Drop the positioning to standard tier and re-engage when the missing outcome has evidence.

### Gate 2 — UX Maturity Level (process gate)

A premium claim must operate at UX Maturity Level 3 (UX Design) minimum. Top-tier (luxury, regulated, mission-critical) requires Level 4 (Experience Design).

Required documented activities at Level 3:
- Problem definition + business objective
- Stakeholder discussions (interview notes)
- Success criteria (signed)
- User research (qualitative + quantitative)
- Competitor analysis matrix
- Personas (named, with goals + pain points)
- User journeys (per primary persona)
- Information architecture (sitemap + navigation flow)
- Wireframes (low-fi + high-fi)
- Clickable prototype (per crucial scenarios)
- Heuristic evaluation report
- Visual design mockups
- ADA / Section 508 verification

Level 4 additionally requires: experience maps, mood boards, usability testing, test cases & scenarios.

### Cross-engine references

- `website-skills/skills/design-quality-score/` — Category 8 (UX Maturity) scores the same gate independently per artifact. Same project may carry separate scores in each engine.
- `website-skills/skills/premium-ui-ux-design/references/enterprise-five-outcomes.md` — same outcomes, applied to website templates.

### Procedure when either gate fails

Do not re-position the product as premium. Either:
1. Close the gap (add the missing evidence or activities) and re-engage, OR
2. Re-position at a lower tier (standard / mid-tier) honestly

Premium claims that fail either gate damage credibility on first audit.
```

- [ ] **Step 3: Verify**

Run: `grep -c "Premium positioning gate (added 2026-05-04" "C:/wamp64/www/srs-skills/01-strategic-vision/07-premium-product-positioning/SKILL.md"`
Expected: 1.

Run: `grep -c "Gate 1\|Gate 2\|Five Outcomes\|UX Maturity Level" "C:/wamp64/www/srs-skills/01-strategic-vision/07-premium-product-positioning/SKILL.md"`
Expected: ≥ 4.

---

## Task 7: Single commit for all 6 file edits

- [ ] **Step 1: Stage and commit**

```bash
cd "C:/wamp64/www/srs-skills"
git add docs/ux-foundations.md \
  03-design-documentation/05-ux-specification/SKILL.md \
  01-strategic-vision/01-prd-generation/SKILL.md \
  01-strategic-vision/03-vision-statement/SKILL.md \
  01-strategic-vision/04-lean-canvas/SKILL.md \
  01-strategic-vision/07-premium-product-positioning/SKILL.md
git status
git commit -m "$(cat <<'EOF'
srs-skills: integrate UX foundations into UX-spec + Strategic-vision clusters

Phase 2 UX upgrade per spec 2026-05-04-srs-skills-uiux-phase2-design.md.
- New shared doc docs/ux-foundations.md (6 sections: Branson personas, Levy tenets + Top-10 + BMC, Synechron 5 outcomes + maturity, working memory + 4-stage affordance, Deacon 3 levels of scope, cross-references)
- 05-ux-specification: UX foundations integration with NFR templates, affordance audit, scope declaration, maturity declaration
- 01-prd-generation: Four Tenets check + persona discipline + Field-of-Dreams flag
- 03-vision-statement: Top-10 anti-pattern filter
- 04-lean-canvas: Lean Canvas ↔ BMC mapping
- 07-premium-product-positioning: 5 outcomes (launch) + maturity (process) gate

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git log -1 --stat
```

Expected: 6 files changed (1 new + 5 modify).

---

## Task 8: End-to-end verification

- [ ] **Step 1: Files exist + extension markers present**

Run:

```bash
cd "C:/wamp64/www/srs-skills"
test -f docs/ux-foundations.md && echo "OK: docs/ux-foundations.md"
echo "--- Files with 2026-05-04 marker ---"
grep -l "added 2026-05-04" \
  03-design-documentation/05-ux-specification/SKILL.md \
  01-strategic-vision/01-prd-generation/SKILL.md \
  01-strategic-vision/03-vision-statement/SKILL.md \
  01-strategic-vision/04-lean-canvas/SKILL.md \
  01-strategic-vision/07-premium-product-positioning/SKILL.md
```

Expected: 1 OK line + 5 file paths.

- [ ] **Step 2: Concept references per SKILL.md**

```bash
cd "C:/wamp64/www/srs-skills"
for f in \
  03-design-documentation/05-ux-specification/SKILL.md \
  01-strategic-vision/01-prd-generation/SKILL.md \
  01-strategic-vision/03-vision-statement/SKILL.md \
  01-strategic-vision/04-lean-canvas/SKILL.md \
  01-strategic-vision/07-premium-product-positioning/SKILL.md \
; do n=$(grep -ciE "ux-foundations|Branson|Levy|Synechron|Four Tenets|Five Outcomes|Essential Persona|Top-10|Maturity|Business Model Canvas" "$f"); echo "$f: $n matches"; done
```

Expected: 5 lines, each with count ≥ 1.

- [ ] **Step 3: Final report**

Print one paragraph:
- Number of new files (expect 1)
- Number of files extended (expect 5)
- Commit SHA
- Any verification step that did not match expectation

If any verification fails, do not declare complete; create follow-up task.

---

## Self-Review

**1. Spec coverage:**
- Shared doc with 6 sections → Task 1 ✓
- 05-ux-specification append (Sections 1, 3, 4, 5) → Task 2 ✓
- 01-prd-generation append (Section 1 + 2) → Task 3 ✓
- 03-vision-statement append (Section 2 Top-10) → Task 4 ✓
- 04-lean-canvas append (Section 2 BMC mapping) → Task 5 ✓
- 07-premium-product-positioning append (Section 3 outcomes + maturity) → Task 6 ✓
- Single commit → Task 7 ✓
- Verification → Task 8 ✓

**2. Placeholder scan:** No "TBD"/"TODO"/"implement later" present. Each section has full content.

**3. Type consistency:** Section names ("Section 1" through "Section 6") match between shared doc and citing SKILL.md files. "Essential Persona" / "Five Outcomes" / "Four Tenets" capitalized consistently. File paths consistent.

No issues to fix.

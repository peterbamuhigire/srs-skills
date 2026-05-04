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

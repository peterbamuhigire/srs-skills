# SRS-Skills UX/UI Phase 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 1 shared UX-foundations doc + 5 inline SKILL.md appends across the UX-specification + Strategic-vision clusters of the srs-skills engine, integrating Branson persona discipline + working-memory + 4-stage affordance, Levy's Four Tenets + Top-10 anti-patterns + Business Model Canvas, Synechron's 5 outcomes + 5-level UX maturity, and Deacon's 3 levels of UX scope.

**Architecture:** Documentation/skill upgrade — markdown only. Each task creates or extends a markdown file. Verification = file exists, expected line count, grep markers pass. One commit at end.

**Tech Stack:** Markdown only. Read-only sources in the [Chwezi Dev Engine](https://github.com/peterbamuhigire/chwezi-dev-engine) `book-extractions/` directory; targets in this SRS engine repository.

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
- Shared doc starts with provenance citing the Chwezi Dev Engine's canonical `book-extractions/` directory
- Do NOT modify existing frontmatter; do NOT introduce emojis
- Append at end-of-file with leading blank line

---

## Task 1: Create `docs/ux-foundations.md`

**Files:**
- Create: `C:\wamp64\www\srs-skills\docs\ux-foundations.md`

- [ ] **Step 1: Write the file.**

> Historical note (2026-09-24): the embedded file content that stood here was a book-by-book digest and has been removed under the "Never store book extractions" rule. `docs/ux-foundations.md` was retired the same day; its knowledge now lives, rewritten by task and with currentness corrections, in `03-design-documentation/05-ux-specification/references/ux-requirements-foundations.md`.

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

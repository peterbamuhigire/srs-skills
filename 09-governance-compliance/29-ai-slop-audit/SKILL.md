---
name: 29-ai-slop-audit
description: Analyse, evaluate, and audit any artefact for AI slop and score it. AUTO-RUNS whenever the user asks to analyse, review, evaluate, audit, critique, or "de-slop" any SRS, technical spec, requirement, user story, acceptance criterion, design doc, test doc, ADR, document, system, codebase, app, website, business plan, or proposal — or asks "does this look AI-generated?". Produces a graded slop report: per-marker findings with severity, evidence, and a concrete fix. Pairs with 28-anti-ai-slop (which prevents slop during production).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
  priority: high
  source: digital-research-engine / ai-slop-detector (2026-06-07), verified per EVIDENCE-AUDIT.md
---

# AI Slop Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

The detector. Given any artefact, it decides how much it reads as AI slop, names exactly why, and says how to fix each finding. Production-side prevention is the companion `28-anti-ai-slop` skill. In this engine it runs as the final gate after the Phase 09 audit and feeds the V&V fail tags.

## Cadence — run after each major iteration

This is the default mode: run this audit after **each major iteration of work on the project** — each drafted SRS section, each completed design or test document, each finished module or feature, each significant revision, each phase or milestone — before moving to the next. Log the verdict each time, mapping any blocking finding to its V&V fail tag. If the verdict is **F (Blocked)**, do not progress to the next section or iteration until the blocking findings are fixed. Treat it like a test suite that runs at every checkpoint, not a one-time final review. This is in addition to running on request and as the final pre-`.docx` gate; the companion `28-anti-ai-slop` skill runs continuously *during* authoring, and this audit runs *at each checkpoint* to catch what slipped through.

## Use When

- The user asks to **analyse, review, evaluate, audit, critique, score, or de-slop** an SRS, spec, requirement set, user story, acceptance criterion, HLD/LLD, API/database design, test document, ADR, runbook, document, system, app, website, business plan, proposal, or codebase.
- The user asks "is this AI slop / does this look AI-generated / why does this requirement feel off?".
- As the final gate before a generated `.docx` deliverable ships.

## Do Not Use When

- The artefact has not been drafted yet — use `28-anti-ai-slop` during production instead.
- The request is purely a factual lookup with no artefact to evaluate.

## What slop is (the yardstick)

Low-quality content produced in quantity by AI and pushed at people who did not ask for it (Merriam-Webster 2025 WOTY, verified). Three diagnostic properties (Kommers et al., arXiv 2601.06060): **superficial competence, asymmetric effort, mass producibility**. The human tell: **absence of intent**. You are measuring how strongly an artefact exhibits these. In an SRS the sharpest signal is a requirement no one could write a deterministic test against.

## Audit method — layered, cheapest first

### Step 1 — Identify artefact type and load the right checklist
Map the artefact to one or more domains: SRS/spec, user story/acceptance criteria, design doc, test doc, written content (EN/FR), UI/UX, app/product, image/video, code. A "system" or "project" usually spans several — audit each layer.

### Step 2 — Automated gates (🤖, machine-checkable) — any hit is hard evidence
Run every applicable check; a hit on a **blocking** marker (✗) fails the artefact outright.

**SRS / spec / requirements**
- ✗ 🤖 Untestable requirement — any "shall be fast/intuitive/reliable/robust/scalable/user-friendly" with no IEEE-982.1 / ISO 25010 metric attached (`[SMART-FAIL]`).
- ✗ 🤖 Hallucinated API, endpoint, schema field, library, or standard clause — resolve each against a real source or the project `_context/`.
- ✗ 🤖 Placeholder section with no content: empty "Challenges and Future Prospects", "Future Enhancements", "TBD", or "lorem"-style filler heading.
- 🤖 Missing edge/error/empty-case specification where `_context/` lists such a case — state-coverage gap (`[V&V-FAIL]`).
- 🤖 Functional requirement that is not stimulus-response, or whose expected result is not a deterministic oracle (`[VERIFIABILITY-FAIL]`).
- 🤖 Requirement with no traceability to a business goal or to a test case (`[TRACE-GAP]`).
- 🤖 Undefined acronym or domain term not in `_context/glossary.md` (`[GLOSSARY-GAP]`).

**User stories / acceptance criteria**
- 🤖 Generic "as a user" persona instead of a named stakeholder; abstract Given-When-Then with no concrete data values; missing negative/boundary criteria; INVEST violations.

**Written content**
- 🤖 Focal-word density — delve/tapestry/realm/navigate/underscore/pivotal/intricate/leverage etc. >2 per 500 words.
- 🤖 Em-dash density >1 per paragraph; reflexive rule-of-three; "it's not X, it's Y" repetition; uniform 15–25-word sentences (low burstiness).
- 🤖 Transition clichés ("in today's fast-paced world", "let's dive in", "in conclusion").
- 🤖 Mechanical formatting: Title-Case headers, excess bold, decorative emoji, leftover tool markup ("oaicite", "contentReference").
- ✗ 🤖 Broken/fake citations: dead URLs, invalid DOI/ISBN, fabricated stats, utm_source params copied in.
- French: "plongeons dans", "il est important de noter que", "force est de constater", filler connectors.

**UI/UX**
- 🤖 Indigo/purple-gradient default (HSL 250–280°, sat 70%+); Inter/Roboto/Poppins-only; uniform border-radius; glassmorphism; gradient text; shadcn coloured card-border.
- ✗ 🤖 Dark-mode/body contrast <4.5:1 (WCAG fail).
- ✗ 🤖 Missing states (error/empty/loading/focus/disabled) — state-coverage audit.

**Code (specs drive code — audit the implementation a spec produced)**
- ✗ 🤖 Hallucinated/uninstallable imports & packages (slopsquatting; Spracklen et al. USENIX Security 2025 measured a 19.7% package-hallucination rate) — resolve every dependency against its registry.
- ✗ 🤖 Hardcoded secrets; SQL built by string interpolation; `innerHTML = userInput` (XSS); insecure defaults (Veracode: 45% of AI code samples carried an OWASP flaw, XSS in 86%, log-injection in 88%).
- 🤖 Placeholder stubs/TODO/`NotImplementedError`/`...` in shipped code; dead code; duplication (GitClear 8.3% in 2020 → 12.3% in 2024); bare-except; cross-language constructs; inconsistent style in one file; tautological tests (`assert true`).

**Image/video**
- 🤖 Missing/contradictory C2PA provenance; SynthID absence (Google-only — absence ≠ authentic); ELA/JPEG-forensics anomalies.

### Step 3 — Structural score (🤖) → 0–100 "genericness"
Combine burstiness, focal-word density, duplication, and template-similarity into a single genericness score. Higher = more slop-like. Report the score and its drivers.

### Step 4 — Human-judgement review (👁) — the checklist no tool replaces
- 👁 **Substance:** what does this requirement assert or decide that required real engineering work? If nothing — slop.
- 👁 **Intent / authored voice:** is there a stated rationale or trade-off, or is it relentlessly positive and viewpoint-free?
- 👁 **Specificity:** real named `_context/` entities, actors, thresholds, and data — or generic placeholders?
- 👁 **Hard parts:** are errors, edge cases, failure modes, risks, and counter-arguments handled?
- 👁 **Visuals:** anatomy (hands/eyes/teeth), "AI sheen", garbled text-in-image, impossible geometry, video "boiling"/lip-sync.
- 👁 **Product/app:** wrapper with nothing added? fleeceware/dark-pattern billing? deceptive AI claims? fake reviews?
- 👁 **Domain-specific (per artefact):**
  - *SRS/spec:* vague requirements, placeholder "Challenges and Future Prospects" sections, missing edge/error specs, hallucinated APIs, untestable ("shall be reliable") requirements with no metric, requirements with no traceability or test oracle.
  - *User story/acceptance criteria:* generic personas, happy-path-only criteria, no boundary or negative cases, non-INVEST stories.
  - *Design doc:* generic boxes with no named components, undocumented trade-offs, no failure-mode/timeout handling, invented standard clauses.
  - *Test doc:* "verify it works" with no deterministic oracle, coverage that does not map to requirement IDs.
  - *Business plan:* fabricated market stats, generic TAM/SAM filler, no authored strategy, "studies show" without a named study.
  - *Proposal/EoI:* inflated superlatives, hollow analogies, unverifiable claims, no visible logic (evidence→warrant→implication).
  - *Blog/social:* engagement-bait, no lived experience, clichés, AI-sheen imagery.

## Scoring & verdict

Aggregate into a grade:

| Grade | Meaning | Trigger |
|---|---|---|
| **A — Clean** | No blocking hits; genericness low; substance & intent present | ship |
| **B — Minor slop** | A few automated hits, no blockers; some genericness | fix listed items |
| **C — Slopy** | Multiple automated hits or weak substance/intent | rework before ship |
| **F — Blocked** | Any ✗ blocker (hallucinated fact/citation/package/API, untestable requirement, secret, WCAG fail, missing states, empty placeholder section) OR no substance at all | do not ship |

## Output format (the audit report)

```
# AI Slop Audit — <artefact name> — <date>
Verdict: <A/B/C/F>   Genericness score: <0-100>
Artefact type(s): <...>

## Blocking findings (X) — must fix
- [marker] <what was found> - evidence: <quote/line/URL/requirement ID> - fix: <concrete action> - V&V tag: <[SMART-FAIL]/[V&V-FAIL]/...>

## Slop findings (by severity)
- [marker] <finding> - evidence: <...> - fix: <...>

## What's good (so it isn't stripped in the fix)
- <substantive, specific, authored elements worth keeping>

## Recommended next step
- <rework / targeted fixes / ship>
```

## Discipline (anti-hallucination — applies to the audit itself)

- Every finding cites concrete evidence from the artefact (a quote, a line number, a requirement ID, a colour value, a screenshot region, a URL). No finding without evidence.
- Do not invent a flaw to pad the report. "This artefact is clean" is a valid, wanted verdict.
- Mark inferences "(inference)"; never present a guess as a measured fact.

## Anti-Patterns

- Reporting a banned word while ignoring the untestable requirement underneath it — grade on substance first.
- Failing an artefact without a concrete fix and a mapped V&V tag.
- Padding the report with low-value lexical nits to look thorough.

## Outputs

- A graded slop report in the format above, with each blocking finding mapped to a V&V fail tag for the originating skill to remediate.
- A ship / targeted-fix / rework recommendation.

## See also

- `28-anti-ai-slop` — prevention companion (write/design/code so slop never appears).
- `02-audit-report` and the V&V SOP in `CLAUDE.md` — this audit feeds the same fail-tag remediation loop.

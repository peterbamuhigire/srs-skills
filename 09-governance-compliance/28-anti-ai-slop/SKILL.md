---
name: 28-anti-ai-slop
description: MANDATORY pre-ship guardrail. Run on EVERY generated SRS, technical spec, user story, acceptance criterion, design document, test document, ADR, or code artefact before it is delivered, so the output cannot be recognised as "AI slop". Carries the verified slop definition, the seven universal markers each paired with an avoidance rule, the banned-vocabulary list merged with this engine's prohibited-adjective rule, the SRS/spec avoidance block, and a ship-gate checklist. Load first; it overrides stylistic preferences but defers to IEEE/ISO grounding.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
  priority: critical
  source: digital-research-engine / ai-slop-detector (2026-06-07), verified per EVIDENCE-AUDIT.md
---

# Anti AI Slop
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

The guardrail every generated artefact passes before it ships. Detection lives in the companion `29-ai-slop-audit` skill; this skill governs **production** — writing the SRS, spec, design doc, test doc, or code so slop never appears in the first place. It sits on top of this engine's V&V SOP and IEEE/ISO grounding, never below them: a requirement that is verifiable but generic still fails here.

## Real-time application (this is a LIVE constraint, not only a final gate)

Apply these rules **continuously, as you author** — to every requirement, section, acceptance criterion, design statement, and line of code at the moment it is written, not only in one pass at the end. The moment you reach for a banned word, a subjective adjective with no IEEE-982.1 metric, a generic placeholder, an unverified figure, a hallucinated API, or a template default, stop and correct it in place. The ship-gate checklist at the end is the final confirmation, not the first time these rules are consulted. If you are mid-draft and notice slop accumulating — an empty "Challenges and Future Prospects" heading, a "shall be reliable" with no threshold, a requirement with no test oracle — fix it then; do not defer to a cleanup pass.

## Use When

- Before delivering any generated SRS section, PRD, user story, acceptance criterion, HLD/LLD, API spec, database design, test strategy/plan/case, runbook, ADR, or shipped code.
- As the last gate after the Phase 09 audit and before the consultant sees the draft (PRIME "Inspect" step).
- Whenever you suspect a section reads as filler, hedged, or template-shaped rather than authored against real `_context/`.

## Do Not Use When

- You are still gathering `_context/` inputs; this skill checks finished drafts, not raw notes.
- The artefact is a private scratch file that will never reach a person or downstream skill.

## What "AI slop" is (so you know what you are preventing)

**AI slop** is low-quality content produced in quantity by generative AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Its three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified):

1. **Superficial competence** — looks fine on the surface, no substance underneath.
2. **Asymmetric effort** — cheap to produce, costly for a human to read, review, or fix.
3. **Mass producibility** — generated at volume.

The human tell named in every domain studied: **absence of intent** — the sense that no one *meant* anything by it. In an SRS this shows up as requirements no engineer could build a test against. Your job is to re-internalise effort (specificity, verification, authored decisions) before the artefact reaches a person.

Two verified data points anchor why this matters for spec-driven code. Spracklen et al. (USENIX Security 2025) measured a 19.7% package-hallucination rate in AI-generated code — invented dependencies that a spec citing a non-existent API will propagate downstream. GitClear found code-duplication share rising from 8.3% (2020) to 12.3% (2024), the kind of copy-paste bulk that asymmetric-effort slop produces.

## The seven universal guardrails (apply to EVERY output)

| # | Marker to prevent | Avoidance rule you MUST follow |
|---|---|---|
| **U1** | Genericness / averaging | Every section carries ≥1 concrete, named, domain-specific element (a real `_context/` entity, a measured threshold, a named actor, a stimulus-response pair) a generic template could not produce. Forbid tool defaults and stock requirement boilerplate. |
| **U2** | Superficial competence | Enforce a substance floor: include a requirement, constraint, test oracle, or decision the artefact could not exist without. A "Challenges and Future Prospects" section with no named challenge is filler — cut or replace it. |
| **U3** | Confident wrongness / hallucination | Verify every statistic, citation, standard clause, named entity, API, schema field, and dependency before emit. Cite at the point of claim. Flag uncertainty with `[CONTEXT-GAP]` rather than inventing. Never specify an API or library that does not exist. |
| **U4** | Volume over substance | Prefer one verifiable requirement over three hollow ones. Do not pad to reach a section length. Honour the Minimum-Length Directive. |
| **U5** | Absence of authored voice / intent | State the engineering rationale, trade-off, or named decision behind a requirement. Ban relentless positivity and sycophancy. Record real trade-offs in an ADR rather than smoothing them over. |
| **U6** | Skipping the hard parts | Specify the error, edge, empty, and failure cases, the counter-arguments, and the design constraints — not just the happy-path requirement. Every edge case in `_context/` must trace to a requirement. |
| **U7** | Mechanical uniformity | Vary sentence length and structure. Break the template. No rule-of-three reflex, no "it's not X, it's Y" formula, no em-dash flood. |

## Banned / high-risk vocabulary (the lexical tells)

These words and constructions are statistically over-produced by LLMs (FSU/COLING-2025; PubMed "delve" +400%). **Do not use them as default register.** A word here is allowed only when it is the genuinely precise term, never as filler.

This list merges with this engine's standing prohibition (CLAUDE.md Principle 7): never use **fast, intuitive, reliable, robust, seamless,** or any subjective adjective without its defined IEEE-982.1 metric. Replace with a measurable threshold: "response time ≤ 500 ms at P95 under normal load."

- **Words:** delve, tapestry, realm, landscape (as metaphor), navigate (as metaphor), leverage, foster, harness, synergy, embark, robust, vibrant, holistic, seamless, intricate, commendable, meticulous, pivotal, underscore, testament, resonate, elevate, paramount, unwavering, multifaceted.
- **Engine-specific banned adjectives (no metric = no use):** fast, intuitive, reliable, scalable, performant, user-friendly, cutting-edge, state-of-the-art, enterprise-grade — each is a `[SMART-FAIL]` unless paired with a specific IEEE-982.1 / ISO 25010 metric.
- **Phrases:** "in today's fast-paced world", "in the ever-evolving landscape of", "it is important to note that", "it's worth mentioning", "let's dive in", "here's the kicker", "at the end of the day", "in conclusion", "studies show" (without a named study), "Challenges and Future Prospects" (as an empty placeholder heading).
- **Constructions:** the "it's not just X, it's Y" antithesis; reflexive rule-of-three lists; em-dash used to manufacture drama; relentless triplet adjectives ("robust, scalable, and reliable").
- **French equivalents** (for Francophone output): "plongeons dans", "il est important de noter que", "force est de constater", "dans un monde en constante évolution", "par ailleurs/de plus/en outre" as filler connectors, "au cœur de", "pierre angulaire".

## Drop-in guardrail block (inherit in dependent skills)

```
ANTI-SLOP GUARDRAIL (inherit in every output):
1. SPECIFICITY FLOOR — every section carries >=1 concrete, named, domain-specific
   element from _context/. No tool defaults, no placeholder requirement copy.
2. VERIFY-BEFORE-EMIT — no statistic, citation, standard clause, named entity,
   API, schema field, or dependency ships unverified; cite at point of claim;
   flag uncertainty with [CONTEXT-GAP].
3. AUTHORED VOICE — state the engineering rationale / trade-off; no relentless
   positivity, no sycophancy; route real trade-offs into an ADR.
4. COVER THE HARD PARTS — error/edge/empty/failure cases, counter-arguments,
   design constraints; every edge case traces to a requirement.
5. BREAK THE TEMPLATE — vary rhythm and structure; forbid default aesthetics,
   the banned-vocabulary list, and undefined subjective adjectives.
```

## Domain-specific avoidance (load the relevant block for the output type)

- **SRS / technical spec (primary):** no vague requirement ("the system shall be fast/intuitive/reliable") — every quality attribute carries an IEEE-982.1 / ISO 25010 metric and threshold; no empty "Challenges and Future Prospects" or "Future Enhancements" placeholder section; every functional requirement uses a stimulus-response pattern with a deterministic test oracle; every edge, error, and empty case in `_context/` has a matching requirement; no hallucinated API, endpoint, schema field, or library — resolve each against a real source; every requirement traces back to a business goal and forward to a test case.
- **User stories / acceptance criteria:** real named persona from `_context/stakeholders.md`, not "as a user"; Given-When-Then with concrete data values, not abstractions; INVEST-checked; negative and boundary criteria present, not only the happy path.
- **Design docs (HLD/LLD/API/DB):** named components and real data flows over generic boxes; documented trade-off per significant decision (link the ADR); failure modes, timeouts, and back-pressure specified; API examples use real field names and types; no invented standard clause.
- **Test docs:** each test case has a deterministic pass/fail oracle, not "verify it works"; coverage maps to specific requirement IDs; negative, boundary, and error-path cases included.
- **Written content:** no focal-word clusters; vary sentence length (mix 3–10 with 25–40 words); ≤1 em-dash/paragraph; no "in conclusion"; specific examples over generic claims; a stated point of view.
- **UI/UX:** no indigo-500/purple-gradient default; no Inter-only typography; intentional (not uniform) radius/shadow; WCAG contrast ≥4.5:1; design ALL states (error/empty/loading/focus/disabled); real testimonials only.
- **Apps/product:** add genuine value over any wrapped API; transparent pricing + in-app cancel; no deceptive AI-capability claims; least-privilege permissions.
- **Code (specs drive code):** verify every imported package exists (slopsquatting — Spracklen et al. measured 19.7% hallucinated packages); no placeholder stubs/TODOs/`NotImplementedError`/`...` in shipped code; parameterised queries (never string-built SQL); no `innerHTML = userInput` (XSS); no hardcoded secrets; idiomatic and deduplicated (GitClear duplication 8.3%→12.3%); real tests, never `assert true`; cover the edge cases the spec named. Veracode found 45% of AI-generated code samples introduced an OWASP-relevant flaw (XSS present in 86%, log-injection in 88%) — verify, do not trust.
- **Image/video:** real specimens only; check anatomy/text/physics; avoid the "AI sheen"; attach provenance (C2PA) where it matters.

## Ship gate (run before delivering ANY output)

- [ ] Every section has ≥1 concrete, named, specific element from `_context/` (U1/U2).
- [ ] Every stat, quote, citation, standard clause, named entity, API, schema field, dependency verified (U3).
- [ ] No banned vocabulary used as filler; no subjective adjective without its IEEE-982.1 metric; scanned the output for both lists above.
- [ ] The output states an engineering rationale / trade-off; no sycophancy (U5).
- [ ] Error/edge/empty/failure cases and counter-arguments addressed; every `_context/` edge case traces to a requirement (U6).
- [ ] Sentence length and structure varied; no rule-of-three reflex, no antithesis formula, no em-dash flood (U7).
- [ ] Every functional requirement is stimulus-response with a deterministic test oracle; no empty "Challenges and Future Prospects" section.
- [ ] Output type's domain block applied.
- [ ] When in doubt, run the `29-ai-slop-audit` skill on the draft.

If any box is unticked, the output is not ready to ship.

## Anti-Patterns

- Treating the banned-vocabulary scan as cosmetic while leaving requirements untestable underneath — slop is a substance failure first, a lexical one second.
- Padding an SRS to a target length with restated obvious statements, violating the Minimum-Length Directive.
- Inventing an API, endpoint, or library to fill a `[CONTEXT-GAP]` instead of flagging it.

## Outputs

- A ship/no-ship decision plus the ticked gate checklist appended to the draft's review notes.
- Any unresolved item promoted to the matching V&V fail tag (`[V&V-FAIL]`, `[SMART-FAIL]`, `[CONTEXT-GAP]`, `[TRACE-GAP]`).

## See also

- `29-ai-slop-audit` — the detection/evaluation/audit companion (analyse any artefact for slop and score it).
- `02-audit-report` and the V&V SOP in `CLAUDE.md` — apply on top of this; IEEE/ISO grounding precedes style.

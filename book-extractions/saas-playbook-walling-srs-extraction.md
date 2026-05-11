# The SaaS Playbook (Rob Walling) — SRS-Engine Extraction

**Source:** Rob Walling, Jessie Kwak, Jason Cohen, *The SaaS Playbook: Build a Multimillion Dollar Startup Without Venture Capital.*

**Lens:** Which product, MVP-scoping, pricing, moat, and growth documents must the engine produce so a bootstrapped/founder-led SaaS gets a world-class SDLC documentation set?

## One-line takeaway

A bootstrapped SaaS is built on **disciplined feature-prioritisation, structured pricing, deliberate moat-building, and a documented growth funnel** — the engine should produce explicit documents for each of these decisions rather than letting them live in the founder's head.

## Distinctive documentation surface

### 1. MVP / Stair-Step scoping doc

The "stair-step method" (Step 1 = one organic channel, Step 2 = rinse & repeat, Step 3 = standalone SaaS) and Walling's "Achieving Escape Velocity" framework drive a **SaaS MVP & Stair-Step Scoping Document** — what's in / out for v1, what defers to v2, the single channel chosen, the success-threshold (e.g., $10K MRR before adding features).

### 2. Feature-request triage doc

The book gives a 3-question test ("use case? what % of customers? fits vision?") for every feature request. The engine should produce a **Feature Request Triage Spec** — categorisation (crackpot / no-brainer / in-between), questions to apply, decision log, link to roadmap.

### 3. Competition response doc

Walling distinguishes the "four signals" to watch on competition (high-level updates, deals lost, low-level details, funding). A **Competitive Posture Document** specifies which signals to watch, the thresholds for action, and the response playbook.

### 4. Moat-building doc

The book's moat taxonomy: integrations/network-effects, brand, owned channels, switching costs, anti-moats (false moats: unique features). The engine should produce a **Moat & Defensibility Plan** in Phase 01.

### 5. Pricing structure doc

Detailed guidance: value metric, feature gating, freemium pros/cons, credit-card-up-front trade-offs, Rule-of-10 for price raises, grandfathering policy, three-plan structure (Indie / Pro / Studio / Enterprise pattern). This becomes the **Pricing & Packaging Spec** template's core content.

### 6. Marketing-funnel doc

High-touch funnel, first-touch → email opt-in → activation. The engine should produce a **Lifecycle/Funnel Map** with stages, conversion targets, and the experiments planned at each stage.

### 7. Vertical/translation/whitelabel decision docs

Each is treated as an explicit decision with a documented trade-off — engine should expose them as **ADR templates** in the SaaS ADR catalogue.

## Documentation patterns the book recommends

- Make every product decision a **document** with a recorded rationale (especially "no" decisions).
- Pricing is a system, not a number — document tiers, value metrics, feature gates, expansion mechanics, grandfathering, raise-cadence.
- Treat moat-building as an explicit roadmap line item.
- Distinguish real moats from false moats (unique features = false moat).

## Implications for the SDLC-Docs-Engine

1. Add Phase 01 skill **`10-saas-mvp-scoping-doc`** (stair-step, escape-velocity, scoping cuts).
2. Add Phase 01 skill **`11-saas-moat-and-defensibility-plan`**.
3. Reinforce `01-strategic-vision/01-prd-generation` with a feature-triage and competition-signal addendum.
4. Drive content of `saas-pricing-and-packaging-spec-template.md` from Ch.7-8 of this book.
5. Add Phase 09 ADR templates: pricing-raise ADR, freemium-yes/no ADR, whitelabel ADR, vertical-expansion ADR.

## Source mapping

- "Stair Step Method" / "Escape Velocity" → MVP scoping skill.
- "Asking the Right Questions" / "In-Betweens" → feature-triage spec.
- "How Can I Build a Moat?" → Moat & Defensibility Plan.
- "How Should I Structure My Pricing?" / "Expansion Revenue" / "Should I Offer Freemium?" / "When Should I Raise Prices?" → Pricing & Packaging template content.
- "Marketing Funnels" / "High-Touch Funnel" → Lifecycle/Funnel Map.

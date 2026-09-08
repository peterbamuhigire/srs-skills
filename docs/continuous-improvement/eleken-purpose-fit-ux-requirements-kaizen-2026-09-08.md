# SRS engine Kaizen: purpose-fit premium UX requirements

Assessment date: 2026-09-08
Repository: `C:\wamp64\www\srs-skills`
Scope: Kaizen governance, UX specification, design-to-requirement traceability, and handoff to design/web implementation
Owner: SRS engine maintainer

## Verdict

The SRS engine now translates targeted UX improvements and premium design intent into testable,
client-specific requirements. It requires actor/job/friction context, a purpose-fit thesis,
authored decisions, critical states, accessibility/responsive expectations, measures, and
traceable handoff evidence. It explicitly prevents “make it like Stripe” or “make it premium” from
becoming an untestable requirement.

The change is structurally implemented. A specific product's user outcome, render, and field
evidence remain conditional until a project supplies them.

```text
raw_diagnostic_score: 61/100 (provisional structural engine diagnostic)
reported_audit_score: 61/100
confidence: medium
hard_gates: conditional
improvement_target: 95/100
```

The portfolio cap remains `min(raw, 65)`; this is not a product-readiness score.

## Currentness and source disposition

| Source/claim | Accessed | Disposition |
|---|---|---|
| Eleken UX improvements article | 2026-09-08 | Tier 5 practitioner input; converted into requirement prompts, not accepted as proof or universal thresholds |
| Eleken dashboard examples article | 2026-09-08 | Tier 5 practitioner input; converted into signal/explanation/action/detail questions |
| Eleken “Making It Like Stripe” article | 2026-09-08 | Tier 5 practitioner input; converted into anti-imitation and purpose-fit authorship rules |
| Accessibility/platform claims | 2026-09-08 | Must be verified by the applicable primary source at project time; unavailable project evidence remains `NOT_ASSESSED` |
| Model-currentness | 2026-09-08 | Official provider release/catalogue reviewed; model-policy helper returned `DRIFT: root model policy drift`; actual runtime/account entitlement `NOT_ASSESSED`; retain authorised Astra/Luna pins without repair |

## Baseline findings and actions

| ID | Gap and root cause | Standardised change | Acceptance evidence |
|---|---|---|---|
| SRS-UX-01 | The Kaizen route covered UX and handoff, but did not prescribe a compact purpose-fit evidence slice | Added `ux-friction-and-premium-experience-requirements.md` | Reference defines actor/job/friction/thesis/signature/state/measure/trace fields and stop condition |
| SRS-UX-02 | Dashboard requirements could drift into widget inventories or arbitrary visual thresholds | Added decision-surface contract: signal, explanation, action, detail, state, evidence | Reference decision table and worked requirement example are inspectable and reusable |
| SRS-UX-03 | UX specification did not make originality and premium fit explicit at the handoff boundary | Added the premium experience and originality addendum to `03-design-documentation/05-ux-specification/SKILL.md` | New addendum requires client context, thesis, authored decisions, states, measures, and proof or `NOT ASSESSED` |

## Design-to-SRS rules now taught

- Requirements begin with the actor's job and observed friction, not the desired screen.
- Import/upload patterns retain editable confirmation and recovery where extraction is uncertain.
- One-page versus wizard decisions are based on decision dependency and scanability, not fashion.
- Dashboard structure is tied to decisions and data meaning, not a generic card count or chart mix.
- Modals and side panels require depth justification and focus/return behaviour; deep work gets a route.
- Progress and loading requirements distinguish real stages, honest waiting, partial completion,
  failure, retry, cancellation, duplicate submission, and interruption.
- “Premium”, “artistic”, and “world-class” are translated into a thesis, signature choice, fit,
  state coverage, measurable quality, and retained evidence.

## Residual gaps and re-audit

- No client project was supplied, so no requirement set has been validated with user evidence or
  rendered implementation: `NOT ASSESSED`.
- Project-level standards, target platform accessibility, locale, and performance claims must be
  verified through the active domain and research routes.
- Re-audit after the first UX specification using the new addendum or by 2026-10-08.

# SaaS UX Scope And Costing For SRS

This reference is self-contained. It distills the user's supplied Design Studio UI/UX
articles into SRS-ready rules for selecting UX scope, documenting assumptions, and
calibrating cost expectations for Ugandan and regional buyers.

Sources used:

- https://www.designstudiouiux.com/blog/saas-ux-design-cost/
- https://www.designstudiouiux.com/blog/how-to-design-and-build-saas-product/
- Bank of Uganda May 2026 macro indicators for USD/UGX calibration.

## When To Load

Load this reference when an SRS, PRD, UX specification, proposal-to-SRS handoff, or
software development plan includes SaaS, dashboards, subscriptions, onboarding,
multi-role workflows, AI features, or UX/design effort estimation.

## UX Scope Decision Table

| Project Situation | UX Scope To Specify | SRS Implication |
|---|---|---|
| Founder MVP, one role, 3-5 features | Lean IA, core flows, clickable prototype for the activation path | Keep requirements narrow; defer non-core modules. |
| Multi-role SaaS MVP | Role-based IA, permissions, onboarding, key dashboards, component states | Add role matrix, state matrix, and UX acceptance criteria. |
| Existing app with adoption or churn issues | UX audit, analytics review, redesigned first-run and high-friction flows | Add measurable activation, time-to-value, and retention requirements. |
| Enterprise or regulated SaaS | Research plan, service blueprint, audit trails, approvals, compliance states | Add evidence, audit, accessibility, and sign-off requirements. |
| AI-enabled workflow | Prompt, streaming, source, confidence, review, override, failure recovery | Add human approval and traceable AI-output criteria. |

## Cost Inputs To Capture In SRS/SDP

The SRS should not promise a UX budget, but it must record cost drivers clearly enough
for estimating and proposal generation:

- User roles and permission tiers.
- Number of primary workflows and exception paths.
- Data density: lists, tables, reports, dashboards, exports, reconciliations.
- Research depth: stakeholder interviews, user interviews, usability testing, field study.
- Fidelity required: low, mid, high, clickable prototype, design system, production QA.
- Accessibility target and device/browser matrix.
- Integration and compliance risk.
- Launch deadline and review/sign-off complexity.

## Uganda-Calibrated Estimation Bands

Use these as scoping context, not as a promise inside the SRS. Convert at proposal time
using the current Bank of Uganda or bank selling rate. Public May 2026 USD/UGX sources
cluster around UGX 3,700-3,800 per USD, so avoid hard-coding a stale rate.

| UX Effort | Local SME / Startup | Established Ugandan Company | Export, Donor, Regional, Or Funded Buyer |
|---|---:|---:|---:|
| UX audit / discovery | $300-$900 | $900-$2,500 | $2,500-$6,000 |
| Lean MVP UX package | $1,200-$3,500 | $3,500-$8,000 | $8,000-$18,000 |
| Full UX specification / funded MVP | $3,500-$9,000 | $9,000-$20,000 | $20,000-$45,000 |
| Growth redesign / dashboard UX | $5,000-$15,000 | $15,000-$35,000 | $35,000-$75,000 |
| Enterprise SaaS UX programme | Rarely a fit | $25,000-$60,000 | $60,000-$150,000+ |

If the buyer budget is below the needed band, reduce scope and fidelity. Do not remove
states, accessibility, traceability, or handoff clarity from the remaining scope.

## Required SRS Sections

Add or update these sections in the UX specification:

- UX assumptions and exclusions.
- Role and permission UX matrix.
- Onboarding and time-to-value requirement.
- Pattern register for screens and workflows.
- Component state matrix.
- Usability metrics: activation, task completion, time-to-value, error recovery, day-7 retention where relevant.
- Design handoff evidence and acceptance criteria.

## Requirement Templates

`UX-SCOPE-###: The system shall support [user segment] completing [primary outcome] in
[flow/screen] with no more than [step/time/error threshold], verified by [prototype test,
usability test, analytics event, or acceptance test].`

`UX-COST-###: The project shall record UX cost drivers including roles, primary
workflows, data surfaces, fidelity, testing depth, accessibility target, and handoff
requirements before proposal finalization. Verification: estimation worksheet attached
to the SRS/SDP evidence bundle.`

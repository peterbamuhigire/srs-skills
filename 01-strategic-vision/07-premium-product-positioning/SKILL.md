---
name: 07-premium-product-positioning
description: Generate or review premium product positioning, PRD/SRS inputs, and design requirements for systems intended for premium, affluent, executive, enterprise, luxury, high-ticket, or elite users. Use when software must justify premium pricing, win high-level buyers, or feel materially better than ordinary alternatives.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Premium Product Positioning

<!-- dual-compat-start -->
## Use When

- In this SRS engine, use this skill by default for commercial products, client-facing systems, websites, SaaS, apps, dashboards, and strategy-led systems unless the work is explicitly internal and non-premium.
- The system is being designed for CEOs, investors, public-sector leaders, enterprise buyers, affluent customers, luxury/lifestyle users, or high-value SMEs.
- The product must support premium pricing, high-trust adoption, executive reporting, prestige, differentiation, or high-touch service.
- A PRD, SRS, UX specification, business case, or feature set needs premium-market discipline.

## Do Not Use When

- The work is purely internal and has no client-facing, buyer-facing, trust, adoption, service, or pricing implications.
- The requester explicitly wants commodity requirements for a non-premium product and accepts that this engine should treat the engagement as poor fit.

## Required Inputs

- Product context, target buyers/users, business model, pricing intent, and decision path.
- Current features, service model, proof assets, constraints, and success metrics.
- Any executive, enterprise, affluent, luxury, public-sector, or high-ticket buyer requirements.

## Workflow

1. Confirm the project is a premium-fit engagement. If it is cheap, vague, low-trust, or commodity-positioned, recommend narrowing the scope to a premium deliverable or declining the work.
2. Define the premium buyer and decision path: economic buyer, users, influencers, gatekeepers, risk owners, and proof required.
3. Convert positioning into requirements: outcomes, trust, speed, reliability, onboarding, reporting, support, service levels, governance, and proof.
4. Specify product quality signals: restrained interface, excellent copy, fast workflows, reliable data, branded outputs, polished notifications, and mature edge states.
5. Specify premium service requirements: onboarding, configuration, training, review meetings, escalation, success reporting, renewal/expansion, and account ownership.
6. Add pricing and sales-support requirements where relevant: packages, tiers, scope boundaries, ROI dashboards, proposal exports, and buyer-specific reports.
7. Run `references/premium-product-requirements-gate.md` before finalising the PRD, SRS, or design spec.

## Quality Standards

- Premium intent must become measurable requirements, acceptance criteria, service levels, reporting needs, governance, proof, and buyer experience.
- Do not use vague premium adjectives unless the SRS defines a verifiable threshold or review criterion.
- If the product cannot support premium positioning, document the product, service, proof, or operational gaps.

## Anti-Patterns

- Treating premium positioning as copywriting instead of requirements.
- Specifying luxury visual style while ignoring onboarding, reliability, support, reporting, and governance.
- Designing for high-value buyers without validating decision path, proof, risk, and service expectations.

## Outputs

- Premium positioning section for PRD/SRS/business case.
- Requirements and acceptance criteria for premium buyer experience.
- Feature priorities that support pricing power and high-level adoption.
- Risks, assumptions, and validation questions.

## References

- `references/premium-product-requirements-gate.md` - requirements gate for premium software and high-value users.
<!-- dual-compat-end -->

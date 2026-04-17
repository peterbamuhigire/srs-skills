---
title: "Lean Canvas — Key Assumptions"
---

# Key Assumptions Underlying the Lean Canvas

The Lean Canvas encodes hypotheses, not facts. The following assumptions are the highest-risk beliefs embedded in the model. Each must be validated before scaling decisions are made. Assumptions are listed in descending order of risk to the business model.

---

## Assumption 1 — Price Sensitivity: East African SMEs Will Pay UGX 250,000–2,500,000/Month for a SaaS ERP

**Statement of the assumption:**
Mid-sized organisations in Uganda with 5–500 employees will regard UGX 250,000–2,500,000/month as an acceptable and sustainable software expense when positioned as a replacement for Excel, QuickBooks, or manual processes. The Starter tier at UGX 250,000 is the critical price threshold — if this price point encounters significant resistance, the mass-market acquisition model fails.

**Minimum viable test:**
Run a 30-day pricing discovery sprint: conduct structured price-sensitivity interviews (Van Westendorp method) with 20 Finance Managers and business owners at target companies. Offer 10 Starter-tier trials at UGX 250,000/month and record conversion rate, time-to-pay, and unprompted objections. A conversion rate of ≥ 50% of trialists to paid confirms willingness to pay.

**If this assumption is false:**
The pricing model will require restructuring before Phase 1 launch. Options include: reducing the Starter price to UGX 150,000/month, extending the free trial to 30 days, or introducing a freemium tier (core modules free, add-ons paid). Revenue milestones for Phase 1 will need revision. Do not invest in sales team expansion until this assumption is confirmed.

---

## Assumption 2 — Usability: Zero-Training UX Is Achievable for Complex ERP Workflows

**Statement of the assumption:**
It is technically and design-feasibly possible to build ERP workflows — including double-entry bookkeeping, three-way purchase matching, payroll processing, and manufacturing Bill of Materials (BOM) management — such that a first-time user with no ERP training can complete the task successfully, unaided, within a reasonable time. The Golden Rule target of ≥ 85% unassisted task success is achievable within the scope of this platform's UX investment.

**Minimum viable test:**
Before Phase 1 launch, conduct moderated usability testing of the 5 highest-complexity workflows (payroll run, purchase order approval, EFRIS invoice submission, GL journal entry, stock physical count) with 10 participants who have no prior ERP experience. Measure unassisted task completion rate and time-on-task. If the ≥ 85% threshold is not met, iterate and retest. A failed second round triggers a redesign gate — no launch until the threshold is cleared.

**If this assumption is false:**
The Golden Rule — the platform's central value proposition and the primary differentiator from all competing ERPs — is unachievable at the feature set currently scoped. The product strategy will require re-scoping: either reduce the feature set to only workflows that pass the ≥ 85% threshold at launch, or acknowledge that some modules will require guided onboarding (which invalidates the "no consultants" promise for those modules). Competitor positioning claims must be revised accordingly.

---

## Assumption 3 — Integration Stability: The EFRIS Integration Will Be Reliable Enough for Daily Production Use

**Statement of the assumption:**
Uganda Revenue Authority (URA)'s EFRIS application programming interface (API) will be stable, well-documented, and available at ≥ 99.5% uptime during business hours. Longhorn ERP's fiscal compliance depends entirely on this integration for VAT invoice submission. An unreliable EFRIS API will create compliance risk for every tenant who issues VAT invoices.

**Minimum viable test:**
Integrate against the URA EFRIS sandbox API and run 1,000 automated test submissions over a 30-day period. Measure API availability, error rate, response time distribution, and error message clarity. Review the EFRIS developer documentation for completeness and currency. Interview 3 developers who have previously integrated EFRIS in production to capture known failure modes. If availability falls below 99% in testing, design an offline queue and retry mechanism before launch — not after.

**If this assumption is false:**
If EFRIS is unreliable or its API is insufficiently documented for automated integration, all tenants who issue VAT invoices face compliance exposure. Mitigation: build an offline queue that holds fiscal submissions and retries on recovery, with a manual override for emergency submissions. Prominently disclose the dependency in the Service Level Agreement (SLA) so tenants understand that EFRIS downtime is outside Chwezi's control. Escalate API reliability concerns to URA through formal channels.

---

## Assumption 4 — Payment Method: Mobile Money Is Sufficient for SaaS Billing in Uganda

**Statement of the assumption:**
The majority of Longhorn ERP's target customers — Ugandan SMEs — will be willing and able to pay their monthly subscription fee via MTN Mobile Money (MoMo) or Airtel Money. A significant proportion will not require bank transfer or card payment options to convert. Mobile money is the primary payment rail for the Ugandan SME market.

**Minimum viable test:**
During the pricing discovery sprint (see Assumption 1), ask each participant their preferred payment method for a recurring monthly software subscription. Record the distribution across mobile money, bank transfer, corporate credit card, and cheque. If fewer than 50% prefer mobile money as primary method, prioritise bank transfer integration ahead of the Phase 1 commercial launch. Test an end-to-end MTN MoMo recurring billing flow with 5 beta tenants and record payment success rate over 3 consecutive billing cycles.

**If this assumption is false:**
If mobile money proves unreliable or insufficient as a billing channel, the Billing & Subscriptions platform service must integrate bank transfer (direct debit or bank-to-bank) and optionally card payments (via Flutterwave or Pesapal) before Phase 1 launch. This adds integration scope, increases Payment Card Industry Data Security Standard (PCI DSS) compliance surface, and delays launch. Budget a 4-week contingency for payment gateway integration if this assumption fails validation.

---

## Assumption 5 — Self-Service: Small Businesses Will Complete Onboarding Without Consultant Support

**Statement of the assumption:**
Starter and Small Business tier customers — the primary self-signup segment — will successfully configure their tenant (chart of accounts, user setup, module activation, opening balances, and first live transaction) within 1 business day, unaided, using in-product guidance alone. No human consultant or Chwezi support agent will be required for the standard onboarding journey.

**Minimum viable test:**
Recruit 10 participants who match the target Starter/Small Business persona (office managers, bookkeepers, or business owners at 3–15-person companies with no prior ERP experience). Ask each to onboard a test tenant from signup through first invoice using only in-product guidance and the knowledge base. Measure time to first productive use (target: ≤ 1 business day), number of support tickets raised during onboarding, and self-reported confidence score at completion. A score of ≥ 70% completing unaided within 1 business day confirms the assumption.

**If this assumption is false:**
If self-service onboarding fails to achieve the 1-business-day target, the "no consultants" promise breaks down for the mass-market segment. Mitigation options in order of cost: (1) improve in-product onboarding flows and contextual help before launch; (2) introduce a mandatory live onboarding session for Starter/Small Business tiers (adds support cost but preserves the zero-consultant promise for ongoing use); (3) partner with a network of affordable local accountants trained on Longhorn ERP to deliver 2-hour onboarding sessions at a fixed fee below UGX 100,000. Option 3 is acceptable only if the session is positioned as optional and time-bounded — the platform must not require ongoing consultant dependency.

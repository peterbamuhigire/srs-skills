# Phase 10: Revenue Infrastructure, Business Growth & Scale

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Complete the revenue collection and growth infrastructure — the final layer that
converts excellent software into a self-sustaining, compounding business. Four new skills,
two stubs completed, and one security enhancement close every remaining gap.

**Architecture:** Stripe payments + subscription lifecycle + PLG tactics + SaaS metrics
form a complete revenue engine. Combined with Phase 8 (deploy) and Phase 9 (operate),
this phase makes the consultancy fully self-sufficient.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

> **EXECUTE THIS PHASE SECOND** after Phase 8. Without payment collection, deployed
> software cannot generate revenue. Cloud + Payments = minimum viable business.

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Integrate Stripe subscriptions into any PHP or Node.js SaaS application
- Handle the full subscription lifecycle: trial, activate, upgrade, downgrade, cancel, pause
- Process Stripe webhooks securely with signature verification and idempotency
- Implement dunning: smart retries, customer notifications, grace periods
- Calculate and display MRR, NRR, LTV:CAC, churn, and expansion revenue in real time
- Design freemium models with clear free→paid conversion triggers
- Build in-app upgrade prompts, activation flows, and viral referral loops
- Track product-qualified leads (PQLs) and act on usage signals
- Complete a restaurant POS with full floor management and kitchen display system
- Implement inventory management with barcode scanning, reorder triggers, and FIFO tracking
- Run A/B experiments on pricing pages, onboarding flows, and feature prompts

---

## Current Strengths — Revenue & Business Skills Already Built

### Billing & Accounting
- `saas-accounting-system` — Double-entry accounting engine, invoicing, reconciliation
- `ai-metering-billing` — Token ledger schema, per-user metering middleware, invoice generation
- `ai-saas-billing` — AI module gating, subscription tier enforcement, quota management
- `ai-cost-modeling` — Token economics, per-tenant margin modelling, pricing strategy

### Business Strategy
- `software-pricing-strategy` — Pricing models: value-based, usage-based, seat-based, hybrid
- `saas-business-metrics` — MRR, ARR, NRR, churn, LTV:CAC — business health metrics
- `software-business-models` — Platform, licensing, SaaS, marketplace revenue models
- `saas-erp-system-design` — Multi-module ERP: financial, HR, inventory, reporting
- `modular-saas-architecture` — Feature modules, plugin design, white-label patterns
- `multi-tenant-saas-architecture` — Tenant isolation, onboarding automation, billing per tenant

### Vertical UI (Partial)
- `pos-sales-ui-design` — Sales POS: item grid, cart, checkout, payment method selection
- `pos-restaurant-ui-standard` — **STUB — 39 lines. Complete this phase.**
- `inventory-management` — **STUB — 40 lines. Complete this phase.**

### Behavioral Design
- `habit-forming-products` — Hooked model: trigger, action, variable reward, investment
- `lean-ux-validation` — Validate before building: smoke tests, concierge, Wizard of Oz

---

## Build Tasks

### Task 1: Create `stripe-payments` skill

**File to create:** `C:\Users\Peter\.claude\skills\stripe-payments\SKILL.md`

**Read first:**
- Stripe Billing documentation — `stripe.com/docs/billing` (read fully — it is excellent)
- Stripe Webhooks guide — `stripe.com/docs/webhooks`
- Stripe Developer Blog — `stripe.dev` (production patterns)
- *Subscribed* — Tien Tzuo (business context)

**Content outline for SKILL.md (target: 400–470 lines):**

1. **Stripe Object Model** — Customer, Product, Price, Subscription, Invoice, PaymentIntent relationships
2. **Setup** — API keys (publishable vs secret), Stripe PHP SDK, Stripe Node.js SDK, environment config
3. **Products & Prices API** — creating products, one-time prices, recurring prices (monthly/annual)
4. **Checkout Sessions** — hosted payment page: `mode: subscription`, success/cancel URLs, metadata
5. **Customer Portal** — self-service subscription management: upgrade, downgrade, cancel, update card
6. **Webhook Architecture** — endpoint registration, signature verification (`Stripe-Signature`), idempotency
7. **Critical Webhook Events:**
   - `customer.subscription.created` → activate account features
   - `customer.subscription.updated` → handle plan change
   - `customer.subscription.deleted` → revoke access, send retention email
   - `invoice.payment_succeeded` → extend billing period, unlock usage quota
   - `invoice.payment_failed` → start dunning sequence
8. **Subscription States** — trialing, active, past_due, unpaid, cancelled, paused: state machine diagram
9. **Dunning Management** — Stripe Smart Retries, email at payment failure, grace period logic
10. **Tax Handling** — Stripe Tax automatic calculation, customer tax IDs, invoice tax lines
11. **Multi-Currency** — `currency` on Price, presentment currency, settlement currency
12. **Metered Billing** — usage records API: `stripe.subscriptionItems.createUsageRecord()`, thresholds
13. **Testing** — test card numbers, webhook CLI (`stripe listen`), clock simulation for renewals
14. **Security** — PCI compliance scope (redirect model = SAQ A), webhook secret rotation, key scoping
15. **PHP Integration Pattern** — complete subscription creation flow: checkout → webhook → DB update
16. **Node.js Integration Pattern** — Fastify route: webhook handler with idempotency key check

**Step 1:** Read Stripe Billing and Webhooks documentation fully.
**Step 2:** Create `SKILL.md`. Every section must have PHP or TypeScript code.
**Step 3:** Section 15 must include a complete, runnable PHP Stripe checkout flow.
**Step 4:** Section 16 must include a complete Node.js webhook handler with signature verification.
**Step 5:** Run `wc -l SKILL.md` — confirm 380–500 lines.
**Step 6:** Commit: `feat(skills): add stripe-payments skill — subscriptions + webhooks + dunning`

---

### Task 2: Create `subscription-billing` skill

**File to create:** `C:\Users\Peter\.claude\skills\subscription-billing\SKILL.md`

**Read first:**
- *Subscribed* — Tien Tzuo (full book)
- Stripe Billing advanced docs — `stripe.com/docs/billing/subscriptions/upgrade-downgrade`

**Content outline for SKILL.md (target: 370–440 lines):**

1. **Subscription Economy Fundamentals** — why subscriptions, recurring revenue mechanics, compounding
2. **Subscription States State Machine** — full diagram: free → trial → active → past_due → cancelled
3. **Trial-to-Paid Conversion** — trial length strategy, trial-end email sequence, soft vs hard paywall
4. **Plan Upgrade Flow** — proration calculation, immediate vs next-cycle upgrade, upgrade confirmation UI
5. **Plan Downgrade Flow** — proration credit, schedule for end-of-cycle, retention offer at downgrade
6. **Cancellation Flow** — exit intent detection, save offers (pause vs cancel), cancellation survey
7. **Pause & Resume** — subscription pause API, paused state UI, resume notification
8. **Billing Anchors** — billing cycle day, anniversary billing, calendar billing
9. **Revenue Recognition** — deferred revenue, monthly recognition for annual plans, revenue schedule
10. **MRR Calculation** — MRR from Stripe data, MRR movements (new, expansion, contraction, churn)
11. **Cohort Retention Analysis** — monthly cohort table: calculate retention by acquisition month
12. **Dunning Email Sequences** — Day 0 (soft fail) → Day 3 → Day 7 → Day 14 → Day 21 (cancel)
13. **Refund & Dispute Handling** — Stripe refund API, chargeback process, fraud prevention
14. **Billing Portal Customisation** — Stripe portal configuration: features to enable, branding
15. **Usage-Based Billing** — metering tiers, overage pricing, threshold alerts to customers
16. **Multi-Tenant Billing** — per-seat pricing, per-tenant billing account, consolidated invoicing

**Step 1:** Read *Subscribed* and Stripe upgrade/downgrade documentation.
**Step 2:** Create `SKILL.md` with all 16 sections.
**Step 3:** Include a complete MRR calculation SQL query.
**Step 4:** Include a dunning email sequence timeline diagram (ASCII art table).
**Step 5:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 6:** Commit: `feat(skills): add subscription-billing skill`

---

### Task 3: Create `product-led-growth` skill

**File to create:** `C:\Users\Peter\.claude\skills\product-led-growth\SKILL.md`

**Read first:**
- *Product-Led Growth* — Wes Bush (full book)
- *Escaping the Build Trap* — Melissa Perri (already in library)
- PostHog documentation — `posthog.com/docs`

**Content outline for SKILL.md (target: 360–430 lines):**

1. **PLG vs Sales-Led vs Marketing-Led** — when to choose PLG, unit economics of each model
2. **Freemium Design** — what to give free (core value), what to gate (advanced value), seat limits
3. **Product-Qualified Lead (PQL)** — definition: usage threshold that signals buying intent
4. **Activation Flow Design** — time-to-first-value target (< 10 minutes), activation checklist UI
5. **Empty State Design** — first-use empty state as onboarding: sample data, quick start guide
6. **In-App Upgrade Prompts** — contextual timing (hitting a limit), copy that focuses on value
7. **Viral Loops** — referral programs, shareable outputs, collaboration invites, public profiles
8. **NPS Collection** — in-app NPS survey timing (day 30 → quarterly), segmentation, follow-up
9. **Feature Flags for PLG** — gradual rollout, A/B test new onboarding, flag-gated premium features
10. **PLG Metrics** — activation rate, PQL conversion rate, expansion MRR, viral coefficient (K-factor)
11. **Product Analytics Setup** — PostHog: event capture, person properties, funnels, session replay
12. **Onboarding Checklist Pattern** — progressive disclosure, checklist completion as activation metric
13. **Self-Serve Documentation** — in-app help, contextual tooltips, knowledge base design
14. **PLG for B2B SaaS** — bottom-up adoption, champion user → team invite → executive buy-in
15. **Growth Loops vs Funnels** — sustainable compounding growth vs one-time acquisition

**Step 1:** Read *Product-Led Growth* (Bush) fully.
**Step 2:** Create `SKILL.md` with all 15 sections.
**Step 3:** Include a PostHog event capture TypeScript snippet.
**Step 4:** Include a PQL definition example with specific usage thresholds.
**Step 5:** Run `wc -l SKILL.md` — confirm 340–500 lines.
**Step 6:** Commit: `feat(skills): add product-led-growth skill`

---

### Task 4: Create `saas-growth-metrics` skill

**File to create:** `C:\Users\Peter\.claude\skills\saas-growth-metrics\SKILL.md`

**Read first:**
- *Hacking Growth* — Ellis & Brown
- PostHog documentation — `posthog.com/docs/analytics`
- Metabase documentation — `metabase.com/docs`

**Content outline for SKILL.md (target: 360–430 lines):**

1. **The SaaS Metrics Framework** — acquisition → activation → retention → revenue → referral (AARRR)
2. **MRR & ARR** — calculation from Stripe data, MRR movements dashboard, ARR projection
3. **Net Revenue Retention (NRR)** — formula, why NRR > 100% means growth without new customers
4. **Customer Lifetime Value (LTV)** — ARPU ÷ churn rate, LTV by acquisition channel
5. **Customer Acquisition Cost (CAC)** — fully-loaded CAC, CAC by channel, LTV:CAC ratio target (3:1)
6. **Churn Analysis** — logo churn vs revenue churn, churn by cohort, early warning signals
7. **Expansion Revenue** — upsell, cross-sell, seat expansion tracking in Stripe
8. **Funnel Analytics** — acquisition → signup → activation → paid: conversion rates at each step
9. **Cohort Retention Table** — building monthly retention cohorts from database events
10. **Feature Usage Analytics** — usage frequency, breadth (features used per user), depth (frequency)
11. **A/B Testing Framework** — hypothesis format, sample size calculator, statistical significance
12. **Revenue Forecasting** — simple linear model, cohort-based forecast, scenario modelling (bull/base/bear)
13. **Metrics Dashboard Design** — PostHog dashboard, Metabase for SQL-based metrics, embedding charts
14. **North Star Metric** — choosing one metric that captures product value delivery
15. **Growth Meeting Cadence** — weekly metrics review: what changed, why, what to do next

**Step 1:** Read *Hacking Growth* (Ellis & Brown).
**Step 2:** Create `SKILL.md` with all 15 sections.
**Step 3:** Include a SQL query for MRR calculation from a `subscriptions` table.
**Step 4:** Include a cohort retention SQL query example.
**Step 5:** Run `wc -l SKILL.md` — confirm 340–500 lines.
**Step 6:** Commit: `feat(skills): add saas-growth-metrics skill`

---

### Task 5: Complete `pos-restaurant-ui-standard` stub

**File to modify:** `C:\Users\Peter\.claude\skills\pos-restaurant-ui-standard\SKILL.md`

**Current state:** 39 lines — blocking the restaurant POS vertical.

**Read first:** `pos-sales-ui-design` skill (already built) for context and cross-reference.

**Content outline for SKILL.md (target: 360–440 lines):**

1. **Restaurant POS Flow Overview** — full transaction lifecycle: table seat → order → KDS → payment
2. **Floor Plan View** — table grid layout, table status colours (available/occupied/reserved/bill-pending)
3. **Order Entry Flow** — category tabs, item grid, item search, quantity input
4. **Modifier Selection** — modifier groups (mandatory vs optional), multi-select, modifier pricing
5. **Kitchen Display System (KDS)** — order ticket structure, prep time colour coding, bump on completion
6. **Table Management** — seat assignment, cover count, merge tables, table transfer
7. **Split Billing** — split by item (drag to seat), split by percentage, split by count
8. **Void & Refund Flow** — manager PIN confirmation, reason codes, void impact on KDS
9. **Receipt Design** — thermal receipt format, logo, itemised list, tax breakdown, QR for digital receipt
10. **End-of-Day Reconciliation** — shift close summary: sales by category, payment method breakdown
11. **Staff Management UI** — clock in/out, tip allocation, server performance summary
12. **Offline Mode** — local order queue, menu cache, sync on reconnect, conflict resolution
13. **Accessibility** — large touch targets (≥ 48×48dp), high-contrast theme for bright kitchen environments

**Step 1:** Rewrite `pos-restaurant-ui-standard/SKILL.md` using the content outline.
**Step 2:** Include Tailwind + React component sketches (not full implementations) for key screens.
**Step 3:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 4:** Commit: `feat(skills): complete pos-restaurant-ui-standard stub`

---

### Task 6: Complete `inventory-management` stub

**File to modify:** `C:\Users\Peter\.claude\skills\inventory-management\SKILL.md`

**Current state:** 40 lines — blocking pharmacy, logistics, and warehouse verticals.

**Content outline for SKILL.md (target: 360–440 lines):**

1. **Inventory Data Model** — Product, SKU, Location, StockLevel, StockMovement, Supplier schema
2. **Stock Level Tracking** — current stock, minimum level, maximum level, reorder point formula
3. **Reorder Triggers** — automatic purchase order generation at reorder point, email notification
4. **Barcode Scanning** — camera scanning (ML Kit / browser BarcodeDetector API), USB scanner HID input
5. **Goods Receive** — PO-matched receive, blind receive, quantity variance handling
6. **Stock Transfer** — inter-location transfer, transit state, confirmation on receipt
7. **Stock Adjustment** — write-off, write-up, adjustment reason codes, manager approval workflow
8. **Batch Operations** — bulk receive via CSV import, bulk adjustment, bulk transfer
9. **Stock-Take (Physical Count)** — cycle count workflow, full stock-take mode, variance report
10. **FIFO/LIFO/WEIGHTED AVERAGE** — cost accounting methods: implementation for each, when to use
11. **Expiry Date Tracking** — batch/lot numbers, FEFO (First Expired First Out), expiry alert schedule
12. **Supplier Management** — supplier catalog, lead time, minimum order quantity, PO workflow
13. **Multi-Location Inventory** — warehouse hierarchy, location codes (aisle-bay-shelf), zone picking
14. **Reporting** — stock valuation report, slow-moving items (no movement > 90 days), turnover rate
15. **Mobile Interface Patterns** — scan-first design, large input targets, offline-capable for warehouse

**Step 1:** Rewrite `inventory-management/SKILL.md` using the content outline.
**Step 2:** Include the SQL schema for the core inventory tables.
**Step 3:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 4:** Commit: `feat(skills): complete inventory-management stub`

---

### Task 7: Enhance `web-app-security-audit`

**File to modify:** `C:\Users\Peter\.claude\skills\web-app-security-audit\SKILL.md`

Add `## Network Security Layer` section covering:

- UFW firewall rules for a typical SaaS VPS: allow 80, 443, deny all else, SSH key-only
- iptables: PREROUTING for port redirects, rate limiting with `hashlimit`, logging DROP rules
- Cloudflare WAF: managed ruleset activation, custom rules (geo-block, IP allowlist for admin)
- ModSecurity (self-hosted WAF): OWASP Core Rule Set, paranoia level tuning, false-positive management
- Zero-trust principles: never trust network location, verify identity on every request
- VPN design for remote team access: WireGuard setup, peer configuration, split tunnelling
- DDoS mitigation: Cloudflare Magic Transit, rate limiting at CDN, SYN flood protection
- TLS certificate lifecycle: Let's Encrypt auto-renewal, HSTS preload, certificate transparency

**Step 1:** Append the new section.
**Step 2:** Include UFW rule commands and a WireGuard peer config snippet.
**Step 3:** Confirm file ≤ 500 lines.
**Step 4:** Commit: `feat(skills): enhance web-app-security-audit with network security layer`

---

## Phase Completion Checklist

- [ ] `stripe-payments` created — 380–500 lines; complete PHP + Node.js webhook handlers
- [ ] `subscription-billing` created — 350–500 lines; MRR SQL query + dunning timeline included
- [ ] `product-led-growth` created — 340–500 lines; PQL definition + PostHog snippet included
- [ ] `saas-growth-metrics` created — 340–500 lines; MRR SQL + cohort retention query included
- [ ] `pos-restaurant-ui-standard` rewritten — 350–500 lines; all 13 sections present
- [ ] `inventory-management` rewritten — 350–500 lines; SQL schema included
- [ ] `web-app-security-audit` enhanced with network security layer
- [ ] No skill file exceeds 500 lines
- [ ] `stripe-payments` cross-references `subscription-billing` and `saas-accounting-system`
- [ ] `product-led-growth` cross-references `saas-growth-metrics` and `saas-business-metrics`
- [ ] Git commit made: `feat(skills): complete phase-10 — revenue infrastructure & scale`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Subscribed: Why the Subscription Model Will Be Your Company's Future* | Tien Tzuo | Portfolio | ~$25 | **The subscription economy bible.** Why subscriptions compound, how to design billing models, the metrics that matter. Read before writing `subscription-billing`. |
| 2 | *Product-Led Growth: How to Build a Product That Sells Itself* | Wes Bush | Product-Led Alliance | ~$25 | The PLG playbook: freemium design, PQLs, activation, viral loops. Read before writing `product-led-growth`. |
| 3 | *Hacking Growth* | Sean Ellis & Morgan Brown | Currency | ~$30 | Growth experiments, funnel analysis, A/B testing framework, retention tactics. Feeds `saas-growth-metrics`. |
| 4 | *INSPIRED: How to Create Tech Products Customers Love* (2nd ed.) | Marty Cagan | Wiley | ~$30 | Product thinking, customer discovery, outcome-based roadmaps. Already in library — re-read for growth context. |
| 5 | *The SaaS Playbook* | Rob Walling | Rocketship.fm | ~$25 | Bootstrapped SaaS from zero to exit — pricing, growth, sales, operations for solo/small teams. |

### Free Resources

- Stripe Billing documentation — `stripe.com/docs/billing` — the authoritative Stripe billing reference; free and superb
- Stripe Webhooks guide — `stripe.com/docs/webhooks` — event types, signature verification, retry behaviour
- Stripe Developer Blog — `stripe.dev` — production patterns, edge cases, architectural decisions
- PostHog documentation — `posthog.com/docs` — product analytics, feature flags, A/B testing, session replay
- PostHog SQL analytics guide — `posthog.com/docs/hogql` — cohort queries and funnel analysis
- Metabase documentation — `metabase.com/docs` — self-hosted BI dashboard for SaaS metrics
- Baremetrics Open Benchmarks — `baremetrics.com/open` — SaaS industry benchmarks for MRR, churn, LTV

---

## Final State: World-Class SDLC Software Documentation Engine

When Phase 10 is complete, the skills library covers the entire arc of a client engagement:

```
PHASE 1  → Client talks to you → Discovery, proposal, business case
PHASE 2  → Agreement reached   → IEEE-compliant SRS, PRD, design docs
PHASE 3  → Architecture        → System design, data modeling, API design
PHASE 4  → Web development     → React/Next.js/TypeScript full-stack
PHASE 5  → Mobile development  → iOS, Android, KMP — all with AI/ML
PHASE 6  → AI features         → RAG, agents, analytics, cost metering
PHASE 7  → Quality assurance   → E2E tests, offline-first PWA, TDD
PHASE 8  → Infrastructure      → Docker, K8s, Terraform, GitHub Actions
PHASE 9  → Production ops      → Observability, SRE, SLOs, runbooks
PHASE 10 → Revenue             → Stripe billing, PLG, growth metrics
```

This is a **complete, world-class ICT consultancy execution engine** — capable of taking
any client from first conversation to deployed, maintained, revenue-generating software,
with no critical capability gap remaining.

---

*Return to: [Master Plan README](README.md)*

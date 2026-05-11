# SaaS Pricing & Packaging Spec — Template

## 1. Value metric

**Chosen value metric:** `<unit>`
**Rationale:** grows with customer's extracted value because ...
**Rejected:** `<alt>` — because ...

## 2. Tier definitions

| Tier | Price (monthly, billed annually) | Value-metric units included | Key features | Support | SLA | Target segment |
|------|----------------------------------|------------------------------|--------------|---------|-----|----------------|
| Free / Trial | $0 (14d) | trial | core | community | none | self-serve eval |
| Indie | $29/mo | 1 user, 100 units | core | email NBD | 99.5% | freelancers |
| Pro | $99/mo | 5 users, 1k units | + collaboration | email 24h | 99.9% | SMB |
| Studio / Business | $299/mo | 20 users, 10k units | + integrations + SSO | priority chat | 99.95% | mid-market |
| Enterprise | contact | unlimited | + dedicated infra + audit + custom DPA + named CSM | 15 min SEV1 + CSM | 99.99% | enterprise |

Limits beyond included units → overage pricing or hard-cap (state choice per metric).

## 3. Feature gates inventory

| Gate ID | Feature | Available from tier | Server-side check | Upsell UX |
|---------|---------|---------------------|-------------------|-----------|
| GATE-SSO | SAML SSO | Studio | `tenant.tier in ('studio','enterprise')` | banner "Upgrade to enable SSO" |
| GATE-AUDIT | Audit log export | Studio | tier check | banner |
| GATE-API-2K | 2k req/min | Pro | rate limit by tier | 429 + portal hint |
| GATE-DPA | Custom DPA | Enterprise | flag at provisioning | contact-us |

## 4. Expansion levers

| Lever | Trigger | In-product UX | Sales path | Target conversion |
|-------|---------|---------------|------------|-------------------|
| Seat add | seat-cap reached | inline "+1 seat $X/mo" | CSM monthly check-in | 15% MoM |
| Usage overage | 80% of cap | banner + email | CSM at 100% | 20% upgrade rate |
| Tier upsell | feature blocked 3 times | timed in-app offer | AE outreach for studio+ | 5% MoM |
| Cross-sell | adoption milestone | recommendation card | CSM at QBR | 8% per quarter |

## 5. Freemium / Trial decision

Decision: `trial 14 days no CC` | `freemium with limits` | `paid only`
Drivers: virality, channel, cost-to-serve, expected paid conversion, competitive pressure.
ADR ref: `adr/saas-freemium.md`

## 6. Credit-card-up-front decision

Decision: `no-CC trial`
Rationale: prioritise top-of-funnel; activation strong enough to convert at 18% to paid; CS team capacity sufficient to chase activated leads.

## 7. Price-raise & grandfathering

- Cadence: annual review, raise no more often than annually.
- Trigger: Rule of 10 — only raise if model projects ≥ 10% MRR uplift.
- Grandfathering: existing customers protected for 12 months from announcement.
- Announcement: 90 days advance for SMB, 180 days for Enterprise.
- Migration discount: 10-20% off new pricing for existing customers if they migrate in the announcement window.

## 8. Discount & concession authority

| Role | Max discount | Approval | Term limit |
|------|--------------|----------|------------|
| AE | 10% | self | annual only |
| Sales lead | 20% | self | annual / 2y |
| VP Sales | 30% | self | up to 3y |
| CFO / CRO | > 30% | required | any |

Every discount is recorded with reason code (competitive, strategic logo, multi-year, volume).

## 9. Public price page contract

| Must show | Must not show |
|-----------|---------------|
| Prices for Free / Indie / Pro / Studio | Negotiated Enterprise prices |
| Tier feature comparison | Unannounced features |
| Limits per tier | Discount thresholds |
| FAQ (billing, refunds, support, residency) | Internal margin / cost |
| Annual vs monthly toggle with discount | |

## 10. Traceability

| Item | Trace to | Verification |
|------|----------|--------------|
| Tier SLAs | SLO_And_Error_Budget_Doc.md | matched per tier |
| Feature gates | PRD feature register | every gated feature has gate ID |
| Pricing economics | Business_Case.md (CAC payback) | model match |
| Public page contract | Marketing site CMS | yearly review |

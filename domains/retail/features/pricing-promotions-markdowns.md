# Feature: Pricing, Promotions & Markdowns

## Description

Retail commercial rules for base pricing, price zones, price ladders, key value items, promotions, coupons, offer stacking, markdowns, clearance, and commercial approval.

## Standard Capabilities

- Price books by channel, store, region, customer segment, and effective period.
- Price zone assignment with approval and rollback history.
- Key value item and good-better-best price ladder flags.
- Promotion calendar with event role, funded source, category scope, eligibility, and channel scope.
- Offer stacking rules that explicitly allow, prevent, or require approval for combined offers.
- Coupon and voucher eligibility by SKU, category, customer segment, channel, basket, and time window.
- Markdown ladder with trigger, aged-stock rule, discount depth, exit plan, and approval route.
- Margin-floor validation before promotion, markdown, or manual discount release.
- A/B or holdout test setup for promotional mechanics where legally and operationally appropriate.
- Post-event review capturing sales, gross margin, sell-through, cannibalisation notes, funding recovery, and exceptions.

## Finance and Control Hooks

- Discounts, markdowns, supplier-funded promotions, vouchers, and manual price overrides must produce source events for finance review.
- Promotions with supplier funding must link to vendor agreement, claim basis, recovery status, and dispute workflow.
- Manual discount thresholds require segregation of duties between cashier, supervisor, and controller roles.
- Markdown events may require inventory net realisable value review where stock value is affected.

## Linked NFRs

- RET-NFR-004 Inventory Accuracy
- RET-NFR-006 Product Data Quality
- RET-NFR-007 Retail Event Auditability
- RET-NFR-008 Dashboard Freshness

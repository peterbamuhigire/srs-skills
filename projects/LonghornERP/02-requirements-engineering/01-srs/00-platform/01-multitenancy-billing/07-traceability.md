## 7. Traceability Matrix

The table below maps each functional requirement in this document to its originating business goal from the Longhorn ERP Product Requirements Document (PRD) and to the test case that will verify it. Where a test case identifier cannot be assigned before the test plan is authored, the gap is flagged with `[TRACE-GAP: FR-PLAT-NNN]`.

| FR / NFR | Business Goal (PRD Reference) | Test Case ID |
|---|---|---|
| **FR-PLAT-001** | BG-01: Enable rapid tenant onboarding by super admin to support sales pipeline velocity | `[TRACE-GAP: FR-PLAT-001]` |
| **FR-PLAT-002** | BG-01: Each tenant must have a unique, stable identity in all URLs and API calls | `[TRACE-GAP: FR-PLAT-002]` |
| **FR-PLAT-003** | BG-02: Offer a 30-day free trial to reduce conversion friction for SME prospects | `[TRACE-GAP: FR-PLAT-003]` |
| **FR-PLAT-004** | BG-01: Every new tenant must be immediately operable by the primary contact on Day 1 | `[TRACE-GAP: FR-PLAT-004]` |
| **FR-PLAT-005** | BG-03: Support Uganda-first localisation with a path to pan-Africa expansion | `[TRACE-GAP: FR-PLAT-005]` |
| **FR-PLAT-006** | BG-04: Core ERP functionality (accounting, inventory, sales, procurement) must be available to all tenants from Day 1 | `[TRACE-GAP: FR-PLAT-006]` |
| **FR-PLAT-007** | BG-01: Every tenant requires at least one operating location to record transactions | `[TRACE-GAP: FR-PLAT-007]` |
| **FR-PLAT-008** | BG-03: Eliminate manual COA setup by pre-seeding from the localisation profile | `[TRACE-GAP: FR-PLAT-008]` |
| **FR-PLAT-009** | BG-01: Tenant admin must be able to log in without contacting support | `[TRACE-GAP: FR-PLAT-009]` |
| **FR-PLAT-010** | BG-05: Audit trail for all provisioning actions required for compliance | `[TRACE-GAP: FR-PLAT-010]` |
| **FR-PLAT-011** | BG-06: Revenue recognition — subscription becomes billable on first payment | `[TRACE-GAP: FR-PLAT-011]` |
| **FR-PLAT-012** | BG-06: Trial-to-paid conversion must be enforced by the platform, not by manual intervention | `[TRACE-GAP: FR-PLAT-012]` |
| **FR-PLAT-013** | BG-06: Payment discipline — access must be restricted when billing lapses to protect platform revenue | `[TRACE-GAP: FR-PLAT-013]` |
| **FR-PLAT-014** | BG-07: Protect tenant relationships by allowing a grace period before hard suspension | `[TRACE-GAP: FR-PLAT-014]` |
| **FR-PLAT-015** | BG-06: Enforce suspension after grace period to maintain billing discipline | `[TRACE-GAP: FR-PLAT-015]` |
| **FR-PLAT-016** | BG-06: Restore access immediately on payment to incentivise settlement | `[TRACE-GAP: FR-PLAT-016]` |
| **FR-PLAT-017** | BG-06: Suspended tenants must retain access to financial data for legal and tax compliance | `[TRACE-GAP: FR-PLAT-017]` |
| **FR-PLAT-018** | BG-06: Full payment restores full access — no manual super admin step required | `[TRACE-GAP: FR-PLAT-018]` |
| **FR-PLAT-019** | BG-06: Archive long-inactive tenants to reclaim resources while retaining data | `[TRACE-GAP: FR-PLAT-019]` |
| **FR-PLAT-020** | BG-06: Archived tenants must not incur active resource consumption | `[TRACE-GAP: FR-PLAT-020]` |
| **FR-PLAT-021** | BG-05: 7-year data retention for legal and tax audit obligations | `[TRACE-GAP: FR-PLAT-021]` |
| **FR-PLAT-022** | BG-06: Allow reactivation of archived tenants to support win-back scenarios | `[TRACE-GAP: FR-PLAT-022]` |
| **FR-PLAT-023** | BG-05: All lifecycle transitions must be auditable | `[TRACE-GAP: FR-PLAT-023]` |
| **FR-PLAT-030** | BG-08: Module activation is the mechanism by which add-on revenue is unlocked | `[TRACE-GAP: FR-PLAT-030]` |
| **FR-PLAT-031** | BG-06: Deactivate add-ons on lapse to enforce subscription boundaries | `[TRACE-GAP: FR-PLAT-031]` |
| **FR-PLAT-032** | BG-09: Prevent undefined behaviour from misconfigured module dependencies | `[TRACE-GAP: FR-PLAT-032]` |
| **FR-PLAT-033** | BG-10: Navigation must reflect only active modules to avoid user confusion | `[TRACE-GAP: FR-PLAT-033]` |
| **FR-PLAT-034** | BG-11: Security — no user must access data of an inactive module via direct URL | `[TRACE-GAP: FR-PLAT-034]` |
| **FR-PLAT-035** | BG-04: Core modules are non-negotiable for all tenants | `[TRACE-GAP: FR-PLAT-035]` |
| **FR-PLAT-036** | BG-08: Plan-included modules must activate automatically on plan assignment | `[TRACE-GAP: FR-PLAT-036]` |
| **FR-PLAT-037** | BG-06: Downgrade must deactivate out-of-plan modules at cycle end | `[TRACE-GAP: FR-PLAT-037]` |
| **FR-PLAT-038** | BG-05: All module activation events must be auditable | `[TRACE-GAP: FR-PLAT-038]` |
| **FR-PLAT-040** | BG-08: Plan assignment is the primary billing configuration event | `[TRACE-GAP: FR-PLAT-040]` |
| **FR-PLAT-041** | BG-08: Plan limits must be enforced to protect the tier pricing model | `[TRACE-GAP: FR-PLAT-041]` |
| **FR-PLAT-042** | BG-08: Branch limits enforce plan tier differentiation | `[TRACE-GAP: FR-PLAT-042]` |
| **FR-PLAT-043** | BG-08: Upgrades must take effect immediately to provide instant value | `[TRACE-GAP: FR-PLAT-043]` |
| **FR-PLAT-044** | BG-07: Downgrades at cycle end protect the tenant from premature access loss | `[TRACE-GAP: FR-PLAT-044]` |
| **FR-PLAT-045** | BG-12: Annual billing incentive (2 months free) drives long-term commitment | `[TRACE-GAP: FR-PLAT-045]` |
| **FR-PLAT-046** | BG-06: Advance invoice generation gives tenants 7 days to arrange payment | `[TRACE-GAP: FR-PLAT-046]` |
| **FR-PLAT-047** | BG-06: Arrears carry-forward prevents revenue leakage | `[TRACE-GAP: FR-PLAT-047]` |
| **FR-PLAT-048** | BG-06: Payment recording is the core billing event that drives lifecycle transitions | `[TRACE-GAP: FR-PLAT-048]` |
| **FR-PLAT-049** | BG-13: Support East African payment methods (MTN MoMo, M-Pesa) to remove payment friction | `[TRACE-GAP: FR-PLAT-049]` |
| **FR-PLAT-050** | BG-06: Immediate status restoration on payment incentivises settlement | `[TRACE-GAP: FR-PLAT-050]` |
| **FR-PLAT-051** | BG-12: Annual billing formula must be auditable and transparent | `[TRACE-GAP: FR-PLAT-051]` |
| **FR-PLAT-052** | BG-08: A-la-carte is available to Small Business and Professional only — not Starter | `[TRACE-GAP: FR-PLAT-052]` |
| **FR-PLAT-053** | BG-08: A-la-carte add-on charges must be itemised on invoices | `[TRACE-GAP: FR-PLAT-053]` |
| **FR-PLAT-054** | BG-14: Upgrade trigger when a-la-carte cost approaches next tier — natural upsell mechanism | `[TRACE-GAP: FR-PLAT-054]` |
| **FR-PLAT-055** | BG-08: POS is priced per terminal, not per organisation | `[TRACE-GAP: FR-PLAT-055]` |
| **FR-PLAT-056** | BG-05: All billing events must be auditable | `[TRACE-GAP: FR-PLAT-056]` |
| **FR-PLAT-057** | BG-05: Settled invoices are immutable financial records | `[TRACE-GAP: FR-PLAT-057]` |
| **FR-PLAT-058** | BG-06: PDF invoices support offline payment workflows common in East Africa | `[TRACE-GAP: FR-PLAT-058]` |
| **FR-PLAT-059** | BG-06: Email delivery of invoices reduces time-to-payment | `[TRACE-GAP: FR-PLAT-059]` |
| **FR-PLAT-060** | BG-07: Credits for disputes or outages protect the tenant relationship | `[TRACE-GAP: FR-PLAT-060]` |
| **NFR-PLAT-001** | BG-01: Provisioning must be fast enough to support same-day onboarding by the sales team | `[TRACE-GAP: NFR-PLAT-001]` |
| **NFR-PLAT-002** | BG-11: Tenant data isolation is a non-negotiable security requirement | `[TRACE-GAP: NFR-PLAT-002]` |
| **NFR-PLAT-003** | BG-15: Platform must scale to ≥ 500 concurrent tenants for Phase 1 MRR targets | `[TRACE-GAP: NFR-PLAT-003]` |
| **NFR-PLAT-004** | BG-08: Module activation must be near-instantaneous to avoid support tickets | `[TRACE-GAP: NFR-PLAT-004]` |
| **NFR-PLAT-005** | BG-06: Lifecycle transitions must be prompt to avoid access limbo | `[TRACE-GAP: NFR-PLAT-005]` |
| **NFR-PLAT-006** | BG-05: 7-year billing data retention for financial audit compliance | `[TRACE-GAP: NFR-PLAT-006]` |
| **NFR-PLAT-007** | BG-06: Notification timeliness affects payment behaviour and tenant trust | `[TRACE-GAP: NFR-PLAT-007]` |
| **NFR-PLAT-008** | BG-11: Billing data of one tenant must never be visible to another | `[TRACE-GAP: NFR-PLAT-008]` |

---

### 7.1 Open Context Gaps Affecting This Document

The following gaps must be resolved before this SRS can be considered final:

- `[CONTEXT-GAP: GAP-004]` — Independent security review of `tenant_id` enforcement required before any production tenant is onboarded. Affects NFR-PLAT-002.
- `[CONTEXT-GAP: GAP-005]` — Formal module dependency map required. Affects FR-PLAT-032. Interim dependency rules are documented inline.
- `[CONTEXT-GAP: GAP-011]` — MTN MoMo Business bulk payment API specification required. Affects FR-PLAT-049.
- `[CONTEXT-GAP: GAP-012]` — M-Pesa Daraja B2C API specification required. Affects FR-PLAT-049.
- `[CONTEXT-GAP: GAP-015]` — White-labelling policy decision required. Affects FR-PLAT-058 (invoice branding).

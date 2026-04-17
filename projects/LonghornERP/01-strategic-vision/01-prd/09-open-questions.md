# Open Questions — Internal Decision Gaps

The following 4 gaps are unresolved internal design decisions. Each must be resolved before the documents they block can be finalised. Recommended defaults are provided to allow work to proceed provisionally, but each default requires explicit owner sign-off before it is treated as a confirmed decision.

---

## GAP-015: White-Labelling Policy

**Description:** Enterprise tenants may request the ability to present Longhorn ERP under their own brand identity — their own logo, product name, domain, and login screen — rather than Chwezi Core Systems' branding. This capability, known as white-labelling, is common in SaaS platforms targeting large enterprises and resellers.

**Decision needed:** Will Enterprise tier tenants be permitted to white-label Longhorn ERP as their own product?

**Impact if unresolved:**
- The Platform Multi-Tenancy SRS cannot specify branding configuration fields.
- The Business Case document cannot quantify the revenue uplift from white-label pricing premiums.
- A white-label capability built retrospectively is significantly more expensive than one designed in from the start.

**Recommended default:** Allow white-labelling as an optional Enterprise add-on at a defined price premium (e.g., UGX 500,000/month additional). Design the tenant configuration profile to support custom logo, custom domain (`CNAME` — DNS alias record), and custom login page text from the outset — even if the white-label feature is not marketed until Phase 2. Provisioning this as a configuration flag costs near zero if designed in; costs significantly more if retrofitted.

---

## GAP-016: Hospitality Module Scope

**Description:** The priority sectors listed in the target market include hotels, lodges, restaurants, and bars. The Point of Sale module (`POS`) includes a restaurant/bar table mode. However, full hospitality operations — room reservations, property management, housekeeping, restaurant ordering integrated with property billing — constitute a distinct functional surface that may exceed the scope of a POS table mode.

**Decision needed:** Will full hospitality functionality be delivered as a Phase 3 add-on module within Longhorn ERP, or as a separate Chwezi product (analogous to Academia Pro for schools)?

**Impact if unresolved:**
- The module inventory and subscription tier descriptions cannot be finalised.
- The Phase 3 development roadmap cannot be scoped.
- Marketing to the hospitality sector in Phase 1 is constrained by an inability to commit to a delivery vehicle or timeline.

**Recommended default:** Deliver a scoped Hospitality add-on module (`HOSPITALITY`) within Longhorn ERP in Phase 3, covering: room/unit configuration, reservation calendar, check-in/check-out, folio billing integrated with Accounting, and housekeeping task assignment. Defer a full standalone property management system to a future product decision. This default avoids premature product proliferation while serving the hospitality sector within the existing platform.

---

## GAP-017: Academia Pro / Medic8 / Kulima Integration Points

**Description:** Chwezi Core Systems operates 3 sibling SaaS products in addition to Longhorn ERP: Academia Pro (school management), Medic8 (healthcare), and Kulima (farm management). Each product manages financial transactions, employee records, and inventory in its own domain. Integration between these products and Longhorn ERP would allow a client operating multiple entities to consolidate financial reporting, payroll, and procurement through a single ERP instance.

**Decision needed:** What are the data flows and integration contracts between Longhorn ERP and each sibling product? Which entity owns the chart of accounts? Which system runs payroll? How are inter-company transactions handled?

**Impact if unresolved:**
- The Integration Layer SRS (`INTEGRATIONS`) cannot specify internal API contracts.
- Schools using Academia Pro cannot be proposed as Longhorn ERP customers without a defined integration path.
- Healthcare organisations using Medic8 may face data duplication if both systems manage employee records independently.

**Recommended default:** Define a read-only financial data push from each sibling product to Longhorn ERP's Accounting module via the `MOBILE_API` (v2). Each sibling product generates journal entries and pushes them to a designated Longhorn ERP GL account. Payroll remains in the sibling product; Longhorn ERP receives the payroll cost as a single GL posting per period. This avoids bidirectional sync complexity while enabling consolidated financial reporting. Document integration contracts as a separate Integration Design document before Phase 2.

---

## GAP-018: Source Code Strategy

**Description:** The default design intention for Longhorn ERP is a proprietary, closed-source SaaS platform. An alternative model is to release a community edition under an open-source licence (e.g., AGPL-3.0 or BSL-1.1), retaining a commercial enterprise edition with hosted services, advanced modules, and support — the model used by GitLab, Odoo, and ERPNext.

**Decision needed:** Will Longhorn ERP remain proprietary SaaS indefinitely, or will a future open-source community edition be released?

**Impact if unresolved:**
- The Business Case document cannot model open-source community adoption as a sales funnel.
- The codebase architecture may need to be structured differently if a community/enterprise split is anticipated.
- Licensing terms in the source code and documentation must reflect the chosen strategy from the start to avoid costly relicensing.

**Recommended default:** Remain proprietary for Phase 1 and Phase 2. Revisit the open-source question at Phase 3 when the competitive landscape in Francophone Africa is better understood. In the interim, design the codebase with module boundaries clean enough to support a future community/enterprise split if the decision changes. Do not embed proprietary logic in core modules that would make open-sourcing them impossible later.

---

*All 4 gaps above must be reviewed and signed off by Peter Bamuhigire before the documents they block are submitted for phase-gate approval.*

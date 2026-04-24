# Project Vision — GarageFlow

## Owner

- **Publisher:** Chwezi Core Systems (chwezicore.com)
- **Product Lead:** Peter Bamuhigire — techguypeter.com — +256 784 464 178
- **Source specification:** C:\Users\Peter\Downloads\garageflow.docx (dated 23 April 2026)

> **Owner notice.** The source document footer refers to "Byoosi.com Ltd"; this is explicitly superseded. The sole organisational owner of GarageFlow is **Chwezi Core Systems**. Every downstream artifact must attribute GarageFlow to Chwezi Core Systems.

## Product statement

GarageFlow is a world-class automotive service management platform — a complete operating system for any garage, repair shop, service centre, body shop, tyre centre, fleet workshop, or multi-branch automotive business. It unifies the entire customer journey into one connected platform: from the first booking request through vehicle check-in, inspection, estimate, approval, repair execution, parts consumption, quality control, invoicing, payment, and long-term customer retention.

GarageFlow is *not* a digital job card system with a booking calendar bolted on. It is a full business platform: workshop operations, customer relationship management, vehicle history, technician coordination, inventory control, native double-entry accounting, payroll, compliance, analytics, and customer self-service — all integrated, all connected, all auditable. The platform is built as a multi-tenant SaaS so any garage anywhere in the world can subscribe, configure, and operate from day one.

Two application families serve two distinct audiences: the **Garage Manager App** (every staff role from technician to owner) and the **Garage Customer App** (vehicle owners, fleet managers, and corporate clients). Both run on Android and iOS, both are backed by a shared secure multi-tenant backend, and both are mobile-first without sacrificing full web functionality.

## Competitive opportunity

The category leader — Tekmetric at USD 179+/month — is US-centric, lacks deep accounting integration, requires QuickBooks as a dependency, and is priced for the US market. Shopmonkey and AutoLeap have clean interfaces but share the accounting-dependency limitation. Shop-Ware emphasises transparency and customer approval but is thin on inventory depth. Mitchell 1 is legacy desktop heritage software. None of these platforms:

- Have a native full double-entry accounting engine — they all require QuickBooks or Xero as a separate subscription.
- Have built-in payroll with labour-linked technician productivity.
- Have a mobile customer app with the depth of GarageFlow's customer journey (inspection photos, live status, digital approval, in-app payment, full service history).
- Are designed for markets outside North America (no mobile money, no Africa/Asia/Middle East localisation).
- Ship a customer-facing app with the quality of a consumer fintech product.

**GarageFlow's opportunity is to build the platform these competitors should have built:** operationally deep, customer-obsessed, accounting-integrated, mobile-native, and globally deployable. The target is both independent garages that want to be professional and enterprise garage chains that want one system across every branch.

## Business goals

- **BG-001** Deliver a single platform that replaces the combined stack of workshop software plus QuickBooks/Xero plus separate customer portal, eliminating inter-system reconciliation.
- **BG-002** Enable first-job-card operation within 30 minutes of tenant sign-up, with progressive post-operational configuration.
- **BG-003** Provide consumer-fintech-grade customer experience, measured by approval-to-invoice conversion, payment completion under 30 seconds, and post-job service-history engagement.
- **BG-004** Enforce strict tenant isolation, audited by automated isolation tests on every CI build.
- **BG-005** Deliver multi-jurisdiction payment and e-invoicing readiness covering Stripe, mobile money (MTN MoMo, Airtel Money), and EFRIS at launch; ZATCA, eTIMS, EBM, CFDI scoped for phase 2.

## Target businesses

- Independent single-bay garages.
- Multi-bay general workshops.
- Tyre centres and quick-fit chains.
- Body shops (collision, paint).
- Dealer-authorised service workshops (future module for OEM-specific workflow).
- Fleet operators with in-house workshops.
- Multi-branch garage groups.

## Target users

- **Garage Manager App:** owner, branch manager, service advisor, workshop controller, technician, storekeeper, accountant, payroll officer.
- **Garage Customer App:** individual vehicle owners, fleet managers, corporate account administrators.

## Hybrid methodology note

Methodology declared as **hybrid** (see `methodology.md`). The Waterfall-phase SRS must be signed off before any Agile-phase sprint is planned. The `hybrid-synchronization` skill must be invoked after Phase 02 sign-off and before any Phase 07 artifact is generated.

## Open strategic decisions (to resolve during planning)

Lifted from Section 9 of the source doc; must be resolved before SRS baseline is sealed:

- [CONTEXT-GAP: offline-capability-matrix] — precise per-module per-role offline scope matrix. Source-doc baseline: accounting offline = no; estimates offline = yes. Full matrix required.
- [CONTEXT-GAP: gl-posting-mode] — real-time vs batch GL posting policy. Source-doc recommendation: real-time-async via durable queue within 60 s.
- [CONTEXT-GAP: customer-app-branding] — single multi-tenant Customer App vs per-tenant white-label builds for Enterprise plan. Source-doc recommendation: single multi-tenant by default; per-tenant build pipeline for Enterprise tier only.
- [CONTEXT-GAP: go-to-market-channel] — direct sales vs channel partners (distributors, OEM dealer programmes, fleet companies). Affects Super Admin Panel design and pricing.
- [CONTEXT-GAP: obd-integration-phase] — reserved API shape at MVP; Phase-2 implementation timing.
- [CONTEXT-GAP: body-shop-and-insurance-modules] — scope and phasing for damage-panel assessment tool and insurance claim workflow.
- [CONTEXT-GAP: deeper-fleet-module] — driver assignment, fuel, mileage, licence/insurance renewals, cost-per-km — phase and pricing.
- [CONTEXT-GAP: oem-dealer-module] — warranty-claim workflow, OEM service intervals, manufacturer reporting.

## Onboarding target

First job card running in under 30 minutes from sign-up, with progressive configuration (accounting chart, payment gateway, custom inspection templates) completed post-operational.

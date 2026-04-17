# 1 Executive Summary

| Field | Value |
|---|---|
| **Document** | Business Case: Medic8 Healthcare Management System |
| **Version** | 1.0 |
| **Date** | 2026-04-03 |
| **Author** | Peter -- Chwezi Core Systems (chwezicore.com) |
| **Standards** | IEEE 1058-1998, IEEE 29148-2018 |

## Business Opportunity

Healthcare information technology in sub-Saharan Africa remains critically underserved. Uganda alone has over 6,000 registered health facilities -- 3,000+ private and 3,000+ government-aided -- the majority of which operate on paper registers, manual billing, and hand-compiled statutory reports. The two incumbent digital solutions each carry structural limitations: ClinicMaster (200+ deployments) is desktop-bound with no SaaS delivery, no mobile money integration, and no FHIR compliance; OpenMRS (8,000+ deployments globally) is free to download but costs USD 35,000-130,000 over 3 years once implementation, customisation, billing bolt-ons, and Java developer fees are factored in. Neither solution serves the full clinical-administrative-financial workflow in a single platform. Medic8 addresses this gap as a multi-tenant SaaS healthcare information management system built Africa-first and globally configurable.

## Investment Profile

Medic8 operates as a solo-developer venture under Chwezi Core Systems, sharing its technology stack (PHP 8.2+, MySQL 8.x, Bootstrap 5/Tabler, Kotlin Android, Swift iOS) and architectural patterns (multi-tenant SaaS, global identity layer, offline-first, country configuration) with Academia Pro, the company's school management platform. This shared codebase reduces Phase 1 development effort by an estimated 30-40% compared to a greenfield build. Phase 1 MVP infrastructure costs are estimated at USD 2,400-4,800 annually (cloud hosting, SMS gateway, domain, SSL), with the primary investment being 6 months of the developer's opportunity cost.

## Expected Return

The revenue model follows a 4-phase trajectory over 24 months:

| Phase | Timeline | Facilities | MRR Target (UGX) | MRR Target (USD) |
|---|---|---|---|---|
| Phase 1 MVP | Month 1-6 | 10 private clinics | 1,500,000 | ~400 |
| Phase 2 Growth | Month 7-12 | 50 facilities | 15,000,000 | ~4,000 |
| Phase 3 Programmes | Month 13-18 | PEPFAR partners + NGOs | 40,000,000 | ~10,700 |
| Phase 4 Enterprise | Month 19-24 | Hospital networks | 100,000,000 | ~26,700 |

At Phase 4 maturity, annual recurring revenue reaches approximately UGX 1.2 billion (USD 320,000). The 3-year total cost of ownership for a Medic8 customer ranges from USD 9,450-71,100 versus USD 35,000-130,000 for OpenMRS, positioning Medic8 as both more affordable and more comprehensive.

## Recommendation

**Proceed with Phase 1 MVP development**, targeting private clinics in Kampala. The investment is low-risk (solo developer, shared infrastructure with Academia Pro, no external funding required), the addressable market is large (6,000+ facilities in Uganda alone), and the competitive landscape presents clear gaps that Medic8 is architected to exploit. All 7 HIGH-priority gaps identified in the gap analysis must be resolved before clinical module development begins. A 30-day pilot programme with 3 private clinics will validate the value proposition before commercial launch.

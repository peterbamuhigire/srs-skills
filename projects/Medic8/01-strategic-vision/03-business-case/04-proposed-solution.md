# 4 Proposed Solution

## 4.1 High-Level Approach

Medic8 is a multi-tenant SaaS healthcare information management system that unifies clinical, administrative, and financial workflows in a single platform. The system shares its technology stack, architectural patterns, and infrastructure with Academia Pro (Chwezi Core Systems' school management platform), reducing development effort and operational costs through codebase reuse.

**Technology stack:** PHP 8.2+ with MySQL 8.x on the backend, Bootstrap 5/Tabler on the web frontend, native Kotlin (Android) and Swift (iOS) mobile applications.

**Architecture:** Centralised multi-tenant model with `facility_id` row-level isolation, openEHR two-level modelling for multi-country clinical configurability, event-driven EHR data bus, FHIR R4 native API, and offline-first design for all clinical workflows.

**Delivery model:** Cloud-hosted SaaS with no on-premise infrastructure required. A facility is operational within 60 minutes of signup with zero-configuration defaults for Ugandan private clinics.

**Build sequence:** 4 phases over 24 months, each gated by formal criteria:

1. **Phase 1 -- MVP (6 months):** Patient registration, OPD, pharmacy, basic lab, cash billing, mobile money. Target: 10 private clinics.
2. **Phase 2 -- Growth (Month 7-12):** IPD, maternity, immunisation, insurance, inventory, HR/payroll, HMIS reporting. Target: 50 facilities.
3. **Phase 3 -- Programmes (Month 13-18):** HIV/AIDS, TB, FHIR R4 API, PEPFAR MER indicators, CHW app, patient app. Target: PEPFAR implementing partners.
4. **Phase 4 -- Enterprise (Month 19-24):** Theatre, blood bank, PACS, multi-facility sharing, Director platform. Target: hospital networks and national referrals.

## 4.2 Key Capabilities

| # | Capability | Business Goal Alignment |
|---|---|---|
| 1 | **SaaS deployment with zero on-premise infrastructure** | Eliminates server maintenance costs for facilities; enables rapid onboarding (60 minutes to first patient); reduces barrier to entry for small clinics that cannot afford IT staff |
| 2 | **Offline-first clinical workflows** | Ensures continuous patient care in areas with intermittent internet connectivity; Room database on Android synchronises when connectivity resumes; addresses Uganda's infrastructure reality |
| 3 | **Mobile money integration (MTN MoMo, Airtel Money)** | Enables digital fee collection aligned with Uganda's dominant payment channel; auto-reconciliation eliminates manual cash tracking; reduces revenue leakage |
| 4 | **Automated HMIS compliance (105/108/033b)** | Eliminates 2-3 staff-days per month of manual tallying; auto-populates HMIS forms from clinical data; direct DHIS2 API submission; reduces non-compliance risk for capitation grants |
| 5 | **FHIR R4 interoperability** | Enables data exchange with external systems (DHIS2, PEPFAR DATIM, laboratory analysers, insurance portals); positions Medic8 as standards-compliant for donor-funded programmes |
| 6 | **Global patient identity layer** | Shared architectural pattern with Academia Pro's global student identity; cross-facility patient record lookup for hospital networks; eliminates duplicate registrations |
| 7 | **Country configuration layer** | Adapts regulatory frameworks, clinical protocols, financial systems, and reporting requirements per tenant; enables expansion to Kenya, Tanzania, Rwanda, DRC, Nigeria, India, and Australia without forking the codebase |

## 4.3 Why Not Build on OpenMRS

The question of whether to fork or extend OpenMRS rather than building Medic8 from scratch requires a technical and commercial assessment. The conclusion is that building on OpenMRS would be more expensive, slower, and architecturally constrained than a purpose-built system.

**Technical arguments against an OpenMRS fork:**

1. **Language and stack mismatch:** OpenMRS is built in Java (Spring Framework). Chwezi Core Systems' development capability is PHP 8.2+ with MySQL 8.x. Adopting OpenMRS would require hiring or contracting Java developers at USD 80-120 per hour -- a cost the venture cannot sustain as a solo-developer operation.

2. **No billing module:** OpenMRS has no integrated billing, insurance management, or financial accounting. These must be built or integrated separately (OpenHMIS or Odoo), adding USD 3,000-15,000 in implementation costs and creating integration maintenance overhead indefinitely.

3. **No HR/payroll:** OpenMRS has no human resources or payroll capability. A separate system (or custom build) is required, adding USD 2,000-8,000 in costs.

4. **No mobile money:** OpenMRS has no mobile money API integration. Building MTN MoMo and Airtel Money integration into an OpenMRS fork requires custom Java development with no upstream support.

5. **Customisation cost trajectory:** OpenMRS customisation costs USD 15,000-60,000 over 3 years. Each customisation diverges from the upstream codebase, increasing maintenance cost with every release cycle.

6. **No multi-tenant SaaS architecture:** OpenMRS is designed for single-facility, on-premise deployment. Converting it to a multi-tenant SaaS platform would require re-architecting the data isolation model, authentication system, and deployment pipeline -- effectively a rewrite of the platform layer.

7. **No shared codebase benefit:** Building on OpenMRS provides no codebase reuse with Academia Pro. Building Medic8 on the same PHP/MySQL stack as Academia Pro enables shared infrastructure, shared authentication patterns, shared multi-tenant architecture, and shared country configuration logic.

8. **Community support model:** OpenMRS relies on community-only support. When a production system fails at 2 AM, there is no vendor to call. Medic8 provides direct Uganda-based support included in the subscription.

**Conclusion:** The total cost of adapting OpenMRS to match Medic8's scope (billing + insurance + HR + payroll + mobile money + SaaS + offline-first + patient app) exceeds the cost of building Medic8 from scratch on the existing PHP stack, while producing an architecturally inferior result with higher ongoing maintenance costs.

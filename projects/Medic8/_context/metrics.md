# KPI Targets and Pricing Metrics: Medic8

This document defines the subscription pricing model, add-on pricing, revenue targets by phase, phase gate criteria, and onboarding metrics for the Medic8 platform.

---

## Subscription Tiers

| Feature | Starter | Growth | Pro | Enterprise |
|---|---|---|---|---|
| Monthly price | UGX 150,000 | UGX 350,000 | UGX 700,000 | Custom |
| Facility type | Small clinic, HC II/III | HC IV, small hospital | General hospital, mission hospital | National referral, hospital group |
| Beds (IPD) | Day case only | Up to 30 | Up to 150 | Unlimited |
| Core clinical modules | All | All | All | All |
| Specialty programmes | All | All | All | All |
| Insurance management | 3 schemes | Unlimited | Unlimited | Unlimited |
| HR and Payroll | Up to 20 staff | Up to 100 staff | Unlimited | Unlimited |
| Advanced accounting | Add-on | Included | Included | Included |
| Patient mobile app | Add-on | Add-on | Included | Included |
| AI analytics | -- | Add-on | Included | Included |
| Multi-site (Director) | -- | -- | Add-on | Included |
| FHIR API access | -- | -- | Included | Included |
| Support | Email + WhatsApp | Priority WhatsApp | Dedicated CSM | On-site + SLA |

---

## Add-On Pricing

| Add-On | Monthly Price |
|---|---|
| Advanced Accounting | +UGX 80,000/month |
| Patient Mobile App | +UGX 60,000/month |
| AI Analytics | +UGX 80,000/month |
| Telemedicine | +UGX 50,000/month |
| Multi-site Director Platform | +UGX 150,000/month per additional facility |
| SMS bundles | UGX 50,000 per 1,000 SMS |

---

## Revenue Targets by Phase

| Phase | Facilities | MRR Target | Timeline |
|---|---|---|---|
| Phase 1 MVP | 10 clinics | UGX 1.5M | 6 months post-launch |
| Phase 2 Growth | 50 facilities | UGX 15M | 12 months |
| Phase 3 Programmes | PEPFAR partners | UGX 40M | 18 months |
| Phase 4 Enterprise | Hospital networks | UGX 100M | 24 months |

---

## Phase Gate Criteria

- **Phase 1 gate:** All 7 HIGH gaps resolved, core clinical workflow tested end-to-end, medication safety validation complete
- **Phase 2 gate:** Phase 1 in production with 10+ paying facilities, zero patient safety incidents reported
- **Phase 3 gate:** FHIR R4 conformance tested against ONC criteria, PEPFAR MER indicators (TX_CURR, TX_NEW, TX_PVLS) validated against manual calculation with less than 1% variance
- **Phase 4 gate:** 50+ active facilities, insurance claims processing validated with 3+ insurers, enterprise SLA defined and tested

---

## Onboarding Metrics

- **Facility onboarding target:** 2-4 hours from account creation to first patient registration
- **Training delivery:** Video-based, module-specific training; mandatory completion before module activation
- **Post-onboarding check-ins:** 30-day, 60-day, and 90-day structured check-ins bundled into the subscription at no additional cost

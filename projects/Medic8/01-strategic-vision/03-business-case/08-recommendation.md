# 8 Recommendation

## 8.1 Decision

**Proceed with Phase 1 MVP development.**

The business case supports proceeding based on the following factors:

1. **Large addressable market:** Over 6,000 registered health facilities in Uganda alone, with an estimated TAM of UGX 20.9 billion (USD 5.6 million) per year.
2. **Low cash investment:** Phase 1 cash outlay of USD 3,315-12,350 (excluding developer opportunity cost), with operational break-even achievable by Month 7-9.
3. **Clear competitive gaps:** ClinicMaster lacks SaaS delivery, mobile money, offline-first, FHIR, and patient app. OpenMRS costs USD 35,000-130,000 over 3 years and lacks billing, insurance, HR, and payroll.
4. **Shared codebase advantage:** 30-40% development effort reduction through architecture and component reuse from Academia Pro.
5. **Favourable unit economics:** Gross margin of 87-95% per facility across all subscription tiers.

## 8.2 Go/No-Go Criteria

| # | Criterion | Threshold | Measurement Method |
|---|---|---|---|
| 1 | All 7 HIGH gaps resolved before clinical development | 7/7 gaps documented as resolved in `_context/gap-analysis.md` | Gap resolution review by Peter; each gap marked with resolution date, decision, and evidence |
| 2 | Drug interaction database licensed | Valid licence agreement signed; database integrated into CDS engine | Licence document on file; CDS engine returns correct alerts for 100 test drug pairs |
| 3 | Uganda PDPA legal review completed | Written legal opinion from Uganda data protection lawyer covering consent categories, lawful basis, and breach notification | Legal opinion document filed in project records; key findings incorporated into privacy policy and Terms of Service |
| 4 | Phase 1 MVP demonstrates 80% feature completion within budget | 80% of Phase 1 module scope (Section 9.2.1 of PRD) functional in staging environment; cash spend within 120% of budget estimate | Feature checklist sign-off; expenditure tracking against Phase 1 budget of USD 3,315-12,350 |
| 5 | First 3 pilot facilities onboarded within 2 months of launch | 3 private clinics in Kampala actively using Medic8 for daily operations within 60 days of production deployment | Facility activity logs showing daily patient registrations, consultations, and billing transactions |

## 8.3 Approval Table

| Role | Name | Decision | Date |
|---|---|---|---|
| Owner / Developer | Peter Bamuhigire -- Chwezi Core Systems | | |
| Medical Advisor | `[TBD -- practising clinician to validate CDS and clinical workflows]` | | |
| Legal Advisor | `[TBD -- Uganda data protection lawyer for PDPA review]` | | |

## 8.4 Pilot Programme

### 8.4.1 Scope

3 private clinics in Kampala for a 30-day pilot period. Pilot facilities will be selected based on the following criteria:

- Small to medium outpatient clinic with 1-5 consultation rooms
- Operating pharmacy and basic laboratory
- Currently using paper, Excel, or ClinicMaster
- Willing to run Medic8 in parallel with existing system for the pilot duration
- Clinic owner or manager available for weekly feedback sessions

### 8.4.2 Success Criteria

| # | Criterion | Threshold |
|---|---|---|
| 1 | Zero patient safety incidents attributable to system error | 0 incidents over 30 days |
| 2 | Feature utilisation rate | Greater than 80% of Phase 1 modules actively used (patient registration, OPD, pharmacy, lab, billing) |
| 3 | Conversion intent | Facility owner or manager expresses willingness to convert to paid subscription at pilot conclusion |
| 4 | Data integrity | 95% or higher cash billing reconciliation rate between Medic8 records and manual daily tally |
| 5 | Onboarding time | Each facility onboarded within 4 hours from account creation to first patient registration |
| 6 | System availability | 99% uptime during pilot period (excluding scheduled maintenance windows communicated 24 hours in advance) |

### 8.4.3 Pilot Cost

- **Subscription:** Free tier during the 30-day pilot period (no subscription charges to pilot facilities)
- **Infrastructure:** Borne by Chwezi Core Systems; estimated at USD 50-100 for 3 facilities over 30 days (cloud hosting + SMS)
- **Support:** Direct WhatsApp and on-site support from Peter during pilot period
- **Training:** Video-based module training + 1 on-site training session per facility (2-4 hours)

### 8.4.4 Timeline

| Activity | Duration | Notes |
|---|---|---|
| Pilot facility recruitment | 2 weeks | Identify and confirm 3 clinics in Kampala |
| Onboarding and training | 1 week | Staggered: 1 facility per day |
| Parallel-run period | 30 days | Medic8 runs alongside existing system |
| Weekly feedback sessions | 4 sessions | Structured feedback collection per facility |
| Pilot evaluation | 1 week | Assess against success criteria |
| Go/no-go decision for commercial launch | Day 45 | Based on pilot evaluation results |

**Total pilot duration:** 45 days from recruitment start to go/no-go decision.

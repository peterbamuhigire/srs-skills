# 2 Problem Statement

## 2.1 Current State of Healthcare Operations in Uganda

Uganda's healthcare delivery system comprises over 6,000 registered health facilities: approximately 4,000+ private clinics and hospitals, and approximately 3,000 government-aided facilities ranging from Health Centre II to National Referral Hospitals. The majority of these facilities manage operations through one of 4 approaches:

1. Paper-based workflows — Patient records in exercise books or paper files, prescriptions on paper, pharmacy stock counted manually, billing via handwritten receipts, and HMIS reports compiled by hand at month-end. This is the dominant mode for government facilities (HC II-IV) and smaller private clinics.
2. ClinicMaster — Desktop-bound software deployed in 200+ facilities across East Africa. On-premise installation requiring each facility to maintain its own server hardware and IT support. The installed base represents less than 5% penetration of the 4,000+ private facilities in Uganda alone.
3. OpenMRS / UgandaEMR — Open-source electronic medical record system deployed in PEPFAR-funded facilities. Free to download but carries a 3-year TCO of USD 35,000-130,000. Lacks billing, insurance, HR, payroll, and mobile money integration.
4. Excel spreadsheets — Used as a supplement to paper or OpenMRS for billing reconciliation, stock tracking, insurance claims, and ad hoc reporting. Common in mission hospitals that have OpenMRS for clinical records but no financial module.

No single solution available in the Ugandan market today delivers a unified clinical, administrative, and financial workflow as a cloud-hosted SaaS platform with mobile money integration, offline resilience, multi-language support, and AI-powered clinical workflows.

## 2.2 Pain Points by Market Segment

### 2.2.1 Private Clinics (4,000+ facilities)

- Server maintenance costs: ClinicMaster requires on-premise server hardware and IT support, adding UGX 2-5 million annually in infrastructure costs for a small clinic.
- No mobile money integration: Patients must pay cash or visit a bank; no MTN MoMo or Airtel Money API for fee collection or auto-reconciliation.
- No patient-facing application: No appointment booking, no lab result access, no payment portal for patients.
- Manual HMIS tallying: HMIS 105 compilation consumes 2+ staff-days per month, diverting clinical staff from patient care.

### 2.2.2 Mission and NGO Hospitals

- No billing in OpenMRS: Mission hospitals running OpenMRS maintain a separate Excel spreadsheet for billing, revenue tracking, and financial reporting.
- No insurance management: Insurance claims are processed manually via paper forms, resulting in high rejection rates and delayed reimbursement.
- Java developer costs: OpenMRS customisation requires Java developers at USD 80-120 per hour; Java developers with healthcare domain experience are scarce in Uganda.
- Expensive training: OpenMRS training requires external trainers and costs USD 6,000-30,000 over 3 years.

### 2.2.3 Government Facilities (3,000 facilities)

- HMIS manual tallying: HMIS 105/108/033b report compilation from paper registers consumes 2-3 staff-days per month at each facility.
- Drug stockouts: No visibility into consumption patterns or stock levels; National Medical Stores (NMS) orders are based on estimates, not consumption data.
- Capitation grant tracking: Grant receipts and expenditures are tracked manually with no audit trail.
- Limited digital literacy: Most staff have limited computer skills, making complex software unusable without extensive training.

### 2.2.4 Multi-Facility Hospital Networks

- No cross-facility patient records: Patients must re-register at each facility in the network; no shared patient identity.
- No consolidated reporting: Each facility reports independently; no unified analytics dashboard for network directors.
- Separate billing systems: No unified revenue view across the network.
- Vendor lock-in: Legacy on-premise vendors offer no migration path and charge premium rates for customisation.

### 2.2.5 PEPFAR/Global Fund Implementing Partners

- Manual MER indicator calculation: PEPFAR Monitoring, Evaluation, and Reporting indicators (TX_CURR, TX_NEW, TX_PVLS) are calculated manually from registers, consuming significant programme staff time.
- OpenMRS customisation costs: USD 15,000 or more per year for UgandaEMR customisation and support.
- No donor fund accounting: No ring-fenced cost centres for PEPFAR, Global Fund, or UNICEF programme funds within the EMR.
- Staff turnover: Constant retraining on a complex system as programme staff rotate.

### 2.2.6 Francophone Africa — The Language Barrier Problem

English-only healthcare systems create a compounding adoption barrier in DRC, Rwanda, Cameroon, and Francophone West Africa, where French is the professional and administrative language:

- Clinical terminology mistranslated by untrained staff: When staff translate system labels verbally, clinical meaning degrades. A nurse reading "chief complaint" in English and transcribing it as a rough Lingala approximation introduces ambiguity into the clinical record — a direct patient safety risk.
- Patient non-adherence from incomprehensible discharge notes: Patients who cannot read English discharge summaries cannot follow post-discharge care instructions. This is not a literacy problem — it is a language problem. A French-speaking DRC patient with a university education cannot act on English clinical instructions.
- Adoption barrier in DRC's 1,200+ registered health facilities: No commercial EHR with a complete, reviewed French-language interface exists in the East Africa market. This is a structural exclusion, not a preference. ClinicMaster is English-only. OpenMRS community translations for French are incomplete and untested in clinical settings.
- Rwanda's digital health ambitions blocked: Rwanda has 1,500+ registered health facilities and an actively digitising health sector with government-mandated Mutuelle de Santé insurance. The absence of a complete French-language clinical system delays this digitisation agenda.

The i18n problem is a patient safety problem, not a localisation convenience. Clinical terminology translated poorly by untrained staff creates patient safety risks at the point of documentation and at the point of care.

### 2.2.7 The Clinical Documentation Time Problem

Clinicians in East Africa spend approximately 35% of each consultation on EHR data entry. This is not unique to the region — global studies report similar ratios — but the impact is amplified in understaffed facilities where every clinical minute matters.

The specific burden by task:

- SOAP note documentation: 8-12 minutes per consultation at facilities with structured EHR templates.
- Discharge summary: 15-25 minutes per inpatient discharge, often completed at the end of a 12-hour shift.
- Referral letter: 5-10 minutes per referral, written from memory and clinical notes.
- ICD coding: 3-5 minutes per encounter at facilities that code diagnoses for insurance purposes; uncoded diagnoses result in claim rejection.

AI-drafted notes — generated from structured encounter data and requiring only clinician review and approval — can reclaim 15-20 minutes per clinician per day. At a 10-clinician facility operating 250 days per year, this is equivalent to adding 0.25 full-time equivalent (FTE) clinical capacity without hiring. No current system in the East Africa market offers this capability.

The absence of AI-assisted documentation is not a comfort issue — it is a capacity issue in a region with a clinician-to-patient ratio far below WHO recommended levels.

## 2.3 Cost of Inaction

Maintaining the status quo imposes measurable costs across clinical safety, revenue, compliance, and operational efficiency:

1. Medication errors from paper prescribing: Handwritten prescriptions are susceptible to misreading, dosing errors, and missed drug interactions. Without a Clinical Decision Support (CDS) engine, allergy-prescription conflicts and drug-drug interactions go undetected.

2. Revenue leakage from manual billing: Facilities without integrated billing lose revenue through unbilled services, duplicate billing, uncollected fees, and cash reconciliation discrepancies. Facilities report reconciliation gaps of 5-15% of daily revenue.

3. HMIS non-compliance risking capitation grant suspension: Government-aided facilities that fail to submit accurate, timely HMIS reports to the District Health Officer risk suspension of Primary Health Care (PHC) conditional grants and capitation funding.

4. Patient record duplication: Without a global patient identity, patients are registered as new at every visit to a different facility. Duplicate records lead to fragmented medical histories, repeated investigations, and missed chronic disease follow-up.

5. Insurance claim rejection: Manual claims processing results in high rejection rates due to incomplete documentation, coding errors, and missed pre-authorisation. Each rejected claim costs the facility in delayed or lost reimbursement plus administrative rework.

6. Drug stockouts and expiry waste: Without consumption-based stock tracking, facilities over-order some items (leading to expiry waste) and under-order others (leading to stockouts that force patients to purchase from external pharmacies).

7. Clinical staff diverted to administrative work: Staff-days consumed by manual HMIS tallying, paper-based stock counts, and handwritten reports reduce the time available for direct patient care.

8. Francophone patient harm from language-barrier care: Post-discharge instructions that patients cannot read in their language lead to non-adherence, complications, and avoidable readmissions. This is a quantifiable patient harm pathway, not a service quality preference.

9. AI documentation gap compounds over time: Facilities that do not adopt AI-assisted documentation accumulate a structural efficiency disadvantage relative to facilities that do. The gap compounds with scale: a 10-clinician facility that reclaims 15 minutes per clinician per day gains the equivalent of 938 clinical hours per year — nearly 0.5 FTE — compared to a facility still on paper documentation.

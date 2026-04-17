# 2 Problem Statement

## 2.1 Current State of Healthcare Operations in Uganda

Uganda's healthcare delivery system comprises over 6,000 registered health facilities: approximately 3,000+ private clinics and hospitals, and approximately 3,000 government-aided facilities ranging from Health Centre II to National Referral Hospitals. The majority of these facilities manage operations through one of four approaches:

1. **Paper-based workflows** -- Patient records in exercise books or paper files, prescriptions on paper, pharmacy stock counted manually, billing via handwritten receipts, and HMIS reports compiled by hand at month-end. This is the dominant mode for government facilities (HC II-IV) and smaller private clinics.
2. **ClinicMaster** -- Desktop-bound software deployed in 200+ facilities across East Africa. On-premise installation requiring each facility to maintain its own server hardware and IT support.
3. **OpenMRS / UgandaEMR** -- Open-source electronic medical record system deployed in PEPFAR-funded facilities. Free to download but carries a 3-year TCO of USD 35,000-130,000. Lacks billing, insurance, HR, payroll, and mobile money integration.
4. **Excel spreadsheets** -- Used as a supplement to paper or OpenMRS for billing reconciliation, stock tracking, insurance claims, and ad hoc reporting. Common in mission hospitals that have OpenMRS for clinical records but no financial module.

No single solution available in the Ugandan market today delivers a unified clinical, administrative, and financial workflow as a cloud-hosted SaaS platform with mobile money integration and offline resilience.

## 2.2 Pain Points by Market Segment

### 2.2.1 Private Clinics (3,000+ facilities)

- **Server maintenance costs:** ClinicMaster requires on-premise server hardware and IT support, adding UGX 2-5 million annually in infrastructure costs for a small clinic
- **No mobile money integration:** Patients must pay cash or visit a bank; no MTN MoMo or Airtel Money API for fee collection or auto-reconciliation
- **No patient-facing application:** No appointment booking, no lab result access, no payment portal for patients
- **Manual HMIS tallying:** HMIS 105 compilation consumes 2+ staff-days per month, diverting clinical staff from patient care

### 2.2.2 Mission and NGO Hospitals

- **No billing in OpenMRS:** Mission hospitals running OpenMRS maintain a separate Excel spreadsheet for billing, revenue tracking, and financial reporting
- **No insurance management:** Insurance claims are processed manually via paper forms, resulting in high rejection rates and delayed reimbursement
- **Java developer costs:** OpenMRS customisation requires Java developers at USD 80-120 per hour; Java developers with healthcare domain experience are scarce in Uganda
- **Expensive training:** OpenMRS training requires external trainers and costs USD 6,000-30,000 over 3 years

### 2.2.3 Government Facilities (3,000 facilities)

- **HMIS manual tallying:** HMIS 105/108/033b report compilation from paper registers consumes 2-3 staff-days per month at each facility
- **Drug stockouts:** No visibility into consumption patterns or stock levels; National Medical Stores (NMS) orders are based on estimates, not consumption data
- **Capitation grant tracking:** Grant receipts and expenditures are tracked manually with no audit trail
- **Limited digital literacy:** Most staff have limited computer skills, making complex software unusable without extensive training

### 2.2.4 Multi-Facility Hospital Networks

- **No cross-facility patient records:** Patients must re-register at each facility in the network; no shared patient identity
- **No consolidated reporting:** Each facility reports independently; no unified analytics dashboard for network directors
- **Separate billing systems:** No unified revenue view across the network
- **Vendor lock-in:** Legacy on-premise vendors offer no migration path and charge premium rates for customisation

### 2.2.5 PEPFAR/Global Fund Implementing Partners

- **Manual MER indicator calculation:** PEPFAR Monitoring, Evaluation, and Reporting indicators (TX_CURR, TX_NEW, TX_PVLS) are calculated manually from registers, consuming significant programme staff time
- **OpenMRS customisation costs:** USD 15,000 or more per year for UgandaEMR customisation and support
- **No donor fund accounting:** No ring-fenced cost centres for PEPFAR, Global Fund, or UNICEF programme funds within the EMR
- **Staff turnover:** Constant retraining on a complex system as programme staff rotate

## 2.3 Cost of Inaction

Maintaining the status quo imposes measurable costs across clinical safety, revenue, compliance, and operational efficiency:

1. **Medication errors from paper prescribing:** Handwritten prescriptions are susceptible to misreading, dosing errors, and missed drug interactions. Without a Clinical Decision Support (CDS) engine, allergy-prescription conflicts and drug-drug interactions go undetected.
2. **Revenue leakage from manual billing:** Facilities without integrated billing lose revenue through unbilled services, duplicate billing, uncollected fees, and cash reconciliation discrepancies. Facilities report reconciliation gaps of 5-15% of daily revenue.
3. **HMIS non-compliance risking capitation grant suspension:** Government-aided facilities that fail to submit accurate, timely HMIS reports to the District Health Officer risk suspension of Primary Health Care (PHC) conditional grants and capitation funding.
4. **Patient record duplication:** Without a global patient identity, patients are registered as new at every visit to a different facility. Duplicate records lead to fragmented medical histories, repeated investigations, and missed chronic disease follow-up.
5. **Insurance claim rejection:** Manual claims processing results in high rejection rates due to incomplete documentation, coding errors, and missed pre-authorisation. Each rejected claim costs the facility in delayed or lost reimbursement plus administrative rework.
6. **Drug stockouts and expiry waste:** Without consumption-based stock tracking, facilities over-order some items (leading to expiry waste) and under-order others (leading to stockouts that force patients to purchase from external pharmacies).
7. **Clinical staff diverted to administrative work:** Staff-days consumed by manual HMIS tallying, paper-based stock counts, and handwritten reports reduce the time available for direct patient care.

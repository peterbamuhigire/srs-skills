# Market Segment Personas: Medic8

This document defines 6 representative personas spanning the Medic8 target market, from small private clinics to national referral hospitals. Each persona captures the facility context, current pain points, and the Medic8 value proposition for that segment.

---

## 1. Dr. Sarah Nakamya

| Attribute | Detail |
|---|---|
| Role | Owner / Director |
| Facility | Nakamya Medical Centre |
| Facility Type | Private clinic |
| Location | Kampala, Uganda |
| Size | 3 consultation rooms, pharmacy, basic lab, 8 staff |
| Current System | ClinicMaster (desktop version) |

**Pain Points:**

- Server maintenance costs are high and require on-site IT support
- No mobile money integration; patients must pay cash or visit the bank
- No patient-facing app for appointment booking or result access
- HMIS 105 tallying is done manually at the end of each month, consuming 2+ staff-days

**What They Want from Medic8:**

- SaaS delivery with no on-premise server to maintain
- Integrated mobile money (MTN MoMo, Airtel Money) payment collection
- Patient appointment booking app to reduce walk-in congestion
- Automated HMIS 105 report generation from clinical data

**Key Modules:** OPD, Pharmacy, Lab, Billing, Appointments

**Target Tier:** Starter (UGX 150,000/month)

---

## 2. Sr. Margaret Akello

| Attribute | Detail |
|---|---|
| Role | Medical Director |
| Facility | St. Joseph's Mission Hospital |
| Facility Type | Mission hospital (80-bed) |
| Location | Eastern Uganda |
| Size | Maternity, lab, pharmacy, HIV programme, 45 staff |
| Current System | OpenMRS (donated by NGO partner) |

**Pain Points:**

- No billing module in OpenMRS; the facility uses a separate Excel spreadsheet for billing and revenue tracking
- No insurance management capability; claims are processed manually via paper forms
- Java developer costs for OpenMRS customisation are prohibitive (USD 80-120/hour)
- OpenMRS training is expensive and requires external trainers

**What They Want from Medic8:**

- Integrated billing and insurance claims management in a single platform
- Donor fund accounting to track and report on restricted programme funds (Global Fund, PEPFAR)
- PMTCT tracking for the HIV/AIDS programme with MoH-compliant indicators
- Local Uganda-based support team with knowledge of MoH reporting requirements

**Key Modules:** OPD, IPD, Maternity, HIV/AIDS, Pharmacy, Lab, Billing, Insurance, Accounting

**Target Tier:** Pro (UGX 700,000/month)

---

## 3. Dr. James Okello

| Attribute | Detail |
|---|---|
| Role | In-Charge |
| Facility | Gulu HC IV |
| Facility Type | Government Health Centre IV |
| Location | Northern Uganda |
| Size | 30 beds, 25 staff |
| Current System | Paper registers + manual DHIS2 entry |

**Pain Points:**

- HMIS manual tallying consumes 2-3 staff-days per month
- Drug stockouts occur because there is no visibility into consumption patterns or stock levels
- Capitation grant tracking is done manually with no audit trail
- Most staff have limited computer skills, making complex software unusable

**What They Want from Medic8:**

- Automated HMIS 105/108 report generation with direct DHIS2 submission
- NMS ordering integration with consumption-based demand forecasting
- Offline-first architecture that works reliably with intermittent internet connectivity
- Simple, intuitive interface designed for staff with limited digital literacy

**Key Modules:** OPD, Maternity, Immunisation, Pharmacy, HMIS Reporting, Inventory

**Target Tier:** Growth (UGX 350,000/month)

---

## 4. Mr. Rajesh Patel

| Attribute | Detail |
|---|---|
| Role | CEO |
| Facility | Patel Hospital Group |
| Facility Type | Multi-facility hospital network (5 hospitals) |
| Location | Mumbai, Pune, Bangalore, India |
| Size | 500+ beds total, 800 staff |
| Current System | Legacy on-premise HIS |

**Pain Points:**

- No cross-facility patient record sharing; patients must re-register at each hospital
- No consolidated analytics dashboard; each facility reports independently
- Separate billing system per hospital with no unified revenue view
- Expensive vendor lock-in with the current on-premise vendor

**What They Want from Medic8:**

- Director platform with cross-facility analytics and unified dashboards
- Unified patient identity across all facilities in the group
- DRG-based billing for insurance integration
- FHIR R4 API for interoperability with external systems and future integrations

**Key Modules:** All clinical modules, Billing, Insurance, Accounting, Director Platform, FHIR API

**Target Tier:** Enterprise (custom pricing)

---

## 5. Jane Achieng

| Attribute | Detail |
|---|---|
| Role | PEPFAR Programme Manager |
| Facility | Health Access Uganda (NGO) |
| Facility Type | NGO supporting 20 health facilities |
| Location | Western Uganda |
| Size | 20 supported facilities under USAID PEPFAR funding |
| Current System | UgandaEMR (OpenMRS fork) |

**Pain Points:**

- No integrated billing module in UgandaEMR; facilities must use a separate system for revenue
- OpenMRS customisation costs approximately USD 15,000/year
- PEPFAR MER indicator calculation (TX_CURR, TX_NEW, TX_PVLS) is done manually, consuming significant programme staff time
- Staff turnover means constant retraining on a complex system

**What They Want from Medic8:**

- Automated PEPFAR MER indicator calculation (TX_CURR, TX_NEW, TX_PVLS) validated against manual tallies
- Donor fund tracking with restricted fund accounting and donor-specific reporting
- Data migration from OpenMRS/UgandaEMR with validated import
- Lower total cost of ownership compared to the current OpenMRS support contract

**Key Modules:** HIV/AIDS, TB, Lab, Pharmacy, HMIS, Donor Fund Accounting

**Target Tier:** Pro (UGX 700,000/month x 20 facilities)

---

## 6. Prof. Edward Ssali

| Attribute | Detail |
|---|---|
| Role | IT Director |
| Facility | Mulago National Referral Hospital |
| Facility Type | National referral hospital |
| Location | Kampala, Uganda |
| Size | 1,500+ beds, 50+ departments, 3,000+ staff |
| Current System | Patchwork of disconnected systems |

**Pain Points:**

- No unified patient record across departments; patients carry physical files between departments
- Lab results are frequently lost during inter-departmental transfer
- Radiology images are stored on CD-ROMs with no digital archive or PACS
- Insurance claims are processed manually with high rejection rates

**What They Want from Medic8:**

- Enterprise-scale EHR with a unified patient record across all departments
- PACS integration for digital radiology image storage and retrieval
- HL7 v2 interfaces for automated analyser connectivity in the laboratory
- FHIR R4 API for research data extraction and interoperability
- Real-time bed management dashboard across all wards

**Key Modules:** All modules, PACS, HL7 v2, FHIR API, Director Platform

**Target Tier:** Enterprise (Phase 4 target)

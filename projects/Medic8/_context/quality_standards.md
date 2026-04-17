# Quality and Performance Standards for Medic8

This document defines the measurable quality, performance, security, and compliance targets for the Medic8 healthcare management system. All thresholds are binding requirements unless marked otherwise.

## 1 Availability

- Cloud uptime: 99.9% (no more than 8.76 hours downtime per year), measured monthly
- $Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$
- Offline clinical capability: core clinical modules (registration, OPD consultation, prescribing, dispensing, lab result entry) shall function at full capacity with 0% internet connectivity
- Generator-aware sync: the system detects power restoration and immediately syncs the offline queue

## 2 Performance

- API response time: P95 under 500 ms under normal load (up to 50 concurrent users per facility)
- Page load time: under 2 seconds on a 1 Mbps connection
- Full sync: requires 1 Mbps bandwidth
- Real-time clinical use: functions on 256 Kbps
- View-only mode: functions on any SMS-capable connection
- Minimum bandwidth for useful operation: 64 Kbps

## 3 Security

- Encryption at rest: AES-256-GCM for all patient health data
- Encryption in transit: TLS 1.2 or higher on all endpoints; TLS 1.0/1.1 disabled
- Session timeout: 15 minutes inactive for clinical users
- MFA: required for Super Admin, Facility Admin, Accountant, Auditor; optional for clinical staff
- Data retention: minimum 10 years from last clinical encounter (Uganda MoH policy)
- Breach notification: identify and report affected records within 72 hours (PDPA 2019 Section 31)
- Audit trail: tamper-proof log of all CRUD operations on patient data (PDPA 2019 Section 24)

## 4 Mobile App

- Android support: 7.0+ (API level 24), 1 GB RAM minimum, 5-year-old budget phones
- Data-lite mode: operates on 2G/3G networks
- Large result images (radiology): download only on WiFi by default
- Offline access: last synced records accessible without internet
- iOS support: iOS 15.0+

## 5 Data Quality

- Auto-save interval: every form interaction (not just on submit)
- ICD-10 coding: mandatory for all diagnoses (computer-assisted, not free text)
- Patient registration: minimum fields enforced (name, sex, age/DOB, contact method)
- Discharge: requires completed summary before finalisation

## 6 FHIR Compliance

- 14 FHIR R4 resource types exposed via API
- HTML narrative fallback in every FHIR response
- SMART on FHIR support for third-party apps

## 7 Onboarding

- Facility onboarding target: 2-4 hours from account creation to first patient registration
- Per-module activation: modules can be enabled independently
- Training materials: video-based, not text-only

# Feature: Student Information System

## Description
Core student demographic and enrollment management — student registration,
identity records, enrollment history, guardian relationships, and FERPA
consent and disclosure tracking.

## Standard Capabilities
- Student registration and demographic data capture (name, DOB, address, contact)
- Student ID generation and management
- Guardian/parent relationship management with FERPA rights tracking
- Enrollment history across academic years, schools, and programs
- Directory information designation and opt-out management
- Student record export (transcript, enrollment verification)
- FERPA disclosure log — tracking all third-party record releases
- Transfer record packaging and inter-district data exchange
- Age-18 transition workflow (rights transfer from parent to student)

## Regulatory Hooks
- FERPA (34 CFR §99.37): directory information must be configurable; opt-out must be honored system-wide
- FERPA (34 CFR §99.32): all disclosures of education records must be logged in a disclosure record
- COPPA: students identified as under 13 must not have data collected before VPC is obtained
- State student privacy laws: data sharing agreements required for any third-party access

## Linked NFRs
- EDU-NFR-001 (Student Record Confidentiality)
- EDU-NFR-003 (Parental Consent for Under-13)
- EDU-NFR-004 (Data Retention — 5 years post-graduation)

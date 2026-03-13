# Feature: Attendance Tracking

## Description
Daily and period-level student attendance recording, absence management,
parent notification, and state attendance reporting with FERPA-compliant
access controls.

## Standard Capabilities
- Daily and period-by-period attendance recording by teacher
- Absence categorization (excused, unexcused, tardy, early departure)
- Automated parent/guardian notification on unexcused absence
- Chronic absenteeism detection and alert workflow
- Attendance summary reports per student, class, and school
- Bulk attendance import from external sources (bus, cafeteria scan)
- State attendance reporting export (average daily attendance, ADA)
- Truancy threshold tracking with intervention workflow triggers
- Attendance record amendment with justification and original value preservation

## Regulatory Hooks
- FERPA: attendance records are education records; access restricted to authorized staff and parents
- State compulsory attendance laws: truancy thresholds and reporting requirements vary by state
- IDEA: attendance data for students with IEPs may be referenced in evaluation documentation
- ADA/Section 504: attendance policies must accommodate disability-related absences

## Linked NFRs
- EDU-NFR-001 (Student Record Confidentiality — attendance is a protected education record)
- EDU-NFR-002 (Accessibility Compliance — attendance interfaces used by teachers and parents)
- EDU-NFR-004 (Data Retention — attendance records retained 5 years post-graduation)

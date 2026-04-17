# Requirements Traceability Matrix — Academia Pro

## 1 Document Information

| Field | Value |
|---|---|
| Project | Academia Pro — Multi-Tenant SaaS School Management Platform |
| Standard | IEEE 1012-2016 (System, Software, and Hardware Verification and Validation) |
| Version | 1.0 |
| Date | 2026-04-03 |
| Prepared by | Chwezi Core Systems |
| Integrity Level | IL-3 (High — student PII, financial data, statutory reporting) |

---

## 2 Traceability Matrix

### 2.1 Functional Requirements

| Req ID | Requirement Summary | Source (BG-ID) | Priority | Test Case ID(s) | Design Element | Verification Method | Status |
|---|---|---|---|---|---|---|---|
| FR-AUTH-001 | Web session login with CSRF and lockout | BG-001 | High | TC-AUTH-001 | AuthModule / `tbl_users` | Test | Specified |
| FR-AUTH-002 | API/mobile JWT login with dual tokens | BG-001, BG-005 | High | TC-AUTH-002 | AuthModule / `tbl_api_refresh_tokens` | Test | Specified |
| FR-AUTH-003 | JWT token refresh with rotation | BG-001 | High | TC-AUTH-003 | AuthModule / `tbl_api_refresh_tokens` | Test | Specified |
| FR-AUTH-004 | Session and token logout | BG-001 | High | TC-AUTH-004 | AuthModule | Test | Specified |
| FR-AUTH-005 | Idle session timeout at 30 minutes | BG-001 | Medium | TC-AUTH-005 | AuthModule | Test | Specified |
| FR-AUTH-006 | Super Admin MFA (TOTP/SMS OTP) | BG-001 | High | TC-AUTH-006 | AuthModule | Test | Specified |
| FR-TNT-001 | Tenant provisioning with owner account | BG-001, BG-005 | High | TC-TNT-001 | TenantModule / `tenants` | Test | Specified |
| FR-TNT-002 | Tenant activation by Super Admin | BG-001 | High | TC-TNT-002 | TenantModule / `tenants` | Test | Specified |
| FR-TNT-003 | Tenant suspension with session invalidation | BG-001 | High | TC-TNT-003 | TenantModule / `tenants` | Test | Specified |
| FR-SIS-001 | New student admission with global identity | BG-001, BG-005 | High | TC-SIS-001 | SISModule / `global_students`, `school_enrollments` | Test | Specified |
| FR-SIS-002 | Cross-school identity lookup and enrolment | BG-005 | High | TC-SIS-002 | SISModule / `global_students` | Test | Specified |
| FR-SIS-003 | Student search via Meilisearch | BG-001 | Medium | TC-SIS-003 | SISModule / Meilisearch | Test | Specified |
| FR-SIS-004 | Student transfer out with record retention | BG-005 | Medium | TC-SIS-004 | SISModule / `school_enrollments` | Test | Specified |
| FR-SIS-005 | Student record 7-year retention lock | BG-001 | High | TC-SIS-005 | SISModule / `global_students` | Test | Specified |
| FR-ACA-001 | Academic year with 3-term Uganda calendar | BG-001, BG-002 | High | TC-ACA-001 | AcademicsModule / `academic_years`, `terms` | Test | Specified |
| FR-ACA-002 | Class and stream configuration | BG-001 | High | TC-ACA-002 | AcademicsModule / `classes`, `streams` | Test | Specified |
| FR-ACA-003 | Automatic UNEB grading schema assignment | BG-002 | High | TC-ACA-003 | AcademicsModule / `classes` | Test | Specified |
| FR-ACA-004 | Subject and timetable conflict detection | BG-001 | Medium | TC-ACA-004 | AcademicsModule / `timetables` | Test | Specified |
| FR-FEE-001 | Fee structure definition per class per term | BG-003 | High | TC-FEE-001 | FeesModule / `fee_structures` | Test | Specified |
| FR-FEE-002 | Manual fee payment with receipt and SMS | BG-003 | High | TC-FEE-002 | FeesModule / `fee_payments` | Test | Specified |
| FR-FEE-003 | Receipt generation and immutability | BG-003 | High | TC-FEE-003 | FeesModule / `receipts` | Test, Inspection | Specified |
| FR-FEE-004 | Automated fee reminders (D-7, D-1, D+7) | BG-003 | Medium | TC-FEE-004 | FeesModule / `fee_reminder_log` | Test | Specified |
| FR-FEE-005 | Refund workflow with owner approval | BG-003 | Medium | TC-FEE-005 | FeesModule / `refund_requests` | Test | Specified |
| FR-FEE-006 | Fee balance inquiry with arrears | BG-003 | High | TC-FEE-006 | FeesModule / `fee_payments` | Test | Specified |
| FR-FEE-007 | Financial reports (collection, defaulters) | BG-003 | Medium | TC-FEE-007 | FeesModule / ReportModule | Test | Specified |
| FR-ATT-001 | Daily attendance entry with duplicate check | BG-001 | High | TC-ATT-001 | AttendanceModule / `attendance_records` | Test | Specified |
| FR-ATT-002 | Consecutive absence alert SMS to parent | BG-001 | Medium | TC-ATT-002 | AttendanceModule / `sms_log` | Test | Specified |
| FR-ATT-003 | Attendance amendment with time-based rules | BG-001 | Medium | TC-ATT-003 | AttendanceModule / `attendance_records` | Test | Specified |
| FR-ATT-004 | Monthly attendance report (PDF/CSV) | BG-001 | Medium | TC-ATT-004 | AttendanceModule / ReportModule | Test | Specified |
| FR-EXM-001 | Exam configuration with subjects and deadline | BG-002 | High | TC-EXM-001 | ExamModule / `exams`, `exam_subjects` | Test | Specified |
| FR-EXM-002 | Mark entry validation with range and deadline | BG-002 | High | TC-EXM-002 | ExamModule / `exam_results` | Test | Specified |
| FR-EXM-003 | Mark entry deadline unlock by Head Teacher | BG-002 | Medium | TC-EXM-003 | ExamModule / `exams` | Test | Specified |
| FR-EXM-004 | PLE grade computation (aggregate, division) | BG-002 | Critical | TC-EXM-004 | ExamModule / `ple_results` | Test | Specified |
| FR-EXM-005 | UCE O-Level grade computation (9-point, div) | BG-002 | Critical | TC-EXM-005 | ExamModule / `uce_results` | Test | Specified |
| FR-EXM-006 | UACE A-Level grade computation (points) | BG-002 | Critical | TC-EXM-006 | ExamModule / `uace_results` | Test | Specified |
| FR-EXM-007 | Thematic curriculum competency descriptors | BG-002 | High | TC-EXM-007 | ExamModule / `thematic_results` | Test | Specified |
| FR-EXM-008 | UNEB candidate registration export | BG-002, BG-004 | High | TC-EXM-008 | ExamModule | Test | Specified |
| FR-RPT-001 | Single student report card generation | BG-002 | High | TC-RPT-001 | ReportModule / `report_cards` | Test | Specified |
| FR-RPT-002 | Bulk report card generation (200 in 120 s) | BG-002 | High | TC-RPT-002 | ReportModule / Laravel Horizon | Test | Specified |
| FR-RPT-003 | School performance summary report | BG-002 | Medium | TC-RPT-003 | ReportModule | Test | Specified |
| FR-RPT-004 | Head Teacher comment entry on report card | BG-002 | Medium | TC-RPT-004 | ReportModule / `report_cards` | Test | Specified |
| FR-RBAC-001 | Permission resolution with 6-step priority | BG-001 | High | TC-RBAC-001 | RBACModule / Redis cache | Test | Specified |
| FR-RBAC-002 | Role assignment with privilege escalation guard | BG-001 | High | TC-RBAC-002 | RBACModule / `tbl_user_roles` | Test | Specified |
| FR-RBAC-003 | User invitation and onboarding workflow | BG-001 | Medium | TC-RBAC-003 | RBACModule / `user_invitations` | Test | Specified |
| FR-RBAC-004 | Session and token expiry enforcement | BG-001 | High | TC-RBAC-004 | RBACModule / AuthModule | Test | Specified |
| FR-RBAC-005 | Super Admin cross-tenant access logging | BG-001 | High | TC-RBAC-005 | RBACModule / AuditModule | Test, Inspection | Specified |
| FR-EMIS-001 | EMIS student headcount export for MoES | BG-004 | High | TC-EMIS-001 | EMISModule / `school_enrollments` | Test | Specified |
| FR-EMIS-002 | EMIS staff data export | BG-004 | Medium | TC-EMIS-002 | EMISModule / `staff` | Test | Specified |
| FR-EMIS-003 | EMIS learner summary form export | BG-004 | Medium | TC-EMIS-003 | EMISModule / `school_enrollments` | Test | Specified |
| FR-AUD-001 | Immutable audit log with 7-year retention | BG-001, BG-003 | High | TC-AUD-001 | AuditModule / `audit_logs` | Test, Inspection | Specified |
| FR-PROM-001 | Class-to-class promotion mapping | BG-001 | High | TC-PROM-001 | PromotionModule / `classes` | Test | Specified |
| FR-PROM-002 | Promotion wizard auto-launch on year create | BG-001 | High | TC-PROM-002 | PromotionModule / `promotion_wizard_sessions` | Test | Specified |
| FR-PROM-003 | Bulk promotion with selective override | BG-001 | High | TC-PROM-003 | PromotionModule / `school_enrollments` | Test | Specified |
| FR-PROM-004 | Wizard skip with reason and force flag | BG-001 | Medium | TC-PROM-004 | PromotionModule / `promotion_wizard_sessions` | Test | Specified |
| FR-PROM-005 | Historical academic year record lock | BG-001 | High | TC-PROM-005 | PromotionModule / `academic_years` | Test | Specified |
| FR-PROM-006 | Promotion wizard draft persistence | BG-001 | Medium | TC-PROM-006 | PromotionModule / `promotion_wizard_sessions` | Test | Specified |
| FR-PROM-007 | Term 1 open gate blocks until wizard done | BG-001 | High | TC-PROM-007 | PromotionModule / `terms` | Test | Specified |
| FR-DEPART-001 | Student departure recording with archival | BG-001, BG-005 | High | TC-DEPART-001 | DepartureModule / `school_departures` | Test | Specified |
| FR-DEPART-002 | Deceased student global identity lock | BG-001 | High | TC-DEPART-002 | DepartureModule / `global_students` | Test | Specified |
| FR-DEPART-003 | Expelled flag privacy in cross-school lookup | BG-001 | High | TC-DEPART-003 | DepartureModule / SISModule | Test | Specified |
| FR-DEPART-004 | Departure reason update with audit trail | BG-001 | Medium | TC-DEPART-004 | DepartureModule / `school_departures` | Test | Specified |
| FR-HIST-001 | Student history tab — school list (global) | BG-005 | High | TC-HIST-001 | HistoryModule / `school_enrollments` | Test | Specified |
| FR-HIST-002 | Student history — record access (read-only) | BG-005 | High | TC-HIST-002 | HistoryModule | Test | Specified |
| FR-HIST-003 | Student history — write operation block | BG-005 | High | TC-HIST-003 | HistoryModule | Test | Specified |
| FR-SHARE-001 | Inter-school record request creation | BG-005 | High | TC-SHARE-001 | SharingModule / `record_requests` | Test | Specified |
| FR-SHARE-002 | Student consent response with per-item control | BG-005 | High | TC-SHARE-002 | SharingModule / `record_requests` | Test | Specified |
| FR-SHARE-003 | Student consent expiry after 7 days | BG-005 | Medium | TC-SHARE-003 | SharingModule / scheduled job | Test | Specified |
| FR-SHARE-004 | Source school approval (subset of consent) | BG-005 | High | TC-SHARE-004 | SharingModule / `record_requests` | Test | Specified |
| FR-SHARE-005 | Source school denial with notifications | BG-005 | Medium | TC-SHARE-005 | SharingModule / `record_requests` | Test | Specified |
| FR-SHARE-006 | School B record access within time window | BG-005 | High | TC-SHARE-006 | SharingModule / `record_requests` | Test | Specified |
| FR-SHARE-007 | Access window expiry with auto-lock | BG-005 | Medium | TC-SHARE-007 | SharingModule / scheduled job | Test | Specified |
| FR-SHARE-008 | Student record request history view | BG-005 | Medium | TC-SHARE-008 | SharingModule / `record_requests` | Test | Specified |
| FR-APPLY-001 | School directory listing with filters | BG-005 | Medium | TC-APPLY-001 | ApplicationModule / `tenants` | Test | Specified |
| FR-APPLY-002 | Application submission (max 5 pending) | BG-005 | High | TC-APPLY-002 | ApplicationModule / `school_applications` | Test | Specified |
| FR-APPLY-003 | Admissions queue for school-side review | BG-005 | Medium | TC-APPLY-003 | ApplicationModule / `school_applications` | Test | Specified |
| FR-APPLY-004 | Application decision with student notification | BG-005 | High | TC-APPLY-004 | ApplicationModule / `school_applications` | Test | Specified |
| FR-APPLY-005 | Application retention purge after 2 years | BG-005 | Low | TC-APPLY-005 | ApplicationModule / scheduled job | Test | Specified |
| FR-ELEARN-001 | Study material file upload with malware scan and deduplication | BG-001, BG-006 | High | TC-ELEARN-001 | ELearnModule / `learning_materials` / Wasabi S3 | Test | Specified |
| FR-ELEARN-002 | Study material access log per student | BG-001, BG-006 | Medium | TC-ELEARN-002 | ELearnModule / `material_access_log` | Test | Specified |
| FR-ELEARN-003 | Assignment creation and FCM/SMS notification | BG-001, BG-006 | High | TC-ELEARN-003 | ELearnModule / `assignments` | Test | Specified |
| FR-ELEARN-004 | Student submission with server-side timestamp and late policy | BG-001, BG-006 | High | TC-ELEARN-004 | ELearnModule / `submissions` | Test | Specified |
| FR-ELEARN-005 | Plagiarism detection at 80% similarity threshold | BG-001, BG-006 | Medium | TC-ELEARN-005 | ELearnModule / `plagiarism_alerts` | Test | Specified |
| FR-ELEARN-006 | Teacher marking with rubric scoring and gradebook auto-post | BG-001, BG-006 | High | TC-ELEARN-006 | ELearnModule / `marks_register` | Test | Specified |
| FR-ELEARN-007 | Online quiz creation with question bank and randomisation | BG-001, BG-006 | High | TC-ELEARN-007 | ELearnModule / `quizzes` / `quiz_questions` | Test | Specified |
| FR-ELEARN-008 | Auto-grading of MCQ, True/False, and Numeric questions | BG-001, BG-006 | High | TC-ELEARN-008 | ELearnModule / `quiz_attempts` | Test | Specified |
| FR-ELEARN-009 | Quiz timer persistence through connectivity loss | BG-001, BG-006 | High | TC-ELEARN-009 | ELearnModule / `quiz_attempts` | Test (device simulation) | Specified |
| FR-ELEARN-010 | Head Teacher e-learning compliance report | BG-001, BG-006 | Medium | TC-ELEARN-010 | ELearnModule / aggregate query | Test | Specified |
| FR-ELEARN-011 | Storage quota enforcement with 90% warning alert | BG-001, BG-006 | High | TC-ELEARN-011 | ELearnModule / `tenant_storage_usage` | Test | Specified |

### 2.2 Non-Functional Requirements

| Req ID | Requirement Summary | Source (BG-ID) | Priority | Test Case ID(s) | Design Element | Verification Method | Status |
|---|---|---|---|---|---|---|---|
| EDU-NFR-001 | Student record confidentiality (PDPO) | BG-001 | High | TC-NFR-001 | RBACModule / AuditModule | Test, Inspection | Specified |
| EDU-NFR-002 | WCAG 2.1 AA web accessibility | BG-001, BG-005 | High | TC-NFR-002 | All web portal modules | Test (Axe CI), Inspection | Specified |
| EDU-NFR-003 | Minor data protection (parental consent) | BG-001 | High | TC-NFR-003 | SISModule / AuditModule | Test | Specified |
| EDU-NFR-004 | 7-year student record retention | BG-001 | High | TC-NFR-004 | SISModule / `global_students` | Test | Specified |
| EDU-NFR-005 | 99.9% uptime during exam periods | BG-002 | Critical | TC-NFR-005 | ExamModule / AttendanceModule / FeesModule | Analysis (Uptime Robot) | Specified |
| UG-NFR-001 | UNEB grading engine 100% accuracy | BG-002 | Critical | TC-NFR-006 | ExamModule | Test (UNEB sample data) | Specified |
| UG-NFR-002 | EMIS export MoES schema compliance | BG-004 | High | TC-NFR-007 | EMISModule | Test (schema validation) | Specified |
| UG-NFR-003 | Uganda 3-term calendar enforcement | BG-001, BG-002 | High | TC-NFR-008 | AcademicsModule / `terms` | Test | Specified |
| UG-NFR-004 | Offline attendance and mark entry (5 min sync) | BG-001 | High | TC-NFR-009 | AttendanceModule / ExamModule (PWA) | Test (device simulation) | Specified |
| UG-NFR-005 | Multi-tenant data isolation | BG-001, BG-005 | Critical | TC-NFR-010 | TenantModule / all modules | Test (cross-tenant probing) | Specified |
| UG-NFR-006 | Fee payment idempotency (0 duplicates) | BG-003 | Critical | TC-NFR-011 | FeesModule / `fee_payments` | Test | Specified |
| UG-NFR-007 | API P95 response ≤ 500 ms (CRUD), ≤ 3 s (report) | BG-001 | High | TC-NFR-012 | All API modules | Test (k6 load test) | Specified |
| UG-NFR-008 | AES-256 at rest, TLS 1.3 in transit | BG-001 | Critical | TC-NFR-013 | Infrastructure / all modules | Test (nmap), Inspection | Specified |

---

## 3 Coverage Summary

| Category | Total Requirements | Linked to BG | Linked to Test Case | Linked to Design Element | Coverage % |
|---|---|---|---|---|---|
| Functional (FR) | 62 | 62 | 62 | 62 | 100% |
| Non-Functional (NFR) | 13 | 13 | 13 | 13 | 100% |
| **Total** | **75** | **75** | **75** | **75** | **100%** |

**Business Goal Coverage:**

| Business Goal | FR Count | NFR Count | Total |
|---|---|---|---|
| BG-001: 500 Uganda schools in 24 months | 50 | 9 | 59 |
| BG-002: Automated UNEB report cards | 14 | 3 | 17 |
| BG-003: 90%+ fee reconciliation rate | 8 | 1 | 9 |
| BG-004: EMIS/MoES integration | 4 | 1 | 5 |
| BG-005: Expand to 3+ African countries | 18 | 2 | 20 |
| BG-006: In-school e-learning and assignment management | 11 | 0 | 11 |

*Note: Requirements may map to multiple business goals; counts reflect all linkages.*

---

## 4 Forward Traceability (Requirements to Design to Test)

Forward traceability confirms that every requirement has a design realisation and at least one test case.

| Trace Path | Count | Status |
|---|---|---|
| FR → HLD Module | 51/51 | Complete |
| FR → DB Table / Component | 51/51 | Complete |
| FR → Test Case (TC-*) | 51/51 | Complete |
| NFR → HLD Module / Infrastructure | 13/13 | Complete |
| NFR → Test Case (TC-NFR-*) | 13/13 | Complete |

**Module-to-Requirement Mapping:**

| HLD Module | Requirement IDs | Count |
|---|---|---|
| AuthModule | FR-AUTH-001 to FR-AUTH-006, FR-RBAC-004 | 7 |
| TenantModule | FR-TNT-001 to FR-TNT-003, UG-NFR-005 | 4 |
| SISModule | FR-SIS-001 to FR-SIS-005, EDU-NFR-001, EDU-NFR-003, EDU-NFR-004 | 8 |
| AcademicsModule | FR-ACA-001 to FR-ACA-004, UG-NFR-003 | 5 |
| FeesModule | FR-FEE-001 to FR-FEE-007, UG-NFR-006 | 8 |
| AttendanceModule | FR-ATT-001 to FR-ATT-004, UG-NFR-004 | 5 |
| ExamModule | FR-EXM-001 to FR-EXM-008, UG-NFR-001, EDU-NFR-005 | 10 |
| ReportModule | FR-RPT-001 to FR-RPT-004 | 4 |
| RBACModule | FR-RBAC-001 to FR-RBAC-005, EDU-NFR-001 | 6 |
| EMISModule | FR-EMIS-001 to FR-EMIS-003, UG-NFR-002 | 4 |
| AuditModule | FR-AUD-001, FR-RBAC-005 | 2 |
| PromotionModule | FR-PROM-001 to FR-PROM-007 | 7 |
| DepartureModule | FR-DEPART-001 to FR-DEPART-004 | 4 |
| HistoryModule | FR-HIST-001 to FR-HIST-003 | 3 |
| SharingModule | FR-SHARE-001 to FR-SHARE-008 | 8 |
| ApplicationModule | FR-APPLY-001 to FR-APPLY-005 | 5 |
| ELearnModule | FR-ELEARN-001 to FR-ELEARN-011 | 11 |

---

## 5 Backward Traceability (Test to Requirement to Business Goal)

Backward traceability confirms that every test case traces to a requirement and every requirement traces to a business goal.

| Test Case ID | Requirement ID | Business Goal(s) |
|---|---|---|
| TC-AUTH-001 | FR-AUTH-001 | BG-001 |
| TC-AUTH-002 | FR-AUTH-002 | BG-001, BG-005 |
| TC-AUTH-003 | FR-AUTH-003 | BG-001 |
| TC-AUTH-004 | FR-AUTH-004 | BG-001 |
| TC-AUTH-005 | FR-AUTH-005 | BG-001 |
| TC-AUTH-006 | FR-AUTH-006 | BG-001 |
| TC-TNT-001 | FR-TNT-001 | BG-001, BG-005 |
| TC-TNT-002 | FR-TNT-002 | BG-001 |
| TC-TNT-003 | FR-TNT-003 | BG-001 |
| TC-SIS-001 | FR-SIS-001 | BG-001, BG-005 |
| TC-SIS-002 | FR-SIS-002 | BG-005 |
| TC-SIS-003 | FR-SIS-003 | BG-001 |
| TC-SIS-004 | FR-SIS-004 | BG-005 |
| TC-SIS-005 | FR-SIS-005 | BG-001 |
| TC-ACA-001 | FR-ACA-001 | BG-001, BG-002 |
| TC-ACA-002 | FR-ACA-002 | BG-001 |
| TC-ACA-003 | FR-ACA-003 | BG-002 |
| TC-ACA-004 | FR-ACA-004 | BG-001 |
| TC-FEE-001 | FR-FEE-001 | BG-003 |
| TC-FEE-002 | FR-FEE-002 | BG-003 |
| TC-FEE-003 | FR-FEE-003 | BG-003 |
| TC-FEE-004 | FR-FEE-004 | BG-003 |
| TC-FEE-005 | FR-FEE-005 | BG-003 |
| TC-FEE-006 | FR-FEE-006 | BG-003 |
| TC-FEE-007 | FR-FEE-007 | BG-003 |
| TC-ATT-001 | FR-ATT-001 | BG-001 |
| TC-ATT-002 | FR-ATT-002 | BG-001 |
| TC-ATT-003 | FR-ATT-003 | BG-001 |
| TC-ATT-004 | FR-ATT-004 | BG-001 |
| TC-EXM-001 | FR-EXM-001 | BG-002 |
| TC-EXM-002 | FR-EXM-002 | BG-002 |
| TC-EXM-003 | FR-EXM-003 | BG-002 |
| TC-EXM-004 | FR-EXM-004 | BG-002 |
| TC-EXM-005 | FR-EXM-005 | BG-002 |
| TC-EXM-006 | FR-EXM-006 | BG-002 |
| TC-EXM-007 | FR-EXM-007 | BG-002 |
| TC-EXM-008 | FR-EXM-008 | BG-002, BG-004 |
| TC-RPT-001 | FR-RPT-001 | BG-002 |
| TC-RPT-002 | FR-RPT-002 | BG-002 |
| TC-RPT-003 | FR-RPT-003 | BG-002 |
| TC-RPT-004 | FR-RPT-004 | BG-002 |
| TC-RBAC-001 | FR-RBAC-001 | BG-001 |
| TC-RBAC-002 | FR-RBAC-002 | BG-001 |
| TC-RBAC-003 | FR-RBAC-003 | BG-001 |
| TC-RBAC-004 | FR-RBAC-004 | BG-001 |
| TC-RBAC-005 | FR-RBAC-005 | BG-001 |
| TC-EMIS-001 | FR-EMIS-001 | BG-004 |
| TC-EMIS-002 | FR-EMIS-002 | BG-004 |
| TC-EMIS-003 | FR-EMIS-003 | BG-004 |
| TC-AUD-001 | FR-AUD-001 | BG-001, BG-003 |
| TC-PROM-001 | FR-PROM-001 | BG-001 |
| TC-PROM-002 | FR-PROM-002 | BG-001 |
| TC-PROM-003 | FR-PROM-003 | BG-001 |
| TC-PROM-004 | FR-PROM-004 | BG-001 |
| TC-PROM-005 | FR-PROM-005 | BG-001 |
| TC-PROM-006 | FR-PROM-006 | BG-001 |
| TC-PROM-007 | FR-PROM-007 | BG-001 |
| TC-DEPART-001 | FR-DEPART-001 | BG-001, BG-005 |
| TC-DEPART-002 | FR-DEPART-002 | BG-001 |
| TC-DEPART-003 | FR-DEPART-003 | BG-001 |
| TC-DEPART-004 | FR-DEPART-004 | BG-001 |
| TC-HIST-001 | FR-HIST-001 | BG-005 |
| TC-HIST-002 | FR-HIST-002 | BG-005 |
| TC-HIST-003 | FR-HIST-003 | BG-005 |
| TC-SHARE-001 | FR-SHARE-001 | BG-005 |
| TC-SHARE-002 | FR-SHARE-002 | BG-005 |
| TC-SHARE-003 | FR-SHARE-003 | BG-005 |
| TC-SHARE-004 | FR-SHARE-004 | BG-005 |
| TC-SHARE-005 | FR-SHARE-005 | BG-005 |
| TC-SHARE-006 | FR-SHARE-006 | BG-005 |
| TC-SHARE-007 | FR-SHARE-007 | BG-005 |
| TC-SHARE-008 | FR-SHARE-008 | BG-005 |
| TC-APPLY-001 | FR-APPLY-001 | BG-005 |
| TC-APPLY-002 | FR-APPLY-002 | BG-005 |
| TC-APPLY-003 | FR-APPLY-003 | BG-005 |
| TC-APPLY-004 | FR-APPLY-004 | BG-005 |
| TC-APPLY-005 | FR-APPLY-005 | BG-005 |
| TC-ELEARN-001 | FR-ELEARN-001 | BG-001, BG-006 |
| TC-ELEARN-002 | FR-ELEARN-002 | BG-001, BG-006 |
| TC-ELEARN-003 | FR-ELEARN-003 | BG-001, BG-006 |
| TC-ELEARN-004 | FR-ELEARN-004 | BG-001, BG-006 |
| TC-ELEARN-005 | FR-ELEARN-005 | BG-001, BG-006 |
| TC-ELEARN-006 | FR-ELEARN-006 | BG-001, BG-006 |
| TC-ELEARN-007 | FR-ELEARN-007 | BG-001, BG-006 |
| TC-ELEARN-008 | FR-ELEARN-008 | BG-001, BG-006 |
| TC-ELEARN-009 | FR-ELEARN-009 | BG-001, BG-006 |
| TC-ELEARN-010 | FR-ELEARN-010 | BG-001, BG-006 |
| TC-ELEARN-011 | FR-ELEARN-011 | BG-001, BG-006 |
| TC-NFR-001 | EDU-NFR-001 | BG-001 |
| TC-NFR-002 | EDU-NFR-002 | BG-001, BG-005 |
| TC-NFR-003 | EDU-NFR-003 | BG-001 |
| TC-NFR-004 | EDU-NFR-004 | BG-001 |
| TC-NFR-005 | EDU-NFR-005 | BG-002 |
| TC-NFR-006 | UG-NFR-001 | BG-002 |
| TC-NFR-007 | UG-NFR-002 | BG-004 |
| TC-NFR-008 | UG-NFR-003 | BG-001, BG-002 |
| TC-NFR-009 | UG-NFR-004 | BG-001 |
| TC-NFR-010 | UG-NFR-005 | BG-001, BG-005 |
| TC-NFR-011 | UG-NFR-006 | BG-003 |
| TC-NFR-012 | UG-NFR-007 | BG-001 |
| TC-NFR-013 | UG-NFR-008 | BG-001 |

---

## 6 Gap Analysis

### 6.1 Requirements Without Full Test Specification

| Req ID | Gap Description | Remediation |
|---|---|---|
| FR-EXM-008 | Partially resolved — core UNEB candidate fields documented from EMIS secondary manual. Exact UNEB registration file format still requires UNEB liaison. | Obtain official UNEB candidate registration CSV/XML column specification for full closure; core fields sufficient for initial implementation. |

*Note: FR-EMIS-001 context gap (MoES EMIS data dictionary) has been fully resolved. A complete EMIS data dictionary was created from 5 official MoES documents. FR-EMIS-002 and FR-EMIS-003 were added as part of this resolution.*

### 6.2 Requirements Without Complete Design Specification

No gaps detected. All 62 requirements map to at least one HLD module and one database table or infrastructure component.

### 6.3 Business Goals Without Direct Requirements

No gaps detected. All 5 business goals have at least 3 requirements tracing to them.

---

## 7 Orphan Detection Report

### 7.1 Orphan Requirements (No Business Goal Link)

None detected. All 64 requirements trace to at least one business goal.

### 7.2 Orphan Test Cases (No Requirement Link)

None detected. All 77 test case IDs (TC-AUTH-001 through TC-NFR-013) trace to exactly one requirement.

### 7.3 Orphan Design Elements (No Requirement Link)

None detected. All 16 HLD modules trace to at least one requirement.

---

## 8 Traceability Metrics

$$CoveragePercent = \frac{LinkedReqs}{TotalReqs} \times 100$$

| Metric | Value |
|---|---|
| Total requirements | 75 |
| Requirements linked to business goals | 75 |
| Requirements linked to test cases | 75 |
| Requirements linked to design elements | 75 |
| Forward traceability coverage | $\frac{75}{75} \times 100 = 100\%$ |
| Backward traceability coverage | $\frac{75}{75} \times 100 = 100\%$ |
| Requirements with context gaps | 1 (FR-EXM-008 — partially resolved, UNEB file format pending) |
| Orphan requirements | 0 |
| Orphan test cases | 0 |
| Orphan design elements | 0 |

---

## 9 Remediation Recommendations

1. **REM-001 — FR-EXM-008: Partially Resolved.** Core UNEB candidate fields have been documented from the EMIS secondary manual. The exact UNEB registration file format (CSV/XML column specification) still requires UNEB liaison for full closure. TC-EXM-008 can proceed with core field validation; final format compliance testing is deferred until the official specification is obtained.

2. **REM-002 — FR-EMIS-001: Resolved.** A complete EMIS data dictionary was created from 5 official MoES documents. FR-EMIS-001 is fully specified. Two additional requirements (FR-EMIS-002, FR-EMIS-003) were added to cover staff data export and learner summary form export respectively. TC-EMIS-001, TC-EMIS-002, TC-EMIS-003, and UG-NFR-002 acceptance testing can now proceed.

3. **Maintain RTM currency.** Update this matrix whenever a requirement is added, modified, or removed. Each update must re-verify forward and backward traceability and recalculate coverage metrics. *Last update: 2026-04-04 — added BG-006 (E-Learning) and FR-ELEARN-001 through FR-ELEARN-011 (11 requirements) for Module 21 Class Library and E-Learning delivered in Phase 2.*

4. **Baseline verification.** Upon resolving all context gaps, conduct a formal baseline verification per IEEE 1012-2016 Clause 9.2, confirming every requirement in this matrix is Correct, Unambiguous, Complete, and Verifiable before development commences.

5. **Audit log for RTM changes.** Record all RTM modifications in `docs/CHANGELOG.md` with the date, author, and affected requirement IDs to maintain auditability under ISO/IEC 15504.


---

## AI Module Traceability Extension

This section extends the Requirements Traceability Matrix (RTM) to cover the FR-AI requirements series. All FR-AI requirements were added following the AI module design review in April 2026.

### Business Goals Covered by FR-AI

| Business Goal ID | Business Goal | FR-AI Requirements |
|---|---|---|
| BG-AI-001 | Generate AI-powered add-on module revenue (UGX 50K–800K/month per school) | FR-AI-001 through FR-AI-007 |
| BG-AI-002 | Improve student academic outcomes by enabling early teacher intervention | FR-AI-001 |
| BG-AI-003 | Reduce teacher administrative burden on report card comment writing | FR-AI-002 |
| BG-AI-004 | Give school owners real-time operational intelligence without manual report navigation | FR-AI-003 |
| BG-AI-005 | Reduce school fee default rate through early identification of at-risk payers | FR-AI-004 |
| BG-AI-006 | Enable schools to systematically respond to parent feedback at scale | FR-AI-005 |

### FR-AI Forward Traceability (Requirement → Test Case)

| Requirement | Description | Test Case ID | Pass Criterion |
|---|---|---|---|
| FR-AI-001 | At-risk student weekly classification | TC-AI-001 | 5 pre-seeded high-risk students classified correctly; no student name in prompt |
| FR-AI-002 | Report card comment generation | TC-AI-002 | 10 suggested comments returned within 20 s; no comment saved without teacher Accept |
| FR-AI-003 | Weekly owner briefing | TC-AI-003 | Briefing delivered by 07:00 EAT Monday; contains no student UIDs or names |
| FR-AI-004 | Fee default prediction | TC-AI-004 | 10 pre-seeded high-risk payers classified; `pii_scrubbed = 1` in all audit log rows |
| FR-AI-005 | Parent sentiment analysis | TC-AI-005 | 20 responses classified correctly; multi-language (Luganda) handled without error |
| FR-AI-006 | AI module activation | TC-AI-006 | Module activated; 9 feature rows seeded; duplicate activation returns HTTP 409 |
| FR-AI-007 | Budget alert and enforcement | TC-AI-007 | 80% alert fires at correct threshold; 100% block enforced; duplicate alert prevented |

### FR-AI Backward Traceability (Requirement → Source)

| Requirement | Source Document | Source Section |
|---|---|---|
| FR-AI-001 | AI Opportunity Canvas (SRS Skills) | Pattern 2 — Predictive Alerts; school domain at-risk pattern |
| FR-AI-002 | AI Opportunity Canvas (SRS Skills) | Pattern 1 — Smart Summarisation; school domain report card narrative |
| FR-AI-003 | AI Analytics Dashboards (SRS Skills) | AI Executive Summary Card pattern |
| FR-AI-004 | AI Predictive Analytics (SRS Skills) | Fee default prediction domain template |
| FR-AI-005 | AI NLP Analytics (SRS Skills) | Feature 1 — Sentiment Analysis; Feature 4 — Theme Detection |
| FR-AI-006 | AI Metering and Billing (SRS Skills) | Gate activation API pattern |
| FR-AI-007 | AI Architecture Patterns (SRS Skills) | BudgetGuard pattern; alert threshold enforcement |

### AI NFR Traceability

| NFR | Description | Test Case | Source |
|---|---|---|---|
| AI-NFR-001 | AI Insights panel ≤ 8 s at P95 | TC-AINF-001 | ai-analytics-dashboards skill — performance requirements |
| AI-NFR-002 | Token ledger write ≤ 200 ms at P95 | TC-AINF-002 | ai-metering-billing skill — metering latency |
| AI-NFR-003 | AI Service availability 99.5%; failover ≤ 30 s | TC-AINF-003 | ai-architecture-patterns skill — provider abstraction |
| AI-NFR-004 | Batch jobs complete by 07:00 EAT | TC-AINF-004 | ai-predictive-analytics skill — batch processing guidance |
| AI-NFR-005 | PIIScrubber 100% detection rate | TC-AINF-005 | ai-security skill — PIIScrubber patterns |
| AI-NFR-006 | JSON output validated before DB write | TC-AINF-006 | ai-security skill — output validation |
| AI-NFR-007 | BudgetGuard ≤ 50 ms at P95 | TC-AINF-007 | ai-architecture-patterns skill — BudgetGuard |
| AI-NFR-008 | ai_audit_log retained 7 years, immutable | TC-AINF-008 | DPPA 2019 Section 26; ai-security skill — audit log |

### Coverage Metrics Update

The addition of 7 FR-AI requirements and 8 AI-NFR requirements increases the total requirement count:

| Category | Previous Count | Added | New Total |
|---|---|---|---|
| Functional Requirements (FR-*) | varies by last update | +7 (FR-AI-001 to FR-AI-007) | +7 |
| Non-Functional Requirements (NFR-*) | varies | +8 (AI-NFR-001 to AI-NFR-008) | +8 |

All 15 new requirements have forward traceability to test cases and backward traceability to source documents. No `[TRACE-GAP]` flags exist for the FR-AI series at the time of this update (2026-04-07).

# Glossary — Academia Pro

All terms follow IEEE Std 610.12-1990 definition format. Every domain-specific term used in any SRS section or design document must appear here. Flag undefined terms with `[GLOSSARY-GAP: <term>]`.

---

- **Academic Year:** The 12-month period, typically January–December in Uganda, during which a school conducts its 3 teaching terms.

- **Aggregate (UNEB):** The numeric sum of grades across a defined set of subjects used to determine a candidate's division. See BR-UNEB-001 (PLE) and BR-UNEB-002 (UCE).

- **Airtel Money:** Mobile money service operated by Airtel Uganda, used as a payment channel for school fees.

- **Attendance Status:** One of four values — Present, Absent, Late, Excused — recorded per student per school day.

- **BoU:** Bank of Uganda — the central bank and financial regulator of Uganda. Issues Payment Systems Operator licences required for direct mobile money processing.

- **Bursar:** The school staff member responsible for fee collection, payment recording, and financial reporting.

- **COPPA:** Children's Online Privacy Protection Act (U.S.) — noted as a US-specific regulation; the Uganda equivalent is the Data Protection and Privacy Act 2019 (PDPO).

- **Division (UNEB):** The classification awarded to a candidate based on their aggregate score. Divisions: I (highest), II, III, IV, Unclassified/Ungraded. Specific ranges per curriculum level defined in BR-UNEB-001, BR-UNEB-002, BR-UNEB-003.

- **EMIS:** Education Management Information System — the Uganda Ministry of Education and Sports (MoES) data platform for school statistics, student headcounts, and teacher records.

- **Enrollment:** The formal registration of a student at a specific school for a specific academic year, represented by a record in the `school_enrollments` table linking a `student_uid` to a `tenant_id`.

- **FCM:** Firebase Cloud Messaging — the push notification service used for Android and iOS app alerts.

- **FERPA:** Family Educational Rights and Privacy Act (U.S.) — noted as a US-specific regulation; the Uganda equivalent for student record privacy is the PDPO 2019.

- **FR:** Functional Requirement — a statement of system behaviour in stimulus-response format following the IEEE 830 "The system shall..." convention.

- **Global Student Identity:** The architecture ensuring a student's core identity record (UID, NIN, LIN, name, DOB) exists once across all Academia Pro tenants, without duplication, enabling cross-school lookup and transfer.

- **Grade:** The performance descriptor assigned to a student for a subject in an exam. Grading scales vary by curriculum level — see BR-UNEB-001 through BR-UNEB-004.

- **Head Teacher:** The senior school administrator responsible for academic oversight, staff management, and statutory reporting. Equivalent to "Principal" in some jurisdictions.

- **JWT:** JSON Web Token — the authentication token format used by Laravel Sanctum. Every JWT payload includes `tenant_id` and `user_id` claims.

- **KUPAA:** A Ugandan micro-payment model (researched in the master document) enabling partial fee payments with no minimum floor, community payment agents, and pre-term instalment plans.

- **Laravel:** PHP web application framework (version 11) used for the Academia Pro backend.

- **LIN:** Learner Identification Number — a unique identifier assigned to students by the Uganda MoES NEMIS system. Used for cross-school global identity lookup.

- **MoES:** Ministry of Education and Sports (Uganda) — the government body responsible for education regulation, EMIS reporting, and UNEB oversight.

- **MTN MoMo:** MTN Mobile Money — Uganda's largest mobile money service, used as a payment channel for school fees. API integration planned for Phase 3.

- **Multi-tenant SaaS:** Software as a Service architecture where a single application instance serves multiple independent client organisations (tenants), each with logically isolated data.

- **NEMIS:** National Education Management Information System (Uganda/Kenya). In Uganda context: MoES's student registration database. Used as source for LIN assignment.

- **NFR:** Non-Functional Requirement — a quality constraint on system behaviour (performance, security, availability, etc.), expressed with measurable metrics per IEEE 830.

- **NIN:** National Identification Number — the biometric identity number issued by the Uganda National Identification and Registration Authority (NIRA) to citizens aged 16 and above.

- **PDPO:** Uganda Personal Data Protection and Privacy Act 2019 — the primary data privacy law in Uganda governing collection, processing, storage, and transfer of personal data. See BR-DP-001 through BR-DP-004 and `_context/gap-analysis.md` HIGH-008.

- **PIF:** Project Input Folder — the `_context/` directory; the living repository of project-specific context that feeds every skill execution.

- **PLE:** Primary Leaving Examinations — Uganda's national examinations for P7 (Primary 7) students, administered by UNEB. Grading defined in BR-UNEB-001.

- **Portal:** A role-scoped web interface for a specific stakeholder group (Super Admin, Owner/Director, Teacher, Student, Parent).

- **Receipt:** A system-generated document confirming a fee payment, numbered sequentially per school, linked to a student, term, and payment channel. Receipts are immutable after generation.

- **Repository Pattern:** A software design pattern that abstracts data access logic. In Academia Pro, every database query is routed through a Repository class that enforces `tenant_id` scoping before execution.

- **RBAC:** Role-Based Access Control — the permission model where users are assigned roles, and roles are granted permissions to perform specific actions on specific resources.

- **SchoolPay:** Uganda's dominant school fee payment platform (15,000+ schools; BoU licensed). Academia Pro integrates via their open API as a payment partner in Phase 1–2.

- **SRS:** Software Requirements Specification — a document that describes the complete behaviour of a software system, following IEEE 830 conventions.

**student_uid:** The globally unique identifier (UUID) assigned to a student at first admission to any Academia Pro school. Persists for the student's lifetime regardless of school transfers.

- **Tenant:** An individual school organisation subscribed to Academia Pro. Identified by a unique `tenant_id` integer in the database.

**tenant_id:** The integer foreign key present on every tenant-scoped database table, used to enforce row-level data isolation between schools.

- **Term:** One of three instructional periods in the Uganda academic year (Term 1, Term 2, Term 3). The primary billing and reporting unit.

- **Thematic Curriculum:** Uganda's competency-based curriculum for P1–P3 students, assessed using descriptors (Highly Competent, Competent, Not Yet Competent) rather than numeric grades.

- **UACE:** Uganda Advanced Certificate of Education — A-Level examinations for Senior 6 (S6) students, administered by UNEB. Grading defined in BR-UNEB-003.

- **UCE:** Uganda Certificate of Education — O-Level examinations for Senior 4 (S4) students, administered by UNEB. Grading defined in BR-UNEB-002.

- **UNEB:** Uganda National Examinations Board — the government body that administers PLE, UCE, and UACE national examinations and publishes official grading rules.

- **URSB:** Uganda Registration Services Bureau — the government body for intellectual property registration, including software copyright under the Uganda Copyright Act 2006.

- **USSD:** Unstructured Supplementary Service Data — a GSM protocol used for feature-phone-accessible services (e.g., fee balance inquiry via short code). Planned for Phase 11.

- **UGX:** Uganda Shilling — the official currency of Uganda. All fee amounts in Academia Pro are stored and displayed in UGX unless the tenant is a foreign-currency school (Phase 11+).

- **V&V:** Verification and Validation — the IEEE 1012 process of confirming that requirements are correct, consistent, complete, and verifiable before development begins.

- **Water-Scrum-Fall:** A hybrid software development methodology combining formal upfront requirements phases (Waterfall) with iterative delivery sprints (Scrum) and formal phase gate sign-offs. Confirmed methodology for Academia Pro.

- **EMIS:** Education Management Information System — the web-based portal operated by MoES for collecting and managing education data from all schools in Uganda (https://emis.go.ug/).

- **LIN:** Learner Identification Number — a unique identifier auto-generated by the EMIS system for every registered learner, used alongside NIN for cross-system identification.

- **NIRA:** National Identification and Registration Authority — the government body that manages NIN issuance and verification in Uganda.

- **IPPS:** Integrated Personnel and Payroll System — the government system for managing civil servant payroll; teachers on the government payroll are identified by their IPPS Number.

- **TMIS:** Teacher Management Information System — an MoES system for tracking teacher records; teachers are identified by their TMIS Number.

- **EMIS Number:** A unique numeric identifier assigned to each education institution by MoES.

- **SMC:** School Management Committee — the governance body for primary schools in Uganda.

- **UNEB Centre Number:** A unique identifier assigned by UNEB to each examination centre (school) for examination registration and result processing.

- **USE:** Universal Secondary Education — a Uganda government programme providing free secondary education.

- **UPOLET:** Universal Post O-Level Education and Training — a Uganda government programme for post-O-Level education.

- **BrightSoma:** A curriculum-aligned digital content and AI tutoring platform that integrates with Academia Pro via API. BrightSoma handles multi-school content distribution and AI tutoring; Academia Pro handles in-school assignment management and resource organisation. The two are complementary, not interchangeable.

- **CAT:** Continuous Assessment Test — a scheduled in-class assessment contributing to a student's term marks. Distinct from homework, projects, and terminal examinations. Maps to a specific column in the school's marks register.

- **CDN:** Content Delivery Network — a geographically distributed network of servers that caches and delivers files from edge nodes closer to the end user. Used in Academia Pro to reduce file download latency for students on slow connections in Uganda.

- **Class Library:** The subject-level repository of study materials organised by class, subject, topic, and term. Each enrolled student accesses their class library via the student portal or mobile app.

- **Gradebook:** The digital marks register that aggregates all assessment scores — homework, CATs, projects, practicals, and exams — into a term-level record per student per subject. Assignment marks auto-post to the gradebook when the teacher publishes them.

- **HLS:** HTTP Live Streaming — an adaptive video streaming protocol used to deliver uploaded MP4 video files via CDN. Allows students to watch school-uploaded videos on slower connections without buffering the entire file.

- **NSubmit:** Not Submitted — the gradebook status assigned to a student who did not submit an assignment by the deadline (or resubmission window if applicable). Distinct from a zero mark; visible to the teacher and parent and does not automatically count as zero in weighted average calculations.

- **Plagiarism Flag:** A system-generated warning raised when a student's text submission is detected as more than 80% identical to another student's submission for the same assignment in the same class. The flag is advisory — it notifies the teacher and does not auto-penalise.

- **Question Bank:** A subject-level repository of quiz questions accumulated by a teacher over time. Questions in the bank can be reused and randomised across multiple quizzes without re-entry.

- **Rubric:** A marking scheme composed of named criteria, each with a maximum mark allocation. When a teacher attaches a rubric to an assignment, students see the criteria before submitting and teachers score per criterion when marking — the total auto-calculates.

- **Study Material:** Any resource (PDF, video link, uploaded MP4, audio file, PPTX, image, external link, or typed rich-text note) uploaded or linked by a teacher to a class library for student access.

- **Wasabi:** A cloud object storage provider compatible with the AWS S3 API. Recommended for Academia Pro file storage due to cost efficiency ($6/TB/month, no egress fees) versus AWS S3 — significant saving for an Africa-market SaaS with high PDF and audio file volumes.


---

## Architectural and Technical Terms

- **AcademiaPro:** The commercial product name of the multi-tenant SaaS school management platform authored by Chwezi Core Systems.
- **AI:** Artificial Intelligence. In Academia Pro, refers specifically to LLM-backed features gated behind the AI Module and the PII scrubber per ADR-0005.
- **ApplicationModule:** Laravel service provider that bootstraps the applicant enrolment domain (FR-APPLY-*).
- **ARPU:** Average Revenue Per User; core SaaS business metric.
- **AtRiskSchema:** Database schema fragment capturing tenants at risk of churn; populated nightly for retention dashboards.
- **AttendanceService:** Domain service orchestrating daily attendance capture and rolled-up reporting (FR-ATT-*).
- **AuditLog:** Append-only table recording sensitive actions; retention is 7 years per DPPA compliance.
- **AuthModule:** Laravel module handling Sanctum authentication, MFA, and session management (FR-AUTH-*).
- **AWS:** Amazon Web Services; the primary cloud hosting provider for Academia Pro production and staging.
- **BudgetGuard:** Runtime middleware that blocks AI calls when the per-tenant token ledger exceeds the configured monthly cap.
- **CloudFront:** AWS Content Delivery Network used to serve static assets and signed-URL document downloads.
- **CloudWatch:** AWS observability service integrated with PagerDuty for on-call paging.
- **CMS:** Content Management System.
- **CoveragePercent:** Aggregated percentage metric displayed on coverage-matrix dashboards.
- **CRDB:** Consolidated reference database used during data migration.
- **DevOps:** Cross-functional discipline integrating development and operations; Academia Pro uses a DevOps-light model with on-call rotation.
- **DOB:** Date of Birth; an S-tier personally identifiable field encrypted at rest.
- **DoD:** Definition of Done; the agile checklist required before a story is accepted.
- **DoR:** Definition of Ready; the agile checklist required before a story may enter a sprint.
- **DPA:** Data Processing Agreement; contractual terms between Academia Pro (processor) and each school tenant (controller).
- **DPIA:** Data Protection Impact Assessment; mandatory under Uganda DPPA Regulation 12 for high-risk processing.
- **DPO:** Data Protection Officer.
- **DPPA:** Uganda Data Protection and Privacy Act 2019; the controlling privacy regulation.
- **EAT:** East Africa Time (UTC+3).
- **EC2:** AWS Elastic Compute Cloud.
- **ECS:** AWS Elastic Container Service; runs Academia Pro Dockerised application on Fargate.
- **ElastiCache:** AWS-managed Redis used for session storage and Horizon queues.
- **EmisExportService:** Service producing the MoES EMIS annual return export file.
- **ERD:** Entity-Relationship Diagram.
- **ERP:** Enterprise Resource Planning.
- **ExamModule:** Laravel module handling internal tests and UNEB-aligned grading (FR-EXM-*).
- **FAQ:** Frequently Asked Questions; end-user help artefact.
- **FeeReminderService:** Queued job dispatching fee-balance reminders via SMS and email.
- **FeesModule:** Laravel module handling fee structures, invoices, and reconciliation (FR-FEE-*).
- **GitHub:** Source-control host for the Academia Pro repository.
- **GPS:** Global Positioning System; used for optional location tagging of offline attendance capture.
- **HistoryModule:** Module capturing append-only historical snapshots of student records for audit trails.
- **HLD:** High-Level Design document.
- **HSTS:** HTTP Strict Transport Security.
- **IAM:** Identity and Access Management.
- **ICT:** Information and Communication Technology.
- **IEC:** International Electrotechnical Commission.
- **IEEE:** Institute of Electrical and Electronics Engineers.
- **ImportStudentsJob:** Queued job consuming a CSV of legacy students and writing records with tenant scoping.
- **includeSubDomains:** HSTS directive so subdomains inherit the HSTS policy.
- **InnoDB:** The default MySQL storage engine used by Academia Pro; chosen for row-level locking and referential integrity.
- **InteractsWithQueue:** Laravel trait included on queued job classes exposing release, delete, and retry controls.
- **IP:** Internet Protocol.
- **ISO:** International Organization for Standardization.
- **KCPE:** Kenya Certificate of Primary Education.
- **KCSE:** Kenya Certificate of Secondary Education.
- **KES:** Kenyan Shilling.
- **KMS:** Key Management Service (AWS).
- **KPI:** Key Performance Indicator.
- **LLM:** Large Language Model; refers to the provider used by the AI Module per ADR-0005.
- **LMS:** Learning Management System.
- **LTS:** Long-Term Support release channel.
- **MacBook:** Laptop reference platform used for iOS development builds.
- **MBA:** Master of Business Administration.
- **MCQ:** Multiple-Choice Question.
- **MD5:** Message-Digest Algorithm 5; referenced for legacy compatibility only; never used for security-sensitive hashing.
- **MFA:** Multi-Factor Authentication.
- **MobileMoney:** Domain aggregate covering MTN MoMo and Airtel Money payment channels.
- **MockAIProvider:** Test double implementing the AI provider interface used in CI and local dev.
- **MoMo:** MTN Mobile Money.
- **MTN:** MTN Uganda; mobile-network operator for MoMo.
- **MTTF:** Mean Time To Failure.
- **MTTR:** Mean Time To Recovery.
- **MVVM:** Model-View-ViewModel UI architecture pattern; applied on Android and iOS clients.
- **MySQL:** The relational database management system chosen per ADR-0002.
- **NECTA:** Tanzania National Examinations Council.
- **NLP:** Natural Language Processing.
- **NPS:** Net Promoter Score.
- **OpenAI:** LLM provider option evaluated during AI Module provider selection.
- **OpenAPI:** API specification standard; see 03-design-documentation/03-api-spec/.
- **OTP:** One-Time Password.
- **OWASP:** Open Web Application Security Project; the OWASP Top 10 is the minimum security checklist for every release.
- **PBI:** Product Backlog Item.
- **PHP:** The programming language of the Laravel backend (PHP 8.2+).
- **PhpSpreadsheet:** PHP library used to produce Excel exports of fees, marks, and attendance.
- **PII:** Personally Identifiable Information.
- **PPTX:** Microsoft PowerPoint file format supported as an uploadable study material.
- **PR:** Pull Request.
- **PRD:** Product Requirements Document.
- **PSO:** Payment Systems Operator (BoU-licensed entity).
- **PurgeExpiredDataJob:** Scheduled job deleting records past retention per DPPA §30 fulfilment.
- **PWA:** Progressive Web App.
- **QR:** Quick Response code.
- **RDS:** AWS Relational Database Service (MySQL managed).
- **RPO:** Recovery Point Objective; target is 15 minutes.
- **RTM:** Requirements Traceability Matrix.
- **RTO:** Recovery Time Objective; target is 4 hours.
- **SaaS:** Software as a Service.
- **SchoolRangeTransactions:** Database partition-range used by the payment reconciliation job.
- **SendFeeReminderJob:** Queued job that assembles and dispatches a batched fee reminder.
- **SerializesModels:** Laravel trait serialising Eloquent models when a queued job is persisted.
- **SharingModule:** Module handling share-outs and announcement distribution.
- **ShouldQueue:** Laravel interface marking a class as queueable.
- **ShuleKeeper:** Named Uganda competitor product evaluated in the market analysis.
- **SIS:** Student Information System.
- **SLA:** Service Level Agreement.
- **SQL:** Structured Query Language.
- **StudentRepository:** Repository-layer class asserting tenant scope before returning student rows.
- **studentPaymentCode:** Generated short code printed on fee invoices so parents can reference a payment against a specific student.
- **SwiftUI:** Apple declarative UI framework used on iOS clients.
- **SyncSchoolTransactions:** Job reconciling MoMo and Airtel payment records into the fees ledger.
- **TenantAwareJob:** Base class for queued jobs that must re-hydrate the tenant context before running.
- **TenantModule:** Module defining tenancy lifecycle, provisioning, and off-boarding.
- **TOTP:** Time-based One-Time Password.
- **TTL:** Time To Live.
- **TypeScript:** The typed superset of JavaScript used for the React web client.
- **UAT:** User Acceptance Testing.
- **UCC:** Uganda Communications Commission.
- **UID:** Unique Identifier.
- **ULRC:** Uganda Law Reform Commission.
- **UPSIA:** Uganda Private Schools Association.
- **UptimeRobot:** Third-party synthetic monitoring service used as a second-source availability check.
- **USD:** United States Dollar.
- **UTC:** Coordinated Universal Time.
- **UUID:** Universally Unique Identifier.
- **ValidationException:** Laravel exception raised when inbound request validation fails; converted to a standard error envelope.
- **VPS:** Virtual Private Server.
- **WAEC:** West African Examinations Council.
- **WAF:** Web Application Firewall (Cloudflare).
- **WAMP64:** Windows-based local development stack used for Windows dev machines.
- **WCAG:** Web Content Accessibility Guidelines; target level AA.
- **withoutTenantScope:** Eloquent scope escape-hatch used only by platform-level jobs that must cross tenant boundaries.
- **withStudentSelfScope:** Query scope restricting a row set to rows owned by the calling student identity.
- **WorkManager:** Android Jetpack background-job scheduler used for offline-sync.
- **WSL2:** Windows Subsystem for Linux v2; supported local-dev path for Windows engineers.
- **YouTube:** Video hosting referenced for in-app help video links.
- **ZAP:** OWASP Zed Attack Proxy; CI security scanner.
- **ZIP:** Archive format used for evidence-pack bundles.

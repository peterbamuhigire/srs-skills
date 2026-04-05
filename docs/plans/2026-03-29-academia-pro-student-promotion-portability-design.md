---
title: "Academia Pro — Student Promotion, Departure, and Portability Design"
date: 2026-03-29
project: AcademiaPro
status: Approved
author: Peter (Chwezi Core Systems)
resolves: HIGH-004 (Academic Year Lifecycle), SRS amendment required
---

# Academia Pro — Student Promotion, Departure, and Portability Design

## Context

This document records the approved design decisions made on 2026-03-29 for:

1. **Year-Start Class Promotion Wizard** — how students advance between classes at the start of each academic year
2. **Unified Departure Model** — how students leave a school for any reason
3. **Cross-Tenant Student History** — how transferred students access their old school's records
4. **Inter-School Record Request System** — how schools formally share student records with each other
5. **In-Platform School Application** — how students apply to other schools on the platform

These decisions resolve gap **HIGH-004** from `_context/gap-analysis.md` and extend the SRS with new FR groups: `FR-PROM`, `FR-DEPART`, `FR-HIST`, `FR-SHARE`, and `FR-APPLY`.

---

## Decision 1: Year-Start Promotion Wizard

### Approved Approach

**Bulk promotion with selective override, enforced at academic year creation.**

When the Head Teacher creates a new academic year, the system immediately launches the Promotion Wizard. The wizard must be completed (or classes explicitly skipped) before Term 1 can be opened.

### Class-to-Class Mapping

Each class in Academics Setup has a **"Promotes To"** destination field configured once and reused every year.

- Final-year classes (P7, S.4, S.6) have `promotes_to = null` — the system treats this as a departure event (see Decision 2).
- If a class has no mapping configured, the wizard flags it: *"Promotion destination not set — configure before proceeding."*
- Multi-stream schools: multiple streams of the same level can each have independent destination mappings. Example: `P6 East → P7 East`, `P6 West → P7 West`.

### Wizard Flow

```
New Academic Year Created
        ↓
Promotion Wizard Launched (cannot dismiss — only save as draft)
        ↓
Class Queue Screen
  Shows all classes with counts and status:
    P1 — 42 students  [Start Promotion]  [Skip]
    P2 — 38 students  ✅ Done
    P7 — 31 students  [Start Graduation] [Skip]
        ↓
Per-Class Promotion Screen (non-final-year)
  Heading: "Promoting P5 (47 students) → P6"
  [☑ Promote All to P6] master toggle
  Student-by-student list with checkboxes
    ☑ Nakato Sarah       → P6
    ☑ Ssemakula John     → P6
    ☐ Okello David       → P5 (Repeating)   ← unchecked = stays
  Running tally: "47 promoting | 1 repeating"
  [Confirm Promotion]
        ↓
Per-Class Departure Screen (final-year classes)
  Heading: "P7 Departures (31 students)"
  [☑ Mark All as Completed Year]
  Student-by-student list:
    ☑ Byamukama Patrick  → Completed Year / Departed
    ☐ Nakimuli Ann       → P7 (Repeating)
  Departure reason dropdown per student (defaults to "Completed Year"):
    Completed Year | Transferred — On Platform | Transferred — External |
    Scholarship | Expelled | Withdrawn | Other
  [Confirm Departures]
        ↓
All Classes Done? → [Open Term 1] unlocked
```

### Blocking Rules

- Term 1 **cannot open** while any class has status `pending_promotion`.
- Only `✅ Done` (promoted) and `⏭ Skipped` (explicitly skipped) statuses unblock Term 1.
- The Skip option is for newly created classes or classes with zero prior-year students.
- Draft auto-saved after each class is confirmed — Head Teacher can close and return.

### Data Operations on Confirmation

For each **promoted** student:
- New `school_enrollments` record created: `student_uid`, `tenant_id`, `class_id` (destination), `academic_year_id` (new year), `status = active`.
- Old `school_enrollments` record updated: `status = completed`, `end_date = last day of final term`.

For each **repeating** student:
- New `school_enrollments` record created in the **same class** for the new academic year.
- Old enrollment marked `status = completed`.

For each **departing** student (final-year, see Decision 2):
- `school_departures` record created with reason code.
- Old enrollment marked `status = archived`.

### Historical Record Locking

All marks, attendance, and payment records for a completed academic year are **locked (immutable)** automatically 30 days after the last term's configured end date. The Head Teacher cannot manually trigger this — it is a scheduled system job. After locking:
- No mark amendments are accepted (HTTP 423 `YEAR_LOCKED`).
- No attendance amendments are accepted.
- Fee records remain editable only for refund processing.

A `promotion_events` audit record is created for the entire wizard session: `{initiated_by, academic_year_id, tenant_id, timestamp, classes_promoted, students_promoted, students_repeating, students_departed}`.

---

## Decision 2: Unified Departure Model

### Approved Approach

**"Graduate" is replaced by a unified "Left School" departure event with reason codes.**

Every student departure — regardless of cause — creates a `school_departures` record. The departure reason determines downstream behaviour.

### Departure Reason Codes

| Code | Label | Global ID Available for Re-enrolment? | Expelled Flag Visible to Other Schools? |
|---|---|---|---|
| `completed` | Completed Year (P7/S4/S6) | Yes | No |
| `transferred_platform` | Transferred — On Platform | Yes | No |
| `transferred_external` | Transferred — Off Platform | Yes | No |
| `scholarship` | Scholarship / Study Abroad | Yes | No |
| `expelled` | Expelled | Yes — but flagged | Via formal record request only |
| `withdrawn` | Withdrawn by Parent | Yes | No |
| `deceased` | Deceased | Locked — no future enrolment | No |
| `other` | Other (reason in notes field) | Yes | No |

### The Expelled Flag

When a student with a prior `expelled` departure is looked up by NIN/LIN at any school, the system shows a **neutral notice only**: *"This student has a prior enrolment record."* The departure reason is **not exposed** in the lookup.

The expelled reason is accessible only if the requesting school goes through the formal Inter-School Record Request workflow (Decision 4) and the student/parent consents to sharing the disciplinary record.

This protects the student from being permanently blacklisted by a school-lookup flag, while giving schools a legitimate pathway to the truth via consent-based disclosure.

### Deceased Students

Global identity record is locked: `global_students.status = deceased`. No future school can enrol this `student_uid`. The historical records remain accessible to the student's family via the originating school (requires a formal support request to Chwezi Super Admin — out of platform scope for Phase 1).

---

## Decision 3: Cross-Tenant Student History

### Approved Approach

**School-scoped portal with a "My Academic History" tab — student sees all prior schools' records in read-only mode.**

### Portal Layout

The student logs in through their **current school's portal**. Their dashboard has two areas:

- **Current School** — live data: results, fees, attendance, timetable.
- **My Academic History** — read-only cards for every prior school, listed reverse-chronologically.

Each history card shows:
- School name and logo
- Academic years attended
- Available record types: Report Cards | Attendance Summaries | Fee Clearance Status

Fee payment amounts from old schools are **not shown** — only a cleared/not-cleared status. The old school's debt relationship does not follow the student.

### Architecture

Cross-tenant history reads use an explicit `withStudentSelfScope($studentUid)` Service method — separate from the standard Repository, which enforces single-tenant isolation. This method:

1. Queries `school_enrollments` by `student_uid` (global table, no `tenant_id` filter).
2. For each prior `tenant_id`, fetches only the data types the student is permitted to view (report cards released by that school, attendance summaries, fee clearance status).
3. Writes an audit log entry for every cross-tenant history read: `{action: STUDENT_SELF_HISTORY_READ, student_uid, viewer_user_id, source_tenant_id, target_tenant_id, data_types_accessed, timestamp}`.

**What the student cannot do from the history tab:**
- Amend any record at the old school.
- Download records that the old school has not released (e.g. if report cards were never published at the old school, they remain inaccessible).
- See other students' records (scope is locked to their own `student_uid`).

**Suspended/archived tenants:** If the old school's tenant is suspended or archived, the student's history records remain accessible to the student. Student data survivability is not tied to the school's subscription status.

---

## Decision 4: Inter-School Record Request System

### Approved Approach

**3-party consent workflow: requesting school → student/parent consent (per item) → source school approval → time-limited access.**

This approach is recommended for strongest PDPO 2019 compliance and aligns with the student-owns-their-records philosophy of the platform.

### Shareable Items (Platform-Defined Canonical List)

Schools may only request items from this list. New items require a platform-level change.

| Code | Item | Student Consent Required? | Notes |
|---|---|---|---|
| `academic_results` | Full academic results by year/term | Yes | All subjects, grades, aggregates |
| `report_cards` | Official report card PDFs | Yes | Only released cards |
| `attendance_summary` | Termly attendance summary | Yes | Present/Absent/Late counts |
| `disciplinary_record` | Disciplinary incidents and resolutions | Yes — **explicit separate checkbox** | Requires extra consent step |
| `fee_clearance` | Confirmation all fees cleared on departure | Yes | Boolean only — no amounts |
| `transfer_letter` | Official transfer letter | Yes | If one was issued |
| `health_summary` | Medical summary | Yes — **Phase 7 only** | Requires additional health data consent |

### Workflow

```
Step 1 — School B raises request
  • Finds student via NIN/LIN lookup
  • Selects items from canonical list
  • Sets reason (e.g. "Enrollment verification")
  • Sets requested access window: 7, 14, or 30 days
  • Submits
  • Status: awaiting_student_consent

Step 2 — Student/Parent notified (SMS + portal)
  Message: "[School B] has requested your records from [School A].
  They are asking for: Academic Results, Report Cards, Disciplinary Record.
  You may approve or decline each item individually."
  • Student/parent approves or declines each item
  • Disciplinary Record has a separate explicit checkbox with plain-language warning:
    "This includes records of behavioural incidents at [School A].
    Are you sure you want to share this?"
  • If no response within 7 days: request expires automatically
    (no silent approval — inaction = denial)
  • Status: awaiting_source_school_review

Step 3 — School A reviews
  • Sees: "[School B] requested records for [Student].
    Student approved: Academic Results, Report Cards.
    Student declined: Disciplinary Record."
  • School A can approve only what the student approved
    (cannot override a student decline)
  • School A may further restrict what they release
    (e.g. approve Academic Results, decline Report Cards)
  • School A sets access window (up to requested duration, or shorter)
  • Status: approved | partially_approved | denied

Step 4 — School B accesses records
  • Approved items in a time-limited read-only view
  • Countdown shows remaining days
  • School B can download PDFs within window
  • After expiry: portal access removed
    (downloaded PDFs are School B's responsibility)

Step 5 — Audit trail
  • Every step immutably logged: request, consent decisions,
    approval decisions, each access event, each download, expiry
  • Visible to: student (full history), School A, School B, Super Admin
```

### PDPO 2019 Alignment Notes

- Each school is a separate Data Controller under PDPO 2019. Sharing personal data between two Data Controllers requires a lawful basis.
- Student/parent consent (Step 2) provides the lawful basis for the transfer.
- The consent is granular (per item), specific (named schools, named purpose), and time-limited (access window).
- The student's right to decline any item is absolute.
- The audit trail satisfies the accountability obligation under PDPO 2019 Section 26.
- The 7-day expiry of unanswered requests prevents indefinite pending consent requests accumulating.

---

## Decision 5: In-Platform School Application

### Approved Approach

**Lightweight expression-of-interest system scoped to Academia Pro platform schools only.**

The application feature is a platform network-effect feature — not a general-purpose school search engine. Only schools on the Academia Pro platform appear in the directory.

### Application Flow

```
Student/Parent (portal)
  ↓
Browse school directory
  Filter by: district, school type (primary/secondary/both),
             curriculum (thematic/O-Level/A-Level),
             boarding/day
  ↓
Click "Apply to this school"
  Form pre-filled from global identity:
    • Student name, DOB, gender (read-only)
    • Requested class and academic year
    • Optional: attach supporting records
      (triggers mini-record-request workflow — student selects
       which items from their history to share with the application)
    • Optional: personal statement (max 500 words)
  ↓
Application submitted
  Status: Under Review
  ↓
School B (admin portal) — Admissions Queue
  Head Teacher sees new application
  Actions: Accept | Request Interview | Decline
  ↓
Student/Parent notified of decision (SMS + portal)
  ↓
If Accepted:
  School uses normal NIN/LIN enrolment (FR-SIS-002) to formally enrol
  Application record is closed and linked to the enrolment
```

### Scoping Rules

- A student may have a maximum of **5 pending applications** at any one time (prevents spam applications).
- A school may close applications for a specific academic year or class (e.g. "P7 2026 — Full").
- Application records are retained for 2 years after creation, then purged.
- The application itself does not share any records — it only shares what the student explicitly attaches. The formal record-sharing (Decision 4) is separate and triggered only if the school requests it after receiving the application.

---

## New FR Groups Required in SRS

This design requires the following new functional requirement groups to be added to `02-requirements-engineering/01-srs/04-functional-requirements.md`:

| Group | Description | Estimated FR Count |
|---|---|---|
| `FR-PROM` | Year-Start Promotion Wizard | 7 |
| `FR-DEPART` | Unified Departure Model | 4 |
| `FR-HIST` | Cross-Tenant Student History | 3 |
| `FR-SHARE` | Inter-School Record Request | 8 |
| `FR-APPLY` | In-Platform School Application | 5 |
| **Total new FRs** | | **~27** |

---

## New Business Rules Required

The following business rule sections must be added to `_context/business_rules.md`:

- `BR-PROM-001` through `BR-PROM-010` — Promotion and departure rules
- `BR-HIST-001` through `BR-HIST-003` — Cross-tenant student history rules
- `BR-SHARE-001` through `BR-SHARE-007` — Inter-school record sharing rules
- `BR-APPLY-001` through `BR-APPLY-004` — In-platform application rules

---

## Gap Analysis Updates

| Gap | Status After This Design |
|---|---|
| HIGH-004: Academic Year Lifecycle | ✅ Resolved — promotion model, year-end locking, repeat student handling all defined |

---

## Open Items (External Actions Required)

| Item | Owner | Urgency |
|---|---|---|
| Legal review of 3-party consent model against PDPO 2019 | Peter + legal counsel | Before FR-SHARE implementation |
| Decision: maximum application window (7 days for student consent — appropriate?) | Peter | Before FR-SHARE spec |
| Platform school directory — opt-in or opt-out for listing? | Peter | Before FR-APPLY spec |
| UNEB expelled student re-examination policy — does expulsion affect UNEB candidacy? | Peter + UNEB | Before FR-DEPART finalised |

---

## Implementation Phases

These features span multiple build phases:

| Feature | Recommended Phase |
|---|---|
| FR-PROM — Year-Start Promotion Wizard | Phase 1 (core academic year workflow) |
| FR-DEPART — Unified Departure Model | Phase 1 (replaces simple graduate status) |
| FR-HIST — Cross-Tenant Student History (web portal) | Phase 5 (Student + Parent portals complete) |
| FR-SHARE — Inter-School Record Request | Phase 5 (requires both school and student portals) |
| FR-APPLY — In-Platform School Application | Phase 5 (requires student/parent portal) |

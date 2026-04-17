---
title: "Role-Based Access Control Matrix — Academia Pro"
version: "1.0"
date: "2026-03-28"
author: "Chwezi Core Systems"
status: "Draft — Awaiting Phase 1 Sign-off"
---

# Role-Based Access Control Matrix — Academia Pro

This document defines the complete Role-Based Access Control (RBAC) model for Academia Pro. It specifies, for every role, exactly which actions are permitted on every module. A developer must be able to implement the `roles`, `permissions`, and `role_permissions` seed records from this file without requiring additional clarification. All rules in Section 6 override individual cell entries in the permission tables. This matrix covers Phase 1 standard modules and Phase 2+ optional modules; Phase 2+ cells are marked accordingly.

The RBAC model is enforced at three layers: the Laravel middleware (gate checks on every API route), the Repository layer (`tenant_id` scoping on every query — see BR-MT-001), and the frontend (route guards hide menu items the authenticated user cannot access). The matrix is the authoritative source for all three layers.

---

# 1. Role Definitions

The table below maps each role slug to its display name, operational scope, and privilege tier. Privilege tier runs from 1 (lowest) to 5 (highest).

| Role Slug | Display Name | Scope | Privilege Tier |
|---|---|---|---|
| `super_admin` | Platform Administrator | Platform-wide (cross-tenant, read-only support mode) | 5 |
| `owner` | School Owner / Director | School-wide (all modules, all data within tenant) | 4 |
| `head_teacher` | Head Teacher | School-wide academic operations; restricted financial view | 3 |
| `teacher` | Class Teacher | Own assigned classes only | 2 |
| `bursar` | Bursar / Accounts Officer | All fee and financial operations within tenant | 3 |
| `receptionist` | Receptionist | Front office module; basic student directory | 1 |
| `librarian` | Librarian | Library module; basic student directory (name, class, photo) | 1 |
| `transport_manager` | Transport Manager | Transport module; boarder/day student list view | 1 |
| `hostel_warden` | Hostel Warden | Hostel module; boarder student profile view | 1 |
| `nurse` | School Nurse | Health module only (Phase 7) | 1 |
| `parent` | Parent / Guardian | Own child's records only (read-only) | 1 |
| `student` | Student | Own records only (read-only) | 1 |

---

# 2. Permission Notation Legend

| Symbol | Meaning |
|---|---|
| `C` | Create — submit a new record |
| `R` | Read / View — view an existing record |
| `U` | Update / Edit — modify an existing record |
| `D` | Delete / Archive — remove or soft-delete a record |
| `A` | Approve — authorise a pending action (e.g., approve a refund, finalise report cards) |
| `X` | Export — download or generate a file export (PDF, CSV, Excel) |
| `CRUD` | Full create, read, update, delete |
| `CRUDAX` | Full access including approve and export |
| `-` | No access |
| `†` | Scope restriction applies — see the footnote below the table for that module |

Compound examples: `CRU` = create + read + update (no delete); `RX` = read and export only; `CRUAX` = all except delete.

---

# 3. Permission Tables by Module

Each module heading is followed by an action-row table. Column headers are role slugs abbreviated for readability. The abbreviation key is:

| Column Header | Role Slug |
|---|---|
| SA | `super_admin` |
| OW | `owner` |
| HT | `head_teacher` |
| TC | `teacher` |
| BU | `bursar` |
| RC | `receptionist` |
| LB | `librarian` |
| TM | `transport_manager` |
| HW | `hostel_warden` |
| NU | `nurse` |
| PA | `parent` |
| ST | `student` |

---

## 3.1 User and RBAC Management

Covers: user accounts (staff and portal users), role assignments, role creation, and permission auditing.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| View user list | R | CRUD | R | - | - | - | - | - | - | - | - | - |
| Create user account | CRUD | CRUD | - | - | - | - | - | - | - | - | - | - |
| Edit user account | CRUD | CRUD | - | - | - | - | - | - | - | - | - | - |
| Deactivate / delete user | CRUD | CRUD | - | - | - | - | - | - | - | - | - | - |
| Assign role to user | R | CRUD | - | - | - | - | - | - | - | - | - | - |
| View role definitions | R | R | R | - | - | - | - | - | - | - | - | - |
| Create / edit custom role | CRUD | - | - | - | - | - | - | - | - | - | - | - |
| View permission audit log | R | R | - | - | - | - | - | - | - | - | - | - |
| Reset user password | CRUD | CRUD | - | - | - | - | - | - | - | - | - | - |
| Impersonate user (support) | R† | - | - | - | - | - | - | - | - | - | - | - |

*† SA impersonation is read-only support mode only. Every impersonation event is logged (BR-MT-003).*

*BR-RBAC-002 applies: no user may assign a role with a privilege tier higher than their own.*

---

## 3.2 Student Information System (SIS)

Covers: student admission, profile management, enrollment records, transfers, and the global student identity lookup.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Admit new student | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| View student full profile | R | R | R | R† | R | R‡ | R‡ | R‡ | R‡ | R§ | R¶ | R¶ |
| Edit student profile | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| View enrollment history | R | R | R | - | R | - | - | - | - | - | R¶ | R¶ |
| Record student transfer (out) | R | CRUD | CRU | - | - | - | - | - | - | - | - | - |
| Record student transfer (in) | R | CRUD | CRU | - | - | - | - | - | - | - | - | - |
| Delete / archive student record | R | D | - | - | - | - | - | - | - | - | - | - |
| Global identity NIN/LIN lookup | R | R | R | - | - | - | - | - | - | - | - | - |
| Export student data (PDPO request) | R | RX | RX | - | - | - | - | - | - | - | - | - |
| Export student list (CSV) | R | RX | RX | - | - | - | - | - | - | - | - | - |

*† TC: own assigned class students only.*
*‡ RC, LB, TM, HW: view is limited to name, class, photo, and student number. No academic, fee, or health data.*
*§ NU: view limited to name, class, photo, emergency contacts, and linked health record only.*
*¶ PA and ST: own child / own record only.*

---

## 3.3 Academics Setup

Covers: academic year and term configuration, class creation, subject setup, timetable management, and curriculum level assignment.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Configure academic year / terms | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Create / edit classes | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Assign teacher to class | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Create / edit subjects | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Assign subject to class | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Build / view timetable | R | CRUD | CRUD | R† | - | - | - | - | - | - | R | R |
| Set curriculum level per class | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| View class list | R | R | R | R† | R | - | - | - | - | - | R | R |

*† TC: own assigned classes only.*

---

## 3.4 Fees and Payments

Covers: fee structure definition, payment recording, receipt management, refunds, ledger reconciliation, and fee reminder configuration.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / edit fee structure | R | CRUD | - | - | CRU | - | - | - | - | - | - | - |
| View fee structures | R | R | R | - | R | - | - | - | - | - | - | - |
| Record manual payment (cash) | R | CRUD | - | - | CRUD | - | - | - | - | - | - | - |
| View payment history | R | R | R | - | R | - | - | - | - | - | R¶ | R¶ |
| Generate / view receipt | R | RX | RX | - | RX | - | - | - | - | - | RX¶ | RX¶ |
| Initiate refund request | R | CRUD | - | - | CRU | - | - | - | - | - | - | - |
| Approve refund | R | A | - | - | - | - | - | - | - | - | - | - |
| View outstanding balances | R | R | R | - | R | - | - | - | - | - | R¶ | R¶ |
| Reconcile SchoolPay payments | R | RX | - | - | CRUX | - | - | - | - | - | - | - |
| Export financial report | R | RX | - | - | RX | - | - | - | - | - | - | - |
| Configure fee reminders | R | CRUD | - | - | CRU | - | - | - | - | - | - | - |
| View fee reminder log | R | R | - | - | R | - | - | - | - | - | - | - |
| Hostel billing (Phase 2) | R | CRUD | - | - | CRUD | - | - | - | HW† | - | R¶ | - |

*¶ PA and ST: own child / own record only.*
*† HW: hostel warden may view hostel billing totals per boarder but may not create or edit fee structures.*

*BR-FEE-007 applies: only `owner` may approve refunds. The `bursar` role may initiate but never approve their own refund request.*

---

## 3.5 Attendance

Covers: daily attendance marking, late-entry corrections, automated alert configuration, and attendance reporting.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mark daily attendance | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Correct attendance (≤ 48 h) | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Amend attendance (> 48 h) | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| View attendance register | R | R | R | R† | - | - | - | - | - | - | R¶ | R¶ |
| View attendance summary report | R | RX | RX | RX† | - | - | - | - | - | - | RX¶ | RX¶ |
| Export attendance data | R | RX | RX | - | - | - | - | - | - | - | - | - |
| Configure attendance alert rules | R | CRUD | CRU | - | - | - | - | - | - | - | - | - |

*† TC: own assigned class only.*
*¶ PA and ST: own child / own record only.*

*BR-ATT-003 applies: corrections within 48 hours are allowed by the class teacher. Amendments beyond 48 hours require `head_teacher` or `owner` role and are audit-logged.*

---

## 3.6 Examinations and Grading

Covers: exam creation, mark entry, grade computation (including UNEB formulas), mark locking/unlocking, and results publication.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create exam / assessment | R | CRUD | CRUD | CRU† | - | - | - | - | - | - | - | - |
| Enter marks | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Edit marks (before lock) | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Lock / unlock mark entry | R | A | A | - | - | - | - | - | - | - | - | - |
| Compute grades (UNEB formulas) | R | A | A | - | - | - | - | - | - | - | - | - |
| Approve final results | R | A | A | - | - | - | - | - | - | - | - | - |
| View marks and grades | R | R | R | R† | - | - | - | - | - | - | R¶ | R¶ |
| Export mark sheet | R | RX | RX | RX† | - | - | - | - | - | - | - | - |
| Export results analysis | R | RX | RX | RX | - | - | - | - | - | - | - | - |

*† TC: own assigned class and subjects only.*
*¶ PA and ST: own child / own record only.*

*BR-UNEB-005 applies: the API layer rejects out-of-range mark submissions regardless of role.*
*BR-CAL-003 applies: mark entry for examination classes locks after the school's configured exam submission deadline.*

---

## 3.7 Report Cards

Covers: report card generation, bulk printing, distribution to parents, and result publication configuration.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Generate individual report card | R | CRUDX | CRUDX | - | - | - | - | - | - | - | - | - |
| Bulk generate report cards | R | CRUDX | CRUDX | - | - | - | - | - | - | - | - | - |
| Approve / finalise report cards | R | A | A | - | - | - | - | - | - | - | - | - |
| Publish results to parent portal | R | A | A | - | - | - | - | - | - | - | - | - |
| View / download report card | R | RX | RX | R† | - | - | - | - | - | - | RX¶ | RX¶ |
| Add head teacher comment | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Add class teacher comment | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Export bulk report card PDF | R | RX | RX | - | - | - | - | - | - | - | - | - |

*† TC: own assigned class only.*
*¶ PA and ST: own child / own record only. Report cards are visible only after `owner` or `head_teacher` publishes results.*

---

## 3.8 Reports and Analytics

Covers: system-wide reporting dashboards, financial summaries, enrollment statistics, attendance and examination trend reports.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform analytics dashboard | R | - | - | - | - | - | - | - | - | - | - | - |
| School summary dashboard | R | R | R | - | - | - | - | - | - | - | - | - |
| Financial reports | R | RX | - | - | RX | - | - | - | - | - | - | - |
| Enrollment reports | R | RX | RX | - | - | - | - | - | - | - | - | - |
| Attendance summary reports | R | RX | RX | RX† | - | - | - | - | - | - | - | - |
| Examination results analysis | R | RX | RX | RX† | - | - | - | - | - | - | - | - |
| Fee collection summary | R | RX | - | - | RX | - | - | - | - | - | - | - |
| AI-generated commentary reports | R | RX | RX | - | - | - | - | - | - | - | - | - |
| Export any report to CSV / PDF | R | RX | RX | - | RX | - | - | - | - | - | - | - |
| EMIS / MoES export | R | RX | RX | - | - | - | - | - | - | - | - | - |

*† TC: own assigned class only.*

---

## 3.9 Front Office

Covers: visitor book, enquiries log, phone call log, appointment scheduling, and walk-in student/parent directory lookups.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Log visitor entry / exit | R | CRUD | CRUD | - | - | CRUD | - | - | - | - | - | - |
| View visitor book | R | R | R | - | - | R | - | - | - | - | - | - |
| Log enquiry | R | CRUD | CRUD | - | - | CRUD | - | - | - | - | - | - |
| View enquiry log | R | R | R | - | - | R | - | - | - | - | - | - |
| Log phone call | R | CRUD | CRUD | - | - | CRUD | - | - | - | - | - | - |
| View phone log | R | R | R | - | - | R | - | - | - | - | - | - |
| Student directory lookup (basic) | R | R | R | R | - | R | - | - | - | - | - | - |
| Export front office report | R | RX | RX | - | - | RX | - | - | - | - | - | - |

---

## 3.10 Notice Board and Communication

Covers: notice creation, bulk SMS/email dispatch, audience targeting, and communication delivery logs.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / publish notice | R | CRUD | CRUD | CRU† | - | - | - | - | - | - | - | - |
| Send bulk SMS | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Send bulk email | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Send targeted SMS (class-level) | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| View communication logs | R | R | R | R† | - | - | - | - | - | - | - | - |
| View / receive notices | R | R | R | R | - | R | R | R | R | R | R | R |
| Export communication log | R | RX | RX | - | - | - | - | - | - | - | - | - |

*† TC: own assigned class only.*

---

## 3.11 Homework and Assignments (Phase 2)

Covers: assignment posting, submission tracking, evaluation/grading, and return to students.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Post assignment | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| View assignments | R | R | R | R† | - | - | - | - | - | - | R¶ | R¶ |
| Submit assignment (student) | - | - | - | - | - | - | - | - | - | - | - | CRU¶ |
| Evaluate / grade submission | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Return graded assignment | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| View assignment analytics | R | R | R | R† | - | - | - | - | - | - | - | - |

*† TC: own assigned class only.*
*¶ ST: own assignments only. PA: can view child's assignments only.*

---

## 3.12 Download Centre (Phase 2)

Covers: file upload management, access-level configuration per file, and student/parent downloads.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Upload file | R | CRUD | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| Set file access level | R | CRUD | CRUD | CRU† | - | - | - | - | - | - | - | - |
| Delete file | R | D | D | D† | - | - | - | - | - | - | - | - |
| Download file | R | R | R | R | R | R | R | R | R | R | R† | R† |
| View download log | R | R | R | - | - | - | - | - | - | - | - | - |

*† TC: own files only; PA and ST: files published to their role tier only.*

---

## 3.13 Calendar and Events (Phase 2)

Covers: school calendar management, event creation, and term schedule publication.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / edit event | R | CRUD | CRUD | CRU | - | - | - | - | - | - | - | - |
| Delete event | R | D | D | - | - | - | - | - | - | - | - | - |
| View calendar | R | R | R | R | R | R | R | R | R | R | R | R |
| Export calendar | R | RX | RX | - | - | - | - | - | - | - | - | - |

---

## 3.14 Certificates and ID Cards (Phase 2)

Covers: certificate template design, individual and bulk generation, and ID card print export.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / edit certificate template | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Generate individual certificate | R | CRUDX | CRUDX | - | - | - | - | - | - | - | - | - |
| Bulk generate certificates | R | CRUDX | CRUDX | - | - | - | - | - | - | - | - | - |
| Generate / print ID card | R | CRUDX | CRUDX | - | - | - | - | - | - | - | - | - |
| Download own ID card / certificate | - | - | - | - | - | - | - | - | - | - | RX | RX |

---

## 3.15 Library (Phase 2)

Covers: library catalogue management, book borrowing and return workflows, fine calculation, and basic student lookup.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manage catalogue (add/edit/remove) | R | CRUD | - | - | - | - | CRUD | - | - | - | - | - |
| Issue book to borrower | R | CRUD | - | - | - | - | CRUD | - | - | - | - | - |
| Record book return | R | CRUD | - | - | - | - | CRUD | - | - | - | - | - |
| Calculate and record fine | R | CRUD | - | - | CRUD | - | CRU | - | - | - | - | - |
| View borrowing history | R | R | R | - | R | - | R | - | - | - | R¶ | R¶ |
| View student directory (basic) | R | R | R | R | - | - | R | - | - | - | - | - |
| Export library report | R | RX | - | - | RX | - | RX | - | - | - | - | - |

*¶ PA and ST: own child / own borrow history only.*

---

## 3.16 Transport (Phase 2)

Covers: route management, vehicle records, student bus assignments, and boarder/day student list access.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / edit route | R | CRUD | - | - | - | - | - | CRUD | - | - | - | - |
| Assign vehicle to route | R | CRUD | - | - | - | - | - | CRUD | - | - | - | - |
| Assign student to route | R | CRUD | CRU | - | - | - | - | CRUD | - | - | - | - |
| View boarder / day student list | R | R | R | - | - | - | - | R | - | - | - | - |
| Record daily bus attendance | R | CRUD | - | - | - | - | - | CRUD | - | - | - | - |
| View transport report | R | RX | - | - | RX | - | - | RX | - | - | R¶ | - |
| Export transport data | R | RX | - | - | - | - | - | RX | - | - | - | - |

*¶ PA: view own child's route assignment only.*

---

## 3.17 Hostel (Phase 2)

Covers: room allocation, boarder profiles, hostel billing, and warden log.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manage hostel / room setup | R | CRUD | - | - | - | - | - | - | CRUD | - | - | - |
| Assign student to room | R | CRUD | CRU | - | - | - | - | - | CRUD | - | - | - |
| View boarder student profile | R | R | R | - | R | - | - | - | R | - | R¶ | R¶ |
| Record hostel incident | R | CRUD | CRUD | - | - | - | - | - | CRUD | - | - | - |
| View warden log | R | R | R | - | - | - | - | - | R | - | - | - |
| Generate hostel billing | R | CRUD | - | - | CRUD | - | - | - | CRU | - | - | - |
| Export hostel report | R | RX | - | - | RX | - | - | - | RX | - | - | - |

*¶ PA and ST: own child / own profile only.*

---

## 3.18 HR and Payroll (Phase 2)

Covers: staff records, leave management, payroll computation, and NSSF/PAYE statutory deductions.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / edit staff record | R | CRUD | CRU | - | - | - | - | - | - | - | - | - |
| View staff list | R | R | R | - | - | - | - | - | - | - | - | - |
| Manage leave requests | R | CRUDAX | CRUDAX | CRU† | - | - | - | - | - | - | - | - |
| Process payroll | R | CRUD | - | - | CRUD | - | - | - | - | - | - | - |
| Approve payroll | R | A | - | - | - | - | - | - | - | - | - | - |
| View own payslip | - | R | R | R | R | R | R | R | R | R | - | - |
| Export payroll report | R | RX | - | - | RX | - | - | - | - | - | - | - |
| Manage NSSF / PAYE deductions | R | CRUD | - | - | CRUD | - | - | - | - | - | - | - |

*† HT: approve / reject leave requests for staff below head teacher tier only.*

---

## 3.19 Health Records (Phase 7)

Covers: student health profiles, clinic visit logs, medication records, and emergency contacts. Governed by BR-DP-003 (special category data).

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Create / edit health record | - | - | - | - | - | - | - | - | - | CRUD | - | - |
| View health record | R† | - | - | - | - | - | - | - | - | R | R¶ | R¶ |
| Record clinic visit | - | - | - | - | - | - | - | - | - | CRUD | - | - |
| Record medication | - | - | - | - | - | - | - | - | - | CRUD | - | - |
| Emergency override (view) | R‡ | ‡ | ‡ | - | - | - | - | - | - | CRUD | - | - |
| Export health report | - | - | - | - | - | - | - | - | - | RX | - | - |

*† SA: read-only support access; all reads logged per BR-MT-003.*
*‡ Emergency override for `owner` and `head_teacher` requires a documented reason, is logged immediately, and triggers an alert to the nurse role. No SA impersonation is used.*
*¶ PA: own child only. ST: own record only.*

*BR-DP-003 applies: health records are special category data. No role — including `owner` — may access individual health records outside the emergency override pathway.*

---

## 3.20 Super Admin Portal

Covers: Chwezi Core Systems platform operations — tenant management, subscription billing, platform-level analytics, and system announcements.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| View tenant list | R | - | - | - | - | - | - | - | - | - | - | - |
| Create / suspend / terminate tenant | CRUD | - | - | - | - | - | - | - | - | - | - | - |
| View platform analytics dashboard | R | - | - | - | - | - | - | - | - | - | - | - |
| Manage subscription billing | CRUD | - | - | - | - | - | - | - | - | - | - | - |
| Cross-tenant read (support mode) | R† | - | - | - | - | - | - | - | - | - | - | - |
| Send platform-wide announcement | CRUD | - | - | - | - | - | - | - | - | - | - | - |
| View platform audit log | R | - | - | - | - | - | - | - | - | - | - | - |
| Manage feature flags per tenant | CRUD | - | - | - | - | - | - | - | - | - | - | - |

*† Every cross-tenant read is logged with `super_admin` user ID, target `tenant_id`, timestamp, and stated access reason. Read-only; no writes permitted in support mode (BR-MT-003).*

---

## 3.21 Owner Portal

Covers: the school owner/director's dashboard, multi-school group overview (Phase 3+), and school KPI monitoring.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| View school dashboard | R | R | - | - | - | - | - | - | - | - | - | - |
| View multi-school group overview | R | R† | - | - | - | - | - | - | - | - | - | - |
| View KPI tiles (fees, attendance, enrolment) | R | R | R | - | R | - | - | - | - | - | - | - |
| Configure owner notification preferences | R | CRUD | - | - | - | - | - | - | - | - | - | - |

*† Multi-school group view (Phase 3+): owner sees only schools within their registered group.*

---

## 3.22 System Settings

Covers: school branding, academic configuration defaults, integration credentials, and data retention policies.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edit school profile / branding | R | CRUD | CRU | - | - | - | - | - | - | - | - | - |
| Configure integrations (SchoolPay, SMS) | CRUD | CRUD | - | - | - | - | - | - | - | - | - | - |
| Manage data retention / backup policy | CRUD | R | - | - | - | - | - | - | - | - | - | - |
| View system settings | R | R | R | - | - | - | - | - | - | - | - | - |
| Configure EMIS export settings | R | CRUD | CRU | - | - | - | - | - | - | - | - | - |
| View integration logs | R | R | - | - | - | - | - | - | - | - | - | - |
| Manage school year / term dates | R | CRUD | CRUD | - | - | - | - | - | - | - | - | - |
| Toggle module visibility per role | CRUD | CRUD | - | - | - | - | - | - | - | - | - | - |

---

# 4. Cross-Cutting Rules

The rules in this section are invariant. They override any permission cell in Section 3. No role, workflow, or edge case may violate these rules.

## 4.1 Tenant Isolation (BR-MT-001 and BR-MT-002)

Every API route that accesses tenant-scoped data appends `WHERE tenant_id = ?` using the `tenant_id` claim embedded in the authenticated JWT. No query reaches the database without this constraint. The Repository base class enforces this before execution — it is not optional and cannot be bypassed by any application-layer code. A `super_admin` user accessing a tenant in support mode is given a scoped read-only token for that tenant; their own tenant claim does not grant write access.

## 4.2 Super Admin Audit Logging (BR-MT-003)

Every action taken by a `super_admin` user — including all cross-tenant reads performed in support mode — is written to the `super_admin_audit_log` table with the following fields: `super_admin_user_id`, `target_tenant_id`, `action`, `resource_type`, `resource_id`, `access_reason`, `ip_address`, `timestamp`. Logs are immutable. Deletion of audit log entries is not permitted by any role including `super_admin`.

## 4.3 Parent and Student Scoping

A `parent` user may only read records belonging to their registered child. The system enforces this via a `guardian_links` table mapping `user_id` (parent portal account) to one or more `student_uid` values. Every API route accessible to the `parent` role validates that the requested `student_uid` is in the authenticated parent's `guardian_links` set. A `student` user may only access records where `student_uid` matches their own profile. Neither `parent` nor `student` may access aggregate reports, class lists, or other students' data.

## 4.4 48-Hour Attendance Amendment Window (BR-ATT-003)

The `teacher` role may correct an attendance record within 48 hours of the record date. The API enforces this time boundary. After 48 hours, the attendance record is read-only for the `teacher` role. The `head_teacher` and `owner` roles may amend any attendance record at any time. All amendments after the original submission timestamp are written to the `attendance_amendments` audit table with `amended_by`, `amended_at`, `original_status`, `new_status`, and `reason`.

## 4.5 Refund Approval Chain (BR-FEE-007)

Fee refund requests follow a two-step workflow. The `bursar` may create a refund request (status: `PENDING_APPROVAL`). Only the `owner` role may approve or reject a refund request (status: `APPROVED` or `REJECTED`). The `bursar` may not approve their own refund request. No refund payment is processed until the owning record's status is `APPROVED`. This chain is enforced at the service layer, not just the UI.

## 4.6 Role Privilege Ceiling (BR-RBAC-002)

No user may assign a role whose privilege tier (see Section 1) is equal to or higher than their own tier, except `super_admin` who may assign any role. Specifically: `owner` (tier 4) may assign tiers 1–3 only; `head_teacher` (tier 3) may assign tiers 1–2 only. Attempts to assign an out-of-ceiling role return HTTP 403 at the API layer.

## 4.7 Health Record Special Category Protection (BR-DP-003)

Health records are classified as special category data under the Uganda PDPO 2019. Access is restricted to the `nurse` role and the linked parent (`parent` role, own child only) and student (`student` role, own record only). The `owner` and `head_teacher` roles may access individual health records only through the emergency override pathway, which requires a typed justification, logs the access immediately, and notifies the `nurse` role in real time. No other role — including `super_admin` in support mode — may read individual health records.

## 4.8 Mark Entry Lock (BR-UNEB-005 and BR-CAL-003)

Once mark entry is locked — either manually by `owner` or `head_teacher`, or automatically at the school's configured exam submission deadline — the `teacher` role receives HTTP 423 (Locked) on all mark write operations. The `owner` and `head_teacher` roles may unlock mark entry. Every lock and unlock event is logged to `exam_lock_audit` with `actioned_by`, `actioned_at`, and `reason`.

## 4.9 Immutable Receipts (BR-FEE-004)

Fee payment receipts cannot be deleted by any role. The `bursar` and `owner` may void a receipt (status: `VOIDED`) with a mandatory reason, but the original receipt record and all its fields remain in the database. The `D` (Delete) action is absent from the receipt row throughout Section 3.4 by design.

## 4.10 Role Assignment Per School (BR-RBAC-001)

Roles are assigned per school per user. A single registered user account may hold different roles at different schools. For example, a user who teaches at School A (`teacher` role on `tenant_id = 1`) may be a `parent` at School B (`tenant_id = 2`). The JWT encodes a single active `tenant_id` and `role` claim per session. Switching school context requires re-authentication or a school-switch token exchange endpoint.

---

# 5. Phase 1 Implementation Checklist

This section enumerates the logical seed records required to initialise the permissions system. These are expressed as role → module → action triples. The implementing developer translates these triples into the actual `INSERT` statements for the `roles`, `modules`, `permissions`, and `role_permissions` tables.

## 5.1 Roles Seed

The following role slugs must exist in the `roles` table at application boot.

- `super_admin` — Platform Administrator — tier 5
- `owner` — School Owner / Director — tier 4
- `head_teacher` — Head Teacher — tier 3
- `bursar` — Bursar / Accounts Officer — tier 3
- `teacher` — Class Teacher — tier 2
- `receptionist` — Receptionist — tier 1
- `librarian` — Librarian — tier 1
- `transport_manager` — Transport Manager — tier 1
- `hostel_warden` — Hostel Warden — tier 1
- `nurse` — School Nurse — tier 1
- `parent` — Parent / Guardian — tier 1
- `student` — Student — tier 1

## 5.2 Modules Seed

The following module slugs must exist in the `modules` table. Phase column indicates earliest phase when the module is active.

| Module Slug | Display Name | Phase |
|---|---|---|
| `rbac` | User and RBAC Management | 1 |
| `sis` | Student Information System | 1 |
| `academics` | Academics Setup | 1 |
| `fees` | Fees and Payments | 1 |
| `attendance` | Attendance | 1 |
| `exams` | Examinations and Grading | 1 |
| `report_cards` | Report Cards | 1 |
| `reports` | Reports and Analytics | 1 |
| `front_office` | Front Office | 1 |
| `communication` | Notice Board and Communication | 1 |
| `homework` | Homework and Assignments | 2 |
| `download_centre` | Download Centre | 2 |
| `calendar` | Calendar and Events | 2 |
| `certificates` | Certificates and ID Cards | 2 |
| `library` | Library | 2 |
| `transport` | Transport | 2 |
| `hostel` | Hostel | 2 |
| `hr_payroll` | HR and Payroll | 2 |
| `health` | Health Records | 7 |
| `super_admin_portal` | Super Admin Portal | 1 |
| `owner_portal` | Owner Portal | 1 |
| `system_settings` | System Settings | 1 |

## 5.3 Actions Seed

The following action slugs must exist in the `actions` table.

- `create`
- `read`
- `update`
- `delete`
- `approve`
- `export`

## 5.4 Phase 1 Role-Module-Action Triples

The following triples define every `role_permissions` row required for Phase 1 modules (`rbac`, `sis`, `academics`, `fees`, `attendance`, `exams`, `report_cards`, `reports`, `front_office`, `communication`, `super_admin_portal`, `owner_portal`, `system_settings`). Scoping constraints (own class, own child, etc.) are enforced in application code — the permission record grants the action; the service layer applies the scope filter.

### super_admin

- `super_admin` → all Phase 1 modules → `read`
- `super_admin` → `rbac` → `create`, `update`, `delete`
- `super_admin` → `super_admin_portal` → `create`, `read`, `update`, `delete`, `approve`, `export`
- `super_admin` → `system_settings` → `create`, `update`

### owner

- `owner` → `rbac` → `create`, `read`, `update`, `delete`
- `owner` → `sis` → `create`, `read`, `update`, `delete`, `export`
- `owner` → `academics` → `create`, `read`, `update`, `delete`
- `owner` → `fees` → `create`, `read`, `update`, `delete`, `approve`, `export`
- `owner` → `attendance` → `create`, `read`, `update`, `delete`, `export`
- `owner` → `exams` → `create`, `read`, `update`, `delete`, `approve`, `export`
- `owner` → `report_cards` → `create`, `read`, `update`, `delete`, `approve`, `export`
- `owner` → `reports` → `read`, `export`
- `owner` → `front_office` → `create`, `read`, `update`, `delete`, `export`
- `owner` → `communication` → `create`, `read`, `update`, `delete`, `export`
- `owner` → `owner_portal` → `read`
- `owner` → `system_settings` → `create`, `read`, `update`, `delete`

### head_teacher

- `head_teacher` → `rbac` → `read`
- `head_teacher` → `sis` → `create`, `read`, `update`, `export`
- `head_teacher` → `academics` → `create`, `read`, `update`, `delete`
- `head_teacher` → `attendance` → `create`, `read`, `update`, `delete`, `export`
- `head_teacher` → `exams` → `create`, `read`, `update`, `delete`, `approve`, `export`
- `head_teacher` → `report_cards` → `create`, `read`, `update`, `delete`, `approve`, `export`
- `head_teacher` → `reports` → `read`, `export`
- `head_teacher` → `front_office` → `create`, `read`, `update`, `export`
- `head_teacher` → `communication` → `create`, `read`, `update`, `delete`, `export`
- `head_teacher` → `system_settings` → `read`, `update`

### teacher

- `teacher` → `sis` → `read` *(scoped: own class)*
- `teacher` → `academics` → `read` *(scoped: own class)*
- `teacher` → `attendance` → `create`, `read`, `update`, `export` *(scoped: own class)*
- `teacher` → `exams` → `create`, `read`, `update`, `export` *(scoped: own class and subjects)*
- `teacher` → `report_cards` → `read`, `update` *(scoped: own class — comment entry only)*
- `teacher` → `reports` → `read`, `export` *(scoped: own class)*
- `teacher` → `communication` → `create`, `read`, `update` *(scoped: own class)*

### bursar

- `bursar` → `sis` → `read`
- `bursar` → `fees` → `create`, `read`, `update`, `export`
- `bursar` → `reports` → `read`, `export` *(financial reports only)*
- `bursar` → `owner_portal` → `read` *(KPI tiles only)*

### receptionist

- `receptionist` → `sis` → `read` *(basic directory only)*
- `receptionist` → `front_office` → `create`, `read`, `update`, `delete`, `export`
- `receptionist` → `communication` → `read`

### librarian

- `librarian` → `sis` → `read` *(name, class, photo only)*
- `librarian` → `reports` → `read`, `export` *(library reports — Phase 2 module; seed at Phase 2)*

### transport_manager

- `transport_manager` → `sis` → `read` *(boarder/day status and class only)*

### hostel_warden

- `hostel_warden` → `sis` → `read` *(boarder student profile only)*

### nurse

- `nurse` → `sis` → `read` *(name, class, photo, emergency contacts only)*
- `nurse` → `health` → `create`, `read`, `update`, `export` *(Phase 7 — seed at Phase 7)*

### parent

- `parent` → `sis` → `read` *(own child only)*
- `parent` → `fees` → `read`, `export` *(own child only)*
- `parent` → `attendance` → `read`, `export` *(own child only)*
- `parent` → `exams` → `read` *(own child only)*
- `parent` → `report_cards` → `read`, `export` *(own child only — after publication)*
- `parent` → `communication` → `read`

### student

- `student` → `sis` → `read` *(own record only)*
- `student` → `fees` → `read`, `export` *(own record only)*
- `student` → `attendance` → `read`, `export` *(own record only)*
- `student` → `exams` → `read` *(own record only)*
- `student` → `report_cards` → `read`, `export` *(own record only — after publication)*
- `student` → `communication` → `read`
- `student` → `academics` → `read` *(timetable only)*

## 5.5 Developer Implementation Notes

1. The `role_permissions` table must carry a `scope` JSON column (nullable) to store structured scope constraints such as `{"class_id": "own"}` or `{"student_uid": "own"}`. The application service layer reads this column and applies the additional filter before query execution.
2. Phase 2+ module permissions are not seeded at Phase 1 database initialisation. The `modules` table row for each Phase 2+ module exists but its `is_active` flag is set to `0`. Permission rows for these modules are inserted when the phase is activated per tenant.
3. Health module (`health`) permission rows must not be seeded until Phase 7 deployment. Inserting them early creates an exploitable surface before the module is fully secured.
4. The `super_admin` role's permission rows are seeded once at platform initialisation, not per tenant. All other role permission rows are per-tenant seed operations executed at school onboarding.
5. Every `role_permissions` insert must reference a valid `role_id`, `module_id`, and `action_id` — no orphaned foreign keys are permitted. Enforce `ON DELETE RESTRICT` on all three foreign keys.

---

*Document version 1.0 — 2026-03-28. Authored by Chwezi Core Systems. Review and sign-off required before Phase 1 development begins (BR-RBAC-003).*


---

## 3.X AI Module (Add-On)

Covers: AI module activation, feature gate management, AI usage and budget visibility, AI insight consumption, and feedback on AI outputs.

> **Gate rule:** All AI Module permissions are non-functional for tenants without an active `tenant_ai_modules` record. Seeding AI permission rows does not activate any AI feature — the AIGate check is a separate runtime enforcement layer.

| Action | SA | OW | HT | TC | BU | RC | LB | TM | HW | NU | PA | ST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Activate / deactivate AI module for tenant | CRUD | - | - | - | - | - | - | - | - | - | - | - |
| View AI module plan and status | R | R | - | - | - | - | - | - | - | - | - | - |
| Enable / disable individual AI feature | - | CRUD | - | - | - | - | - | - | - | - | - | - |
| Set monthly AI budget | - | CRUD | - | - | - | - | - | - | - | - | - | - |
| View AI usage dashboard (per-user breakdown) | R | R | - | - | - | - | - | - | - | - | - | - |
| View AI usage (own usage only) | - | R | R | R | R | - | - | - | - | - | - | - |
| View at-risk student AI insights | R | R | R | R† | - | - | - | - | - | - | - | - |
| Generate AI report card comments | - | - | - | CRUD† | - | - | - | - | - | - | - | - |
| Accept / edit / reject AI report card comments | - | - | CRUD | CRUD† | - | - | - | - | - | - | - | - |
| View owner weekly briefing (AI narrative) | R | R | R | - | - | - | - | - | - | - | - | - |
| View fee default prediction (AI risk list) | R | R | - | - | R | - | - | - | - | - | - | - |
| Export fee default risk list (CSV) | - | RX | - | - | RX | - | - | - | - | - | - | - |
| View parent sentiment analysis | R | R | R | - | - | - | - | - | - | - | - | - |
| Rate AI output (thumbs up / down) | - | R | R | R | R | - | - | - | - | - | - | - |
| View all-tenant AI usage (Super Admin) | R | - | - | - | - | - | - | - | - | - | - | - |

*† TC: own assigned class students only.*

**AI-specific permission slugs for `permissions` table seeding:**

| Module | Action | Roles |
|---|---|---|
| `ai_module` | `activate` | `super_admin` |
| `ai_module` | `view_plan` | `super_admin`, `owner` |
| `ai_features` | `toggle` | `owner` |
| `ai_budget` | `manage` | `owner` |
| `ai_usage` | `view_all` | `super_admin`, `owner` |
| `ai_usage` | `view_own` | `owner`, `head_teacher`, `teacher`, `bursar` |
| `ai_insights.at_risk` | `view` | `super_admin`, `owner`, `head_teacher`, `teacher` |
| `ai_insights.report_comments` | `generate` | `teacher` |
| `ai_insights.report_comments` | `approve` | `head_teacher`, `teacher` |
| `ai_insights.briefing` | `view` | `super_admin`, `owner`, `head_teacher` |
| `ai_insights.fee_risk` | `view` | `super_admin`, `owner`, `bursar` |
| `ai_insights.fee_risk` | `export` | `owner`, `bursar` |
| `ai_insights.sentiment` | `view` | `super_admin`, `owner`, `head_teacher` |
| `ai_feedback` | `submit` | `owner`, `head_teacher`, `teacher`, `bursar` |

**Note:** AI Module permissions are not seeded at Phase 1 database initialisation. They are inserted when the tenant activates the AI add-on. This prevents any AI surface from being exploitable before the module is commercially active for the tenant.

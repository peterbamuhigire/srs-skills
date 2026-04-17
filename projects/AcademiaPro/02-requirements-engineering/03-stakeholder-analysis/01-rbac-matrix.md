# RBAC Permission Matrix — Academia Pro Phase 1

> This document resolves gap `HIGH-005` from `_context/gap-analysis.md`. It defines the complete permission matrix for all Phase 1 actions and roles. This matrix is the authoritative reference for middleware and policy implementation.
>
> **Legend:**
> - `✓` — Permitted unconditionally within tenant scope
> - `✗` — Denied
> - `✓*` — Permitted with conditions (see footnote)
> - `—` — Not applicable to this role

---

## Role Definitions

| Role Code | Role Name | Panel | Scope |
|---|---|---|---|
| `SA` | Super Admin | `/adminpanel/` | Platform-wide (all tenants, logged) |
| `OW` | School Owner / Director | `/` | Own tenant only |
| `HT` | Head Teacher | `/` | Own tenant only |
| `CT` | Class Teacher | `/` | Own tenant, assigned classes only |
| `BU` | Accounts Bursar | `/` | Own tenant only |
| `RC` | Receptionist | `/` | Own tenant only |
| `PA` | Parent / Guardian | `/memberpanel/` | Own children only |
| `ST` | Student | `/memberpanel/` | Own records only |

---

## Section A: Authentication and User Management

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `auth:login` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `auth:logout` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `auth:change_own_password` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `users:invite` | ✓ | ✓ | ✓* ¹ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `users:view_all` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `users:edit` | ✓ | ✓ | ✓* ² | ✗ | ✗ | ✗ | ✗ | ✗ |
| `users:deactivate` | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `users:delete` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `roles:assign` | ✓ | ✓ | ✓* ³ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `roles:create_custom` | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

**Footnotes:**
1. Head Teacher may invite Class Teacher, Bursar, and Receptionist roles only — not Owner or Head Teacher.
2. Head Teacher may edit users with lower privilege (Class Teacher, Bursar, Receptionist) — not Owner or peer Head Teachers.
3. Head Teacher may assign roles with strictly lower privilege than their own.

---

## Section B: Student Information System

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `students:create` | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| `students:view` | ✓ | ✓ | ✓ | ✓* ⁴ | ✓* ⁵ | ✓ | ✓* ⁶ | ✓* ⁷ |
| `students:edit` | ✓ | ✓ | ✓ | ✗ | ✗ | ✓* ⁸ | ✗ | ✗ |
| `students:edit_global_identity` | ✓* ⁹ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `students:transfer_out` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `students:delete` (soft) | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `students:data_export` (PDPO) | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `students:search` | ✓ | ✓ | ✓ | ✓* ⁴ | ✓ | ✓ | ✗ | ✗ |

**Footnotes:**
4. Class Teacher may view only students in their assigned classes.
5. Bursar may view student name, class, admission number, and fee balance — not medical summary or disciplinary records.
6. Parent may view their own child's data only.
7. Student may view their own data only.
8. Receptionist may edit non-identity fields (contact details, emergency contacts) — not name, DOB, or gender.
9. Super Admin may edit global identity fields in documented exceptional circumstances only; action is logged with justification.

---

## Section C: Academics Setup

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `academics:create_year` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `academics:edit_year` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `academics:create_class` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `academics:edit_class` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `academics:create_subject` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `academics:create_timetable` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `academics:view_timetable` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓* ⁶ | ✓* ⁷ |
| `academics:assign_teacher` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

---

## Section D: Fees Management

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `fees:define_structure` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| `fees:record_payment` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| `fees:view_balance` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `fees:view_payment_history` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `fees:request_refund` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| `fees:approve_refund` | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `fees:delete_payment` | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `fees:view_collection_report` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| `fees:export_defaulters` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| `fees:configure_reminders` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

*Note: `fees:delete_payment` is permanently denied for all roles. Payments are immutable; only refunds via the refund workflow are permitted.*

---

## Section E: Attendance

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `attendance:submit` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✗ | ✗ |
| `attendance:view` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `attendance:amend_own` | ✓ | ✓ | ✓ | ✓* ¹¹ | ✗ | ✗ | ✗ | ✗ |
| `attendance:amend_any` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `attendance:view_monthly_report` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✗ | ✗ |

**Footnotes:**
10. Class Teacher limited to their assigned classes only.
11. Class Teacher may amend own attendance entries within 48 hours only.

---

## Section F: Examinations and Grading

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `exams:create` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `exams:edit` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `exams:enter_marks` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✗ | ✗ |
| `exams:unlock` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `exams:compute_grades` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `exams:view_results` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `exams:publish_results` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `exams:export_uneb_registration` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

---

## Section G: Report Cards

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `reports:generate_single` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✗ | ✗ |
| `reports:generate_bulk` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `reports:add_comment` | ✓ | ✓ | ✓ | ✓* ¹² | ✗ | ✗ | ✗ | ✗ |
| `reports:release` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `reports:view` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `reports:download_pdf` | ✓ | ✓ | ✓ | ✓* ¹⁰ | ✗ | ✗ | ✓* ⁶ | ✓* ⁷ |
| `reports:school_performance` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

**Footnotes:**
12. Class Teacher may add/edit their own comment on report cards for their assigned students. After the release date, only Head Teacher and above may amend.

---

## Section H: Government Exports

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `emis:export` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `emis:view` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

---

## Section I: School Settings

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `settings:view` | ✓ | ✓ | ✓* ¹³ | ✗ | ✓* ¹³ | ✗ | ✗ | ✗ |
| `settings:edit_school_profile` | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `settings:edit_academic` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `settings:edit_fee_config` | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ |
| `settings:edit_notifications` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `settings:edit_rbac` | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

**Footnotes:**
13. Head Teacher may view academic settings; Bursar may view fee configuration settings only.

---

## Section J: Audit Trail and Platform Administration

| Permission | SA | OW | HT | CT | BU | RC | PA | ST |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `audit:view_own_tenant` | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `audit:view_all_tenants` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `tenants:create` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `tenants:suspend` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `tenants:view_all` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `tenants:impersonate` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `platform:analytics` | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

---

## Privilege Hierarchy

For the purpose of role assignment (FR-RBAC-002, BR-RBAC-002), the privilege levels are:

| Level | Role(s) |
|---|---|
| 5 (highest) | Super Admin |
| 4 | School Owner / Director |
| 3 | Head Teacher |
| 2 | Class Teacher, Accounts Bursar, Receptionist |
| 1 (lowest) | Parent, Student |

A user may only assign roles at levels strictly below their own level. Example: Head Teacher (level 3) may assign level 2 roles but not level 3, 4, or 5 roles.

---

## Implementation Notes

1. **Permission caching:** All resolved permissions are cached in Redis with a 15-minute TTL per `(user_id, tenant_id)` key. On any role or permission change, the affected user's cache key is deleted immediately (not on TTL expiry).
2. **Default deny:** Any permission not explicitly listed in this matrix and not granted via a role is denied.
3. **Cross-tenant requests:** Any authenticated request from a non-Super Admin user where the target resource's `tenant_id` differs from the user's `tenant_id` returns HTTP 404 (not 403 — to prevent tenant enumeration).
4. **Tenant-level overrides:** The School Owner may disable specific permissions for a role within their school (e.g., disable `fees:request_refund` for the Bursar role) via the `tbl_franchise_role_overrides` table. This overrides the default grant.
5. **Custom roles:** School Owner may create custom roles with any subset of the permissions they themselves hold. Custom roles follow the same priority resolution as built-in roles.

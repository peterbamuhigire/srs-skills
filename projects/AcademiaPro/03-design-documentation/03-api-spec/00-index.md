# OpenAPI 3.1 Specification — Academia Pro Phase 1

**Document ID:** DD-03-00
**Project:** Academia Pro
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review
**Gap Resolved:** HIGH-003

---

## Purpose

This directory contains the complete OpenAPI 3.1 specification for all Phase 1 API endpoints.
The spec is the authoritative contract between the backend (Laravel 11 / PHP 8.2), the web
frontend (React 18 / TypeScript), and the Android mobile clients (Kotlin / Jetpack Compose).

No endpoint may be implemented that is not described here. No described endpoint may be
omitted from the Phase 1 deliverable without a formal change request.

---

## Base URL

| Environment | Base URL |
|-------------|---------|
| Development | `http://localhost:8000/api/v1` |
| Staging | `https://staging.academiapro.chwezi.com/api/v1` |
| Production | `https://app.academiapro.com/api/v1` |

Super Admin endpoints use the prefix `/adminpanel/api/v1`.

---

## Authentication

All endpoints (except `/auth/login` and `/auth/refresh`) require:

```
Authorization: Bearer <access_token>
```

The access token is a Laravel Sanctum token with the following claims stored in the
`personal_access_tokens.abilities` JSON column:

```json
{ "tenant_id": 42, "user_id": 1007, "role": "bursar" }
```

Super Admin tokens carry `"tenant_id": null` and `"role": "super_admin"`.

---

## File Structure

| File | Endpoints Covered | FR Groups |
|------|------------------|-----------|
| `01-auth.yaml` | Authentication and session management | FR-AUTH-001 – FR-AUTH-006 |
| `02-tenants.yaml` | Tenant lifecycle (Super Admin) | FR-TNT-001 – FR-TNT-003 |
| `03-students.yaml` | Student Information System | FR-SIS-001 – FR-SIS-005 |
| `04-academics.yaml` | Academic year, classes, timetable | FR-ACA-001 – FR-ACA-004 |
| `05-fees.yaml` | Fee structures and payments | FR-FEE-001 – FR-FEE-007 |
| `06-attendance.yaml` | Attendance entry and reporting | FR-ATT-001 – FR-ATT-004 |
| `07-examinations.yaml` | Exams, marks, grading, UNEB | FR-EXM-001 – FR-EXM-008 |
| `08-reports.yaml` | Report cards and school performance | FR-RPT-001 – FR-RPT-004 |
| `09-rbac.yaml` | Users, roles, permissions | FR-RBAC-001 – FR-RBAC-005 |
| `10-emis-audit.yaml` | EMIS export and audit trail | FR-EMIS-001, FR-AUD-001 |
| `11-schemas.yaml` | Shared reusable components and schemas | All |

---

## Common Response Envelopes

All API responses use a consistent envelope.

### Success (single object)

```json
{
  "success": true,
  "data": { }
}
```

### Success (list)

```json
{
  "success": true,
  "data": [ ],
  "meta": {
    "total": 142,
    "page": 1,
    "per_page": 25,
    "last_page": 6
  }
}
```

### Error

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The given data was invalid.",
    "details": {
      "field_name": ["Validation message."]
    }
  }
}
```

---

## Standard Error Codes

| Code | HTTP | Meaning |
|------|------|---------|
| `UNAUTHENTICATED` | 401 | No valid token |
| `TOKEN_EXPIRED` | 401 | Access token expired |
| `TOKEN_REVOKED` | 401 | Refresh token revoked |
| `FORBIDDEN` | 403 | Authenticated but insufficient permission |
| `TENANT_SUSPENDED` | 403 | School account suspended |
| `NOT_FOUND` | 404 | Resource not found |
| `VALIDATION_ERROR` | 422 | Request body failed validation |
| `DUPLICATE_PAYMENT` | 409 | Double-payment detected (FR-FEE) |
| `CONFLICT` | 409 | State conflict (e.g., locked record) |
| `SERVER_ERROR` | 500 | Unexpected server error |

---

## AI Module Endpoints

> All endpoints in this group require: (a) a valid JWT with an authenticated tenant, (b) the tenant to have an active `tenant_ai_modules` record, and (c) the specific feature to be enabled in `tenant_ai_features`. Requests that fail condition (b) or (c) return HTTP 402 `AI_MODULE_INACTIVE`.

### AI Feature Management

| Method | Path | Description | Roles |
|---|---|---|---|
| `GET` | `/api/v1/ai/module` | Get the tenant's AI module status, plan, and budget | owner, super_admin |
| `PATCH` | `/api/v1/ai/features/{slug}` | Enable or disable a specific AI feature | owner |
| `PATCH` | `/api/v1/ai/budget` | Update the monthly AI budget ceiling | owner |

### AI Feature Execution

| Method | Path | Description | Roles |
|---|---|---|---|
| `POST` | `/api/v1/ai/report-card-comments` | Generate suggested report card comments for a class | teacher, head_teacher |
| `GET` | `/api/v1/ai/insights/at-risk` | Get the current at-risk student list for this tenant | owner, head_teacher, teacher |
| `GET` | `/api/v1/ai/insights/fee-risk` | Get the fee default prediction list for the current term | owner, bursar |
| `GET` | `/api/v1/ai/insights/sentiment` | Get the current parent sentiment summary | owner, head_teacher |
| `GET` | `/api/v1/ai/insights/briefing` | Get the latest weekly owner briefing narrative | owner, head_teacher |

### AI Usage and Billing

| Method | Path | Description | Roles |
|---|---|---|---|
| `GET` | `/api/v1/ai/usage` | Get AI usage for the current billing period (per-feature breakdown) | owner, super_admin |
| `GET` | `/api/v1/ai/usage/users` | Get per-user AI usage for the current billing period | owner |
| `GET` | `/adminpanel/api/v1/ai/usage` | Get AI usage across all tenants (Super Admin) | super_admin |

### AI Feedback

| Method | Path | Description | Roles |
|---|---|---|---|
| `POST` | `/api/v1/ai/feedback` | Submit thumbs-up/down feedback on an AI output | teacher, owner, head_teacher, bursar |

### Super Admin — AI Module Management

| Method | Path | Description | Roles |
|---|---|---|---|
| `POST` | `/adminpanel/api/v1/tenants/{id}/ai-module` | Activate the AI module for a tenant | super_admin |
| `PATCH` | `/adminpanel/api/v1/tenants/{id}/ai-module` | Update AI module plan or status | super_admin |
| `DELETE` | `/adminpanel/api/v1/tenants/{id}/ai-module` | Cancel the AI module for a tenant | super_admin |

### Key Response Schemas

**GET /api/v1/ai/insights/at-risk — 200 OK:**
```json
{
  "generated_at": "2026-04-07T06:00:00Z",
  "period": "2026-04",
  "high_risk_count": 14,
  "medium_risk_count": 23,
  "students": [
    {
      "student_uid": "uuid",
      "name": "Sandra Nakato",
      "class": "S.4A",
      "risk_level": "high_risk",
      "signal": "Attendance 54% and average mark 38% this term",
      "attendance_pct": 54,
      "avg_mark_pct": 38,
      "days_since_login": 12
    }
  ]
}
```

**POST /api/v1/ai/report-card-comments — 200 OK:**
```json
{
  "comments": [
    {
      "student_uid": "uuid",
      "generated_comment": "Sandra has shown strong performance in Mathematics this term...",
      "confidence": "high",
      "status": "pending_review"
    }
  ]
}
```

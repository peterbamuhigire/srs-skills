# HR and Payroll Module Endpoints

All endpoints in this section require `Authorization: Bearer <token>` and the `hr` module claim in the JWT. The `tenant_id` is resolved exclusively from the token.

---

## GET /api/v1/hr/employees

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/hr/employees` |
| **Auth Required** | Yes — `hr.read` permission |
| **Description** | Returns a paginated list of employees for the authenticated tenant. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `department_id` | string (UUID) | No | Filter by department. |
| `branch_id` | string (UUID) | No | Filter by branch. |
| `status` | string | No | `active`, `on_leave`, `terminated`. Default: `active`. |
| `search` | string | No | Partial match on name, employee number, or email. |
| `page` | integer | No | Page number (default: 1). |
| `per_page` | integer | No | Results per page (default: 25, max: 100). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "emp-uuid-0042",
        "employee_number": "EMP-0042",
        "full_name": "Grace Namutebi",
        "department_id": "dept-uuid-003",
        "department_name": "Finance",
        "branch_id": "branch-uuid-001",
        "designation": "Accountant II",
        "employment_type": "permanent",
        "start_date": "2022-06-01",
        "status": "active",
        "nssf_number": "CF123456",
        "tin": "1001234567"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 67, "total_pages": 3 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`.

---

## POST /api/v1/hr/employees

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/hr/employees` |
| **Auth Required** | Yes — `hr.write` permission |
| **Description** | Creates a new employee record. The employee is assigned to a department, branch, and payroll grade. |

**Request Body:**

```json
{
  "first_name": "Robert",
  "last_name": "Okello",
  "date_of_birth": "1990-03-15",
  "gender": "male",
  "national_id": "CM90000012345ABCD",
  "tin": "1009876543",
  "nssf_number": "CF654321",
  "email": "r.okello@acme.co.ug",
  "phone": "+256750000099",
  "department_id": "dept-uuid-005",
  "branch_id": "branch-uuid-001",
  "designation": "Sales Executive",
  "employment_type": "permanent",
  "start_date": "2026-04-07",
  "payroll_grade_id": "grade-uuid-003",
  "bank_account": {
    "bank_name": "Stanbic Bank",
    "branch": "Kampala Main",
    "account_number": "9030001234567"
  }
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `first_name` | string | Yes | Legal first name. |
| `last_name` | string | Yes | Legal last name. |
| `national_id` | string | Yes | National ID or passport number. Must be unique within the tenant. |
| `tin` | string | No | URA Tax Identification Number. |
| `nssf_number` | string | No | NSSF membership number. |
| `department_id` | string (UUID) | Yes | Assigned department. |
| `branch_id` | string (UUID) | Yes | Primary branch. |
| `employment_type` | string | Yes | `permanent`, `contract`, `casual`. |
| `start_date` | string (ISO 8601) | Yes | Employment start date. |
| `payroll_grade_id` | string (UUID) | Yes | Payroll grade that defines the base salary and allowances. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "emp-uuid-0068",
    "employee_number": "EMP-0068",
    "full_name": "Robert Okello",
    "status": "active",
    "created_at": "2026-04-07T08:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 409 `CONFLICT` (duplicate national ID or TIN within tenant), 404 `NOT_FOUND` (invalid `department_id`, `branch_id`, or `payroll_grade_id`).

---

## POST /api/v1/hr/leave/applications

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/hr/leave/applications` |
| **Auth Required** | Yes — `hr.leave` permission |
| **Description** | Submits a leave application for an employee. The application enters the approval workflow. Leave entitlement is validated against the employee's current leave balance; insufficient balance returns 422. |

**Request Body:**

```json
{
  "employee_id": "emp-uuid-0042",
  "leave_type_id": "ltype-uuid-001",
  "start_date": "2026-04-14",
  "end_date": "2026-04-18",
  "reason": "Annual leave — family event.",
  "relief_officer_id": "emp-uuid-0031"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `employee_id` | string (UUID) | Yes | Employee applying for leave. |
| `leave_type_id` | string (UUID) | Yes | Leave type (e.g., Annual, Sick, Maternity). |
| `start_date` | string (ISO 8601) | Yes | First day of leave. |
| `end_date` | string (ISO 8601) | Yes | Last day of leave. Must be ≥ `start_date`. |
| `reason` | string | No | Reason for leave. |
| `relief_officer_id` | string (UUID) | No | Employee covering during the absence. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "lapp-uuid-0099",
    "reference": "LVA-2026-0099",
    "employee_id": "emp-uuid-0042",
    "leave_type": "Annual Leave",
    "days_requested": 5,
    "status": "pending_approval",
    "created_at": "2026-04-05T09:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing fields or `end_date` before `start_date`. |
| 404 | `NOT_FOUND` | Invalid `employee_id` or `leave_type_id`. |
| 422 | `UNPROCESSABLE_ENTITY` | Insufficient leave balance; overlapping leave application exists. |

---

## POST /api/v1/hr/leave/applications/{id}/approve

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/hr/leave/applications/{id}/approve` |
| **Auth Required** | Yes — `hr.leave.approve` permission |
| **Description** | Approves or rejects a leave application. On approval, the employee's leave balance is decremented by the number of approved days. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Leave application identifier. |

**Request Body:**

```json
{
  "action": "approve",
  "comment": "Approved. Ensure handover notes are submitted."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `action` | string | Yes | `approve` or `reject`. |
| `comment` | string | No | Approver comment. |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "lapp-uuid-0099",
    "status": "approved",
    "approved_by": "emp-uuid-0010",
    "approved_at": "2026-04-05T11:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (application already processed), 403 `FORBIDDEN` (approver is the same as the applicant).

---

## POST /api/v1/hr/attendance

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/hr/attendance` |
| **Auth Required** | Yes — `hr.attendance` permission |
| **Description** | Records an attendance entry for an employee. The `source` field identifies the recording mechanism for audit purposes. |

**Request Body:**

```json
{
  "employee_id": "emp-uuid-0042",
  "date": "2026-04-05",
  "check_in": "08:02:00",
  "check_out": "17:05:00",
  "source": "biometric",
  "notes": null
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `employee_id` | string (UUID) | Yes | Employee whose attendance is being recorded. |
| `date` | string (ISO 8601) | Yes | Attendance date. |
| `check_in` | string (HH:MM:SS) | Yes | Check-in time. |
| `check_out` | string (HH:MM:SS) | No | Check-out time. Can be submitted separately on departure. |
| `source` | string | Yes | `biometric`, `manual`, `mobile_app`. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "att-uuid-0512",
    "employee_id": "emp-uuid-0042",
    "date": "2026-04-05",
    "check_in": "08:02:00",
    "check_out": null,
    "hours_worked": null,
    "source": "biometric",
    "created_at": "2026-04-05T08:02:00Z"
  },
  "error": null
}
```

**Error Codes:** 400 `BAD_REQUEST`, 409 `CONFLICT` (attendance record for this employee and date already exists).

---

## POST /api/v1/hr/payroll/runs

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/hr/payroll/runs` |
| **Auth Required** | Yes — `payroll.run` permission |
| **Description** | Initiates a payroll run for a specified period and set of branches. The system calculates gross pay, PAYE, NSSF employee and employer contributions, and any configured deductions for all active employees in the specified branches. The run is created in `draft` status pending approval. |

**Request Body:**

```json
{
  "period_id": "pp-uuid-2026-04",
  "branch_ids": ["branch-uuid-001", "branch-uuid-002"],
  "notes": "April 2026 payroll run."
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `period_id` | string (UUID) | Yes | Payroll period identifier. Must be an open, unprocessed period. |
| `branch_ids` | array of string (UUID) | Yes | Branches to include. Must be non-empty. |
| `notes` | string | No | Optional run description. |

**Success Response — 201 Created:**

```json
{
  "success": true,
  "data": {
    "id": "prun-uuid-2026-04",
    "reference": "PAY-2026-04-001",
    "period_id": "pp-uuid-2026-04",
    "status": "draft",
    "employees_included": 67,
    "total_gross": 189000000.00,
    "total_paye": 23400000.00,
    "total_nssf_employee": 5670000.00,
    "total_nssf_employer": 9450000.00,
    "total_net": 159930000.00,
    "created_at": "2026-04-05T12:00:00Z"
  },
  "error": null
}
```

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 400 | `BAD_REQUEST` | Missing required fields or empty `branch_ids`. |
| 404 | `NOT_FOUND` | Invalid `period_id` or any `branch_id`. |
| 409 | `CONFLICT` | A payroll run for this period and overlapping branches already exists. |
| 422 | `UNPROCESSABLE_ENTITY` | Period is already closed or a prior run for the period was approved. |

---

## POST /api/v1/hr/payroll/runs/{id}/approve

| Field | Value |
|---|---|
| **Method** | POST |
| **Path** | `/api/v1/hr/payroll/runs/{id}/approve` |
| **Auth Required** | Yes — `payroll.approve` permission |
| **Description** | Approves a draft payroll run. On approval, the system posts the payroll journal to the GL and the run status changes to `approved`. Payslips become available for download. The run cannot be reversed after approval; corrections require a supplementary run. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Payroll run identifier. |

**Request Body:**

```json
{
  "comment": "Approved for April 2026."
}
```

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "id": "prun-uuid-2026-04",
    "status": "approved",
    "gl_entry_id": "jnl-uuid-payroll-2026-04",
    "approved_by": "emp-uuid-0010",
    "approved_at": "2026-04-05T13:00:00Z"
  },
  "error": null
}
```

**Error Codes:** 404 `NOT_FOUND`, 409 `CONFLICT` (run already approved or rejected), 403 `FORBIDDEN`.

---

## GET /api/v1/hr/payroll/runs/{id}/payslips

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/hr/payroll/runs/{id}/payslips` |
| **Auth Required** | Yes — `payroll.read` permission |
| **Description** | Returns a paginated list of payslip summaries for all employees included in the specified payroll run. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Payroll run identifier. |

**Query Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `department_id` | string (UUID) | No | Filter payslips by department. |
| `page` | integer | No | Page number (default: 1). |

**Success Response — 200 OK:**

```json
{
  "success": true,
  "data": {
    "run_id": "prun-uuid-2026-04",
    "run_reference": "PAY-2026-04-001",
    "items": [
      {
        "employee_id": "emp-uuid-0042",
        "employee_number": "EMP-0042",
        "full_name": "Grace Namutebi",
        "department": "Finance",
        "gross_pay": 3200000.00,
        "paye": 396000.00,
        "nssf_employee": 96000.00,
        "other_deductions": 0.00,
        "net_pay": 2708000.00,
        "currency": "UGX"
      }
    ],
    "pagination": { "page": 1, "per_page": 25, "total": 67, "total_pages": 3 }
  },
  "error": null
}
```

**Error Codes:** 401 `UNAUTHORIZED`, 403 `FORBIDDEN`, 404 `NOT_FOUND`.

---

## GET /api/v1/hr/payroll/runs/{id}/payslips/{employee_id}/download

| Field | Value |
|---|---|
| **Method** | GET |
| **Path** | `/api/v1/hr/payroll/runs/{id}/payslips/{employee_id}/download` |
| **Auth Required** | Yes — `payroll.read` permission (own payslip) or `payroll.download_all` (any payslip) |
| **Description** | Returns the PDF payslip for a specific employee within a payroll run. The response body is a binary PDF stream, not a JSON envelope. The `Content-Disposition` header instructs the client to treat the response as a file download. |

**Path Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `id` | string (UUID) | Payroll run identifier. |
| `employee_id` | string (UUID) | Employee identifier. |

**Success Response — 200 OK:**

- `Content-Type: application/pdf`
- `Content-Disposition: attachment; filename="Payslip_EMP-0042_2026-04.pdf"`
- Response body: binary PDF data.

**Error Codes:**

| Status | Code | Condition |
|---|---|---|
| 403 | `FORBIDDEN` | Employee attempts to download another employee's payslip without `payroll.download_all` permission. |
| 404 | `NOT_FOUND` | Payslip not found; run may not yet be approved. |

---
title: "Maduuka Platform — Low-Level Design, Section 5: HR and Payroll Service"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# HR and Payroll Service

**Document ID:** MADUUKA-LLD-005
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Overview

`PayrollService` computes, approves, and distributes monthly payroll for all active staff within a tenant. It enforces Uganda statutory deductions for the 2024/25 financial year: Pay As You Earn (PAYE), National Social Security Fund (NSSF), and Local Service Tax (LST). It depends on the following injected collaborators:

- `StaffRepository` — queries active staff and their salary structures
- `PayrollRunRepository` — creates and updates `payroll_runs`
- `PayslipRepository` — creates `payslips` rows
- `PaymentAccountRepository` — records payroll disbursement against the designated salary payment account
- `AuditLogService` — audit trail writes
- `PDFService` — generates payslip PDFs
- `NotificationService` — dispatches payslips via WhatsApp or email

---

## 2. Tax Computation Methods

### 2.1 computePAYE

```php
public function computePAYE(float $grossMonthly): float;
```

Uganda Income Tax Act, 2024/25 annual bands converted to monthly thresholds:

| Monthly Gross (UGX) | Rate |
|---|---|
| 0 – 235,000 | 0% |
| 235,001 – 335,000 | 10% on the amount above 235,000 |
| 335,001 – 410,000 | 20% on the amount above 335,000 (plus UGX 10,000 from previous band) |
| Above 410,000 | 30% on the amount above 410,000 (plus UGX 25,000 from previous bands) |

Implementation:

```php
public function computePAYE(float $grossMonthly): float
{
    if ($grossMonthly <= 235_000) {
        return 0.0;
    }

    $tax = 0.0;

    if ($grossMonthly > 235_000) {
        $tax += min($grossMonthly - 235_000, 100_000) * 0.10; // Band 2
    }
    if ($grossMonthly > 335_000) {
        $tax += min($grossMonthly - 335_000, 75_000) * 0.20;  // Band 3
    }
    if ($grossMonthly > 410_000) {
        $tax += ($grossMonthly - 410_000) * 0.30;             // Band 4
    }

    return round($tax, 2);
}
```

**Verification example:** gross = UGX 600,000.
- Band 2: 100,000 × 10% = UGX 10,000
- Band 3: 75,000 × 20% = UGX 15,000
- Band 4: 190,000 × 30% = UGX 57,000
- **Total PAYE = UGX 82,000**

---

### 2.2 computeNSSF

```php
/**
 * @return array{employee: float, employer: float}
 */
public function computeNSSF(float $gross): array;
```

Uganda NSSF Act: employee contribution = 5% of gross; employer contribution = 10% of gross.

```php
public function computeNSSF(float $gross): array
{
    return [
        'employee' => round($gross * 0.05, 2),
        'employer' => round($gross * 0.10, 2),
    ];
}
```

NSSF is applied on gross pay before PAYE. The employee contribution is a deduction; the employer contribution is an additional cost to the business, not deducted from the employee's gross.

---

### 2.3 computeLST

```php
public function computeLST(float $grossMonthly, string $district): float;
```

LST is an annual tax divided into monthly instalments. The system holds a `lst_rates` configuration table keyed by `district` and `gross_annual_band`. For Phase 1 (Uganda-first), the Kampala rate is hardcoded as the default:

| Annual Gross (UGX) | Annual LST (UGX) | Monthly Instalment (UGX) |
|---|---|---|
| <= 12,000,000 (UGX 1,000,000/month) | 0 | 0 |
| > 12,000,000 | 100,000 | 8,333 |

```php
public function computeLST(float $grossMonthly, string $district): float
{
    // Phase 1: Kampala rate only. Other districts require lst_rates table lookup.
    $annualGross = $grossMonthly * 12;

    if ($annualGross <= 12_000_000) {
        return 0.0;
    }

    // Kampala: UGX 100,000 per year = UGX 8,333.33 per month
    return round(100_000 / 12, 2);
}
```

*[CONTEXT-GAP: LST rates for districts outside Kampala are not yet configured. The `lst_rates` table must be populated before payroll can be run for staff in other districts. Flag for consultant review before Phase 1 production deployment.]*

---

## 3. PayrollService Method Signatures and Behaviour

### 3.1 computePayroll

```php
public function computePayroll(
    int $franchiseId,
    int $periodMonth,
    int $periodYear,
    int $branchId = null
): PayrollRun;
```

**Pre-conditions:**

- No `payroll_runs` row with `status = 'approved'` may exist for the same `franchiseId`, `period_month`, and `period_year`. A draft may exist; it will be overwritten.

**Behaviour:**

1. Check for an existing approved payroll run for the period; throw `BusinessRuleViolationException` with code `PAYROLL_ALREADY_APPROVED` if found.
2. Query all `staff` rows with `is_active = TRUE AND franchise_id = $franchiseId` (filtered by `branch_id` if `$branchId` is non-null).
3. For each staff member, retrieve the most recent `salary_structures` row where `effective_from <= last_day_of_period`.
4. Compute gross pay: $Gross = basicSalary + housingAllowance + transportAllowance + \sum{otherEarnings}$.
5. Compute deductions:
   - `nssf = computeNSSF($gross)['employee']`
   - `paye = computePAYE($gross - nssf)` — PAYE is computed on gross minus NSSF employee contribution, per URA guidance.
   - `lst = computeLST($gross, $staff->district)`
   - `otherDeductions = SUM(salary_structures.other_deductions)`
6. Compute net pay: $NetPay = Gross - nssf - paye - lst - otherDeductions$.
7. Insert or update a `payslips` row for each staff member.
8. Insert or update the `payroll_runs` row: set `status = 'draft'`, update totals (`total_gross`, `total_deductions`, `total_net`).
9. Fire `PayrollComputed` event; audit observer writes `action = 'payroll.computed'`.
10. Return the `PayrollRun` entity with all associated `payslips`.

---

### 3.2 approvePayroll

```php
public function approvePayroll(int $payrollRunId, int $authorisedBy, int $franchiseId): void;
```

**Pre-conditions:**

- `$authorisedBy` must hold the `hr.payroll.approve` permission (Business Owner only for Phase 1).
- The payroll run must have `status = 'draft'`.

**Behaviour (BR-012):**

1. Verify `$authorisedBy` holds `hr.payroll.approve` permission via `RBACService::can()`.
2. Update `payroll_runs.status = 'approved'`, `approved_by = $authorisedBy`, `approved_at = UTC_NOW()`.
3. Write the payroll disbursement to the financial accounts: call `PaymentAccountRepository::recordTransaction()` for the designated salary payment account with `type = 'payroll'` and `amount = -1 * total_net` (negative = money out).
4. Dispatch `GeneratePayslipJob` for each staff member in the payroll run (asynchronous, queued).
5. Fire `PayrollApproved` event; audit observer writes `action = 'payroll.approved'` with `new_values = { payrollRunId, totalNet, authorisedBy }`.

After approval, the payroll run and its payslips are read-only. Any correction requires a reversal entry in the following period's payroll run, not a modification of the approved run (BR-012).

---

### 3.3 generatePayslip

```php
public function generatePayslip(int $staffId, int $payrollRunId, int $franchiseId): PayslipPDF;
```

**Behaviour:**

1. Retrieve the `payslips` row for `staff_id = $staffId AND payroll_run_id = $payrollRunId AND franchise_id = $franchiseId`.
2. Retrieve staff details, business name, logo URL, and the payroll period.
3. Render the payslip HTML template with all computed values.
4. Call `PDFService::renderFromHtml(string $html): string $pdfFilePath` — server-side HTML-to-PDF conversion (e.g., Dompdf or wkhtmltopdf).
5. Upload the PDF to Wasabi S3 at path `payslips/{franchiseId}/{year}/{month}/{staffId}.pdf`.
6. Update `payslips.pdf_url` with the S3 path.
7. Dispatch delivery:
   - If the staff member has a WhatsApp-capable phone on record, call `NotificationService::sendWhatsApp()` with the PDF attachment via Africa's Talking.
   - Otherwise, if an email is on record, call `NotificationService::sendEmail()` with the PDF as an attachment via the configured SMTP adapter.
8. Set `payslips.sent_at = UTC_NOW()` on successful dispatch.
9. Return `PayslipPDF { staffId, payrollRunId, pdfUrl, sentAt }`.

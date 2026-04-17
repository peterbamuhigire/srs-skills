---
title: "Maduuka Platform — Low-Level Design, Section 6: Reporting Service"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# Reporting Service

**Document ID:** MADUUKA-LLD-006
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Overview

`ReportService` provides all reporting capabilities across Phase 1 modules: POS/Sales, Inventory, Finance, Customer, and HR. It implements the Template Method design pattern: a base report-generation skeleton is defined once, and each report type overrides only the query-building and result-formatting steps.

`ReportService` depends on:

- `ReportRepository` — executes parameterised queries and returns raw result arrays
- `PDFService` — HTML-to-PDF conversion for export
- `CSVService` — serialises result arrays to CSV strings
- `AuditLogService` — logs report generation and export events (for sensitive reports such as payroll and audit trail)

---

## 2. Core Data Structures

### 2.1 ReportRequest

```php
class ReportRequest
{
    public function __construct(
        public readonly string   $reportType,     // e.g., 'sales_summary', 'stock_valuation'
        public readonly int      $franchiseId,
        public readonly string   $dateFrom,        // ISO 8601 date: 'YYYY-MM-DD'
        public readonly string   $dateTo,          // ISO 8601 date: 'YYYY-MM-DD'
        public readonly ?int     $branchId,        // null = all branches
        public readonly ?string  $groupBy,         // 'day' | 'week' | 'month' | 'cashier' | 'product'
        public readonly int      $page = 1,
        public readonly int      $perPage = 25,
    ) {}
}
```

### 2.2 ReportResult

```php
class ReportResult
{
    public function __construct(
        public readonly string  $reportType,
        public readonly array   $rows,
        public readonly array   $summary,         // Aggregated totals row
        public readonly array   $meta,            // Pagination meta
        public readonly string  $generatedAt,     // ISO 8601 datetime
    ) {}
}
```

---

## 3. ReportInterface

Each report type implements this interface:

```php
interface ReportInterface
{
    /**
     * Builds the parameterised query for this report type.
     * Must include WHERE franchise_id = :franchiseId at minimum.
     */
    public function buildQuery(ReportRequest $request): QueryBuilder;

    /**
     * Transforms raw database rows into the report's output structure.
     */
    public function formatResult(array $rows, ReportRequest $request): array;

    /**
     * Returns the summary/totals row for the report.
     */
    public function computeSummary(array $rows, ReportRequest $request): array;
}
```

---

## 4. ReportService Method Signatures and Behaviour

### 4.1 generate

```php
public function generate(ReportRequest $request): ReportResult;
```

**Behaviour (Template Method):**

1. Resolve the concrete `ReportInterface` implementation from a report-type registry (PHP array mapping `reportType` strings to class names).
2. Call `$report->buildQuery($request)` to obtain the parameterised `QueryBuilder`.
3. Apply pagination: `LIMIT $perPage OFFSET ($page - 1) * $perPage`.
4. Execute the query via `ReportRepository::runQuery()`.
5. Call `$report->formatResult($rows, $request)`.
6. Call `$report->computeSummary($rows, $request)`.
7. Assemble and return `ReportResult`.

---

### 4.2 exportPDF

```php
public function exportPDF(ReportResult $result): string $pdfFilePath;
```

**Behaviour:**

1. Render the report result to an HTML string using a Blade/Twig template keyed by `$result->reportType`.
2. Call `PDFService::renderFromHtml(string $html, PaperSize::A4, Orientation::LANDSCAPE): string $pdfFilePath`.
3. Store the generated PDF temporarily in the server's local `storage/reports/` directory.
4. Return the absolute file path; the controller streams the file to the client with `Content-Disposition: attachment`.
5. A scheduled cleanup job deletes report PDFs older than 1 hour from `storage/reports/`.

---

### 4.3 exportCSV

```php
public function exportCSV(ReportResult $result): string $csvContent;
```

**Behaviour:**

1. Extract column headers from the first row of `$result->rows`.
2. Write a UTF-8 BOM prefix (`\xEF\xBB\xBF`) so Excel opens the file correctly on Windows.
3. Iterate `$result->rows`; write each as a comma-separated line with values escaped per RFC 4180.
4. Append the summary row as the final line, prefixed with `"TOTAL"` in the first column.
5. Return the full CSV content as a string; the controller responds with `Content-Type: text/csv; charset=UTF-8` and `Content-Disposition: attachment; filename="{reportType}_{date}.csv"`.

---

## 5. Phase 1 Report Types

| `reportType` | Description | Roles with Access |
|---|---|---|
| `sales_summary` | Total sales, discounts, tax, net revenue grouped by day/week/month or cashier | Owner, Manager, Accountant |
| `sales_by_product` | Units sold and revenue per product | Owner, Manager, Accountant |
| `sales_by_cashier` | Per-cashier session performance | Owner, Manager |
| `pos_session_detail` | Full transaction list for a single POS session | Owner, Manager, Cashier (own sessions) |
| `receipt_gap_report` | Gaps detected in receipt number sequences | Owner, Manager |
| `stock_valuation` | Current stock quantity × cost price per product | Owner, Manager, Stock Manager, Accountant |
| `stock_movement_history` | Chronological log of all stock movements for a product | Owner, Manager, Stock Manager |
| `stock_count_variance` | Expected vs. counted quantities for a completed count | Owner, Manager, Stock Manager |
| `low_stock_items` | Products at or below reorder level | Owner, Manager, Stock Manager |
| `customer_balance_age` | Aged debtors report: outstanding credit balances by age bucket | Owner, Manager, Accountant |
| `expense_summary` | Expenses by category and period | Owner, Manager, Accountant |
| `account_statement` | Transactions for a single payment account | Owner, Accountant |
| `payroll_summary` | Gross, deductions, net pay per payroll run | Owner, HR Manager |
| `supplier_payables` | Amounts owed to suppliers | Owner, Manager, Accountant |

---

## 6. Scheduled Report Service

```php
class ScheduledReportService
{
    /**
     * Generates the report defined by the schedule record and dispatches it
     * to the configured recipients.
     */
    public function dispatch(int $scheduleId, int $franchiseId): void;
}
```

**Behaviour:**

1. Retrieve the `report_schedules` row by `$scheduleId` (columns: `reportType`, `franchiseId`, `recipients` JSON, `deliveryChannel` ENUM `smtp|sms`, `cronExpression`).
2. Build a `ReportRequest` from the schedule configuration, computing `dateFrom` and `dateTo` relative to the current date (e.g., `dateFrom = first_day_of_last_month`, `dateTo = last_day_of_last_month`).
3. Call `ReportService::generate()` to produce the `ReportResult`.
4. If `deliveryChannel = 'smtp'`: call `ReportService::exportPDF()` and send the PDF as an email attachment via the tenant's configured SMTP adapter.
5. If `deliveryChannel = 'sms'`: generate a plain-text summary (totals only; no full row listing) and dispatch via Africa's Talking SMS API.
6. Log the dispatch: insert a `report_dispatch_log` row with `scheduleId`, `dispatched_at`, `recipientCount`, `status`.
7. Fire `ScheduledReportDispatched` event; audit observer writes `action = 'report.scheduled.dispatched'`.

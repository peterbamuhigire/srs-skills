# 15. ReportService

**Namespace:** `App\Services\Reports\ReportService`
**Dependencies:** `ReportRepository`, `PDFService`, `SpreadsheetService`, `AuditLogService`
**Test coverage required:** ≥ 60% (output format tests)
**Design pattern:** Template Method

## 15.1 Template Method Pattern

All report generation classes extend `AbstractReport`. The template method `generate()` defines the invariant steps; subclasses implement the abstract `buildDataset()` and `formatOutput()` methods.

```php
abstract class AbstractReport
{
    /**
     * Template method — invariant report generation pipeline.
     * Subclasses must not override this method.
     */
    final public function generate(array $params, string $format = 'PDF'): ReportOutput
    {
        $this->validateParams($params);          // Validates required parameters (abstract)
        $dataset = $this->buildDataset($params); // Queries database (abstract)
        $this->checkPermission($params);         // Verifies caller has report-level access
        return $this->formatOutput($dataset, $format); // PDF | Excel | JSON (abstract)
    }

    abstract protected function validateParams(array $params): void;
    abstract protected function buildDataset(array $params): array;
    abstract protected function formatOutput(array $dataset, string $format): ReportOutput;
}
```

## 15.2 Report Implementations

### 15.2.1 DailySalesReport

**Class:** `App\Services\Reports\Sales\DailySalesReport`

Generates daily revenue summary by product, territory, and payment method.

**Parameters:** `{date: DateString, territory_id: int|null}`
**Output formats:** PDF (mPDF), Excel (PhpSpreadsheet)
**Scheduled delivery:** Daily 21:00 EAT to Director and Sales Manager.

### 15.2.2 ARAgingReport

**Class:** `App\Services\Reports\AR\ARAgingReport`

Customer Accounts Receivable aging: current, 30, 60, 90, 120+ days.

**Parameters:** `{as_of_date: DateString, customer_id: int|null}`
**Output formats:** PDF, Excel
**Source:** `vw_ar_aging`

### 15.2.3 AgentOutstandingBalancesReport

**Class:** `App\Services\Reports\Agents\AgentOutstandingBalancesReport`

Displays real-time agent cash balance (total invoiced − total verified remittances) per agent, sortable by territory or balance amount.

**Parameters:** `{as_of_date: DateString, territory_id: int|null}`
**Output formats:** PDF, Excel
**Source:** `vw_agent_cash_balance`

### 15.2.4 StockOnHandReport

**Class:** `App\Services\Reports\Inventory\StockOnHandReport`

Warehouse stock on hand by location, product, and batch. Dual-track: separate sections for warehouse and agent-held stock (BR-001).

**Parameters:** `{as_of_date: DateString, location_id: int|null, track: string}`
**Output formats:** PDF, Excel
**Source:** `vw_stock_on_hand` + `vw_agent_stock_on_hand`

### 15.2.5 ProductionSummaryReport

**Class:** `App\Services\Reports\Manufacturing\ProductionSummaryReport`

Production orders summary: planned vs. actual output, yield variance, mass balance status, by-product volumes.

**Parameters:** `{period_start: DateString, period_end: DateString}`
**Output formats:** PDF, Excel

### 15.2.6 PayrollSummaryReport

**Class:** `App\Services\Reports\Payroll\PayrollSummaryReport`

Payroll run summary: total gross, PAYE, NSSF, LST, net pay, by department.

**Parameters:** `{run_id: int}`
**Output formats:** PDF, Excel
**Access restriction:** Finance Director and Payroll Officer only.

### 15.2.7 FarmerPaymentHistoryReport

**Class:** `App\Services\Reports\Farmers\FarmerPaymentHistoryReport`

Full payment history for a cooperative or individual farmer: deliveries, quality grades, deductions, net payments.

**Parameters:** `{farmer_id: int|null, cooperative_id: int|null, period_start: DateString, period_end: DateString}`
**Output formats:** PDF, Excel

### 15.2.8 ParliamentaryBudgetVsActualReport

**Class:** `App\Services\Reports\Budget\ParliamentaryBudgetVsActualReport`

PIBID parliamentary vote expenditure: budget allocation vs. actual spend, variance (UGX and %), percentage consumed.

**Parameters:** `{fiscal_year_id: int, vote_id: int|null, as_of_date: DateString}`
**Output formats:** PDF, Excel
**Source:** `vw_budget_vs_actual` (PIBID mode only)
**Access restriction:** Director and Finance Director only.

### 15.2.9 BIRDCCommercialPLReport

**Class:** `App\Services\Reports\GL\BIRDCCommercialPLReport`

IFRS Profit & Loss Statement for BIRDC commercial operations.

**Parameters:** `{period_start: DateString, period_end: DateString}`
**Output formats:** PDF
**Source:** GL journal lines filtered by `entity_mode IN (0, 2)`

### 15.2.10 GLHashChainIntegrityReport

**Class:** `App\Services\Reports\Audit\GLHashChainIntegrityReport`

Full hash chain integrity scan for all GL accounts (or a single account). Produced on demand by Finance Director or OAG auditor.

**Parameters:** `{account_id: int|null, as_of_date: DateString}`
**Output formats:** PDF
**Source:** `GLService::verifyHashChainIntegrity()` per account

## 15.3 ReportOutput Structure

```php
class ReportOutput
{
    public string $reportType;       // e.g., 'DAILY_SALES'
    public string $format;           // 'PDF' | 'EXCEL' | 'JSON'
    public string $filePath;         // Absolute path to generated file (for PDF/Excel)
    public array  $data;             // Raw dataset (for JSON format)
    public DateTimeString $generatedAt;
    public int    $generatedByUserId;
}
```

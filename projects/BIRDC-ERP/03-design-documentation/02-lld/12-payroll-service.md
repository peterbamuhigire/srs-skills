# 12. PayrollService

**Namespace:** `App\Services\Payroll\PayrollService`
**Dependencies:** `PayrollRunRepository`, `EmployeeRepository`, `AttendanceRepository`, `GLService`, `MobileMoneyService`, `AuditLogService`, `PDFService`
**Test coverage required:** 100% (financial-critical)

## 12.1 Method Signatures

```php
final class PayrollService
{
    /**
     * Compute a full payroll run for a pay period.
     *
     * @param array $period {
     *   period_start: DateString,
     *   period_end: DateString,
     *   pay_date: DateString,
     *   entity_mode: int,       // 0 = BIRDC commercial; 1 = PIBID government pay scales
     * }
     *
     * @return PayrollRun {
     *   run_id: int,
     *   period: array,
     *   status: 'DRAFT',
     *   total_gross: Money,
     *   total_paye: Money,
     *   total_nssf_employer: Money,
     *   total_nssf_employee: Money,
     *   total_lst: Money,
     *   total_net: Money,
     *   employee_lines: PayrollRunLine[],
     * }
     *
     * @throws ActiveRunExistsException  If a payroll run for this period already exists
     *                                   and has not been voided.
     *
     * Business rules:
     *   - Calls sp_run_payroll stored procedure for batch computation.
     *   - All payroll elements (earnings and deductions) are configurable in
     *     tbl_payroll_elements — no hardcoded elements (DC-002).
     *   - PAYE computed by calculatePAYE(); NSSF by calculateNSSF(); LST per local government.
     *   - [CONTEXT-GAP: GAP-008] — URA PAYE tax bands must be confirmed for current tax year.
     *   - Staff loans deducted per tbl_employee_loan_deductions.
     *   - Run is created in DRAFT status; requires Finance Manager approval to lock (BR-010).
     */
    public function computePayroll(array $period): PayrollRun;

    /**
     * Calculate Uganda PAYE for an employee's gross salary.
     *
     * @param Money $grossSalary  Monthly gross salary in UGX.
     *
     * @return Money  PAYE deduction in UGX for the month.
     *
     * Business rules:
     *   - Tax bands are stored in tbl_paye_tax_bands (configurable by Finance Director — DC-002).
     *   - [CONTEXT-GAP: GAP-008] — Exact current UGX thresholds and rates to be confirmed.
     *   - Monthly exemption threshold applied before band calculation.
     *   - Formula (example — to be validated against current URA bands):
     *     $\text{PAYE} = \sum_{i=1}^{n} \min(\text{gross} - \text{lower}_i, \text{upper}_i - \text{lower}_i) \times \text{rate}_i$
     *   - Returns 0 if grossSalary ≤ monthly exemption threshold.
     */
    public function calculatePAYE(Money $grossSalary): Money;

    /**
     * Calculate NSSF contributions for an employee.
     *
     * @param Money $grossSalary  Monthly gross salary in UGX.
     *
     * @return array {employer: Money, employee: Money}
     *
     * Business rules:
     *   - Employer contribution: 10% of gross salary.
     *   - Employee contribution: 5% of gross salary.
     *   - $\text{Employer NSSF} = \text{grossSalary} \times 0.10$
     *   - $\text{Employee NSSF} = \text{grossSalary} \times 0.05$
     *   - Rates are configurable in tbl_nssf_rates (DC-002) in case of regulatory change.
     *   - NSSF remittance schedule exported in NSSF Uganda required format.
     *     [CONTEXT-GAP: GAP-009] — exact format to be confirmed with BIRDC HR.
     */
    public function calculateNSSF(Money $grossSalary): array;

    /**
     * Approve and lock a payroll run.
     *
     * Once locked, no modification to this run is permitted (BR-010).
     *
     * @param int $runId       The payroll run to approve.
     * @param int $approverId  The Finance Manager approving the run.
     *
     * @return void
     *
     * @throws RunNotFoundException           If runId does not exist.
     * @throws InvalidStatusException         If run is not in DRAFT status.
     * @throws SegregationOfDutiesException   If approverId = run.created_by (BR-003).
     *
     * Business rules:
     *   - SoD: approverId ≠ payroll_run.created_by (BR-003).
     *   - Run status set to APPROVED_LOCKED with approver ID and timestamp.
     *   - trg_payroll_lock trigger prevents any subsequent UPDATE on this run row (BR-010).
     *   - GL auto-post on approval:
     *       DR Salary Expense / CR Salary Payable
     *       DR NSSF Employer Expense / CR NSSF Payable
     *       DR PAYE Liability / CR PAYE Payable (net of employee PAYE)
     *   - Payslips generated for all employees (PDF via mPDF or WhatsApp delivery).
     *   - Bank bulk credit transfer file generated.
     *     [CONTEXT-GAP: GAP-006] — file format pending bank confirmation.
     */
    public function approvePayroll(int $runId, int $approverId): void;

    /**
     * Generate a payslip PDF for an employee for a period.
     *
     * @param int        $employeeId
     * @param DateString $periodStart
     *
     * @return string  Absolute server path to the generated PDF file.
     *
     * @throws EmployeeNotFoundException     If employeeId does not exist.
     * @throws NoPayrollDataException        If no approved payroll run exists for this period.
     *
     * Business rules:
     *   - Payslip format includes: employee name, NIN (last 4 digits only for privacy),
     *     department, all earnings, all deductions, net pay, BIRDC employer details, period.
     *   - PDF generated via mPDF; stored at: storage/payslips/{year}/{month}/{employee_id}.pdf.
     *   - Can be delivered via email (PHPMailer) or WhatsApp (Africa's Talking) per employee preference.
     */
    public function generatePayslip(int $employeeId, string $periodStart): string;
}
```

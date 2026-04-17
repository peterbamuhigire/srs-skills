# Payslips and Salary Disbursement

## 7.1 Payslip Generation

**FR-HR-042** — When a payroll run is confirmed, the system shall generate an individual payslip PDF for every employee in the run; each payslip shall display: employee name, employee ID, pay period, department, gross pay, itemised earnings, itemised deductions (statutory and voluntary), net pay, and tenant branding (logo, company name).

**FR-HR-043** — Payslip PDFs shall be generated using mPDF with the tenant's configured page size (default A4); the payslip layout shall be fixed-format and consistent regardless of the number of payroll elements, using a scrollable table structure to accommodate variable element counts.

**FR-HR-044** — The system shall store all generated payslip PDFs in the tenant's document storage and retain them for a minimum of 10 years; payslip records shall be non-deletable at the application layer.

## 7.2 Statutory Schedules

**FR-HR-045** — The system shall generate an NSSF employer schedule export per pay period listing all employees with their NSSF numbers, gross salary, employer contribution, employee contribution, and total remittable amount; the export format shall be compatible with the NSSF online portal upload format `[CONTEXT-GAP: GAP-003 — confirm current NSSF upload format]`.

**FR-HR-046** — The system shall generate a URA PAYE e-return export per pay period listing all employees with their TINs, gross taxable income, PAYE computed, and year-to-date PAYE; the export format shall conform to URA's current e-return template `[CONTEXT-GAP: GAP-002 — confirm URA PAYE e-return format]`.

## 7.3 Salary Disbursement

**FR-HR-047** — The system shall generate a bank payment file from the confirmed payroll run, listing each employee's bank name, account number, account name, and net pay amount; the file format shall be configurable per tenant to match their banking institution's bulk payment format.

**FR-HR-048** — The system shall support bulk MTN MoMo and Airtel Money salary disbursement; when mobile money disbursement is selected, the system shall invoke the applicable mobile money bulk payment API with each employee's registered phone number and net pay amount, and shall record the API transaction reference against each payroll record.

**FR-HR-049** — When a mobile money disbursement transaction fails for any employee, the system shall flag that employee's payment status as "Failed", log the API error message, and present a retry screen to the payroll administrator without requiring a full payroll re-run.

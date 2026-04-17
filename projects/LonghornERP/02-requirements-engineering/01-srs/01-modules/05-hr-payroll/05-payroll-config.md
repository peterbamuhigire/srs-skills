# Payroll Configuration

## 5.1 Payroll Elements

**FR-HR-026** — The system shall support configurable payroll elements of two types: earnings (additions to gross pay) and deductions (subtractions from gross pay); each element shall define: element name, element code, calculation method (fixed amount, percentage of basic, formula), taxability (taxable or non-taxable), and NSSF applicability.

**FR-HR-027** — The system shall provide the following built-in payroll elements that cannot be deleted: Basic Salary, PAYE, NSSF Employee Contribution, NSSF Employer Contribution, Net Pay, and the applicable jurisdiction-specific levies (NITA, NHIF, PSSSF, RSSB) activated by the tenant's country configuration.

**FR-HR-028** — When a tenant activates a country profile (Uganda, Kenya, Tanzania, Rwanda), the system shall auto-enable the statutory elements and tax bands for that country and suppress those of all other countries in the payroll computation.

## 5.2 Employee Payroll Assignments

**FR-HR-029** — The system shall support per-employee element assignments that override the default element definition, allowing individual fixed allowances (transport, housing, medical) to be configured per employee with effective start and end dates.

**FR-HR-030** — When a payroll element assignment's end date is reached, the system shall automatically exclude the element from subsequent payroll runs without requiring manual intervention.

## 5.3 Pay Periods

**FR-HR-031** — The system shall support monthly pay periods as the default; the payroll calendar shall display all periods for the current financial year, marking each as: Open, Processing, Closed, or Paid.

**FR-HR-032** — When a pay period is closed, the system shall prevent further modifications to payroll records for that period; any adjustment shall require creation of a payroll adjustment batch in the next open period.

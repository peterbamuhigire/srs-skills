# Loans and Advances

## 8.1 Loan Setup

**FR-HR-050** — When an HR administrator creates an employee loan record, the system shall capture: loan type (salary advance or structured loan), principal amount, currency, interest rate (default 0% for advances), repayment start period, and total number of instalments.

**FR-HR-051** — The system shall calculate the monthly instalment amount as: $Instalment = \frac{Principal + (Principal \times Rate \times Periods)}{Periods}$ where $Rate$ is the monthly interest rate and $Periods$ is the total number of repayment months; the instalment shall be displayed before final loan approval.

**FR-HR-052** — Loan creation shall require approval from an HR manager or Finance manager (configurable); unapproved loan records shall not affect payroll computation.

## 8.2 Payroll Deduction

**FR-HR-053** — When an approved loan is active, the system shall automatically include the instalment amount as a payroll deduction in each pay period from the repayment start date until the loan balance reaches zero.

**FR-HR-054** — When an employee's net pay after all deductions is less than the loan instalment, the system shall deduct only the available net amount (flooring at zero) and carry the shortfall forward to the next payroll period, updating the outstanding loan balance accordingly.

**FR-HR-055** — The system shall provide a loan ledger per employee displaying: disbursement date, each instalment deducted (amount and pay period), outstanding principal balance, and projected payoff date.

## 8.3 Loan Closure

**FR-HR-056** — When the outstanding loan balance reaches zero, the system shall automatically mark the loan as "Closed", remove the instalment from future payroll runs, and record the closure date in the loan ledger.

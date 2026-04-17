# Payroll Run and Statutory Deductions

## 6.1 Payroll Run Execution

**FR-HR-033** — When a payroll administrator initiates a payroll run, the system shall execute the following steps in order: (1) load all active employees for the pay period, (2) apply attendance deductions for unapproved absent days, (3) compute gross pay per employee, (4) compute statutory deductions, (5) apply voluntary deductions (loans, advances), (6) compute net pay, (7) generate a payroll summary for review, and (8) await final confirmation before posting.

**FR-HR-034** — The system shall compute net pay using the formula:

$NetPay = GrossPay - \sum Deductions$

where $\sum Deductions$ includes PAYE, NSSF employee contribution, NITA levy, and all approved voluntary deductions.

**FR-HR-035** — When the payroll run encounters an employee with a negative net pay (deductions exceed gross), the system shall flag that employee record in the payroll summary, prevent posting until the issue is resolved, and display a descriptive error identifying which deductions caused the shortfall.

## 6.2 PAYE Calculation

**FR-HR-036** — The system shall calculate Uganda PAYE using the tiered tax band formula:

$PAYE = \sum_{i=1}^{n} (Band_i \times Rate_i)$

where $Band_i$ is the portion of taxable income falling within tax band $i$ and $Rate_i$ is the applicable marginal rate for that band; the tax band thresholds and rates shall be configurable by an administrator `[CONTEXT-GAP: GAP-002 — confirm current Uganda PAYE bands]`.

**FR-HR-037** — The system shall apply equivalent band-based PAYE calculation for Kenya (PAYE + NHIF), Tanzania (PAYE + PSSSF), and Rwanda (PAYE + RSSB) when the respective country profile is active; each country's bands and rates shall be independently configurable.

## 6.3 NSSF and Statutory Levies

**FR-HR-038** — The system shall calculate Uganda NSSF contributions as:

$NSSF_{employer} = GrossSalary \times 0.10$

$NSSF_{employee} = GrossSalary \times 0.05$

Both amounts shall be posted to separate GL liability accounts and included in the NSSF employer schedule.

**FR-HR-039** — The system shall calculate the Uganda NITA levy as a fixed monthly amount per employee, configurable by the administrator; the NITA levy shall be reported separately on the NSSF employer schedule.

## 6.4 GL Posting

**FR-HR-040** — When a payroll run is confirmed, the system shall post the following journal entries atomically: (a) Debit salary expense accounts per cost centre, Credit salary payable; (b) Debit PAYE liability, Credit PAYE payable to URA; (c) Debit NSSF employer contribution, Credit NSSF payable; (d) Debit NSSF employee contribution (withheld), Credit NSSF payable.

**FR-HR-041** — Payroll journal entries shall carry the payroll run ID as a reference, enabling drill-down from the GL to the originating payroll run.

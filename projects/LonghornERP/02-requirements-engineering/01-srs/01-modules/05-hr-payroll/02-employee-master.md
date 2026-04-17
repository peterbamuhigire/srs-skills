# Employee Master and Organisational Structure

## 2.1 Employee Record

**FR-HR-001** — When a user creates an employee record, the system shall capture the following mandatory fields: full legal name, national ID number (or passport number), date of birth, gender, nationality, Tax Identification Number (TIN), NSSF number, employment start date, department, job title, and grade/salary scale.

**FR-HR-002** — When an employee record is saved, the system shall assign a unique employee ID in the format `EMP-NNN` scoped to the tenant and prevent duplicate national ID or TIN values within the same tenant.

**FR-HR-003** — The system shall store employee contact data: residential address, personal phone number, personal email, and next-of-kin name and phone number; these fields shall be accessible only to users with the `hr.employee.personal_data.view` permission.

**FR-HR-004** — When a user updates any field on an employee record, the system shall write the old value, new value, acting user identity, and UTC timestamp to the audit log before committing the change.

**FR-HR-005** — The system shall support multiple concurrent employment contracts per employee (e.g., fixed-term then permanent), with each contract recording: contract type (permanent, fixed-term, probation), start date, end date (nullable for open-ended), probation end date, and notice period days.

## 2.2 Organisational Structure

**FR-HR-006** — The system shall maintain a configurable organisation chart with a minimum of 5 hierarchy levels (Company → Division → Department → Team → Employee); the org chart shall drive leave approval routing and payroll cost-centre allocation.

**FR-HR-007** — When a user reassigns an employee to a new department, the system shall record the effective date of the transfer, the originating and destination department IDs, and the acting user in the employee's movement history.

## 2.3 Grade and Salary Scales

**FR-HR-008** — The system shall support a configurable pay grade matrix where each grade defines a minimum salary, midpoint salary, and maximum salary; the payroll run shall warn if an employee's basic salary falls outside the defined grade band.

**FR-HR-009** — The system shall support multiple currencies on employee records for multi-country tenants; the payroll run shall use the employee's contract currency for gross pay computation and convert to the tenant's reporting currency using the exchange rate on the payroll run date.

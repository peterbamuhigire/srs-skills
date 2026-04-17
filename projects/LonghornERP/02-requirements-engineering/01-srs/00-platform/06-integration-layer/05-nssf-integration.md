# 5. NSSF Integration Requirements

`[CONTEXT-GAP: GAP-013 — NSSF Uganda and NSSF Kenya contribution file format, API endpoint, authentication mechanism, and SFTP server details not confirmed. Requirements below use placeholder references to "NSSF-specified format" pending receipt of the official integration specification from both funds.]`

## 5.1 Activation and Scope

**FR-INTG-063:** The system shall activate the NSSF integration adapter when the HR & Payroll module is active and the tenant localisation profile is `UG` or `KE`, when the tenant completes module activation.

**FR-INTG-064:** The system shall apply the Uganda National Social Security Fund (NSSF Uganda) contribution rules and file format for tenants with profile `UG`, and the Kenya National Social Security Fund (NSSF Kenya) contribution rules and file format for tenants with profile `KE`, when generating a monthly contribution file.

## 5.2 Contribution File Generation

**FR-INTG-065:** The system shall generate a monthly NSSF contribution file containing employee names, national identification numbers, employee NSSF numbers, gross salary, employer contribution amount, and employee contribution amount for all active employees in the payroll run, when the Payroll module confirms the monthly payroll close for the relevant pay period.

**FR-INTG-066:** The system shall format the contribution file in the NSSF-specified data format and encoding for the active localisation profile (`UG` or `KE`), when the file is prepared for submission.

**FR-INTG-067:** The system shall allow an authorised Payroll administrator to preview the contribution file before submission, displaying all employee records and computed contribution amounts, when the file generation process completes.

## 5.3 Submission

**FR-INTG-068:** The system shall submit the generated contribution file to the NSSF portal via the NSSF REST API or SFTP, depending on the submission method specified for the active localisation profile, when the Payroll administrator confirms the file for submission.

**FR-INTG-069:** The system shall record the NSSF submission reference number, submission timestamp (UTC), and submission status against the corresponding payroll period record, when the NSSF portal acknowledges receipt of the contribution file.

## 5.4 Error Handling

**FR-INTG-070:** The system shall surface validation errors returned by the NSSF portal — including rejected employee records and the specific rejection reasons — to the Payroll administrator, when the NSSF portal returns an error or partial-acceptance response.

**FR-INTG-071:** The system shall allow the Payroll administrator to correct rejected records and resubmit the corrected file for the same pay period without regenerating the entire contribution batch, when a partial rejection requires targeted correction.

## 5.5 Audit and Reconciliation

**FR-INTG-072:** The system shall retain a copy of every generated NSSF contribution file and its submission outcome for a minimum of 7 years, when files are generated and submitted, in compliance with statutory record-keeping requirements.

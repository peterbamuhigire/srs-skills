# Subcontractor Management

## 6.1 Overview

Subcontractors are external companies or individuals engaged to perform part of a project's scope under a separate contract. This section specifies requirements for the subcontractor register, linking subcontractor work to Procurement POs, managing subcontractor payments, and applying PPDA compliance requirements for government projects.

## 6.2 Subcontractor Register

**FR-PROJ-053:** When a user with `projects.edit` permission adds a subcontractor to a project, the system shall create a project subcontractor record linking an existing Procurement module supplier to the project. Each project subcontractor record shall store:

- Supplier (lookup to Procurement supplier register; required)
- Scope of Work (text, minimum 10 characters; required)
- Subcontract Value (numeric, ≥ 0; required)
- Subcontract Start Date (date; required)
- Subcontract End Date (date; must be ≥ Start Date; required)
- Contract Reference Number (string; optional for non-government projects, required for Government project type)
- PPDA Compliant (boolean; required for Government project type; read-only for non-government projects, value: N/A)
- Status (enumeration: Active, Completed, Terminated; default: Active)

**FR-PROJ-054:** The system shall display the total subcontract value as a running sum on the project detail screen under **Subcontractors**: $TotalSubcontractValue = \sum SubcontractValue_i$ across all Active and Completed subcontractor records on the project.

## 6.3 PO Linkage

**FR-PROJ-055:** The system shall allow a user to link one or more Procurement module POs to a project subcontractor record. The linked POs must have their `supplier_id` field matching the subcontractor's supplier. If the PO supplier does not match, the system shall reject the linkage with HTTP 422 and the error "PO supplier does not match subcontractor supplier."

**FR-PROJ-056:** The system shall display a subcontractor cost summary showing for each project subcontractor: Subcontract Value, Total PO Value (sum of linked PO amounts), Paid to Date (sum of confirmed payments against linked POs), Outstanding Balance ($SubcontractValue - PaidToDate$), and % Paid.

## 6.4 Subcontractor Payment Tracking

**FR-PROJ-057:** When a Procurement module payment is confirmed against a PO that is linked to a project subcontractor record, the system shall automatically update the subcontractor's Paid to Date figure within 60 seconds of payment confirmation.

**FR-PROJ-058:** When the Paid to Date for a subcontractor reaches or exceeds the Subcontract Value, the system shall display a warning banner on the subcontractor record: "Total payments have reached the subcontract ceiling. Raise a contract variation before approving further payments."

## 6.5 PPDA Compliance

**FR-PROJ-059:** For projects of type Government, when a user adds a subcontractor record without setting PPDA Compliant = true, the system shall display a non-blocking warning banner: "Government projects require PPDA compliance documentation for all subcontractors. Mark as PPDA Compliant only after uploading the required procurement documentation."

**FR-PROJ-060:** The system shall allow a user to attach documents to a project subcontractor record. Accepted file types are PDF, DOCX, XLSX, and image formats (JPEG, PNG). Maximum file size per attachment is 20 MB. Document attachments shall be stored with a description field and the upload timestamp.

**FR-PROJ-061:** The system shall generate a Subcontractor Compliance Report for a government project listing all subcontractors with columns: Supplier Name, Contract Reference, Subcontract Value, PPDA Compliant status, and attachment count. This report shall be exportable to PDF and Excel.

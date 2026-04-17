# Tax Management Requirements

## 6.1 Overview

The Tax Management module configures, calculates, and reports on Value Added Tax (VAT) and withholding tax obligations in compliance with the Uganda VAT Act and Uganda Income Tax Act. Pay As You Earn (PAYE) band application is owned by the HR/Payroll module; this section defines the configuration interface and GL posting side only. EFRIS integration is flagged as deferred to the Platform Integration Layer (FR-INTG series).

## 6.2 VAT Configuration

**FR-ACCT-079:** The system shall allow an authorised user to configure VAT registration settings for a tenant by providing: VAT registration number, effective registration date, default VAT rate (percentage), and the return filing period (monthly or quarterly).

**FR-ACCT-080:** The system shall default the VAT rate to 18% for tenants selecting the Uganda localisation profile at onboarding; this default shall be editable by a Super Admin when the applicable rate changes by statutory instrument.

**FR-ACCT-081:** The system shall support the following tax codes, each configurable per transaction line: Standard Rate (applies the configured VAT %), Zero Rate (0%), Exempt (excluded from VAT return), and Out of Scope (excluded from all tax calculations).

**FR-ACCT-082:** The system shall map each tax code to the correct VAT Control GL account at posting time: Standard Rate and Zero Rate transactions post to VAT Control (Output) for sales and VAT Control (Input) for purchases; Exempt and Out of Scope transactions generate no VAT GL entry.

## 6.3 VAT Calculation on Transactions

**FR-ACCT-083:** The system shall auto-calculate VAT on each line of a sales invoice when the invoice is saved, applying the tax code assigned to the line item; VAT amount shall be calculated as:

$VATAmount = LineNetAmount \times \frac{TaxRate}{100}$

**FR-ACCT-084:** The system shall auto-calculate input VAT on each line of a purchase invoice when the invoice is saved, applying the same formula as FR-ACCT-083 using the tax code assigned to the purchase line.

**FR-ACCT-085:** The system shall display the net amount, VAT amount, and gross amount as separate fields on every sales and purchase invoice line, and shall display totals for each at the invoice footer.

**FR-ACCT-086:** The system shall post VAT amounts to the VAT Control (Output) or VAT Control (Input) accounts as part of the auto-generated sub-ledger journal per FR-ACCT-027 and FR-ACCT-028.

## 6.4 VAT Return

**FR-ACCT-087:** The system shall generate a VAT Return report for a selected return period when an authorised user requests it; the report shall present: total output tax (sales VAT collected), total input tax (purchase VAT paid), and net VAT payable or refundable, calculated as:

$NetVAT = OutputTax - InputTax$

**FR-ACCT-088:** The system shall itemise all transactions contributing to the VAT Return — including invoice number, date, counterparty name, net amount, tax code, and VAT amount — in a supporting schedule exportable to Excel (.xlsx).

**FR-ACCT-089:** The system shall link every VAT posting to its source transaction via `source_module` and `source_document_id` fields, providing an audit trail from each VAT Return line item back to the originating invoice or journal.

**FR-ACCT-090:** The system shall flag any VAT Return period that contains transactions with missing or invalid tax codes using a banner warning identifying the affected transactions by invoice number and date.

## 6.5 EFRIS Integration Flag

**FR-ACCT-091:** The system shall expose an *EFRIS Integration Enabled* configuration toggle per tenant; when enabled, the system shall transmit confirmed sales invoices to the EFRIS endpoint as defined in the Platform Integration Layer (FR-INTG series). *This requirement defers implementation details to the FR-INTG series.*

## 6.6 Withholding Tax

**FR-ACCT-092:** The system shall allow an authorised user to configure withholding tax (WHT) rates per vendor or customer category, specifying the category name, applicable rate (%), and the GL account to which withheld amounts are posted (defaulting to Withholding Tax Payable).

**FR-ACCT-093:** The system shall auto-calculate withholding tax on applicable purchase invoices when a vendor is assigned a WHT category, deducting the withheld amount from the net payable and posting it to the Withholding Tax Payable GL account as part of the auto-generated payment journal.

**FR-ACCT-094:** The system shall generate a Withholding Tax report for a selected period listing all withheld amounts by vendor, WHT category, invoice reference, and posting date, exportable to Excel (.xlsx).

## 6.7 PAYE (Configuration Interface)

**FR-ACCT-095:** The system shall store the Uganda Income Tax Act PAYE band table (income thresholds and marginal rates) as a tenant-level configuration, editable by Super Admin when statutory bands change; PAYE calculation and payroll journal posting are owned by the HR/Payroll module and are out of scope for this section.

**FR-ACCT-096:** The system shall post PAYE liabilities from payroll runs to the PAYE Payable GL account as part of the auto-generated payroll journal per FR-ACCT-030.

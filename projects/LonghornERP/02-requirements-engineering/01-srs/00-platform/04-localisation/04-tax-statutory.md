## 4. Tax, Statutory Deductions, and Fiscal API Configuration

### 4.1 VAT and Tax Rate Configuration

**FR-LOC-050:** The system shall apply the tax rate, tax name, and return format stored in the `vat_rate_default`, `vat_name`, and `vat_return_format` fields of the tenant's active localisation profile, when calculating tax on a taxable transaction.

**FR-LOC-051:** The system shall display the jurisdiction-specific tax name from `vat_name` on all invoices, credit notes, and tax reports, rather than a hard-coded label, when generating tax-bearing documents.

**FR-LOC-052:** The system shall support multiple tax rates per profile by allowing additional rate records in the `tax_rates` table linked to the profile by `profile_id`, with fields for rate name, rate value, and applies-to rules (e.g., exempt, zero-rated, standard), when a profile requires more than one tax rate.

**FR-LOC-053:** The system shall generate tax return export files in the format identified by `vat_return_format` in the tenant's active localisation profile, when an authorised user requests a tax return export for a completed period.

*Example profile values:*

| Parameter | Uganda | Kenya | Tanzania | Rwanda | DRC (Francophone) |
|---|---|---|---|---|---|
| `vat_name` | VAT | VAT | VAT | VAT | TVA |
| `vat_rate_default` | 0.1800 | 0.1600 | 0.1800 | 0.1800 | 0.1800 |
| `vat_return_format` | `URA_VAT_CSV` | `KRA_ETIMS` | `TRA_RETURN` | `RRA_RETURN` | `DRC_TVA` |

*Note:* These are illustrative profile values. All rates must be verified annually against the current published schedules of the respective tax authority.

### 4.2 Statutory Deduction Configuration

**FR-LOC-054:** The system shall calculate Pay As You Earn (PAYE) income tax by applying the tax band array stored in the `paye_config_json` field of the tenant's active localisation profile to the employee's taxable gross salary, when the payroll calculation is run.

The `paye_config_json` structure shall conform to:

```json
[
  {"from": 0, "to": 235000, "rate": 0.00},
  {"from": 235001, "to": 335000, "rate": 0.10},
  {"from": 335001, "to": 410000, "rate": 0.20},
  {"from": 410001, "to": null, "rate": 0.30}
]
```

Where `to: null` denotes an open upper bound. All monetary values in the array are denominated in the profile's base currency.

**FR-LOC-055:** The system shall calculate all employer and employee statutory deductions by applying the rules in the `statutory_deductions_json` field of the tenant's active localisation profile to the employee's gross salary, when the payroll calculation is run.

The `statutory_deductions_json` structure shall conform to:

```json
[
  {
    "name": "NSSF",
    "employee_rate": 0.05,
    "employer_rate": 0.10,
    "employee_cap": null,
    "employer_cap": null,
    "applies_to": "gross_salary"
  }
]
```

**FR-LOC-056:** The system shall calculate Withholding Tax (WHT) at the rate stored in the `wht_rate` field of the tenant's active localisation profile, when a payment is made to a supplier classified as non-VAT-registered and the profile's `wht_rate` is non-null.

*Example profile values — PAYE and statutory deductions:*

*Uganda profile:* PAYE per URA tax bands (current financial year — `[CONTEXT-GAP: GAP-002]`); NSSF at 10% employer + 5% employee; NITA levy 1% of gross salary; WHT 6% on services to non-VAT-registered suppliers.

*Kenya profile:* PAYE per KRA bands; NHIF/SHIF per SHIF 2023 rates; NSSF per NSSF Act 2013 rates; WHT at applicable KRA rates.

*Tanzania profile:* PAYE per TRA bands; PSSSF at 20% employer + 10% employee.

*Rwanda profile:* PAYE per RRA bands; RSSB at 8% employer + 5% employee.

*Note:* Tax band arrays and deduction rates must be verified against current published schedules before each financial year. The profile record is the single update point; no code change is required.

### 4.3 Fiscal Receipt Integration Configuration

**FR-LOC-057:** The system shall route fiscal receipt submissions to the provider identified by the `fiscal_receipt_provider` field of the tenant's active localisation profile, when an invoice is finalised and the profile's `fiscal_receipt_provider` is non-null.

**FR-LOC-058:** The system shall use the endpoint reference and credential key identifiers in `fiscal_receipt_config_json` to resolve the active API endpoint and credentials from the secrets vault, when making a fiscal receipt API call — plaintext credentials shall not be stored in the profile record.

**FR-LOC-059:** The system shall queue the fiscal receipt submission for retry if the fiscal receipt provider API returns an error or is unreachable, and shall mark the invoice with a `fiscal_pending` status visible to the accounts user, when a submission attempt fails.

*Example profile values:*

| Parameter | Uganda | Kenya |
|---|---|---|
| `fiscal_receipt_provider` | `URA_EFRIS` | `KRA_ETIMS` |

`[CONTEXT-GAP: GAP-001]` — URA EFRIS API specification and sandbox credentials are required before the `URA_EFRIS` provider integration can be implemented. Obtain from URA (`efris@ura.go.ug`).

### 4.4 Payroll Statutory API Configuration

**FR-LOC-060:** The system shall route payroll statutory filing submissions to the provider identified by the `payroll_statutory_api_provider` field of the tenant's active localisation profile, when an authorised user initiates a statutory payroll filing export and the profile's `payroll_statutory_api_provider` is non-null.

**FR-LOC-061:** The system shall use the endpoint reference and credential key identifiers in `payroll_statutory_api_config_json` to resolve the active API endpoint and credentials from the secrets vault, when making a payroll statutory API call.

**FR-LOC-062:** The system shall generate the statutory payroll export file in the format required by the configured provider when the super admin triggers a statutory period export for a completed payroll period.

*Example profile values:*

| Parameter | Uganda | Kenya |
|---|---|---|
| `payroll_statutory_api_provider` | `URA_PAYE` | `KRA_ITAX` |

`[CONTEXT-GAP: GAP-002]` — URA PAYE return file format (2024/25) must be confirmed before the `URA_PAYE` provider export can be implemented. Download current template from the URA portal.

`[CONTEXT-GAP: GAP-009]` — KRA iTax API credentials and specification are required before the `KRA_ITAX` provider integration can be implemented. Register on the KRA Developer Portal.

### 4.5 Data Retention Configuration

**FR-LOC-063:** The system shall enforce the minimum data retention period defined in the `data_retention_years` field of the tenant's active localisation profile by preventing deletion of financial records, payroll records, and audit log entries that are younger than the configured retention period, when a deletion request is submitted.

*Example profile values:*

| Profile | `data_retention_years` | Basis |
|---|---|---|
| Uganda Phase 1 | 7 | Uganda Companies Act (minimum 5 years; 7 years recommended). |
| Kenya Phase 2 | 7 | Kenya Companies Act, 2015. |

### 4.6 Withholding Tax Display

**FR-LOC-064:** The system shall display WHT deductions as a separate line on supplier payment documents using the label "Withholding Tax" and the rate from `wht_rate`, when the payment involves a WHT-applicable supplier under the active profile.

**FR-LOC-065:** The system shall generate a WHT certificate document for each WHT deduction applied, containing the supplier name, payment amount, WHT rate, WHT amount, and the tax period, when a WHT-applicable payment is completed and the profile's `wht_rate` is non-null.

**FR-LOC-066:** The system shall produce a WHT summary return export in the format required by the active profile's `vat_return_format` (or a separate `wht_return_format` field if defined), when an authorised user requests a WHT period return.

*Note:* The `wht_return_format` field is provisioned in the parameter catalogue in Section 2.4 under `vat_return_format` as a potential extension. `[CONTEXT-GAP: GAP-002]` applies to the Uganda WHT return format as well.

### 4.7 VAT Multi-Rate Handling

**FR-LOC-067:** The system shall apply exempt or zero-rated tax treatment to a transaction line when the stock item or service is classified under an exempt or zero-rated tax rate record linked to the active profile's `tax_rates`, overriding the standard `vat_rate_default` for that line.

**FR-LOC-068:** The system shall display the applicable tax rate name and rate percentage beside each invoice line when the line's tax classification differs from the profile's default rate.

**FR-LOC-069:** The system shall calculate the total tax amount on a document as the sum of per-line tax amounts, each derived from the line's applicable rate from the `tax_rates` table, when generating a tax invoice or credit note.

**FR-LOC-070:** The system shall include a tax rate breakdown table in the generated tax return export file, grouping transaction lines by rate classification, when producing the VAT return file per **FR-LOC-053**.

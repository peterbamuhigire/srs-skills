## 2. Localisation Profile Management

### 2.1 Overview

A localisation profile is the single configuration record that determines all market-specific behaviour for a tenant. Every requirement in this document operates on the active profile assigned to the requesting tenant. The profile is the variable; the requirement is the constant.

### 2.2 Profile Lifecycle Requirements

**FR-LOC-001:** The system shall maintain a localisation profile record per tenant in the `localisation_profiles` table, containing all market-specific configuration parameters defined in Section 2.4, when the tenant account is active.

**FR-LOC-002:** The system shall apply the tenant's active localisation profile to all financial calculations, display formatting, and statutory integrations when a request is processed for that tenant.

**FR-LOC-003:** The system shall allow a super admin to assign a localisation profile to a tenant at provisioning time by selecting a profile from the list of defined profiles and saving the tenant record.

**FR-LOC-004:** The system shall allow a super admin to update a tenant's active localisation profile by selecting a replacement profile and confirming the change, without requiring a code deployment or application server restart.

**FR-LOC-005:** The system shall support adding a new market by inserting a new localisation profile record in the `localisation_profiles` table, with no code changes required, when a super admin creates the record and maps it to a tenant.

**FR-LOC-006:** The system shall record a profile version entry in the `localisation_profile_versions` table, capturing the previous values, the super admin's user identity, and the UTC timestamp, when a localisation profile is updated.

**FR-LOC-007:** The system shall allow a super admin to view the full version history of any localisation profile, ordered by timestamp descending, when the super admin navigates to the profile's audit trail view.

**FR-LOC-008:** The system shall allow a super admin to restore a previous profile version by selecting a historical version and confirming the rollback, which shall create a new version entry recording the restoration action rather than overwriting existing history.

### 2.3 Profile Inheritance Requirements

**FR-LOC-009:** The system shall support a two-level profile hierarchy — a base profile and a tenant-level override profile — such that tenant-level parameter values override the base profile values for the parameters specified, and all unspecified parameters inherit base profile values.

**FR-LOC-010:** The system shall resolve the effective value for any profile parameter by checking the tenant-level override first; if no tenant-level override exists for that parameter, the system shall use the base profile value, when a tenant profile is evaluated.

**FR-LOC-011:** The system shall allow a super admin to create a base profile that serves as the default for a region or country grouping, when the admin saves the base profile record with `is_base = true`.

*Example:* A "East Africa — English" base profile defines shared defaults (IFRS COA, English language, d M Y date format). Country-level overrides then set currency, VAT rate, and statutory deduction rates for Uganda, Kenya, and Tanzania without duplicating the shared parameters.

### 2.4 Profile Parameter Catalogue

The following parameters shall be supported on every localisation profile record. Parameters marked *required* must have a non-null value on any profile used as an active tenant profile.

| Parameter | Data Type | Required | Description |
|---|---|---|---|
| `profile_name` | VARCHAR(100) | Yes | Human-readable profile identifier (e.g., "Uganda Phase 1"). |
| `iso_currency_code` | CHAR(3) | Yes | ISO 4217 currency code for the tenant's base currency. |
| `currency_symbol` | VARCHAR(10) | Yes | Display symbol (e.g., "UGX", "KSh", "TSh"). |
| `currency_decimal_places` | TINYINT | Yes | Number of decimal places for currency display (0–4). |
| `currency_thousand_separator` | CHAR(1) | Yes | Thousands separator character ("," or "."). |
| `currency_decimal_separator` | CHAR(1) | Yes | Decimal separator character ("." or ","). |
| `language_code` | CHAR(5) | Yes | BCP 47 language tag (e.g., `en-UG`, `fr-CM`, `sw-KE`). |
| `date_format` | VARCHAR(20) | Yes | PHP date format string (e.g., `d M Y`, `d/m/Y`, `Y-m-d`). |
| `number_decimal_separator` | CHAR(1) | Yes | Decimal separator for non-currency numbers. |
| `number_thousand_separator` | CHAR(1) | Yes | Thousands separator for non-currency numbers. |
| `financial_year_start_month` | TINYINT | Yes | Month number (1–12) on which the financial year begins. |
| `vat_rate_default` | DECIMAL(5,4) | Yes | Standard VAT/tax rate as a decimal (e.g., 0.1800 for 18%). |
| `vat_name` | VARCHAR(50) | Yes | Jurisdiction-specific tax name displayed on invoices (e.g., "VAT", "TVA"). |
| `vat_return_format` | VARCHAR(50) | No | Identifier for the return file format (e.g., `URA_VAT_CSV`, `KRA_ETIMS`). |
| `paye_config_json` | JSON | Yes | Tax band array: `[{"from": 0, "to": 235000, "rate": 0.00}, ...]`. |
| `statutory_deductions_json` | JSON | Yes | Array of deduction rules: name, employee rate, employer rate, cap. |
| `fiscal_receipt_provider` | VARCHAR(50) | No | Integration provider identifier (e.g., `URA_EFRIS`, `KRA_ETIMS`). |
| `fiscal_receipt_config_json` | JSON | No | Provider-specific endpoint and credential references (not plaintext secrets). |
| `payroll_statutory_api_provider` | VARCHAR(50) | No | Payroll filing provider (e.g., `URA_PAYE`, `KRA_ITAX`). |
| `payroll_statutory_api_config_json` | JSON | No | Provider-specific configuration (endpoint reference; credential keys resolved from vault). |
| `coa_starter_template` | VARCHAR(100) | Yes | COA template identifier loaded on tenant creation (e.g., `UGANDA_IFRS`, `OHADA_SYSCOHADA_2017`). |
| `invoice_legal_text` | TEXT | No | Mandatory legal footer text displayed on invoices for the jurisdiction. |
| `ppda_workflow_enabled` | BOOLEAN | Yes | Whether PPDA procurement workflow is active for this profile. |
| `address_format_json` | JSON | Yes | Ordered array of address field labels for the jurisdiction. |
| `sms_gateway_provider` | VARCHAR(50) | No | SMS gateway identifier (e.g., `AFRICAS_TALKING`, `ORANGE_MONEY`). |
| `sms_gateway_config_json` | JSON | No | Gateway-specific configuration (shortcode reference; credential keys resolved from vault). |
| `mobile_money_providers_json` | JSON | No | Array of enabled mobile money providers and their configuration references. |
| `wht_rate` | DECIMAL(5,4) | No | Withholding tax rate as a decimal (e.g., 0.0600 for 6%). |
| `data_retention_years` | TINYINT | Yes | Minimum data retention period in years per jurisdiction law. |
| `is_base` | BOOLEAN | Yes | `true` if this record is a base/regional profile; `false` if it is a tenant-level profile. |

**FR-LOC-012:** The system shall validate that all *required* profile parameters contain non-null values before allowing a profile to be assigned to an active tenant, when the super admin attempts the assignment.

**FR-LOC-013:** The system shall reject any profile parameter update that would produce an inconsistent state — such as `currency_decimal_places` set to 0 while `currency_decimal_separator` is non-null — by returning a validation error with the specific conflict identified, when the super admin attempts to save the change.

**FR-LOC-014:** The system shall make the resolved effective localisation profile available to all modules as a read-only object for the duration of the request lifecycle, resolved once per request from the `tenant_id` in the authenticated session.

**FR-LOC-015:** The system shall log every read access to a localisation profile in the audit log, capturing the `tenant_id`, requesting module, and UTC timestamp, when a profile is resolved during request processing.

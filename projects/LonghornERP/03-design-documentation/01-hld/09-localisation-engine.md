# Localisation Engine

## 9.1 Design Principle: One Codebase, All Markets

The Longhorn ERP Localisation Engine is a configuration-driven mechanism that enables the platform to operate correctly in any supported market without modifying source code, database schema, or deployment artefacts. Entering a new country requires only:

1. Creating a localisation profile record for the target jurisdiction.
2. Assigning the profile to a tenant.
3. Verifying that any required external integrations (tax authority APIs, mobile money gateways) are available.

No code branches, no country-specific forks, and no per-country deployment pipelines.

## 9.2 Localisation Profile Structure

Each tenant is assigned exactly 1 localisation profile. The profile is stored as a structured record in the `localisation_profiles` table and linked to the tenant via `tenants.localisation_profile_id`. The profile governs the following dimensions:

| Dimension | Description |
|---|---|
| Currency | ISO 4217 currency code and display format (symbol, decimal separator, thousands separator). |
| Language | ISO 639-1 language code for UI labels and system-generated documents. |
| Date format | Display format string (e.g., `DD/MM/YYYY` for Uganda, `MM/DD/YYYY` for US). |
| Financial year | Start month of the financial year (e.g., July for Uganda government entities, January for calendar-year businesses). |
| VAT configuration | VAT registration threshold, standard VAT rate, exempt categories, VAT return format. |
| Statutory deductions | Ordered list of statutory deduction rules (e.g., PAYE bands, NSSF employer/employee rates for Uganda; NHIF, NSSF for Kenya). Each rule references a formula or rate table resolved at payroll run time. |
| Chart of Accounts starter | The COA template applied when the tenant is provisioned. After provisioning, the tenant may customise their COA. |
| Invoice legal text | Jurisdiction-required text printed on invoices (e.g., tax registration number format, payment terms mandated by regulation). |
| Payment gateways | Ordered list of enabled mobile money and payment gateway codes (e.g., `MTN_MOMO_UG`, `AIRTEL_MONEY_UG`, `MPESA_KE`). |
| Fiscal receipt integration | Whether the tenant is subject to electronic fiscal receipt requirements (e.g., URA EFRIS for Uganda) and the gateway code to use. |
| Address format | Field order and label set for postal addresses (varies by country). |
| Phone format | Country dial code and local number format validation rules. |

## 9.3 How Services Consume the Localisation Profile

Services access the localisation profile exclusively through `TenantContext::getLocalisationProfile()`. The profile object exposes typed accessors — no service reads raw profile fields from the database directly.

The design rule for localisation in functional requirements is: *"The system shall apply [rate/format/rule] from the tenant's active localisation profile."* The profile is the variable; the code is the constant.

Example application in the HR & Payroll module: "The system shall calculate PAYE by applying the income tax band table from the tenant's active localisation profile to the employee's gross taxable pay for the period." The same code path executes for a Uganda tenant (Uganda Income Tax Act bands) and a Kenya tenant (KRA iTax bands) because the band table is in the profile, not in the code.

## 9.4 Uganda Phase 1 Reference Implementation

Uganda is the Phase 1 reference implementation. The Uganda localisation profile is the first fully defined profile and serves as the template and validation baseline for all subsequent profiles.

### Uganda Profile Summary

| Dimension | Uganda Phase 1 Value |
|---|---|
| Currency | `UGX` — Ugandan Shilling |
| Language | `en` — English |
| Date format | `DD/MM/YYYY` |
| Financial year start | July (month 7) |
| VAT standard rate | 18% |
| PAYE bands | Uganda Revenue Authority (URA) graduated scale |
| NSSF contribution | Employer 10%, Employee 5% of gross salary |
| COA starter | Uganda IFRS-aligned COA with URA chart references |
| Invoice legal text | TIN required; VAT registration number if VAT-registered |
| Mobile money gateways | MTN Mobile Money Uganda (`MTN_MOMO_UG`), Airtel Money Uganda (`AIRTEL_MONEY_UG`) |
| Fiscal receipt | URA EFRIS (`URA_EFRIS`) — required for VAT-registered tenants |
| NITA-U compliance | Cloud SaaS provider obligations per NITA-U SaaS Guidelines |

## 9.5 Localisation Profile Versioning

Statutory rates (PAYE bands, NSSF rates, VAT rates) change when governments enact new legislation. The `localisation_profiles` table supports versioned rate tables linked by effective date. When a new financial year begins or new rates are gazetted, Chwezi operators publish a new rate table version. The system applies the rate table version whose effective date is ≤ the transaction date, ensuring that historical payroll runs and financial reports remain accurate without retroactive data corruption.

## 9.6 Adding a New Market

The process for extending Longhorn ERP to a new country is:

1. Create a localisation profile record for the new jurisdiction, populating all dimensions listed in Section 9.2.
2. Define the statutory deduction rules and rate tables for the jurisdiction.
3. Configure the applicable payment gateway integrations (if not already available in the Integration Layer).
4. If a fiscal receipt integration is required, implement the gateway adapter in the Integration Layer service.
5. Assign the profile to a test tenant, run the full functional test suite scoped to the new profile, and verify output documents against the jurisdiction's regulatory requirements.
6. Make the profile available for selection during tenant provisioning in the Super Admin Panel.

No application code is modified, no deployment is required, and existing tenants are unaffected.

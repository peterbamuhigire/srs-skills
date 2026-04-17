# Localisation Engine — Longhorn ERP

## Design Principle

Localisation is configuration-driven, not code-change-driven. One codebase serves all markets. Every market-specific behaviour is defined in a localisation profile stored per tenant. Adding a new country requires no code changes — only a new profile configuration.

## Localisation Profile Parameters

Each tenant's localisation profile configures:

| Parameter | Description |
|---|---|
| Currency | ISO 4217 code and symbol (UGX, KES, TZS, RWF, XOF, XAF, USD, GBP, etc.) |
| Language | UI language (English, French, Swahili) |
| Date Format | Display format (d/m/Y, m/d/Y, Y-m-d) |
| Number Format | Decimal separator, thousands separator |
| Financial Year | Start month (e.g., July for Uganda, January for most Francophone) |
| VAT/Tax Configuration | Tax name, rate(s), return format |
| Statutory Deductions | Employer and employee contribution rates and caps |
| Chart of Accounts Starter | Default COA template on tenant creation |
| Address Format | Field order and labels for physical addresses |
| Invoice Legal Text | Mandatory legal footer text per jurisdiction |
| SMS Gateway | Africa's Talking (East Africa), Orange Money (Francophone), etc. |
| Mobile Money Gateway | MTN MoMo, Airtel Money, M-Pesa, Orange Money, etc. |
| Fiscal Receipt Integration | EFRIS (Uganda), eTIMS (Kenya), TRA (Tanzania), RRA (Rwanda) |
| Payroll Statutory API | URA PAYE, KRA iTax, TRA, RRA, CNSS |

## Requirement Pattern for Localisation

Functional requirements that vary by jurisdiction are written once with a configuration profile reference:

> **FR-PAYROLL-041:** The system shall calculate statutory deductions by applying the deduction rates and thresholds defined in the active localisation profile for the tenant's jurisdiction.
>
> *Uganda profile:* PAYE per URA tax bands (current FY); NSSF at 10% employer + 5% employee; NITA levy 1%.
> *Kenya profile:* PAYE per KRA bands; NHIF per SHIF 2023; NSSF at 12% employer + 6% employee.
> *Tanzania profile:* PAYE per TRA bands; PSSSF at 20% employer + 10% employee.
> *Rwanda profile:* PAYE per RRA bands; RSSB at 8% employer + 5% employee.

## Phase 1 Localisation Profile — Uganda (Reference Implementation)

| Parameter | Value |
|---|---|
| Currency | UGX (Ugandan Shilling) |
| Language | English |
| Date Format | d M Y (e.g., 15 Apr 2026) |
| Financial Year | 1 July – 30 June |
| VAT Rate | 18% (URA standard rate) |
| VAT Return | URA VAT return format (CSV) |
| PAYE | Per URA tax bands (current FY — verify annually, see GAP-002) |
| NSSF | Employer 10%, Employee 5% (see GAP-003 for upload format) |
| NITA Levy | 1% of gross salary |
| Fiscal Receipt | URA EFRIS integration (see GAP-001) |
| SMS Gateway | Africa's Talking (Uganda shortcode) |
| Mobile Money | MTN MoMo Uganda, Airtel Money Uganda |
| COA Starter | Uganda standard COA (based on IFRS) |
| PPDA Workflow | PPDA Act procurement thresholds (verify current — see GAP-006) |
| Withholding Tax | 6% WHT on services to non-VAT registered suppliers |
| Data Retention | 7 years minimum (Uganda Companies Act, minimum 5 years) |

## Phase 2 Localisation Profiles — East Africa

### Kenya

| Parameter | Value |
|---|---|
| Currency | KES |
| VAT | 16% KRA standard rate; eTIMS fiscal receipt |
| PAYE | Per KRA bands |
| NHIF/SHIF | Per SHIF 2023 rates |
| NSSF | Per NSSF Act 2013 rates |
| Mobile Money | M-Pesa Daraja B2C |
| Payroll API | KRA iTax (see GAP-009) |

### Tanzania

| Parameter | Value |
|---|---|
| Currency | TZS |
| VAT | 18% TRA standard rate |
| PAYE | Per TRA bands |
| PSSSF | Employer 20%, Employee 10% |
| Mobile Money | M-Pesa Tanzania, Airtel Money Tanzania |

### Rwanda

| Parameter | Value |
|---|---|
| Currency | RWF |
| VAT | 18% RRA standard rate |
| PAYE | Per RRA bands |
| RSSB | Employer 8%, Employee 5% |
| Mobile Money | MTN MoMo Rwanda |

## Phase 3 Localisation — Francophone Africa

| Parameter | Value |
|---|---|
| Language | French |
| COA | OHADA SYSCOHADA 2017 (see GAP-010) |
| Currencies | XOF (BCEAO zone), XAF (BEAC zone) |
| TVA Rates | DRC 18%, Cameroon 19.25%, Côte d'Ivoire 18%, Senegal 18% |
| CNSS | Per country rates |
| Mobile Money | Orange Money, MTN MoMo (Cameroon, DRC, Rwanda) |
| Date Format | d/m/Y |

## Global Extension

Any country is addable by creating a new localisation profile record in the `localisation_profiles` table and mapping it to the tenant. No code deployment required.

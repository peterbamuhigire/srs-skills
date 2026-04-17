## 3. Currency, Language, Date, Number, and Financial Year Configuration

### 3.1 Currency Configuration

**FR-LOC-020:** The system shall display all monetary values using the `iso_currency_code`, `currency_symbol`, `currency_decimal_places`, `currency_thousand_separator`, and `currency_decimal_separator` fields from the tenant's active localisation profile, when rendering any financial figure.

**FR-LOC-021:** The system shall store all monetary values in the database as `DECIMAL(19,4)` in the tenant's base currency, regardless of the display format defined in the profile, when a financial transaction is persisted.

*Example profile values:*

| Parameter | Uganda (UGX) | Kenya (KES) | Tanzania (TZS) |
|---|---|---|---|
| `iso_currency_code` | UGX | KES | TZS |
| `currency_symbol` | UGX | KSh | TSh |
| `currency_decimal_places` | 0 | 2 | 2 |
| `currency_thousand_separator` | , | , | , |
| `currency_decimal_separator` | . | . | . |

### 3.2 Multi-Currency Support

**FR-LOC-022:** The system shall designate one currency per tenant as the base currency, determined by the `iso_currency_code` in the tenant's active localisation profile, when performing General Ledger postings and statutory reporting.

**FR-LOC-023:** The system shall store exchange rate records per tenant in the `exchange_rates` table, each containing the foreign ISO 4217 currency code, the rate relative to the tenant's base currency, and the effective date, when an exchange rate is entered or imported.

**FR-LOC-024:** The system shall apply the exchange rate record with the latest effective date on or before the transaction date when converting a foreign-currency transaction amount to the base currency.

**FR-LOC-025:** The system shall calculate Foreign Exchange (FX) revaluation entries for open foreign-currency balances at period end by applying the closing exchange rate from the `exchange_rates` table, when the period-end revaluation process is triggered by an authorised user.

### 3.3 Language Configuration

**FR-LOC-026:** The system shall load all user-interface strings from the language file identified by the `language_code` field in the tenant's active localisation profile, when rendering any screen, report, or document for that tenant.

**FR-LOC-027:** The system shall support the following language codes at minimum: `en-UG` (English — Uganda), `en-KE` (English — Kenya), `en-TZ` (English — Tanzania), `fr-CM` (French — Cameroon), `fr-CI` (French — Côte d'Ivoire), `sw-KE` (Swahili — Kenya), when the corresponding language file exists in the `lang/` directory.

**FR-LOC-028:** The system shall fall back to `en-UG` when a requested language file is absent, and shall log a `[CONTEXT-GAP]` warning identifying the missing language code, when the fallback is triggered.

*Note:* French and Swahili language files are a Phase 3 deliverable. Phase 1 requires `en-UG` only.

### 3.4 Date Format Configuration

**FR-LOC-029:** The system shall format all displayed dates using the PHP date format string stored in the `date_format` field of the tenant's active localisation profile, when rendering a date in the user interface, a report, or a document.

**FR-LOC-030:** The system shall store all date values in the database as `DATE` or `DATETIME` in UTC, independent of the display format, when persisting any record with a date field.

*Example profile values:*

| Profile | `date_format` | Display Example |
|---|---|---|
| Uganda Phase 1 | `d M Y` | 15 Apr 2026 |
| Kenya Phase 2 | `d/m/Y` | 15/04/2026 |
| Francophone Phase 3 | `d/m/Y` | 15/04/2026 |
| ISO/API contexts | `Y-m-d` | 2026-04-15 |

### 3.5 Number Format Configuration

**FR-LOC-031:** The system shall format all non-currency numeric values using the `number_decimal_separator` and `number_thousand_separator` fields from the tenant's active localisation profile, when rendering any numeric figure in the user interface or a document.

**FR-LOC-032:** The system shall store all numeric values in the database in standard decimal notation (`DECIMAL` or `FLOAT` types) without formatting characters, when persisting any numeric field.

### 3.6 Financial Year Configuration

**FR-LOC-033:** The system shall determine the start date of the current financial year by using the `financial_year_start_month` field from the tenant's active localisation profile, when generating period-based reports, budget comparisons, or year-end General Ledger entries.

**FR-LOC-034:** The system shall label accounting periods as "Period N — [Month] [Year]" where N is the ordinal position of the month within the financial year as defined by the `financial_year_start_month` of the tenant's profile, when displaying period selectors or report headers.

**FR-LOC-035:** The system shall prevent posting of journal entries to a period that has been closed, and shall display the tenant's current open period boundaries derived from `financial_year_start_month`, when a user attempts to post outside the open period.

*Example profile values:*

| Profile | `financial_year_start_month` | Financial Year Example |
|---|---|---|
| Uganda Phase 1 | 7 | 1 July 2025 – 30 June 2026 |
| Kenya Phase 2 | 1 | 1 January 2026 – 31 December 2026 |
| Francophone Phase 3 | 1 | 1 January 2026 – 31 December 2026 |

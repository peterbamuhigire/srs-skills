# Data Formatting Conventions

These conventions govern how all data is stored in the database and how it is presented to end users. Separating storage format from display format prevents data corruption and ensures consistent rendering across all modules.

## Dates

| Context | Format | Example |
|---|---|---|
| Database storage | `Y-m-d` | `2026-04-05` |
| Display in UI and reports | `d M Y` | `05 Apr 2026` |
| Datetime storage | `Y-m-d H:i:s` | `2026-04-05 14:30:00` |

Developers shall never store dates in display format. Conversion to `d M Y` shall occur in the presentation layer only.

## Numbers and Currency

| Context | Format | Example |
|---|---|---|
| Database storage | No thousand separators, full decimal precision | `1500000.00` |
| Display in UI and reports | With thousand separators, 2 decimal places | `1,500,000.00` |
| Currency display | Symbol + formatted number | `UGX 1,500,000.00` |

The `number_format()` function shall be used exclusively for display. Values read from user input for storage shall have thousand separators stripped before saving.

```php
// Correct — strip separators before storage
$amount = (float) str_replace(',', '', $input['amount']);

// Correct — apply formatting for display
echo 'UGX ' . number_format($amount, 2);
```

## Percentages

Percentages shall be displayed with the `%` symbol and exactly 2 decimal places.

```php
// Correct
echo number_format($rate, 2) . '%'; // Output: 18.00%
```

## Phone Numbers

Phone numbers shall be stored in E.164 format (e.g., `+256784464178`). Display formatting (adding spaces or parentheses) may be applied in the presentation layer but shall never be persisted to the database.

## Booleans

Boolean values shall be stored in MySQL as `TINYINT(1)` with values `0` (false) or `1` (true). `VARCHAR` columns using `'yes'`/`'no'`, `'true'`/`'false'`, or `'Y'`/`'N'` are prohibited for boolean semantics. New columns shall use `TINYINT(1) NOT NULL DEFAULT 0` unless a NULL state is explicitly required by the business rule.

```sql
-- Correct
`is_active` TINYINT(1) NOT NULL DEFAULT 1,

-- INCORRECT — string booleans prohibited
`is_active` VARCHAR(3) NOT NULL DEFAULT 'yes',
```

## Summary Reference Table

| Data Type | Storage Format | Display Format |
|---|---|---|
| Date | `Y-m-d` | `d M Y` |
| Datetime | `Y-m-d H:i:s` | `d M Y H:i` |
| Currency amount | `1500000.00` | `UGX 1,500,000.00` |
| Percentage | `18.00` | `18.00%` |
| Phone | `+256784464178` | As typed (E.164 stored) |
| Boolean | `TINYINT(1)` — `0` or `1` | Contextual label in UI |

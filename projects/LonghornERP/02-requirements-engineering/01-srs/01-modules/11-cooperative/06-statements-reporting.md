# 6. Statements, Reporting, and Price Management Requirements

## 6.1 Overview

This section specifies requirements for generating per-farmer statements, seasonal summaries, society-level reports, and for managing the three-tier price model (floor price, market price, premium) that underpins all payment calculations.

## 6.2 Farmer Statements

**FR-COOP-049** — When a farmer, collection officer, or administrator requests a farmer statement for a specified season, the system shall generate a statement document containing: farmer name and ID, NIN (masked to last 4 characters), society and group, season name, a line-by-line listing of all intake entries (date, commodity, grade, weight, unit price, gross payment, itemised deductions, net payment), and a totals summary row, within 5 seconds of the request.

*Acceptance criterion:* A statement for a farmer with 30 intake entries in a season is generated in ≤ 5 seconds; the totals summary matches the sum of line items (verified independently); NIN displays as "**********ABCDE".

**FR-COOP-050** — When a farmer statement is generated, the system shall render it in PDF format suitable for A4 printing with the cooperative's name, logo, and season header on each page, and allow download from the web interface and share via the mobile application.

*Acceptance criterion:* The PDF renders correctly on A4, contains the cooperative branding, and is downloadable from the web and shareable from the mobile app.

**FR-COOP-051** — When a cooperative manager requests a bulk statement generation for all farmers in a society for a season, the system shall generate all individual statements as a single merged PDF or as a ZIP archive of individual PDFs (configurable), and complete the generation within 60 seconds for up to 500 farmers.

*Acceptance criterion:* Bulk generation for 300 farmers completes within 60 seconds and produces a ZIP containing 300 individual PDF files, each correctly named with the farmer ID.

## 6.3 Seasonal Summaries

**FR-COOP-052** — When an administrator requests a seasonal summary report for a season, the system shall produce a report containing: total weight received (kg) by grade and by society, total gross value, total deductions (by type: loan, society levy, union levy), total net disbursed, number of active farmers, number of payment batches, and the batch reconciliation status.

*Acceptance criterion:* The seasonal summary totals for weight, gross, deductions, and net are consistent with the sum of all individual farmer statements for the same season (cross-check tolerance: UGX 0 — no rounding discrepancy).

**FR-COOP-053** — When an administrator exports the seasonal summary to Excel (`.xlsx`), the system shall produce a file with one row per farmer, all numeric columns formatted as numbers (not text), all date columns formatted as ISO 8601 (`YYYY-MM-DD`), and column headers in row 1.

*Acceptance criterion:* The exported `.xlsx` file opens in Microsoft Excel 365; numeric columns sum correctly using Excel's SUM function; date columns sort correctly in chronological order.

## 6.4 Society Reports

**FR-COOP-054** — When a society manager requests a society performance report for a date range, the system shall display: intake volume (kg) by commodity and grade, farmer count, average weight per farmer, total levies collected (society and union), and a comparison to the same period in the prior year (if prior data exists).

*Acceptance criterion:* Report for "Butebo Primary Cooperative Society" Q1 2025 shows correct totals and, when prior-year data exists, displays the year-on-year delta as a percentage.

**FR-COOP-055** — When a society treasurer requests a levy collection report for a season, the system shall list all levy deductions by levy type, the total collected per levy type, and the remittance status (pending transfer to union / transferred) with the transfer reference where applicable.

*Acceptance criterion:* The levy report shows society levy total = UGX X and union levy total = UGX Y with distinct remittance statuses; totals match the sum of levy lines on all individual payment records.

## 6.5 Price Management

**FR-COOP-056** — When a price administrator sets a market price for a commodity-grade-season combination, the system shall store the market price, record the effective date, and use the market price as the default unit price on new intake entries unless the market price is below the configured floor price, in which case the floor price is applied.

$AppliedPrice = \max(MarketPrice, FloorPrice)$

*Acceptance criterion:* MarketPrice = UGX 380/kg, FloorPrice = UGX 400/kg → applied price = UGX 400 on intake entries. MarketPrice = UGX 470/kg, FloorPrice = UGX 400/kg → applied price = UGX 470.

**FR-COOP-057** — When a price administrator views the price history for a commodity-grade, the system shall display a chronological list of all price changes for all seasons, showing: effective date, price type (floor / market / effective), value (UGX), and the user who set the price.

*Acceptance criterion:* Price history for "Arabica Coffee Grade A" shows all historical price records in descending date order; each row includes the setting user and timestamp.

**FR-COOP-058** — When a price administrator attempts to set a floor price lower than the union's published minimum support price (if configured), the system shall display a warning: "Floor price UGX [value] is below the union's minimum support price of UGX [MSP]. Confirm override?" and require explicit confirmation before saving.

*Acceptance criterion:* MSP = UGX 420/kg; attempting floor price = UGX 410/kg triggers the warning; the price is only saved after the administrator confirms.

[CONTEXT-GAP: Uganda Coffee Development Authority (UCDA) published minimum support price schedule for 2025 — confirm whether this is to be fetched via an external API or entered manually by the administrator.]

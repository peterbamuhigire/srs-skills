# Financial Statement Requirements

## 4.1 Overview

The Financial Statements module generates statutory and management reports from posted GL data. All statements comply with International Financial Reporting Standards (IFRS) and the applicable International Accounting Standards (IAS) cited in Section 1.4. Statements are generated on demand for any closed or open period within the tenant's data range.

## 4.2 Trial Balance

**FR-ACCT-043:** The system shall generate a Trial Balance report when an authorised user selects a reporting period; the report shall list every GL account with a non-zero balance for that period, displaying account code, account name, debit total, and credit total, with a grand total row confirming that total debits equal total credits.

**FR-ACCT-044:** The system shall allow the user to filter the Trial Balance by account type (Asset, Liability, Equity, Revenue, Expense) or to display all types simultaneously.

**FR-ACCT-045:** The system shall flag any Trial Balance where the grand total debit does not equal the grand total credit with a banner error stating "Out-of-balance condition detected. Contact system administrator." and shall log the discrepancy as a system alert.

## 4.3 Income Statement (Profit and Loss)

**FR-ACCT-046:** The system shall generate an Income Statement when an authorised user selects a reporting period; the report shall present the following sections in order: Revenue, Cost of Goods Sold, Gross Profit, Operating Expenses, Earnings Before Interest, Taxes, Depreciation, and Amortisation (EBITDA), Other Income/Expense, and Net Profit.

**FR-ACCT-047:** The system shall calculate Gross Profit as:

$GrossProfit = Revenue - CostOfGoodsSold$

**FR-ACCT-048:** The system shall calculate EBITDA as:

$EBITDA = GrossProfit - OperatingExpenses + Depreciation + Amortisation + Interest$

**FR-ACCT-049:** The system shall calculate Net Profit as:

$NetProfit = EBITDA - Interest - Taxes - Depreciation - Amortisation + OtherIncome - OtherExpense$

**FR-ACCT-050:** The system shall display a comparative Income Statement when the user selects the *Compare* option, showing current period, prior period, and the variance (amount and percentage) for each line item.

## 4.4 Balance Sheet

**FR-ACCT-051:** The system shall generate a Balance Sheet when an authorised user selects a reporting date; the report shall present assets classified as current and non-current per IAS 1, liabilities classified as current and non-current, and equity, and shall verify that:

$TotalAssets = TotalLiabilities + TotalEquity$

**FR-ACCT-052:** The system shall display an error banner and log a system alert when the Balance Sheet equation in FR-ACCT-051 does not hold for the generated report.

**FR-ACCT-053:** The system shall display a comparative Balance Sheet when the user selects the *Compare* option, showing balances for the selected date and the same date in the prior year side by side.

## 4.5 Cash Flow Statement (IAS 7)

**FR-ACCT-054:** The system shall generate a Cash Flow Statement using the indirect method as defined in IAS 7 when an authorised user selects a reporting period; the report shall present three sections: Operating Activities, Investing Activities, and Financing Activities, with a reconciliation to the opening and closing cash balance.

**FR-ACCT-055:** The system shall calculate Net Cash from Operating Activities by starting with Net Profit and adjusting for non-cash items (depreciation, amortisation) and changes in working capital accounts (trade receivables, trade payables, inventory) mapped from the GL account sub-types.

**FR-ACCT-056:** The system shall require that GL accounts are tagged with cash-flow classification (`operating`, `investing`, `financing`, or `non-cash`) at the account level, and shall use these tags as the basis for Cash Flow Statement classification.

## 4.6 Comparative Periods and Budgets

**FR-ACCT-057:** The system shall allow an authorised user to generate any financial statement with a comparative column showing the same period in the prior financial year, where "prior year" is defined by the tenant's configured financial year start month.

**FR-ACCT-058:** The system shall allow an authorised user to generate a Budget vs. Actual report for any period that has an approved budget, displaying actual GL balances, budgeted amounts, and variance (amount and %) per account per period.

## 4.7 Multi-Currency Consolidation

**FR-ACCT-059:** The system shall translate foreign-currency GL account balances to the tenant's functional currency using the platform exchange rate in effect on the statement date when generating consolidated financial statements.

**FR-ACCT-060:** The system shall isolate and present unrealised currency translation gains/losses as a separate line item in the equity section of the Balance Sheet, per IFRS requirements.

## 4.8 Export

**FR-ACCT-061:** The system shall export any generated financial statement to Excel (.xlsx) format when the user selects the *Export to Excel* action, preserving the section headings, line item groupings, and subtotal rows.

**FR-ACCT-062:** The system shall export any generated financial statement to PDF format when the user selects the *Export to PDF* action, applying the tenant's configured report header (logo, company name, registration number) and a page footer showing the page number, report title, and generation timestamp.

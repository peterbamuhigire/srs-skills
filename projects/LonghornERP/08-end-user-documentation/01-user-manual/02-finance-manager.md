# Finance Manager Guide

**Role:** Finance Manager

**Accessible modules:** Accounting, Budgets, Financial Reports, Bank Reconciliation

---

## Creating a Manual Journal Entry

1. In the left sidebar, click **Finance**, then click **Journal Entries**.
2. Click **New Journal Entry**.
3. In the **Date** field, click the date picker and select the transaction date.
4. Enter a brief description in the **Narration** field.
5. In the **Lines** table, click **Add Line** to insert the first row.
6. Select the account from the **Account** dropdown (type to search).
7. Enter the amount in either the **Debit** or **Credit** column.
8. Repeat steps 5–7 for each line. The **Total Debits** and **Total Credits** indicators at the bottom of the table must match before you can save.
9. Attach any supporting document by clicking **Attach File** and selecting the file.
10. Click **Save Draft** to save without posting, or proceed to the next section to post.

---

## Posting and Reversing a Journal

### Posting a Draft Journal

1. Open the draft journal entry you want to post.
2. Review all lines and confirm the narration is correct.
3. Click **Post**. A confirmation dialog appears.
4. Click **Confirm** in the dialog.
5. The journal status changes to **Posted** and the entry updates the general ledger immediately.

### Reversing a Posted Journal

1. Open the posted journal entry you want to reverse.
2. Click **Reverse**.
3. In the dialog, select the **Reversal Date** using the date picker.
4. Click **Confirm Reversal**.
5. The system creates a new journal with opposite debit and credit values. Both journals remain visible in the ledger.

---

## Creating and Posting a Sales Invoice

1. In the sidebar, click **Finance**, then click **Sales Invoices**.
2. Click **New Invoice**.
3. Select the customer from the **Customer** dropdown.
4. Set the **Invoice Date** and **Due Date** using the date pickers.
5. In the **Lines** table, click **Add Line**.
6. Select the account or item, enter quantity and unit price. The line total calculates automatically.
7. Add all invoice lines using step 6.
8. Confirm the **Total** at the bottom matches the expected amount.
9. Click **Save Draft** to hold, or click **Post Invoice** to finalise.
10. Click **Confirm** in the confirmation dialog to post.

---

## Allocating a Customer Payment

1. In the sidebar, click **Finance**, then click **Customer Receipts**.
2. Click **New Receipt**.
3. Select the customer from the **Customer** dropdown.
4. Enter the **Amount Received** and the **Payment Date**.
5. Select the **Bank Account** the payment was deposited into.
6. In the **Allocate to Invoices** table, the system lists all open invoices for that customer.
7. Enter the amount to allocate against each invoice in the **Allocated** column. The running **Unallocated Balance** updates as you type.
8. When the unallocated balance reaches zero (or you have allocated the full payment), click **Post Receipt**.
9. Click **Confirm** to finalise.

---

## Viewing the Trial Balance

1. In the sidebar, click **Finance**, then click **Trial Balance**.
2. Set the **From Date** and **To Date** using the date pickers.
3. Select the **Branch** from the dropdown, or leave it set to **All Branches** for a consolidated view.
4. Click **Generate**.
5. The report loads in a table showing account code, account name, debit total, and credit total.
6. Click **Export to Excel** or **Print** to save a copy.

---

## Running the Balance Sheet Report

1. In the sidebar, click **Finance**, then click **Financial Reports**, then click **Balance Sheet**.
2. Set the **As at Date** to the reporting date.
3. Select the branch or choose **Consolidated**.
4. Click **Generate Report**.
5. The report displays assets, liabilities, and equity grouped by category.
6. Click **Export to PDF** or **Export to Excel** to save the report.

---

## Running the Profit and Loss Report

1. In the sidebar, click **Finance**, then click **Financial Reports**, then click **Profit & Loss**.
2. Set the **From Date** and **To Date**.
3. Select the branch or choose **Consolidated**.
4. Click **Generate Report**.
5. The report shows income accounts, expense accounts, and the net profit or loss for the period.
6. Click **Export to PDF** or **Export to Excel** to save.

---

## Setting Up a Budget by Account

1. In the sidebar, click **Finance**, then click **Budgets**.
2. Click **New Budget**.
3. Enter a name for the budget in the **Budget Name** field (for example, "FY2026 Operating Budget").
4. Select the **Financial Year** from the dropdown.
5. Click **Add Account Line**.
6. Select the account from the **Account** dropdown.
7. Enter a budget amount for each month across the row.
8. Repeat steps 5–7 for each account you want to budget.
9. Click **Save Budget**.

---

## Viewing Budget vs. Actual Variance

1. In the sidebar, click **Finance**, then click **Budgets**, then click **Budget vs. Actual**.
2. Select the **Budget** from the dropdown.
3. Set the reporting **Period** (month or year-to-date).
4. Click **Generate**.
5. The table shows budgeted amounts, actual amounts, and the variance for each account. Negative variances (over budget) are highlighted in red.

---

## Importing a Bank Statement for Reconciliation

1. In the sidebar, click **Finance**, then click **Bank Reconciliation**.
2. Select the **Bank Account** you want to reconcile.
3. Click **Import Statement**.
4. Click **Choose File** and select your bank statement file (CSV or OFX format).
5. Confirm the **Date Format** matches the format in your file.
6. Click **Import**. The system loads the statement lines into the reconciliation screen.

---

## Matching Bank Transactions

After importing a statement, the reconciliation screen shows two panels: **Bank Statement Lines** on the left and **System Transactions** on the right.

1. Click a bank statement line on the left to select it.
2. The system automatically suggests matching system transactions on the right, highlighted in green.
3. If the suggestion is correct, click **Match** to confirm the pair.
4. If no suggestion appears, search for the system transaction manually using the search box above the right panel.
5. Select the correct system transaction and click **Match**.
6. Repeat until all bank lines are matched.
7. The **Unreconciled Balance** at the top updates after each match. When it reaches zero, all lines are reconciled.
8. Click **Save Reconciliation** to record the completed reconciliation.

---

## Closing an Accounting Period

*Closing a period is irreversible. Confirm all journals are posted and the trial balance is balanced before proceeding.*

1. In the sidebar, click **Finance**, then click **Period Management**.
2. Locate the period you want to close in the list.
3. Click **Close Period** next to that period.
4. A confirmation dialog lists any unposted journals still open in that period. Review the list.
5. If there are unposted journals, click **Cancel**, post or delete those journals, then return to this step.
6. When the list is clear, click **Confirm Close**.
7. The period status changes to **Closed**. No further entries can be posted to a closed period.

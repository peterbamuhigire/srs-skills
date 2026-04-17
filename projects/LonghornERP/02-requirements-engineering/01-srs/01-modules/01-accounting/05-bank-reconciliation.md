# Bank Reconciliation Requirements

## 5.1 Overview

Bank reconciliation is the process of matching GL cash/bank account entries against an external bank statement to confirm that both records agree. This module supports multi-currency bank accounts, statement import in standard formats, automated matching, and a reconciliation report that surfaces outstanding items on either side.

## 5.2 Bank Account Configuration

**FR-ACCT-063:** The system shall allow an authorised user to create a bank account record by providing the following mandatory fields: account name, bank account number, bank name, branch name (optional), currency, and opening balance with opening balance date.

**FR-ACCT-064:** The system shall link each bank account record to exactly 1 GL account from the tenant's Chart of Accounts; the linked GL account must have account type Asset and sub-type Bank or Cash.

**FR-ACCT-065:** The system shall allow an authorised user to deactivate a bank account when its linked GL account carries a zero balance; a deactivated bank account shall be excluded from transaction entry drop-downs and statement import screens.

## 5.3 Bank Statement Import

**FR-ACCT-066:** The system shall accept bank statement uploads in Comma-Separated Values (CSV) and Open Financial Exchange (OFX) formats when an authorised user initiates a statement import for a selected bank account.

**FR-ACCT-067:** The system shall parse imported statement records and create unmatched bank statement lines in the reconciliation workspace, capturing date, description, debit amount, credit amount, and bank-supplied reference for each line.

**FR-ACCT-068:** The system shall reject an import file and return a validation error specifying the line number and field name when the file contains rows where the date format is unrecognised or the debit/credit fields contain non-numeric values.

**FR-ACCT-069:** The system shall prevent duplicate import of the same bank statement file; duplicate detection shall compare file hash (SHA-256) per bank account, and shall display a warning if a matching hash has been imported previously.

## 5.4 Automated Matching

**FR-ACCT-070:** The system shall attempt automated matching of each imported bank statement line against unreconciled GL journal lines on the same bank account, using the following criteria: amount match (exact) AND date proximity within ±3 calendar days AND reference text match (case-insensitive substring).

**FR-ACCT-071:** The system shall mark a matched pair as *Auto-Matched* and display it in a separate section of the reconciliation workspace, allowing the user to review and confirm or reject each auto-matched pair.

**FR-ACCT-072:** The system shall leave unmatched bank statement lines and unmatched GL lines in the *Unreconciled* section of the reconciliation workspace pending manual review.

## 5.5 Manual Matching and Unmatching

**FR-ACCT-073:** The system shall allow an authorised user to manually match an unreconciled bank statement line with 1 or more unreconciled GL lines when the user selects the lines and confirms the match, provided the sum of selected GL line amounts equals the bank statement line amount.

**FR-ACCT-074:** The system shall allow an authorised user to unmatch any matched pair (auto-matched or manually matched) when the reconciliation has not been locked, returning both lines to the *Unreconciled* section.

## 5.6 Reconciliation Report and Lock

**FR-ACCT-075:** The system shall generate a Reconciliation Report when an authorised user selects the *View Report* action, presenting: opening GL balance, total cleared receipts, total cleared payments, closing GL balance, bank statement closing balance, and unreconciled difference.

**FR-ACCT-076:** The system shall list all outstanding items (unreconciled transactions) on the Reconciliation Report in two sections: *Outstanding in GL* (GL lines with no matching bank line) and *Outstanding in Bank* (bank lines with no matching GL line), each with date, description, and amount.

**FR-ACCT-077:** The system shall allow an authorised user with the Finance Manager role to lock a completed reconciliation, preventing any further matching or unmatching actions; the locked state and locking user shall be recorded in the audit log.

**FR-ACCT-078:** The system shall allow export of the Reconciliation Report to PDF and Excel (.xlsx) formats using the same export mechanism defined in FR-ACCT-061 and FR-ACCT-062.

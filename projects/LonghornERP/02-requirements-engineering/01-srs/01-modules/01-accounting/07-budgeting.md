# Budgeting Requirements

## 7.1 Overview

The Budgeting module enables tenants to define financial targets at the GL account level, import budget data from Excel, track actuals against budget in real time, and manage budget approval workflows. Multiple budget versions per period are supported to accommodate revised forecasts without overwriting the original approved budget.

## 7.2 Budget Period Configuration

**FR-ACCT-097:** The system shall allow an authorised user to create a budget for a specified period by selecting a period type (annual, quarterly, or monthly) and a financial year aligned to the tenant's configured financial year start month.

**FR-ACCT-098:** The system shall allow an authorised user to define budget lines by specifying a GL account, a period (month or quarter within the budget year), and a budgeted amount; each GL account may have at most 1 budget line per period per budget version.

## 7.3 Budget Import

**FR-ACCT-099:** The system shall provide a downloadable Excel (.xlsx) budget import template containing columns: Account Code, Account Name, and 1 column per period (month or quarter) in the selected budget year.

**FR-ACCT-100:** The system shall import budget lines from a completed Excel template when an authorised user uploads the file, mapping each row to the corresponding GL account by account code, and shall report the count of successfully imported lines and any rejected rows with the reason for rejection (e.g., account code not found, non-numeric amount).

## 7.4 Budget Versions

**FR-ACCT-101:** The system shall support multiple budget versions per period (e.g., Original, Revised Q1, Revised Q2), identified by a user-supplied version label; each version is independent and can be in a different workflow status.

**FR-ACCT-102:** The system shall allow an authorised user to copy an existing budget version as the starting point for a new version, pre-populating all budget lines from the source version.

## 7.5 Budget Approval Workflow

**FR-ACCT-103:** The system shall enforce a 5-state budget approval workflow: *Draft* → *Submitted* → *Approved* → *Locked*, with an optional *Rejected* terminal state; status transitions shall be permitted only to authorised roles as defined in the platform RBAC configuration.

**FR-ACCT-104:** The system shall prevent editing of any budget line once the budget version reaches *Approved* status; lines shall become read-only and the edit controls shall be hidden.

**FR-ACCT-105:** The system shall lock all budget lines in a *Locked* budget version against any modification, including by Super Admin; unlocking requires creation of a new version per FR-ACCT-101.

## 7.6 Variance Reporting

**FR-ACCT-106:** The system shall generate a Budget vs. Actual Variance Report for a selected budget version and period when an authorised user requests it; the report shall display per GL account: budgeted amount, actual GL balance, variance amount, and variance percentage, calculated as:

$VariancePercent = \frac{Actual - Budget}{Budget} \times 100$

**FR-ACCT-107:** The system shall allow the user to filter the Variance Report by account type, department (if cost-centre tagging is configured), or period range, and shall export the report to Excel (.xlsx) and PDF formats.

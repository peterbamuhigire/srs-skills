# Depreciation — Monthly Run, Methods, GL Posting, and Period Lock

## 3.1 Overview

The Depreciation sub-module computes periodic depreciation charges for all active assets, posts the resulting double-entry journals to the General Ledger, and enforces period-lock rules that prevent retroactive alteration. Depreciation method and rate are set per asset class and may be overridden at the individual asset level.

## 3.2 Depreciation Methods

### 3.2.1 Straight-Line Method

Annual depreciation under the straight-line method is:

$$Dep = \frac{Cost - ResidualValue}{UsefulLife}$$

where *Cost* is the acquisition cost (or revalued amount after revaluation), *ResidualValue* is the estimated residual value, and *UsefulLife* is expressed in years. The monthly charge is $Dep \div 12$.

### 3.2.2 Reducing Balance Method

Depreciation for period *n* under the reducing balance method is:

$$Dep_n = NBV_{n-1} \times Rate$$

where $NBV_{n-1}$ is the Net Book Value at the end of the preceding period and *Rate* is the annual depreciation rate expressed as a decimal. The monthly charge is $Dep_n \div 12$.

**FR-ASSET-013:** When the depreciation method assigned to an asset is *Straight-Line*, the system shall compute the monthly depreciation charge as $\frac{Cost - ResidualValue}{UsefulLife \times 12}$, rounded to 2 decimal places using half-up rounding, and store the computed amount against the depreciation run record.

**FR-ASSET-014:** When the depreciation method assigned to an asset is *Reducing Balance*, the system shall compute the monthly depreciation charge as $\frac{NBV_{n-1} \times Rate}{12}$, where $NBV_{n-1}$ is the NBV after all depreciation posted through the last completed period, rounded to 2 decimal places using half-up rounding.

**FR-ASSET-015:** When the computed depreciation charge for any period would reduce an asset's NBV below its configured residual value, the system shall cap the charge so that the resulting NBV equals exactly the residual value and shall not post any further depreciation for that asset until a new residual value or useful life is configured.

## 3.3 Monthly Depreciation Run

**FR-ASSET-016:** When an authorised user initiates the monthly depreciation run for a selected accounting period, the system shall compute depreciation for every active asset whose depreciation method is enabled, create a single consolidated depreciation journal for that period containing one journal line pair per asset, and post it to the GL — all within a single atomic database transaction; if any line fails validation, the entire run shall be rolled back and an error report returned.

**FR-ASSET-017:** When the depreciation run completes successfully, the system shall set the run status to *Posted*, record the run timestamp, the initiating user identity, and the total number of assets processed, and display a summary screen showing total depreciation charged, asset count, and the journal reference number.

**FR-ASSET-018:** When an authorised user requests a depreciation run for a period that already has a posted depreciation run, the system shall reject the request with HTTP 422 and the message "Depreciation run for [Period] is already posted; reverse the run before re-running."

**FR-ASSET-019:** When an asset is acquired part-way through a period, the system shall pro-rate the first-period depreciation charge by the number of days remaining in the period divided by the total days in the period.

## 3.4 General Ledger Posting for Depreciation

**FR-ASSET-020:** When a depreciation journal is posted, the system shall generate a double-entry GL journal with the following structure for each asset line:

- Debit: Depreciation Expense account mapped to the asset's category, amount = computed monthly depreciation charge.
- Credit: Accumulated Depreciation account mapped to the asset's category, amount = computed monthly depreciation charge.

The journal description shall include the asset number, asset description, period label (e.g., "March 2026"), and depreciation method applied.

**FR-ASSET-021:** When the GL posting for a depreciation journal fails (e.g., GL period is hard-closed or the mapped account is inactive), the system shall abort the entire depreciation run, roll back all database changes within the transaction, and return an error report identifying the specific asset and GL account that caused the failure.

**FR-ASSET-022:** When a posted depreciation journal is viewed in the GL module, the system shall display the source module as "Asset Management" and the source document identifier as the depreciation run reference number, enabling drill-through from the GL journal back to the depreciation run screen.

## 3.5 Depreciation Period Lock

**FR-ASSET-023:** When a depreciation run for a period has been posted and the corresponding GL accounting period has been set to *Hard Closed*, the system shall prevent any reversal or modification of that depreciation run; any attempt shall return HTTP 422 with the message "Depreciation run cannot be reversed: accounting period is Hard Closed."

**FR-ASSET-024:** When an authorised user with the `assets.reverse_depreciation` permission reverses a depreciation run for a period that is *Soft Closed* or *Open*, the system shall generate an equal and opposite reversal journal dated the first day of the current open period, link the reversal journal to the original via a `reversal_of` foreign key, update the NBV of each affected asset to its pre-run value, and write an audit log entry recording the reversal reason, user identity, and timestamp.

# Asset Transfers and Maintenance — Inter-Branch Transfer, Custodian Change, Work Orders, and History

## 5.1 Overview

Asset transfers record the movement of an asset between branches or the reassignment of custodial responsibility. Maintenance covers planned preventive maintenance scheduling, work order generation, and the maintenance history log that supports future service decisions.

## 5.2 Inter-Branch Asset Transfer

**FR-ASSET-036:** When an authorised user initiates an inter-branch asset transfer, the system shall require: asset identifier, transfer date, source branch, destination branch, transfer reason (free text, ≥ 5 characters), and authorising user signature (approval action in the workflow).

**FR-ASSET-037:** When an inter-branch transfer is approved, the system shall post a GL journal within a single atomic transaction debiting the Asset Cost account of the destination branch and crediting the Asset Cost account of the source branch, for the NBV at the transfer date; accumulated depreciation shall be similarly transferred between the respective accumulated depreciation accounts of each branch.

**FR-ASSET-038:** When an inter-branch transfer GL posting fails (e.g., the destination branch GL period is hard-closed), the system shall roll back the entire transfer transaction, retain the asset record at the source branch, and return an error report identifying the failing GL account and period.

**FR-ASSET-039:** When an inter-branch transfer is completed, the system shall update the asset master record's branch and location fields to the destination branch, record a transfer history entry with source branch, destination branch, transfer date, approving user, and reason, and display the transfer history on the asset detail screen in reverse-chronological order.

## 5.3 Custodian Change

**FR-ASSET-040:** When an authorised user reassigns an asset's custodian, the system shall record the previous custodian identity, the new custodian identity, the effective date, and the initiating user identity in the custodian change audit log without generating a GL journal entry.

**FR-ASSET-041:** When an authorised user views an asset's custodian history, the system shall display the complete chronological list of custodian assignments — including custodian name, effective start date, effective end date (or "Current"), and the user who made the change — with no upper limit on historical entries displayed.

## 5.4 Planned Maintenance Calendar

**FR-ASSET-042:** When an authorised user configures a maintenance schedule for an asset, the system shall record: asset identifier, maintenance type (Preventive, Inspection, Service, or Overhaul), recurrence interval (Daily, Weekly, Monthly, Quarterly, Annual, or custom-day interval), next due date, estimated duration (hours), assigned technician or contractor, and estimated cost.

**FR-ASSET-043:** When the scheduled next due date for a maintenance task is reached or is within 7 calendar days, the system shall automatically generate a work order record with status *Pending*, populate it with the maintenance type, assigned technician, asset details, and due date, and send an in-app notification to the assigned technician and the Asset Manager role.

**FR-ASSET-044:** When an authorised user updates a maintenance schedule's recurrence interval, the system shall recompute all future pending work orders from the effective change date; work orders already in status *In Progress* or *Completed* shall not be altered.

## 5.5 Work Order Management

**FR-ASSET-045:** When a work order is created, it shall progress through the following states in sequence: *Pending* → *In Progress* → *Completed*; transition to *Completed* shall require: actual completion date, labour hours recorded, materials used (free text or itemised list), actual cost incurred, and technician sign-off (approval action).

**FR-ASSET-046:** When a work order is completed and the actual cost is entered, the system shall prompt the user to optionally post the maintenance cost to the GL (debit Maintenance Expense account, credit Accounts Payable or Cash as selected); the GL posting is optional at work order completion but is mandatory before the accounting period for that date is hard-closed.

**FR-ASSET-047:** When an authorised user views the maintenance history for an asset, the system shall display all completed work orders in reverse-chronological order, showing work order reference, maintenance type, completion date, technician, actual cost, and a link to the associated GL journal (if posted), with no upper limit on the number of history entries displayed.

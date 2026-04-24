# Traceability Matrix — Asset Management Module

## 9.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6, and records the IEEE 830 verifiability criterion (the deterministic test oracle) for each requirement. All FRs without a mapping to a business goal are flagged `[TRACE-GAP]`.

## 9.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-ASSET-001 | Complete, auditable accountability for every fixed asset across its full lifecycle |
| BG-ASSET-002 | IAS 16 and IAS 12 compliance in all asset accounting computations and disclosures |
| BG-ASSET-003 | URA tax depreciation compliance and accurate deferred tax liability reporting |
| BG-ASSET-004 | Reduce asset loss through physical verification, QR tagging, and custodian assignment |
| BG-ASSET-005 | Improve vehicle fleet utilisation and maintenance reliability |
| BG-ASSET-006 | Improve maintenance planning discipline, schedule compliance, and uptime for critical assets |
| BG-ASSET-007 | Improve reliability and repair-versus-replace decisions using structured evidence |

## 9.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | Test Oracle |
|---|---|---|---|---|
| FR-ASSET-001 | 2.2 | Create asset master record with mandatory fields | BG-ASSET-001 | Submit valid form; verify HTTP 201 and asset number in format `ASSET-{YYYY}-{NNNNNN}`. |
| FR-ASSET-002 | 2.2 | Reject asset creation with missing mandatory fields | BG-ASSET-001 | Submit form with blank Useful Life; verify HTTP 422 and field-level error within 500 ms. |
| FR-ASSET-003 | 2.2 | Audit log on asset master edit | BG-ASSET-001 | Edit asset description; verify audit log entry with old value, new value, user, and timestamp. |
| FR-ASSET-004 | 2.2 | Lock acquisition cost and date after depreciation is posted | BG-ASSET-002 | Attempt to change cost on an asset with 1 posted depreciation run; verify HTTP 422. |
| FR-ASSET-005 | 2.2 | Restrict status change to Disposal workflow only | BG-ASSET-001 | Attempt direct status override via API; verify HTTP 422. |
| FR-ASSET-006 | 2.3 | Create asset category with depreciation defaults and GL mappings | BG-ASSET-001, BG-ASSET-002 | Create category; verify depreciation method, rate, useful life, and GL accounts stored. |
| FR-ASSET-007 | 2.3 | Pre-populate asset depreciation fields from category defaults | BG-ASSET-002 | Create asset under category; verify depreciation method and rate pre-filled on the form. |
| FR-ASSET-008 | 2.3 | Apply category default rate changes prospectively only | BG-ASSET-002 | Update category rate; verify existing asset schedule unchanged; new asset uses new rate. |
| FR-ASSET-009 | 2.3 | Block deletion of category with active assets | BG-ASSET-001 | Attempt category deletion with 1 active asset; verify HTTP 422. |
| FR-ASSET-010 | 2.4 | Auto-generate QR code on asset record creation | BG-ASSET-004 | Create asset; verify QR data string is stored and encodes the asset number. |
| FR-ASSET-011 | 2.4 | Generate printable QR label PDF batch | BG-ASSET-004 | Request label sheet for 200 assets; verify PDF returned within 10 seconds with correct fields. |
| FR-ASSET-012 | 2.4 | Mobile QR scan retrieves asset master record | BG-ASSET-004 | Scan QR tag via mobile app; verify asset detail screen loads within 3 seconds. |
| FR-ASSET-013 | 3.2 | Compute straight-line monthly depreciation | BG-ASSET-002 | Asset: cost 12,000,000, residual 0, 5 years; verify monthly charge = 200,000. |
| FR-ASSET-014 | 3.2 | Compute reducing balance monthly depreciation | BG-ASSET-002 | Asset: NBV 10,000,000, rate 25%; verify monthly charge = 208,333.33 (half-up). |
| FR-ASSET-015 | 3.2 | Cap depreciation charge at residual value ceiling | BG-ASSET-002 | Run depreciation on asset where remaining depreciable amount < computed charge; verify capped charge and no further depreciation thereafter. |
| FR-ASSET-016 | 3.3 | Monthly depreciation run — atomic GL posting | BG-ASSET-001, BG-ASSET-002 | Initiate run; verify single journal posted with one line pair per asset; verify rollback on injected failure. |
| FR-ASSET-017 | 3.3 | Depreciation run summary screen | BG-ASSET-001 | Complete run; verify status *Posted*, journal reference, asset count, and total charge displayed. |
| FR-ASSET-018 | 3.3 | Reject duplicate depreciation run for same period | BG-ASSET-001 | Attempt second run for same period; verify HTTP 422. |
| FR-ASSET-019 | 3.3 | Pro-rate first-period depreciation on mid-period acquisition | BG-ASSET-002 | Asset acquired on 15th of 30-day period; verify first charge = full monthly × 15/30. |
| FR-ASSET-020 | 3.4 | GL journal structure for depreciation | BG-ASSET-002 | Post run; verify Debit: Depreciation Expense and Credit: Accumulated Depreciation for each asset line. |
| FR-ASSET-021 | 3.4 | Abort depreciation run on GL posting failure | BG-ASSET-001 | Deactivate mapped GL account; attempt run; verify full rollback and error report identifying failing account. |
| FR-ASSET-022 | 3.4 | Depreciation journal tagged with source module and run reference | BG-ASSET-001 | View depreciation journal in GL; verify source_module = "Asset Management" and source_document_id populated. |
| FR-ASSET-023 | 3.5 | Block reversal of depreciation run in Hard Closed period | BG-ASSET-001, BG-ASSET-002 | Hard-close period; attempt run reversal; verify HTTP 422. |
| FR-ASSET-024 | 3.5 | Reverse depreciation run in Open or Soft Closed period | BG-ASSET-001 | Reverse run as user with `assets.reverse_depreciation`; verify reversal journal and NBV restored. |
| FR-ASSET-025 | 4.2 | Post upward revaluation with Revaluation Reserve credit | BG-ASSET-002 | Revalue asset upward by 2,000,000; verify Credit: Revaluation Reserve and updated NBV. |
| FR-ASSET-026 | 4.2 | Reverse prior P&L loss before crediting Revaluation Reserve | BG-ASSET-002 | Asset with prior P&L loss of 500,000; revalue up by 800,000; verify 500,000 to P&L, 300,000 to Revaluation Reserve. |
| FR-ASSET-027 | 4.2 | Post downward revaluation to Profit and Loss | BG-ASSET-002 | Revalue asset downward by 1,500,000 with no prior reserve; verify Debit: Impairment Loss on P&L. |
| FR-ASSET-028 | 4.2 | Use Revaluation Reserve before debiting P&L on downward revaluation | BG-ASSET-002 | Asset with reserve 400,000; revalue down by 700,000; verify 400,000 from reserve, 300,000 to P&L. |
| FR-ASSET-029 | 4.2 | Require revaluation basis note | BG-ASSET-001 | Submit revaluation without basis note; verify HTTP 422. |
| FR-ASSET-030 | 4.3 | Disposal by sale — mandatory fields | BG-ASSET-001 | Submit disposal without proceeds amount; verify HTTP 422. |
| FR-ASSET-031 | 4.3 | Write-off disposal — mandatory fields | BG-ASSET-001 | Submit write-off without reason; verify HTTP 422. |
| FR-ASSET-032 | 4.3 | GL journal structure for disposal | BG-ASSET-001, BG-ASSET-002 | Dispose asset with NBV 5,000,000, proceeds 6,000,000; verify Gain = 1,000,000 credited to Disposal Gain account. |
| FR-ASSET-033 | 4.3 | Set asset status to Disposed after disposal | BG-ASSET-001 | Complete disposal; verify asset status = *Disposed* and excluded from next depreciation run. |
| FR-ASSET-034 | 4.3 | Transfer Revaluation Reserve to Retained Earnings on disposal | BG-ASSET-002 | Dispose asset with reserve balance 500,000; verify 500,000 transferred to Retained Earnings in same journal. |
| FR-ASSET-035 | 4.3 | Reverse disposal with approval | BG-ASSET-001 | Reverse disposal with reason and approver; verify reversal journal, asset status restored to *Active*, audit log entry. |
| FR-ASSET-036 | 5.2 | Initiate inter-branch transfer with mandatory fields | BG-ASSET-001 | Submit transfer without reason; verify HTTP 422. |
| FR-ASSET-037 | 5.2 | GL journal for inter-branch transfer | BG-ASSET-001, BG-ASSET-002 | Approve transfer; verify Debit: Asset Cost (destination branch) and Credit: Asset Cost (source branch) in GL. |
| FR-ASSET-038 | 5.2 | Rollback transfer on GL posting failure | BG-ASSET-001 | Hard-close destination period; attempt transfer; verify full rollback and asset remains at source. |
| FR-ASSET-039 | 5.2 | Update asset master and log transfer history | BG-ASSET-001 | Complete transfer; verify asset branch updated and transfer history entry created. |
| FR-ASSET-040 | 5.3 | Custodian change audit log (no GL entry) | BG-ASSET-001 | Reassign custodian; verify audit log entry with old and new custodian, date, and user; verify no GL journal. |
| FR-ASSET-041 | 5.3 | Display full custodian change history | BG-ASSET-001 | Navigate to custodian history tab; verify all previous custodian assignments displayed chronologically. |
| FR-ASSET-042 | 5.4 | Configure maintenance schedule | BG-ASSET-005 | Create monthly preventive schedule; verify recurrence, due date, and assigned technician stored. |
| FR-ASSET-043 | 5.4 | Auto-generate work order and notify when due date reached | BG-ASSET-005 | Set due date to today; verify work order created with status *Pending* and notification sent. |
| FR-ASSET-044 | 5.4 | Recompute future work orders on schedule change | BG-ASSET-005 | Change interval from Monthly to Quarterly; verify future pending work orders updated; completed work orders unchanged. |
| FR-ASSET-045 | 5.5 | Work order state machine and completion fields | BG-ASSET-005 | Transition work order to *Completed* without actual cost; verify HTTP 422. |
| FR-ASSET-046 | 5.5 | Optional GL posting for work order cost | BG-ASSET-001 | Complete work order with cost 250,000; elect to post to GL; verify Debit: Maintenance Expense, Credit: AP. |
| FR-ASSET-047 | 5.5 | Maintenance history list on asset detail | BG-ASSET-001, BG-ASSET-005 | View asset with 5 completed work orders; verify all 5 displayed in reverse-chronological order with GL link. |
| FR-ASSET-048 | 6.2 | Create insurance policy record | BG-ASSET-004 | Create insurance record; verify all required fields stored and policy document attached. |
| FR-ASSET-049 | 6.2 | Compute days-to-expiry and flag Expiring Soon at ≤ 30 days | BG-ASSET-004 | Set expiry to 25 days from today; run daily job; verify status = *Expiring Soon*. |
| FR-ASSET-050 | 6.2 | Notify Asset Manager on Expiring Soon status | BG-ASSET-004 | Policy expires in 20 days; verify in-app and email notification sent to Asset Manager within 24 hours. |
| FR-ASSET-051 | 6.2 | Set policy to Expired and flag asset after expiry | BG-ASSET-004 | Set expiry to yesterday; run daily job; verify policy status = *Expired* and asset shows *Insurance Expired* flag. |
| FR-ASSET-052 | 6.2 | Renew insurance policy and clear Expired flag | BG-ASSET-004 | Record renewal with new policy dates; verify prior policy = *Superseded* and asset flag cleared. |
| FR-ASSET-053 | 6.2 | Insurance Expiry Report with ≤ 90-day filter | BG-ASSET-004 | Generate report; verify only policies expiring within 90 days listed, sorted ascending by days-to-expiry. |
| FR-ASSET-054 | 6.3 | Create physical verification session | BG-ASSET-004 | Create session with scope *By Location*; verify session reference, start timestamp, and status = *In Progress*. |
| FR-ASSET-055 | 6.3 | Record asset scan during verification session | BG-ASSET-004 | Scan asset QR; verify scan timestamp, location, and user recorded; asset marked *Verified* in session. |
| FR-ASSET-056 | 6.3 | Flag Location Mismatch when scanned location differs from register | BG-ASSET-004 | Scan asset at different location; verify *Location Mismatch* flag and warning shown with registered vs. scanned location. |
| FR-ASSET-057 | 6.3 | Generate Physical Verification Discrepancy Report on session close | BG-ASSET-004 | Close session with 3 verified, 1 missing, 1 mismatch; verify report shows correct counts and percentages; verify PDF and Excel export. |
| FR-ASSET-058 | 7.2 | URA tax depreciation rate field on asset category | BG-ASSET-003 | Create category with Uganda jurisdiction; verify URA rate field is mandatory and stored. |
| FR-ASSET-059 | 7.2 | Compute and store both book and tax depreciation per run | BG-ASSET-003 | Run depreciation; verify both book and tax amounts stored on each run line record. |
| FR-ASSET-060 | 7.2 | Post deferred tax GL journal on depreciation run | BG-ASSET-003 | Run with DTL increase of 540,000; verify GL journal posts Debit: Income Tax Expense, Credit: DTL account for 540,000. |
| FR-ASSET-061 | 7.2 | Book vs. Tax Depreciation Report | BG-ASSET-003 | Generate report for 10 assets; verify all 12 columns present and DTL values match manual computation. |
| FR-ASSET-062 | 7.2 | Apply URA rate changes prospectively | BG-ASSET-003 | Update URA rate; verify historical tax records unchanged; next run uses new rate. |
| FR-ASSET-063 | 7.3 | Fleet data fields on Vehicle Fleet category assets | BG-ASSET-005 | Create asset under Vehicle Fleet category; verify registration, fuel type, and driver fields present and saved. |
| FR-ASSET-064 | 7.3 | Record mileage log entry and update cumulative mileage | BG-ASSET-005 | Log trip start 50,000 km, end 50,250 km; verify trip distance = 250 km and cumulative mileage updated. |
| FR-ASSET-065 | 7.3 | Record fuel log and compute fuel efficiency | BG-ASSET-005 | Log refuel; verify L/100 km computed from odometer delta since prior refuel entry. |
| FR-ASSET-066 | 7.3 | Record vehicle service record linked to maintenance history | BG-ASSET-005 | Record service; verify service record appears in asset maintenance history log. |
| FR-ASSET-067 | 7.3 | Trigger work order and notification near service threshold | BG-ASSET-005 | Set service interval at 5,000 km; current odometer 4,600 km (400 km to threshold); verify work order and notification triggered. |
| FR-ASSET-068 | 7.3 | Fleet Utilisation Report | BG-ASSET-005 | Generate report for 3 vehicles over 90 days; verify km, fuel, cost, and efficiency columns; verify Excel and PDF export. |
| FR-ASSET-069 | 5A | Define functional locations and hierarchy | BG-ASSET-001, BG-ASSET-006 | Create multi-level location tree and assign asset; verify hierarchy persisted and asset resolves to 1 active functional location. |
| FR-ASSET-070 | 5A | Asset criticality classification drives priority rules | BG-ASSET-006, BG-ASSET-007 | Set asset to *Critical*; submit breakdown request; verify recommended priority and response window reflect criticality rule. |
| FR-ASSET-071 | 5A | Work-request intake with duplicate screening | BG-ASSET-006 | Submit 2 similar requests for same asset; verify second request is flagged as possible duplicate. |
| FR-ASSET-072 | 5A | Screen request to reject, merge, or convert | BG-ASSET-006 | Screen request and convert to work order; verify request status updated and work-order link stored. |
| FR-ASSET-073 | 5A | Planning package on work order | BG-ASSET-006 | Plan work order with labour, materials, and permit steps; verify planning package fields saved and rendered. |
| FR-ASSET-074 | 5A | Weekly scheduling board with over-allocation guard | BG-ASSET-006 | Overbook a crew; verify conflict shown and override reason required. |
| FR-ASSET-075 | 5A | Planned/unplanned classification and backlog age | BG-ASSET-006, BG-ASSET-007 | Complete corrective job after 12 days; verify `unplanned` classification and backlog age = 12 days. |
| FR-ASSET-076 | 5A | Shutdown/turnaround package | BG-ASSET-006 | Group 4 work orders into outage package; verify shared window, coordinator, and readiness summary. |
| FR-ASSET-077 | 6A | Reserve MRO materials for work order | BG-ASSET-006 | Reserve 3 stock items against work order; verify reservations exist and unavailable quantity is flagged. |
| FR-ASSET-078 | 6A | Material shortage exception and linked supply request | BG-ASSET-006 | Reserve unavailable part; verify shortage exception created and linked procurement or transfer request available. |
| FR-ASSET-079 | 6A | Condition-event threshold evaluation | BG-ASSET-006, BG-ASSET-007 | Submit meter reading above threshold; verify inspection or corrective action recommendation is generated. |
| FR-ASSET-080 | 6A | Structured closeout with failure coding | BG-ASSET-007 | Attempt to close corrective work order without failure code; verify rejection. |
| FR-ASSET-081 | 6A | Reliability dashboard metrics | BG-ASSET-006, BG-ASSET-007 | Open dashboard for date range; verify PM compliance, MTBF, MTTR, and backlog metrics are present. |
| FR-ASSET-082 | 6A | Bad-actor detection and root-cause workflow | BG-ASSET-007 | Trigger repeat-failure threshold; verify bad-actor flag and root-cause workflow action available. |
| FR-ASSET-083 | 6A | Mobile offline work execution | BG-ASSET-006 | Complete checklist and parts usage offline; reconnect; verify records sync and timestamps preserved. |

## 9.4 Context Gaps Identified

The following gaps were identified during requirements authoring. Each must be resolved before the downstream design and development phases commence.

- `[CONTEXT-GAP: deferred tax asset recognition policy]` — Section 7.2.2 notes that when *TaxBase > CarryingAmount* a Deferred Tax Asset arises. The recognition criteria (IAS 12 §24 — probable future taxable profit) are a policy decision by management. The asset module should only recognise a DTA if a policy decision is made and configured. Consultant must specify: does Longhorn ERP recognise DTAs, and if so, under what tenant-level configuration switch?
- `[CONTEXT-GAP: disposal approval workflow]` — The number of approval tiers and the minimum approval role for disposal have not been defined in `_context/`. Confirm: does disposal require a single approver (Asset Manager), or a two-tier approval (Asset Manager + Finance Manager)?
- `[CONTEXT-GAP: insurance notification channels]` — Section 6.2 specifies in-app and email notifications. Confirm whether SMS via Africa's Talking should also be sent for insurance expiry alerts, and which tenant subscription plans include SMS notifications.

## 9.5 LaTeX Formula Verification Notes

Additional context gaps introduced by Sections 5A and 6A:

- `[CONTEXT-GAP: asset criticality model]` â€” Confirm the default criticality scale, scoring method, and whether LonghornERP will support categorical criticality only or probability-versus-consequence scoring at tenant level.
- `[CONTEXT-GAP: condition-event source scope]` â€” Confirm which external sources are in scope for first release: manual inspections only, mobile meter capture, or direct telemetry ingestion through the integration layer.

The following formulas appear in the body of this SRS. Integrity verification is performed against IAS 16 and IAS 12 source standards.

| Formula | Standard | Integrity Check |
|---|---|---|
| $Dep = \frac{Cost - ResidualValue}{UsefulLife}$ | IAS 16 §50 | Confirmed: annual depreciable amount divided by years. Monthly charge = annual ÷ 12. |
| $Dep_n = NBV_{n-1} \times Rate$ | IAS 16 §62 | Confirmed: rate applied to carrying amount at start of period. NBV floor = ResidualValue per FR-ASSET-015. |
| $DTL = (TaxBase - CarryingAmount) \times TaxRate$ | IAS 12 §15 | Confirmed: temporary difference × applicable tax rate. Sign convention: negative result = liability (CarryingAmount > TaxBase). |
| $Gain = DisposalProceeds - NBV$ | IAS 16 §71 | Confirmed: net proceeds minus carrying amount at disposal date. Negative result = loss, recognised in P&L per IAS 16 §71. |

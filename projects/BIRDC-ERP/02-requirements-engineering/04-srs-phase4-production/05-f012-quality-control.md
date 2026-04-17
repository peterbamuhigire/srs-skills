# 4. Specific Requirements — F-012: Quality Control & Laboratory

## 4.1 Inspection Template Management

**FR-QC-001**
*When* a QC Manager creates a new inspection template, *the system shall* record the template name, template code (format `QCT-NNN`), applicable product category, inspection stage (Incoming Material, In-Process, or Final Product), version number, and status (Draft or Active); and *the system shall* prevent use of a Draft template in live inspection records.

*Test oracle:* Assigning a Draft template to an inspection record returns a validation error; only Active templates are selectable on the inspection creation form.

---

**FR-QC-002**
*When* a parameter line is added to an inspection template, *the system shall* support the following parameter types, each with its own configuration fields:

- **Numeric:** parameter name, unit of measure, LSL, USL, target value, decimal places
- **Pass/Fail:** parameter name, pass criteria text, fail criteria text
- **Text:** parameter name, maximum character length, required field flag
- **Photo:** parameter name, minimum photo count, maximum photo count, guidance text

*Test oracle:* A template with one parameter of each type is saved successfully; each parameter line is retrievable with all type-specific fields populated.

---

**FR-QC-003**
*When* a QC Manager assigns a template to a product category and inspection stage, *the system shall* enforce that only one Active template exists per product-category and inspection-stage combination, and reject a new assignment that would create a duplicate, displaying the existing active template name.

*Test oracle:* Attempting to set a second Active template for "Matooke Flour — Final Product" returns the name of the existing Active template and blocks the assignment.

---

**FR-QC-004**
*When* a QC Manager creates a new version of an active template, *the system shall* increment the version number, set the new version to "Draft", carry forward all parameter lines as editable defaults, and record the previous version's deactivation date when the new version is activated.

*Test oracle:* After activation of version 2, version 1 status equals "Superseded" with a deactivation date; version 2 is Active; all inspection records created under version 1 remain linked to version 1 for historical accuracy.

---

## 4.2 Incoming Material Inspection

**FR-QC-005**
*When* a goods receipt batch of raw matooke is created in F-009 (Procurement), *the system shall* automatically create a pending incoming material inspection record linked to that batch ID, and send an in-application notification to the QC Manager (STK-010) that a batch awaits inspection.

*Test oracle:* A new GRN batch in F-009 triggers an inspection record with status "Pending" and a notification to the QC Manager; the inspection record references the GRN batch ID.

---

**FR-QC-006**
*When* a QC analyst opens an incoming material inspection record and selects the applicable inspection template, *the system shall* present all parameter lines from the template in a sequential input form, validate each numeric entry against LSL and USL in real time (highlighting out-of-specification values in red before submission), and require all parameters to be completed before the inspection can be submitted.

*Test oracle:* Entering a moisture content of 18% against a USL of 14% highlights the field red immediately; submitting with any incomplete mandatory parameter returns a field-level validation error.

---

**FR-QC-007**
*When* a QC analyst submits an incoming material inspection, *the system shall* evaluate all parameter results against their specification limits, determine the overall quality grade (A, B, or C) based on the configurable grading rules, and record the grade on the inspection record and on the linked GRN batch.

The grading rules are configurable by the QC Manager (DC-002):

- Grade A: all parameters within specification limits
- Grade B: up to [configurable N] parameters within a configurable secondary tolerance band
- Grade C: any parameter outside grade B tolerance

*Test oracle:* With N = 1 and all parameters within spec, grade equals A; with exactly 1 parameter within secondary tolerance, grade equals B; the grade is stored on the GRN batch and is readable by F-009.

---

**FR-QC-008**
*When* the quality grade for an incoming batch is set to A, B, or C, *the system shall* write the grade to the procurement batch record in F-009, enabling the procurement payment tier logic to apply the configured price for that grade in the farmer payment calculation.

*Test oracle:* A batch graded B has the grade "B" readable on the F-009 batch record before the farmer payment is processed; the payment uses the price tier configured for grade B.

---

**FR-QC-009**
*When* an incoming batch receives a quality grade of C or is otherwise rejected, *the system shall* set the batch inventory status to "Rejected", prevent the batch from being selected for production material requisition, and require the QC Manager to record a disposition (Return to Supplier or Dispose) before the batch record can be closed.

*Test oracle:* A batch with "Rejected" status does not appear in the material selection list for production requisitions; the batch record cannot be closed without a disposition entry.

---

**FR-QC-010**
*When* a QC analyst records a Photo parameter result during incoming inspection, *the system shall* accept images captured from the device camera or uploaded from device storage, store the images linked to the inspection record and batch ID, and display thumbnails on the inspection summary page.

*Test oracle:* An inspection record with photo parameters shows image thumbnails on the summary page; the images are accessible by inspection record ID through the inspection detail view.

---

**FR-QC-011**
*When* an incoming material inspection record is submitted, *the system shall* record the inspector's user ID, submission timestamp, and the inspection template version used, and prevent any modification to the submitted record; all changes after submission must be recorded as a new inspection event referencing the original.

*Test oracle:* Submitting an inspection record sets it to immutable; attempting to edit any field via the API returns HTTP 403; a re-inspection creates a new record referencing the original inspection ID.

---

**FR-QC-012**
*When* the QC Manager requests the incoming material quality summary report, *the system shall* display, for the selected period: total batches received, count and percentage by quality grade (A, B, C, Rejected), average result per numeric parameter, and a trend chart of grade distribution over time (weekly or monthly granularity).

*Test oracle:* Grade A count + Grade B count + Grade C count + Rejected count equals total batches received; percentages sum to 100%; the trend chart renders with ApexCharts.

---

## 4.3 In-Process QC Checkpoints

**FR-QC-013**
*When* a job card operation is configured as a quality checkpoint (FR-MFG-025), *the system shall* link an inspection template to that checkpoint, and upon reaching the checkpoint during production order execution, require a QC analyst to complete the template before the operation can be marked complete.

*Test oracle:* A checkpoint operation cannot be marked "Complete" until the linked inspection template is fully submitted; the system records the QC analyst's user ID on the checkpoint result.

---

**FR-QC-014**
*When* a critical checkpoint result is outside specification (FR-MFG-028), *the system shall* set the checkpoint status to "Failed — Critical", halt production on the operation (preventing the next operation from starting), create an NCR record pre-populated with the batch ID, checkpoint name, out-of-specification parameter, and measured value, and notify the QC Manager immediately via an in-application alert.

*Test oracle:* A critical checkpoint failure sets the checkpoint status to "Failed — Critical"; the next operation's start button is disabled; an NCR record is created with the batch ID and parameter value; the QC Manager alert record is created.

---

**FR-QC-015**
*When* a non-critical checkpoint result is outside specification (FR-MFG-029), *the system shall* record the result as "Out of Spec — Non-Critical", allow the operation to proceed, log the event in the batch quality record, and display a warning to the supervisor confirming acknowledgement is required before proceeding.

*Test oracle:* The operation can be started after the supervisor clicks an acknowledgement button; the out-of-specification event appears in the batch quality record with a "Non-Critical" flag.

---

**FR-QC-016**
*When* a production order has one or more in-process checkpoint results recorded, *the system shall* display a checkpoint result summary on the production order detail page showing: checkpoint name, parameter, result, specification limit, pass/fail status, and inspector for each checkpoint in the job card sequence.

*Test oracle:* The checkpoint summary on the production order page lists all checkpoints in job card sequence order; each row contains all 6 specified data elements.

---

## 4.4 Finished Product Certification and Certificate of Analysis

**FR-QC-017**
*When* a production order advances to "QC Check" status, *the system shall* create a final product inspection record linked to the production order, auto-populate it with the applicable final product inspection template for the product category, and set the inspection status to "Pending Final Inspection".

*Test oracle:* On status transition to "QC Check", a final inspection record appears in the QC inspection queue with status "Pending Final Inspection" and the correct template attached.

---

**FR-QC-018**
*When* a QC Manager submits a final product inspection where all parameters are within specification, *the system shall* set the batch quality status to "Approved", generate a Certificate of Analysis (CoA) document, record the CoA number (format `COA-YYYY-NNNN`), record the approving QC Manager's user ID and timestamp, and trigger the production order status transition to "Completed" (FR-MFG-018).

*Test oracle:* All parameters within spec produces a "Approved" batch status; a CoA record is created with a sequential CoA number; the production order status transitions to "Completed"; the approving user ID and timestamp are stored.

---

**FR-QC-019**
*When* a QC Manager submits a final product inspection where any parameter is outside specification, *the system shall* set the batch quality status to "Rejected", block finished goods transfer to saleable inventory (BR-004), create an NCR record, and require the QC Manager to specify a disposition (Reprocess, Dispose, or Downgrade) before the batch can be closed.

*Test oracle:* A batch with one out-of-specification parameter has status "Rejected"; the stock transfer API for that batch returns HTTP 400 with error code QC_GATE_BLOCKED; no CoA is generated; the NCR record is created.

---

**FR-QC-020**
*When* a QC Manager sets a batch quality status to "On Hold" (pending further testing), *the system shall* prevent the batch from being selected for sales order allocation, display the batch as "On Hold" in inventory reports, and allow the QC Manager to transition the batch to "Approved" or "Rejected" upon test completion.

*Test oracle:* A batch with "On Hold" status does not appear in available-to-sell quantities; the status transitions to "Approved" or "Rejected" upon QC Manager action; each status change is logged in the audit trail.

---

**FR-QC-021**
*When* a CoA is generated for domestic market distribution, *the system shall* produce a PDF document (using mPDF) formatted to UNBS standards containing: CoA number, batch number, product name, production date, expiry date, test parameter list with results and specification limits, overall disposition (Approved/Rejected), QC Manager name, signature line, and the BIRDC letterhead.

*Test oracle:* The generated PDF contains all 10 specified data elements; the CoA number matches the database record; the document is retrievable by CoA number.

---

**FR-QC-022**
*When* a batch is designated for export to South Korea, *the system shall* generate an export-grade CoA formatted to South Korea MFDS (Ministry of Food and Drug Safety) requirements, containing market-specific parameter set and limits as configured by the QC Manager.

[CONTEXT-GAP: GAP-010 — exact MFDS parameter list and format not yet provided by BIRDC QC Manager; export CoA template cannot be finalised until this information is received.]

*Test oracle:* The South Korea CoA document contains the MFDS-specific parameter set; the document format matches the MFDS-required layout once GAP-010 is resolved.

---

**FR-QC-023**
*When* a batch is designated for export to the European Union (Italy), *the system shall* generate an export-grade CoA formatted to Codex Alimentarius standards with EU-specific parameters as configured by the QC Manager.

[CONTEXT-GAP: GAP-010 — exact EU/Codex Alimentarius parameter list not yet provided; export CoA template pending QC Manager input.]

*Test oracle:* The EU CoA contains the Codex Alimentarius parameter set; format complies with EU import documentation requirements once GAP-010 is resolved.

---

**FR-QC-024**
*When* a batch is designated for export to Saudi Arabia, *the system shall* generate an export-grade CoA formatted to Saudi Food and Drug Authority (SFDA) requirements with market-specific parameters.

[CONTEXT-GAP: GAP-010 — SFDA parameter list and format not yet provided.]

*Test oracle:* The Saudi CoA contains the SFDA-required parameter set once GAP-010 is resolved.

---

**FR-QC-025**
*When* a batch is designated for export to Qatar, *the system shall* generate an export-grade CoA formatted to Qatar Ministry of Public Health (MOPH) requirements.

[CONTEXT-GAP: GAP-010 — Qatar MOPH parameter list and format not yet provided.]

*Test oracle:* The Qatar CoA contains the MOPH-required parameter set once GAP-010 is resolved.

---

**FR-QC-026**
*When* a batch is designated for export to the United States, *the system shall* generate an export-grade CoA formatted to U.S. Food and Drug Administration (FDA) requirements.

[CONTEXT-GAP: GAP-010 — FDA parameter list and format not yet provided.]

*Test oracle:* The USA CoA contains the FDA-required parameter set once GAP-010 is resolved.

---

**FR-QC-027**
*When* a sales order is dispatched for an export market and the linked batch has status "Approved for Domestic" only, *the system shall* block the dispatch and display an error requiring an export-grade CoA for the destination market before dispatch can proceed (BR-017).

*Test oracle:* Dispatching a "Domestic Only" approved batch on a South Korea export order returns an error code EXPORT_COA_REQUIRED; dispatch is blocked until an export CoA for South Korea is generated for that batch.

---

**FR-QC-028**
*When* the QC Manager views the CoA register, *the system shall* list all issued CoAs in the selected date range with: CoA number, batch number, product name, issue date, destination market, QC Manager name, and a link to the PDF; the register must be filterable by destination market and date range.

*Test oracle:* The CoA register filtered for "South Korea" shows only South Korea export CoAs; the PDF link opens the correct CoA document for each record.

---

## 4.5 Statistical Process Control

**FR-QC-029**
*When* a QC parameter is designated as SPC-tracked in the inspection template, *the system shall* record each result in the SPC data series linked to that parameter and product combination, accumulating values across inspection events.

*Test oracle:* Submitting 10 inspection results for an SPC-tracked moisture content parameter results in 10 SPC data points in the series; each point stores the inspection date, batch ID, and result value.

---

**FR-QC-030**
*When* a user opens the SPC chart for a parameter, *the system shall* compute and display an X-bar (mean) control chart and an R (range) control chart for the last N subgroups (configurable, default N = 25), showing: the centre line ($\bar{\bar{x}}$ or $\bar{R}$), upper control limit (UCL), and lower control limit (LCL) calculated as:

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_2 \bar{R}, \quad LCL_{\bar{x}} = \bar{\bar{x}} - A_2 \bar{R}$$

$$UCL_R = D_4 \bar{R}, \quad LCL_R = D_3 \bar{R}$$

where $A_2$, $D_3$, $D_4$ are standard SPC constants for the configured subgroup size.

*Test oracle:* For a subgroup size of 5, $A_2 = 0.577$, $D_4 = 2.114$, $D_3 = 0$; with $\bar{\bar{x}} = 12.0$ and $\bar{R} = 0.8$, $UCL_{\bar{x}} = 12.462$ and $LCL_{\bar{x}} = 11.538$; the chart displays these values.

---

**FR-QC-031**
*When* a new subgroup is added to an SPC series and any point falls outside the UCL or LCL, *the system shall* mark the point as "Out of Control" on the chart, generate an out-of-control alert to the QC Manager, and create a preliminary NCR record for investigation.

*Test oracle:* A point exceeding the UCL is displayed in red on the X-bar chart; the QC Manager alert record is created; a preliminary NCR record exists for the out-of-control event.

---

**FR-QC-032**
*When* a user opens the process capability report for a parameter, *the system shall* compute and display:

$$C_p = \frac{USL - LSL}{6\hat{\sigma}}, \quad C_{pk} = \min\left(\frac{USL - \bar{x}}{3\hat{\sigma}}, \frac{\bar{x} - LSL}{3\hat{\sigma}}\right)$$

where $\hat{\sigma}$ is estimated from $\hat{\sigma} = \bar{R} / d_2$, using the standard SPC constant $d_2$ for the configured subgroup size.

*Test oracle:* For $USL = 14$, $LSL = 10$, $\bar{x} = 12.0$, $\hat{\sigma} = 0.344$ (with $\bar{R} = 0.8$ and $d_2 = 2.326$ for subgroup size 5): $C_p = 1.94$ and $C_{pk} = 1.94$; the report displays these values.

---

**FR-QC-033**
*When* $C_{pk}$ falls below a configurable threshold (default 1.33), *the system shall* flag the parameter as "Capability Concern" in the process capability report and send an alert to the QC Manager, recommending process review.

*Test oracle:* A $C_{pk}$ value of 1.10 (below the 1.33 threshold) flags the parameter as "Capability Concern" and generates a QC Manager alert; a $C_{pk}$ of 1.50 generates no alert.

---

**FR-QC-034**
*When* a user views the SPC trend report, *the system shall* display parameter trend charts (ApexCharts line charts) for all SPC-tracked parameters for the selected product over the selected date range, with USL and LSL lines rendered as horizontal reference lines on each chart.

*Test oracle:* The trend report renders one chart per SPC-tracked parameter; USL and LSL lines are visible on each chart; the chart data points match the inspection result records for the period.

---

## 4.6 Non-Conformance Reports

**FR-QC-035**
*When* a QC analyst or automated system creates an NCR, *the system shall* record: NCR number (format `NCR-YYYY-NNNN`), date raised, product / batch affected, detection stage (Incoming, In-Process, Final, Post-Release), severity (Minor, Major, Critical), description of non-conformance, and the raising user ID.

*Test oracle:* A new NCR is retrievable by NCR number with all fields populated; the NCR number follows the sequential format.

---

**FR-QC-036**
*When* an NCR is created, *the system shall* set its status to "Open" and assign it to the QC Manager for root cause analysis, sending an in-application notification to the QC Manager with the NCR number and brief description.

*Test oracle:* A newly created NCR has status "Open" and an assignment record to the QC Manager user ID; the notification record is created with the NCR number.

---

**FR-QC-037**
*When* the QC Manager records a root cause analysis on an NCR, *the system shall* accept: root cause category (Material, Process, Equipment, Human Error, Measurement, Environment — configurable per DC-002), root cause description text, and the analysis date; and advance the NCR status to "Root Cause Identified".

*Test oracle:* An NCR with root cause category and description recorded advances to "Root Cause Identified" status; the analysis date is stored.

---

**FR-QC-038**
*When* a corrective action is added to an NCR, *the system shall* record: corrective action description, responsible person (employee ID from F-013), target completion date, and status (Open, In Progress, Completed); and set the NCR status to "Corrective Action In Progress".

*Test oracle:* An NCR with a corrective action record transitions to "Corrective Action In Progress"; the corrective action lists responsible person, target date, and status.

---

**FR-QC-039**
*When* the responsible person marks a corrective action as "Completed", *the system shall* record the completion date and require the QC Manager to verify closure by clicking **Verify Closure** before the NCR status advances to "Closed".

*Test oracle:* Marking corrective action "Completed" does not close the NCR; the NCR status changes to "Closed" only after the QC Manager clicks **Verify Closure**; both the completion date and verification timestamp are stored.

---

**FR-QC-040**
*When* an NCR severity is "Critical" and the corrective action target date is overdue by more than 7 days, *the system shall* send a daily in-application alert to the BIRDC Director (STK-001) and the QC Manager until the NCR is closed.

*Test oracle:* An overdue Critical NCR generates a Director alert on day 8 and each subsequent day; the alert ceases when the NCR status equals "Closed".

---

**FR-QC-041**
*When* a user views the NCR register, *the system shall* list all NCRs filterable by: status, severity, detection stage, product, and date range; displaying NCR number, date, product, severity, status, and days open for each record; with a summary row showing total open NCRs by severity at the top.

*Test oracle:* Filtering by severity "Critical" and status "Open" returns only Critical Open NCRs; the summary row counts match the filtered counts.

---

## 4.7 Laboratory Equipment Management

**FR-QC-042**
*When* a laboratory instrument is registered, *the system shall* record: instrument name, instrument code (format `INST-NNN`), category (balance, moisture analyser, spectrophotometer, etc. — configurable), serial number, manufacturer, model number, location, acquisition date, and status (Active, Under Calibration, Out of Service).

*Test oracle:* A new instrument record is retrievable by instrument code with all fields populated.

---

**FR-QC-043**
*When* a calibration event is recorded for an instrument, *the system shall* capture: calibration date, calibration certificate reference number, calibrated by (internal staff or external vendor), next calibration due date, and calibration result (Passed, Failed, Conditional Pass); and update the instrument's status accordingly.

*Test oracle:* After recording a calibration event with result "Passed", the instrument status equals "Active" and next calibration due date is stored; after "Failed", status equals "Out of Service".

---

**FR-QC-044**
*When* an instrument's next calibration due date is within 30 days, *the system shall* generate an in-application alert to the QC Manager (STK-010) with the instrument code, name, and due date, refreshed daily until the calibration is recorded.

*Test oracle:* An instrument with calibration due in 25 days generates a QC Manager alert today; the alert is generated again the next day if calibration remains unrecorded.

---

**FR-QC-045**
*When* a calibration due date passes without a new calibration record being entered, *the system shall* automatically set the instrument status to "Calibration Overdue", flag all inspection results recorded using that instrument after the due date as "Suspect — Instrument Overdue", and prevent the instrument from being selected for new inspections.

*Test oracle:* An instrument overdue for 1 day has status "Calibration Overdue"; inspection results recorded after the due date carry a "Suspect" flag; the instrument does not appear in the instrument selection list for new inspections.

---

**FR-QC-046**
*When* an inspection result is linked to an instrument with "Suspect" or "Calibration Overdue" status, *the system shall* display a prominent warning on the inspection record indicating that the result may be unreliable due to the instrument calibration status.

*Test oracle:* An inspection detail page for a result recorded on an overdue instrument shows a "Suspect Instrument" warning; the warning includes the instrument code and the calibration due date that was missed.

---

**FR-QC-047**
*When* the QC Manager requests the calibration status report, *the system shall* list all registered instruments with: instrument code, name, last calibration date, next calibration due date, and status (colour-coded: green for Active, amber for due within 30 days, red for Overdue); filterable by category and status.

*Test oracle:* The report shows all instruments; instruments due within 30 days have amber status; overdue instruments have red status; colour coding is rendered via CSS class, not inline style.

---

## 4.8 Incubation and Maturation Tracking

**FR-QC-048**
*When* a fermented product batch (e.g., banana wine) is created in a production order, *the system shall* create an incubation tracking record linked to the batch ID, recording: batch ID, product name, incubation start date, configured incubation period (days), sampling schedule (list of sampling days, e.g., Day 7, Day 14, Day 21, Day 30), and target completion date.

*Test oracle:* A banana wine production batch creates an incubation record with all specified fields; target completion date equals start date plus configured incubation period.

---

**FR-QC-049**
*When* a scheduled sampling day arrives for an incubating batch, *the system shall* generate an in-application prompt to the QC Manager to perform the sampling, display the elapsed days since incubation start, and record: sampling event date, inspector user ID, tasting notes (text), and analysis results (linked to an inspection template specific to in-process fermentation).

*Test oracle:* On the Day 14 sampling date, an alert appears in the QC Manager's task list; submitting sampling results records the date, user, and analysis values linked to the incubation record.

---

**FR-QC-050**
*When* the incubation period is complete and the final sampling results meet the configured release criteria, *the system shall* allow the QC Manager to mark the batch as "Maturation Complete" and transition it to the final product inspection stage (FR-QC-017).

*Test oracle:* A batch whose incubation period has elapsed and whose final sampling results meet release criteria can be transitioned to Final Inspection; a batch with an unelapsed incubation period cannot be transitioned to Final Inspection.

---

**FR-QC-051**
*When* a QC Manager views the incubation tracking dashboard, *the system shall* display all active incubating batches with: batch ID, product, start date, current elapsed days, next sampling date, days until completion, and current status (Active, Sampling Due, Overdue for Sampling, Maturation Complete).

*Test oracle:* A batch at Day 20 of a 30-day incubation shows elapsed = 20 days, days until completion = 10; a batch whose next sampling date has passed without a result shows "Overdue for Sampling".

---

**FR-QC-052**
*When* the incubation period elapses without a "Maturation Complete" action, *the system shall* generate a daily alert to the QC Manager until the batch is either marked as "Maturation Complete" or given an alternative disposition (Extended Incubation, Rejected).

*Test oracle:* A batch 3 days past its incubation end date generates a daily alert; the alert stops when the QC Manager records a disposition.

---

## 4.9 Batch Quality Status and Inventory Integration

**FR-QC-053**
*When* a batch quality status is set by the QC module, *the system shall* write the status to the inventory batch record in F-003 in real time, ensuring that inventory allocation logic (for sales, transfers, and production requisitions) immediately respects the updated status.

*Test oracle:* Setting a batch to "Rejected" in F-012 causes the batch to be excluded from available-to-sell quantity in F-003 within 1 second; confirmed by querying the F-003 available quantity API before and after the status change.

---

**FR-QC-054**
*When* a warehouse operator attempts to allocate a batch with status "Rejected" or "On Hold" to a sales order or stock transfer, *the system shall* return an error message identifying the batch, its quality status, and the name of the QC Manager responsible for the batch, and block the allocation.

*Test oracle:* Attempting to add a "Rejected" batch to a sales order line returns error code BATCH_QC_STATUS_BLOCKED with the batch number and QC status; the batch does not appear in the available batch selection list.

---

**FR-QC-055**
*When* a QC Manager changes a batch status from "On Hold" to "Approved" or "Rejected", *the system shall* record the status change with user ID, old status, new status, timestamp, and reason text in the audit trail; and send an in-application notification to the Store Manager (STK-008).

*Test oracle:* The audit trail entry for the status change contains all 5 specified fields; the Store Manager notification is created within 30 seconds of the status change.

---

## 4.10 QC Reports

**FR-QC-056**
*When* the QC Manager requests the batch quality summary report, *the system shall* list all production batches in the selected period with: batch ID, product, production date, quality status, CoA number (if issued), destination market, and the name of the approving inspector; exportable to PDF and Excel.

*Test oracle:* The report lists all batches in the period; the CoA number column is blank for batches without an issued CoA; the export produces valid PDF and Excel files.

---

**FR-QC-057**
*When* the QC Manager requests the yield-quality correlation report, *the system shall* display, for each production order in the selected period, the actual yield% alongside the final QC disposition (Approved, Rejected), enabling visual identification of the relationship between yield deviation and quality outcome, rendered as a scatter plot (ApexCharts).

*Test oracle:* Each data point on the scatter plot corresponds to one production order; hovering over a point displays the production order ID, yield%, and QC disposition.

---

**FR-QC-058**
*When* the QC Manager requests the parameter trend chart for a specific quality parameter, *the system shall* display all inspection results for that parameter and product over the selected date range as a time-series line chart, with USL and LSL reference lines, colour-coded to distinguish incoming, in-process, and final product inspection results.

*Test oracle:* The chart shows 3 distinct data series (incoming, in-process, final); results exceeding USL or below LSL are displayed in a distinct colour; the chart is rendered by ApexCharts.

---

**FR-QC-059**
*When* a user views the NCR status report, *the system shall* display: total NCRs by status (Open, Root Cause Identified, Corrective Action In Progress, Closed) for the selected period; average time to closure (days) for closed NCRs; and a list of NCRs overdue for corrective action, with days overdue shown.

*Test oracle:* Total NCR count equals Open + Root Cause Identified + Corrective Action In Progress + Closed; average time to closure is the mean of (close date − open date) in days for all Closed NCRs in the period.

---

**FR-QC-060**
*When* a user exports the CoA register to PDF, *the system shall* produce a multi-page PDF listing all CoAs in the selected period with: CoA number, batch ID, product name, production date, approval date, QC Manager name, and destination market; formatted with the BIRDC letterhead and page numbers.

*Test oracle:* The exported PDF contains one row per CoA in the period; page numbers are present; the BIRDC letterhead appears on every page.

---

**FR-QC-061**
*When* the QC Manager views the equipment calibration status report, *the system shall* display all instruments grouped by status (Active, Due Soon, Overdue, Out of Service) with the calibration due date sorted ascending within each group, enabling prioritised scheduling.

*Test oracle:* Instruments with the nearest calibration due dates appear at the top of the "Due Soon" group; instruments in "Out of Service" are listed separately from "Overdue".

---

## 4.11 Additional QC Requirements

**FR-QC-062**
*When* a QC analyst opens the inspection entry form on a mobile device or tablet (responsive web), *the system shall* render all parameter input fields with touch-friendly input controls (minimum 44 px touch target), numeric keypad for numeric parameters, and camera access for photo parameters, in compliance with DC-001.

*Test oracle:* On a device with a 7-inch screen, all input fields are tappable without zooming; numeric fields invoke the numeric keypad; photo fields open the device camera.

---

**FR-QC-063**
*When* a CoA PDF is generated, *the system shall* produce the document within 5 seconds from the generation request under normal load conditions (defined as fewer than 10 concurrent CoA generation requests).

*Test oracle:* Under load conditions, 10 simultaneous CoA generation requests each complete within 5 seconds; the generated PDFs are identical in content to the database record for each batch.

---

**FR-QC-064**
*When* the system detects that a batch has been "Approved" in the QC module, *the system shall* write the CoA document reference (CoA number and PDF file path) to the batch record in F-003, making the CoA accessible from the inventory batch detail view without navigating to the QC module.

*Test oracle:* The inventory batch detail in F-003 displays a clickable CoA link after QC approval; clicking the link opens the CoA PDF.

---

**FR-QC-065**
*When* a new inspection template is created or an existing template is versioned, *the system shall* log the action in the system audit trail with: user ID, action (Created or Versioned), template code, old version (if applicable), new version, and timestamp; preserving the immutable compliance record required by DC-003.

*Test oracle:* The audit trail contains an entry for every template creation and versioning event; the entry includes all 6 specified fields.

---

**FR-QC-066**
*When* a production batch is released for export, *the system shall* verify that an export-grade CoA for the destination market has been issued for that batch before the system allows the sales order to be dispatched, and if no export CoA exists, return a clear error identifying the missing CoA type and the batch number.

*Test oracle:* Attempting to dispatch a Saudi Arabia export order without a Saudi SFDA CoA returns error EXPORT_COA_REQUIRED — SFDA; dispatch proceeds only after the SFDA CoA is generated.

---

**FR-QC-067**
*When* the QC Manager requests the aflatoxin monitoring report (a subset of the incoming material inspection parameters), *the system shall* display all aflatoxin test results (ppb) for all incoming matooke batches in the selected period, with: batch ID, supplier cooperative, delivery date, aflatoxin result (ppb), USL, pass/fail status, and quality grade; sorted by date descending.

*Test oracle:* The aflatoxin report shows only aflatoxin parameter results from incoming inspections; the pass/fail determination uses the USL defined on the active incoming inspection template.

---

**FR-QC-068**
*When* the Finance Director requests the QC cost of non-conformance report, *the system shall* calculate and display the total value of rejected batches (quantity × FIFO cost), total rework costs, and total disposal costs for the selected period, sourced from NCR and batch rejection records.

*Test oracle:* The cost of non-conformance total equals the sum of rejected batch values plus rework costs plus disposal costs for the period; each component is displayed separately with a drill-down to supporting records.

---

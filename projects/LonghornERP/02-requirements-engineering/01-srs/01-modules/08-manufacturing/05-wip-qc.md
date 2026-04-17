# WIP Tracking and Quality Checkpoints

## 5.1 WIP Tracking

**FR-MFG-023** — The system shall maintain a WIP ledger per production order showing: total raw material cost issued, labour cost applied (from timesheet entries linked to the production order), overhead absorbed to date, and total WIP value; the WIP ledger shall update in real time as issues, labour entries, and overhead allocations are posted.

**FR-MFG-024** — The system shall display a production order progress indicator showing: percentage of raw materials issued versus required, percentage of production time elapsed versus planned, and current WIP value versus standard cost.

## 5.2 Quality Checkpoints

**FR-MFG-025** — The system shall support configurable QC checkpoints on a BOM; each checkpoint defines: checkpoint name, stage in the production process (e.g., "After Mixing", "After Filling"), the test parameters to record (e.g., moisture content, pH, weight per unit), and pass/fail criteria.

**FR-MFG-026** — When a production order reaches a QC checkpoint, the system shall generate a QC inspection task assigned to the quality inspector; the production order shall be blocked from proceeding to the next stage until the inspection result is recorded.

**FR-MFG-027** — When a QC inspection result is recorded as "Pass", the system shall unblock the production order and allow the next stage to proceed; the inspector identity, result values, and pass/fail decision shall be stored immutably in the production order audit record.

**FR-MFG-028** — When a QC inspection result is recorded as "Fail", the system shall transition the production order to "Quality Hold" status; the production supervisor shall have three options: (a) rework — return to a previous stage, (b) downgrade — reclassify the batch to a lower grade, or (c) reject — scrap the entire production run.

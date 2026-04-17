# 4. Seasonal Intake and Weighbridge Integration Requirements

## 4.1 Overview

This section specifies requirements for opening and managing seasonal intake periods, recording individual commodity deliveries from farmers, integrating with RS-232 weighbridge hardware for automatic weight capture, and posting validated batches to the inventory and accounting ledgers.

## 4.2 Seasonal Intake Periods

**FR-COOP-023** — When an administrator opens an intake period for a season by selecting the season record and setting the collection centre, the system shall activate an intake session that constrains all new intake entries to the active season's commodity, date range, and price schedule.

*Acceptance criterion:* An active intake session for "2025 Long Rains Tea" at "Butebo Collection Centre" only accepts Tea entries dated within the season's start-to-end window.

**FR-COOP-024** — When an administrator closes an intake period, the system shall set the period status to "Closed", prevent new intake entries from being added, and require a supervisor PIN or two-factor confirmation before the period transitions to "Closed".

*Acceptance criterion:* A supervisor enters their PIN; the period transitions to "Closed" and the "New Intake" button is disabled; an attempt to add intake via the API returns HTTP 403.

**FR-COOP-025** — When an intake period is closed, the system shall generate a period closure summary showing: total weight received (kg), total number of entries, total gross value (UGX), breakdown by grade, and breakdown by society/group.

*Acceptance criterion:* A period with 150 entries across 3 grades produces a closure summary with correct aggregated totals matching the sum of individual entries (verified by independent calculation).

## 4.3 Intake Entry Recording

**FR-COOP-026** — When a collection officer selects a registered farmer, selects a commodity and grade, and submits an intake entry with the recorded weight (kg) and delivery date, the system shall compute the gross payment as:

$GrossPayment = Weight \times GradePrice$

persist the entry with a unique intake reference number, and display the computed gross payment to the officer.

*Acceptance criterion:* 120 kg of Grade A Tea at UGX 450/kg → GrossPayment = UGX 54,000; the entry is stored with a unique reference and the computed value displayed within 1 second of submission.

**FR-COOP-027** — When a collection officer submits an intake entry with a weight of 0 kg or a negative weight, the system shall reject the entry and display: "Weight must be greater than 0."

*Acceptance criterion:* Submission with weight = 0 returns the specified error; no record is created.

**FR-COOP-028** — When a collection officer submits an intake entry for a farmer who is not registered or whose registration is inactive, the system shall reject the entry and display: "Farmer [ID/Name] is not active. Complete registration before recording intake."

*Acceptance criterion:* An intake attempt for an unregistered farmer ID returns the rejection message; the entry is not persisted.

**FR-COOP-029** — When a collection officer records more than 1 intake entry per farmer per day for the same commodity, the system shall display a warning: "Farmer [Name] already has [N] intake entry/entries today for [Commodity]. Proceed?" and require explicit confirmation before saving.

*Acceptance criterion:* A second Tea entry for the same farmer on the same day triggers the warning; the officer must confirm; the record is only saved after confirmation.

## 4.4 Weighbridge RS-232 Serial Integration

**FR-COOP-030** — When a weighbridge device is connected via RS-232 serial port and the collection officer initiates weight capture, the system shall read the weight data stream from the configured COM port at the configured baud rate (default: 9600 baud, 8 data bits, no parity, 1 stop bit), parse the weight value, populate the weight field on the intake form, and display the raw serial string in a diagnostic field.

*Acceptance criterion:* A weighbridge transmitting "00120.5 KG\r\n" results in the weight field being auto-populated with 120.5; the raw string is shown in the diagnostic display.

**FR-COOP-031** — When the RS-232 connection is configured but the serial port does not respond within 5 seconds of a capture request, the system shall display: "Weighbridge not responding on [COM port]. Check cable and power." and allow the officer to enter weight manually.

*Acceptance criterion:* With the COM port disconnected, a capture attempt triggers the timeout message after exactly 5 seconds (± 200 ms); the weight field remains editable.

**FR-COOP-032** — When the system receives a weight reading from the weighbridge that is below the minimum stable weight threshold (configurable, default 1.0 kg) or is flagged as unstable by the weighbridge (detected via device-specific stability flag in the data string), the system shall reject the reading, display: "Weight is unstable — place commodity on scale and retry", and not auto-populate the weight field.

*Acceptance criterion:* A simulated unstable reading string that contains the device's instability flag does not populate the weight field; the specified message is shown.

**FR-COOP-033** — When an administrator configures the weighbridge integration settings, the system shall provide fields for: COM port (e.g., COM1–COM20), baud rate (1200 / 2400 / 4800 / 9600 / 19200 / 38400 / 57600 / 115200), data bits (7 / 8), parity (None / Even / Odd), stop bits (1 / 2), and a regex pattern for parsing the weight value from the device's raw output string.

*Acceptance criterion:* Configuration saved with COM3, 9600 baud, 8N1, and parse pattern `(\d+\.?\d*)\s*KG` is persisted and applied on the next capture request.

[CONTEXT-GAP: Specific weighbridge hardware models deployed at collection centres — confirm make/model (e.g., Avery Weigh-Tronix, Mettler Toledo) to validate the default RS-232 output format and stability flag byte position.]

## 4.5 Batch Posting

**FR-COOP-034** — When a supervisor approves a completed intake batch, the system shall post a stock receipt to the Inventory module (Module 02) with the commodity, total weight, collection centre as receiving warehouse, and the intake period reference, and post the corresponding payable journal entry to the Accounting module (Module 01) with farmer payables allocated to each farmer's ledger account.

*Acceptance criterion:* Approving a batch of 50 Tea entries totalling 6,000 kg creates 1 stock receipt in Module 02 for 6,000 kg Tea and 50 individual journal entries in Module 01 (one per farmer) that sum to the batch gross total; no entry is created if approval is not granted.

**FR-COOP-035** — When a supervisor attempts to post a batch that contains entries flagged with a `[V&V-FAIL]` data quality error (e.g., weight outside valid range, unresolved grade mismatch), the system shall block the posting, display a list of all flagged entries with their error descriptions, and require each flag to be resolved before re-attempting the post.

*Acceptance criterion:* A batch with 2 flagged entries cannot be posted until both flags are cleared; the block message lists the entry reference numbers and error descriptions.

# Persona 6: Dr. Amara — QC / Lab Manager

**Profile:** Age 38, MSc Food Science, proficient. Designs inspection templates, conducts in-process and finished product inspections, issues Certificates of Analysis for domestic and export batches, manages Non-Conformance Reports (NCRs), monitors SPC charts for quality trends.

**Critical requirement:** Configurable CoA templates by market (South Korea format differs from EU format).

---

## US-056: Design a Configurable Inspection Template

**US-056:** As Dr. Amara, I want to create and configure inspection templates with different parameter types, so that the inspection form matches exactly what needs to be tested for each product and inspection stage.

**Acceptance criteria:**

- Dr. Amara creates a new inspection template by specifying: template name, applicable product(s), inspection stage (incoming / in-process / finished product), and a list of inspection parameters.
- Each parameter supports 4 data types: Numeric (with minimum and maximum tolerance, unit of measure), Pass/Fail (binary toggle), Text (free entry with character limit), and Photo (mandatory photo attachment).
- A numeric parameter with a measurement outside the configured tolerance range is automatically flagged as "Out of Spec" in red when entered.
- Templates are versioned: when Dr. Amara edits a template, the previous version is retained; all inspection records reference the template version active at the time of inspection.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-001

---

## US-057: Conduct a Finished Product Inspection and Issue a Domestic CoA

**US-057:** As Dr. Amara, I want to complete a finished product inspection and issue a Certificate of Analysis for domestic distribution, so that the production batch can be released to saleable inventory.

**Acceptance criteria:**

- Dr. Amara opens the pending inspection queue, selects a finished product batch, and enters inspection results against the configured template parameters.
- When all required parameters pass (all numeric measurements within tolerance, all pass/fail parameters marked Pass), Dr. Amara can set the batch quality status to "Approved for Domestic" and generate the CoA.
- The CoA PDF includes: BIRDC/PIBID header, batch number, product name, production date, expiry date, inspection date, parameter results table, and Dr. Amara's digital signature (role-based).
- Until Dr. Amara sets the batch status to "Approved," the stock transfer API endpoint for that production batch returns an error if triggered (per BR-004); the batch cannot enter saleable inventory.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-002

---

## US-058: Generate an Export-Grade CoA for a Specific Market

**US-058:** As Dr. Amara, I want to generate an export-grade Certificate of Analysis formatted for the destination market, so that every export shipment is accompanied by the correct documentation.

**Acceptance criteria:**

- Dr. Amara selects the target export market (South Korea, Saudi Arabia, Qatar, Italy, United States) before generating the export CoA; the system loads the market-specific CoA template with the parameters required by that market's import authority.
- A batch with "Approved for Domestic" status cannot generate an export CoA until all additional market-specific parameters are completed and within the destination market's tolerance (per BR-017).
- The export CoA is generated in English and is formatted to the layout accepted by the destination market's import authority; the template is configurable by Dr. Amara without developer involvement (per DC-002).
- The generated CoA is linked to the production batch, the sales order, and the export invoice, creating a complete traceability chain from farm to export.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-003

---

## US-059: Raise a Non-Conformance Report (NCR)

**US-059:** As Dr. Amara, I want to raise an NCR when a quality failure is detected and track the corrective action to closure, so that quality failures are documented and their root causes are eliminated.

**Acceptance criteria:**

- Dr. Amara raises an NCR from any inspection record by specifying: NCR type (incoming material / in-process / finished product), failure description, affected product and batch, severity (Minor / Major / Critical), and immediate containment action taken.
- The NCR is assigned a sequential NCR number and routed to the relevant department head (Production Manager for in-process; Procurement Manager for incoming material) for corrective action assignment.
- The corrective action owner records their corrective action steps and target close date; Dr. Amara reviews and closes the NCR when satisfied.
- NCRs overdue (past their target close date without closure) appear in Dr. Amara's overdue NCR report and an automated reminder is sent to the corrective action owner.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-004

---

## US-060: View SPC Control Charts for Key Quality Parameters

**US-060:** As Dr. Amara, I want to view X-bar and R-chart control charts for critical quality parameters, so that I can detect process drift before it causes a quality failure.

**Acceptance criteria:**

- The SPC module displays X-bar and R-charts for any numeric inspection parameter over a configurable time period (7 days, 30 days, 90 days, custom range).
- Control limits (Upper Control Limit, Lower Control Limit, Centre Line) are calculated automatically from the first 20 data points and are recalculated when Dr. Amara resets the baseline.
- Points outside control limits are displayed in red; the chart triggers an in-app alert to Dr. Amara when 7 or more consecutive points are on the same side of the centre line (Nelson Rule 2).
- The system calculates Cp and Cpk capability indices for each parameter with a minimum of 30 data points and displays them beside the chart.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-005

---

## US-061: Manage Incoming Matooke Quality Grading

**US-061:** As Dr. Amara, I want to grade incoming matooke deliveries as Grade A, B, or C at the factory gate, so that each grade receives the correct purchase price and the production team knows the input quality.

**Acceptance criteria:**

- Dr. Amara or her designee opens the incoming inspection queue, selects the cooperative batch in Stage 2 of the procurement workflow, and records quality grades for the batch using the configured incoming inspection template.
- Three quality grades are supported: A (premium), B (standard), C (downgraded). Each grade has a configurable unit price per kilogramme maintained in the procurement configuration table.
- The quality grade recorded at inspection is used in the Stage 3 farmer contribution breakdown to calculate each farmer's unit price and net payable.
- Batches with > 20% Grade C material generate an automatic alert to the Procurement Manager and Production Supervisor.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-006

---

## US-062: Track Lab Equipment Calibration

**US-062:** As Dr. Amara, I want to track calibration due dates for lab equipment and receive reminders before calibration is overdue, so that all measurements are traceable to calibrated instruments.

**Acceptance criteria:**

- Each lab equipment item has a record with: equipment ID, name, model, serial number, last calibration date, calibration frequency (days), next calibration due date, and calibration certificate attachment.
- The system sends Dr. Amara an email and in-app notification 30 days before any equipment's calibration due date.
- If a calibration due date passes without a new calibration record being uploaded, the equipment status changes to "Calibration Overdue" and inspection results recorded with that equipment are flagged with a warning: "Instrument [ID] calibration expired. Results may not be valid."
- Dr. Amara can upload the new calibration certificate PDF directly to the equipment record; the system records the upload date, certificate number, and calibration lab name.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-012-007

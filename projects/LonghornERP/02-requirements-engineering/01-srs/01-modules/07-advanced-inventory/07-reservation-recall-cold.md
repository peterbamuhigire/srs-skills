# Stock Reservation, Recall Management, and Cold Chain

## 7.1 Stock Reservation

**FR-ADVINV-036** — When a sales order is confirmed, the system shall allow the user to reserve specific quantities of each ordered item against the sales order; reserved stock shall be deducted from the available-to-promise (ATP) balance and shall not be committed to another order without supervisor override.

**FR-ADVINV-037** — The ATP balance shall be computed as: $ATP = OnHandQty - ReservedQty - OpenPickQty$; the system shall display the ATP balance alongside the on-hand balance in all item enquiry screens and sales order entry forms.

**FR-ADVINV-038** — When a reservation is cancelled (by cancelling or closing the linked sales order), the system shall immediately release the reserved quantity back to the ATP balance without requiring manual intervention.

## 7.2 Recall Management

**FR-ADVINV-039** — When an authorised user initiates a product recall, the system shall accept a batch number or a date range as the recall scope and shall: (a) set the QC status of all in-scope batches to "Quarantined", (b) generate a recall trace report listing every sales delivery that issued stock from the affected batches (customer name, invoice number, quantity, delivery date), and (c) generate a supplier trace report listing the originating GRN.

**FR-ADVINV-040** — The recall trace report shall be generated within 2 minutes of recall initiation for a dataset of ≤ 5 years of sales history; this is a compliance SLA, not a design target.

**FR-ADVINV-041** — The system shall provide a recall status dashboard showing the total quantity recalled, quantity in quarantine, quantity already consumed (unrecoverable), and the estimated financial impact.

## 7.3 Cold Chain Compliance

**FR-ADVINV-042** — For items in the cold-chain category (configurable), the system shall attach storage temperature fields to each stock movement: minimum storage temperature (°C), maximum storage temperature (°C), and actual storage temperature at time of movement (optional, sourced from IoT sensor integration or manual entry).

**FR-ADVINV-043** — When a cold-chain item's recorded temperature falls outside the allowed range at any movement step, the system shall flag the batch with a temperature excursion alert, set the QC status to "Quarantined" pending review, and record the excursion in the batch ledger.

**FR-ADVINV-044** — The UNBS certification tracking field shall store: UNBS certificate number, product standard reference (e.g., US EAS 39), certificate issue date, and certificate expiry date; the system shall alert the quality manager 30 days before a UNBS certificate expires.

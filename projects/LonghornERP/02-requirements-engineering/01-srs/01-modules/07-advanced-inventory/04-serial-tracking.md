# Serial Number Tracking

## 4.1 Serial Number Assignment

**FR-ADVINV-016** — When an item is configured as serial-tracked, the system shall require a unique serial number per individual unit on every inbound and outbound stock movement; a serial-tracked item shall always have a quantity of 1 per serial number.

**FR-ADVINV-017** — The system shall support two serial number entry modes: (a) manual entry (user types or scans the serial number) and (b) system-generated (the system assigns a serial number in a configured format, e.g., `SN-YYYYMMDD-NNNN`).

**FR-ADVINV-018** — The system shall validate that a serial number being received on a GRN is not already active in the tenant's inventory; duplicate serial numbers within the same item code shall be rejected.

## 4.2 Serial Number Ledger

**FR-ADVINV-019** — The system shall maintain a serial number ledger for each serialised unit recording: item code, serial number, current location (branch, bin), current owner (in-stock, sold-to customer, in-transit), all movement history (date, document reference, from location, to location), and status (Active, Returned, Scrapped).

**FR-ADVINV-020** — When a serial-tracked item is sold and the delivery note is confirmed, the system shall update the serial number status to "Sold" and record the customer name, invoice number, and sale date in the serial number ledger.

**FR-ADVINV-021** — The system shall provide a serial number enquiry screen where a user can enter a serial number and immediately see its full movement history, current location, and warranty expiry date (if applicable).

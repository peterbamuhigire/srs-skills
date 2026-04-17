# Offline Mode

## 6.1 Offline Transaction Processing

**FR-POS-052** — The POS terminal application shall detect loss of internet connectivity and automatically switch to offline mode; in offline mode, the terminal shall continue to accept sales transactions using the locally cached item catalogue and price list.

**FR-POS-053** — The system shall maintain a local SQLite database on the terminal device containing: item catalogue (code, name, price, VAT rate), current stock balance snapshot (for display purposes only — not a live ledger), active price lists, and the customer list with credit limits; the local database shall be refreshed from the server at every session open.

**FR-POS-054** — The system shall queue all offline transactions in the local database with a unique local transaction ID, the session ID, all basket items, payment method, and the device-local timestamp; the queue shall persist across device restarts.

**FR-POS-055** — The system shall support a minimum offline operation window of 8 hours; if the device has been offline for more than 8 hours, the system shall alert the cashier and recommend escalation to a supervisor.

## 6.2 Offline Payment Restrictions

**FR-POS-056** — In offline mode, the system shall permit cash and card (manual entry) payment methods only; mobile money payment shall be disabled because it requires real-time API connectivity; the cashier shall be notified of this restriction at offline mode entry.

**FR-POS-057** — In offline mode, the system shall not enforce real-time stock-negative checks; the stock balance displayed shall carry a "Cached — may not reflect live stock" disclaimer.

## 6.3 Synchronisation

**FR-POS-058** — When internet connectivity is restored, the system shall automatically detect reconnection within 30 seconds and begin synchronising queued offline transactions to the server; synchronisation shall process transactions in chronological order of their device-local timestamp.

**FR-POS-059** — When a transaction sync conflict is detected (e.g., item price changed server-side during offline period), the system shall log the conflict with the device value and server value, apply the server value for GL posting purposes, and flag the transaction for supervisor review.

**FR-POS-060** — When synchronisation completes, the system shall post all synced transactions to the Inventory and GL modules as a single batch, generate any pending EFRIS submissions, and display a sync summary to the cashier showing the number of transactions synced and any flagged conflicts.

**FR-POS-061** — The system shall guarantee at-least-once delivery for EFRIS fiscal submissions during sync; if an EFRIS submission fails, the system shall retry with exponential back-off (maximum 5 retries) and log each attempt with the EFRIS API response code.

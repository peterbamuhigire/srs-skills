# Terminal Management

## 2.1 Terminal Registration

**FR-POS-001** — When a Super Admin registers a new POS terminal, the system shall assign a unique terminal ID in the format `TERM-NNN`, record the terminal name, assigned branch, assigned cashier(s), and hardware descriptor (device model and OS); the terminal shall remain inactive until explicitly activated.

**FR-POS-002** — When a Super Admin activates a terminal, the system shall generate a one-time pairing code valid for 15 minutes; the cashier device shall present this code during first-launch setup to bind the device to the terminal record.

**FR-POS-003** — The system shall support deactivation of a terminal; a deactivated terminal shall not accept new transactions, and any open session on that terminal shall be flagged for supervisor review before forced closure.

## 2.2 Multi-Terminal and Multi-Branch

**FR-POS-004** — The system shall support multiple concurrent active terminals per branch, with each terminal maintaining an independent till session; transactions from all terminals shall be visible in the branch manager's consolidated sales dashboard.

**FR-POS-005** — The system shall enforce that a cashier may operate only one active terminal session at a time across all branches of the tenant; opening a second session shall require the first session to be closed by a supervisor.

## 2.3 Terminal Configuration

**FR-POS-006** — Each terminal shall carry a configurable profile defining: receipt printer connection (Bluetooth ESC/POS or network IP), default VAT rate, customer display enabled/disabled, and restaurant/retail mode selection.

**FR-POS-007** — The system shall allow a Super Admin to push terminal configuration updates remotely; the updated configuration shall take effect at the start of the next terminal session, not mid-session.

## 2.4 Restaurant / Table Mode

**FR-POS-008** — When a terminal is configured in restaurant mode, the system shall display a table layout grid configured by the Super Admin; each table shall show its current status: Available, Occupied, or Bill Pending.

**FR-POS-009** — When a cashier assigns an order to a table, the system shall link all subsequent items added to the order with that table number and the ordering time, maintaining an open order until payment is completed or the order is voided.

**FR-POS-010** — The system shall support split-bill functionality in restaurant mode: when a user splits a table bill, the system shall allow the user to assign individual line items or a proportional split to up to 10 sub-bills, each payable independently using any supported payment method.

**FR-POS-011** — The system shall support "rounds" ordering in restaurant mode: a round links additional item orders placed at intervals to the same open table order without creating a new sale transaction.

**FR-POS-012** — When a table order is transferred from one table to another, the system shall record the transfer with the original table number, destination table number, acting user, and UTC timestamp.

# Till Management

## 5.1 Session Open

**FR-POS-041** — When a cashier opens a terminal session, the system shall require entry of an opening float amount; the system shall record the float as the starting cash balance for the session, along with the cashier identity, terminal ID, and UTC session open timestamp.

**FR-POS-042** — The system shall prevent a cashier from processing transactions until an active session with a confirmed opening float exists on the terminal.

## 5.2 Cash In and Cash Out

**FR-POS-043** — The system shall allow a supervisor to record a cash-in event (adding cash to the till mid-session) or a cash-out event (removing cash from the till) at any point during an active session; each event shall require a mandatory reason, the supervisor's authentication, and the amount, and shall update the running session cash balance.

## 5.3 X-Report (Intra-Shift)

**FR-POS-044** — The system shall generate an X-report on cashier request at any time during an active session; the X-report shall display: opening float, total sales by payment method, total returns, cash-in/cash-out events, and the expected cash balance; the X-report shall not close the session.

## 5.4 Session Close and Z-Report

**FR-POS-045** — When a cashier closes a session, the system shall require entry of the actual counted cash amount; the system shall compute: $CashVariance = CountedCash - ExpectedCash$ where $ExpectedCash = OpeningFloat + CashSales + CashIn - CashOut - CashRefunds$.

**FR-POS-046** — When a session is closed, the system shall generate a Z-report displaying: session ID, cashier name, terminal ID, session open and close timestamps, sales totals by payment method, return totals, cash variance, and all transaction line counts; the Z-report shall be printable and stored immutably.

**FR-POS-047** — When the cash variance exceeds the configurable cash variance threshold (default: UGX 5,000), the system shall flag the variance, prevent automatic session closure, and require a supervisor override with a written justification before proceeding.

## 5.5 Shift Handover

**FR-POS-048** — The system shall support shift handover: when cashier A ends their session and cashier B begins on the same terminal, the system shall require cashier A to close their session first, the supervisor to confirm the handover, and cashier B to enter the opening float for the new session.

**FR-POS-049** — The system shall generate a handover record capturing: outgoing cashier, incoming cashier, terminal ID, expected cash balance at handover, confirmed handover amount, and supervisor identity.

## 5.6 Daily Summary Reports

**FR-POS-050** — The system shall provide a daily sales summary per branch consolidating all terminal sessions for the day, showing: total transactions, total revenue by payment method, total VAT collected, total returns, and net revenue; this report shall be used as the input for the day-end GL posting.

**FR-POS-051** — The system shall provide a cashier performance report per period showing: total transactions processed, total revenue, average transaction value, and void count per cashier.

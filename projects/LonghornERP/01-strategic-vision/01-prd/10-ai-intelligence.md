# AI Intelligence Module — Intelligent Business Add-On

## Positioning

The AI Intelligence Module is a paid add-on sold separately from the core LonghornERP subscription. It is off by default. Account owners activate it — feature by feature — from **Settings → AI Intelligence**. Every feature described here is explained in terms that a Finance Director, Managing Director, or Business Owner will understand immediately, without requiring a data science background.

**Pricing (indicative):** Professional plan add-on — UGX 100,000/month; Business plan add-on — UGX 300,000/month; Enterprise plan add-on — UGX 800,000/month. All plans include a configurable monthly token budget enforced at 80% consumption alert and 100% hard stop.

---

## AI Feature 1: Know Your Cash Position for the Next 90 Days

**Who benefits:** Finance Directors, Business Owners, CFOs.

**The problem it solves:** A managing director approves a large equipment purchase on Monday, not knowing that a VAT remittance is due to URA on Thursday and payroll runs on Friday. The bank account is fine today but will be negative by the weekend. Cash flow crises almost always come from a failure to look forward — not from a failure of profitability.

**What it does:** Every morning, the system reads the AR aging (when customers are expected to pay based on their payment history), the AP schedule (when supplier invoices fall due), payroll dates, loan repayment schedules, and tax payment dates. It produces a 90-day rolling cash flow forecast with three curves: Best Case, Base Case, and Worst Case. The Finance Director sees exactly which weeks are at risk — before they arrive.

**Why owners pay for it:** One cash flow crisis averted, one emergency overdraft not drawn, one supplier relationship not strained — the AI module recovers its cost in the first month.

**Pricing tier:** Professional and above.

**FR-AI-001** — see SRS Module 15, FR-AI-001 for full technical specification.

---

## AI Feature 2: Catch Unusual Journal Entries Before the Auditor Does

**Who benefits:** Finance Directors, External Auditors, Managing Directors.

**The problem it solves:** GL fraud typically involves small, repeated unusual journal entries: round numbers, unusual account combinations, entries posted at unusual times. Manual review of a 10,000-line journal register is impractical. Fraud is usually discovered by accident or by external auditors — not by internal controls.

**What it does:** After each posting cycle, the system analyses all new journal entries against four behavioural classifiers: unusual posting times, unusual debit/credit account combinations for this tenant, round-number amounts without a source document, and entries posted by users whose role does not normally post to those accounts. Flagged journals appear in the Finance Director's Anomaly Inbox with a brief explanation. The Finance Director reviews and clears or escalates each flag.

**Why owners pay for it:** Internal fraud detection that would otherwise require hiring an internal auditor is automated. The Audit Log module already captures every action — this module makes sense of it.

**Pricing tier:** Business and Enterprise.

**FR-AI-002** — see SRS Module 15, FR-AI-002 for full technical specification.

---

## AI Feature 3: Know What to Reorder Before Your Shelves Run Out

**Who benefits:** Procurement Managers, Inventory Controllers, Branch Managers.

**The problem it solves:** A procurement officer orders inventory based on intuition and the last stockout they remember. They over-order slow-moving items — tying up cash — and under-order fast movers, causing stockouts. Neither problem is visible until it is already a problem.

**What it does:** Every Sunday, the system analyses the last 90 days of sales velocity per product per branch, applies a seasonal adjustment based on same-period performance in prior years, and generates a Reorder Recommendation report. For each product below or near its reorder level, the system recommends an exact order quantity calculated to cover 45 days of adjusted demand without over-ordering. The procurement officer reviews and converts recommendations to Purchase Requisitions with one click.

**Why owners pay for it:** In a 10-branch business, optimising inventory typically frees 15–25% of the working capital tied up in stock. Over-stocked slow-movers and stockout revenue losses are eliminated simultaneously.

**Pricing tier:** Professional and above.

**FR-AI-003** — see SRS Module 15, FR-AI-003 for full technical specification.

---

## AI Feature 4: Flag the Customers Most Likely to Pay Late — Before You Give Them More Credit

**Who benefits:** Credit Controllers, Sales Managers, Finance Directors.

**The problem it solves:** A salesperson opens a new sales order for a customer with a credit limit. Unknown to the salesperson, this customer has paid late repeatedly and currently has a 60-day overdue invoice. The credit controller only finds out when the order is already confirmed.

**What it does:** Before a new credit sale is confirmed for any customer, the system runs the customer through a Risk Scorecard — payment history, average days-to-pay, current overdue balance, and trend direction — and produces a Green / Amber / Red rating. Amber ratings display a warning that the sales team can acknowledge. Red ratings require explicit Sales Manager approval before the order is confirmed; the approval reason is logged in the audit trail.

**Why owners pay for it:** Bad debt reduction. One prevented bad debt can cover 12 months of subscription fees. Credit teams use the weekly risk ranking to prioritise collection calls.

**Pricing tier:** Growth and above.

**FR-AI-004** — see SRS Module 15, FR-AI-004 for full technical specification.

---

## AI Feature 5: Get a Plain-English Explanation of What the Numbers Mean

**Who benefits:** Managing Directors, Board Members, Business Owners who are not accountants.

**The problem it solves:** A business owner receives a 12-page financial report every month. They read the revenue line and the profit line, skip the rest, and sign the acknowledgement. They are missing important signals buried in the numbers — signals that would prompt them to act.

**What it does:** On the 5th of each month, after the preceding month's accounts are finalised, the system reads the P&L, Balance Sheet, and Cash Flow and generates a 3-paragraph Management Commentary in plain English: what changed versus last month, what changed versus the same month last year, and the 3 most important things the owner should act on this month. No accounting jargon. The commentary is sent as a push notification to the Finance Director and Managing Director, with a link to the full report.

**Why owners pay for it:** It makes the monthly accounts intelligible to every level of management. Board packs become readable. The owner can discuss the business with confidence.

**Pricing tier:** Business and Enterprise.

**FR-AI-005** — see SRS Module 15, FR-AI-005 for full technical specification.

---

## AI Intelligence Module Packaging Summary

| Feature | Professional (UGX 100K/mo) | Business (UGX 300K/mo) | Enterprise (UGX 800K/mo) |
|---|---|---|---|
| Cash Flow Intelligence | Yes | Yes | Yes |
| Demand Forecasting and Reorder | Yes | Yes | Yes |
| Debtor Default Risk Scoring | Yes | Yes | Yes |
| GL Anomaly Detection | — | Yes | Yes |
| Narrative Financial Reports | — | Yes | Yes |

**All features are off by default within the purchased plan.** The account owner enables each feature individually from **Settings → AI Intelligence**.

---
title: "Maduuka Frequently Asked Questions"
---

# Maduuka Frequently Asked Questions

## Getting Started

**What devices can I use Maduuka on?**

You can use Maduuka on any Android phone running Android 8.0 (Oreo) or newer with at least 2 GB of RAM. Maduuka also works in any modern web browser — Chrome, Firefox, Edge, or Safari — on a laptop, desktop, or tablet. No installation is required for the web version.

**How much does Maduuka cost?**

Maduuka is a monthly subscription. Pricing depends on your plan (number of users and branches). Visit your Maduuka account page under **Settings** → **Subscription** to see current plan prices in your local currency.

**Can I try Maduuka before paying?**

Yes. Every new account gets a 14-day free trial with full access to all Phase 1 features. No credit card is required to start the trial. At the end of 14 days, you choose a plan and subscribe to continue.

**What happens to my data if I cancel?**

Your data is not deleted immediately. When you cancel, your account enters a 30-day grace period. During this period you can export all your data (go to **Settings** → **Data Export**). After 30 days, your data is permanently deleted from Maduuka's servers. Export your data before the grace period ends.

**How do I add more users to my account?**

1. Go to **Settings** → **Users**.
2. Tap **Invite User**.
3. Enter the new user's email address and select their role.
4. Tap **Send Invite**.

The new user receives an email with a link to set their password and log in. The number of users you can add depends on your subscription plan.

---

## POS and Sales

**Can I use Maduuka without internet?**

Yes. Maduuka is built to work offline. You can open a session, make sales, accept cash payments, and print receipts — all without internet. The only features that require internet are mobile money payments (MTN MoMo, Airtel Money) and sending receipts via SMS or WhatsApp.

**What happens to sales made offline?**

Sales made while offline are saved on your phone. When your phone connects to the internet, Maduuka automatically syncs all offline sales to the server. You do not need to do anything. A small sync indicator at the top of the screen turns green when all data is uploaded.

**Can I use my own receipt printer?**

Yes. Maduuka supports 80mm Bluetooth thermal receipt printers (for Android) and USB thermal printers (for the web). Printers confirmed to work include Epson TM-T82, Xprinter XP-58, and TP-Link 80mm thermal printers. Any printer that uses the ESC/POS command standard will work. See the Installation Guide for pairing steps.

**How do I handle a customer who wants to pay half cash half MoMo?**

Use the split payment feature. On the payment screen, tap **Split Payment**. Select **Cash**, enter the cash amount. Tap **Add Another Payment**, select **MTN MoMo** or **Airtel Money**, and enter the remaining amount. Maduuka confirms when the total matches the sale amount.

**What is a POS session and why do I need to open one?**

A POS session is a record of one cashier's shift. It tracks the opening cash float, every sale made during the shift, and the closing cash count. Sessions allow the business owner to see exactly what each cashier sold, collected, and whether the cash in the till matches the records. You must open a session before you can make a sale.

**Can I refund a sale from a previous day?**

Yes, but this requires manager or owner permission. Go to **More** → **Sales History**, find the sale, and tap **Refund**. Enter the reason and the amount to refund (full or partial). The manager must enter their approval PIN. The refund creates a new transaction in the records.

**How do I find a receipt I printed last week?**

Go to **More** → **Sales History**. Use the date filter to select last week's date range. Search by customer name, product, or transaction amount to narrow the results. Tap the sale to view or reprint the receipt.

**What is the receipt gap report?**

The receipt gap report checks whether any receipt numbers are missing in sequence. In a legitimate business, every sale gets a sequential receipt number. If numbers are skipped, it may mean a sale was deleted after printing. Find this report under **More** → **Reports** → **Receipt Gap Report**.

---

## Inventory

**How does FIFO/FEFO work — why does the system pick a specific batch?**

FIFO means First In, First Out — the batch you received first is sold first. FEFO means First Expired, First Out — the batch expiring soonest is sold first. For products with expiry dates, Maduuka uses FEFO so you do not accidentally hold stock past its expiry date. For products without expiry dates, Maduuka uses FIFO. You do not choose the batch at the POS — Maduuka selects it automatically.

**What is a stock count and how often should I do it?**

A stock count is when you physically count every item on your shelves and compare the number to what Maduuka's records show. This confirms that no stock has been lost, stolen, or miscounted. For most retail shops, a full stock count once a month is sufficient. High-value or high-movement categories can be counted weekly.

**Can I track products that expire?**

Yes. When you add a product, turn on **Track Expiry Dates**. When you receive that product from a supplier, enter the batch number and expiry date. Maduuka sends you alerts 30, 60, or 90 days before expiry, depending on your settings (set under **Settings** → **Inventory Settings**).

**What happens when stock goes to zero — can I still sell?**

By default, Maduuka will warn you when stock hits zero but will still allow the sale if your business owner has enabled **Allow Sales Below Zero Stock**. If this setting is off, the product will be greyed out in the POS and you cannot add it to a cart. Check your setting under **Settings** → **Inventory Settings** → **Negative Stock**.

**How do I transfer stock between my two branches?**

Go to **Stock** → **Stock Transfers** → **New Transfer**. Select the sending branch and the receiving branch. Add the products and quantities. Tap **Send Transfer**. The stock shows as "In Transit" until the receiving branch confirms delivery. See the Inventory section of the User Manual for full steps.

---

## Payments and Mobile Money

**Which mobile money providers does Maduuka support?**

Maduuka Phase 1 supports MTN Mobile Money (Uganda) and Airtel Money (Uganda). Additional mobile money gateways for other African countries will be added when Maduuka expands to those markets.

**What happens if a MoMo payment times out?**

If the customer does not confirm the MoMo prompt within 90 seconds, the payment request expires. Maduuka shows a **"Payment Timed Out"** message. Ask the customer to check their phone. You can tap **Retry Payment** to send a new prompt, or switch to a different payment method (cash, Airtel Money). No money is deducted from the customer when a payment times out.

**Can customers pay using Visa or Mastercard?**

Card payments (Visa, Mastercard) are not available in Phase 1. They are planned for a future update. Currently accepted methods are: Cash, MTN MoMo, Airtel Money, and credit accounts.

**Is it safe to process payments through Maduuka?**

Yes. Maduuka does not store MoMo PINs or any payment credentials. Mobile money transactions go directly through the MTN and Airtel official APIs using encrypted connections. Your business MoMo account credentials are stored using industry-standard encryption. Maduuka is also protected by 2-factor authentication for owner accounts.

---

## HR and Payroll

**How does Maduuka calculate PAYE?**

Maduuka uses the Uganda Revenue Authority (URA) income tax bands as defined in the Uganda Income Tax Act. The PAYE calculation is: monthly chargeable income = gross salary minus NSSF employee contribution. Tax is then applied at the correct band (0% up to UGX 235,000; 10% on the next UGX 265,000; 20% on the next UGX 500,000; 30% above UGX 1,000,000 per month). Maduuka keeps these bands updated. You do not calculate PAYE manually.

**Can I pay salaries directly through Maduuka?**

Yes, for mobile money. After approving a payroll run, you can initiate bulk salary payments to staff MTN MoMo or Airtel Money numbers directly from Maduuka. For bank transfers, Maduuka generates a bank payment file in the format accepted by Centenary Bank, Stanbic, ABSA, KCB, Equity, and Dfcu, which you upload directly to your bank's online portal.

**What happens if I made a mistake in a payroll that is already approved?**

An approved payroll cannot be edited — this protects the integrity of your financial records. To correct it, create an **adjustment** in the following month's payroll: add a one-off earning or deduction line item that corrects the error. Add a note explaining that it is a correction for the previous month. Your accountant can advise on the correct adjustment amount.

**How do staff receive their payslips?**

After approving a payroll run, go to the payroll run and tap **Send Payslips**. You can send payslips via WhatsApp (as a PDF to each staff member's phone) or by email. Staff do not need a Maduuka account to receive their payslip — it is delivered directly to their WhatsApp or inbox.

---

## Data and Security

**Is my business data backed up?**

Yes. Maduuka automatically backs up all data on its servers. Backups run multiple times per day. Your data is not stored only on your phone — it is always on the Maduuka cloud servers. If you lose or break your phone, your data is safe. Simply log in on a new device.

**Can my competitor see my data if they also use Maduuka?**

No. Each business account is completely separated from all other accounts. Maduuka uses a multi-tenant architecture where your data is stored in an isolated partition. No other business — whether they use Maduuka or not — can access your sales, customers, or any other information.

**What happens if my phone is stolen — can someone access my Maduuka account?**

If your phone is stolen, take these steps immediately:

1. From another device, go to your Maduuka URL and log in.
2. Go to **Settings** → **Security** → **Connected Devices**.
3. Find the stolen phone in the list and tap **Revoke Access**.

This logs the stolen phone out of Maduuka immediately. The thief cannot access your account even if the Maduuka app is still open on the stolen phone.

Enable 2FA (two-factor authentication) on your account — this adds a second layer of protection so your password alone is not enough to log in.

**How do I export all my data?**

1. Go to **Settings** → **Data Export**.
2. Select the data you want to export: Sales, Products, Customers, Suppliers, Expenses, Staff, or All Data.
3. Select the date range.
4. Tap **Export**. Maduuka prepares a CSV file.
5. When ready, tap **Download** to save the file to your device.

For a full account export (all data, all history), select **All Data** and leave the date range blank. This is recommended when cancelling your subscription.

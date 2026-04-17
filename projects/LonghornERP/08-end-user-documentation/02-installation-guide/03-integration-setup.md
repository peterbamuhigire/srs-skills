# Step 3: Set Up Integrations

Integrations connect Longhorn ERP to external systems such as tax authority portals, mobile payment providers, and your email server. Configure only the integrations that apply to your business. Each integration can be enabled or disabled at any time from **Settings > Integrations**.

---

## URA EFRIS — Uganda Electronic Fiscal Receipting and Invoicing System

*This integration is mandatory for VAT-registered businesses operating in Uganda.* It submits every tax invoice to the Uganda Revenue Authority (URA) in real time.

`[CONTEXT-GAP: GAP-001 — URA EFRIS API credential issuance process and exact portal URL pending confirmation from URA. Contact efris@ura.go.ug for the current registration procedure.]`

1. Obtain your EFRIS credentials from the URA taxpayer portal. You will need:
   - Device Number (issued by URA).
   - Taxpayer Identification Number (TIN).
   - EFRIS API Key.
2. In Longhorn ERP, navigate to **Settings > Integrations > URA EFRIS**.
3. Enter your **Device Number**, **TIN**, and **API Key** in the corresponding fields.
4. Click **Test Connection**. A green status message confirms that Longhorn ERP can communicate with the URA EFRIS server.
5. Navigate to **Settings > Modules > Sales** and enable the **EFRIS Submission** toggle.

Once enabled, every posted sales invoice is automatically submitted to URA and a QR-coded fiscal receipt is appended to the printed document.

---

## MTN MoMo and Airtel Money

This integration allows customers to pay invoices directly via mobile money. Payments are automatically matched to open invoices in Longhorn ERP.

`[CONTEXT-GAP: GAP-011 — MTN MoMo and Airtel Money developer portal registration URLs and approval timelines pending confirmation. Refer to the respective developer portals for current onboarding requirements.]`

### MTN MoMo

1. Register a business account on the MTN MoMo developer portal and obtain your API Key, Secret, and Subscription Key.
2. In Longhorn ERP, navigate to **Settings > Integrations > Mobile Money > MTN MoMo**.
3. Enter your **API Key**, **Secret**, and **Subscription Key**.
4. Set **Environment** to **Sandbox** for testing or **Production** for live transactions.
5. Click **Test Transaction** and authorise a UGX 100 test payment on your MTN line.
6. Confirm the test payment appears in **Accounting > Bank Transactions** before switching to Production.

### Airtel Money

1. Register a business account on the Airtel Money developer portal and obtain your Client ID and Client Secret.
2. Navigate to **Settings > Integrations > Mobile Money > Airtel Money**.
3. Enter your **Client ID** and **Client Secret**.
4. Set **Environment** to **Sandbox**, then run a UGX 100 test transaction.
5. Confirm the transaction reconciles correctly, then set **Environment** to **Production**.

*Do not switch either integration to Production until the test transaction has reconciled successfully in the accounts.*

---

## Email (SMTP)

Longhorn ERP sends invoices, purchase orders, payslips, and system notifications by email. By default it uses Chwezi Core's shared mail server. To send from your own domain (e.g., `billing@yourcompany.com`), configure your own SMTP server.

1. Navigate to **Settings > Email Configuration**.
2. Enter the following details provided by your email service provider:

   | Field | Example |
   |---|---|
   | **SMTP Server** | smtp.yourprovider.com |
   | **Port** | 587 |
   | **Username** | billing@yourcompany.com |
   | **Password** | Your SMTP password |
   | **Encryption** | TLS (recommended) |

3. Click **Send Test Email** and enter a recipient address.
4. Confirm the test email arrives in the recipient's inbox.
5. Click **Save Configuration**.

If the test email does not arrive, check your SMTP credentials and ensure your mail provider allows third-party SMTP access. Contact your IT administrator or email provider for assistance.

---
title: "Maduuka Installation and Setup Guide"
---

# Maduuka Installation and Setup Guide

This guide covers everything you need to do to install Maduuka, connect your hardware, and configure your business for the first time.

---

## Section 1: Android App Installation

### Minimum Requirements

Before you install, confirm your phone meets these requirements:

- **Operating system:** Android 8.0 (Oreo) or newer
- **RAM:** 2 GB or more
- **Free storage:** 500 MB or more
- **Camera:** Required for barcode scanning
- **Bluetooth:** Required for connecting a receipt printer

Maduuka is designed to run on affordable Android phones. It is tested on devices as low-cost as a UGX 250,000 Android handset.

### How to Install from Google Play Store

1. Open the **Google Play Store** app on your Android phone.
2. Tap the search bar at the top.
3. Type `Maduuka` and tap the search icon.
4. Tap the **Maduuka — Business POS** app in the results.
5. Tap **Install**.
6. Wait for the download to complete. The app installs automatically.
7. Tap **Open** to launch Maduuka for the first time.

### First Launch: Grant Required Permissions

When Maduuka opens for the first time, it will ask for two permissions. Both are required for the app to work correctly.

**Camera permission (for barcode scanning):**

1. A pop-up appears: *"Maduuka wants to access your camera."*
2. Tap **Allow**.
3. Without camera permission, you cannot scan barcodes at the POS.

**Bluetooth permission (for receipt printer):**

1. A second pop-up appears: *"Maduuka wants to use Bluetooth."*
2. Tap **Allow**.
3. Without Bluetooth permission, you cannot connect a wireless receipt printer.

*If you accidentally tapped "Deny" for either permission, go to your phone's **Settings** → **Apps** → **Maduuka** → **Permissions** and turn on Camera and Bluetooth manually.*

### How to Log In for the First Time

1. On the Maduuka welcome screen, enter your **Email** or **Phone Number**.
2. Enter the **Password** you set when your account was created. (If your business owner created your account, they will give you a temporary password.)
3. Tap **Log In**.
4. If it is your first login with a temporary password, Maduuka will ask you to set a new password. Enter a password you will remember and tap **Save Password**.

### How to Set Up a Bluetooth Thermal Receipt Printer

Maduuka works with most 80mm Bluetooth thermal printers. Confirmed compatible models include Epson TM-T82, Xprinter XP-58, and TP-Link 80mm thermal printers.

**Step 1: Pair your printer with your phone.**

1. Turn on the receipt printer.
2. On your Android phone, go to **Settings** → **Bluetooth**.
3. Make sure Bluetooth is turned on.
4. Tap **Pair new device** or **Scan**.
5. Your printer appears in the list (for example, `Xprinter-58` or `BT-Printer`).
6. Tap the printer name to pair. If prompted for a PIN, enter `0000` or `1234` (check your printer's manual).
7. Your phone shows **"Paired"** next to the printer name.

**Step 2: Connect the printer in Maduuka.**

1. Open Maduuka and go to **More** → **Settings** → **Receipt Printer**.
2. Tap **Search for Printers**.
3. Your paired printer appears in the list. Tap it to connect.
4. Tap **Print Test Receipt**. A test receipt prints. If it prints correctly, your printer is set up.

### Offline Mode

Offline mode is turned on by default. You do not need to enable it. When your phone has no internet connection, Maduuka automatically saves all work locally and syncs when internet returns.

To check that offline mode is active, go to **More** → **Settings** → **Sync Settings**. You will see **"Offline mode: Enabled."**

### How to Check Sync Status

- A **green cloud icon** at the top of the screen means all data is synced.
- An **orange cloud icon** means there is data waiting to sync (your phone may be offline).
- A **spinning icon** means Maduuka is actively syncing.

To force a manual sync when you reconnect to internet, pull down on the home screen (swipe down from the top of the screen and release).

---

## Section 2: Web App Access

### Requirements

You do not install anything for the web version. All you need is a modern web browser:

- Chrome 90 or newer (recommended)
- Firefox 90 or newer
- Microsoft Edge 90 or newer
- Safari 14 or newer

Maduuka does not support Internet Explorer.

### Accessing the Web App

Open your browser and go to your business Maduuka URL. This URL was provided when your account was created — for example, `yourshop.maduuka.com`. Bookmark this address so you can find it quickly.

### How to Add Maduuka to Your Home Screen on Android (PWA Install)

If you prefer using the web app on Android without going through a browser, you can install it as a Progressive Web App (PWA). It will appear on your home screen like a regular app.

1. Open **Chrome** on your Android phone.
2. Go to your Maduuka URL.
3. Log in.
4. Tap the **three dots** (menu) at the top right of Chrome.
5. Tap **Add to Home screen**.
6. Type a name for the shortcut (for example, `Maduuka`) and tap **Add**.
7. The Maduuka icon appears on your home screen. Tap it to open Maduuka directly.

### How to Connect a USB Receipt Printer (Web)

1. Connect your USB thermal printer to your computer using a USB cable.
2. Make sure the printer is turned on.
3. In Maduuka (web), go to **More** → **Settings** → **Receipt Printer** → **USB Printer**.
4. When you print a receipt, your browser's print dialog opens. Select your thermal printer from the list of printers.
5. Set paper size to **80mm** (or **Roll** if listed) and margins to **None**.
6. Click **Print**.

*Tip: Save these print settings in your browser to avoid setting them every time.*

### How to Connect a USB Barcode Scanner (Web)

1. Plug your USB barcode scanner into your computer's USB port.
2. No driver installation is required. The scanner works as keyboard input — when you scan a barcode, the number is typed into whatever field is selected.
3. In the POS screen, click the **Search** field to make sure it is active.
4. Scan a product barcode. Maduuka finds and adds the product automatically.

---

## Section 3: Setting Up Your Business (First Time)

Complete these steps in order when logging in as Business Owner for the first time.

1. Go to **Settings** → **Business Profile**. Enter your business name, physical address, and TIN (Tax Identification Number). Upload your business logo. Tap **Save**.

2. Go to **Settings** → **Tax Settings**. Confirm the VAT rate. For Uganda, the standard rate is **18%**. Select whether your product prices are tax-inclusive (the price already includes VAT) or tax-exclusive (VAT is added on top at the point of sale). Tap **Save**.

3. Go to **Settings** → **Currency**. Select **UGX — Ugandan Shilling**, or select your country's currency if you are outside Uganda. Tap **Save**.

4. Go to **Settings** → **Payment Accounts**. Add each account your business uses:
   - Tap **Add Account** → select **Cash Till** → name it (e.g., `Main Till`).
   - Tap **Add Account** → select **MTN MoMo** → enter your MTN Mobile Money business number.
   - Tap **Add Account** → select **Airtel Money** → enter your Airtel Money business number.
   - Tap **Save** after each account.

5. Go to **Inventory** → **Products**. Add your first products one by one using the **+** button. Alternatively, import products in bulk: tap **Import** → **Download Template**, fill in the CSV template in Excel, and upload it.

6. Go to **Settings** → **Users**. Tap **Invite User** for each staff member. Enter their email and select their role (Cashier, Stock Keeper, etc.). They will receive an email invitation to set their password.

---

## Section 4: Troubleshooting

**App will not open or crashes on launch**

1. Press and hold the Maduuka icon on your phone.
2. Tap **Force Stop** (or go to **Settings** → **Apps** → **Maduuka** → **Force Stop**).
3. Go to **Settings** → **Apps** → **Maduuka** → **Storage** → **Clear Cache**.
4. Reopen Maduuka. Do not tap **Clear Data** — this deletes any unsynced local data.

**Cannot scan barcodes**

1. Go to **Settings** → **Apps** → **Maduuka** → **Permissions**. Confirm **Camera** is set to **Allow**.
2. Make sure there is enough light. Barcode scanning in dim light is unreliable.
3. Hold the phone steady and point the camera directly at the barcode — do not angle it.
4. If the barcode is faded or damaged, type the barcode number manually in the search bar.

**Receipt printer not connecting via Bluetooth**

1. Confirm the printer is turned on and has paper loaded.
2. On your phone, go to **Settings** → **Bluetooth**. Find your printer in the list of paired devices.
3. Tap the printer name and tap **Forget** (unpair).
4. Repeat the pairing process from Section 1: pair the printer in your phone's Bluetooth settings, then reconnect in Maduuka under **Settings** → **Receipt Printer**.
5. If the printer still does not connect, try turning the printer off, waiting 10 seconds, and turning it back on before pairing.

**Sales showing "pending sync" for a long time**

1. Check that your phone or computer has an active internet connection. Open a browser and try loading a website.
2. If you have internet, open Maduuka and pull down on the home screen to trigger a manual sync.
3. If sales are still pending after 5 minutes with a confirmed internet connection, go to **More** → **Settings** → **Sync Settings** → **Force Full Sync**.
4. If the problem persists, contact Maduuka support and provide your business name and the date of the affected sales.

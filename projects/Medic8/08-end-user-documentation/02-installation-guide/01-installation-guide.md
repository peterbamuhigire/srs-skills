# Medic8 Installation and Onboarding Guide

**Version:** 1.0
**Product:** Medic8 Healthcare Management System
**Date:** 2026-04-03

---

## 1 Cloud SaaS Setup (Primary)

Medic8 is a cloud-based system. For most facilities, there is nothing to install on your computers. You access Medic8 through your web browser, just like you would access email or a banking website.

### 1.1 No Installation Required

Medic8 runs entirely in the cloud. You do not need to buy a server, install software, or hire an IT technician. All you need is a device with a web browser and an internet connection (as slow as 256 Kbps works for clinical use).

### 1.2 Account Provisioning

There are two ways to get started:

- **Self-register:** Go to `https://medic8.com` and click **Start Free Trial**. Enter your facility name, your name, email address, and phone number. You receive a confirmation email within minutes.
- **Contact Medic8 sales:** Call, email, or WhatsApp the Medic8 sales team. They set up your account and walk you through the first steps.

### 1.3 Facility Setup Wizard Walkthrough

After your account is created, you log in for the first time and the system guides you through a 5-step setup wizard. The target is to have your facility ready for its first patient within 2-4 hours.

1. **Facility Profile:** Enter your facility name, physical address, phone number, email, and timezone (default: East Africa Time, UTC+3). Upload your facility logo. This logo appears on receipts, reports, and printed documents.
2. **Module Activation:** Choose which modules to turn on. Start with the modules your facility needs immediately. Phase 1 modules include:
   - Patient Registration and Master Index
   - Outpatient Department (OPD)
   - Pharmacy and Dispensary
   - Laboratory Information System (LIS)
   - Billing and Revenue Management
   - Appointments and Scheduling
3. **Staff Accounts:** Create accounts for your team. For each person, enter their name, email, phone number, and assign a role. Available roles: Facility Admin, Doctor, Clinical Officer, Nurse/Midwife, Pharmacist, Lab Technician, Receptionist, Records Officer, Cashier, Insurance Clerk, Accountant, Store Keeper, and Auditor. Each person receives an email with instructions to set their password.
4. **Price List:** Enter the fees for your services. The price list is organised by category: Consultation, Laboratory, Pharmacy, Radiology, Procedures, and Bed Charges. You can set different prices for different patient categories (Adult, Paediatric, Staff, VIP, Indigent/Sponsored).
5. **Review and Finish:** Check all your entries. Click **Complete Setup**. Your facility is now live.

### 1.4 Mobile App Download

The Medic8 mobile app is for patients to view their records, book appointments, and make payments. Staff can also use it for quick access to the system on the go.

- **Android:** Open the Google Play Store. Search for "Medic8." Tap **Install**.
- **iPhone:** Open the Apple App Store. Search for "Medic8." Tap **Get**.

### 1.5 First Login and Password Setup

1. Open your web browser and go to `https://app.medic8.com`.
2. Enter the email address that was used when your account was created.
3. Click **Set Password** (for first-time login) or enter your existing password.
4. Create a strong password with at least 8 characters, including uppercase and lowercase letters, a number, and a special character.
5. If your role requires two-step verification (Super Admin, Facility Admin, Accountant, and Auditor roles require it; it is optional for clinical staff), set up your verification method now. The system sends a code to your phone each time you log in.
6. Select your facility from the list (if you work at more than one facility).
7. You are now on your home screen, ready to begin.

---

## 2 Local Server Setup (Optional -- for Facilities with No Internet)

Some facilities in remote areas have no reliable internet connection. For these facilities, Medic8 can run on a small local server inside the facility. The local server handles all clinical workflows independently and synchronises data to the cloud whenever internet is available.

*This setup requires a technical person. If your facility does not have IT support, contact the Medic8 team for assisted installation.*

### 2.1 Hardware Requirements

You need one of the following small computers to act as the local server:

- **Intel NUC** (or similar mini PC): at least 4 GB of RAM and a 64 GB solid-state drive (SSD). This is a small box about the size of a paperback book.
- **Raspberry Pi 4:** 4 GB RAM model with a 64 GB microSD card or external SSD. This is even smaller and very affordable.

You also need:

- A UPS (uninterruptible power supply) to keep the server running during power outages.
- A WiFi router to create a local wireless network for facility devices (phones, tablets, laptops).

### 2.2 Ubuntu Server 22.04 Installation

1. Download Ubuntu Server 22.04 LTS from `https://ubuntu.com/download/server`.
2. Write the downloaded file to a USB flash drive using a tool such as Rufus or Balena Etcher.
3. Insert the USB drive into the NUC or Raspberry Pi and boot from it.
4. Follow the on-screen instructions to install Ubuntu Server. Use the default settings unless you have specific requirements.
5. When installation is complete, the server restarts and you see a command-line prompt.

### 2.3 Medic8 Server Package Installation

Medic8 provides an automated installation tool (called an Ansible playbook) that sets up everything for you:

1. Connect the server to the internet (temporarily) to download the installation package.
2. Run the following command:
   ```
   curl -sL https://install.medic8.com/local | bash
   ```
3. The script installs all required software (web server, database, application code) automatically. This takes approximately 15-30 minutes depending on your internet speed.
4. When the script finishes, it displays the local URL where Medic8 is running (for example, `https://medic8.local`).

### 2.4 Network Configuration

1. Connect a WiFi router to the server using an Ethernet cable.
2. Configure the router to create a local WiFi network (for example, network name: "Medic8-Clinic").
3. Connect all facility devices (laptops, tablets, phones) to this WiFi network.
4. Devices on the network can access Medic8 by opening a browser and going to `https://medic8.local`.

### 2.5 Sync Agent Configuration

The sync agent handles data transfer between the local server and the cloud:

1. When internet is available (even briefly), the sync agent automatically sends data to the cloud and downloads any updates.
2. To configure sync settings, log in to Medic8 as Facility Admin and go to **Settings > Sync**.
3. Set the sync mode:
   - **Automatic:** Syncs whenever internet is detected. Recommended.
   - **Manual:** You click **Sync Now** to trigger synchronisation. Use this if your internet is metered and you want to control data usage.
4. The system detects power restoration and immediately begins syncing the offline queue.

### 2.6 SSL Certificate for Local HTTPS

The installation script automatically generates a local SSL certificate so that all connections between facility devices and the server are encrypted, even on the local network. No additional configuration is needed.

If your browser shows a certificate warning when accessing the local server, this is normal for a self-signed certificate. Click **Advanced** and then **Proceed** to continue safely.

---

## 3 Workstation Setup

This section covers setting up the computers and peripherals that staff will use daily.

### 3.1 Supported Browsers

Install one of the following browsers on each workstation:

| Browser | Minimum Version |
|---|---|
| Google Chrome | 90 |
| Mozilla Firefox | 88 |
| Microsoft Edge | 90 |
| Apple Safari | 14 |

Chrome is recommended for the best experience. Keep your browser updated to the latest version.

### 3.2 Minimum Screen Resolution

- Minimum: 1024 x 768 pixels (standard laptop screen)
- Recommended: 1920 x 1080 pixels (Full HD)
- For clinical workstations (doctor, nurse), a dual-monitor setup is recommended. Use one monitor for the patient record and the other for writing clinical notes, viewing lab results, or looking up drug information.

### 3.3 Barcode Scanner Setup (USB HID)

Barcode scanners are used in the laboratory (scanning sample labels) and at the reception (scanning patient ID cards). Medic8 works with any USB barcode scanner that uses the HID (Human Interface Device) standard. This means the scanner acts like a keyboard and types the barcode into the active field.

1. Plug the USB barcode scanner into a free USB port on the computer.
2. The computer recognises it automatically. No driver installation is needed.
3. In Medic8, click on any search or ID field.
4. Scan a barcode. The scanned value appears in the field, as if you had typed it.
5. Test the scanner by scanning a known barcode and verifying that the correct value appears.

### 3.4 Thermal Receipt Printer Setup (80mm ESC/POS)

Thermal printers are used for printing patient receipts and dispensing labels. Medic8 supports 80mm thermal printers that use the ESC/POS command language (this is the standard used by most receipt printers).

1. Connect the printer to the computer using a USB cable.
2. Install the printer driver provided by the manufacturer (for example, Epson TM-T20, Star TSP143, or POS-80).
3. In Medic8, go to **Settings > Printing**.
4. Select the receipt printer from the list of installed printers.
5. Print a test receipt by clicking **Test Print**.
6. If the test receipt looks correct (facility name, logo, sample text), the setup is complete.

### 3.5 Fingerprint Scanner Setup

Fingerprint scanners are used for biometric patient registration (optional). This allows patients to be identified by their fingerprint instead of carrying an ID card.

1. Connect the fingerprint scanner to the computer using a USB cable.
2. Install the driver provided by the scanner manufacturer. Follow the manufacturer's installation instructions.
3. In Medic8, go to **Settings > Biometrics** and enable fingerprint registration.
4. Test the scanner by enrolling a test fingerprint and verifying that it is recognised on a subsequent scan.

---

## 4 Mobile Device Setup

### 4.1 Android Devices

- **Operating system:** Android 7.0 (API level 24) or newer
- **Memory (RAM):** 1 GB minimum
- **Supported phones:** The app is designed to work on budget phones up to 5 years old
- **Storage:** At least 100 MB of free space for the app and cached data

#### Installation Steps

1. Open the Google Play Store.
2. Search for "Medic8."
3. Tap **Install**.
4. Open the app.
5. Log in with your email/username and password.
6. Select your facility from the list.
7. The app downloads initial data for your facility (this may take a few minutes on the first login).

### 4.2 iOS Devices

- **Operating system:** iOS 15.0 or newer
- **Supported devices:** iPhone 6s or newer, iPad (5th generation) or newer

#### Installation Steps

1. Open the Apple App Store.
2. Search for "Medic8."
3. Tap **Get**.
4. Open the app.
5. Log in and select your facility.

### 4.3 Offline Mode Configuration

The Medic8 mobile app can work without an internet connection. Your most recent health records and patient data are stored on the device and sync automatically when connectivity returns.

To configure offline mode:

1. Open the app and go to **Settings > Offline**.
2. Enable **Offline Mode**.
3. Select how much data to store locally (last 7 days, 30 days, or 90 days).
4. Tap **Sync Now** to download the data immediately.

### 4.4 Data Usage Settings (Data-Lite Mode)

If you use mobile data (not WiFi) and want to reduce data consumption:

1. Open the app and go to **Settings > Data**.
2. Enable **Data-Lite Mode**. This compresses all data transfers and avoids downloading large files (such as radiology images) over mobile data.
3. Large images download only on WiFi.
4. The app is designed to operate on 2G and 3G networks.

---

## 5 Initial Configuration Checklist

After completing the setup, use this checklist to confirm that everything is ready. Tick off each item as you complete it.

- [ ] Facility profile configured (name, address, logo, timezone)
- [ ] Staff accounts created with correct roles assigned
- [ ] Price list configured with fees for all active services
- [ ] Drug formulary reviewed and customised for your facility
- [ ] Lab test catalogue reviewed with correct reference ranges
- [ ] Insurance schemes added (if your facility processes insurance claims)
- [ ] Receipt template configured (header text, footer text, logo)
- [ ] SMS gateway configured (Africa's Talking) for appointment reminders and notifications
- [ ] Mobile money API keys configured for MTN MoMo and/or Airtel Money (if your facility accepts mobile money payments)
- [ ] Backup schedule verified (automatic daily backups are enabled by default; confirm backup destination and retention period)

### After Completing the Checklist

1. Register a test patient and walk through the full workflow: registration, triage, consultation, prescription, dispensing, lab request, result entry, and billing.
2. Collect a test payment and print a test receipt.
3. Run the daily reconciliation to verify that the billing totals match.
4. If everything works correctly, you are ready to begin seeing real patients.
5. If you encounter any issues, contact Medic8 support via WhatsApp, email (support@medic8.com), or phone.

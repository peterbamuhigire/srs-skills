# Section 1: Web Browser Access

The BIRDC ERP web application runs on BIRDC's own server at Nyaruzinga. No software installation is needed to use the web application — only a supported browser.

---

## 1.1 Supported Browsers

Use one of the following browsers for the best experience:

| Browser | Minimum Version | Notes |
|---|---|---|
| Google Chrome | 110 or later | Recommended |
| Mozilla Firefox | 110 or later | Fully supported |
| Microsoft Edge | 110 or later | Fully supported |
| Safari | 16 or later | Supported on Mac and iPad |

*Internet Explorer is not supported. Do not use it to access the BIRDC ERP.*

---

## 1.2 Accessing the System URL

1. Open your supported browser.
2. Type the BIRDC ERP address in the address bar: `http://erp.birdc.local` (on the BIRDC internal network) or the external URL provided by the IT Administrator.
3. Press Enter. The login page appears.

*If the login page does not load, confirm that your computer is connected to the BIRDC network and that the server is running. Contact the IT Administrator if the problem persists.*

---

## 1.3 First-Time Login

1. On the login page, enter the **Username** and **Password** given to you by the IT Administrator.
2. Click **Login**.
3. The system prompts you to change your password on first login.
4. Enter your current (temporary) password in the **Current Password** field.
5. Enter a new password in the **New Password** field. Your password must be at least 10 characters long and include at least 1 number and 1 special character.
6. Re-enter the new password in the **Confirm Password** field.
7. Click **Set Password**. Your new password is saved.
8. The system logs you in and takes you to your home dashboard.

---

## 1.4 Password Setup Requirements

All passwords must meet the following rules:

- Minimum length: 10 characters.
- Must include at least 1 uppercase letter.
- Must include at least 1 number.
- Must include at least 1 special character (for example: `!`, `@`, `#`, `$`).
- Cannot be the same as your last 5 passwords.
- Expires every 90 days. The system will prompt you to change it before expiry.

---

## 1.5 Two-Factor Authentication (2FA) — Director and Finance Roles

Users in the **Director**, **Finance Director**, and **Finance Manager** roles are required to configure two-factor authentication (2FA). This is enforced on first login.

1. After setting your password, the system shows a 2FA setup screen.
2. Open the **Google Authenticator** app on your phone (download it from Google Play Store if you do not have it).
3. Tap the **+** button in Google Authenticator.
4. Tap **Scan a QR code**.
5. Point your phone camera at the QR code shown on the ERP screen.
6. Google Authenticator adds the BIRDC ERP account and shows a 6-digit code.
7. Enter the 6-digit code in the **Verification Code** field on the ERP screen.
8. Click **Verify**. 2FA is now active on your account.

From this point on, every login requires your password plus the 6-digit code from Google Authenticator.

*If you lose your phone and cannot access your 2FA codes, contact the IT Administrator to reset your 2FA. Only the IT Administrator can perform a 2FA reset.*

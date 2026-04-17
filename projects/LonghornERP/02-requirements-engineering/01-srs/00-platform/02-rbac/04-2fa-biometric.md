## 4. Two-Factor Authentication, Biometric Integration, and USSD Access

### 4.1 TOTP 2FA Enrollment

**FR-RBAC-060:** The system shall generate a TOTP shared secret and present it as both a QR code and a plain-text key when a user initiates 2FA enrollment from their account security settings; the QR code shall be compatible with Google Authenticator and Authy (RFC 6238, SHA-1, 6-digit code, 30-second window).

**FR-RBAC-061:** The system shall complete 2FA enrollment and activate TOTP authentication for the user's account when the user submits a valid TOTP code generated from the displayed shared secret; if the code is invalid, enrollment shall not complete and the system shall display a retry prompt.

**FR-RBAC-062:** The system shall generate exactly 10 single-use backup codes at the time of successful 2FA enrollment; the codes shall be displayed once and shall not be retrievable in plain text after the user dismisses the display screen. The user shall be advised to store these codes securely.

**FR-RBAC-063:** The system shall mark a backup code as used and prevent any further use of that code when it is submitted as a 2FA alternative credential; if all 10 backup codes have been used, the user shall be directed to contact an administrator or re-enroll 2FA.

### 4.2 2FA Enforcement

**FR-RBAC-064:** The system shall prompt a user for their TOTP code or a backup code on every login attempt when 2FA is enabled for their account, after the username and password have been validated successfully; login shall not proceed until the second factor is verified.

**FR-RBAC-065:** The system shall allow a tenant administrator to mandate 2FA enrollment for one or more specific roles; when 2FA is mandated for a role, any user assigned to that role who has not yet enrolled shall be forced through the 2FA enrollment flow before accessing any other part of the application.

**FR-RBAC-066:** The system shall disable 2FA for a user's account when an administrator explicitly removes the 2FA requirement for that user, or when the user deactivates 2FA from their account settings (if self-service deactivation is permitted by the tenant policy).

### 4.3 Biometric Login Integration (Zkteco)

**FR-RBAC-067:** The system shall receive biometric authentication events from Zkteco hardware devices via the configured integration endpoint when an employee presents their fingerprint or face to the device; each event payload shall include the device identifier, the employee identifier, and the UTC timestamp.

**FR-RBAC-068:** The system shall record an attendance entry in the HR & Attendance module and optionally create an authenticated session for the corresponding user when a valid Zkteco biometric event is received and the employee identifier maps to an active user account.

**FR-RBAC-069:** The system shall reject a Zkteco biometric event and log a warning in the Audit Log when the event payload fails signature verification, the device identifier is not registered to the tenant, or the employee identifier does not map to an active user account.

**FR-RBAC-070:** The system shall allow a tenant administrator to configure, per user, whether a successful biometric event from a Zkteco device creates an authenticated application session in addition to recording attendance; the default shall be attendance-only (no session creation).

### 4.4 USSD Access for Warehouse Workers

**FR-RBAC-071:** The system shall expose a USSD menu via Africa's Talking for module code `USER_MGMT` when a registered warehouse worker dials the configured USSD shortcode from their feature phone; the session shall authenticate the caller by matching their registered mobile number to an active user account in the tenant's USSD-enabled user list.

**FR-RBAC-072:** The system shall provide a stock lookup function via USSD when an authenticated USSD session user selects the stock inquiry option and enters a valid item code; the system shall return the item name and current stock quantity for the user's assigned branch in a response that fits within a single USSD screen (≤ 182 characters).

**FR-RBAC-073:** The system shall allow an authenticated USSD session user to confirm a pending Goods Receipt Note (GRN) when the user selects the GRN confirmation option, enters a valid GRN reference number, and confirms the action; the system shall mark the GRN as confirmed by the warehouse worker and record the confirmation in the Audit Log.

**FR-RBAC-074:** The system shall terminate a USSD session and display an "Unauthorised" message when the caller's mobile number does not match any active USSD-enabled user in the tenant's user list, or when the tenant has not activated USSD access.

**FR-RBAC-075:** The system shall terminate a USSD session and log the event when the session exceeds 3 minutes of inactivity or when the Africa's Talking gateway signals a session close; any unconfirmed GRN action in progress shall be discarded and no partial state shall be written.

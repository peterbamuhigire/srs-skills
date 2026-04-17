# Section 5: Offline Mode Guide

BIRDC operates in Bushenyi, where internet connectivity can be intermittent. The ERP is designed so that the most critical field operations continue without interruption when internet is unavailable.

---

## 5.1 What Works Offline

The following apps and features continue to function with no internet connection:

| App / Feature | Works Offline | Notes |
|---|---|---|
| Factory Gate POS | Yes | Sales are stored locally. Sync on reconnect. |
| Sales Agent App — POS | Yes | Offline sales queue up and sync when online. |
| Sales Agent App — cash balance | Yes (last synced value) | Balance updates after next sync. |
| Farmer Delivery App — farmer registration | Yes | New farmer records upload on sync. |
| Farmer Delivery App — delivery recording | Yes | Deliveries queue and sync. |
| Farmer Delivery App — receipt printing | Yes | Bluetooth printer does not need internet. |
| Warehouse App — barcode scanning | Yes | Scans queue and sync. |
| Warehouse App — stock counts | Yes | Count data uploads on sync. |
| Factory Floor App — production entry | Yes | Entries queue and sync. |

---

## 5.2 What Requires Internet

The following features require an active internet connection:

| Feature | Why Internet Is Required |
|---|---|
| Financial reports and Trial Balance | Data is fetched live from the server. |
| EFRIS submission | Requires real-time connection to URA. |
| Remittance verification | Supervisor must confirm against live bank records. |
| Executive Dashboard App | Dashboard data is fetched live. |
| Payroll approval | Requires posting to the live GL. |
| User management and role changes | System security operations require the server. |
| Backup and restore | Backup is written to the server. |

*EFRIS submissions for offline POS transactions are queued and submitted automatically when internet connectivity is restored. There is no manual step required.*

---

## 5.3 Sync Indicator

Every Android app shows a sync status icon in the top status bar:

| Icon | Meaning |
|---|---|
| Green cloud | Online. Synced. All data is up to date. |
| Orange cloud with arrow | Online. Sync in progress. |
| Grey cloud with line through it | Offline. Transactions are queuing locally. |
| Red cloud with exclamation mark | Sync error. See Section 5.5. |

The web application shows a banner at the top of the screen if the server loses its internet connection: "EFRIS submissions paused — internet connection lost."

---

## 5.4 Manual Sync Trigger

The apps sync automatically when connectivity is detected. To trigger a sync manually:

1. Open the app.
2. Tap the menu icon (three lines, top left).
3. Tap **Sync Now**.
4. A progress bar shows the sync status.
5. When complete, the status icon turns green.

---

## 5.5 What to Do If Sync Shows an Error

If the sync status icon turns red (error):

1. Tap the red cloud icon.
2. The error message describes the problem. Common errors:
   - "Server unreachable" — check your internet connection.
   - "Authentication failed" — your session has expired. Log out and log back in.
   - "Conflict detected" — a record was changed on both the phone and the server. The app will ask which version to keep.
3. Resolve the issue described in the error message.
4. Tap **Retry Sync**.

If the error persists after retrying, contact the IT Administrator with a screenshot of the error message.

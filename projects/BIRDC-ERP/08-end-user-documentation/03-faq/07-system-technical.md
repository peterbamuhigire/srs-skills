# Topic 7: System and Technical

---

**Q34. How do I reset a user's password?**

Only the IT Administrator can reset another user's password. To do so:

1. Log in as IT Administrator.
2. Click **System Administration** then **Users**.
3. Search for the user by name or username.
4. Click on the user's record.
5. Click **Reset Password**.
6. The system sends the user a temporary password to their registered email address.
7. The user logs in with the temporary password and is prompted to set a new one immediately.

Users in the Director, Finance Director, and Finance Manager roles also have two-factor authentication (2FA). If they cannot access their 2FA codes (for example, lost phone), the IT Administrator must also reset their 2FA from the same user record. The IT Administrator should verify the identity of the user requesting the reset before proceeding.

---

**Q35. What do I do if EFRIS submission keeps failing?**

EFRIS submissions fail when the ERP cannot reach the URA EFRIS server, or when the submitted document contains a data error that URA rejects.

1. Click **Finance** then **EFRIS** then **Submission Queue**.
2. Find the failed submission and click on it.
3. Read the error code and message from URA. Common errors:
   - "TIN not found" — the customer's TIN entered on the invoice is incorrect.
   - "Duplicate FDN" — the same document has already been submitted. Check if it was submitted manually outside the system.
   - "Network timeout" — the internet connection was interrupted. Click **Retry** — the system will resubmit.
4. For data errors, correct the underlying invoice and resubmit.
5. If the error message is unclear or the problem persists after retrying, contact the system support contact at techguypeter.com with a screenshot of the error code.

*EFRIS submissions for offline POS transactions are queued automatically and submitted when internet is restored. These do not require manual intervention unless the queue shows an error.*

---

**Q36. How do I check when the last backup was taken?**

1. Log in as IT Administrator.
2. Click **System Administration** then **Backup Management**.
3. The **Last Backup** field shows the date and time of the most recent successful backup.
4. The backup history shows a log of all backups: date, time, size, and status (Success or Failed).

Backups are scheduled to run automatically every night. If the last backup shows a **Failed** status or is more than 24 hours old, investigate immediately. Contact the system support contact at techguypeter.com if you cannot identify the cause of the backup failure.

---

**Q37. The Android app is showing "sync pending" — what does that mean?**

"Sync pending" means the app has transactions or records stored on your phone that have not yet been uploaded to the main server. This is normal when you have been working offline. The sync happens automatically when you connect to the internet. To check status and manually trigger a sync:

1. Open the app.
2. Tap the menu icon (three lines, top left).
3. Tap **Sync Status**. You can see how many records are waiting to sync and when the last successful sync happened.
4. Tap **Sync Now** to force an immediate sync.

If "sync pending" persists even when you have a good internet connection, try logging out and logging back in. If the problem continues, contact the IT Administrator — do not uninstall the app, as this will delete the unsynced records.

---

**Q38. Who do I contact when there is a system problem?**

Follow this escalation path:

1. **First:** Check this FAQ document for a solution.
2. **Second:** Contact your immediate supervisor or the IT Administrator within BIRDC.
3. **Third:** If the IT Administrator cannot resolve the issue, contact the system support contact: Peter Bamuhigire, ICT Consultant, at techguypeter.com.

When contacting support, provide:

- Your name and role.
- The name of the app or module where the problem occurred.
- A description of what you were trying to do.
- The exact error message shown (take a screenshot if possible).
- The date and time the problem occurred.

This information allows the support team to resolve the issue without needing to ask you a series of follow-up questions.

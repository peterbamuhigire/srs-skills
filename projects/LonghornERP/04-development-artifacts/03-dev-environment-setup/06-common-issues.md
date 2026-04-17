# Common Issues and Troubleshooting

This section documents the setup problems reported most frequently and their remediation steps.

## Apache Returns a 500 Internal Server Error

*This is almost always a `mod_rewrite` or `AllowOverride` misconfiguration.*

1. Confirm `mod_rewrite` is enabled. On WAMP, open the tray icon > **Apache** > **Apache modules** and verify `rewrite_module` is checked. On Linux, run `sudo a2enmod rewrite && sudo systemctl restart apache2`.
2. Open the VirtualHost configuration block for `longhorn-erp.local` and confirm the `<Directory>` block contains `AllowOverride All`. If it reads `AllowOverride None`, the `.htaccess` routing rules are silently ignored.
3. Check the Apache error log for the specific error. On WAMP, the log is at `C:\wamp64\logs\apache_error.log`. On Linux, it is at `/var/log/apache2/longhorn-erp-error.log`.

## PHP Extension Missing

1. Open a browser and navigate to a PHP file containing `<?php phpinfo(); ?>` served by Apache (not the CLI). Locate the extension name in the output. If it is absent, the extension is either not installed or not enabled for the Apache SAPI.
2. Open the correct `php.ini` — the path is shown in the `phpinfo()` output under **Loaded Configuration File**. Add or uncomment the relevant `extension=<name>` line.
3. Restart Apache and reload `phpinfo()` to confirm the extension now appears.

## Database Connection Refused

1. Verify MySQL is running. On WAMP, the tray icon must show all services green. On Linux, run `sudo systemctl status mysql`.
2. Open `.env` and confirm `DB_HOST`, `DB_PORT`, `DB_USER`, and `DB_PASSWORD` are correct. A common error is leaving the values from `.env.example` without substituting real credentials.
3. Connect to MySQL directly from the terminal to confirm the user and password are valid:
   ```
   mysql -u longhorn_user -p longhorn_erp
   ```
   If this fails, the user does not exist or the password is wrong — recreate the user as described in Section 3, step 9.

## Session Not Persisting (Repeated Login Redirects)

*This is always caused by `SESSION_SECURE=true` on a non-HTTPS local environment.*

1. Open `.env` and set `SESSION_SECURE=false`. The session cookie name `LONGHORN_ERP_SESSION` uses `SameSite=Strict`; on HTTP, a secure-flagged cookie is never transmitted, so every request appears unauthenticated.
2. Clear all browser cookies for `longhorn-erp.local` and log in again.

## Migration Errors

1. The most common cause is insufficient database privileges. Connect to MySQL as root and verify:
   ```sql
   SHOW GRANTS FOR 'longhorn_user'@'localhost';
   ```
   The user requires `CREATE`, `ALTER`, `DROP`, `INDEX`, `INSERT`, `UPDATE`, `DELETE`, and `SELECT` on the `longhorn_erp` database.
2. If a migration fails partway through, the schema may be in a partially applied state. Inspect `migration_log` (or the equivalent tracking table) to identify the last successful migration, then re-run `php run_migrations.php`. The runner is idempotent and skips already-applied migrations.

## CSRF Token Mismatch Errors

*CSRF token errors present as rejected POST requests with a 403 response or a "Token mismatch" message.*

1. Clear all browser cookies for `longhorn-erp.local`. A stale session cookie from a previous PHP session will carry an expired CSRF token.
2. Confirm `SESSION_NAME` in `.env` matches the value expected by the application. If the cookie name was changed after a session was established, the old cookie is ignored and a new session — with a new token — is issued on the next request, invalidating any forms already open in the browser.
3. If the error persists in a development environment after clearing cookies, check that the session save path is writable by the Apache process user.

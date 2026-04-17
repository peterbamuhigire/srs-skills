# Windows Setup (WAMP)

The system uses WAMP as the recommended local development stack on Windows. WAMP provides Apache 2.4, MySQL 9.1, and PHP 8.3 in a single installer with a tray-based version switcher. Complete the following steps in order.

## Installation and Configuration

1. Download the WAMP installer from wampserver.com and run it. Accept the default installation path (`C:\wamp64\`). Allow the installer to install all Visual C++ redistributables when prompted.

2. Open the WAMP tray icon, navigate to **PHP** > **Version**, and select **8.3.x**. WAMP will restart Apache automatically.

3. Open the active `php.ini` file (WAMP tray > **PHP** > **php.ini**) and verify that the following lines are present and uncommented (remove the leading `;` if present):
   - `extension=pdo_mysql`
   - `extension=mbstring`
   - `extension=gd`
   - `extension=zip`
   - `extension=openssl`
   - `extension=fileinfo`

   Save `php.ini` and restart all WAMP services.

4. Open a terminal and clone the repository into the WAMP web root:

   ```
   git clone <repository-url> C:\wamp64\www\longhorn-erp
   ```

5. In the WAMP Apache Virtual Hosts configuration file (`C:\wamp64\bin\apache\apache2.4.x\conf\extra\httpd-vhosts.conf`), add the following block:

   ```
   <VirtualHost *:80>
       ServerName longhorn-erp.local
       DocumentRoot "C:/wamp64/www/longhorn-erp/public"
       <Directory "C:/wamp64/www/longhorn-erp/public">
           Options Indexes FollowSymLinks
           AllowOverride All
           Require all granted
       </Directory>
   </VirtualHost>
   ```

   `AllowOverride All` is required so that Apache processes the `.htaccess` rules that enable `mod_rewrite` routing.

6. Open `C:\Windows\System32\drivers\etc\hosts` as Administrator and append the following line:

   ```
   127.0.0.1 longhorn-erp.local
   ```

7. Confirm that `mod_rewrite` is enabled. In WAMP, open **Apache** > **Apache modules** from the tray icon and verify `rewrite_module` is checked. If not, click it to enable it; WAMP will restart Apache.

8. In the terminal, navigate to the project root and install all PHP dependencies:

   ```
   composer install
   ```

   This installs all `require` and `require-dev` packages, including PHPStan 1.11, PHP CS Fixer 3.64, and PHPUnit 11.2, into `vendor/`.

9. Copy the environment template and populate all required variables:

   ```
   copy .env.example .env
   ```

   Edit `.env` as described in Section 4. At minimum, set `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `APP_URL`, `JWT_SECRET`, `MYSQL_BIN_PATH`, and `MYSQLDUMP_BIN_PATH`.

10. Connect to MySQL and create the application database:

    ```sql
    CREATE DATABASE longhorn_erp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```

    Grant the database user configured in `.env` full privileges on this database.

11. Run the versioned migration files to build the schema:

    ```
    php run_migrations.php
    ```

    The migration runner is idempotent; re-running it on an already-migrated database is safe.

12. Open `http://longhorn-erp.local/` in a browser. A successful setup displays the Longhorn ERP login screen. A 500 error indicates an Apache or PHP configuration issue; see Section 6 for troubleshooting steps.

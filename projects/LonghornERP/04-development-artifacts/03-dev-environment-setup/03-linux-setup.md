# Linux Setup (Ubuntu / Debian)

This procedure mirrors the production Apache-on-Linux environment and is the recommended setup for Continuous Integration pipelines and for developers working on Linux. All commands assume a Debian-based distribution (Ubuntu 22.04 LTS or later). Run commands as a user with `sudo` privileges.

## Installation and Configuration

1. Update the package list and install Apache 2.4:

   ```
   sudo apt update
   sudo apt install apache2
   ```

   Verify Apache is running: `sudo systemctl status apache2`.

2. Add the Ondrej PPA for PHP 8.3 and install PHP with all required extensions:

   ```
   sudo add-apt-repository ppa:ondrej/php
   sudo apt update
   sudo apt install php8.3 php8.3-mysql php8.3-mbstring php8.3-gd php8.3-zip php8.3-xml php8.3-curl
   ```

   Verify the active PHP version: `php -v`. The output must show `8.3.x`.

3. Add the official MySQL APT repository and install MySQL 9.x:

   ```
   wget https://dev.mysql.com/get/mysql-apt-config_0.8.33-1_all.deb
   sudo dpkg -i mysql-apt-config_0.8.33-1_all.deb
   sudo apt update
   sudo apt install mysql-server
   ```

   During installation, select the MySQL 9.x series when prompted. Secure the installation after setup: `sudo mysql_secure_installation`.

4. Enable the `mod_rewrite` Apache module:

   ```
   sudo a2enmod rewrite
   sudo systemctl restart apache2
   ```

5. Clone the repository to the web root and set correct file ownership:

   ```
   sudo git clone <repository-url> /var/www/longhorn-erp
   sudo chown -R www-data:www-data /var/www/longhorn-erp
   sudo chmod -R 755 /var/www/longhorn-erp
   ```

6. Create a new Apache VirtualHost configuration file:

   ```
   sudo nano /etc/apache2/sites-available/longhorn-erp.conf
   ```

   Paste the following content:

   ```
   <VirtualHost *:80>
       ServerName longhorn-erp.local
       DocumentRoot /var/www/longhorn-erp/public
       <Directory /var/www/longhorn-erp/public>
           Options Indexes FollowSymLinks
           AllowOverride All
           Require all granted
       </Directory>
       ErrorLog ${APACHE_LOG_DIR}/longhorn-erp-error.log
       CustomLog ${APACHE_LOG_DIR}/longhorn-erp-access.log combined
   </VirtualHost>
   ```

   Enable the site and reload Apache:

   ```
   sudo a2ensite longhorn-erp.conf
   sudo systemctl reload apache2
   ```

   `AllowOverride All` is required so that Apache processes the `.htaccess` rules that enable `mod_rewrite` routing.

7. Install Composer globally and then install PHP dependencies from the project root:

   ```
   curl -sS https://getcomposer.org/installer | php
   sudo mv composer.phar /usr/local/bin/composer
   cd /var/www/longhorn-erp
   composer install
   ```

8. Copy the environment template and populate all required variables:

   ```
   cp .env.example .env
   nano .env
   ```

   Edit `.env` as described in Section 4. At minimum, set `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `APP_URL`, and `JWT_SECRET`. On Linux, `MYSQL_BIN_PATH` and `MYSQLDUMP_BIN_PATH` typically resolve to `/usr/bin`.

9. Connect to MySQL and create the application database:

   ```
   sudo mysql -u root -p
   ```

   ```sql
   CREATE DATABASE longhorn_erp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'longhorn_user'@'localhost' IDENTIFIED BY '<strong-password>';
   GRANT ALL PRIVILEGES ON longhorn_erp.* TO 'longhorn_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

   Then run the versioned migration files:

   ```
   php run_migrations.php
   ```

10. Add the local hostname entry to `/etc/hosts`:

    ```
    echo "127.0.0.1 longhorn-erp.local" | sudo tee -a /etc/hosts
    ```

    Open `http://longhorn-erp.local/` in a browser. A successful setup displays the Longhorn ERP login screen. Check `/var/log/apache2/longhorn-erp-error.log` for any startup errors.

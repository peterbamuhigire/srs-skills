# Environment Configuration

The system uses `vlucas/phpdotenv` 5.6 to load runtime configuration from a `.env` file in the project root. Copy `.env.example` to `.env` and populate every variable before running the application.

*Never commit `.env` to version control. The file is listed in `.gitignore`. Committing it exposes database credentials and the JWT signing secret.*

## Variable Reference

| Variable | Description | Example |
|---|---|---|
| `DB_HOST` | MySQL host | `localhost` |
| `DB_PORT` | MySQL port | `3306` |
| `DB_NAME` | Database name | `longhorn_erp` |
| `DB_USER` | Database user | `longhorn_user` |
| `DB_PASSWORD` | Database password | `[strong password]` |
| `APP_ENV` | Environment mode (`development` or `production`) | `development` |
| `APP_DEBUG` | Enable verbose error output. Set to `false` in production. | `true` |
| `APP_URL` | Application base URL (no trailing slash) | `http://longhorn-erp.local` |
| `SESSION_NAME` | Session cookie name | `LONGHORN_ERP_SESSION` |
| `SESSION_SECURE` | Require HTTPS for the session cookie. Set to `false` on non-HTTPS local dev. | `false` |
| `JWT_SECRET` | 256-bit secret key used to sign mobile API JWT tokens (firebase/php-jwt 7.0) | `[256-bit random key]` |
| `SUPERADMIN_EMAIL` | Email address of the initial super admin account | `admin@chwezicore.com` |
| `MYSQL_BIN_PATH` | Absolute path to the directory containing the `mysql` binary | `C:/wamp64/bin/mysql/mysql9.1.0/bin` |
| `MYSQLDUMP_BIN_PATH` | Absolute path to the directory containing the `mysqldump` binary | `C:/wamp64/bin/mysql/mysql9.1.0/bin` |

## Notes on Specific Variables

**`APP_ENV`** controls framework behaviour and error verbosity. The only supported values are `development` and `production`. Running `production` on a local machine suppresses all error output; use `development` during all local work.

**`SESSION_SECURE`** must be `false` on any environment not served over HTTPS. Setting it to `true` on a plain HTTP local setup will cause the browser to refuse to send the session cookie, resulting in repeated login failures.

**`JWT_SECRET`** must be a cryptographically random value of at least 256 bits (32 bytes). Generate one with:

```
php -r "echo bin2hex(random_bytes(32));"
```

**`MYSQL_BIN_PATH` / `MYSQLDUMP_BIN_PATH`** are used by the database backup and restore utilities. On Linux these typically point to `/usr/bin`. On Windows with WAMP, the path includes the MySQL version directory as shown in the example column.

# Prerequisites

All software listed below must be installed and operational before following the platform-specific setup procedures in Sections 2 and 3.

## Required Software

| Dependency | Minimum Version | Purpose |
|---|---|---|
| PHP | 8.3.0 | Server-side runtime (strict types, PSR-4) |
| MySQL | 9.1.0 | Primary data store (InnoDB, utf8mb4) |
| Apache | 2.4 | HTTP server with mod_rewrite |
| Composer | latest stable | PHP dependency manager |
| Git | 2.x | Source control |
| PHPStan | 1.11 | Static analysis (installed via Composer) |
| PHP CS Fixer | 3.64 | Code style enforcement (installed via Composer) |

Node.js is optional and required only if the project introduces a front-end build pipeline in future iterations.

## Required PHP Extensions

The following extensions must be enabled in `php.ini` before the application will start:

- `pdo_mysql` — PDO driver for MySQL; all database access uses PDO with prepared statements only.
- `mbstring` — multi-byte string functions; required for UTF-8 text handling throughout the platform.
- `gd` — image processing; required by mPDF 8.2 for PDF generation.
- `zip` — archive support; required for export and import file handling.
- `openssl` — cryptographic functions; required for TLS operations and JWT signing via `firebase/php-jwt` 7.0.
- `fileinfo` — MIME-type detection; required for file upload validation.

## Windows Development Environment

WAMP (available at wampserver.com) is the recommended local development stack on Windows. It bundles Apache 2.4, MySQL 9.1, and PHP 8.3 with a tray-based version switcher, eliminating manual path configuration. All Windows setup steps in Section 2 assume WAMP is the installed stack.

## Development Tool Versions

PHPStan 1.11 and PHP CS Fixer 3.64 are not installed globally; they are declared as `require-dev` dependencies in `composer.json` and installed into `vendor/bin/` by running `composer install`. No separate global installation is needed.

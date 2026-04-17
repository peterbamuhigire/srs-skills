# 4. CI/CD Pipeline

## 4.1 GitHub Actions Workflow

The CI/CD pipeline runs on every push to any branch and on every pull request targeting `develop` or `main`. The pipeline has 5 stages executed in sequence. Any stage failure stops the pipeline — downstream stages do not run.

```
push / PR
   │
   ▼
[Stage 1: Lint]
  ├── PHPStan level 8
  └── PHP_CodeSniffer (PSR-12)
   │
   ▼ (on pass)
[Stage 2: Test]
  └── PHPUnit — 80% minimum coverage gate for financial services
   │
   ▼ (on pass)
[Stage 3: Build]
  └── Composer install --no-dev, asset compilation
   │
   ▼ (on pass, on develop/main branches only)
[Stage 4: Deploy to Staging]
  └── SSH deploy to staging server; smoke test
   │
   ▼ (manual approval required)
[Stage 5: Deploy to Production]
  └── SSH deploy to production; health check
```

### Stage 1 — Lint

Two tools run in parallel:

**PHPStan (level 8):**

```yaml
- name: PHPStan Static Analysis
  run: vendor/bin/phpstan analyse src tests --level=8 --no-progress
```

PHPStan level 8 checks include: undefined variables, type mismatches, dead code, missing return types, and unchecked return values. A level 8 failure blocks the PR.

**PHP_CodeSniffer (PSR-12):**

```yaml
- name: PHP_CodeSniffer
  run: vendor/bin/phpcs --standard=PSR12 src/
```

Code style violations are reported as errors — not warnings. The linter does not auto-fix in CI; the developer must run `phpcbf` locally before pushing.

### Stage 2 — Test

```yaml
- name: PHPUnit
  run: vendor/bin/phpunit --coverage-clover coverage.xml
- name: Coverage Gate
  run: |
    php scripts/check-coverage.php coverage.xml 80 \
      BirdcErp\\Application\\Finance \
      BirdcErp\\Application\\Sales \
      BirdcErp\\Application\\Payroll \
      BirdcErp\\Application\\AgentDistribution
```

The 80% coverage gate applies to these namespaces (financial services):

- `BirdcErp\Application\Finance` — GL posting, journal entries, financial statements
- `BirdcErp\Application\Sales` — invoice lifecycle, EFRIS submission
- `BirdcErp\Application\Payroll` — gross-to-net, PAYE, NSSF, LST
- `BirdcErp\Application\AgentDistribution` — commission calculation, FIFO remittance allocation

Coverage below 80% in any of these namespaces fails the pipeline.

### Stage 3 — Build

```yaml
- name: Composer Install (production)
  run: composer install --no-dev --optimize-autoloader
- name: Build Assets
  run: npm run build
```

### Stage 4 — Deploy to Staging

Runs automatically after Stage 3 passes, on the `develop` branch only. Uses SSH deployment with a deployment key stored in GitHub Secrets.

After deployment, a smoke test script runs 5 critical health checks:

1. HTTP 200 on the login page.
2. Database connection successful.
3. EFRIS API credentials valid (dry run).
4. JWT token issue and verify cycle completes.
5. Last database backup timestamp is within 25 hours.

### Stage 5 — Deploy to Production

Requires manual approval from the project consultant or BIRDC IT Administrator via the GitHub Actions approval gate. This gate prevents accidental production deployments. Production deployment only proceeds from the `main` branch.

---

# 5. Security Requirements

## 5.1 Password Hashing

All user passwords are hashed using Argon2id as the preferred algorithm, with bcrypt as the fallback for PHP environments where `sodium` is not available:

```php
$hash = password_hash($plaintext, PASSWORD_ARGON2ID, [
    'memory_cost' => 65536,  // 64 MB
    'time_cost'   => 4,
    'threads'     => 2,
]);
```

Plain-text passwords are never stored, logged, or transmitted in any response body. Password reset tokens are single-use, expire in 1 hour, and are stored as a SHA-256 hash of the original token.

## 5.2 SQL Injection Prevention

100% of database queries use PDO prepared statements. String concatenation in SQL queries is architecturally prohibited — the Repository pattern enforces this by providing no mechanism for raw query construction in the Service layer.

Prohibited patterns (rejected at code review):

```php
// PROHIBITED — string concatenation
$pdo->query("SELECT * FROM tbl_invoices WHERE customer_id = " . $customerId);

// PROHIBITED — sprintf interpolation
$pdo->query(sprintf("SELECT * FROM tbl_farmers WHERE name = '%s'", $name));
```

Required pattern:

```php
// REQUIRED — prepared statement
$stmt = $pdo->prepare("SELECT * FROM tbl_invoices WHERE customer_id = :customer_id");
$stmt->execute([':customer_id' => $customerId]);
```

PHPStan level 8 combined with a custom rule catches string-concatenated SQL patterns in PR reviews.

## 5.3 XSS Prevention

All user-supplied data rendered in HTML views is escaped with `htmlspecialchars()` using `ENT_QUOTES | ENT_HTML5` and the `UTF-8` charset:

```php
echo htmlspecialchars($userInput, ENT_QUOTES | ENT_HTML5, 'UTF-8');
```

Twig templating (if adopted for views) auto-escapes by default. Raw output (`{{ variable | raw }}`) is prohibited in Twig templates except for pre-sanitised PDF content.

Content Security Policy headers are sent on all web responses:

```
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{random}'; style-src 'self' 'unsafe-inline'; img-src 'self' data:
```

## 5.4 CSRF Protection

All state-changing HTTP requests (POST, PUT, PATCH, DELETE) from the web application require a CSRF token. The token is:

1. Generated per session using `random_bytes(32)` → base64 encoded.
2. Stored in the PHP session (`$_SESSION['csrf_token']`).
3. Embedded in every HTML form as a hidden field: `<input type="hidden" name="_csrf" value="...">`.
4. Validated in middleware before the controller receives the request.

CSRF validation failures return HTTP 419 with the standard error envelope.

Mobile API endpoints use JWT Bearer authentication and are exempt from CSRF token validation (JWT in Authorization header is not vulnerable to CSRF).

## 5.5 Authentication: Rate Limiting and Lockout

| Trigger | Action |
|---|---|
| 5 consecutive failed login attempts (same username) | Account locked for a configurable duration (default: 15 minutes) |
| 5 consecutive failed login attempts (same IP address, across any accounts) | IP rate-limited: subsequent attempts receive a 429 response with `Retry-After` header |
| Account locked | Alert email sent to IT Administrator with username, IP, timestamp |
| 2FA failure (3 attempts) | Session terminated; user must re-authenticate from username/password |

Lockout duration and attempt threshold are configurable by IT Administrator (DC-002) without developer involvement.

## 5.6 Data Encryption in Transit and at Rest

- **In transit:** TLS 1.3 is enforced on the web server. TLS 1.2 and below are disabled. HTTP requests are redirected to HTTPS (301 redirect).
- **At rest — sensitive fields:** The following column types are encrypted at rest using AES-256-GCM before storage:
  - Employee NIN (National Identification Number)
  - Farmer NIN
  - Employee bank account numbers
  - Mobile money account numbers used for salary/farmer payments
  - JWT secret (stored in `.env`, encrypted at OS level)
- **`.env` file:** Never committed to version control. Listed in `.gitignore`. Provided to the production server via a secure out-of-band process.

## 5.7 Database Security

- A dedicated application database user (`birdc_app`) has only the permissions required: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `EXECUTE` (for stored procedures) on the `birdc_erp` database only.
- The MySQL `root` account is disabled from remote access. Root is only accessible locally via socket.
- Database credentials are in `.env` only: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASS`.
- MySQL binary logging is enabled for point-in-time recovery.

## 5.8 Two-Factor Authentication (2FA)

2FA using TOTP (RFC 6238, compatible with Google Authenticator and Authy) is mandatory for:

- Director
- Finance Director
- IT Administrator

2FA is optional for all other roles (users are encouraged to enable it; the prompt appears after first login).

TOTP secrets are stored AES-256 encrypted in `tbl_users.totp_secret`. Recovery codes (8 codes, single-use) are generated at 2FA enrolment and stored as bcrypt hashes.

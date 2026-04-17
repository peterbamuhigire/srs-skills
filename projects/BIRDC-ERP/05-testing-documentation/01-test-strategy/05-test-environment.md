## 4. Test Environment Specification

### 4.1 Web Application — Staging Server

The staging environment must mirror the production hardware and software configuration at BIRDC Nyaruzinga.

| Component | Staging Specification |
|---|---|
| Server | On-premise staging server at BIRDC or equivalent-spec VM |
| Operating System | Same Linux distribution as planned production server |
| Web server | Apache or Nginx with HTTPS (self-signed certificate acceptable for staging) |
| PHP version | PHP 8.3 with `declare(strict_types=1)` |
| Database | MySQL 9.1 InnoDB, utf8mb4, same schema version as production branch |
| Dataset | Representative anonymised BIRDC data: 1,307-account chart of accounts, ≥ 500 test farmer records, ≥ 50 test agent records, sample production orders, payroll records |
| CI/CD | GitHub Actions pipeline connected to staging branch |

### 4.2 Android Mobile Apps

| Requirement | Specification |
|---|---|
| Minimum Android version | Android 8.0 (API level 26) |
| Test devices | Minimum 2 physical Android devices: one flagship (e.g., Samsung Galaxy A-series or equivalent), one low-end device (minimum spec for field agents) |
| Network simulation | Airplane mode for offline testing; throttled Wi-Fi for sync latency testing |
| Bluetooth thermal printer | 80mm ESC/POS printer for Sales Agent App and Farmer Delivery App print tests |
| Barcode scanner | Camera-based ML Kit scanning tested on Warehouse App |

### 4.3 External Integration Sandboxes

| Integration | Sandbox Requirement | Status |
|---|---|---|
| URA EFRIS | URA-provided EFRIS developer sandbox. All integration tests submit to sandbox only. | [CONTEXT-GAP: GAP-001 — Sandbox credentials and endpoint URL not yet confirmed with URA. Obtain sandbox access credentials from URA Developer Portal before Phase 1 integration testing begins.] |
| MTN MoMo | MTN Uganda MoMo API sandbox environment. Test with MTN-provided sandbox API keys. | [CONTEXT-GAP: GAP-002 — MTN MoMo sandbox API key and collection URL not yet confirmed. Obtain from MTN Uganda Developer Portal (momodeveloper.mtn.com) before Phase 1 integration testing.] |
| Airtel Money | Airtel Africa Money API sandbox. | [CONTEXT-GAP: GAP-003 — Airtel Money sandbox credentials not yet confirmed. Obtain from Airtel Africa developer programme before Phase 1 integration testing.] |
| ZKTeco biometric | Physical ZKTeco device deployed at BIRDC; use device SDK in test mode with test fingerprint templates. | To be confirmed at HR module testing phase. |

### 4.4 Environment Promotion Policy

1. All development occurs on feature branches.
2. Automated CI (lint → unit test → integration test) runs on every pull request.
3. Merges to `main` trigger deployment to staging.
4. Manual promotion to production requires Phase Gate sign-off from BIRDC client representative and Peter Bamuhigire.
5. No direct commits to `main` — pull requests only.

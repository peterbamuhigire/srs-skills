# Technology Stack -- Maduuka

## Phase 1: Android

| Layer | Technology |
|---|---|
| Language | Kotlin |
| UI Framework | Jetpack Compose |
| Architecture | MVVM + Clean Architecture (Presentation / Domain / Data layers) |
| Local Database | Room (SQLite) -- offline-first |
| DI | Hilt |
| Background Sync | WorkManager |
| Barcode Scanning | CameraX + ML Kit (EAN-13, EAN-8, Code-128, Code-39, QR) |
| Bluetooth Scanner | HID keyboard profile (external scanners) |
| Bluetooth Printing | 80mm thermal (Epson, Xprinter, TP-Link) |
| Push Notifications | Firebase Cloud Messaging (FCM) |
| Auth Tokens | JWT: 15-min access token + 30-day refresh. AES-256-GCM EncryptedSharedPreferences |
| Biometric Auth | BiometricPrompt API |
| Certificate Pinning | OkHttp CertificatePinner |
| Root Detection | At app launch |
| Maps | Leaflet.js (customer map, Android WebView) |
| PDF Generation | Local PDF render (receipts + payslips) |

## Phase 1: Web

| Layer | Technology |
|---|---|
| Language | PHP 8.3+ |
| Frontend Framework | Bootstrap 5 + Tabler UI |
| JavaScript | Vanilla JS / Alpine.js (minimal) |
| Charts | ApexCharts |
| Maps | Leaflet.js |
| Auth | Session-based + CSRF token on every state-changing form |
| PWA | Service Worker, Web App Manifest |
| Barcode Input | USB/Bluetooth scanner (keyboard HID events), browser camera API |
| Receipt Printing | Browser print dialog (Ctrl+P), USB-connected thermal printer |
| Kitchen Display | Browser auto-refresh URL (no authentication lock after initial session) |
| PDF Export | Server-side PDF generation (HTML to PDF) |

## Shared Backend API

| Layer | Technology |
|---|---|
| API Type | REST (JSON) -- single API consumed by Android, iOS (Phase 2), and Web |
| Platform-Specific Endpoints | None -- one API serves all clients |
| Auth (mobile) | JWT Bearer tokens |
| Auth (web) | Session cookies + CSRF |
| Database | MySQL 8.x |
| File Storage | Wasabi S3-compatible (receipt photos, payslip PDFs, product images) |
| Email | SMTP (configurable per business) |
| SMS / WhatsApp | Africa's Talking API |
| Mobile Money | MTN MoMo Business API + Airtel Money API (Uganda) |

## Phase 2: iOS

| Layer | Technology |
|---|---|
| Language | Swift |
| UI Framework | SwiftUI |
| Architecture | MVVM + Clean Architecture |
| Local Database | Core Data (SQLite) |
| Barcode Scanning | AVFoundation + Vision framework |
| Bluetooth Printing | Core Bluetooth / Raw Print protocol (verify 3 Uganda-market printers before build) |
| Push Notifications | APNs via Firebase |
| Biometric Auth | Face ID / Touch ID |
| Encrypted Storage | Keychain (AES-256) |

## Security Baselines

- TLS 1.3 -- all data in transit
- bcrypt -- all stored passwords
- AES-256 -- all local mobile storage (tokens, sensitive data)
- Certificate pinning -- mobile API calls
- RBAC -- enforced at every API endpoint, not just UI layer
- Immutable audit log -- every create/edit/delete/void/adjustment (actor, timestamp, device, IP)
- 2FA (TOTP) -- available for owner and admin accounts

## Deployment

- Platform: VPS or cloud server (Uganda-region preferred for latency)
- Web server: Nginx
- SSL: Let's Encrypt
- Backup: Daily automated database backup + Wasabi file sync
- CI/CD: GitHub Actions (TBD)

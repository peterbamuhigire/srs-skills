# Technology Stack — Academia Pro

## Backend (Web Application)

- **Language:** PHP 8.2+
- **Framework:** Laravel 11 (Service/Repository pattern; no Eloquent ORM in business logic — use Repository interfaces)
- **Architecture:** Multi-tenant SaaS with row-level tenant isolation (`tenant_id` on every tenant-scoped table, enforced at the Repository layer before every query)
- **Database:** MySQL 8.x InnoDB (strict mode enabled; utf8mb4 charset)
- **Cache / Queue:** Redis 7 (queue driver: Redis; cache driver: Redis)
- **Job Queue:** Laravel Horizon
- **Search:** Laravel Scout + Meilisearch (for student/staff search)
- **Authentication:** Laravel Sanctum (JWT-style tokens); every JWT payload includes `tenant_id` claim
- **API:** RESTful JSON API (OpenAPI 3.1 spec to be written — see gap-analysis.md HIGH-003)

## Frontend (Web Portals)

- **Framework:** React 18 / TypeScript (Vite build)
- **UI Library:** shadcn/ui + Tailwind CSS
- **State Management:** Zustand
- **HTTP Client:** Axios with interceptors for tenant header injection
- **Progressive Web App:** Yes — offline support via service worker (Workbox) for attendance and mark entry

## Mobile Applications (Android — Phase 1–8)

- **Language:** Kotlin
- **UI:** Jetpack Compose
- **Architecture:** MVVM + Repository pattern
- **Offline:** Room database + background sync (WorkManager)
- **Push notifications:** Firebase Cloud Messaging (FCM)
- **Apps (6):** Super Admin, School Owner/Director, Teacher, Student, Parent, Bus Driver

## Mobile Applications (iOS — Phase 9–10)

- **Language:** Swift
- **UI:** SwiftUI
- **Architecture:** MVVM + Repository pattern
- **Apps (6):** Same 6 as Android

## Payments

- **Phase 1–2:** SchoolPay API (primary payment backbone — student payment codes, auto-reconcile)
- **Phase 3+:** MTN MoMo API, Airtel Money API (direct, post-BoU PSO licence)
- **Phase 4+:** Visa/Mastercard card-not-present (via Flutterwave)
- **Phase 11:** M-Pesa Daraja API (Kenya), Flutterwave/Paystack (Nigeria/Ghana), Airtel/Tigo (Tanzania)

## Communications

- **SMS:** Africa's Talking (Uganda local sender ID)
- **WhatsApp:** Meta Business Cloud API
- **Email:** Mailgun or Postmark (transactional); Mailchimp (bulk newsletters)
- **Push (web):** Firebase Cloud Messaging

## AI / Analytics

- **Model:** Anthropic Claude API (claude-sonnet-4-6)
- **Use cases:** Predictive fee defaulter alerts, attendance pattern analysis, exam performance trends, natural-language report commentary generation

## Infrastructure

- **Hosting:** Ubuntu 22.04 LTS VPS (initial); AWS EC2 Auto Scaling (Phase 8+)
- **Object Storage:** AWS S3 (report PDFs, student photos, documents)
- **CDN:** CloudFront
- **SSL/TLS:** Let's Encrypt (auto-renew)
- **DNS:** Cloudflare
- **Containerisation:** Docker + Docker Compose (local dev); ECS Fargate (production Phase 8+)

## EMIS / Government Integration

- **Uganda:** MoES EMIS portal — bulk student data export in MoES-specified format (XML/CSV)
- **Kenya (Phase 11):** NEMIS API
- **UNEB:** Exam registration data export in UNEB-specified format

## Legal / Compliance

- **Uganda Data Protection and Privacy Act 2019** — compliance spec in `_context/gap-analysis.md` HIGH-008
- **Uganda Copyright Act 2006** — software registered with URSB; all developers sign IP assignment agreements
- **BoU Payment Systems Operator licence** — to be pursued Phase 3–4 for direct mobile money processing

## Development Environment

- **OS:** Windows 11 / WSL2 (development); Ubuntu 22.04 (production)
- **Local Server:** WAMP64 (development)
- **Version Control:** Git (GitHub)
- **CI/CD:** GitHub Actions
- **Code Quality:** PHP CS Fixer, PHPStan level 8, ESLint, Prettier
- **Testing:** PHPUnit (backend), Pest (preferred), Vitest (frontend), Playwright (E2E)

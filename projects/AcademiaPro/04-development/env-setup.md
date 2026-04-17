# Development Environment Setup — Academia Pro

Reproducible local development for every new engineer. Target: engineer checks out the repo, runs three commands, and has a working local Academia Pro instance within 20 minutes.

## Prerequisites

- Docker Desktop 4.30+ (Mac/Windows) or Docker Engine 24+ (Linux)
- Git 2.40+
- Make (GNU Make 4+)
- SSH key registered against the repo host

## One-Shot Bootstrap

```bash
git clone git@github.com:chwezi/academiapro.git
cd academiapro
make bootstrap
```

`make bootstrap` executes:

1. `docker compose up -d mysql redis mailhog`
2. `docker compose run --rm app composer install`
3. `docker compose run --rm app php artisan migrate --seed`
4. `docker compose run --rm web npm ci && npm run dev`

## Verification

```bash
make health
```

Expected output:

```
ok MySQL reachable on 3306
ok Redis reachable on 6379
ok App responds 200 on http://localhost:8080/health
ok Web dev server responds 200 on http://localhost:5173
```

## Environment Variables

Copy `.env.example` → `.env`. No secrets required locally — a sandbox MoMo key is seeded. Production secrets are injected via AWS Secrets Manager (see `06-deployment-operations/runbook.md`).

## Test Suite

```bash
make test           # full suite
make test-unit      # PHPUnit unit tests
make test-feature   # Laravel HTTP feature tests
make test-web       # Vitest + React Testing Library
make test-android   # Gradle connectedAndroidTest (emulator required)
make test-ios       # xcodebuild test (macOS required)
```

## IDE Setup

Recommended: VS Code with `.vscode/extensions.json` recommended-extensions list. PHPStorm and IntelliJ configurations in `docs/ide/`.

## Troubleshooting

- "Address already in use" on 3306 — stop the host MySQL (`brew services stop mysql` or `systemctl stop mysql`).
- Composer install OOM — increase Docker memory to 4 GB or more.
- See `06-deployment-operations/runbook.md §Local-dev escalation` for more.

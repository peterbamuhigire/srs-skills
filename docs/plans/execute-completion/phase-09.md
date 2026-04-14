# Phase 9: Production Operations, Observability & SRE

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Build full production visibility — the ability to know when your systems are
degrading before clients do, measure SLO compliance, and operate production with
engineering discipline rather than guesswork.

**Architecture:** One new comprehensive skill (`observability-platform`) plus three
targeted enhancements that add SRE practices, reverse proxy ops, and workflow automation
to existing microservices skills.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Instrument Node.js, PHP, Android, and iOS applications with OpenTelemetry
- Deploy SigNoz (self-hosted, open-source) as an all-in-one observability stack
- Define SLOs, SLIs, and error budgets for every production service
- Build Grafana dashboards showing request rate, error rate, and latency (RED method)
- Set up Prometheus alerting rules with proper severity levels and routing
- Track application errors end-to-end with Sentry on web, iOS, and Android
- Run distributed tracing with Jaeger to find latency bottlenecks across microservices
- Configure Nginx as a production reverse proxy with rate limiting and SSL termination
- Operate Kong or Traefik as an API gateway with auth plugins and route management
- Automate workflows with n8n and Temporal for background job orchestration
- Conduct blameless postmortems and prevent repeated incidents with structural fixes
- Calculate error budget burn rate and make data-driven decisions about feature vs reliability work

---

## Current Strengths — Operations Skills Already Built

- `database-reliability` — MySQL/PostgreSQL reliability: replication, failover, backup, PITR
- `reliability-engineering` — Site reliability principles: toil elimination, risk quantification
- `observability-monitoring` — Basic logging, metrics, alerting setup (foundational; this phase deepens it)
- `microservices-resilience` — Circuit breaker, bulkhead, timeout, retry, fallback patterns
- `microservices-architecture-models` — CQRS, saga, API gateway patterns (enhance: add ops section)
- `microservices-communication` — gRPC, message queues, async patterns (enhance: add automation engines)

---

## Build Tasks

### Task 1: Create `observability-platform` skill

**File to create:** `C:\Users\Peter\.claude\skills\observability-platform\SKILL.md`

**Read first:**
- *Observability Engineering* — Majors, Fong-Jones, Miranda (full book)
- Site Reliability Engineering — Google (free at `sre.google/books`, Chapters 4, 6, 13)
- SigNoz documentation — `signoz.io/docs`
- OpenTelemetry documentation — `opentelemetry.io/docs`
- Sentry documentation — `docs.sentry.io`

**Content outline for SKILL.md (target: 420–490 lines):**

1. **Three Pillars of Observability** — logs, metrics, traces: what each answers, when to use each
2. **Structured JSON Logging** — log schema design: `timestamp`, `level`, `service`, `trace_id`, `user_id`; log levels (FATAL/ERROR/WARN/INFO/DEBUG/TRACE) and when to use each
3. **SigNoz Setup** — Docker Compose deployment, data retention config, first dashboard
4. **OpenTelemetry Node.js** — `@opentelemetry/sdk-node` setup, auto-instrumentation, custom spans
5. **OpenTelemetry PHP** — `open-telemetry/sdk` setup, HTTP server instrumentation, attribute naming
6. **OpenTelemetry Android** — `io.opentelemetry.android` agent, Compose screen tracking, crash correlation
7. **OpenTelemetry iOS** — OpenTelemetry-Swift, URLSession instrumentation, SwiftUI screen tracing
8. **Prometheus Metrics** — counter, gauge, histogram, summary: naming conventions (RED method)
9. **Grafana Dashboards** — dashboard JSON structure, variables, template queries, RED dashboard template
10. **Alerting Rules** — Prometheus alert syntax, severity levels, inhibition rules, routing to PagerDuty/OpsGenie
11. **Distributed Tracing with Jaeger** — trace context (W3C `traceparent`), sampling strategies, trace analysis
12. **Sentry Setup** — DSN configuration, source maps for Next.js, iOS/Android SDK setup, issue triage
13. **SLO/SLI Design:**
    - SLI examples: availability (successful requests / total), latency (P95 ≤ 500ms), error rate
    - SLO examples: 99.9% availability over rolling 28 days
    - Error budget: `(1 - SLO) × window` — how much downtime you can afford
14. **Error Budget Burn Rate** — fast burn (1h) vs slow burn (6h) alert thresholds
15. **Real User Monitoring (RUM)** — Core Web Vitals collection, Sentry Performance, session replay
16. **On-Call Runbooks** — incident classification (SEV1–SEV4), escalation path, communication template
17. **Blameless Postmortem** — timeline reconstruction, 5-why root cause, action items, JIRA tickets
18. **Production Dashboards** — the four essential dashboards every SaaS needs: Service Health, Infrastructure, Business KPIs, SLO Tracker

**Step 1:** Read Observability Engineering (full) and SRE book Chapters 4, 6, 13.
**Step 2:** Create `SKILL.md` with all 18 sections.
**Step 3:** Include SigNoz Docker Compose snippet, OpenTelemetry Node.js setup code, and
   a complete Prometheus alert rule YAML example.
**Step 4:** Include a complete SLO definition example with SLI query and error budget calculation.
**Step 5:** Run `wc -l SKILL.md` — confirm 400–500 lines.
**Step 6:** Commit: `feat(skills): add observability-platform skill — SigNoz + OTel + SRE`

---

### Task 2: Enhance `database-reliability`

**File to modify:** `C:\Users\Peter\.claude\skills\database-reliability\SKILL.md`

Add `## Platform SRE for Databases` section covering:

- Database SLIs: query P95 latency, replication lag, connection pool utilisation, deadlock rate
- Database SLOs: query P95 ≤ 100ms for 99.5% of requests over 28 days
- Error budget tracking for databases: how much replication lag is acceptable per month
- Chaos engineering for databases: controlled failover drills, connection pool exhaustion simulation
- Blameless database postmortem template: timeline, root cause, replication lag root cause tree
- Toil identification: repeated manual tasks (backup monitoring, index rebuilds) → automate
- Runbook structure: title, severity, trigger condition, investigation steps, resolution, escalation

**Step 1:** Append the new section.
**Step 2:** Include a concrete SLI PromQL query and SLO definition YAML.
**Step 3:** Confirm file ≤ 500 lines.
**Step 4:** Commit: `feat(skills): enhance database-reliability with platform SRE section`

---

### Task 3: Enhance `microservices-architecture-models`

**File to modify:** `C:\Users\Peter\.claude\skills\microservices-architecture-models\SKILL.md`

Add `## Reverse Proxy & API Gateway Operations` section covering:

- Nginx as reverse proxy: `proxy_pass`, `upstream` block, health checks, `keepalive`
- Nginx rate limiting: `limit_req_zone`, burst, nodelay — production configuration
- Nginx SSL termination: Let's Encrypt integration, HSTS, OCSP stapling, TLS 1.3
- Nginx cache configuration: `proxy_cache`, cache bypass, cache status header
- Nginx zero-downtime reload: `nginx -s reload` vs `nginx -t` validation
- Kong API Gateway: service + route + plugin model, JWT auth plugin, rate-limit plugin
- Traefik as alternative: Docker provider, automatic TLS, middleware chains, dashboard
- HAProxy for TCP/HTTP load balancing: backend health checks, sticky sessions, stats page

**Step 1:** Append the new section.
**Step 2:** Include complete Nginx server block example (proxy + rate limit + SSL).
**Step 3:** Include Kong declarative config (`deck` format) for a service + route + JWT plugin.
**Step 4:** Confirm file ≤ 500 lines.
**Step 5:** Commit: `feat(skills): enhance microservices-architecture-models with reverse proxy ops`

---

### Task 4: Enhance `microservices-communication`

**File to modify:** `C:\Users\Peter\.claude\skills\microservices-communication\SKILL.md`

Add `## Workflow Automation & Async Orchestration` section covering:

- n8n self-hosted: installation, workflow concepts (nodes, triggers, credentials), HTTP Request node
- n8n for SaaS automations: Stripe webhook → n8n → send onboarding email → create Slack channel
- Temporal workflow orchestration: workflow code vs activity code, durable execution guarantees
- Temporal patterns: retries with backoff, timeouts, signals, queries, child workflows
- Temporal vs BullMQ: when to use each (long-running durable workflows vs short background jobs)
- Apache Airflow: DAG structure, task dependencies, XCom for task communication, sensor patterns
- Airflow vs Temporal: ETL pipelines (Airflow) vs business process workflows (Temporal)
- Workflow observability: Temporal Web UI, n8n execution logs, Airflow task instance logs

**Step 1:** Append the new section.
**Step 2:** Include a minimal Temporal workflow + activity TypeScript example.
**Step 3:** Include an n8n webhook → HTTP Request → email workflow description.
**Step 4:** Confirm file ≤ 500 lines.
**Step 5:** Commit: `feat(skills): enhance microservices-communication with workflow automation`

---

## Phase Completion Checklist

- [ ] `observability-platform` created — 400–500 lines, all 18 sections present
- [ ] SigNoz Docker Compose snippet included in observability-platform
- [ ] Complete Prometheus alert YAML rule included
- [ ] SLO/SLI section includes a concrete PromQL SLI query and error budget formula
- [ ] `database-reliability` enhanced with Platform SRE section
- [ ] `microservices-architecture-models` enhanced with Nginx + Kong/Traefik ops section
- [ ] `microservices-communication` enhanced with n8n + Temporal + Airflow section
- [ ] No skill file exceeds 500 lines
- [ ] `observability-platform` cross-references `kubernetes-platform` and `cicd-pipelines`
- [ ] Git commit made: `feat(skills): complete phase-9 — production operations & SRE`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Observability Engineering* | Majors, Fong-Jones, Miranda | O'Reilly | ~$55 | **The definitive observability book.** Structured events, tracing, instrumentation, SLO implementation. Read fully before writing `observability-platform`. |
| 2 | *Site Reliability Engineering* | Google | O'Reilly | Free (sre.google/books) | SLO/SLI/error budget design. Chapters 4 (SLOs), 6 (monitoring), 13 (emergency response) are essential. |
| 3 | *The Practice of Cloud System Administration* (2nd ed.) | Limoncelli, Chalup, Hogan | Addison-Wesley | ~$50 | SRE practices, capacity planning, runbook design, on-call management. |
| 4 | *Linux System Administration Handbook* (5th ed.) | Nemeth, Snyder, Hein, Mackin | Addison-Wesley | ~$60 | Comprehensive Linux ops — networking, storage, security, monitoring, scripting. Deepens `cicd-jenkins-debian`. |

### Free Resources

- SigNoz documentation — `signoz.io/docs` — self-hosted observability stack: install, dashboards, alerts
- OpenTelemetry documentation — `opentelemetry.io/docs` — vendor-neutral instrumentation for all languages
- Sentry documentation — `docs.sentry.io` — error tracking for web + mobile
- Prometheus documentation — `prometheus.io/docs` — metrics collection, alerting rules, PromQL
- Grafana documentation — `grafana.com/docs/grafana` — dashboard authoring, alerting, data sources
- Temporal documentation — `docs.temporal.io` — durable workflow patterns, activity retries
- n8n documentation — `docs.n8n.io` — workflow automation setup and node reference
- Google SRE book (free) — `sre.google/books` — the foundational SRE text

---

*Next phase: [Phase 10 — Revenue Infrastructure, Business Growth & Scale](phase-10.md)*

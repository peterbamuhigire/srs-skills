# ADR-0001 Laravel 11 over Node/NestJS for backend

- Status: accepted
- Date: 2026-04-17

## Context

Academia Pro is a multi-tenant SaaS for Ugandan schools. Primary constraints: the team already holds Laravel 10/11 expertise, the Uganda developer pool for PHP is materially deeper than Node/TypeScript, deployment target is shared-VPS-and-cPanel for Tier-2 schools, and we need first-class Eloquent scopes for the dual-layer tenant isolation model (Repository + global scope).

## Decision

Adopt Laravel 11 (PHP 8.2) as the backend framework. Use Laravel Sanctum for authentication, Laravel Horizon with Redis 7 for queues, and Eloquent with a `TenantScope` global scope for tenant isolation. Ship Laravel Reverb alongside Horizon for WebSocket support.

## Consequences

- Positive: fastest path to first paying school; lowest hiring cost in Uganda; Sanctum delivers first-party SPA + mobile token auth out of the box.
- Negative: PHP process-per-request model caps single-server throughput; must scale horizontally sooner than Node.
- Mitigated: horizontal scaling via AWS Auto-Scaling Group behind ALB; Reverb deployed alongside Horizon for WebSocket needs.

## Affects

- All FR-AUTH-* requirements (Sanctum implementation).
- NFR-PERF-001 (response time — requires horizontal scale plan).
- ADR-0003 (tenant isolation relies on Eloquent global scopes).

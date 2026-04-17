## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Longhorn ERP Mobile Application Programming Interface (Mobile API). The document provides a contractual baseline for the design, development, testing, and acceptance of the Mobile API layer, per IEEE 830-1998.

The primary audience is the engineering team responsible for backend API implementation, mobile app developers targeting Android (Kotlin + Jetpack Compose) and iOS (Swift + SwiftUI), and quality assurance personnel authoring test cases from this SRS.

### 1.2 Scope

The Mobile API is a JSON Web Token (JWT)-secured Representational State Transfer (REST) API exposed at `/api/mobile/v1/` (and subsequent version paths). It provides authenticated mobile clients with access to Longhorn ERP data and operations subject to tenant isolation, Role-Based Access Control (RBAC), and module-level gating.

The scope of this document covers:

- JWT-based authentication and token lifecycle management.
- Tenant isolation enforcement at the API boundary.
- API versioning and backward-compatibility guarantees.
- Offline data collection and delta synchronisation for the Cooperative Procurement module.
- Push notification dispatch and device token management.
- Per-tenant and per-user rate limiting.
- Data-lite mode for low-bandwidth mobile environments.
- Non-functional requirements (performance, security, availability) governing the Mobile API.

The Mobile API does not replace the web-session-based API at `/api/`. The two API surfaces are independent and share no authentication state.

### 1.3 Definitions

The following terms are used throughout this document. All definitions conform to IEEE Std 610.12-1990 unless otherwise stated.

**Bearer Token** — An HTTP Authorization header value of the form `Authorization: Bearer <token>`, used by mobile clients to present a JWT access token with every authenticated API request.

**Delta Synchronisation** — A synchronisation strategy in which the mobile client transmits the timestamp of its last successful sync to the server, and the server returns only records modified after that timestamp, minimising data transfer volume.

**JWT (JSON Web Token)** — A compact, URL-safe token format defined by RFC 7519 used to convey claims between the mobile client and the server. The JWT is cryptographically signed; the server validates the signature and reads claims directly without a database lookup on every request.

**Offline Sync** — The capability allowing a mobile client to record transactions locally while disconnected from the network and to transmit those records to the server upon reconnection.

**Push Notification** — A server-initiated message delivered to a registered mobile device via Apple Push Notification service (APNs) for iOS or Firebase Cloud Messaging (FCM) for Android, without the app being in the foreground.

**Refresh Token** — A long-lived, opaque token stored securely on the mobile device. It is exchanged for a new access token when the current access token expires. Refresh tokens rotate on each use.

**Tenant Context** — The authoritative `tenant_id` value extracted from the validated JWT `tid` claim. The `tenant_id` is never accepted from request parameters or the request body.

**Token Bucket** — A rate-limiting algorithm in which each client is allocated a bucket of tokens replenished at a fixed rate; each request consumes one token, and requests that arrive when the bucket is empty are rejected with HTTP 429.

### 1.4 Applicable Standards

| Standard | Application |
|---|---|
| IEEE 830-1998 | SRS structure and completeness criteria |
| IEEE Std 610.12-1990 | Terminology definitions |
| IEEE 1012-2016 | Verification and Validation framework |
| RFC 7519 | JSON Web Token specification |
| RFC 6750 | Bearer Token usage in HTTP |
| OWASP API Security Top 10 (2023) | API threat modelling and mitigation |
| NIST SP 800-63B | Authentication assurance levels and token management |
| Uganda Data Protection and Privacy Act 2019 | Data handling obligations for mobile-collected data |

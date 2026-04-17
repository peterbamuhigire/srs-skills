---
title: "BIRDC ERP — REST API Specification"
subtitle: "Design Documentation — Document 03-API-SPEC"
author: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0 — Draft"
---

# BIRDC ERP — REST API Specification

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC
**Date:** 2026-04-05
**Version:** 1.0 — Draft
**Classification:** Confidential — BIRDC Internal

---

## Document Purpose

This specification defines the REST API consumed by all 6 BIRDC Android mobile applications. Every endpoint listed here represents a contract between the Android client applications and the PHP 8.3+ backend server hosted on BIRDC's on-premise infrastructure at Nyaruzinga, Bushenyi.

This document covers:

- All HTTP endpoints (minimum 80) across 10 functional domains
- Standard request and response envelope formats
- Authentication and authorisation requirements per endpoint
- Role-Based Access Control (RBAC) permissions per endpoint
- Error handling conventions
- Pagination conventions
- JWT token structure

## Scope

The API serves 6 Android applications:

1. **Sales Agent App** — offline Point of Sale (POS), agent stock, remittance, commissions
2. **Farmer Delivery App** — offline farmer registration, GPS profiling, delivery recording
3. **Warehouse App** — barcode-scan stock receipts, transfers, physical counts
4. **Executive Dashboard App** — financial KPI snapshots, budget variance alerts
5. **HR Self-Service App** — leave management, payslips, attendance
6. **Factory Floor App** — production orders, QC results, worker attendance

## Base URL

All API endpoints are relative to:

```
https://<birdc-server>/api/v1
```

During development and testing, the base URL resolves to the on-premise server IP or hostname configured in each Android app's `BuildConfig`.

## API Version Strategy

The API is versioned via the URL path prefix `/api/v1`. Breaking changes require a new version prefix (`/api/v2`). Non-breaking additions (new optional fields, new endpoints) are deployed in-place without a version increment.

---

# Coverage Matrix — Academia Pro

Generated from test-plan frontmatter. Refreshed by `scripts/sync-coverage.sh` or manually when stories close.

## FR Coverage (skeleton — to be auto-generated)

| FR ID | Test Case(s) | Status |
|---|---|---|
| FR-AUTH-001 | TC-AUTH-001, TC-AUTH-002 | ready-for-impl |
| FR-AUTH-002 | TC-AUTH-003 | ready-for-impl |
| FR-ENR-001 | TC-ENR-001, TC-ENR-002, TC-ENR-003 | ready-for-impl |
| FR-ENR-002 | TC-ENR-004 | ready-for-impl |
| FR-FEE-001 | TC-FEE-001, TC-FEE-002 | ready-for-impl |
| FR-FEE-005 | TC-FEE-010 (duplicate-payment detection) | ready-for-impl |
| FR-ATT-001 | TC-ATT-001 | ready-for-impl |
| FR-EXM-001 | TC-EXM-001 | ready-for-impl |
| FR-EXM-008 | TC-EXM-020 (UNEB export byte-for-byte) | ready-for-impl |
| FR-EMIS-001 | TC-EMIS-001 | ready-for-impl |
| FR-AI-001 | TC-AI-001 (PII scrubber coverage) | ready-for-impl |
| ... | ... | ... |

## NFR Coverage

| NFR ID | Test Case(s) | Status |
|---|---|---|
| NFR-PERF-001 | TC-PERF-001 (k6 load test) | ready-for-impl |
| NFR-SEC-001 | TC-SEC-001 (AES-256-GCM at rest) | ready-for-impl |
| NFR-SEC-002 | TC-ISO-001 through TC-ISO-010 (tenant leakage) | ready-for-impl |
| NFR-AVAIL-001 | TC-AVAIL-001 (99.5% availability) | ready-for-impl |
| NFR-COST-001 | TC-COST-001 (shared-hosting fit) | ready-for-impl |
| ... | ... | ... |

> The living matrix is regenerated on demand; this skeleton lives in git to satisfy the phase05 coverage-matrix expectation and is kept roughly current through sprint.

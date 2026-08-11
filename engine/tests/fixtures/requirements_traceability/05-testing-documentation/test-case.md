---
phase: "05"
inputs:
  - claim ID already exists for the tenant
expected_results:
  - duplicate submission is rejected with DUPLICATE_CLAIM_ID
requirement_trace:
  - FR-001
---
# Test Case TC-001

Given an existing claim ID, when the same claim ID is submitted again, then the system rejects the submission with `DUPLICATE_CLAIM_ID`.

# Test Coverage Map — Maduuka Phase 1

**Source:** `TestStrategy_Maduuka.docx` (10 sections, 8 test levels, IEEE 829/1012)
**Date:** 2026-04-05

## Test Level Coverage (Strategy vs Plan)

| Test Level | Strategy Defined | Test Plan Written | Test Cases Exist |
|---|---|---|---|
| Unit Testing | Yes | No | No |
| Integration Testing | Yes | No | No |
| System Testing | Yes | No | No |
| Acceptance Testing (UAT) | Yes | No | No |
| Performance Testing | Yes | No | No |
| Security Testing | Yes | No | No |
| Offline / Sync Testing | Yes | No | No |
| Regression Testing | Yes | No | No |

*The Test Strategy document defines what each level covers, entry/exit criteria, and roles. No executable test cases exist yet. The Test Plan Phase 1 document must be written to close this gap.*

## Module Test Priority (Recommended)

| Priority | Module | Reason |
|---|---|---|
| 1 | POS — Payment Processing (FR-POS-011 to FR-POS-015) | Revenue-critical; MoMo integration risk |
| 2 | HR / Payroll — PAYE / NSSF computation | Legal liability if incorrect |
| 3 | Inventory — FIFO/FEFO enforcement and expiry alerts | Regulatory requirement (pharmacy Phase 2) |
| 4 | Offline sync — conflict resolution | Design Covenant core constraint |
| 5 | Multi-tenant isolation | Security: tenant data separation |
| 6 | Customer credit limit enforcement (FR-POS-014, BR-002) | Financial risk |
| 7 | All remaining modules | Standard functional coverage |

## IEEE 829 Artifacts Required

| Artifact | Status |
|---|---|
| Test Plan (IEEE 829 §4) | Missing |
| Test Design Specifications | Missing |
| Test Case Specifications | Missing |
| Test Procedure Specifications | Missing |
| Test Item Transmittal Report | Missing |
| Test Log | Missing (pre-development) |
| Test Incident Report | Missing (pre-development) |
| Test Summary Report | Missing (pre-development) |

*Only the Test Strategy (analogous to IEEE 829 Master Test Plan) has been produced. All downstream artifacts are pending.*

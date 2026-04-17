# Traceability Matrix, Context Gaps, and Verification Notes

## 9.1 Requirements-to-Business-Goals Traceability Matrix

| Requirement ID | Requirement Summary | Business Goal(s) | Verification Method |
|---|---|---|---|
| **FR-AGENT-001** | Create agent record with unique Agent ID | BG-01 | Functional test: submit valid form, verify Agent ID format and DB record |
| **FR-AGENT-002** | Deactivate agent; block new attributions | BG-01 | Functional test: deactivate, attempt attribution, expect AGENT_INACTIVE |
| **FR-AGENT-003** | Audit trail on agent record updates | BG-05 | Functional test: update field, inspect audit log for 5 required fields |
| **FR-AGENT-004** | Profile photo upload and resize | BG-01, BG-03 | Functional test: upload image, verify 256×256 dimensions in storage |
| **FR-AGENT-005** | Agent search by name, ID, phone | BG-01 | Performance test: 1,000-agent tenant, search returns within 1 second |
| **FR-AGENT-006** | Territory assignment to agent | BG-01, BG-07 | Functional test: assign territory, verify record and start date |
| **FR-AGENT-007** | Territory reassignment with history | BG-05 | Functional test: reassign, verify previous record has end date |
| **FR-AGENT-008** | Territory map view | BG-07 | Functional test: map renders within 3 seconds, agent counts correct |
| **FR-AGENT-009** | Product assignment restricts attribution | BG-01, BG-05 | Functional test: attribute non-assigned product, expect PRODUCT_NOT_ASSIGNED |
| **FR-AGENT-010** | Product removal preserves history | BG-05 | Functional test: remove product, verify historical records intact |
| **FR-AGENT-011** | Sales target creation and duplicate guard | BG-01, BG-03 | Functional test: create duplicate period target, expect DUPLICATE_TARGET_PERIOD |
| **FR-AGENT-012** | Bulk target CSV import | BG-01 | Integration test: 500-row CSV with 10 invalid rows, verify counts and timing |
| **FR-AGENT-013** | Target Achievement Percentage formula | BG-03 | Calculation test: known sales and target, verify formula output and update latency |
| **FR-AGENT-014** | Automatic target period closure | BG-01 | Scheduled job test: verify status transition by 06:00 EAT after end date |
| **FR-AGENT-015** | Auto attribution on invoice post | BG-01, BG-05 | Integration test: post invoice with Agent field, verify attribution record within 30 s |
| **FR-AGENT-016** | Manual attribution with audit | BG-01, BG-05 | Functional test: manually attribute, verify Manual flag and justification stored |
| **FR-AGENT-017** | Re-attribution rules and locked invoices | BG-05 | Functional test: re-attribute finalised-run invoice, expect ATTRIBUTION_LOCKED |
| **FR-AGENT-018** | Split attribution summing to 100% | BG-01 | Functional test: enter 101% split, expect SPLIT_SUM_NOT_100 |
| **FR-AGENT-019** | Attribution report performance | BG-01, BG-03 | Performance test: 90-day report on 10,000 records within 3 seconds |
| **FR-AGENT-020** | Attribution exception for unassigned product | BG-05 | Integration test: post invoice with non-assigned product, verify exception log and notification |
| **FR-AGENT-021** | Commission rule creation and overlap guard | BG-04, BG-05 | Functional test: create overlapping rule, expect RULE_OVERLAP |
| **FR-AGENT-022** | Rule ID assignment and availability | BG-04 | Functional test: save rule, verify Rule ID format and presence in run configuration list |
| **FR-AGENT-023** | Rule deactivation | BG-04, BG-05 | Functional test: deactivate, verify not in new run list; existing run values intact |
| **FR-AGENT-024** | Flat rate commission formula | BG-01 | Calculation test: known sales and rate, verify computed amount |
| **FR-AGENT-025** | Tiered rate application | BG-01, BG-04 | Calculation test: known sales and tiers, verify correct tier and amount |
| **FR-AGENT-026** | Tiered rule gap and range validation | BG-04 | Functional test: define gap in tiers, expect TIER_GAP_DETECTED |
| **FR-AGENT-027** | Cumulative tiered rate formula | BG-01, BG-04 | Calculation test: known sales and tiers, verify marginal calculation |
| **FR-AGENT-028** | Product-specific commission formula | BG-01, BG-04 | Calculation test: two products with different rates, verify sum |
| **FR-AGENT-029** | Missing rate exclusion and exception log | BG-05 | Functional test: run with undefined-rate product, verify exclusion and exception |
| **FR-AGENT-030** | Agent-level rule override | BG-04, BG-05 | Functional test: override agent rule, run commission, verify override applied flag |
| **FR-AGENT-031** | Commission run initiation and duplicate guard | BG-01, BG-05 | Functional test: initiate duplicate period run, expect DUPLICATE_RUN_PERIOD |
| **FR-AGENT-032** | Commission run batch performance | BG-01 | Performance test: 500-agent run completes within 120 seconds |
| **FR-AGENT-033** | Commission run summary record | BG-01, BG-05 | Functional test: run completes, verify summary accessible within 5 seconds |
| **FR-AGENT-034** | Commission run exception CSV export | BG-05 | Functional test: 15-exception run, verify CSV row count and download time |
| **FR-AGENT-035** | Approver notification on run submission | BG-01, BG-05 | Integration test: run enters Pending Approval, verify notifications within 5 minutes |
| **FR-AGENT-036** | Commission run approval and lock | BG-05 | Functional test: approve run, verify irreversibility and Initiate Payment unlocked |
| **FR-AGENT-037** | Commission run rejection | BG-05 | Functional test: reject with short reason (blocked), valid reason triggers notification |
| **FR-AGENT-038** | Pre-payment MoMo number validation | BG-02 | Functional test: 3 agents with missing MoMo numbers excluded, exception report generated |
| **FR-AGENT-039** | Bulk MoMo payment submission | BG-02 | Integration test: submit batch to gateway, verify gateway reference stored |
| **FR-AGENT-040** | Payment callback processing | BG-02 | Integration test: simulate callbacks, verify per-agent status updates within 60 seconds |
| **FR-AGENT-041** | Failed payment retry (max 3) | BG-02 | Functional test: retry 3 times, verify 4th attempt blocked |
| **FR-AGENT-042** | Run closure report generation | BG-02, BG-05 | Functional test: terminal state reached, PDF generated within 10 seconds |
| **FR-AGENT-043** | Portal authentication and lockout | BG-03 | Security test: 5 failed attempts triggers 15-minute lockout |
| **FR-AGENT-044** | Portal data isolation | BG-03, BG-05 | Security test: cross-agent request returns 403 |
| **FR-AGENT-045** | Agent sales list performance | BG-03 | Performance test: 1,000-record list loads within 2 seconds |
| **FR-AGENT-046** | Sales date filter with total | BG-03 | Functional test: apply filter, verify results and sum within 2 seconds |
| **FR-AGENT-047** | Commission run history in portal | BG-03 | Functional test: agent sees all runs from join date with correct statuses |
| **FR-AGENT-048** | Commission breakdown detail view | BG-03 | Functional test: tiered run breakdown shows tier rows summing to correct total |
| **FR-AGENT-049** | PDF commission statement download | BG-03 | Functional test: PDF generated within 10 seconds with all required fields |
| **FR-AGENT-050** | Target progress indicator and formula | BG-03 | Calculation test: known sales and target, verify %, latency ≤ 5 minutes |
| **FR-AGENT-051** | Target milestone notifications | BG-03 | Integration test: attribution crossing 80%, 100%, 120% triggers agent notification |
| **FR-AGENT-052** | Agent payment notifications | BG-02, BG-03 | Integration test: Paid transition triggers in-app and email within 5 minutes |
| **FR-AGENT-053** | Stock issuance to agent | BG-06 | Functional test: issue 50 units, verify main ledger −50, agent balance +50 |
| **FR-AGENT-054** | Agent stock return (good and damaged) | BG-06 | Functional test: good return credits ledger; damaged return writes off |
| **FR-AGENT-055** | Agent stock balance formula | BG-06 | Calculation test: issue, attribute sales, return — verify formula output |
| **FR-AGENT-056** | Stock reorder alert notification | BG-06 | Integration test: balance drops below threshold, notification within 5 minutes |
| **FR-AGENT-057** | Stock reconciliation and variance approval | BG-06 | Functional test: physical count variance generates pending entry, not posted until approved |
| **FR-AGENT-058** | Remittance recording and mobile money reference guard | BG-06 | Functional test: MoMo remittance without reference blocked |
| **FR-AGENT-059** | Remittance variance and tolerance gate | BG-06 | Calculation test: known invoices and remittance amount, verify variance and tolerance block |
| **FR-AGENT-060** | Verified remittance ledger posting | BG-06 | Integration test: verify remittance, confirm receipt entry and invoice balance reduction |
| **FR-AGENT-061** | Overdue remittance flagging and daily notification | BG-06 | Scheduled job test: SLA elapsed, flag set, daily notification confirmed |
| **FR-AGENT-062** | Daily activity summary generation | BG-07 | Scheduled job test: 23:45 EAT job generates one record per active agent |
| **NFR-AGENT-001** | Page load P95 ≤ 3 seconds | BG-03 | Load test: 100 concurrent users, measure P95 |
| **NFR-AGENT-002** | Commission run for 500 agents ≤ 120 seconds | BG-01 | Performance test: timed batch run |
| **NFR-AGENT-003** | Bulk MoMo submission ≤ 30 seconds | BG-02 | Performance test: timed payment initiation |
| **NFR-AGENT-004** | Portal P95 ≤ 2 seconds, 200 concurrent | BG-03 | Load test: 200 concurrent agents |
| **NFR-AGENT-005** | Monthly uptime ≥ 99.5% | BG-01, BG-02, BG-03 | Monitoring: ≤ 216 minutes downtime per month |
| **NFR-AGENT-006** | Idempotent commission run on recovery | BG-01 | Chaos test: mid-calculation failure recovery, verify no duplicate ledger entries |
| **NFR-AGENT-007** | Financial write durability ≤ 1 second | BG-05 | Chaos test: kill app server post-write, verify persistence |
| **NFR-AGENT-008** | TLS 1.2+ on portal; HTTP redirects to HTTPS | BG-03 | SSL Labs scan; HTTP redirect test |
| **NFR-AGENT-009** | Server-side RBAC enforcement | BG-05 | Security test: out-of-role destructive requests return 403 |
| **NFR-AGENT-010** | Immutable 7-year audit log | BG-05 | Security test: no delete endpoint; retention policy verification |

## 9.2 Context Gaps

The following items require input from the client or product owner before the affected requirements can be marked `Verified`:

- [CONTEXT-GAP: Mobile Money API credentials and sandbox environment details] — Required for FR-AGENT-039, FR-AGENT-040, FR-AGENT-041. The specific MTN Mobile Money and Airtel Money API versions (B2C or Bulk Disbursement endpoint) and authentication flow must be confirmed to finalise integration specifications.
- [CONTEXT-GAP: Tenant-configurable commission rule scope] — FR-AGENT-021 assumes a rule can be scoped as either tenant-wide or agent-specific. Confirm whether group-level (e.g., agent category) scoping is also required.
- [CONTEXT-GAP: Currency multi-tenancy] — FR-AGENT-031 and FR-AGENT-039 default to UGX. If pan-Africa tenants require USD, KES, or TZS commission runs with currency conversion, additional requirements for exchange rate management are needed.
- [CONTEXT-GAP: Commission tax withholding] — Uganda's Income Tax Act requires withholding tax (WHT) on commissions paid to non-employee agents. Whether the system should auto-calculate and deduct WHT before disbursement, and generate WHT certificates, must be decided before FR-AGENT-039 is finalised.
- [CONTEXT-GAP: Approval workflow stages] — FR-AGENT-035 and FR-AGENT-036 define a single-stage approval. If the tenant requires a two-stage approval (e.g., Territory Manager then Finance Director), the workflow engine requirements must be extended.

## 9.3 Verification Notes

- All formulas in sections 3, 4, 5, 6, and 7 must be validated against the same inputs using an independent calculation (e.g., an Excel model) before system acceptance.
- Commission run idempotency (NFR-AGENT-006) is a critical correctness requirement; it must be demonstrated in a chaos engineering test, not merely unit-tested.
- RBAC enforcement (NFR-AGENT-009) must be tested by an independent security reviewer, not the development team, to satisfy the audit requirement under ISO/IEC 15504.
- The 7-year audit log retention (NFR-AGENT-010) must be validated against the current Uganda Income Tax Act retention clause before the system is deployed to production.

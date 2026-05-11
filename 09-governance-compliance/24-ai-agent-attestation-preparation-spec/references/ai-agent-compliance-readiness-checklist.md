# AI Agent Compliance Readiness Checklist (50–100 points)

Pre-audit assessment. Each item checked Yes / No / N/A with evidence reference. SEV1 gap = any unchecked item flagged Critical.

## Policies (10)

1. Agent Action Governance Policy signed within last 12 months and current version published. [Ref: `policies/agent-action-governance-policy.md`]
2. Agent Audit-Log Retention Policy signed and retention table matches operational configuration. [Ref: `policies/agent-audit-log-retention-policy.md`]
3. Agent Approval and Supervision Policy signed; supervision matrix per feature current.
4. Agent Kill-Switch and Drill Policy signed; last drill within 90 days.
5. Agent Memory Erasure Policy signed; erasure SLA current.
6. Agent Red-Team and Safety Policy signed; weekly full set executed within last week.
7. Agent Compliance Evidence and Attestation Policy signed.
8. Sign-off ledger lists every policy and every signature.
9. Exceptions and waivers ledger current; no expired waivers in effect.
10. Public Responsible-AI Declaration current and matches internal Responsible-AI Addendum.

## Controls — SOC 2 (15)

11. CC1.1: Agent governance owner named in policy and reachable.
12. CC2.3: In-product agent disclosure modal live and screenshot captured.
13. CC4.1: Burn-rate alerts active for every required SLI; configuration exported.
14. CC5.1: Approval event signed; sample 25 events available.
15. CC6.1: Agent service principal access review completed within last 90 days.
16. CC6.3: Cross-tenant tool-routing red-team scenario passing.
17. CC7.2: Anomaly detection rules for irreversible-action rate, intervention rate, cost-per-run active.
18. CC7.3: Agent-incident playbooks current.
19. CC7.4: Kill-switch drill report within 90 days.
20. CC8.1: 25 PR sample available with ADR, red-team smoke, eval gate, sign-off.
21. A1.2: Agent-task availability SLO report within 30 days.
22. C1.1: Tool-output classification rules current; sample audit-log redaction verified.
23. C1.2: Memory erasure event log sample available.
24. PI1.4: Hash-chain integrity report within 24 hours.
25. P3: DPIA addendum current; consultation status documented.

## Controls — ISO 27001 (15)

26. SoA agent delta current and merged.
27. A.5.7: Threat intel sources monitored; scenario change log within 7 days of last advisory.
28. A.5.9: Agent service principal inventory current.
29. A.5.19: Model provider supplier-risk assessment within last 12 months.
30. A.5.25: Incident classification trace for last 25 events.
31. A.5.27: AI RCA taxonomy applied to last 5 postmortems.
32. A.5.30: Kill-switch + replay drill reports within 90 days.
33. A.5.34: DPIA addendum current.
34. A.8.2: Two-person rule enforced for global kill-switch; recent invocations documented.
35. A.8.9: Configuration management — planner / catalogue under version control with PR gates.
36. A.8.10: Memory erasure certificates sample available.
37. A.8.15: Action audit log retention configuration matches policy.
38. A.8.16: Monitoring activities active.
39. A.8.25: SDLC gates fired on last 25 relevant PRs.
40. A.8.29: Weekly red-team replay report within 7 days.

## Controls — HIPAA (10) — if PHI in scope

41. PHI touch classification current per feature.
42. Admin-only constraint statement signed by Security Officer for clinical features.
43. §164.308(a)(7) Contingency plan drill report within 90 days.
44. §164.308(b)(1) BAA addendum executed with every PHI tenant; ledger current.
45. §164.312(a)(1) Unique service-principal ID; auto-logoff on operator console.
46. §164.312(b) Audit controls — hash-chain integrity verified daily.
47. §164.312(c)(1) Integrity — signed approval events sample available.
48. §164.312(d) Authentication — approver identity sample traceable to workforce.
49. §164.312(e)(1) Transmission security — TLS 1.2+ verified.
50. §164.316(b)(1) Documentation retention 6 years confirmed.

## Evidence completeness (10)

51. Every evidence artefact in the pack spec has a sample for the current window.
52. Sampling for 25-event populations is complete and stratified.
53. Daily-review tickets cover every day in the window.
54. Kill-switch drill reports cover at least 4 events in 12 months.
55. External red-team report current.
56. Incident postmortems for SEV1/SEV2 in window complete.
57. Evidence-pack signed zip exporter tested in the last 30 days.
58. Auditor portal access mechanism tested with named-recipient flow.
59. Chain-of-custody manifests current.
60. Redaction policy applied consistently across the window.

## Training and drills (5)

61. Agent on-call training completed by every on-call engineer within 12 months.
62. Agent disclosure training completed by product, sales, support within 12 months.
63. Kill-switch drill rehearsal — staging quarterly, production annual.
64. Replay-a-run drill within 90 days.
65. Memory erasure drill within 90 days.

## Sub-processors and contracts (5)

66. Sub-processor list public and current.
67. Model provider contracts include training-data exclusion clauses; clauses verified.
68. BAA addendum template current; signed addenda for every PHI tenant.
69. DPA addendum template current; signed addenda for every GDPR / African-DPA tenant.
70. Sub-processor change notification process tested.

## Pre-audit logistics (10)

71. Auditor scope letter received and acknowledged.
72. Auditor portal credentials prepared; named auditors only.
73. Prior-year findings status table prepared.
74. On-the-day playbook printed and distributed to demoers.
75. Demoer roles assigned for each walkthrough.
76. Pre-window dry run with internal audit completed.
77. Mid-window gap check completed; remediation actions closed.
78. Closure-preparation checklist completed.
79. Management response template prepared.
80. Corrective-action-plan template prepared.

Optional rows 81–100 may extend per project scope (additional regulators, sectoral overlays, sub-jurisdictions).

## Sign-off

| Role | Name | Date |
|------|------|------|
| AI Lead | | |
| Compliance Manager | | |
| CISO | | |

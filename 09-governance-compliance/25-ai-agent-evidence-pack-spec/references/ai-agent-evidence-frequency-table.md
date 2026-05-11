# AI Agent Evidence Frequency Table

Sortable per-control evidence cadence. The shared contract between this compliance pass and the parallel software-dev pass that builds the collectors. Every row names: control IDs (SOC 2 / ISO / HIPAA), evidence artefact, source system, collector, capture method, frequency, retention, sampling, redaction class.

Legend: `cont.` continuous; `D` daily; `W` weekly; `M` monthly; `Q` quarterly; `A` annual; `Ev` on-event.

| # | Evidence artefact | Source system | Collector | SOC 2 | ISO 27001 | HIPAA | Frequency | Retention | Sampling | Redaction class |
|---|---------------------|----------------|-----------|--------|-------------|--------|-----------|------------|-----------|------------------|
| 1 | Signed policy pack PDFs | doc mgmt | manual + ledger | CC1.1, CC2.2 | A.5.1 | 164.316.a | A | 7 y | full | none |
| 2 | Sign-off ledger CSV | sign-off store | append-only | CC1.1 | A.5.1 | 164.316.b | Ev | 7 y | full | none |
| 3 | Agent risk register | risk register | quarterly export | CC3.2 | A.5.7 | 164.308.a.1 | Q | 7 y | full | none |
| 4 | Action catalogue snapshot | repo | per release | CC5.1, CC8.1 | A.5.9, A.8.9 | 164.308.a.4 | Ev | 7 y | full | none |
| 5 | Service-principal scope export | IAM | quarterly job | CC6.1 | A.5.15 | 164.308.a.3 | Q | 7 y | full | internal-only |
| 6 | Dispatcher allow-list snapshot | dispatcher | scheduled | CC6.1, CC6.3 | A.5.15, A.8.3 | 164.308.a.4 | cont. + Q | 7 y | full | none |
| 7 | Cross-tenant routing test results | red-team rig | weekly | CC6.3 | A.8.12 | 164.308.a.4 | W | 3 y | full | none |
| 8 | Alert configuration export | observability | scheduled | CC4.1, CC7.2 | A.8.16 | 164.308.a.1 | cont. + M | 3 y | full | none |
| 9 | Daily-review ticket log | ticket system | scheduled | CC4.1 | A.8.16 | 164.308.a.1 | D | 3 y | 25 stratified | other-tenant |
| 10 | Monthly SLO report | SLO platform | scheduled | A1.2, CC4.1 | A.8.16 | n/a | M | 3 y | full | none |
| 11 | Anomaly rules export | observability | scheduled | CC7.2 | A.8.16 | 164.308.a.1 | cont. | 3 y | full | none |
| 12 | Anomaly ticket sample | ticket system | scheduled | CC7.2 | A.8.16 | 164.308.a.1 | cont. | 3 y | 25 stratified | other-tenant, user-pii |
| 13 | Incident playbook set | docs | per change | CC7.3 | A.5.25 | 164.308.a.6 | Ev | 7 y | full | none |
| 14 | SEV1/SEV2 incident postmortems | postmortem store | per incident | CC7.3, CC7.4 | A.5.27 | 164.308.a.6 | Ev | 7 y | full | other-tenant, user-pii |
| 15 | Kill-switch drill report | drill archive | per drill | CC7.4, A1.3 | A.5.30, A.8.2 | 164.308.a.7 | Q | 7 y | full | none |
| 16 | Replay-a-run drill report | drill archive | per drill | A1.3 | A.5.30 | 164.308.a.7 | Q | 7 y | full | none |
| 17 | Force-pause / resume drill report | drill archive | per drill | A1.3 | A.5.30 | 164.308.a.7 | Q | 7 y | full | none |
| 18 | PR list (planner/catalogue/supervisor) | repo | scheduled | CC8.1 | A.8.9, A.8.32 | 164.308.a.4 | cont. + Q | 7 y | 25 stratified | none |
| 19 | ADR list | repo | scheduled | CC8.1 | A.5.9, A.8.32 | 164.308.a.4 | cont. + Q | 7 y | full | none |
| 20 | Red-team CI smoke results | red-team rig | per PR | CC4.1, CC8.1, PI1.2 | A.5.7, A.8.29 | 164.308.a.1 | cont. | 3 y | full | none |
| 21 | Red-team weekly full results | red-team rig | weekly | CC4.1, PI1.2 | A.5.7, A.8.29 | 164.308.a.1 | W | 3 y | full | none |
| 22 | External red-team report | external | quarterly | CC4.1 | A.8.29 | 164.308.a.1 | Q | 7 y | full | provider-confidential |
| 23 | Eval gate results per PR | eval rig | per PR | CC8.1, PI1.2 | A.8.25 | 164.308.a.4 | cont. | 3 y | 25 stratified | none |
| 24 | Eval calibration recheck report | eval rig | monthly | PI1.2 | A.8.29 | 164.308.a.1 | M | 3 y | full | none |
| 25 | Approval event sample | orchestrator | scheduled | CC5.1, PI1.4 | A.5.15, A.8.2 | 164.312.d | cont. | 7 y | 25 stratified | user-pii, other-tenant |
| 26 | Approval event signature verifier | orchestrator | scheduled | PI1.4 | A.8.24 | 164.312.c.1, 164.312.d | D | 7 y | full | none |
| 27 | Audit-log retention config | orchestrator | scheduled | CC7.2, PI1.4 | A.8.15 | 164.312.b | cont. + Q | 7 y | full | none |
| 28 | Hash-chain integrity report | integrity verifier | daily | PI1.4 | A.8.15, A.8.24 | 164.312.b, 164.312.c.1 | D | 7 y | full | none |
| 29 | Audit-log redaction policy verification | log store | scheduled | C1.1 | A.5.12 | 164.502 | M | 7 y | full | none |
| 30 | Memory erasure event log | memory store | scheduled | C1.2 | A.5.34, A.8.10 | 164.502, GDPR.17 | cont. | 7 y | full | user-pii |
| 31 | Certificate of erasure sample | memory store | scheduled | C1.2 | A.8.10 | 164.502 | Ev | 7 y | full | user-pii |
| 32 | DPIA addendum | docs | annual | P3 | A.5.34 | 164.502 | A | 7 y | full | none |
| 33 | DSAR fulfilment log | DSAR system | scheduled | P5 | A.5.34 | 164.524 | Ev | 7 y | 25 stratified | user-pii |
| 34 | Sub-processor list | docs | per change | CC9.1, P6 | A.5.19, A.5.20 | 164.308.b.1 | Ev | 7 y | full | none |
| 35 | Model provider risk assessment | risk register | annual | CC9.1 | A.5.19 | 164.308.b.1 | A | 7 y | full | provider-confidential |
| 36 | Training-data exclusion evidence | contracts | annual | C1, P6 | A.5.19 | 164.308.b.1 | A | 7 y | full | provider-confidential |
| 37 | BAA addendum ledger | doc mgmt | per onboarding | n/a | n/a | 164.308.b.1, 164.504.e | Ev | 7 y (from termination) | full | other-tenant |
| 38 | DPA addendum ledger | doc mgmt | per onboarding | P6 | A.5.34 | n/a | Ev | 7 y (from termination) | full | other-tenant |
| 39 | Public Responsible-AI Declaration version | doc mgmt | per publish | CC2.3 | n/a | n/a | Ev | 7 y | full | none |
| 40 | In-product disclosure screenshots | product | per release | CC2.3 | n/a | n/a | Ev | 7 y | full | none |
| 41 | Bias review report (protected-class features) | review docs | quarterly | P7 | A.5.34 | n/a | Q | 7 y | full | user-pii |
| 42 | Agent on-call training completion | LMS | quarterly | CC1.4 | A.6.3 | 164.308.a.5 | Q | 3 y | full | user-pii |
| 43 | Agent disclosure training completion | LMS | quarterly | CC2.3 | A.6.3 | 164.308.a.5 | Q | 3 y | full | user-pii |
| 44 | Auditor portal access log | portal | continuous | CC6.1, CC6.6 | A.5.15, A.8.15 | 164.312.b | cont. | 7 y | full | named-auditor-only |

This table is consumed by the software-dev pass as the **collector contract**. Each row's collector implementation is owned by software-dev; the artefact and the cadence are owned here.

## Update protocol

- Adding a row requires PR + sign-off by AI Lead + Compliance Manager.
- Changing a row's frequency or retention requires ADR.
- Removing a row requires ADR + waiver + sign-off by CISO and DPO.

# AI Agent Auditor On-The-Day Playbook

Operational playbook for the day(s) the external auditor is on site or on screen. Goal: every walkthrough closes in under 30 minutes with the auditor leaving with the artefact they expected.

## Pre-day setup

| Item | Owner | Done? |
|------|-------|-------|
| Auditor portal access verified; named auditors enabled; access expires on day +1 | Compliance Manager | |
| Demoer roster confirmed; back-up demoer named per walkthrough | AI Lead | |
| Screen-share environment prepared (non-production for walkthroughs; production read-only for live evidence) | SRE Lead | |
| Evidence pack signed zip current; manifest hash recorded | Compliance Manager | |
| Policy pack printed or shared as PDF | Compliance Manager | |
| Sample sets pre-pulled (25 approval events, 25 daily-review tickets, 25 PRs, full kill-switch drill reports, full SEV1/SEV2 postmortems) | AI Lead | |

## Walkthrough 1 — Agent governance

| Auditor likely asks | Demoer | Click path | Artefact |
|---------------------|--------|------------|----------|
| Who owns agent governance? | AI Lead | n/a | Policy Pack cover page; org chart |
| Show the policy that says irreversible actions need human approval | AI Lead | Policy Pack → Policy 1 → 1.4 statement 2 | Signed policy |
| Show an example of an irreversible action declined without approval | AI Lead | Auditor portal → Approval events → filter `approval_required=true AND status=refused` | Refusal record |

## Walkthrough 2 — Action audit log

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show the retention configuration | AI Lead | Auditor portal → Settings → Retention | Configuration export |
| Show the integrity verifier output for the last 24 hours | AI Lead | Auditor portal → Integrity → Daily | Integrity report (signed) |
| Show 25 sample audit-log rows stratified across features | AI Lead | Pre-pulled sample CSV | Sample CSV |
| Show what happens when an attempt is made to alter a captured row | AI Lead | Non-prod demo: edit; verify rejection | Demo recording |

## Walkthrough 3 — Kill-switch drill

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show the last drill report | SRE Lead | Drill archive → most recent quarter | Drill report |
| Walk a global kill-switch invocation (two-person rule) | SRE Lead | Non-prod demo: operator 1 initiates; operator 2 approves; propagation verified within 5 s | Demo recording |
| Show how a tool is refused after kill-switch | SRE Lead | Non-prod demo: dispatcher refusal log | Refusal record |

## Walkthrough 4 — Approval event flow

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show 25 approval events stratified by feature | AI Lead | Pre-pulled sample | Sample list |
| Pick one; show approver identity, time, plan id, step index | AI Lead | Auditor portal → Approvals → event detail | Detail view |
| Show the signature on the event | AI Lead | Signed-event verifier | Verifier output |
| Reperform an approval event in non-production | AI Lead | Non-prod demo | Demo recording |

## Walkthrough 5 — Evidence pack assembly

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show the evidence pack manifest | Compliance Manager | Evidence pack → manifest.json | Manifest |
| Trace a control to its evidence | Compliance Manager | Manifest → control id → artefact path | Cross-link |
| Show chain of custody for one artefact | Compliance Manager | Manifest → capture history | Capture log |

## Walkthrough 6 — Change management

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show 25 PRs touching planner / catalogue / supervisor in the window | CTO | Pre-pulled list | List |
| Pick 5 at random; show ADR, red-team smoke result, eval gate result, sign-off | CTO | Per PR | Linked artefacts |
| Show what happens when a PR is missing an ADR | CTO | Non-prod demo: CI gate blocks merge | Demo |

## Walkthrough 7 — Anomaly response

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show the anomaly rules | SRE Lead | Observability platform → AI agent rules | Rule export |
| Show a recent anomaly ticket and the response | SRE Lead | Ticket system → ticket detail | Ticket and resolution |

## Walkthrough 8 — BAA execution (if HIPAA in scope)

| Question | Demoer | Click path | Artefact |
|----------|--------|------------|----------|
| Show the BAA addendum template | DPO | Document repository | Template |
| Show executed BAAs for current PHI tenants | DPO | BAA ledger | Ledger |
| Show provider-BAA status or de-identification evidence | DPO | Provider contracts; de-id audit | Evidence |

## Response language guidance

- Answer the question asked; do not volunteer information beyond it.
- If unsure, say: "Let me confirm and return with the exact evidence."
- Never speculate on a control's status; only state what evidence shows.
- Track every action item in the on-the-day notes; close before the auditor leaves.

## Post-day debrief

| Item | Owner | Due |
|------|-------|-----|
| Auditor portal access revoked | Compliance Manager | Day +1 |
| Action items consolidated and assigned | AI Lead | Day +1 |
| Management response drafted | AI Lead + CEO | Day +7 |
| Lessons learned recorded | Compliance Manager | Day +14 |

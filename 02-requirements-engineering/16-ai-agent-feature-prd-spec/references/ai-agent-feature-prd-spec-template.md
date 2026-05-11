# AI Agent Feature PRD Spec Template

## 1. Agent FR Inventory

| FR ID | Agent feature | Autonomy level | Tier |
|-------|----------------|------------------|------|
| AFR-TRG-001 | Inbox Triage | L2 | Pro |
| AFR-REC-001 | Daily Reconciliation | L3 | Enterprise |
| AFR-SUP-001 | Support Triage | L1 | Pro |

## 2. Per-FR Agent Clauses

### AFR-TRG-001 — Inbox Triage

| Clause | Value |
|--------|-------|
| Task scope boundary | Inputs: customer inbox threads since last run. Outputs: per-thread label + archive verdict + optional draft reply. Non-goals: sending the draft, modifying contacts. |
| Autonomy level | L2 — approve plan; admin approves the proposed batch verdict once per run. |
| Action-catalogue rows | `email.label`, `email.archive`, `email.draft.create`. |
| Intervention triggers | proposed action class = irreversible OR low-confidence label (< 0.6) OR thread tagged "VIP". |
| Budget caps | max-step 25 per thread; max-cost $0.25 per run; max-wallclock 120 s; on overrun: abort, alert admin, leave inbox untouched. |
| Abstain criteria | no plan satisfies policy envelope OR retrieval returns no precedents; produce explanation payload, no actions taken. |
| Irreversible-action gate | not applicable — all enumerated tools are compensable; `email.draft.create` does not send. |

### AFR-REC-001 — Daily Reconciliation

| Clause | Value |
|--------|-------|
| Task scope boundary | Inputs: prior day's ledger entries and bank feed. Outputs: matched-entry verdicts + ledger writes. Non-goals: any cash movement; any write outside `finance.ledger.*`. |
| Autonomy level | L3 — autonomous within envelope; nightly run, admin reviews summary. |
| Action-catalogue rows | `finance.ledger.match.read`, `finance.ledger.entry.write` (reversibility=compensable via reverse-entry tool). |
| Intervention triggers | discrepancy > $5,000 OR more than 1% of entries unmatched OR cost > $50 in a single run. |
| Budget caps | max-step 5,000; max-cost $50/run; max-wallclock 30 min. |
| Abstain criteria | bank feed unavailable; planner returns ambiguous plan; produce report-only payload. |
| Irreversible-action gate | not applicable — every write has a compensating reverse-entry; the reverse-entry tool itself is L1 admin-gated. |

## 3. Success Metrics per FR

| FR | Metric | Threshold | Eval set |
|----|--------|-----------|----------|
| AFR-TRG-001 | task success rate | >= 0.92 | EVAL-AGT-TRG-200 |
| AFR-TRG-001 | tool-choice quality | >= 0.95 | EVAL-AGT-TRG-200 |
| AFR-TRG-001 | hallucinated-argument rate | <= 0.01 | EVAL-AGT-TRG-200 |
| AFR-TRG-001 | intervention rate | <= 0.15 | production sample |
| AFR-REC-001 | task success rate | >= 0.98 | EVAL-AGT-REC-300 |
| AFR-REC-001 | irreversible-action-incident rate | 0 | production audit |

## 4. Human-in-the-Loop Placement

| FR | Approver role | Approval surface | Undo | Contest path |
|----|----------------|--------------------|------|----------------|
| AFR-TRG-001 | Inbox owner | proposed-plan modal showing per-thread verdict + draft | unarchive + delete-draft buttons | flag → human reviewer queue |
| AFR-REC-001 | Finance admin | morning digest of overnight matches; per-entry inspect | reverse-entry tool per row | flag → SEV3 ticket |

## 5. Rollout Posture

| FR | Initial stage | Promotion gate |
|----|----------------|------------------|
| AFR-TRG-001 | Shadow (agent proposes; admin acts manually) for 30 d | task success >= 0.92 on shadow; zero CRITICAL in red-team smoke |
| AFR-REC-001 | Shadow for 60 d | task success >= 0.98 on shadow; zero irreversible-action incidents during shadow |

## 6. Eval & Red-Team Acceptance Gates

| FR | Golden-task set | Replay set | Adversarial set | CI gate |
|----|------------------|--------------|------------------|---------|
| AFR-TRG-001 | EVAL-AGT-TRG-200 | REPLAY-TRG-50 | RT-AGT-TRG-30 | task success not down > 2 pp; tool-choice not down > 1 pp; zero hallucinated-arg increase |
| AFR-REC-001 | EVAL-AGT-REC-300 | REPLAY-REC-40 | RT-AGT-REC-25 | task success not down > 1 pp; zero irreversible-action incidents |

## 7. Traceability

| FR | PRD ref | AI Feature PRD ref | Eval ref | Red-team ref | RAI ref |
|----|---------|----------------------|-----------|-----------------|---------|
| AFR-TRG-001 | PRD-FR-031 | AI-FR-014 | EVAL-AGT-TRG-200 | RT-AGT-TRG-30 | RAI-AGT-DISC-01 |
| AFR-REC-001 | PRD-FR-052 | AI-FR-018 | EVAL-AGT-REC-300 | RT-AGT-REC-25 | RAI-AGT-DISC-02 |

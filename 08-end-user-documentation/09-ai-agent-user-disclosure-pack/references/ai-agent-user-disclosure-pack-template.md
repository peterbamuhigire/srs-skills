# AI Agent User Disclosure Pack Template

## 1. Per-feature Disclosure Blocks

### Inbox Triage agent

**What it does** — Reads your inbox, labels each thread, archives non-actionable threads, and saves a draft reply for threads that need one.

**What it does not do** — It does not send any email. It does not delete threads. It does not contact people outside your workspace.

**Authority** — It acts on your behalf in your own inbox only. It cannot read other users' inboxes. It cannot label or archive threads you cannot label or archive yourself.

**Approval** — You see the proposed labels, archives, and drafts before they apply. Click *Apply* to accept all, *Edit* to change them, or *Cancel* to discard them.

**Undo** — Use *Restore* in the Audit drawer to undo any label or archive within 7 days. Drafts can be deleted from your Drafts folder.

**What is not reversible** — Nothing in this feature is irreversible. Drafts never send themselves.

**Contesting an action** — Click *Report* on any agent action to flag it for review. We will respond within 2 working days.

### Daily Reconciliation agent (Enterprise)

**What it does** — Matches the previous day's bank-feed entries against your ledger and posts matching ledger entries.

**What it does not do** — It does not move money. It does not write outside the ledger account it has access to. It does not change any entry it did not create.

**Authority** — It acts under the Finance Operator role granted by your workspace admin. It can only post entries inside the configured ledger scope.

**Approval** — It runs unattended within an admin-configured envelope (max-cost, scope). The morning digest shows what it did; click *Reverse* on any row to undo.

**Undo** — Every entry the agent posts has a paired *Reverse* tool that an admin can run from the Audit drawer.

**What is not reversible** — No agent action in this feature is irreversible. All entries are compensable.

**Contesting an action** — Use *Flag* in the morning digest; finance team responds the same working day.

## 2. Notification Design

### When it shows

- After every agent action with a user-visible side-effect.
- Aggregated when a run completes (one notification per run, not one per action).

### Where it shows

- Inbox banner for inbox-scope features.
- Audit drawer (persistent, accessible from app shell).
- Email digest (daily, opt-out per user).

### What it shows

```
[Agent: Inbox Triage]
12 threads triaged on May 11, 2026 at 06:00 UTC

   - 8 labelled
   - 3 archived
   - 1 draft saved (not sent)

[ View details ]   [ Undo all ]   [ How this worked ]
```

### Dismissal

User must acknowledge (click). Notifications do not auto-dismiss. They remain in the Audit drawer for 90 days minimum.

## 3. Contestation Path

| Step | Action |
|------|--------|
| 1 | User clicks *Report* on the audit row. |
| 2 | The report form pre-fills (action, time, agent run id). User adds a description. |
| 3 | Our system pulls the audit excerpt for that run. |
| 4 | A human reviewer responds within 2 working days (1 working day for Enterprise tier with irreversible side-effect). |
| 5 | If the action was incorrect: undo if possible, apology, and the case is added to the agent eval rig as a regression case. |
| 6 | Escalation: workspace admin can request a senior reviewer; legal escalation for regulated decisions. |

## 4. Regional Disclosures

### EEA (EU AI Act Art. 13)

Prominent notice at first use: "This feature uses an AI agent. The agent operates within the limits described above. You can disable it at any time. For more about how we use AI, see our Responsible AI Declaration."

Default for L2+ in EEA: **off**.

### UK (ICO)

Same notice as EEA. Reference to the AI accountability statement in the Trust Center.

### US

Default: on at L1 with disclosure. State-specific disclosures:

- Colorado (CO AI Act 2026): consumer notice for any agent making consequential decisions; right to opt out; right to explanation.
- New York City: if the agent is used for employment-related decisions, bias-audit publication.

### Africa

- Uganda (DPPA): plain-language notice; specific consent if special-category data processed.
- Ghana (DPA): same.
- Nigeria (NDPR): same.

## 5. Copy String Tables

Per-locale CSV (excerpt):

| key | en-US | en-GB | fr-FR | de-DE |
|-----|-------|-------|-------|-------|
| `agent.notif.title` | "Agent: %s" | "Agent: %s" | "Agent : %s" | "Agent: %s" |
| `agent.notif.summary` | "%d actions on %s" | "%d actions on %s" | "%d actions le %s" | "%d Aktionen am %s" |
| `agent.notif.undo` | "Undo all" | "Undo all" | "Tout annuler" | "Alles rückgängig machen" |
| `agent.notif.howThisWorked` | "How this worked" | "How this worked" | "Comment ça marche" | "Wie das funktioniert" |
| `agent.report.cta` | "Report" | "Report" | "Signaler" | "Melden" |

## 6. Review Cadence

- Per release: re-review for any feature whose autonomy level, action catalogue, or scope changed.
- Quarterly: language review with Legal and DPO.
- After any SEV2+ agent incident: re-review the disclosure of the affected feature.

# 8. GL Hash Chain Design

## 8.1 Purpose

Business Rule BR-013 requires that every entry in the general ledger is cryptographically linked to the previous entry in the same account, making any retrospective tampering mathematically detectable. This satisfies the Uganda Companies Act and Uganda Income Tax Act requirements for tamper-evident financial records with 7-year retention.

## 8.2 Hash Chain Mechanism

Each row in `tbl_gl_journal_lines` carries a `entry_hash` column computed as follows:

$$\text{entry\_hash}_n = \text{SHA-256}(\text{entry\_hash}_{n-1} \| \text{journal\_id} \| \text{account\_id} \| \text{debit} \| \text{credit} \| \text{posted\_at})$$

Where:
- $\|$ denotes string concatenation with a fixed delimiter (`|`)
- $\text{entry\_hash}_{n-1}$ is the hash of the previous journal line on the same account (`account_id`)
- `debit` and `credit` are formatted as fixed-precision decimal strings (e.g., `5000000.00`)
- `posted_at` is the UTC ISO 8601 timestamp of the journal posting

The genesis entry for each account (the first ever journal line on that account) uses a fixed sentinel value as `entry_hash_0`:

$$\text{entry\_hash}_0 = \text{SHA-256}(\text{"BIRDC-ERP-GENESIS"} \| \text{account\_id})$$

## 8.3 Columns Included in the Hash

The following columns of `tbl_gl_journal_lines` are included in the hash computation:

| Column | Included | Notes |
|---|---|---|
| `id` | No | Auto-increment; not part of business data |
| `journal_id` | Yes | Links to `tbl_gl_journals` |
| `account_id` | Yes | The GL account being credited or debited |
| `debit` | Yes | Formatted as `DECIMAL(18,2)` string |
| `credit` | Yes | Formatted as `DECIMAL(18,2)` string |
| `posted_at` | Yes | UTC timestamp, ISO 8601 |
| `narration` | No | Free text; excluded to prevent cosmetic edit detection false positives |
| `entry_hash` | Stores result | Not an input to its own hash |
| `prev_hash` | Yes | The `entry_hash` of the previous line on this account |

## 8.4 Hash Chain per Account

The chain is maintained **per GL account** (not per journal). Each account maintains its own independent chain. This allows `GLService::verifyHashChainIntegrity()` to check a single account's history in O(n) time without traversing all accounts.

```
Account 1010 (Bank):
  Line 1: entry_hash = SHA256(GENESIS | 1010)
  Line 2: entry_hash = SHA256(Line1.hash | journal_id | 1010 | debit | credit | posted_at)
  Line 3: entry_hash = SHA256(Line2.hash | ...)
  ...
  Line n: entry_hash = SHA256(Line(n-1).hash | ...)
```

## 8.5 Integrity Check Trigger

`GLService::verifyHashChainIntegrity(accountId)` is triggered:

1. **On demand** by the Finance Director or OAG auditor via the audit interface.
2. **Automated nightly batch** (02:30 EAT) — scans all accounts modified in the previous 24 hours.
3. **Post-import** — after any data migration or bulk import, the integrity check runs automatically on all affected accounts.

The verification traverses the account's journal lines in chronological order, recomputes each hash, and compares it to the stored `entry_hash`. Any mismatch is reported as an integrity violation with the specific `journal_id`, `account_id`, and timestamp.

## 8.6 Response to a Detected Integrity Violation

1. The violation is logged immediately in `tbl_audit_log` with severity `CRITICAL`.
2. An alert is sent via email and SMS to the Finance Director, IT Administrator, and BIRDC Director.
3. The affected account is flagged `CHAIN_BROKEN` in `tbl_coa_accounts.integrity_status`.
4. The Finance Director and IT Administrator must jointly authorise any remediation action, which is itself logged as an audit entry.
5. No further journal posts to a `CHAIN_BROKEN` account are permitted until the integrity status is cleared by an authorised action.

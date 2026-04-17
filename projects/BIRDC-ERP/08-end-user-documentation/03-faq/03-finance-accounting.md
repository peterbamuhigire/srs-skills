# Topic 3: Finance and Accounting

---

**Q14. Can I edit a journal entry after it has been posted?**

No. A posted journal entry cannot be edited or deleted. This is a fundamental control required by Uganda Companies Act and the BIRDC design covenant (DC-003). The General Ledger uses a cryptographic hash chain — any modification to a posted entry would break the chain and be immediately detectable by the system and by auditors. If a posted journal entry contains an error, the correct approach is to create a reversing entry (a new journal entry that cancels the original) and then post the correct entry. The Finance Director approves both entries. The original entry and the correction remain permanently visible in the audit trail.

---

**Q15. How do I view PIBID parliamentary accounts separately from BIRDC commercial accounts?**

The system supports three viewing modes for all financial reports:

- **PIBID Parliamentary:** shows only PIBID government accounts, budget votes, and parliamentary expenditure.
- **BIRDC Commercial:** shows only BIRDC IFRS commercial accounts.
- **Consolidated:** shows both side by side, clearly labelled.

To switch modes, go to any financial report (Trial Balance, P&L, Balance Sheet) and use the **Accounting Mode** selector at the top of the report screen. The Finance Director can run both modes simultaneously in two browser tabs.

---

**Q16. What does the hash chain integrity check do?**

The hash chain integrity check verifies that no General Ledger entry has been tampered with since it was posted. Every GL entry references a cryptographic fingerprint (hash) of the previous entry. If any historical record is changed — even by a direct database edit — the chain breaks at that point. To run the check:

1. Click **Finance** then **Audit** then **Hash Chain Integrity Check**.
2. Click **Run Check**.
3. The system scans all GL entries and reports either "Chain Intact — all records verified" or lists the specific entries where the chain is broken.

The Finance Director or external auditor (OAG Uganda) can run this check at any time without notice. A broken chain is a serious audit finding and must be investigated immediately.

---

**Q17. Can I post to a closed accounting period?**

No. Once an accounting period is closed, no journal entries can be posted to it. This protects the integrity of approved financial statements. If you need to correct an entry in a closed period, the Finance Director must approve a manual adjustment in the current open period with a clear description referencing the original transaction date. The adjustment is visible in both the current period and in the audit trail cross-referencing the original period.

---

**Q18. Why does the system show two different profit figures — one parliamentary and one commercial?**

PIBID parliamentary accounts follow government accounting rules (budget vs. expenditure reporting to Parliament). BIRDC commercial accounts follow International Financial Reporting Standards (IFRS) for the commercial operation. The two sets of accounts have different chart structures, different period ends, and different reporting purposes. Both are maintained in the same system simultaneously. The "profit" shown in parliamentary mode is a budget surplus or deficit against the parliamentary vote. The "profit" in commercial mode is the commercial net income per IFRS. Neither figure is wrong — they measure different things.

---

**Q19. How do I run the GL hash chain check to satisfy an OAG audit request?**

See Q16 above. The Finance Director or IT Administrator runs the check from **Finance → Audit → Hash Chain Integrity Check**. The result can be exported to PDF for inclusion in the audit file. The PDF includes the timestamp, the user who ran the check, the number of entries scanned, and the result (intact or broken, with details).

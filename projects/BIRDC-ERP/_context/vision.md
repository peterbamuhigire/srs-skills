# Product Vision — BIRDC ERP

**Project:** BIRDC ERP
**Client:** PIBID / BIRDC, Nyaruzinga hill, Bushenyi District, Western Uganda
**Consultant:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Date:** 2026-04-05

---

## Vision Statement

A purpose-built, single-tenant enterprise resource planning system that gives BIRDC and PIBID
complete operational visibility and control over Uganda's only industrial-scale banana
processing enterprise — simultaneously satisfying parliamentary accountability requirements,
commercial IFRS reporting, cooperative farmer management, and food export compliance, in a
system owned and operated by Ugandans, hosted on BIRDC's own infrastructure.

## Strategic Goals

1. **Operational unity** — replace fragmented spreadsheets and manual registers with one system covering all 17 operational domains, from cooperative farmer delivery to export Certificate of Analysis.
2. **Financial integrity** — provide a dual-mode accounting system that tracks PIBID parliamentary budget votes and BIRDC commercial accounts simultaneously, with an immutable, hash-chained audit trail meeting Uganda Companies Act and Income Tax Act 7-year retention requirements.
3. **Agent accountability** — eliminate the cash accountability gap in BIRDC's 1,071-strong field agent network through real-time agent cash balance tracking and automated FIFO remittance allocation.
4. **Circular economy visibility** — provide the first ERP mass balance for Uganda's banana value chain: every kilogramme of input matooke accounted for across primary products, by-products (biogas from peels, bio-slurry from waste water), and scrap.
5. **Government replicability** — build every BIRDC-specific rule in configuration tables, not code, so the system can be redeployed for any Uganda government agro-processing entity without a rebuild.

## Design Covenant (7 Binding Constraints)

All requirements generated must be validated against all 7:

- **DC-001:** Zero mandatory training for routine operations. Every screen a staff member uses daily must be self-discoverable. A newly hired accounts assistant must post a journal entry correctly without reading a manual.
- **DC-002:** Configuration over code. All business rules — PAYE tax bands, NSSF rates, recipe ingredients, commission rates, PPDA procurement thresholds, price lists — configurable via the UI by the Finance Director or IT Administrator, with no developer involvement.
- **DC-003:** Audit readiness by design. Every financial transaction creates an immutable audit trail automatically. The external auditor finds every journal entry, invoice, and payment with full source traceability. 7-year retention enforced.
- **DC-004:** Dual-mode accounting. PIBID parliamentary budget votes and BIRDC commercial IFRS accounts are tracked simultaneously in the same system. Consolidated and separated reporting always available.
- **DC-005:** Offline-first where it matters. Factory gate POS, Farmer Delivery App, and Warehouse App function completely offline. Data syncs when connectivity returns. Critical for Bushenyi intermittent connectivity.
- **DC-006:** Data sovereignty. All BIRDC data — farmer records, financial accounts, production data, employee records — stored on BIRDC's own servers in Uganda. No SaaS vendor holds data as leverage.
- **DC-007:** Replicable by design. Every BIRDC-specific configuration is isolated in configuration tables. The same codebase can be redeployed for Uganda Coffee Development Board, National Enterprise Corporation, or any government agro-processor by changing configuration, not code.

## The Organisation

PIBID was established in 2005 by presidential directive. Over 20 years and UGX 200 billion (~$54M) in government investment, it built the Nyaruzinga factory, developed the Tooke brand, and established 6,440+ cooperative farmers. It has now transitioned to BIRDC — commercially oriented, pursuing export orders to South Korea, Saudi Arabia, Qatar, Italy, and the United States, while remaining publicly funded and accountable to Parliament.

**Dual nature:** government initiative (PPDA procurement, parliamentary budget votes, public sector accounting) + commercial enterprise (IFRS, export markets, private sector financial discipline).

## Success Criteria

- All 17 modules live and in daily use within the delivery roadmap timeline
- Finance Director can generate Trial Balance, P&L, and Budget vs. Actual for both parliamentary and commercial modes at any moment without period closing
- Procurement Manager can trace every kilogramme of matooke from farm delivery through processing to finished product sale
- Every one of the 1,071 agents' cash balances visible in real time at all times
- External audit (OAG Uganda) requires no manual reconciliation — full audit trail in system
- System passes PPDA procurement documentation compliance review
- Replication framework documented and demonstrated to one additional government entity

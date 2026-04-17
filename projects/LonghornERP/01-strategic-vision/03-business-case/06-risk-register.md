# Business Risk Register

*Likelihood and Impact ratings: H = High, M = Medium, L = Low. Sourced primarily from `_context/gaps.md` HIGH-priority gaps and strategic context.*

## Risk Table

| Risk ID | Description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| BRK-001 | **URA EFRIS API unavailability or specification change** (GAP-001). URA may change the EFRIS API without advance notice, breaking invoice submission for all Uganda clients. | H | H | Obtain sandbox credentials early; build an abstraction layer so EFRIS connector can be updated independently of core Sales/Accounting modules. Monitor URA developer communications. |
| BRK-002 | **Multi-tenancy data isolation breach** (GAP-004). A defect in `tenant_id` enforcement exposes one tenant's data to another, triggering regulatory liability and client loss. | L | H | Commission independent security review before first tenant onboarding. Automated test suite must include cross-tenant isolation assertions on every data access path. Formal sign-off required before go-live. |
| BRK-003 | **Uganda Data Protection and Privacy Act 2019 non-compliance** (GAP-007). Processing employee medical and financial data without adequate legal basis or sub-processor agreements exposes Chwezi Core Systems to regulatory penalty. | M | H | Commission legal review before HR and Payroll module is activated for any client. Implement consent capture, data retention controls, and a sub-processor register. |
| BRK-004 | **Statutory format changes invalidate payroll and VAT exports** (GAP-002, GAP-003). URA PAYE return formats and NSSF upload formats change without notice, causing client compliance failures. | H | M | Subscribe to URA and NSSF developer notification channels. Build statutory export format as a versioned configuration template, not hardcoded logic, so updates require configuration changes only. |
| BRK-005 | **Module dependency misconfiguration causes data corruption** (GAP-005). Activating Manufacturing without Advanced Inventory, or Cooperative Procurement without Inventory, produces undefined behaviour and potentially corrupted stock records. | M | H | Define and enforce a formal module dependency graph before activation logic is implemented. Prevent activation of a dependent module unless its prerequisites are active. Display dependency errors at activation time with a clear resolution path. |
| BRK-006 | **Slow sales adoption — Phase 1 client target missed.** The 60–100 client target within 12 months is not achieved, leaving MRR below break-even and threatening Phase 2 funding. | M | H | Build 10 anchor clients with full case studies before public launch. Use EFRIS compliance mandate as a high-urgency sales trigger. Offer annual billing upfront discounts to accelerate pipeline conversion. |
| BRK-007 | **White-labelling and source code strategy undecided** (GAP-015, GAP-018). Absence of a white-label policy prevents upselling to resellers; absence of a source code strategy delays enterprise procurement conversations where open-source audits are required. | M | M | Resolve both decisions before Phase 1 client onboarding begins. Document outcome in `_context/vision.md` and propagate to the Business Case and Platform SRS. |
| BRK-008 | **Mobile money API credentials delayed** (GAP-011, GAP-012). MTN MoMo Business bulk payment and M-Pesa Daraja B2C credentials are gatekept by the providers and may take 4–12 weeks to obtain, delaying payroll and cooperative payment features. | M | M | Begin MTN MoMo and Safaricom developer portal registration during the specification phase, not the development phase. Treat API credential acquisition as a critical-path dependency on the project schedule. |

## Risk Ownership

All risks in this register are owned by Peter Bamuhigire (Lead Developer, Chwezi Core Systems) until a formal risk owner is assigned per risk item. Review this register at each phase-gate sign-off.

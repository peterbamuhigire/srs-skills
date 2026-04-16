---
gate: phase03
checks:
  - phase03.architecture_decisions_recorded
  - phase03.interfaces_have_contracts
  - phase03.data_model_has_keys
  - phase03.nfrs_link_to_design_choices
  - phase03.security_threat_model_present
  - phase03.iot_signal_inventory_present
clause_refs:
  - standard: "ISO/IEC/IEEE 42010:2011"
    clause: "5.3"
---

# Phase 03 Deterministic Gate

Before finalizing design artifacts, confirm clause-level proof per IEEE 1016, ISO 42010, and applicable NFR standards.

1. **Architecture Viewpoints**
   - `projects/<ProjectName>/03-design-documentation/01-high-level-design/HLD.md` references IEEE 1016 viewpoints: conceptual, module, data, deployment.
   - Each viewpoint cites one or more clauses (e.g., IEEE 1016 §5.2 for component decomposition, ISO 42010 for architecture rationale).

2. **Rationale and ADR Evidence**
   - Low-level design (`LLD`) includes architecture decisions and alternatives referencing IEEE 1016 §6 and ISO 42010 decision rationale.
   - Link to ADR entries stored under `projects/<ProjectName>/docs/adr/` or similar; every ADR references a requirement ID and constraint clause.

3. **Traceability to Requirements**
   - API specs (`03-api-specification`), database design, UX specs each include a traceability appendix mapping components/interfaces back to SRS IDs; cite clauses from IEEE 29148 or domain standards (e.g., WCAG, ISO 9241 for UX).

4. **Design Constraints**
   - Document constraints referencing ISO/IEC 25010 or applicable regulatory requirements (HIPAA, PCI DSS) with clause citations.

5. **Verification**
   - Run `03-design-documentation/06-infrastructure-design` decision gate and `03-design-documentation/07-iot-system-design` (if applicable) and log clause-specific findings.

Store proof of these checks in `docs/deterministic-governance.md` or the phase manifest before moving to Phase 05.

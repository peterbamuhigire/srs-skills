# Quality Standards — GarageFlow

## Applicable frameworks

- **IEEE 830-1998** — SRS content and structure.
- **IEEE 1012-2016** — V&V planning and execution.
- **IEEE 1233-1998** — system requirements guidance.
- **IEEE 610.12-1990** — software engineering terminology.
- **ASTM E1340-96** — user documentation standards.
- **PCI-DSS v4.0** — cardholder data protection (tokenization-only scope).
- **ISO 3779 / ISO 3780** — VIN content and manufacturer codes.
- **SAE J1979 / ISO 15031** — OBD-II diagnostic trouble codes.
- **GDPR** — applies to any EU-resident customer data.
- **Uganda DPPA 2019** — applies to any Ugandan tenant or customer.
- **Local e-invoicing regimes** (per tenant): EFRIS (Uganda), KRA eTIMS (Kenya), RRA EBM (Rwanda), ZATCA (Saudi Arabia), CFDI (Mexico).

## Non-functional thresholds (baseline)

See `domains/automotive/references/nfr-defaults.md` — NFR-AUTO-001 through NFR-AUTO-015 apply. Tenant-specific tightening is permissible at Enterprise tier.

## V&V gate policy

- Every FR must carry a deterministic test oracle.
- Every NFR must carry a measurable metric with threshold and measurement method.
- No vague adjectives (fast, intuitive, reliable, robust, seamless) without an IEEE-982.1 metric.
- Hybrid-synchronization gate must pass before any Phase 07 Agile artifact.

## Tooling

- `python -m engine validate projects/GarageFlow` — kernel gate.
- `python -m engine validate-skills` — skill-content check.
- `python -m engine sync projects/GarageFlow` — registry regeneration.
- `python -m engine baseline snapshot projects/GarageFlow --label v<phase>` — phase-closure baseline.

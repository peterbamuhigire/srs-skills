# Domains Index

Domain knowledge bases provide baseline requirements, regulations, architecture
patterns, and feature defaults for specific industry verticals. When a consultant
starts a new project and selects a domain, Claude reads from this knowledge base
to auto-inject `[DOMAIN-DEFAULT]` tagged requirements into the project scaffold.

## Available Domains

| Domain | Key Standards | Risk Level | Directory |
|---|---|---|---|
| Healthcare | HIPAA, HL7/FHIR, FDA 21 CFR | High | [healthcare/](healthcare/INDEX.md) |
| Finance | PCI-DSS, SOX, AML/KYC | High | [finance/](finance/INDEX.md) |
| Education | FERPA, COPPA | Medium | [education/](education/INDEX.md) |
| Retail | PCI-DSS, GDPR | Medium | [retail/](retail/INDEX.md) |
| Logistics | DOT, ISO 28000 | Medium | [logistics/](logistics/INDEX.md) |
| Government | FISMA, FedRAMP, GDPR | High | [government/](government/INDEX.md) |
| Agriculture | Uganda DPA, EUDR, GlobalGAP, Employment Act | Medium | [agriculture/](agriculture/INDEX.md) |

## How Domain Injection Works

1. Consultant selects a domain when running "start a new project"
2. Claude reads `domains/<domain>/INDEX.md` and `references/nfr-defaults.md`
3. `[DOMAIN-DEFAULT]` tagged blocks are injected into relevant section stubs
4. `_context/domain.md` is pre-populated with the domain profile
5. Consultant reviews tagged blocks — keep, edit, or delete before building `.docx`

## Domain Injection Tag Format

```markdown
<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-001: Requirement Title
The system shall...
<!-- [END DOMAIN-DEFAULT] -->
```

## Adding a New Domain

1. Create `domains/<domain-name>/` directory
2. Add `INDEX.md` following the format in any existing domain
3. Add `references/` subdirectory with: `regulations.md`, `architecture-patterns.md`, `security-baseline.md`, `nfr-defaults.md`
4. Add `features/` subdirectory with one `.md` per feature module
5. Register the domain in this `INDEX.md` table

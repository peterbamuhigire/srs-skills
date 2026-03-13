# Government: Architecture Patterns

## Zero-Trust Architecture

- No implicit trust is granted to any user, device, or network segment — including internal networks
- Every access request must be authenticated, authorized, and continuously validated
- Micro-segmentation: workloads are isolated; lateral movement between systems requires explicit policy authorization
- All traffic, including east-west (internal), must be encrypted and inspected

Zero-Trust policy evaluation per request:
```
Identity Verification → Device Posture Check → Least-Privilege Authorization →
Session Risk Scoring → Resource Access → Continuous Monitoring
```

- Implement per NIST SP 800-207 (Zero Trust Architecture) guidance

## Data Sovereignty (In-Country Data Residency)

- All citizen PII and government records must be stored on infrastructure physically located within the national jurisdiction
- Cloud services must contractually guarantee data residency with audit rights
- Data replication and backup must also comply with residency requirements — no cross-border replication without legal basis
- Egress monitoring must alert when data transfers are initiated to foreign IP address ranges

## Citizen Identity Proofing (NIST SP 800-63)

| Assurance Level | Description | Applicable Use Cases |
|---|---|---|
| IAL1 | Self-asserted identity; no proofing required | Anonymous or low-risk services |
| IAL2 | Remote or in-person identity proofing; evidence verification required | Benefits applications, permit applications |
| IAL3 | In-person proofing with biometric binding | High-value transactions, credentialing |

- Systems handling benefit determinations, tax records, or law enforcement data must require IAL2 minimum
- Identity proofing must be performed via a trusted credential service provider (CSP) per NIST SP 800-63A
- Login.gov (U.S. federal) or national equivalent must be the preferred identity provider

## Multi-Factor Authentication (Mandatory)

- MFA is mandatory for all government system users without exception (OMB M-22-09)
- Phishing-resistant MFA (FIDO2/WebAuthn, PIV/CAC) required for privileged users and high-impact systems
- SMS-based OTP is not acceptable for high-impact systems (NIST SP 800-63B)
- MFA bypass procedures require documented justification, supervisor approval, and audit logging

## Air-Gapped Systems for Classified Data

- Systems processing classified information (SECRET, TOP SECRET) must operate on isolated networks
- No connection to the public internet or unclassified networks; data transfer via approved removable media only
- Cross-Domain Solutions (CDS) must be used for any data transfer between classification levels
- Physical access controls (man-trap, biometric) required for classified system rooms

## Audit Logging Architecture

Every system action involving citizen records must produce an immutable log entry:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "user_id": "string",
  "user_role": "string",
  "agency": "string",
  "action": "READ | WRITE | DELETE | EXPORT | FOIA_RESPONSE",
  "record_type": "CitizenRecord | CaseFile | ContractDocument | ...",
  "record_id": "string",
  "classification_level": "UNCLASSIFIED | CUI | SBU",
  "ip_address": "string",
  "outcome": "SUCCESS | FAILURE | DENIED"
}
```

- Audit logs must be write-once, stored in a separate hardened log management system
- Minimum retention: 3 years general, 7 years for financial records (per OMB guidance)

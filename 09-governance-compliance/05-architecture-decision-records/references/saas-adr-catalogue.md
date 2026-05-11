# SaaS ADR Catalogue

Reference list of the ADR families a SaaS engine should expect to produce, with a one-line trigger and template-pointer per family.

## Tenancy & isolation

| ADR | Trigger | Template |
|-----|---------|----------|
| Tenancy pattern per microservice | every microservice in scope | `03-design-documentation/10-saas-multi-tenancy-architecture-spec/references/saas-tenancy-decision-template.md` |
| Control-plane / application-plane boundary | once per system | same template |
| Data-residency per region | when EU/UK/APAC commitments made | tenancy template |
| Per-tenant KMS key (Enterprise) | when offering BYOK or per-tenant keys | tenancy template |

## Pricing & packaging

| ADR | Trigger |
|-----|---------|
| Value metric chosen | once, revisited yearly |
| Freemium yes/no | once, revisit if churn / conversion shifts |
| Credit-card-up-front yes/no | once |
| Price raise event | every price raise |
| Grandfathering policy change | every change |
| Tier introduction or retirement | every change |
| White-label policy | once if relevant |
| Vertical expansion | every new vertical |

## GTM & commercial

| ADR | Trigger |
|-----|---------|
| Sales methodology selection | per product line |
| Channel commit (single-channel discipline) | per product line |
| Partner / reseller policy | once |
| Discount-authority schedule | once, revisit yearly |

## Operations & SLO

| ADR | Trigger |
|-----|---------|
| Per-tier SLO targets | once, revisit yearly |
| Error-budget freeze rules | once |
| Incident-severity matrix | once, revisit after major incident |
| Status-page protocol | once |

## Compliance

| ADR | Trigger |
|-----|---------|
| Attestation target (SOC 2 / ISO 27001 / etc) | per attestation |
| Sub-processor addition | every addition |
| Retention policy per data class | once, revisit per region |
| Breach-notification SLA | once |
| Legal-hold policy | once |

## Engineering

| ADR | Trigger |
|-----|---------|
| Schema migration approach (online vs offline) | per major migration |
| Background-job framework | once per system |
| Feature-flag system | once |
| Event bus selection | once |
| Identity provider / IdP federation | once + per major change |

## AI features

The full AI ADR family (17 required slots) is owned by `09-governance-compliance/17-ai-adr-catalogue/`. The slots listed below are the ones every AI-feature SaaS must record; promotion is from the AI ADR catalogue into this central register.

| ADR | Trigger | Template |
|-----|---------|----------|
| Model Gateway as sole egress | once | `17-ai-adr-catalogue/references/ai-adr-templates.md` |
| Primary model per AI feature | per feature; revisit per model bump | same |
| Fallback model per AI feature | per feature | same |
| RAG vs fine-tune vs agent | per feature | same |
| Vector store choice | once per product | same |
| Embedding model choice | once + per version bump | same |
| Eval threshold (regression tolerance) | once, revisit yearly | same |
| Abstain policy | once per feature | same |
| Content filter chain | once, revisit on filter change | same |
| Prompt registry change protocol | once | same |
| Conversation log retention | once per region | same |
| Training-data exclusion policy | once + per provider change | same |
| Cross-tenant retrieval prohibition mechanism | once | same |
| Judge-LLM selection | once + on swap | same |
| Cost ceiling and throttle policy | once per tier; revisit on pricing change | same |
| Rollback trigger set | once + after every incident | same |
| Retraining / re-evaluation trigger | once per feature | same |

## Each ADR carries

- Context.
- Decision.
- Status (proposed / accepted / superseded).
- Drivers (with measurable thresholds where applicable).
- Alternatives considered.
- Consequences (positive, negative, operational).
- Evidence pointers.
- Sign-off owners.

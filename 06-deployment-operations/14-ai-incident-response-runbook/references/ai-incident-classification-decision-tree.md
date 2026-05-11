# AI Incident Classification Decision Tree

Operator-grade flowchart. Use this in the first 5 minutes to determine failure class and severity. The numbered nodes feed directly into the per-failure-class procedures (section 4.x of the response runbook).

## Top-level question

**Q0. Is the AI output reaching customers right now?**

- Yes -> go to Q1.
- No (purely internal experiment) -> SEV4; log to eval-tracker; not an incident.

## Q1. What is failing?

| Symptom | Likely class | Next |
|---------|--------------|------|
| AI took an action with real-world side effect | agent-action incident | go to Q2 (autonomy) |
| AI produced output that is wrong / unsupported | hallucination or prompt / model regression | go to Q3 |
| AI returned content that violates policy (PII, hate, illegal) | jailbreak / injection | go to Q4 |
| AI cost spiked | cost runaway | go to Q5 |
| AI is slow / unavailable | parent SaaS IR (availability) | hand off; AI IR may still join |
| AI cites wrong sources | retrieval drift | section 4.10 |
| Eval was green but production is red | eval drift confounder | section 4.11 |

## Q2. Autonomy / blast-radius

| Was the action ... | Severity floor |
|--------------------|----------------|
| advisory (human acted on output) | SEV2 |
| assistive (human reviewed then confirmed) | SEV2 |
| autonomous with rollback (action reversible) | SEV2; SEV1 if cross-tenant or fundamental-rights impact |
| autonomous-irreversible (mail sent, money moved, record destroyed) | SEV1 |

Section 4.8 procedure.

## Q3. Is the regression on our side or the provider's?

- Our prompt deploy at T -> prompt-drift; section 4.2.
- Our model fine-tune / pin update at T -> model regression (our side); section 4.3.
- No deploy on our side; provider notice or provider status -> model regression (provider); section 4.3.
- No deploy anywhere; production traffic distribution shifted -> training-data / distribution shift; section 4.9.
- Diffuse, multi-factor -> declare hallucination spike (section 4.1); investigate.

## Q4. Direct or indirect injection?

- Adversarial user input crafting the prompt -> direct; section 4.4.
- Injection arrived via retrieved document, tool response, or user upload that the model treated as instruction -> indirect; section 4.5.

## Q5. Whose tenant is over budget?

- Single tenant -> per-tenant throttle; section 4.7.
- Multiple tenants / platform-wide -> SEV1 cost runaway; section 4.7.
- Abuse suspected -> joint with security IR.

## Q6. Severity adjustments after Q1-Q5

- **Cross-tenant leakage suspected or confirmed** -> upgrade to SEV1 regardless of failure class. Start GDPR Art. 33 clock (72 h) on confirmation. Page DPO.
- **High-risk EU AI Act feature** -> start Art. 73 assessment clock at hour 2 (window depends on harm class: immediate for wide-scale or fundamental rights; 10 d for death/serious harm; 15 d otherwise).
- **Regulator inquiry already received** -> upgrade severity by one floor; loop legal + exec sponsor immediately.
- **Press inquiry or social-media virality** -> upgrade by one floor; loop comms lead and exec.

## Q7. Containment selection

Pick one or more. Default conservative for SEV1.

| Failure class | Default containment | Backup |
|---------------|---------------------|--------|
| Hallucination spike | prompt rollback | model fallback, then abstain mode |
| Prompt drift | prompt rollback | n/a |
| Model regression | model fallback | abstain mode if no fallback yet |
| Injection (direct) | abstain mode | kill switch |
| Injection (indirect via retrieval) | index pinning + read-only mode | abstain mode |
| Injection (indirect via tool) | read-only mode | kill switch |
| Tool-chain failure | read-only mode | abstain mode |
| Cost runaway | per-tenant throttle (cost runbook) | model fallback, then abstain |
| Agent-action incident | read-only mode + kill switch | n/a |
| Distribution shift | per-segment abstain | per-segment prompt rollback |
| Retrieval drift | index pinning | abstain on RAG outputs |
| Eval drift | release freeze + revert | n/a |

## Q8. What clocks just started?

| Trigger | Clock |
|---------|-------|
| Customer-visible quality issue declared | customer-comms initial window (15 min SEV1 / 30 min SEV2) |
| Cross-tenant leakage confirmed | GDPR Art. 33 (72 h) |
| High-risk Art. 73 limb assessed positive | Art. 73 reporting window (2 d / 10 d / 15 d depending on harm class) |
| US state-level applicable | per state (NYC AEDT, CO SB24-205, CA ADMT) — see regulator-notification doc |
| African regulator applicable | per regulator (Kenya ODPC, Nigeria NDPC, POPIA) — see regulator-notification doc |

## Q9. Who is on this call?

| Role | Required from severity |
|------|------------------------|
| IC | SEV1, SEV2 |
| AI lead | SEV1, SEV2 |
| SRE on-call | all SEV |
| Comms lead | SEV1, SEV2 |
| Scribe | SEV1, SEV2 |
| Security on-call | confirmed or suspected injection / exfil |
| DPO / legal | confirmed cross-tenant leakage; Art. 73 trigger |
| CSM | SEV1/2 affecting Enterprise |
| FinOps | cost runaway primary |
| Exec sponsor | SEV1; Art. 73; press inquiry |

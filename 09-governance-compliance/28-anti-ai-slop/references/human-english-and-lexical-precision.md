# Human English and Lexical Precision

Parent skill: [28-anti-ai-slop](../SKILL.md). Also loaded by
`09-ux-content-and-form-specification`, end-user documentation skills and
`AGENTS.md`. Load it when drafting or reviewing requirements, UX content,
user manuals, FAQs, release notes, runbooks, training material or support
messages. It sits alongside the IEEE/ISO requirement-quality rules,
traceability, accessibility and security controls; it never overrides them.

## 1. Standard

Write for the person who must build, test, operate, approve or use the
product. Human technical writing is exact, not casual: it names actors,
states, intent, constraints and consequences. Interface text is warm enough
to help and exact enough not to mislead. The target register is polished,
literate and restrained. Never add typos, slang, unexplained humour, ornate
diction or fake warmth to make text seem human.

## 2. Five-pass procedure

1. **Frame.** Name the reader, task, system state, decision and required
   outcome.
2. **Choose the artefact.** Requirement, user story, API description,
   runbook, manual, FAQ or microcopy; each has its own structure.
3. **Trace.** Link facts, rules, fields, standards and examples to project
   evidence; mark `[CONTEXT-GAP]` where evidence is missing.
4. **Revise.** Unambiguous grammar, controlled terminology, active actors,
   parallel lists, restrained sentence rhythm, one centre of gravity per
   paragraph.
5. **Proof.** Identifiers, units, examples, links, punctuation, alt text and
   test oracles; read user-facing text aloud in its screen or message context.

## 3. Language rules

- British English by default unless the approved product, buyer, legal or
  locale brief says otherwise. Preserve approved product, local, legal and
  technical terms (for example "mobile money", "NIN", "EFRIS").
- Prefer the common word when it is exact. Use specialist vocabulary only
  when necessary, defined in the glossary and used consistently.
- Check the grammatical frame and collocation of load-bearing terms: "raise
  an invoice", "post a journal", "approve a requisition". Do not swap in a
  thesaurus synonym because it sounds sophisticated; a synonym in a
  specification reads as a second concept.
- Check agreement, articles, tense, pronoun reference, relative clauses,
  prepositions, parallelism, dangling modifiers, punctuation, spelling and
  sentence boundaries.
- Avoid idioms, figurative claims, vague intensifiers and culturally narrow
  phrasing in requirements, error states, runbooks, security, accessibility
  and anything that may be translated.
- Calibrate claims: state what is known, what is assumed and what is
  unverified. Polished prose must not hide an unsupported claim, a missing
  owner, an unmeasured adjective or an unresolved decision.
- For design rationale, test privately: decision, evidence, trade-off,
  failure case, implication.

## 4. Requirements check

For each requirement confirm actor, trigger, behaviour, condition and
observable outcome, then replace "fast", "intuitive", "seamless", "robust"
and similar words with a measurable condition.

| Weak | Precise |
|---|---|
| The system should quickly show the balance. | When a signed-in member opens **Savings**, the system shall display the current balance within 2 s at P95 on a 3G connection. |
| Users can easily reset passwords. | The system shall let a member reset a password from the sign-in screen using a one-time code sent to the registered phone number; the code shall expire after 10 minutes. |

## 5. Microcopy test

Every user-facing message answers, as space allows: what happened; whether
the user's data or action was saved; what they can do now; where to get
help. Error copy never blames the user and never exposes secrets or stack
traces. Labels name the control; help text explains the decision;
confirmation text sets a truthful expectation.

Example: "Payment not confirmed yet. Your order is saved. We will check with
MTN MoMo for 10 minutes; you can close this page. Need help? Call 0800 100 200."

## 6. Anti-slop questions

- Could this sentence belong to any product? Add the real actor, field,
  state, threshold, dependency or failure case, or cut it.
- Is every quality adjective measurable?
- Is each term used with one meaning throughout?
- Does a real engineer or user know what to do next?
- Is a polished template being mistaken for a usable specification?

## 7. Evidence record

Record: artefact type, reader and task, source and traceability status,
terminology check, test-oracle review, user-facing language review, proof
status, open context gaps, reviewer and date.

## Sources and currentness

Independent synthesis informed by general English usage, collocation and
register references and CAE-level writing guidance; no source text, word
lists or exercises are reproduced. These inputs are durable concept sources
only and do not override IEEE/ISO requirements practice, approved product
terminology or accessibility guidance. Evidence/currentness (2026-09-24):
`NO_TIME_SENSITIVE_CLAIMS` in this reference; phone number and provider in
the microcopy example are illustrative.

# Book Analysis: Business Style Handbook — Cunningham & Greene
**Analyzed:** 2026-03-15
**Feeds:** M-08, M-09, NQW-8, CLAUDE.md writing quality rules

---

## Key Rules for CLAUDE.md

| Rule | Source | Improvement ID |
|------|---------|---------------|
| Every sentence must earn its length; mix short and long; no choppy all-short | pp. 43–44 | M-08 |
| Headings must say something and stand on their own — not just label a category | p. 44 | Reinforces existing |
| Bullets: complete sentence = period; phrase = no period; lead-in colon = treat items as sentence continuations | pp. 98–99 | New rule |
| Bold: headings, requirement IDs, and single critical tokens only; never more than ~4 consecutive words in body text | pp. 52, 96 | NQW-8 |
| Italic: lighter emphasis within body text; in Markdown: warnings and first-use of defined terms only | p. 53 | NQW-8 |
| Bold + italic together: prohibited for more than a few words | p. 53 | NQW-8 |
| Underline: prohibited as emphasis | p. 53 | NQW-8 |
| Acronyms: spell out on first use per document; define in glossary.md | p. 171 | M-09 |
| Technical vocabulary: every field-specific term must be explained or defined | p. 247 | M-09 |
| Numbers: always use figures for Version, Section, Page, Appendix designations | pp. 104, 203–204 | New rule |
| Paragraph max: 5–6 sentences; one idea per paragraph; main point in first sentence | p. 211 | New rule |
| Passive voice acceptable only when actor is irrelevant or object emphasis is required | pp. 47–48, 213 | Reinforces existing |
| All list items must follow the same grammatical pattern (parallel structure) | p. 45 | Reinforces existing |
| Consistency: all style decisions declared once and held throughout the document | pp. 38–40, 53, 158 | Meta-rule |

---

## Sentence Length (M-08)

- No rigid maximum — rule is balance and every-word-counts concision
- Mix short and long for rhythm; short-only writing is choppy
- "Space is at a premium, more than ever if your message will be read on a mobile device." (p. 44)
- "Direct sentences start with a noun and follow closely with the verb. Don't tax the reader with sentences loaded down with adjectives and adverbs." (p. 44)

**CLAUDE.md directive:** "Every sentence must earn its length. Prefer short sentences for requirements and definitions. Where a long sentence is necessary, every word must be load-bearing. Never let a sentence grow from padding."

---

## Active vs. Passive Voice

- Primary rule: active voice whenever possible (p. 47, p. 213)
- Passive is acceptable when: avoiding blame, emphasizing object over actor, scientific/legal/academic writing (p. 47–48)
- IEEE SRS "The system shall…" is active — fully consistent

---

## Paragraph Structure

- Max 5–6 sentences per paragraph (p. 211)
- One idea per paragraph
- Main point in first sentence (p. 46)
- "Start with your conclusion... then make your case in order of importance" (p. 46)

---

## Emphasis — Validation of Three-Emphasis Rule (NQW-8)

The existing Three-Emphasis Rule (bold=UI, italic=warning, monospace=commands) is consistent with and supported by Cunningham:

- **Bold:** "Reserve for headlines, headings, subheads. When emphasis needed, use boldface sparingly in text; otherwise it can look muddy." (p. 96) — Our rule narrows "critical info" to UI elements specifically.
- **Italic:** Cunningham accepts for differentiation but increasingly prefers quotation marks due to device rendering. Our rule (italic=warnings) is a valid technical writing convention.
- **Monospace:** Not explicitly covered by Cunningham (predates Markdown tooling), but her "quotation marks for set-off terms" use case maps cleanly to backtick notation.
- **Bold + italic together:** Prohibited for more than a few words (p. 53)
- **Underline:** Absolute prohibition (p. 53)

**Bolding requirement IDs:** "For bulleted information, it is sometimes effective to set off introductory words in bold to guide the reader. But don't go overboard and bold the entire thought." (p. 52) — Supports bolding **FR-001** without bolding the full requirement text.

---

## Acronyms and Glossary (M-09)

- Spell out on first use, then use acronym: "Software Requirements Specification (SRS)" on first reference, "SRS" thereafter (p. 171)
- If widely recognizable (like IEEE, ISO), first-use expansion is not required
- Jargon must be explained for broader audiences (p. 176)
- "Every field has its own technical vocabulary, so explain terms that may be unfamiliar to readers." (p. 247)

**Glossary.md implication:** Every domain-specific term used in SRS output must be defined in `_context/glossary.md`. Undefined acronym in delivered SRS = audit anomaly.

---

## Numbers

- Figures (not words) for: Version, Section, Page, Appendix designations (pp. 104, 203–204)
- "Section 3.2.1" not "section three point two"
- "Response time shall not exceed 2 seconds" not "two seconds"
- Percentages always use % symbol

---

## Lists

- Ordered lists (numbered) are mandatory for sequential procedures (supports M-04)
- Bullet items: complete sentence → period; phrase → no period (pp. 98–99)
- Lead-in sentence with colon → treat bullet items as continuations of that sentence
- Bold introductory words in bullets is acceptable but don't bold the full item (p. 52)
- Parallel structure is a hard rule — all items must start with the same grammatical form (p. 45)

---

## Headings

- Must "say something and stand on their own" — "Requirements" is weak; "Functional Requirements for the Loan Processing Module" is strong (p. 44)
- Choose one capitalization style and hold it throughout the document (p. 158)
- Differentiate heading levels via bold, size, or capitalization — consistently (p. 159)

---

## Tables

- Always use figures and abbreviations in tabular material, regardless of spell-out rules (p. 247)
- Column header numbers match body text numbers exactly (p. 204)
- Titles: concise, information-dense (p. 107)

---

## Citations and Standards References

- Scientific/academic = footnotes/endnotes preferred (p. 109)
- IEEE standards citations: consistent format throughout; either "IEEE Std 830-1998" as a proper noun OR quoted title — pick one per document (p. 109)

---

## Verification Checklist for Generated Documents

- [ ] Every sentence earns its length — no padding
- [ ] Active voice used; passive only where actor is irrelevant
- [ ] Paragraphs ≤ 5–6 sentences, one idea each, main point in first sentence
- [ ] Headings stand on their own (informative, not just category labels)
- [ ] Lists: parallel structure throughout; periods on complete sentences only
- [ ] Bold: only for headings, requirement IDs, UI elements, and critical tokens (≤4 words)
- [ ] Italic: only for warnings and first-use of defined terms
- [ ] Bold + italic never combined on same element
- [ ] Underline: not used anywhere
- [ ] All acronyms defined on first use (or in glossary.md)
- [ ] Technical terms explained or defined in glossary.md
- [ ] Numbers: figures used for Section, Version, Page, measurement, data
- [ ] Consistent citation format throughout document

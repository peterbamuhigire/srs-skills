---
title: "Definition of Ready — Maduuka Phase 1"
version: "1.0"
date: "2026-04-05"
status: "Approved"
owner: "Peter Bamuhigire"
---

# Definition of Ready — Maduuka Phase 1

A user story is *Ready* to be pulled into a sprint only when ALL of the following criteria are true. Stories that do not satisfy these criteria remain in the backlog and must be refined before sprint planning.

## Clarity

- [ ] The story has a clear title in the format: "As a [role], I want to [action] so that [benefit]."
- [ ] Acceptance criteria are written in Given/When/Then format — at least 2 criteria per story.
- [ ] The story references the corresponding FR identifier(s) from the SRS (e.g., **FR-POS-012**).
- [ ] The story has a MoSCoW priority assigned: Must Have, Should Have, or Could Have.

## Scope

- [ ] The story is small enough for 1 developer to complete in 1–3 days.
- [ ] If the story is larger than 3 days of work, it has been split into sub-tasks, each independently deliverable.
- [ ] Dependencies are identified: other stories or external items (GAP-001, GAP-004) that must be resolved before this story can start are listed in the story description.

## Design

- [ ] `UXSpec_Maduuka.docx` has been reviewed for this feature — or a UX note has been added to the story flagging that the spec needs updating.
- [ ] The relevant API endpoint is documented in the API specification — or the gap is explicitly flagged in the story.
- [ ] Database schema changes required by this story are identified: new tables, new columns, new indexes.

## Team

- [ ] The story has been reviewed by the team in a backlog refinement session.
- [ ] All questions and ambiguities have been resolved; no open questions remain without a recorded answer in the story description.
- [ ] External dependencies that block this story (MTN MoMo sandbox credentials — GAP-001; NDA drug codes — GAP-003; EFRIS credentials — GAP-005; Africa's Talking WhatsApp Business API — GAP-006) are noted in the story with an owner assigned.

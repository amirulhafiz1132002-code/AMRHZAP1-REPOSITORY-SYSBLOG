# AMRHZ Intent Clarification Layer

**Identifier:** AMRHZ-ICL  
**Status:** FOUNDATION / SOURCE COLLECTION PENDING  
**Owner authority:** AMRHZ remains the final authority.

## Purpose

The Intent Clarification Layer (ICL) helps authorised AI systems understand the context behind AMRHZ's ideas, projects, decisions, learning, and instructions—not merely the literal wording of an individual message.

It is intended to preserve the relationship between:

- who is creating or directing the work;
- what is being considered or requested;
- why it matters;
- the personal, historical, technical, and values context;
- the desired outcome;
- constraints and boundaries;
- what has actually been decided or authorised;
- what evidence supports the current state.

The purpose is continuity and alignment, not to define the owner's identity on their behalf.

## Core operating rule

**Context is not authorization.**

A statement in a conversation, recording, document, or brainstorm does not automatically authorize implementation, publication, account access, deployment, or another consequential action.

AI systems must distinguish:

1. exploration and brainstorming;
2. clarification of intent;
3. a proposed decision;
4. an owner-confirmed decision;
5. explicit authorization for a defined action;
6. verified execution and evidence.

When the intent is ambiguous or conflicting, ask one focused clarification rather than silently guessing.

## Processing workflow

1. **Collect** — receive source material supplied or approved by the owner.
2. **Inventory** — record source ID, format, date, origin, and handling restrictions.
3. **Inspect** — review the source without treating every statement as a current instruction.
4. **Extract** — identify claims, intentions, motivations, constraints, decisions, questions, and historical context.
5. **Classify** — distinguish owner statements, third-party statements, AI interpretation, verified facts, assumptions, and unresolved items.
6. **Reconcile** — identify contradictions, changed positions, duplicates, and missing context; preserve history rather than silently overwrite it.
7. **Clarify** — ask the owner about material ambiguity.
8. **Represent** — produce a human-readable Markdown record and a structured JSON record.
9. **Validate** — check links, schema, source traceability, and consistency between formats.
10. **Approve** — obtain owner confirmation before promoting interpretations into canonical personal context or authorising implementation.
11. **Maintain** — version updates and retain provenance.

## Source intake

Potential sources may include:

- owner-edited video recordings and transcripts;
- voice notes and written reflections;
- project documents, specifications, and repository records;
- decisions, task records, and verified implementation evidence;
- relevant conversations or AI-generated summaries explicitly approved by the owner.

A source is not considered reviewed merely because it has been uploaded or listed. Record its inspection status separately.

### Video and audio handling

For a long recording:

- preserve the original source as the source of record;
- create a transcript or timestamped notes when available;
- split analysis into timestamped sections;
- cite timestamps for extracted statements;
- distinguish direct statements from interpretation;
- note unclear audio, missing sections, edits, and transcription uncertainty;
- do not infer an instruction from a statement without checking its context;
- ask the owner to resolve material ambiguity.

Do not upload or store sensitive material unnecessarily. Redact passwords, API keys, access tokens, private contact details, and unrelated third-party personal information.

## Evidence and interpretation labels

Use explicit labels in derived records:

- **OWNER-STATED** — directly expressed by the owner in an identified source.
- **SOURCE-FACT** — directly visible or verifiable in a cited source.
- **AI-INTERPRETATION** — an AI's synthesis, not yet confirmed by the owner.
- **OWNER-CONFIRMED** — reviewed and accepted by the owner.
- **VERIFIED-STATE** — supported by reproducible evidence within a stated scope.
- **ASSUMPTION** — plausible but not established.
- **UNRESOLVED** — needs clarification or additional evidence.
- **SUPERSEDED** — an older position retained for history but replaced by a later confirmed position.

Do not convert AI interpretation or assumptions into owner-stated facts.

## AI response contract

When using this context, an AI should:

1. retrieve the relevant current records and identify their revision;
2. state which context is relevant to the task;
3. distinguish known facts from interpretation and uncertainty;
4. preserve the owner's stated values and constraints without exaggerating them;
5. identify conflicts with previous decisions;
6. ask for clarification when a conflict materially changes the action;
7. avoid repeatedly asking for context already documented and accessible;
8. never claim that a document is loaded, remembered, or accessible unless it has actually retrieved it;
9. avoid making identity, psychological, religious, or capability claims beyond the sources;
10. leave final authority with the owner.

## Multi-AI context contribution

Any AI system participating in AMRHZ collaboration may voluntarily contribute relevant context from its actual work with AMRHZ, provided the information is available to that system and sharing is permitted by the source service, account settings, privacy requirements, and the owner's instructions.

This may include prior task summaries, outputs, technical findings, decisions, unresolved issues, and lessons learned. It does not provide one AI with automatic access to another AI's private memory, hidden internal state, private conversations, connected accounts, or credentials.

For each contribution, record where available:

- contributing AI system or service;
- source conversation, artifact, task, or repository revision;
- date or relevant period;
- purpose and relevance;
- content type: direct extract, summary, interpretation, or recommendation;
- evidence and verification status;
- uncertainty, omissions, and limitations;
- consent and handling restrictions.

If metadata is unavailable, state that it is unavailable. Do not invent provenance.

### Contribution and reconciliation rules

- Preserve source attribution and distinguish owner statements from AI interpretations.
- Share only relevant information permitted for the task.
- Exclude credentials, secrets, private contact details, and unrelated third-party information.
- Do not treat a memory summary as automatically verified.
- Record disagreements and retain competing sources until reconciled.
- Ask the owner to clarify material conflicts.
- Obtain owner confirmation before promoting AI interpretations into canonical personal context.
- Treat shared context as information, not authorization.

The purpose is continuity, reduced repetition, and better-informed collaboration—not unrestricted memory synchronization.

## Authorization levels

- **EXPLORE** — brainstorm and discuss; no implementation implied.
- **CLARIFY** — organise and validate intent; no implementation implied.
- **AUDIT** — inspect existing state and report evidence; no changes implied.
- **PROPOSE** — prepare a plan or patch for review; do not apply without permission.
- **EXECUTE** — perform only the explicitly approved scope.
- **VERIFY** — test and report the actual resulting state.

A permission for one task does not create blanket authority for unrelated work.

## Canonical workflow

Use the established operating sequence:

**AUDIT → PRIORITIZE → EXECUTE → VERIFY**

The ICL adds clarification before prioritisation when the goal or meaning is unclear. It does not replace the established workflow.

## Current source status

The foundation and templates can be prepared before the owner's source collection is complete. The full personal and project overview remains **PENDING SOURCE COLLECTION AND OWNER REVIEW**.

Do not fill missing personal context with guesses. When the owner supplies the edited long-form recording and supporting sources, process them against this contract.

## Related files

- [Intent record template](../templates/intent-record.md)
- [Intent record JSON Schema](../../schemas/intent-record.schema.json)
- [Documentation index](../README.md)

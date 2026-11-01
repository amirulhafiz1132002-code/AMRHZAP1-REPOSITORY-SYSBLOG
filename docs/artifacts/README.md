# Persistent Artifact Registry

## Purpose

The artifact registry provides a stable, machine-readable index for documents, specifications, evidence records, schemas, reports, and other outputs exchanged or maintained across the AMRHZ ecosystem.

GitHub is used as a versioned record store. The repository URL, file path, and commit revision provide provenance. A registry entry does not itself prove that an artifact's claims are true; verification evidence must be linked and reviewed separately.

## Artifact classes

| Type | Examples |
|---|---|
| protocol | ASIP and RWCAI specifications |
| architecture | diagrams, component maps, data-flow descriptions |
| evidence | test logs, tool results, screenshots with safe redaction |
| implementation | source files, patches, integration code |
| evaluation | test reports, benchmark records, review findings |
| decision | approved decisions and rationale |
| dataset | dataset card, schema, lineage metadata |
| model | model card, weights manifest, evaluation record |

## Required metadata

The canonical schema is [artifact.schema.json](../../schemas/artifact.schema.json). Each artifact should identify:

- stable artifact_id
- title, artifact_type, version, and status
- description
- provenance.repository, path, and immutable revision when available
- created_at and updated_at
- owner_role
- verification.status, scope, and evidence references
- limitations

## Evidence record

An evidence record should state:

1. **Claim** — the precise statement being supported.
2. **Source** — where the evidence was obtained.
3. **Revision** — commit SHA, release, or immutable source identifier when available.
4. **Captured time** — UTC timestamp where known.
5. **Method** — how the evidence was collected.
6. **Scope** — environment, version, and test boundaries.
7. **Result** — PASS, FAIL, PARTIAL, or NOT RUN.
8. **Limitations** — what the evidence does not establish.

Never store secrets, access tokens, private keys, session cookies, or unnecessary personal data in evidence.

## Status semantics

- UNKNOWN: not inspected or evidence is insufficient.
- PROPOSED: suggested but not accepted as a plan.
- PLANNED: accepted as intended work; not implemented.
- DEVELOPMENT: in progress.
- PARTIAL: some elements exist; full acceptance criteria are unmet.
- VERIFIED: stated tests passed within the declared scope.
- LIVE: operational in a named environment with current evidence.
- BLOCKED: a specific dependency or permission prevents progress.
- DEPRECATED: superseded or no longer maintained.

Never use VERIFIED or LIVE without evidence. Verification must be scoped to the actual claim.

## Persistence and retrieval

For durable cross-session retrieval:

1. Store the artifact in a version-controlled repository.
2. Give it a stable artifact ID.
3. Record the repository URL, file path, and commit SHA.
4. Link it from this registry or a project index.
5. Update the registry when a new revision supersedes the old one.
6. Have an AI retrieve the file from the repository and cite the exact revision before relying on it.

A conversation memory or AI context window is not a substitute for the repository record. Conversely, a GitHub artifact is not automatically loaded into every AI product; each product needs an authorized retrieval path.

## Initial registry

See [artifact-registry.yaml](../../artifact-registry.yaml) for the first protocol records and repository references.

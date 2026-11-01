# Artifact Registry Validation — 2026-11-01

**Scope:** Revalidation and evidence reconciliation for the canonical artifact registry  
**Repository:** AMRHZAP1-REPOSITORY-SYSBLOG  
**Validated branch:** `main`  
**Validated commit (immutable snapshot):** `42fbe265ef122093dc640369b8c2e8b88573f84c`  
**Validation environment:** Assistant-side Python 3.13.5 runtime; jsonschema 4.26.0; PyYAML 6.0.3  
**Result:** PASS for the checks listed below, within the stated evidence boundary

## Discrepancy reconciliation

The earlier version of this report stated that the YAML parser found **four** artifact entries. That count does not describe the canonical registry at the validated revision recorded above.

The registry retrieved from `main` at commit `42fbe265ef122093dc640369b8c2e8b88573f84c` contains **five** artifact entries:

1. `ASIP-13`
2. `RWCAI-13`
3. `AMRHZ-ARTIFACT-SCHEMA-001`
4. `RWCAI-TASK-TEMPLATE-001`
5. `AMRHZ-ARTIFACT-VALIDATION-001`

The existing four-entry statement is therefore treated as stale or mismatched evidence. The inspected report does not define a separate four-entry subset, so no such distinction is inferred. The checks below were rerun against the five-entry registry snapshot identified by the commit and blob revisions in this report.

## Exact validation inputs

All repository inputs below were fetched from the same immutable commit, `42fbe265ef122093dc640369b8c2e8b88573f84c`.

| Input | Repository path | Git blob SHA |
|---|---|---|
| Artifact registry | `artifact-registry.yaml` | `189d19b57fe23ab69675752399cd5376956c07ce` |
| JSON Schema | `schemas/artifact.schema.json` | `b7d5109c8bf13d18546879ce0faf650d8dd90821` |
| ASIP metadata | `docs/artifacts/ASIP-13.json` | `154e9c6c5b1ffa66e1fb4783261c77b10c0941f7` |
| RWCAI metadata | `docs/artifacts/RWCAI-13.json` | `cca0ab5da6c20aaba5f910fe4cafd764e89e0f46` |
| ASIP protocol document | `docs/protocols/ASIP-13.md` | `49b7172f4695bea2ec3a4cfb00f418d64259df06` |
| RWCAI protocol document | `docs/protocols/RWCAI-13.md` | `08b7289d7f66414245d6a0d68cb40a5cd8dc5cf6` |
| RWCAI task template | `docs/templates/RWCAI-task-record.md` | `a4724e35504e98dcae1b881f11ef681bd1a2a32c` |

The three additional path targets referenced by the registry—the schema, task template, and validation report—were also fetched successfully from this same commit. The two declared metadata paths were fetched and validated as described below.

## Checks performed

| Check | Result | Notes |
|---|---|---|
| JSON Schema document syntax | PASS | Schema parsed as JSON |
| JSON Schema Draft 2020-12 meta-validation | PASS | `Draft202012Validator.check_schema` completed |
| ASIP-13 metadata instance | PASS | Validated against the retrieved schema with format checking enabled |
| RWCAI-13 metadata instance | PASS | Validated against the retrieved schema with format checking enabled |
| YAML registry parsing | PASS | `yaml.safe_load` parsed the registry; five artifact entries found |
| Registry entry count | PASS | Exactly five entries |
| Artifact ID uniqueness | PASS | Five IDs present; five unique |
| Lifecycle status vocabulary | PASS | Every registry artifact status is in the schema's declared status enum |
| Registry path readback | PASS | All five artifact `path` targets were fetched at the validated commit |
| Declared metadata path readback | PASS | Both declared metadata targets were fetched at the validated commit |
| CI automation | NOT RUN | No CI validation workflow was added or invoked |

## Reproduction outline

Using the exact input files identified above:

1. Parse `schemas/artifact.schema.json` as JSON.
2. Run JSON Schema Draft 2020-12 meta-validation.
3. Validate `docs/artifacts/ASIP-13.json` and `docs/artifacts/RWCAI-13.json` against the schema with a format checker.
4. Parse `artifact-registry.yaml` with PyYAML `safe_load`.
5. Assert that the registry contains five artifacts, that all artifact IDs are unique, and that each lifecycle status belongs to the schema's declared status enum.
6. Read back the registry's referenced artifact and metadata paths from the same commit.

## Validation environment and evidence boundary

Validation was performed in an assistant-side Python 3.13.5 runtime using jsonschema 4.26.0 and PyYAML 6.0.3. The repository files were retrieved from GitHub at the immutable commit identified above; validation was performed in that assistant-side runtime.

This validation was **not** run on the user's Termux device, on a local checkout controlled by the user, or in GitHub Actions. No CI workflow was added or executed. The checks establish syntax, schema validity for the two supplied metadata instances, and the stated registry consistency properties for this repository snapshot only.

This evidence does not establish external AI-provider conformance, automated cross-provider dispatch, shared cross-provider memory, a completed end-to-end multi-provider task, Meta AI independent review, or human acceptance. Those matters remain outside this validation scope and pending where applicable. Human authority and the existing ASIP/RWCAI governance boundaries are unchanged.

## Result

**PASS** — the schema, both metadata instances, YAML parsing, five-entry count, unique IDs, allowed lifecycle statuses, and referenced-path readbacks passed for the exact repository snapshot and input blobs identified above.

CI reproduction, validation in the user's Termux environment, Meta AI independent review, and separate human acceptance remain pending.

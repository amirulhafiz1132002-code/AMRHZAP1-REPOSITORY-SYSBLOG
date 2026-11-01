# Artifact Registry Validation — 2026-11-01

**Scope:** Original validation snapshot, post-merge re-execution, and reproducible validation workflow  
**Repository:** AMRHZAP1-REPOSITORY-SYSBLOG  
**PR #4 merge snapshot:** `5e430312f3b922995c45d89d1deb4aaa2f60231e`  
**Historical PR #4 baseline:** NOT VERIFIED — the identifier previously recorded was 38 hexadecimal characters and did not resolve as a Git commit.  
**GPT-side validation environment:** Python 3.13.5; jsonschema 4.26.0; PyYAML 6.0.3

## 1. Historical PR #4 validation snapshot

PR #4 corrected the stale four-entry count and recorded a baseline identifier. A subsequent GitHub commit lookup found that the recorded identifier was only 38 hexadecimal characters and did not resolve as a Git commit. The exact historical PR #4 base snapshot is therefore not independently verified in this record; no replacement SHA is guessed.

The pre-PR #5 main snapshot that GPT fetched and revalidated contained five entries:
1. `ASIP-13`
2. `RWCAI-13`
3. `AMRHZ-ARTIFACT-SCHEMA-001`
4. `RWCAI-TASK-TEMPLATE-001`
5. `AMRHZ-ARTIFACT-VALIDATION-001`

The PR #4 report recorded the following seven input blob identifiers. GPT subsequently confirmed that each identifier matches the corresponding file in the current `main` tree. Because the historical baseline identifier does not resolve, this comparison does not independently prove that all seven blobs belonged to a reproducible historical commit:

| Input | Repository path | Git blob SHA |
|---|---|---|
| Artifact registry | `artifact-registry.yaml` | `189d19b57fe23ab69675752399cd5376956c07ce` |
| JSON Schema | `schemas/artifact.schema.json` | `b7d5109c8bf13d18546879ce0faf650d8dd90821` |
| ASIP metadata | `docs/artifacts/ASIP-13.json` | `154e9c6c5b1ffa66e1fb4783261c77b10c0941f7` |
| RWCAI metadata | `docs/artifacts/RWCAI-13.json` | `cca0ab5da6c20aaba5f910fe4cafd764e89e0f46` |
| ASIP protocol | `docs/protocols/ASIP-13.md` | `49b7172f4695bea2ec3a4cfb00f418d64259df06` |
| RWCAI protocol | `docs/protocols/RWCAI-13.md` | `08b7289d7f66414245d6a0d68cb40a5cd8dc5cf6` |
| RWCAI task template | `docs/templates/RWCAI-task-record.md` | `a4724e35504e98dcae1b881f11ef681bd1a2a32c` |

## 2. GPT-side post-merge re-execution

After PR #4 was merged, GPT retrieved the current-main registry, schema, both metadata records, protocol documents, task template, and validation report from GitHub. The current `main` HEAD was confirmed as the PR #4 merge commit `5e430312f3b922995c45d89d1deb4aaa2f60231e`.

A fresh Python execution was performed using the retrieved schema, metadata, and registry content:

| Check | Result | Detail |
|---|---|---|
| JSON Schema document parsing | PASS | Schema parsed as JSON |
| Draft 2020-12 meta-validation | PASS | `Draft202012Validator.check_schema` |
| ASIP-13 metadata validation | PASS | Format checking enabled |
| RWCAI-13 metadata validation | PASS | Format checking enabled |
| YAML parsing | PASS | PyYAML `safe_load` |
| Registry count at this snapshot | PASS | Five entries |
| Artifact ID uniqueness | PASS | Five unique IDs |
| Lifecycle status vocabulary | PASS | All statuses are in the schema enum |
| Registry path readback | PASS | Five declared artifact path targets fetched from GitHub |
| Metadata path readback | PASS | Both declared metadata targets fetched from GitHub |

Environment:
- Python 3.13.5
- jsonschema 4.26.0
- PyYAML 6.0.3

**Execution boundary:** This was a GPT-side execution using content retrieved from GitHub at the verified PR #4 merge snapshot/current `main` state. It was not run on the user's Termux device. The GitHub blob SHAs above were retrieved separately from GitHub; this Python run did not recompute Git object hashes. The exact pre-merge PR #4 base commit remains unresolved because the earlier recorded identifier was malformed.

## 3. Reproducible repository validator

This PR adds:
- `scripts/validate_artifact_registry.py`
- `requirements-validation.txt`
- `.github/workflows/validate-artifact-registry.yml`

The validator checks:
1. JSON Schema Draft 2020-12 meta-validation.
2. YAML registry parsing.
3. Non-empty artifact list.
4. Unique artifact IDs.
5. Lifecycle statuses against the schema enum.
6. Repository-relative artifact paths exist and do not escape the repository root.
7. Every declared metadata file parses as JSON, its `artifact_id` matches the registry entry, and it validates against the schema with format checking.

Reproduction command:

```bash
python -m pip install -r requirements-validation.txt
python scripts/validate_artifact_registry.py
```

The validator was exercised locally against a temporary test tree containing the retrieved schema, metadata, and registry structures. Result: **PASS**. This local script test is not a GitHub Actions result.

## 4. Registry revision introduced by this PR

This PR adds two traceable records to the registry:
- `META-AI-POST-MERGE-AUDIT-PR4-001`
- `RWCAI-TASK-2026-001-REV-002`

The proposed registry therefore contains seven entries. The five-entry GPT-side re-execution above applies to the pre-PR #5 main snapshot. The seven-entry PR #5 registry and all newly referenced paths were checked by GitHub Actions run 41271236103 against the PR merge ref containing head commit 17b42c132d752e5c510560d3f7ae25278b914c5c and base main commit 5e430312f3b922995c45d89d1deb4aaa2f60231e.

## 5. CI status

The GitHub Actions workflow is included in this PR and is configured for relevant pull requests, pushes to `main`, and manual dispatch.

**CI result: PASS.** GitHub Actions run 41271236103 completed successfully. Job 124744269522 completed all steps successfully, including dependency installation and execution of the registry validator.

## 6. Independent review record

Meta AI's supplied revised post-merge audit rated PR #4 **PASS WITH CONDITIONS** for its evidence-reconciliation objective. The report itself stated that Meta did not rerun Python validation. GPT's subsequent Python run is recorded separately above and is not attributed to Meta AI.

See `docs/records/META-AI-INDEPENDENT-REVIEW-2026-11-01.md`.

### GitHub Actions execution evidence

- Workflow: `Validate Artifact Registry`
- Run ID: `41270885295`
- Job ID: `124743240429`
- PR merge candidate: `17b42c132d752e5c510560d3f7ae25278b914c5c`
- Run status: `completed`; conclusion: `success`
- Runner: Ubuntu 26.04
- Python: 3.13.17
- Dependencies: jsonschema 4.26.0; PyYAML 6.0.3
- Checkout, Python setup, dependency installation, and registry validation steps all completed successfully.

Validator output: Draft 2020-12 meta-validation PASS; YAML registry 7 entries; 7 unique IDs; lifecycle status vocabulary PASS; 7 registry path targets exist; 2 metadata artifact IDs match their registry entries; 2 metadata instances validate with format checking; final result PASS.

The workflow now uses Node 24-compatible major versions of `actions/checkout` and `actions/setup-python`; the earlier Node.js 20 deprecation warning was addressed in the subsequent workflow revision.

## 7. Evidence boundary and limitations

These checks establish the schema and metadata results, registry consistency, and the stated repository path readbacks for the identified snapshot. They do not establish:
- validation on the user's Termux device;
- runtime cross-provider integration;
- external AI-provider conformance;
- automated cross-provider dispatch;
- shared cross-provider memory;
- a completed end-to-end multi-provider task;
- separate human acceptance.

Human authority and the ASIP/RWCAI governance boundaries are unchanged.

## Result

**PASS** for the GPT-side re-execution on the pre-PR #5 five-entry snapshot and the local validator test against the temporary test tree.

**PASS** for the seven-entry PR #5 merge candidate in GitHub Actions run 41270885295. Termux-side validation, runtime cross-provider dispatch, shared memory, and human acceptance remain outside this CI result.

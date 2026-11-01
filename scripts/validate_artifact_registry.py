#!/usr/bin/env python3
"""Validate the AMRHZ persistent artifact registry and referenced metadata."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "artifact-registry.yaml"
SCHEMA_PATH = ROOT / "schemas" / "artifact.schema.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read valid JSON from {path.relative_to(ROOT)}: {exc}")


def safe_repo_path(value: object, field: str, artifact_id: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        fail(f"{artifact_id}: {field} must be a non-empty repository-relative path")

    candidate = (ROOT / value).resolve()
    if not candidate.is_relative_to(ROOT):
        fail(f"{artifact_id}: {field} escapes the repository root: {value}")

    if not candidate.is_file():
        fail(f"{artifact_id}: {field} target does not exist: {value}")
    return candidate


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        fail(f"JSON Schema Draft 2020-12 meta-validation failed: {exc.message}")
    print("PASS: JSON Schema Draft 2020-12 meta-validation")

    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    try:
        registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        fail(f"Cannot parse artifact-registry.yaml: {exc}")

    if not isinstance(registry, dict):
        fail("Registry root must be a YAML mapping")

    artifacts = registry.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail("Registry must contain a non-empty 'artifacts' list")

    allowed_statuses = set(schema["properties"]["status"]["enum"])
    seen_ids: set[str] = set()
    metadata_count = 0
    path_count = 0

    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(f"Registry artifact at index {index} must be a mapping")

        artifact_id = artifact.get("artifact_id")
        if not isinstance(artifact_id, str) or not artifact_id:
            fail(f"Registry artifact at index {index} has no valid artifact_id")
        if artifact_id in seen_ids:
            fail(f"Duplicate artifact_id: {artifact_id}")
        seen_ids.add(artifact_id)

        status = artifact.get("status")
        if status not in allowed_statuses:
            fail(f"{artifact_id}: lifecycle status {status!r} is not in the schema enum")

        safe_repo_path(artifact.get("path"), "path", artifact_id)
        path_count += 1

        metadata_path = artifact.get("metadata_path")
        if metadata_path is not None:
            metadata_file = safe_repo_path(metadata_path, "metadata_path", artifact_id)
            metadata = load_json(metadata_file)
            if not isinstance(metadata, dict) or metadata.get("artifact_id") != artifact_id:
                fail(f"{artifact_id}: metadata artifact_id does not match the registry entry")
            errors = sorted(
                validator.iter_errors(metadata),
                key=lambda error: list(error.absolute_path),
            )
            if errors:
                details = "; ".join(
                    f"{'/'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
                    for error in errors
                )
                fail(f"{artifact_id}: metadata validation failed: {details}")
            metadata_count += 1

    print(f"PASS: YAML parsed; {len(artifacts)} artifact entries")
    print(f"PASS: {len(seen_ids)} unique artifact IDs")
    print("PASS: all lifecycle statuses use the schema vocabulary")
    print(f"PASS: {path_count} registry path targets exist")
    print(f"PASS: {metadata_count} metadata artifact IDs match registry entries")
    print(f"PASS: {metadata_count} metadata instances validate with format checking")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

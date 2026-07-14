#!/usr/bin/env python3
"""Validate Agentic Threat Atlas records using the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ENTRY_DIR = ROOT / "atlas" / "entries"
CONTROL_FILE = ROOT / "controls" / "control-catalog.md"
SOURCE_FILE = ROOT / "references" / "sources.md"

REQUIRED_FIELDS = {
    "id",
    "title",
    "status",
    "evidence_level",
    "risk_band",
    "first_published",
    "last_reviewed",
    "summary",
    "affected_layers",
    "trust_boundaries",
    "preconditions",
    "attack_path",
    "security_impact",
    "observable_signals",
    "controls",
    "limitations",
    "open_questions",
    "references",
}

ALLOWED_STATUS = {"draft", "active", "contested", "retired"}
ALLOWED_EVIDENCE = {"E0", "E1", "E2", "E3", "E4"}
ALLOWED_RISK = {"context-dependent", "low", "moderate", "high", "critical"}
ALLOWED_LAYERS = {
    "instruction",
    "identity",
    "data",
    "planning",
    "tool",
    "memory",
    "orchestration",
    "runtime",
    "supply-chain",
    "oversight",
    "recovery",
}
ALLOWED_IMPACT = {
    "confidentiality",
    "integrity",
    "availability",
    "authorization",
    "privacy",
    "accountability",
}

ID_PATTERN = re.compile(r"^ATA-[0-9]{3}$")
CONTROL_PATTERN = re.compile(r"CTL-[0-9]{3}")
SOURCE_PATTERN = re.compile(r"SRC-[0-9]{3}")


def read_defined_ids(path: Path, pattern: re.Pattern[str]) -> set[str]:
    if not path.exists():
        raise FileNotFoundError(f"required catalog is missing: {path.relative_to(ROOT)}")
    return set(pattern.findall(path.read_text(encoding="utf-8")))


def valid_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_string_list(
    record: dict[str, Any],
    field: str,
    errors: list[str],
    *,
    minimum: int = 1,
) -> None:
    value = record.get(field)
    if not isinstance(value, list) or len(value) < minimum:
        errors.append(f"{field} must be a list with at least {minimum} item(s)")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{field}[{index}] must be a non-empty string")


def validate_record(
    path: Path,
    record: dict[str, Any],
    known_controls: set[str],
    known_sources: set[str],
) -> list[str]:
    errors: list[str] = []

    missing = sorted(REQUIRED_FIELDS - record.keys())
    unknown = sorted(record.keys() - REQUIRED_FIELDS)
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    if unknown:
        errors.append(f"unknown fields: {', '.join(unknown)}")

    record_id = record.get("id")
    if not isinstance(record_id, str) or not ID_PATTERN.fullmatch(record_id):
        errors.append("id must match ATA-000")
    elif path.stem != record_id:
        errors.append(f"filename must be {record_id}.json")

    title = record.get("title")
    if not isinstance(title, str) or len(title.strip()) < 8:
        errors.append("title must contain at least 8 characters")

    summary = record.get("summary")
    if not isinstance(summary, str) or len(summary.strip()) < 40:
        errors.append("summary must contain at least 40 characters")

    if record.get("status") not in ALLOWED_STATUS:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUS)}")
    if record.get("evidence_level") not in ALLOWED_EVIDENCE:
        errors.append(f"evidence_level must be one of {sorted(ALLOWED_EVIDENCE)}")
    if record.get("risk_band") not in ALLOWED_RISK:
        errors.append(f"risk_band must be one of {sorted(ALLOWED_RISK)}")

    for field in ("first_published", "last_reviewed"):
        if not valid_date(record.get(field)):
            errors.append(f"{field} must use YYYY-MM-DD")

    validate_string_list(record, "affected_layers", errors)
    validate_string_list(record, "trust_boundaries", errors)
    validate_string_list(record, "preconditions", errors)
    validate_string_list(record, "attack_path", errors, minimum=2)
    validate_string_list(record, "security_impact", errors)
    validate_string_list(record, "observable_signals", errors)
    validate_string_list(record, "controls", errors)
    validate_string_list(record, "limitations", errors)
    validate_string_list(record, "open_questions", errors)
    validate_string_list(record, "references", errors)

    layers = record.get("affected_layers", [])
    if isinstance(layers, list):
        invalid_layers = sorted(set(layers) - ALLOWED_LAYERS)
        if invalid_layers:
            errors.append(f"unknown affected_layers: {', '.join(invalid_layers)}")
        if len(layers) != len(set(layers)):
            errors.append("affected_layers contains duplicates")

    impacts = record.get("security_impact", [])
    if isinstance(impacts, list):
        invalid_impacts = sorted(set(impacts) - ALLOWED_IMPACT)
        if invalid_impacts:
            errors.append(f"unknown security_impact values: {', '.join(invalid_impacts)}")
        if len(impacts) != len(set(impacts)):
            errors.append("security_impact contains duplicates")

    controls = record.get("controls", [])
    if isinstance(controls, list):
        malformed = [item for item in controls if not isinstance(item, str) or not CONTROL_PATTERN.fullmatch(item)]
        undefined = sorted(set(controls) - known_controls)
        if malformed:
            errors.append(f"malformed control identifiers: {malformed}")
        if undefined:
            errors.append(f"undefined controls: {', '.join(undefined)}")
        if len(controls) != len(set(controls)):
            errors.append("controls contains duplicates")

    references = record.get("references", [])
    if isinstance(references, list):
        malformed = [item for item in references if not isinstance(item, str) or not SOURCE_PATTERN.fullmatch(item)]
        undefined = sorted(set(references) - known_sources)
        if malformed:
            errors.append(f"malformed source identifiers: {malformed}")
        if undefined:
            errors.append(f"undefined references: {', '.join(undefined)}")
        if len(references) != len(set(references)):
            errors.append("references contains duplicates")

    return errors


def main() -> int:
    if not ENTRY_DIR.exists():
        print(f"error: missing entry directory: {ENTRY_DIR.relative_to(ROOT)}", file=sys.stderr)
        return 1

    try:
        known_controls = read_defined_ids(CONTROL_FILE, CONTROL_PATTERN)
        known_sources = read_defined_ids(SOURCE_FILE, SOURCE_PATTERN)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    paths = sorted(ENTRY_DIR.glob("ATA-*.json"))
    if not paths:
        print("error: no threat records found", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    seen_ids: set[str] = set()

    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            all_errors.append(f"{path.relative_to(ROOT)}: cannot read valid JSON: {exc}")
            continue

        if not isinstance(record, dict):
            all_errors.append(f"{path.relative_to(ROOT)}: top-level value must be an object")
            continue

        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in seen_ids:
                all_errors.append(f"{path.relative_to(ROOT)}: duplicate id {record_id}")
            seen_ids.add(record_id)

        for error in validate_record(path, record, known_controls, known_sources):
            all_errors.append(f"{path.relative_to(ROOT)}: {error}")

    if all_errors:
        print("Atlas validation failed:", file=sys.stderr)
        for error in all_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} threat record(s), {len(known_controls)} controls, and {len(known_sources)} sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

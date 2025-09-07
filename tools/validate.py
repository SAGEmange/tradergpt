"""Validate JSON files against schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"


def load_schema(name: str) -> dict:
    """Load a schema file by name."""
    with open(SCHEMAS / name, "r", encoding="utf-8") as fh:
        return json.load(fh)


def check_file(path: Path, schema_name: str, errors: list[str]) -> None:
    """Validate *path* against *schema_name* collecting errors."""
    schema = load_schema(schema_name)
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    try:
        validate(data, schema)
    except ValidationError as exc:  # pragma: no cover - simple script
        errors.append(f"{path}: {exc.message}")


def main() -> int:
    errors: list[str] = []
    check_file(ROOT / "signals" / "today.json", "signal.schema.json", errors)
    for file in (ROOT / "signals" / "archive").glob("*.json"):
        check_file(file, "signal.schema.json", errors)
    check_file(ROOT / "configs" / "account.json", "account.schema.json", errors)
    for cfg in ["boom500.json", "crash1000.json"]:
        check_file(ROOT / "configs" / cfg, "market.schema.json", errors)
    for file in (ROOT / "overlays").glob("*_overlay.json"):
        check_file(file, "overlay.schema.json", errors)
    for file in ROOT.glob("logs/*-recap.json"):
        check_file(file, "recap.schema.json", errors)

    if errors:
        for e in errors:
            print(e)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry
    sys.exit(main())

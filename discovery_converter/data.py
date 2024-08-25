from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .errors import InvalidJSONError, InvalidYAMLError


def load_json(file_path: str) -> dict[str, Any]:
    with Path(file_path).open(encoding="utf-8") as file:
        result = json.load(file)

    if not isinstance(result, dict):
        msg = "File must be a JSON object"
        raise InvalidJSONError(msg)

    return result


def write_json(file_path: str, data: dict[str, Any]) -> None:
    with Path(file_path).open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_yaml(file_path: str) -> dict[str, Any]:
    with Path(file_path).open(encoding="utf-8") as file:
        result = yaml.safe_load(file)

    if not isinstance(result, dict):
        msg = "File must be a YAML object"
        raise InvalidYAMLError(msg)

    return result

from __future__ import annotations

from typing import Any

import pytest
from jsonschema import ValidationError, validate


def test_if_metavalidate_json_schema(metaschema_draft_07: dict[str, Any]) -> None:
    validate(metaschema_draft_07, metaschema_draft_07)


def test_if_valid_discovery_file_is_valid(
    cloud_run_discovery: dict[str, Any],
    metaschema_draft_07: dict[str, Any],
) -> None:
    validate(cloud_run_discovery, metaschema_draft_07)


def test_if_valid_schema_is_valid(
    valid_schema: dict[str, Any],
    metaschema_draft_07: dict[str, Any],
) -> None:
    validate(valid_schema, metaschema_draft_07)


def test_if_invalid_schema_is_invalid(
    invalid_schema: dict[str, Any],
    metaschema_draft_07: dict[str, Any],
) -> None:
    with pytest.raises(ValidationError):
        validate(invalid_schema, metaschema_draft_07)

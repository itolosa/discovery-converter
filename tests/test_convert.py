from __future__ import annotations

from typing import Any

import pytest
from discovery_converter import builders, convert
from jsonschema import ValidationError, validate


def test_convert_discovery_to_schema_is_valid(
    cloud_run_discovery: dict[str, Any],
    metaschema_draft_07: dict[str, Any],
) -> None:
    schema = convert(cloud_run_discovery, builders.cloud_run)

    validate(schema, metaschema_draft_07)


def test_valid_spec_is_valid(
    valid_cloud_run_spec: dict[str, Any],
    cloud_run_discovery: dict[str, Any],
) -> None:
    validate(valid_cloud_run_spec, convert(cloud_run_discovery, builders.cloud_run))


def test_invalid_spec_is_invalid_using_pre_existing_schema(
    invalid_cloud_run_spec: dict[str, Any],
    valid_cloud_run_schema: dict[str, Any],
) -> None:
    with pytest.raises(ValidationError):
        validate(invalid_cloud_run_spec, valid_cloud_run_schema)


def test_invalid_spec_is_invalid(
    invalid_cloud_run_spec: dict[str, Any],
    cloud_run_discovery: dict[str, Any],
) -> None:
    cloud_run_json_schema = convert(cloud_run_discovery, builders.cloud_run)

    with pytest.raises(ValidationError):
        validate(invalid_cloud_run_spec, cloud_run_json_schema)

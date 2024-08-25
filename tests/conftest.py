from __future__ import annotations

from typing import Any

import pytest
from discovery_converter import load_json, load_yaml

from tests.test_helpers import fixture_path


@pytest.fixture
def invalid_discovery_file_path() -> str:
    return str(fixture_path("invalidDiscovery.json"))


@pytest.fixture
def cloud_run_discovery_file_path() -> str:
    return str(fixture_path("cloudRunDiscovery.json"))


@pytest.fixture
def metaschema_file_path() -> str:
    return str(fixture_path("schema.json"))


@pytest.fixture
def valid_schema_file_path() -> str:
    return str(fixture_path("validSchema.json"))


@pytest.fixture
def metaschema_draft_07(metaschema_file_path: str) -> dict[str, Any]:
    return load_json(metaschema_file_path)


@pytest.fixture
def valid_schema(valid_schema_file_path: str) -> dict[str, Any]:
    return load_json(valid_schema_file_path)


@pytest.fixture
def cloud_run_discovery(cloud_run_discovery_file_path: str) -> dict[str, Any]:
    return load_json(cloud_run_discovery_file_path)


@pytest.fixture
def invalid_schema_file_path() -> str:
    return str(fixture_path("invalidSchema.json"))


@pytest.fixture
def invalid_schema(invalid_schema_file_path: str) -> dict[str, Any]:
    return load_json(invalid_schema_file_path)


@pytest.fixture
def valid_yaml_file_path() -> str:
    return str(fixture_path("validDiscoverySpec.yaml"))


@pytest.fixture
def invalid_yaml_file_path() -> str:
    return str(fixture_path("invalidDiscoverySpec.yaml"))


@pytest.fixture
def valid_cloud_run_spec() -> dict[str, Any]:
    return load_yaml(str(fixture_path("validCloudRunSpec.yaml")))


@pytest.fixture
def invalid_cloud_run_spec() -> dict[str, Any]:
    return load_yaml(str(fixture_path("invalidCloudRunSpec.yaml")))


@pytest.fixture
def valid_cloud_run_schema() -> dict[str, Any]:
    return load_json(str(fixture_path("validCloudRunSchema.json")))

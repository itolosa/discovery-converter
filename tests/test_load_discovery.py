import pytest
from discovery_converter import InvalidJSONError, load_json


def test_load_valid_discovery(cloud_run_discovery_file_path: str) -> None:
    content = load_json(cloud_run_discovery_file_path)
    assert isinstance(content, dict)


def test_load_invalid_discovery(invalid_discovery_file_path: str) -> None:
    with pytest.raises(InvalidJSONError):
        load_json(invalid_discovery_file_path)

import pytest
from discovery_converter import InvalidYAMLError, load_yaml


def test_load_yaml_file(valid_yaml_file_path: str) -> None:
    content = load_yaml(valid_yaml_file_path)
    assert isinstance(content, dict)


def test_load_invalid_yaml_file(invalid_yaml_file_path: str) -> None:
    with pytest.raises(InvalidYAMLError):
        load_yaml(invalid_yaml_file_path)

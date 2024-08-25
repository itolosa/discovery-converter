from pathlib import Path

from discovery_converter import load_json, write_json


def test_write_json() -> None:
    file_path = Path("test.json")

    written_data = {"key": "value"}

    write_json(str(file_path), written_data)
    read_data = load_json(str(file_path))

    assert read_data == written_data

    file_path.unlink()

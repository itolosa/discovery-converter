from __future__ import annotations

from typing import Any

import pytest
from discovery_converter import replace_refs


@pytest.fixture
def example_input() -> dict[str, Any]:
    return {
        "ListLocationsResponse": {
            "id": "ListLocationsResponse",
            "description": "The response message for Locations.ListLocations.",
            "type": "object",
            "properties": {
                "locations": {
                    "description": "A list of locations that matches the specified "
                    "filter in the request.",
                    "type": "array",
                    "items": {"$ref": "Location"},
                },
                "nextPageToken": {
                    "description": "The standard List next-page token.",
                    "type": "string",
                },
            },
        }
    }


@pytest.fixture
def example_output() -> dict[str, Any]:
    return {
        "ListLocationsResponse": {
            "id": "ListLocationsResponse",
            "description": "The response message for Locations.ListLocations.",
            "type": "object",
            "properties": {
                "locations": {
                    "description": "A list of locations that matches the specified "
                    "filter in the request.",
                    "type": "array",
                    "items": {"$ref": "#/$defs/Location"},
                },
                "nextPageToken": {
                    "description": "The standard List next-page token.",
                    "type": "string",
                },
            },
        }
    }


def test_replace(example_input: dict[str, Any], example_output: dict[str, Any]) -> None:
    assert replace_refs(example_input) == example_output

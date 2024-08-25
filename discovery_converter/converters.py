from __future__ import annotations

import uuid
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def replace_refs(node: T | dict[str, Any]) -> T | dict[str, Any]:
    if isinstance(node, dict):
        return {
            key: replace_refs(value) if key != "$ref" else f"#/$defs/{value}"
            for key, value in node.items()
        }
    return node


def convert(
    discovery: dict[str, Any],
    props_builder: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Convert a Discovery document to a JSON Schema.

    Args:
    ----
        discovery: The Discovery document.
        props_builder: A function that takes the Discovery document and returns \
            additional properties to include in the JSON Schema.

    Returns:
    -------
        The JSON Schema.

    """
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": f"https://discovery-converter.com/schemas/{uuid.uuid4().hex}",
        "title": discovery["title"],
        "type": "object",
        "$defs": replace_refs(discovery["schemas"]),
        **(props_builder(discovery) if props_builder else {}),
    }

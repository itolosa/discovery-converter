from __future__ import annotations

from typing import Any


def cloud_run(discovery: dict[str, Any]) -> dict[str, Any]:
    root_schemas = {
        key: value
        for key, value in discovery["schemas"].items()
        if "properties" in value
        and "kind" in value["properties"]
        and "spec" in value["properties"]
    }

    return {
        "allOf": [
            {
                "if": {"properties": {"kind": {"const": name}}},
                "then": {"$ref": f"#/$defs/{name}"},
            }
            for name in root_schemas
        ]
    }

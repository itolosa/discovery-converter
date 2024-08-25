from __future__ import annotations

from typing import Any, Callable, TypeVar

T = TypeVar("T")


def replace_refs(node: T | dict[str, Any]) -> T | dict[str, Any]:
    if isinstance(node, dict):
        return {
            key: replace_refs(value) if key != "$ref" else f"#/$defs/{value}"
            for key, value in node.items()
        }
    return node


def remove_ids(node: T | dict[str, Any]) -> T | dict[str, Any]:
    if isinstance(node, dict):
        return {
            key: remove_ids(value)
            for key, value in node.items()
            if not (key == "id" and isinstance(value, str))
        }
    return node


def replace_formats(node: T | dict[str, Any]) -> T | dict[str, Any]:
    if isinstance(node, dict):
        if "format" not in node:
            return {key: replace_formats(value) for key, value in node.items()}
        return map_format_node(node)
    return node


def map_format_node(node: dict[str, Any]) -> dict[str, Any]:
    format_map = {
        # A 32-bit signed integer. It has a minimum value of -2,147,483,648
        # and a maximum value of 2,147,483,647 (inclusive).
        "int32": {
            "type": "integer",
            "format": "int32",
        },
        # A 32-bit unsigned integer. It has a minimum value of 0 and a
        # maximum value of 4,294,967,295 (inclusive).
        "uint32": {
            "type": "integer",
            "format": "uint32",
        },
        # A double-precision 64-bit IEEE 754 floating point.
        "double": {
            "type": "number",
            "format": "double",
        },
        # A single-precision 32-bit IEEE 754 floating point.
        "float": {
            "type": "number",
            "format": "float",
        },
        # A padded, base64-encoded string of bytes, encoded with
        # a URL and filename safe alphabet (sometimes referred to
        # as "web-safe" or "base64url"). Defined by RFC4648.
        "byte": {
            "type": "string",
            "pattern": "^[-A-Za-z0-9+/]*={0,3}$",
        },
        # An RFC3339 date in the format YYYY-MM-DD. Defined in the JSON Schema spec.
        "date": {
            "type": "string",
            "format": "date",
        },
        # An RFC3339 timestamp in UTC time. This in the format of
        # yyyy-MM-ddTHH:mm:ss.SSSZ. The milliseconds portion (".SSS")
        # is optional. Defined in the JSON Schema spec.
        "date-time": {
            "type": "string",
            "format": "date-time",
        },
        # An RFC3339 timestamp in UTC time. This in the format of
        # yyyy-MM-ddTHH:mm:ss.SSSZ. The milliseconds portion (".SSS") is optional.
        "google-datetime": {
            "type": "string",
            "format": "date-time",
        },
        # A string ends in the suffix "s" (indicating seconds) and
        # is preceded by the number of seconds, with nanoseconds
        # expressed as fractional seconds. The period is always used
        # as the decimal point, not a comma.
        "google-duration": {
            "type": "string",
            "pattern": "^-?[0-9]+(.[0-9]+)?s$",
        },
        # A string where field names are separated by a comma. Field
        # names are represented in lower-camel naming conventions.
        "google-fieldmask": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_]+(?:,[ ]?[a-zA-Z0-9_]+)*$",
        },
        # A 64-bit signed integer. It has a minimum value of
        # -9,223,372,036,854,775,808 and a maximum value
        # of 9,223,372,036,854,775,807 (inclusive).
        "int64": {
            "type": "string",
            "pattern": "^-?[0-9]+$",
        },
        # A 64-bit unsigned integer. It has a minimum value
        # of 0 and a maximum value of (2^64)-1 (inclusive).
        "uint64": {
            "type": "string",
            "pattern": "^[0-9]+$",
        },
    }

    return {
        **{k: v for k, v in node.items() if k != "format"},
        **format_map.get(node["format"], {}),
    }


def transform_enums(node: T | dict[str, Any]) -> T | dict[str, Any]:
    if isinstance(node, dict):
        if "enumDescriptions" not in node:
            return {key: transform_enums(value) for key, value in node.items()}
        return enum_to_anyof(node)
    return node


def enum_to_anyof(node: dict[str, Any]) -> dict[str, Any]:
    new_node = dict(node)
    new_node.pop("enumDescriptions")
    new_node.pop("enum")

    return {
        **new_node,
        "anyOf": [
            {"const": enum, "title": desc}
            for enum, desc in zip(node["enum"], node["enumDescriptions"])
        ],
    }


def replace_any_with_object(node: T | dict[str, Any]) -> T | dict[str, Any]:
    if isinstance(node, dict):
        return {
            key: replace_any_with_object(value)
            if not (key == "type" and value == "any")
            else "object"
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
        "$id": "https://json.schemastore.org/cloud-run-v1.json",
        "title": discovery["title"],
        "type": "object",
        "$defs": transform_enums(
            replace_any_with_object(
                replace_formats(remove_ids(replace_refs(discovery["schemas"])))
            )
        ),
        **(props_builder(discovery) if props_builder else {}),
    }

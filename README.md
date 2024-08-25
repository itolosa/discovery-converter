# Discovery to JSON Schema Converter

[![codecov](https://codecov.io/github/itolosa/discovery-converter/graph/badge.svg?token=2KGGT1RWI4)](https://codecov.io/github/itolosa/discovery-converter)

The goal of this project is to provide a tool to convert Google Discovery documents to JSON Schemas,
so they can be used to validate JSON or YAML specs.

It requires to create a property builder for every discovery document you want to convert.

There are some already converted schemas in the `schemas` directory.

You can also check the builders in the `discovery_converter/builders` directory.

## Usage

Clone this repository

```bash
git clone git@github.com:itolosa/discovery-converter.git
```

Install the dependencies

```bash
poetry install
```

Run the generator

```bash
poetry run python generate.py
```

Check generated schemas in the `schemas` directory.

## Contributing

Feel free to contribute to this project by creating a new builder for a new discovery document.

You can also create a PR to improve the existing code or open an issue if you find a bug.

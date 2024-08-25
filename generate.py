import logging
from pathlib import Path

from discovery_converter import builders, convert, load_json
from discovery_converter.data import write_json

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    log.info("Generating schemas...")
    schemas_dir = Path("schemas")
    discovery_docs_dir = schemas_dir / "discovery_docs"

    for discovery_doc in discovery_docs_dir.glob("*.json"):
        discovery = load_json(str(discovery_doc))
        schema = convert(discovery, getattr(builders, discovery_doc.stem))
        output_file = str(schemas_dir / f"{discovery_doc.stem}.json")
        write_json(output_file, schema)

        log.info("Generated schema for %s", discovery_doc.stem)

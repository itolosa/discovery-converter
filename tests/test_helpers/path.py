from tests import TESTS_DIR


def fixture_path(file_name: str) -> str:
    return str(TESTS_DIR / "fixture_files" / file_name)

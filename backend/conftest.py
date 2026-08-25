import sys
from pathlib import Path

# Ensure the backend package root is on sys.path so tests can import `app`.
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def pytest_ignore_collect(collection_path, config):
    # Prevent collecting the example/run scripts in `tests` which are operational scripts
    # rather than unit tests. This keeps pytest fast during CI and local runs.
    try:
        p = Path(collection_path)
        if p.match("tests") or p.parts and "tests" in p.parts:
            return True
    except Exception:
        pass
    return False

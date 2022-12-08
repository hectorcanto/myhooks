"""Function and script to check you are inside a virtualenv"""
import sys
from pathlib import Path

__version__ = "0.1.0"


def in_venv():
    """Check virtualenv active using sys prefixes"""
    inside_venv = hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )
    if not inside_venv:
        print("You are not in a virtualenv")
        sys.exit(1)
    current_venv = sys.prefix.rsplit("/", 1)[-1]
    venv_without_hash = current_venv.split("-",1)[0]
    current_route = Path(__file__).parent.parent.resolve()

    if venv_without_hash not in str(current_route):
        print(f"You are not in the right a virtualenv: current: {current_venv}")
        sys.exit(1)
    print(f"You are in virtualenv '{current_venv}'")
    sys.exit(0)


if __name__ == "__main__":
    in_venv()


import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Return the path to the testdata directory."""
    return Path(__file__).parent / "_data"


@pytest.fixture
def has_snakemake() -> bool:
    """Return True if snakemake is installed."""
    try:
        subprocess.run(["snakemake", "--version"], check=True)
        return True
    except Exception:
        return False

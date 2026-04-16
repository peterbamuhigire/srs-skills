from pathlib import Path
import pytest

@pytest.fixture
def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"

@pytest.fixture
def tiny_project(fixtures_dir: Path) -> Path:
    return fixtures_dir / "tiny_project"

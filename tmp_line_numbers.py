from pathlib import Path
path = Path(__file__).resolve().parent / "README.md"
with path.open() as f:
    lines = f.read().splitlines()
for i, line in enumerate(lines, 1):
    if 35 <= i <= 80:
        print(f"{i:03d}: {line}")

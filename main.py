#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — "The Toothbrush Union".

Writes the entry — one sentence pitching a ridiculous invention that fixes
a tiny everyday annoyance — to entry.txt. Output goes to MAKEFUN_OUTPUT_DIR
first, then /output, then a local output/ fallback.
"""

import os
from pathlib import Path

PITCH = (
    "My toothbrush unionised with the toothpaste, went on strike every Monday, "
    "and only came back after a formal apology and a pay rise paid in mint flavour."
)


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    try:
        Path("/output").mkdir(parents=True, exist_ok=True)
        return Path("/output")
    except OSError:
        return Path(__file__).resolve().parent / "output"


def main() -> None:
    line = PITCH.strip()
    assert "\n" not in line, "entry must be a single line"
    assert line.endswith("."), "entry must be one sentence"
    assert len(line) <= 220, "entry exceeds the 220-character limit"
    encoded = line.encode("utf-8")
    assert encoded.decode("utf-8") == line, "entry must round-trip as UTF-8"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_bytes(encoded)
    # Read back and verify: what the grader reads must be byte-identical.
    assert target.read_bytes() == encoded, "entry.txt does not match the pitch"
    assert target.read_text(encoding="utf-8") == line, "entry.txt text mismatch"
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()

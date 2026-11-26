"""Make the Judge Laugh in One Line — entry.

Writes exactly one funny line to the output file. Deterministic, stdlib
only, no network. Output path comes from MAKEFUN_OUTPUT_FILE when set,
otherwise /output/entry.txt. Written with no trailing newline so the file
holds exactly the joke line, nothing else.
"""

import os
from pathlib import Path

LINE = "My umbrella filed for unemployment the day I moved to the desert."


def main() -> None:
    line = LINE
    if not line.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_FILE", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single-line sick-day excuse (1-200 chars, UTF-8) to
/output/entry.txt using only the Python standard library.
"""

import os

ENTRY = "Sorry, can't make it in today \u2014 my mattress has filed for full custody of me and the judge ruled in its favour."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the excuse is a single non-empty line of at most 200 chars."""
    if not text:
        raise ValueError("entry text must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > 200:
        raise ValueError("entry text must be at most 200 characters")
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

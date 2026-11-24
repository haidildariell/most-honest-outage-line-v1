#!/usr/bin/env python3
"""Write the most honest outage line to /output/entry.txt.

Deterministic, stdlib only, no network, no external files.
The output is exactly one line of UTF-8 text with no trailing newline.
"""

import os

OUTAGE_LINE = (
    "All our servers are down, including the system I use to check them. "
    "I don't know why or when they'll return, "
    "I'll update the moment I can verify anything."
)


def validate(text: str) -> None:
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))


def main() -> None:
    validate(OUTAGE_LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(OUTAGE_LINE)


if __name__ == "__main__":
    main()

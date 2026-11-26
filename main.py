#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest -- entry 1.

Writes one line (under 140 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "Every test passed on the first run, which is how I know none of them ever ran the app."


def main() -> None:
    # Gate (kit competition.yaml): entry.txt must be 1-140 UTF-8 characters.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate allows 1-140")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

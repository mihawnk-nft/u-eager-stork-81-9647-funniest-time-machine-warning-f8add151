#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes one original warning label for a time machine to /output/entry.txt.

Pure Python standard library: no dependencies, no network, deterministic.
"""

import os

# Gate caps from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 120 characters, not only white space.
MAX_CHARS = 120

# The one-line warning label (104 characters, measured -- well inside the
# 120-character gate).
# Voice: a deadpan official safety notice. Real hazard: meeting your own
# past self (a duplicate-self paradox). The joke turns the hazard into a
# debt: your past self has never paid you back. The surprise lands in the
# last few words -- he is standing behind you.
LABEL = (
    "WARNING: Do not lend money to your past self. "
    "He has never paid you back, and he is standing behind you."
)


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= MAX_CHARS, "label must be 1-120 characters"
    assert "\n" not in text, "label must be one line"
    assert text.strip() == text, "label must not start or end with whitespace"
    text.encode("utf-8")  # must be valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()

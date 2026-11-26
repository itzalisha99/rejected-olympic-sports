#!/usr/bin/env python3
"""Rejected Olympic Sports — entry writer.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, no network, no reads outside this repository.
"""

import hashlib
import os

ENTRY = (
    "Speed-reading the terms and conditions: the gold goes to the "
    "first athlete to reach the bottom and still have a soul."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text, 1 to 200 characters,
    not only white space, and a single line."""
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read it back and prove the file on disk is byte-identical
    # to what we meant to write.
    back = open(path, "rb").read()
    if back != data:
        raise ValueError("read-back mismatch: entry.txt differs from ENTRY")
    validate(back.decode("utf-8"))
    print(f"wrote {path}: {len(data)} bytes, md5 {hashlib.md5(data).hexdigest()}")


if __name__ == "__main__":
    main()

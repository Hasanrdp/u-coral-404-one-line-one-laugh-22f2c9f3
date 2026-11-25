#!/usr/bin/env python3
"""One Line, One Laugh — u-coral-404-one-line-one-laugh-22f2c9f3.

The entry program writes one funny line (114 characters) to
/output/entry.txt. The line is fixed and deterministic: the program
writes the same bytes on every run, and it refuses to report success
unless the file on disk matches the pinned hash and byte count.
"""

import hashlib
import os
import sys

LINE = "My password manager emailed to say my password is too weak, signed in with the same password I use for everything."

EXPECTED_SHA256 = "ad74f767b64e63ec0808404e347ce7aad134c26460a76421d2df5522ac8349b7"
EXPECTED_BYTES = 114
OUTPUT_PATH = "/output/entry.txt"


def verify(path, data):
    """Read the file back and refuse to succeed unless it is exactly the line."""
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if len(on_disk) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry is {len(on_disk)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(on_disk).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"entry sha256 {digest}, expected {EXPECTED_SHA256}")
    if on_disk != data:
        raise SystemExit("entry bytes differ from the line")
    return on_disk


def main():
    data = LINE.encode("utf-8")
    if not 1 <= len(data) <= 200:
        raise SystemExit(f"line is {len(data)} bytes, outside 1-200")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("line hash does not match the pinned hash")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    verify(OUTPUT_PATH, data)
    sys.stdout.write(
        f"wrote {OUTPUT_PATH} "
        f"({len(data)} bytes, sha256 {EXPECTED_SHA256})\n"
    )


if __name__ == "__main__":
    main()

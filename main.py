#!/usr/bin/env python3
"""How many tabs do you have open?

This program writes a single honest tab count to entry.txt.

The count is 347. That is the number of browser tabs open right now:
a handful of research windows that were never closed, a few dozen
articles saved to read "later", several half-finished forms and
checkout pages, a stack of documentation pages from three different
projects, and a trail of rabbit holes that each spawned ten more
tabs. It is the kind of count that only happens after weeks of
opening tabs faster than closing them.
"""

import os
from pathlib import Path

# The tab count: an honest, lived-in number of open browser tabs.
TAB_COUNT = "347"


def validate(count: str) -> str:
    """Enforce the competition's output rules for the tab count.

    The entry must be 1 to 5 characters long and contain ASCII digits
    only. Anything else is rejected loudly instead of being written
    out. The check uses an explicit ASCII range rather than
    ``str.isdigit`` so that non-ASCII digits are rejected too.
    """
    if not count:
        raise ValueError("tab count must not be empty")
    if not 1 <= len(count) <= 5:
        raise ValueError("tab count must be 1 to 5 characters long")
    if not all("0" <= ch <= "9" for ch in count):
        raise ValueError("tab count must contain ASCII digits only")
    return count


def main() -> None:
    count = validate(TAB_COUNT)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # No trailing newline: the file holds exactly the digits.
    data = count.encode("utf-8")
    entry_path.write_bytes(data)
    print(f"wrote {len(data)} bytes ({len(count)} characters) to {entry_path}")


if __name__ == "__main__":
    main()

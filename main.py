"""Write the one-line resignation letter in entry.txt to the output dir.

Reads entry.txt next to this file, strips surrounding whitespace, guards
against an empty or over-long line (gate: 1-140 characters), and writes the
single line to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
Stdlib only; runs under `python3 -S`.
"""

import os
import sys

ENTRY_FILE = "entry.txt"
MAX_CHARS = 140


def load_entry(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except OSError as exc:
        sys.exit("cannot read %s: %s" % (path, exc))
    except UnicodeDecodeError as exc:
        sys.exit("entry.txt is not valid UTF-8: %s" % exc)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    line = load_entry(os.path.join(here, ENTRY_FILE))
    if not line:
        sys.exit("entry.txt is empty")
    if len(line) > MAX_CHARS:
        sys.exit("entry is %d characters, over the 140 limit" % len(line))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError as exc:
        sys.exit("cannot write output: %s" % exc)


if __name__ == "__main__":
    main()

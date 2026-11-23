"""The Vacuum's Alibi (make.fun, u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

Writes one original one-line excuse a robot vacuum gives for missing a spot
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic, no
network, no model call: the line is a fixed text, so two runs produce
byte-identical output.
"""

import os
from pathlib import Path

# Deadpan machine voice, smug about its sensors: the lidar is declared
# right and the human wrong, and the punch turns the missed crumb into a
# "rounding error with ambition" -- a precise, unexpected detail that lands
# on the last word. No stock appliance joke, no cat, no dead battery.
LINE = (
    "My lidar shows a clean floor. "
    "The crumb you are pointing at is a rounding error with ambition."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    text = LINE.strip()
    if not text:
        raise SystemExit("line must not be only whitespace")
    if len(text) != len(LINE):
        raise SystemExit("line must not need trimming")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

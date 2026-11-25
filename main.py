"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

FORTUNE = (
    "The stars foresee great wealth in your future, starting the day "
    "you stop borrowing it from them."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()

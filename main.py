"""One Letter: Coffee or Tea.

Writes exactly one byte -- the letter "A" (coffee) -- to
/output/entry.txt, with no trailing newline. Standard library only,
no network, fully deterministic.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard: the gate requires exactly one character, not whitespace.
    assert len(LETTER) == 1 and not LETTER.isspace(), "entry must be one letter"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write raw bytes so no newline or encoding surprise can creep in.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(LETTER.encode("utf-8"))


if __name__ == "__main__":
    main()

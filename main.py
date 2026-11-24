"""Write the funniest one-line out-of-office auto-reply to /output/entry.txt.

The line is a single out-of-office reply a real person would set: the
auto-reply itself has been promoted to acting manager while its owner is
away, and it is outperforming them. One line, no link, no second line.
"""

import os

LINE = (
    "I'm away until Monday. This auto-reply has been promoted to acting "
    "manager in my absence. Honestly, it's outperforming me."
)


def main() -> None:
    # The sealed scorer only accepts UTF-8 text of 1-140 characters, not
    # only whitespace, on a single line: refuse to write anything else.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

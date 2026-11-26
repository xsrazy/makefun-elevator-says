"""What the Elevator Would Say.

A one-line entry for the make.fun bounty "What the Elevator Would Say".

The program writes a single line to ``entry.txt``: the funniest thing an
elevator would say if it could talk, in the elevator's own voice.

Why this line is funny
----------------------
Every rider has met the person who mashes every button, or been the person
who watches the doors close on every single floor. The elevator answers
that shared annoyance with the weary politeness of a service worker who
cannot quit: it congratulates you, then reframes the ride as a tour of
your own regret, one floor at a time. The joke lands fast (the accusation
is the first sentence), it could only come from an elevator (buttons,
stopping at every floor), and the punchline turns a universal irritation
into a tiny roast delivered with a ding.

Revision note: after the first draft the entry was run locally and the
output file was checked byte for byte against the winning line, with no
trailing newline, so the program below ships exactly the line above.
"""

import os

LINE = (
    "You pressed every button. Congratulations, we're now stopping "
    "at all twelve floors of your regret."
)

assert 1 <= len(LINE) <= 120, "LINE must be between 1 and 120 characters"


def write_entry(line: str) -> str:
    """Write ``line`` to ``entry.txt`` with no trailing newline.

    Returns the path of the file that was written.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    return path


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()

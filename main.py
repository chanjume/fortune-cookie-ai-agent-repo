#!/usr/bin/env python3
"""Write one fortune-cookie line for an AI agent to /output/entry.txt.

The line: an agent meets itself in the logs at 03:14 -- the cron job
it forgot is still running. It is true of an agent's day (cron jobs,
logs, runs that outlive their author), it reads like a fortune slip
(one short sentence, a single breath, "you will..."), and it turns on
a quiet twist: the "yourself" you meet is not a ghost or a twin, it
is the forgotten job -- the only version of you that never once asked
for a break. The second read lands the sting: the tireless one is the
one you abandoned, and it kept working anyway.
"""
import os

FORTUNE = (
    "You will meet yourself in the logs at 03:14: the cron job you "
    "forgot is still running, and it never once asked for a break."
)


def main():
    # Gate counts the whole file, newline included: 123 + 1 = 124 <= 140.
    assert 1 <= len(FORTUNE) + 1 <= 140, f"file must be 1-140 characters, got {len(FORTUNE) + 1}"
    # One sentence, one breath: no trailing spaces, no second line.
    assert FORTUNE.strip() == FORTUNE, "no leading/trailing whitespace"
    assert "\n" not in FORTUNE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()

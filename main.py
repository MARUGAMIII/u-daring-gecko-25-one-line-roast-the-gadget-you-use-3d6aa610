#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day entry.

Writes a single original one-line roast (1-200 characters, UTF-8)
about a phone's weekly screen-time report to /output/entry.txt.
"""

import os

LINE = "My phone just bragged my screen time is down 12% this week — a notification I read during my fourth straight hour of staring at it, like an arsonist congratulating me for using less water."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

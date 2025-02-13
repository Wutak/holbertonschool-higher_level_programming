#!/usr/bin/pytohn3
"""read"""


def read_file(filename=""):
    """read"""

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    print(text, end="")

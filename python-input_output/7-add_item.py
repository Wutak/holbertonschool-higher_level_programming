#!/usr/bin/python3
"""add item"""
import json
import sys
from save_json_file import save_to_json_file
from load_json_file import load_from_json_file


def main():
    """main"""

    filename = "add_item.json"

    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filenames)

if __name__  = "__main__":
    main()

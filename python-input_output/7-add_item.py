#!/usr/bin/python3
"""json"""


import sys
import json
from save_json_file import save_to_json_file
from load_json_file import load_from_json_file

def main()
    """json"""

    filename = "add_item.json"

    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()

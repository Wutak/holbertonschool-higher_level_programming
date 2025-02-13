#!/usr/bin/python3
"""json"""


import json


def save_to_json_file(my_obj, filename):
    """json"""

    with open(filename, "w", encoding="utf-8") as file:
        dump = json.dumps(my_obj)
        file.write(dump)

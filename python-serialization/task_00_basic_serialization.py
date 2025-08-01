#!/usr/bin/env python3
"""serialization"""


def serialize_and_save_to_file(data, filename):
    """serialize"""
    with open(filename, "w") as file:
        file.write(str(data).replace("'", "'"))

def load_and_deserialize(filename):
    """deserialize"""
    with open(filename, "r") as file:
        content = file.read()
        return eval(conntent.replace("null", "None"))

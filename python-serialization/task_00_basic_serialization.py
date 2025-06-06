#!/usr/bin/env python3
"""serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize"""
        with open(filename, "w") as file:
            json.dump(data, file)
        return filename

def load_and_deserialize(filename):
    """deserialize"""
        with open(filename, "r") as file:
            data = json.load(file)
        return data

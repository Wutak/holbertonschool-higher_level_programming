#!/usr/bin/env python3
"""serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize"""
    with open(filename, "w") as file:
        return json.dump(data, file)
    pass

def load_and_deserialize(filename):
    """deserialize"""
    with open(filename, "r") as file:
        return json.load(file)
    pass
        

#!/usr/bin/python3
"""serialization"""


import json


def serialize_and_save_to_file(data, filename):
    """serialize"""
    try:
        with open("filename", "w") as file:
            json.dump(data, file)
        except Exception as exc:
            print(f"Error serializing data: {exc}")

def load_and_deserialize(filename):
    """deserialize"""
    try:
        with open("filename", "r") as file:
            return json.load(file)
    except Exception as exc:
        print(f"Error deserializing data: {exc}")
        return None

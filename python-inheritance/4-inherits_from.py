#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """inherits from"""
    if issubclass(obj, a_class):
        return True
    else:
        return False

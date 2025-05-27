#!/usr/bin/python3
"""kind of class"""


def is_kind_of_class(obj, a_class):
    """kind of class"""
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    else:
        return False

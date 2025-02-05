#!/usr/bin/python3
"""return true if object is an instance of the class or an inherited"""


def is_kind_of_class(obj, a_class):
    """checks if obj is instance of a class inherited from a_class"""

    if isinstance(obj, a_class) is True:
        return True
    else:
        return False

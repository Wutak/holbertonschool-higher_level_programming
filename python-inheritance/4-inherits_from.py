#!/usr/bin/python3
"""return True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """cheks if obj is instance of class inherited from a_class"""

    return isinstance(obj, a_class) and type(obj) is not a_class

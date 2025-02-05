#!/usr/bin/python3
"""return True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """cheks if obj is instance of class inherited from a_class"""

    if isinstance(obj, a_class) is True:
        return True
    else:
        return False

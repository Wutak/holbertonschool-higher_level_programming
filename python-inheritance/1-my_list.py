#!/usr/bin/python3
"""my list"""


class Mylist(list):
    """
    mylist
    """

    def print_sorted(self):
        """print"""
        if not isinstance(self, int):
            raise AttributeError("instance must be a int")
        else:
            print(sorted(self))

#!/usr/bin/python3
"""my list"""


class Mylist(list):
    """mylist"""

    def print_sorted(self):
        """print"""
        if not isinstance(self, list):
            raise AttributeError("instance must be a list")
        else:
            print(sorted(self))

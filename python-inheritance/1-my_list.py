#!/usr/bin/python3
"""MyList inherits from list and print it sorted"""


class MyList(list):
"""MyList inherits from list"""

    def print_sorted(self):
        """print list sorted"""
        if not isinstance(self, list):
            raise AttributeError("instance must be a list")
        else:
            print(sorted(self))

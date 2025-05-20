#!/usr/bin/python3
"""class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """retrieve size"""
        return self.size

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """area"""
        return self.size**2

    def my_print(self):
        """print"""
        if size == 0:
            print("")
        else:
            for i in range(self.size):
                print(self.size * "#")

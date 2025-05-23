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
        return self._size

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """area"""
        return self.size**2

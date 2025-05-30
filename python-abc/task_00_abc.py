#!/usr/bin/python3
"""ABC"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """class animal"""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """class dog"""

    def sound(self):
        return "Bark"

class Cat(Animal):
    """class cat"""

    def sound(self):
        return "Meow"

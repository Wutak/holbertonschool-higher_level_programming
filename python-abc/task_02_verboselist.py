#!/usr/bin/python3
class VerboseList(list):

    def append(self, item):
        print(f"Added [{item]} to the list.")
        super().append(item)

    def extend(self, iterable):
        count = len(iterable)
        print(f"Extended the list with [{count}] items.")
        super().extend(iterable)

    def remove(self, item):
        if item not in self:
            raise ValueError("Can't find this value in this instance")
        print(f"Removed [{item}] from the list.")
        super().remove(item)
        
    def pop(self, index=-1):
        
        if self[item] is None:
            raise IndexError("Index does not exist")
        print(f"Popped[{item}] from the list.")
        retour =  super().pop(item)
        return retour

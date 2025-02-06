#!/usr/bin/python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item]} to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        item = self[index] if len(self) > 0 else None
        if item is not None:
            print(f"Popped[{item}] from the list.")
            return super().pop(index)
        else:
            print("Cannot  pop from an empty list.")
            return None

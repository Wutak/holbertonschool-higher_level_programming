#!/usr/bin/python3


class Verboselist(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item]} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        try:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        except ValueError:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        try:
            item = super().pop(index)
            print(f"Popped[{item}] from the list.")
            return item
        except IndexError:
            print("Attempted to pop from an empty list.")
            raise

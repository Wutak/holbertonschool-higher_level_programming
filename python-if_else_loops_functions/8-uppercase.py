#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            c = c - 32
            print("{}".format(c), end="")
        else
            print("{}".format(c), end="")

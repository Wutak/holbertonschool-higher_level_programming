#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list[::-1]

    for i in my_list:
        print("{:d}".format(i))

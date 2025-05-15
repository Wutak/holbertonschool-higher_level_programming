#!/usr/bin/python3
def new_in_line(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list = [i for i in my_list]
    new_list[idx] = element
    return new_list

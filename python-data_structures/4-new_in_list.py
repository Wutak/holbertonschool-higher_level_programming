#!/usr/bin/python3
def new_in_line(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    copie = list(my_list)
    copie[idx] = element
    return new_list

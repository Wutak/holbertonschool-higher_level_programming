#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]
        for i in my_list:
            if i > max_value[0]:
                max_value[0] = i
        return max_value
    return(None)

#!/usr/bin/python3
def update_dicitonary(a_dictionary, key, value):
    for k, v in a_dictionary.item():
        if k == key:
            a_dictionay[k] = value
            break
        else:
            a_dictionary[key] = value
        return(a_dictionary)

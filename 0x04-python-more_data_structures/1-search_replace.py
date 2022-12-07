#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list.copy()
    for item in new_list:
        if item == search:
            new_list[item] = replace
    return new_list

#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    list_set = set(my_list)
    unique_list = list(list_set)
    unique_sum = 0
    for i in range(len(unique_list)):
        unique_sum += unique_list[i]
    return (unique_sum)

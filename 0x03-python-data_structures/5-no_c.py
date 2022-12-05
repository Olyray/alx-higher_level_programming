#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    list_len = len(string_list)
    for i in range(list_len):
        if list_len > len(string_list):
            break
        elif string_list[i] == 'c' or string_list[i] == 'C':
            string_list.pop(i)
    new_string = "".join(string_list)
    return new_string

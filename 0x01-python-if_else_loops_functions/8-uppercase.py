#!/usr/bin/python3
def uppercase(str):
    str_list = list(str)
    for i in range(len(str_list)):
        ascii_value = ord(str_list[i])
        if ascii_value >= 97 and ascii_value <= 122:
            str_list[i] = chr(ord(str_list[i]) - 32)
    final_string = "".join(str_list)
    print("{}".format(final_string))

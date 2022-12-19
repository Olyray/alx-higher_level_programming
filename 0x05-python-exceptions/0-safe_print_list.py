#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    character_count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            character_count += 1
    except IndexError:
        pass
    print()
    return character_count

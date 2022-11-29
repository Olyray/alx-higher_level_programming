#!/usr/bin/python3
def uppercase(str):
    ascii_value = ord(str)
    if ascii_value >= 97 and ascii_value <= 122:
        return True
    else:
        return False

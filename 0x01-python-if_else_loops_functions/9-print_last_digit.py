#!/usr/bin/python3
def print_last_digit(number):
    number_str = str(number)
    print(number_str[len(number_str) - 1], end="")
    return number_str[len(number_str) - 1]

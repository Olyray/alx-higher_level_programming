#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
number_str = str(number)
if int(number_str[len(number_str) - 1]) > 5:
    print(
        f"Last digit of {number} is {number_str[len(number_str) - 1]}\
 and is greater than 5"
    )
elif int(number_str[len(number_str) - 1]) == 0:
    print(f"Last digit of {number} is {number_str[len(number_str) - 1]}\
 and is 0")
elif int(number_str[len(number_str) - 1]) < 6:
    print(
        f"Last digit of {number} is {number_str[len(number_str) - 1]}\
 and is less than 6 and not 0"
    )

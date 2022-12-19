#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_of_sums = [None] * list_length
    for i in range(list_length):
        try:
            list_of_sums[i] = my_list_1[i]/my_list_2[i]
        except (TypeError, ValueError):
            list_of_sums[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            list_of_sums[i] = 0
            print("division by 0")
        except IndexError:
            list_of_sums[i] = 0
            print("out of range")
        finally:
            pass
    return list_of_sums

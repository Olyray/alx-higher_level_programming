#!/usr/bin/python3
"""Find the peak from a list of integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: The peak integer.

    """
    if len(list_of_integers) == 0:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid+1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_ind = 0
    for val in range(len(arr)):
        if arr[val] < arr[min_ind]:
            min_ind = val
    return min_ind



from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    l_ = 0
    r_ = len(arr) - 1

    while l_ <= r_:
        cur_ind = (l_ + r_) // 2
        if elem < arr[cur_ind]:
            r_ = cur_ind - 1
        elif elem > arr[cur_ind]:
            l_ = cur_ind + 1
        else:
            while arr[cur_ind - 1] == elem:
                cur_ind -= 1
            return cur_ind

    return None



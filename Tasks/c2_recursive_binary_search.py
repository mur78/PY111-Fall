from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    cur_ind = len(arr) // 2
    if not arr:
        return None
    elif len(arr) == 1:
        return cur_ind if arr[cur_ind] == elem else None
    elif arr[cur_ind] == elem:
        while arr[cur_ind - 1] == elem:
            cur_ind -= 1
        return cur_ind
    else:
        if elem < arr[cur_ind]:
            return binary_search(elem, arr[:cur_ind])
        elif elem > arr[cur_ind]:
            r_binary = binary_search(elem, arr[cur_ind:])
            return cur_ind + r_binary if r_binary is not None else None



    # print(elem, arr)
    # return None

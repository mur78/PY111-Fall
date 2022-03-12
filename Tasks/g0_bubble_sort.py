from typing import List
from operator import lt, gt

def sort(container: List[int], ascending: bool = True, inplace: bool = True) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not inplace:
        container = container.copy()
    compare_operator = gt if ascending else lt
    offset = 1
    for _ in range(len(container)):
        is_change = False
        for i in range(len(container) - offset):
            # if container[i] > container[i + 1]:
            if compare_operator(container[i], container[i+1]):
                container[i], container[i+1] = container[i+1], container[i]
                is_change = True
            offset += 1
            if not is_change:
                break
    return container
if __name__ == 'main':
    # print(sort())
    list_ = [3, 2, 1]
    sorted_copy = sort(list_, inplace=False)
    print(list_)
    print(sorted_copy)
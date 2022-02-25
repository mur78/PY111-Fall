from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    # print(stairway)
    # return direct_stairway_path(stairway)
    # return reverse_stairway_path(stairway)
    return stairway_path_lazy(stairway)

def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
   Прямой метод

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    count_stairs = len(stairway)
    total_cost = [float("inf")] * count_stairs  # стоимсоть перемещения

    total_cost[0] = stairway[0]
    total_cost[1] = stairway[1]

    for i in range(0, count_stairs):  # len(stairway)
        if i + 1 < count_stairs:
            total_cost[i + 1] = min(total_cost[i + 1], stairway[i + 1] + total_cost[i])
        if i + 2 < count_stairs:
            total_cost[i + 2] = min(total_cost[i + 2], stairway[i + 2] + total_cost[i])
    return total_cost[-1]

def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
   обратный метод

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    stairway # цены на ступени
    count_stairs = len(stairway)
    total_cost = [float("inf")] * count_stairs  # стоимсоть перемещения

    total_cost[0] = stairway[0]
    total_cost[1] = min(stairway[1], stairway[0] + stairway[1])

    for i in range(2, count_stairs): # len(stairway)
        total_cost[i] = stairway[i] + min(total_cost[i-2], total_cost[i-1])
    return total_cost[-1]


def stairway_path_lazy(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
     ленивый метод

      :param stairway: list of ints, where each int is a cost of appropriate step
      :return: minimal cost of getting to the top
      """
    total_coasts = {}
    def lazy_path(stair_number):

        if stair_number in total_coasts:
            return total_coasts[stair_number]

        if stair_number == 0:
            total_coasts[stair_number] = stairway[stair_number]
            return total_coasts[stair_number]

        if stair_number == 1:
            total_coasts[stair_number] = stairway[stair_number]
            return total_coasts[stair_number]

        current_cost = stairway[stair_number] + min(lazy_path(stair_number - 1), lazy_path(stair_number -2))
        total_coasts[stair_number] = current_cost
        return total_coasts[stair_number]

    return lazy_path(len(stairway) -1)

from functools import lru_cache
def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    # print(shape, point)
    # return 0
    rows = shape[0]  # количество строк
    cols = shape[1]  # количество столбцов

    @lru_cache
    def count_paths(i, j):

        if i == 0 or j == 0:
            return 1
        if not 0 <= i < rows:
            return 0
        if not 0 <= j < cols:
            return 0

        return sum([count_paths(i-2, j-1),
                    count_paths(i-2, j+1),
                    count_paths(i-1, j-2),
                    count_paths(i+1, j-2)
                    ])

    return count_paths(point[0], point[1])

# if __name__ == '__main__':
#     assert 13309 == calculate_paths((7, 15), (6, 14))
#     assert 2 == calculate_paths((4, 4), (3, 3))
def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError

    if n == 0 or n == 1:
        return 1

    return n * factorial_iterative(n-1)

    # print(n)
    # return 0


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """

    if n < 0:
        raise ValueError
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


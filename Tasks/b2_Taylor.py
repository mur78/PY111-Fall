"""
Taylor series
"""
from typing import Union
import math
from itertools import count


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    EPS_ = 0.0001
    sum_ = 0

    def g_item(n):
        return (x ** i) / math.factorial(i)

    for i in count(0, 1):
        c_var = g_item(i)
        if c_var <= EPS_:
            return sum_
        else:
            sum_ += c_var


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    EPS_ = 0.0001
    sum_ = 0

    def g_item(n):
        return ((-1) ** (i)) * ((x**(2*i + 1))/math.factorial(2*i + 1))

    for i in count(0, 1):
        c_var = g_item(i)
        sum_ += c_var
        if abs(c_var) <= EPS_:
            return sum_


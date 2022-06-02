#!/usr/bin/env python

'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
'''

import ipdb
import pytest


# from code wars
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
#------


# MY SOLUTION ===============
def divided_by(b):
    return "divide", b


def plus(b):
    return "plus", b


def minus(b):
    return "minus", b


def times(b):
    return "times", b


def common_calc(operation: str, right_int: int, left_int: int) -> int:
    """
    :param operation: str - операция делания, умножения и тд
    :param left_int: int - число слева
    :param right_int: int - число справа
    :return: int - результат арифметической операции
    """
    if operation == "divide":
        if right_int != 0:
            return int(left_int) // int(right_int)
    elif operation == "plus":
        return left_int + right_int
    elif operation == "minus":
        return left_int - right_int
    elif operation == "times":
        return left_int * right_int
    else:
        return None


def zero(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 0) if number_or_func else 0


def one(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 1) if number_or_func else 1


def two(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 2) if number_or_func else 2


def three(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 3) if number_or_func else 3


def four(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 4) if number_or_func else 4


def five(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 5) if number_or_func else 5


def six(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 6) if number_or_func else 6


def seven(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 7) if number_or_func else 7


def eight(number_or_func=None):

    return common_calc(number_or_func[0], number_or_func[1], 8) if number_or_func else 8


def nine(number_or_func=None):
    return common_calc(number_or_func[0], number_or_func[1], 9) if number_or_func else 9


@pytest.mark.parametrize("input_, expected",
                         [(plus(nine()), 13)])
def test_solution_four(input_, expected):
    assert four(input_) == expected

@pytest.mark.parametrize("input_, expected",
                         [(divided_by(two()), 3)])
def test_solution_six(input_, expected):
    assert six(input_) == expected

#--- 7 ---
@pytest.mark.parametrize("input_, expected",
                         [(times(five()), 35)])
def test_solution_seven(input_, expected):
    assert seven(input_) == expected

@pytest.mark.parametrize("input_, expected",
                         [(minus(three()), 5)])
def test_solution_eight(input_, expected):
    assert eight(input_) == expected


if __name__ == '__main__':

    # print(eight())
    #print(divided_by(three()))

    #print(seven(times(five())))
    print(eight(minus(three())))
    #print(four(plus(nine())))
    #print(eight(divided_by(three())))



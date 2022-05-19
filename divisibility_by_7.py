#!/usr/bin/env python

"""
https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python
"""
import ipdb
import pytest

DIVIDER = 10


def seven(m, step=0):
    if m < 100:
        return m, step

    x, y, step = m // 10, m % 10, step + 1
    res = x - 2 * y
    return seven(res, step)


def seven_my(m: int) -> tuple:
    """
    :param m: int - входное число
    :return: (остаток , количество делений)  # в задании неправильно написано!
    """

    # количество делений
    counter = 0

    if m == 0:
        return 0, 0

    while True:
        ostatok = m % DIVIDER
        m = m // DIVIDER
        counter += 1

        m = m - 2 * ostatok
        if m < 100:
            break

    return m, counter


@pytest.mark.parametrize("input_, expected",
                         [(1603, (7, 2)),
                          (371, (35, 1)),
                          (483, (42, 1)),
                          (483595, (28, 4))])
def test_solution(input_, expected):
    assert seven(input_) == expected


if __name__ == '__main__':
    print(seven(371))
    # print(seven(0))
    # print(seven(1603))

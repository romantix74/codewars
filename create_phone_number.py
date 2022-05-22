#!/usr/bin/env python

"""
https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python
"""
import ipdb
import pytest

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number_MY(n: list) -> str:
    """
    :param n: int - входной массив чисел
    :return: номер телефона в заданном формате
    """
    out_str = ""

    out_str = [str(i) for i in n]
    return f"({''.join(out_str[0:3])}) {''.join(out_str[3:6])}-{''.join(out_str[6:])}"

    #return [str.join(out_str) for i in n]


@pytest.mark.parametrize("input_, expected",
                         [([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"),
                          ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "(111) 111-1111"),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"),
                          ([0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890")])
def test_solution(input_, expected):
    assert create_phone_number(input_) == expected


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


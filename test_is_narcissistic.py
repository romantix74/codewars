#!/usr/bin/env python

import pytest
import ipdb

def solution_from_codewars(value):
    return bool(value == sum([int(a) ** len(str(value)) for a in str(value)]))

def is_narcissistic(value: int) -> bool:
    # Code away
    #ipdb.set_trace()
    input_digits = str(value)
    print(f" length is {len(input_digits)}")
    sum = 0
    for i in range(len(input_digits)):
        print(input_digits[i])
        sum += int(input_digits[i])**len(input_digits)

    return True if sum == value else False

@pytest.mark.parametrize("int_, expected",
                         [(7, True),
                          (371, True ),
                          (122, False),
                          (4887, False)])
def test_solution(int_, expected):
    assert is_narcissistic(int_) == expected

if __name__ == '__main__':
    print(is_narcissistic(371))
    print(is_narcissistic(22))
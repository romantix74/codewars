#!/usr/bin/env python

'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
'''

import pytest

@pytest.mark.parametrize("a_, b_, expected",
                         [([1,2], [1], [2]),
                          ([1,2,2], [1], [2,2]),
                          ([1,2,2], [], [1,2,2]),
                          ([], [1,2], [])])
def test_solution(a_, b_, expected):
    assert array_diff(a_, b_) == expected


def array_diff(a: list, b:list) -> list:
    return [i for i in a if i not in b]

if __name__ == '__main__':
    print(array_diff([1,2], [1]))
"""
https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
"""

import string
import pytest

def to_jaden_case_MY(_string):
    return " ".join(s.capitalize() for s in _string.split())

def to_jaden_case(_str):
    return string.capwords(_str)

@pytest.mark.parametrize("string, expected",
                         [("How can mirrors be real if our eyes aren't real",
                           "How Can Mirrors Be Real If Our Eyes Aren't Real")])
def test_solution(string, expected):
    assert to_jaden_case(string) == expected

if __name__ == '__main__':
    print(to_jaden_case("How can mirrors"))

#!/usr/bin/env python
import ipdb
import pytest


# from codewars
def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a

def move_zeros_FROM_CODE_WARS(array):
    for i in array:
        if i == 0:
            array.remove(i)  # Remove the element from the array
            array.append(i)  # Append the element to the end
    return array


def move_zeros_MY(array):
    out_arr = []
    zero_counter = 0
    for i, val in enumerate(array):
        print(i, val)
        if val != 0:
            out_arr.append(val)
        if val == 0:
            zero_counter += 1
    [ out_arr.append(0) for i in range(zero_counter)]
    return out_arr



@pytest.mark.parametrize("input_, expected",
                         [([1, 2, 0, 1, 0, 1, 0, 3, 0, 1],
                           [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
                          ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
                           [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                          ([0, 0],
                          [0, 0]),
                          ([], []),
                          ([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
                            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                          )
                          ])
def test_solution(input_, expected):
    assert move_zeros(input_) == expected


if __name__ == '__main__':
    # print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
    print(move_zeros([4, 0, 0, 7]))
    # print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

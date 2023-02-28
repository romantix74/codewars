#!/usr/bin/env python

"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
    He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, 
    but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
"""


"""
!!! SOLUTION FROM CODEWARS !!!

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
"""


import pytest

from itertools import product


def get_list_for_digit(digit: str) -> list:
    if int(digit) == 1:
        out_list = ['1','2','4']
    if int(digit) == 2:
        out_list = ['1','2','3','5']
    if int(digit) == 3:
        out_list = ['2','3','6']
    if int(digit) == 4:
        out_list = ['1','4','5','7']
    if int(digit) == 5:
        out_list = ['2','4','5','6','8']
    if int(digit) == 6:
        out_list = ['3','5','6','9']
    if int(digit) == 7:
        out_list = ['4','7','8']
    if int(digit) == 8:
        out_list = ['5','7','8','9','0']
    if int(digit) == 9:
        out_list = ['6','8','9']
    if int(digit) == 0:
        out_list = ['0','8']
    return out_list

def get_pins(observed) -> list:

    # observed_len = len(observed)
    # print(observed_len)
    
    out_list = []
    for digit in observed:
        print(digit)
    
    #return [[].append(get_pins(i)) for i in observed]
      
    #return [ get_list_for_digit(i) for i in observed ]
    print(*[ get_list_for_digit(i) for i in observed ])
    print("-----")
    for i in  product( *[ get_list_for_digit(i) for i in observed ] ):
        print(''.join(i))
        out_list.append(''.join(i))
    
    return (out_list) #['5','7','8','9','0']



@pytest.mark.parametrize("input_, expected",
                         [('8', ['5','7','8','9','0']),
                          ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                          ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])
                        ])
def test_solution(input_, expected):
    assert get_pins(input_) == expected


if __name__ == "__main__":

    #pin = '81'
    pin = '11'
    #pin = '369'
    print(get_pins(pin))
    
    #print(get_pins('2'))
#!/usr/bin/env python

"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

Given an n x n array, return the array elements arranged from outermost 
elements to the middle element, traveling clockwise.
"""

'''
# SOLUTION FROM CODEWARS

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
'''

#import ipdb
import pytest

out_list = []

def snail(snail_map):
    # calc side
    side_len = len(snail_map[0])
    print(f"side_len is: {side_len}")
    #print(side_len)
    out_list = []
    
    # идем от большого квадарат внутрь, уменьшая сторону и сдигаясь циклично на 1
    for cur_side in range(side_len):  #//2+1): #range(side_len,0):

        
        print(f"cur_side is: {cur_side}")
        
        # первая строка 
        #out_list += snail_map[0]
        out_list += snail_map[cur_side][cur_side:side_len-cur_side]
        
        if cur_side == side_len//2:
            return out_list

        
        # правый бок берем, уменьшая сразу и сверху и снизу, 
        # чтобы внизу сразу целую строку брать
        for i in range(cur_side+1,side_len-cur_side-1):
            out_list.append(snail_map[i][-cur_side-1])
    
        # низ
        #print(list(reversed(snail_map[side_len-1])))
        out_list += list(reversed(snail_map[side_len-1-cur_side][cur_side:side_len-cur_side]))
        
        # левый бок , конец
        #import ipdb; ipdb.set_trace()
        for i in reversed(range(cur_side+1,side_len-cur_side-1)):
            out_list.append(snail_map[i][cur_side])
     
    return out_list

@pytest.mark.parametrize("input_, expected",
                        [([[1,2,3],
                        [4,5,6],
                        [7,8,9]], 
                          [1,2,3,6,9,8,7,4,5]),
                         
                        ([[1,2,3],
                        [8,9,4],
                        [7,6,5]],
                         [1,2,3,4,5,6,7,8,9]),
                        
                        ([[1,2,3,1],
                        [4,5,6,4],
                        [7,8,9,7],
                        [7,8,9,7]],
                        [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8] )
                        ])
def test_solution(input_, expected):
    assert snail(input_) == expected

if __name__ == "__main__":
    input1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
    input2= [[1,2,3,1],
             [4,5,6,4],
             [7,8,9,7],
             [7,8,9,7]]
    input3 = [[1,2,3,4,5],
              [16,17, 18, 19, 6,],
              [15, 24, 25, 20, 7],
              [14, 23, 22, 21, 8],
              [13, 12, 11, 10, 9]]
    
    print(snail(input3))
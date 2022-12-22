#!/usr/bin/env python

import pytest
import re

"""
import socket

def is_valid_IP(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False
        
def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))       
"""


def is_valid_IP(strng):
    s_lst = strng.split('.')
    
    print(s_lst)
    
    #match = re.search(r'[1-9]d+(.)[0-9]+(.)')
    
    if len(s_lst) != 4:
        return False
    for i in s_lst:
        if not i.isnumeric():
            return False
        if i == '':
            return False
        if int(i) > 255:
            return False
        if len(i) == 1:  # 0.0.0.0
            continue
        if int(i[0]) == 0:
            print(i)
            print(type(i))
            print(i[0])
            return False
    return True


@pytest.mark.parametrize("input_, expected",
                         [('12.255.56.1', True),
                          ('', False),
                          ('abc.def.ghi.jkl', False),
                          ('123.456.789.0', False),
                          ('.456.789.0', False)])
def test_solution(input_, expected):
    assert is_valid_IP(input_) == expected


if __name__ == '__main__':
    #print(is_valid_IP('12.255.56.1'))
    # 149.104.241.90
    #print(is_valid_IP('149.104.241.90')) # True
    #print(is_valid_IP('123.045.067.089'))
    #print(is_valid_IP('192.168.1.300'))
    print(is_valid_IP('.168.1.300'))
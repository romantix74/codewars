#!/usr/bin/env python

"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/python
"""
import ipdb
import pytest


"""
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

# from codewars solution
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

@pytest.mark.parametrize("input_, expected",
                         [('Pig latin is cool', 'igPay atinlay siay oolcay'),
                          ('Hello world !', 'elloHay orldway !')])
def test_solution(input_, expected):
    assert move_first_letter_of_each_word_to_the_end(input_) == expected


def move_first_letter_of_each_word_to_the_end(text: str)-> str:
    return ' '.join([f"{i[1:]}{i[0]}ay" if i not in ['!',',','?'] else i for i in text.split() ])
    # out_str= '' 
    # for i in s.split():
    #     #print(i)
    #     out_str += i[1:]
    # return out_str

if __name__ == '__main__':
    print(move_first_letter_of_each_word_to_the_end('Pig latin is cool'))
    print(move_first_letter_of_each_word_to_the_end('Hello world !'))
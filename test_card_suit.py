#!/usr/bin/env python

import pytest


# from codewars
def define_suit(card):
    d = {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}
    return d[card[-1]]


def define_suit_MY(card):
    if card[-1] == 'C':
        return 'clubs'
    elif card[-1] == 'S':
        return 'spades'
    elif card[-1] == 'D':
        return 'diamonds'
    else:
        return 'hearts'


@pytest.mark.parametrize("input_, expected",
                         [('3C', 'clubs'),
                          ('QS', 'spades'),
                          ('9D', 'diamonds'),
                          ('JH', 'hearts')])
def test_solution(input_, expected):
    assert define_suit(input_) == expected


if __name__ == '__main__':
    print(define_suit('3C'))

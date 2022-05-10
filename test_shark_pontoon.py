#!/usr/bin/env python
import ipdb
import pytest

"""
https://www.codewars.com/kata/57e921d8b36340f1fd000059/train/python
"""


def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2

    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed

    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"

def shark_MY(pontoon_distance: int, shark_distance: int, you_speed: int, shark_speed: int, dolphin: bool) -> str:
    """

    :param pontoon_distance:
    :param shark_distance:
    :param you_speed:
    :param shark_speed:  relative to you !!!
    :param dolphin:
    :return:
    """
    #ipdb.set_trace()
    if dolphin:
        shark_speed = shark_speed/2

    if shark_distance < pontoon_distance:
        return "Shark Bait!"

    if shark_speed <= you_speed:
        return "Alive!"

    # время, за которое акула до понтона
    time_shark = shark_distance/shark_speed

    # время, за которое ты доплывешь до понтона
    time_you = pontoon_distance/you_speed

    # время, за которое тебя догонят
    time_attack = (shark_distance - pontoon_distance) / shark_speed

    #ipdb.set_trace()

    if time_shark < time_you:
        return "Shark Bait!"
    else:
        return "Alive!"


@pytest.mark.parametrize("pontoon_distance, shark_distance, you_speed, shark_speed, dolphin, expected",
                         [(12, 50, 4, 8, True, "Alive!"),
                          (7, 55, 4, 16, True, "Alive!"),
                          (24, 0, 4, 8, True, "Shark Bait!"),
                          (49, 57, 2, 2, True, "Alive!"),
                          (17, 6, 4, 1, True, "Alive!"),
                          (48, 71, 4, 14, True, "Shark Bait!"),
                          ])
def test_solution(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin, expected):
    assert shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin) == expected


if __name__ == '__main__':
    # print(shark(49, 57, 2, 2, True))
    # print(shark(12, 50, 4, 8, True))
    # print(shark(24, 0, 4, 8, True))
    # print(shark(49, 57, 2, 2, True))
    print(shark(17, 6, 4, 1, True))
    #print(shark(48, 71, 4, 14, True))

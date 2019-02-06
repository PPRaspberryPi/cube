import multiprocessing
from enum import IntEnum


class Direction(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    BACK = 5
    FORTH = 6
    ENTER = 7


direction_p_1 = multiprocessing.Value('i')
direction_p_2 = multiprocessing.Value('i')

direction = direction_p_1
direction2 = direction_p_2

direction_p_1.value = 1
direction_p_2.value = 1

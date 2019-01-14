from enum import Enum

import main as cube

import numpy as np


class Face(Enum):
    FRONT = 1
    BACK = 2
    LEFT = 3
    RIGHT = 4
    UP = 5
    DOWN = 6


cubeSize = 8


def clear_all():
    for x in range(0, cubeSize ** 3):
        cube.buffer_cubes[x].setOff()


def change_face(face: Face, face_num: int, frame):
    face_num = face_num % 8
    if face is Face.FRONT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[y + ((7 - x) * 8)] == 1:
                    cube.buffer_cubes[(face_num % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(face_num % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOff()

    elif face is Face.BACK:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[y + (x * 8)] == 1:
                    cube.buffer_cubes[((7 - face_num) % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[((7 - face_num) % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOff()

    elif face is Face.LEFT:
        frame = list(reversed(frame))
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + ((face_num % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + ((face_num % 8) * 64)].setOff()

    elif face is Face.RIGHT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + ((7 - y) * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + (((7 - face_num) % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + (((7 - face_num) % 8) * 64)].setOff()

    elif face is Face.UP:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((face_num % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((face_num % 8) * 8) + ((y % 8) * 64)].setOff()

    elif face is Face.DOWN:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + (((7 - face_num) % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + (((7 - face_num) % 8) * 8) + ((y % 8) * 64)].setOff()
    display()


def led_on(*target_leds):
    """
    Schaltet beliebige Menge an LED's an
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        cube.buffer_cubes[(x[0] % 8) + ((x[1] % 8) * 8) + ((x[2] % 8) * 64)].setOn()


def led_off(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        cube.buffer_cubes[(x[0] % 8) + ((x[1] % 8) * 8) + ((x[2] % 8) * 64)].setOff()


def display():
    cube.display()


def pad_led_on(*target_led_location):
    """
    Schaltet beliebige Menge an LED's an
    :paramtarget_led_location: [0-1, 0-1]
    :return: none
    """
    for x in target_led_location:
        ceil1 = int((np.ceil(x[0] * (cubeSize - 1))))
        if ceil1 == 0:
            ceil1 = 1
        floor1 = int((np.floor(x[0] * (cubeSize - 1))))
        if floor1 == (cubeSize - 1):
            floor1 = (cubeSize - 2)

        ceil2 = int((np.ceil(x[1] * (cubeSize - 1))))
        if ceil2 == 0:
            ceil2 = 1
        floor2 = int((np.floor(x[1] * (cubeSize - 1))))
        if floor2 == (cubeSize - 1):
            floor2 = (cubeSize - 2)

        cube.buffer_cubes[ceil1 + 0 + (ceil2 * 64)].setOn()
        cube.buffer_cubes[floor1 + 0 + (floor2 * 64)].setOn()
        cube.buffer_cubes[ceil1 + 0 + (floor2 * 64)].setOn()
        cube.buffer_cubes[floor1 + 0 + ceil2 * 64].setOn()


def pad_led_off(*target_led_location):
    """
    Schaltet beliebige Menge an LED's aus
    :paramtarget_led_location: [0-1, 0-1]
    :return: none
    """
    for x in target_led_location:
        ceil1 = int((np.ceil(x[0] * (cubeSize - 1))))
        if ceil1 == 0:
            ceil1 = 1
        floor1 = int((np.floor(x[0] * (cubeSize - 1))))
        if floor1 == (cubeSize - 1):
            floor1 = (cubeSize - 2)

        ceil2 = int((np.ceil(x[1] * (cubeSize - 1))))
        if ceil2 == 0:
            ceil2 = 1
        floor2 = int((np.floor(x[1] * (cubeSize - 1))))
        if floor2 == (cubeSize - 1):
            floor2 = (cubeSize - 2)

        cube.buffer_cubes[ceil1 + 0 + (ceil2 * 64)].setOff()
        cube.buffer_cubes[floor1 + 0 + (floor2 * 64)].setOff()
        cube.buffer_cubes[ceil1 + 0 + (floor2 * 64)].setOff()
        cube.buffer_cubes[floor1 + 0 + ceil2 * 64].setOff()


def start():
    cube.main()

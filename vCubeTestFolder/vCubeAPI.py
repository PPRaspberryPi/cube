from enum import Enum

import vCubeTestFolder.main as cube


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


def change_face(face: Face, frame):
    if face is Face.FRONT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(0 % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(0 % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOff()

    elif face is Face.BACK:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(7 % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(7 % 8) + ((x % 8) * 8) + ((y % 8) * 64)].setOff()

    elif face is Face.LEFT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + ((0 % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + ((0 % 8) * 64)].setOff()

    elif face is Face.RIGHT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + ((7 % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((y % 8) * 8) + ((7 % 8) * 64)].setOff()

    elif face is Face.UP:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((0 % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((0 % 8) * 8) + ((y % 8) * 64)].setOff()

    elif face is Face.DOWN:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * 8)] == 1:
                    cube.buffer_cubes[(x % 8) + ((0 % 8) * 8) + ((y % 8) * 64)].setOn()
                else:
                    cube.buffer_cubes[(x % 8) + ((0 % 8) * 8) + ((y % 8) * 64)].setOff()


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


def start():
    cube.main()

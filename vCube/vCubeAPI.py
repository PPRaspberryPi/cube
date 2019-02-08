from enum import Enum

import numpy as np

from vCube import main as cube


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


def draw_sun(target_location, size_x, size_y, size_z):
    x = target_location[0] * (cubeSize - 1)
    y = target_location[1] * (cubeSize - 1)
    z = target_location[2] * (cubeSize - 1)

    half_x = size_x / 2
    half_y = size_y / 2
    half_z = size_z / 2

    if size_x % 2 == 0:
        if x < 1:
            x_center = 0.5
        elif x > 6:
            x_center = 6.5
        else:
            x_center = np.floor(x) + 0.5
    else:
        x_center = round(x)

    if size_y % 2 == 0:
        if y < 1:
            y_center = 0.5
        elif y > 6:
            y_center = 6.5
        else:
            y_center = np.floor(y) + 0.5
    else:
        y_center = round(y)

    if size_z % 2 == 0:
        if z < 1:
            z_center = 0.5
        elif z > 6:
            z_center = 6.5
        else:
            z_center = np.floor(z) + 0.5
    else:
        z_center = round(z)

    for r_x in range(size_x):
        for r_y in range(size_y):
            for r_z in range(size_z):
                if not ((r_x == 1 or r_x == (size_x - 2)) and (r_y == 1 or r_y == (size_y - 2)) and (
                        r_z == 1 or r_z == (size_z - 2))) and not (((r_x == 0 or r_x == size_x - 1) and (
                        r_y == 0 or r_y == 1 or r_y == size_y - 1 or r_y == size_y - 2)) or (
                                                                           (r_y == 0 or r_y == size_y - 1) and (
                                                                           r_x == 0 or r_x == 1 or r_x == size_x - 1 or r_x == size_x - 2)) or (
                                                                           (r_y == 0 or r_y == size_y - 1) and (
                                                                           r_z == 0 or r_z == 1 or r_z == size_z - 1 or r_z == size_z - 2)) or (
                                                                           (r_z == 0 or r_z == size_z - 1) and (
                                                                           r_y == 0 or r_y == 1 or r_y == size_y - 1 or r_y == size_y - 2)) or (
                                                                           (r_x == 0 or r_x == size_x - 1) and (
                                                                           r_z == 0 or r_z == 1 or r_z == size_z - 1 or r_z == size_z - 2)) or (
                                                                           (r_z == 0 or r_z == size_z - 1) and (
                                                                           r_x == 0 or r_x == 1 or r_x == size_x - 1 or r_x == size_x - 2))):
                    cube.buffer_cubes[((int(np.ceil(x_center - half_x + r_x)) % cubeSize) + (
                            (int(np.ceil(y_center - half_y + r_y)) % cubeSize) * cubeSize) + (
                                               (int(np.ceil(z_center - half_z + r_z)) % cubeSize) * (
                                               cubeSize ** 2)))].setOn()


def cuboid_on(target_location, size_x, size_y, size_z):
    x = target_location[0] * (cubeSize - 1)
    y = target_location[1] * (cubeSize - 1)
    z = target_location[2] * (cubeSize - 1)

    half_x = size_x / 2
    half_y = size_y / 2
    half_z = size_z / 2

    if size_x % 2 == 0:
        if x < 1:
            x_center = 0.5
        elif x > 6:
            x_center = 6.5
        else:
            x_center = np.floor(x) + 0.5
    else:
        x_center = round(x)

    if size_y % 2 == 0:
        if y < 1:
            y_center = 0.5
        elif y > 6:
            y_center = 6.5
        else:
            y_center = np.floor(y) + 0.5
    else:
        y_center = round(y)

    if size_z % 2 == 0:
        if z < 1:
            z_center = 0.5
        elif z > 6:
            z_center = 6.5
        else:
            z_center = np.floor(z) + 0.5
    else:
        z_center = round(z)

    for r_x in range(size_x):
        for r_y in range(size_y):
            for r_z in range(size_z):
                cube.buffer_cubes[((int(np.ceil(x_center - half_x + r_x)) % cubeSize) + (
                            (int(np.ceil(y_center - half_y + r_y)) % cubeSize) * cubeSize) + (
                                               (int(np.ceil(z_center - half_z + r_z)) % cubeSize) * (
                                                   cubeSize ** 2)))].setOn()


def cuboid_off(target_location, size_x, size_y, size_z):
    x = target_location[0] * (cubeSize - 1)
    y = target_location[1] * (cubeSize - 1)
    z = target_location[2] * (cubeSize - 1)

    half_x = int(size_x / 2)
    half_y = int(size_y / 2)
    half_z = int(size_z / 2)

    if size_x % 2 == 0:
        if x < 1:
            x_center = 0.5
        elif x > 6:
            x_center = 6.5
        else:
            x_center = np.floor(x) + 0.5
    else:
        x_center = round(x)

    if size_y % 2 == 0:
        if y < 1:
            y_center = 0.5
        elif y > 6:
            y_center = 6.5
        else:
            y_center = np.floor(y) + 0.5
    else:
        y_center = round(y)

    if size_z % 2 == 0:
        if z < 1:
            z_center = 0.5
        elif z > 6:
            z_center = 6.5
        else:
            z_center = np.floor(z) + 0.5
    else:
        z_center = round(z)

    for r_x in range(size_x):
        for r_y in range(size_y):
            for r_z in range(size_z):
                cube.buffer_cubes[((int(np.ceil(x_center - half_x + r_x)) % cubeSize) + (
                            (int(np.ceil(y_center - half_y + r_y)) % cubeSize) * cubeSize) + (
                                               (int(np.ceil(z_center - half_z + r_z)) % cubeSize) * (
                                                   cubeSize ** 2)))].setOff()


def start():
    cube.main()

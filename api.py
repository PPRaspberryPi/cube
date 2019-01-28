# Import für die sleep funktionen
import time
from enum import Enum
import RPi.GPIO as IO
import numpy as np

IO.VERBOSE = False

###############

# INHALT
# 01: Attribute der API (LED-Array, Pin-Arrays etc)
# 02: Softwareseitige Funktionalitäten (led_on, led_off) mit variablen Parameterlängen
# 03: Hardwareseitige Funktionalitäten (Hilfsfunktionen für das Programmverhalten)
# 04: Eigentlicher API-Code mit threading und Speisen der Schieberegister

###############


# 01: ATTRIBUTE DER API

# Variable für die Anzahl der LED's pro Dimension
cubeSize = 8

# Delay für sleep-Funktion
delay = 0.001

# Array enthält die Namen der Anoden-Pins
anodePins = [9, 10, 11]

# Array enthält die Namen der Kathoden-Pins
kathodePins = [24, 23, 22, 27, ]

# 512-Bit boolean-Array für die LED's
leds = [0 for x in range(cubeSize ** 3)]
buffer_leds = [0 for y in range(cubeSize ** 3)]


# 02: SOFTWARESEITIGE FUNKTIONALITÄTEN

class Face(Enum):
    FRONT = 1
    BACK = 2
    LEFT = 3
    RIGHT = 4
    UP = 5
    DOWN = 6


def led_on(*target_leds):
    """
    Schaltet beliebige Menge an LED's an
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        buffer_leds[(x[0] % cubeSize) + ((x[1] % cubeSize) * cubeSize) + ((x[2] % cubeSize) * (cubeSize ** 2))] = 1


def led_off(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        buffer_leds[(x[0] % cubeSize) + ((x[1] % cubeSize) * cubeSize) + ((x[2] % cubeSize) * (cubeSize ** 2))] = 0


def led_to(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>, <state> 0 oder 1]
    :return: none
    """
    for x in target_leds:
        buffer_leds[(x[0] % cubeSize) + ((x[1] % cubeSize) * cubeSize) + ((x[2] % cubeSize) * (cubeSize ** 2))] = x[3]


def clear_all():
    for x in range(0, cubeSize ** 3):
        buffer_leds[x] = 0


def change_face(face: Face, face_num: int, frame):
    face_num = face_num % cubeSize
    if face is Face.FRONT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[y + (((cubeSize - 1) - x) * cubeSize)] == 1:
                    buffer_leds[
                        (face_num % cubeSize) + ((x % cubeSize) * cubeSize) + ((y % cubeSize) * (cubeSize ** 2))] = 1
                else:
                    buffer_leds[
                        (face_num % cubeSize) + ((x % cubeSize) * cubeSize) + ((y % cubeSize) * (cubeSize ** 2))] = 0

    elif face is Face.BACK:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[y + (x * cubeSize)] == 1:
                    buffer_leds[(((cubeSize - 1) - face_num) % cubeSize) + ((x % cubeSize) * cubeSize) + (
                                (y % cubeSize) * (cubeSize ** 2))] = 1
                else:
                    buffer_leds[(((cubeSize - 1) - face_num) % cubeSize) + ((x % cubeSize) * cubeSize) + (
                                (y % cubeSize) * (cubeSize ** 2))] = 0

    elif face is Face.LEFT:
        frame = list(reversed(frame))
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * cubeSize)] == 1:
                    buffer_leds[
                        (x % cubeSize) + ((y % cubeSize) * cubeSize) + ((face_num % cubeSize) * (cubeSize ** 2))] = 1
                else:
                    buffer_leds[
                        (x % cubeSize) + ((y % cubeSize) * cubeSize) + ((face_num % cubeSize) * (cubeSize ** 2))] = 0

    elif face is Face.RIGHT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (((cubeSize - 1) - y) * cubeSize)] == 1:
                    buffer_leds[(x % cubeSize) + ((y % cubeSize) * cubeSize) + (
                                (((cubeSize - 1) - face_num) % cubeSize) * (cubeSize ** 2))] = 1
                else:
                    buffer_leds[(x % cubeSize) + ((y % cubeSize) * cubeSize) + (
                                (((cubeSize - 1) - face_num) % cubeSize) * (cubeSize ** 2))] = 0

    elif face is Face.UP:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * cubeSize)] == 1:
                    buffer_leds[
                        (x % cubeSize) + ((face_num % cubeSize) * cubeSize) + ((y % cubeSize) * (cubeSize ** 2))] = 1
                else:
                    buffer_leds[
                        (x % cubeSize) + ((face_num % cubeSize) * cubeSize) + ((y % cubeSize) * (cubeSize ** 2))] = 0

    elif face is Face.DOWN:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                if frame[x + (y * cubeSize)] == 1:
                    buffer_leds[(x % cubeSize) + ((((cubeSize - 1) - face_num) % cubeSize) * cubeSize) + (
                                (y % cubeSize) * (cubeSize ** 2))] = 1
                else:
                    buffer_leds[(x % cubeSize) + ((((cubeSize - 1) - face_num) % cubeSize) * cubeSize) + (
                                (y % cubeSize) * (cubeSize ** 2))] = 0
    display()


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
                    buffer_leds[((int(np.ceil(x_center - half_x + r_x)) % cubeSize) + (
                            (int(np.ceil(y_center - half_y + r_y)) % cubeSize) * cubeSize) + (
                                         (int(np.ceil(z_center - half_z + r_z)) % cubeSize) * (
                                         cubeSize ** 2)))] = 1


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
                buffer_leds[((int(np.ceil(x_center - half_x + r_x)) % cubeSize) + (
                        (int(np.ceil(y_center - half_y + r_y)) % cubeSize) * cubeSize) + (
                                     (int(np.ceil(z_center - half_z + r_z)) % cubeSize) * (cubeSize ** 2)))] = 1


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
                buffer_leds[((int(np.ceil(x_center - half_x + r_x)) % cubeSize) + (
                        (int(np.ceil(y_center - half_y + r_y)) % cubeSize) * cubeSize) + (
                                     (int(np.ceil(z_center - half_z + r_z)) % cubeSize) * (cubeSize ** 2)))] = 0


# 03: HARDWARESEITIGE FUNKTIONALITÄTEN

def display():
    global leds
    leds = buffer_leds


def start():
    setup_pins()
    print_registers()

def setup_pins():
    """
    Setup der Pins
    :return: none
    """
    IO.setmode(IO.BCM)
    for x in anodePins + kathodePins:
        IO.setup(x, IO.OUT)


def print_registers():
    while True:
        for y in kathodePins:
            for x in leds:
                # Serieller Input über den ser-Pin
                IO.output(anodePins[0], x)
                time.sleep(delay)

                # sck-bit down Flanke. Schaltet Bits weiter (Bit shift des Registers)
                IO.output(anodePins[1], 1)
                time.sleep(delay)
                IO.output(anodePins[1], 0)
                time.sleep(delay)

            # rck-bit
            IO.output(anodePins[2], 1)
            time.sleep(delay)
            IO.output(anodePins[2], 0)
            time.sleep(delay)

            IO.output(y - 1, 0)
            IO.output(y, 1)

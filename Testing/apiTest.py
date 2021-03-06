# Import für die sleep funktionen
import time
# Import fürs multithreading (die dummy-library erlaubt Umgang mit threads)
from enum import Enum
from multiprocessing.dummy import Pool

# Dummy-library, welche (nicht implementierte) Funktionen der RPi.GPIO-library
# bereitstellt, damit das Programm ordentlich kompiliert wird
import RPi.GPIO as IO

IO.VERBOSE = False

# numpy import für die arrays
import numpy as np

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
kathodePins = [12, 13, 14, 15, 16, 17, 18, 19]

# 512-Bit boolean-Array für die LED's
leds = [0 for x in range(cubeSize ** 3)]


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
        leds[x[0]][x[1]][x[2]] = 1


def led_off(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        leds[x[0]][x[1]][x[2]] = 0


def led_on(*target_leds):
    """
    Schaltet beliebige Menge an LED's an
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        leds[(x[0] % 8) + ((x[1] % 8) * 8) + ((x[2] % 8) * 64)] = 1


def led_off(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        cube.buffer_cubes[(x[0] % 8) + ((x[1] % 8) * 8) + ((x[2] % 8) * 64)].setOff()


def led_to(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>, <state> 0 oder 1]
    :return: none
    """
    for x in target_leds:
        leds[x[0]][x[1]][x[2]] = x[3]


def change_face(face: Face, frame):
    if face is Face.FRONT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                leds[x][0][y] = frame[(x + 1) * (y + 1)]
    elif face is Face.BACK:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                leds[x][7][y] = frame[(x + 1) * (y + 1)]
    elif face is Face.LEFT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                leds[x][y][0] = frame[(x + 1) * (y + 1)]
    elif face is Face.RIGHT:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                leds[x][y][7] = frame[(x + 1) * (y + 1)]
    elif face is Face.UP:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                leds[0][x][y] = frame[(x + 1) * (y + 1)]
    elif face is Face.DOWN:
        for x in range(0, cubeSize):
            for y in range(0, cubeSize):
                leds[7][x][y] = frame[(x + 1) * (y + 1)]


# 03: HARDWARESEITIGE FUNKTIONALITÄTEN


def led_setup():
    """
    Setup der Pins
    :return: none
    """
    IO.setmode(IO.BCM)
    for x in np.ravel(anodePins):
        IO.setup(x, IO.OUT)


def get_set(x, y):
    """
    Erzeugung von 16Bit-Informationen, welche an die Shift-Registerpaare
    übergeben werden.
    :param x: Layer (Eingabebereich: 0 - 7)
    :param y: Paare aus y-ten Zeilen innerhalb des Arrays (Eingabebereich: 0 - 3)
    :return: Eindimensionales 16er Array
    """
    return np.ravel(leds[x, (y * 2):(y * 2 + 2), 0:])


def get_pins(y):
    """
    :param y:
    :return: Dreistelliges Array, in dem die Pins gespeichert sind, die für das aktuelle LED-Set zuständig sind
    """
    return anodePins[y, 0:]


def print_registers(args):
    """
    Gibt Informationen an die Pins weiter
    :param args: Zweidimensionales Array für LED's und Pins
    :return: none
    """

    # Auflösen des Parametertupels
    # sub_leds enthält 16-Bit Input für Schieberegister
    sub_leds = args[0]
    # sub_pins enthält die für diese Schieberegister zuständigen Pins
    sub_pins = args[1]

    for x in sub_leds:
        # Serieller Input über den ser-Pin
        IO.output(sub_pins[0], x)
        time.sleep(delay)

        # sck-bit down Flanke. Schaltet Bits weiter (Bit shift des Registers)
        IO.output(sub_pins[1], 1)
        time.sleep(delay)
        IO.output(sub_pins[1], 0)
        time.sleep(delay)

    # rck-bit down Flanke. Gibt 16-Bit Informationen aus
    IO.output(sub_pins[2], 1)
    time.sleep(delay)
    IO.output(sub_pins[2], 0)
    time.sleep(delay)


# 04: PROGRAMMVERHALTEN

# Setup-Methode der IO-pins
def setup():
    led_setup()

    for x in range(kathodePins.size):
        # Setzt Pin, welcher den NPN-Transistor des aktuellen layers steuert auf 1
        IO.output(kathodePins[x], 1)
        time.sleep(delay)

        # THREADING DER VIER SCHIEBEREGISTERPAARE
        # benutzt die Pool Klasse der multiprocessing.dummy Library
        # pool.map ruft die print_registers methode mit einem iterator als parameter auf
        # der iterator ist in dem fall [0,1,2,3], also gibt es insgesamt vier funktionsaufrufe
        # der parameter für print_registers ist das Tupel aus get_set und get_pins
        # tupel deswegen, weil die map funktion nur über einen Parameter mappen kann
        # get_set liefert das 16 stellige array als input für die schieberegister
        # get_pins liefert die für das jeweilie Set zuständigen IO Pins
        # das tupel wird in der print_registers methode wieder aufgelöst

        with Pool(4) as pool:
            pool.map(print_registers, [(get_set(x, y), get_pins(y)) for y in [0, 1, 2, 3]])

        # setzt layer pin wieder auf 0
        IO.output(kathodePins[x], 0)
        time.sleep(delay)

# TO DO:

# 01: SYNCHRONISATION VON PROGRAMMCODE UND API
# irgendwie muss verhindert werden, dass das led array geändert wird, WÄHREND die api das array ausliest
# das ist auf jeden fall der allerwichtigste punkt!

# 02: SLEEP FUNKTIONEN
# ich hab die zwar eingepflegt aber das genaue verhalten muss nochmal geprüft werden
# ein kompletter durchgang enthält im moment 52 sleeps
# davon sind 48 durch threading parallelisiert
# ergibt also effektiv 16 sleeps (1 + 16 * 3 / 4 + 2 + 1)

# 03: REFACTORING
# keine ahnung ich hab alles ohne klasse programmiert. das geht bestimmt auch schöner. queue python pros
# vieles ist bestimmt noch hässlich oder unübersichtlich
# vielleicht halten wir uns an den PEP 8 style guide (den hab ich selber nur noch nicht drauf)

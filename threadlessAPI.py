# Import für die sleep funktionen
import time
# Import fürs multithreading (die dummy-library erlaubt Umgang mit threads)
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
# ser, rck, sck
anodePins = np.array([[4, 3, 2], [18, 15, 14], [25, 24, 23], [22, 27, 17]])

# Array enthält die Namen der Kathoden-Pins
kathodePins = np.array([26, 19, 13, 6, 5, 11, 9, 10])

# 512-Bit boolean-Array für die LED's
leds = np.array([[[0 for x in range(cubeSize)] for y in range(cubeSize)] for z in range(cubeSize)])


# 02: SOFTWARESEITIGE FUNKTIONALITÄTEN


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


# 03: HARDWARESEITIGE FUNKTIONALITÄTEN


def led_setup():
    """
    Setup der Pins
    :return: none
    """
    IO.setmode(IO.BCM)
    for x in np.ravel(anodePins):
        IO.setup(x, IO.OUT)

    for x in np.ravel(kathodePins):
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


def print_registers(layer):
    for x in anodePins:
        i = 0
        led = np.ravel(leds)
        for y in reversed(led[(i * 16) + (layer * 64): ((i + 1) * 16) + (layer * 64)]):
            # Serieller Input über den ser-Pin
            IO.output(x[0], y)
            time.sleep(delay)

            # sck-bit down Flanke. Schaltet Bits weiter (Bit shift des Registers)
            IO.output(x[2], 1)
            time.sleep(delay)
            IO.output(x[2], 0)
            time.sleep(delay)

            # rck-bit down Flanke. Gibt 16-Bit Informationen aus
        IO.output(x[1], 1)
        time.sleep(delay)
        IO.output(x[1], 0)
        time.sleep(delay)

        i += 1


# 04: PROGRAMMVERHALTEN

# Setup-Methode der IO-pins
led_setup()

k = 0
while 1:
    k = k % 8
    IO.output(k, 1)
    print_registers(k)
    IO.output(k, 0)
    k += 1

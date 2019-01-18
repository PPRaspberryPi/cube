# Import für die sleep funktionen
import threading
import time
# Import fürs multithreading (die dummy-library erlaubt Umgang mit threads)
from multiprocessing.dummy import Pool

# Dummy-library, welche (nicht implementierte) Funktionen der RPi.GPIO-library
# bereitstellt, damit das Programm ordentlich kompiliert wird
# import RPi.GPIO as IO

# IO.VERBOSE = False

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
# leds = np.array([[[0 for x in range(cubeSize)] for y in range(cubeSize)] for z in range(cubeSize)])
leds = [x % 2 for x in range(cubeSize) for y in range(cubeSize) for z in range(cubeSize)]


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
    i = 0
    for x in anodePins:
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


def print_test(shift_pair):
    x = anodePins[shift_pair]
    for y in reversed(leds[(shift_pair * 16) + (current_layer * 64): ((shift_pair + 1) * 16) + (current_layer * 64)]):
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


class ShiftPair(threading.Thread):

    def __init__(self, shift_pair):
        super().__init__()
        self.shift_pair = shift_pair
        self.done = False

    def is_done(self):
        return self.done

    def run(self):
        while True:
            while not self.done:
                # threadLock.acquire(True)
                print_test(self.shift_pair)
                print("done ", self.shift_pair)
                self.done = True
                # threadLock.release()


# 04: PROGRAMMVERHALTEN

# Setup-Methode der IO-pins
# led_setup()
threadLock = threading.Lock()
current_layer = 0


def threadTest():
    print(leds)
    global current_layer
    sp0 = ShiftPair(0)
    sp1 = ShiftPair(1)
    sp2 = ShiftPair(2)
    sp3 = ShiftPair(3)
    sp0.start()
    sp1.start()
    sp2.start()
    sp3.start()
    while current_layer != 8:
        if sp0.done and sp1.done and sp2.done and sp3.done:
            time.sleep(0.1)

            current_layer += 1
            sp0.done = False
            sp1.done = False
            sp2.done = False
            sp3.done = False


def threadlessTest():
    led_setup()
    while 1:
        for z in range(0, cubeSize):
            IO.output(kathodePins[z], 1)
            print_registers(z)
            IO.output(kathodePins[z], 0)

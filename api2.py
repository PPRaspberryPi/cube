# import für die sleep funktionen
import time
# import fürs multithreading (die dummy library erlaubt umgang mit threads)
from multiprocessing.dummy import Pool

# meine fake RPi import. ersetze durch den auskommentierten, damit der code auf windows läuft
import FakeRPi.GPIO as IO
# import RPi.GPIO as IO
# numpy import für die arrays
import numpy as np

###############

# INHALT
# 01: attribute der api (led array, pin arrays etc)
# 02: softwareseitige funktionen (led_on, led_off) mit variablen parameterlängen
# 03: hardwareseitige funktionen (hilfsfunktionen fürs programmverhalten)
# 04: eigentlicher api code mit threading und speisen der schieberegister

###############


# 01: ATTRIBUTE DER API

# variable für anzahl der led's pro dimension
cubeSize = 8

# delay für sleep funktion
delay = 0.001

# array enthält die namen der anoden pins
anodePins = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

# array enthält die namen der kathoden pins
kathodePins = np.array([12, 13, 14, 15, 16, 17, 18, 19])

# 512 bit boolean array für unsere led's
leds = np.array([[[0 for x in range(cubeSize)] for y in range(cubeSize)] for z in range(cubeSize)])


# 02: SOFTWARESEITIGE FUNKTIONEN

# schaltet beliebige menge an led's an
def led_on(*target_leds):
    for x in target_leds:
        leds[x[0]][x[1]][x[2]] = 1


# schaltet beliebige menge an led's aus
def led_off(*target_leds):
    for x in target_leds:
        leds[x[0]][x[1]][x[2]] = 0


# 03: HARDWARESEITIGE FUNKTIONEN

# setup der pins
def led_setup():
    IO.setmode(IO.BCM)
    for x in np.ravel(anodePins):
        IO.setup(x, IO.OUT)


# erzeugt 16 bit information für die shift register paare als array
def get_set(x, y):
    return np.ravel(leds[x, (y * 2):(y * 2 + 2), 0:])


# erzeugt dreistelliges array, in dem die pins gespeichert sind, die für das aktuelle led set zuständig sind
def get_pins(y):
    return anodePins[y, 0:]


# gibt information an die pins weiter
def print_registers(args):
    # auflösen des parameter tupels
    # sub_leds enthält 16 bit input für schieberegister
    sub_leds = args[0]
    # sub_pins enthält die für diese schieberegister zuständigen pins
    sub_pins = args[1]

    for x in sub_leds:
        # serieller input über den ser pin
        IO.output(sub_pins[0], x)
        time.sleep(delay)

        # sck bit down flanke. schaltet bits weiter (bit shift des registers)
        IO.output(sub_pins[1], 1)
        time.sleep(delay)
        IO.output(sub_pins[1], 0)
        time.sleep(delay)

    # rck bit down flanke. gibt 16 bit information aus
    IO.output(sub_pins[2], 1)
    time.sleep(delay)
    IO.output(sub_pins[2], 0)
    time.sleep(delay)


# 04: PROGRAMMVERHALTEN

# setup methode der IO pins
led_setup()

for x in range(kathodePins.size):
    # setzt pin welcher den npn transistor des aktuellen layers steuert auf 1
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

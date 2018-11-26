import time

import RPi.GPIO as GPIO

import led


# Temporäre Dummy-Werte für die Pins
data = 1
clock = 2
latch = 3


def initialise():
    """LED-Objekt mit Cube- sowie Buffer-Array erstellen"""
    return led.LED()


def test_all(led):
    """Durchläuft alle Layer einmal."""
    for layer in range(0, 8):
        led.nth_layer(layer)
        shift_write_all(led)
        time.sleep(.01)


def shift_write_layer(led, layer):
    for x in range(0, 8):
        if x == layer:
            led.cube_array[x+512] = 1
        else:
            led.cube_array[x+512] = 0
    shift_write_all(led)


def shift_write_all(led):
    """
    aktuelles Bitmuster wird in die Shift-Register geschoben.
    Soweit nur Implementation für 8 zusammenhängende Register.
    TO-DO (falls gewünscht): Funktion erweitern, sodass abhhängig von der aktuellen
    Position im Array der Pin für die nächste Shift-Registerreihe angesprochen wird.
    """
    for x in range(0, 520):
        temp = led.cube_array[x]
        if temp == 1:
            GPIO.output(data, GPIO.HIGH)
        else:
            GPIO.output(data, GPIO.LOW)
        pulse_clock()
    trigger_latch()
    return


def pulse_clock():
    """manueller Taktgeber"""
    GPIO.output(clock, GPIO.HIGH)
    time.sleep(.01)
    GPIO.output(clock, GPIO.LOW)
    return


def trigger_latch():
    """
    Gespeichertes Bitmuster ins latch übertragen.
    TO-DO: Falls nicht alle Shift-Register aneinander: Funktion erweitern.
    (parallel zu "shiftWrite(led)")
    """
    GPIO.output(latch, GPIO.HIGH)
    time.sleep(.01)
    GPIO.output(latch, GPIO.LOW)
    return

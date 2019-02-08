import time

import RPi.GPIO as IO  # um die Pins ansteuern zu koennen, brauchen wir die Lib

# paar 1: ser 4, rck 3, sck 2 (voll funktionsfaehig)
# paar 2: ser 18, rck 15, sck 14 (kurzschluss zwischen rck und sck??)
# paar 3: ser 25, rck 24, sck 23 (5. von oben anloeten)
# paar 4: ser 22, rck 27, sck 17 (nicht angelötet) (5. von oben) sonst geht das paar

ser = 9  # serial 4th
rck = 4  # out 5th
sck = 25  # clock 6th

IO.setmode(IO.BCM)  # Programmiermodus, um die Pins zu setzen
IO.setup(ser, IO.OUT)
IO.setup(sck, IO.OUT)
IO.setup(rck, IO.OUT)

pins = [14, 15, 17, 18, 27, 22, 23, 24]

for x in pins:
    IO.setup(x, IO.OUT)
    IO.output(x, 0)

while 1:
    IO.output(ser, 1)
    for x in pins:
        IO.output(x, 1)
        for y in range(64):
            time.sleep(0.01)
            IO.output(sck, 1)
            time.sleep(0.01)
            IO.output(sck, 0)
            time.sleep(0.01)
            IO.output(ser, 0)

        IO.output(rck, 1)
        time.sleep(0.01)
        IO.output(rck, 0)
        time.sleep(0.4)
        IO.output(x, 0)

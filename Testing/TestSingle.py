import time

import RPi.GPIO as IO  # um die Pins ansteuern zu koennen, brauchen wir die Lib

# paar 1: ser 4, rck 3, sck 2 (voll funktionsfaehig)
# paar 2: ser 18, rck 15, sck 14 (kurzschluss zwischen rck und sck??)
# paar 3: ser 25, rck 24, sck 23 (5. von oben anloeten)
# paar 4: ser  22, rck 27, sck 17 (nicht angelötet) (5. von oben) sonst geht das paar


temp = 10
ser1 = 4  # inout 4th
rck1 = 3  # store 5th
sck1 = 2  # shift 6th

mstr = 23  # reset

IO.setmode(IO.BCM)  # Programmiermodus, um die Pins zu setzen

pins = [2, 3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10, 9, 25, 11, 8, 7, 5, 6, 12, 13, 19, 16, 26, 20, 21]
pinsbPlus = [2, 3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21]
for x in pinsbPlus:
    IO.setup(x, IO.OUT)
    IO.output(x, 0)

while 1:
    for x in pinsbPlus:
        IO.output(x, 1)
        print(x)
        time.sleep(0.2)
        #  IO.output(x,0)
        time.sleep(0.2)

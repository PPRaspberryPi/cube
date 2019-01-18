import RPi.GPIO as IO   # um die Pins ansteuern zu koennen, brauchen wir die Lib
import time

#paar 1: ser 4, rck 3, sck 2 (voll funktionsfaehig)
#paar 2: ser 18, rck 15, sck 14 (kurzschluss zwischen rck und sck??)
#paar 3: ser 25, rck 24, sck 23 (5. von oben anloeten)
#paar 4: ser 22, rck 27, sck 17 (nicht angelötet) (5. von oben) sonst geht das paar

ser = [4,18,25,22]   #inout 4th
rck = [3,15,24,27]   #out 5th
sck = [2,14,23,17]  #clock 6th

mstr = 23 # reset

IO.setmode(IO.BCM)      # Programmiermodus, um die Pins zu setzen
for x in range(4):
	IO.setup(ser[x],IO.OUT)
	IO.setup(sck[x],IO.OUT)
	IO.setup(rck[x],IO.OUT)

for i in range(4):
	for x in range(16):
		IO.output(ser[i], 0)
		time.sleep(0.01)
		IO.output(sck[i],1)
		time.sleep(0.01)
		IO.output(sck[i],0)
		time.sleep(0.01)

	IO.output(rck[i],1)
	time.sleep(0.01)
	IO.output(rck[i],0)
	time.sleep(0.01)

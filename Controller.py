from evdev import InputDevice, ecodes

"""
Ich habe mich für das Mapping des Controllers an die Beschreibung folgender Seite gehalten:

https://core-electronics.com.au/tutorials/using-usb-and-bluetooth-controllers-with-python.html

Hier wird erklärt, wie man die Tastendrücke eines über USB angeschlossenen Controllers erfasst.
Mein PS4-Controller hatte die unten genannten eventCodes.
Für die Abfrage: "test_keyMapping" in der main aufrufen und Werte ablesen. Danach hier eintragen.

Das Modul "evdev" läuft soweit ich das verstanden habe nicht unter Windows 10, 
jedoch lief es auf dem Raspberry Pi ohne Probleme.

Bei meinem Controller gab es zusätzlich das Problem, dass die Pfeiltasten als Koordinaten
(und nicht als reine Tastendrücke, also "events") erfasst wurden, was man nicht mit 
event codes mappen kann. Grund dafür war wahrscheinlich die Interferenz mit dem
Sechs-Achsen-Sensor, welcher permanent Koordinaten übertragen hat.
Also sollten wir uns am besten keinen Controller mit Sensor holen.
"""

# event codes der Tastendrücke. Müssen bei neuen Gamepads erst noch abgefragt werden.
aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291

start = 297
select = 296

lTrig = 292
rTrig = 293

up = 1
left = 2
right = 3
down = 4


class Controller():

    def __init__(self, eventnum):
        """
        Hier wird ein Gamepad generiert.
        :param eventnum: Kennung des angeschlossenen Gamepads.
        """

        self.gamepad = InputDevice('/dev/input/event' + str(eventnum))
        self.aBtn = aBtn
        self.bBtn = bBtn
        self.xBtn = xBtn
        self.yBtn = yBtn
        self.start = start
        self.select = select
        self.lTrig = lTrig
        self.rTrig = rTrig

    def getInput(self):
        """
        Wartet, bis Eingabe getätigt wird und gibt diese als Zahl zurück.
        :return: event code des Tastendrucks
        """
        for event in self.gamepad.read_loop():
            if event.type == ecodes.EV_ABS:
                if event.value == 0:
                    if event.code == 1:
                        print(up)
                    if event.code == 0:
                        print(left)
                if event.value == 255:
                    if event.code == 0:
                        print(right)
                    if event.code == 1:
                        print(down)
            if event.type == ecodes.EV_KEY:
                if event.value == 1:
                    if event.code == self.xBtn:
                        print(self.xBtn)
                    elif event.code == self.yBtn:
                        print(self.yBtn)
                    elif event.code == self.aBtn:
                        print(self.aBtn)
                    elif event.code == self.bBtn:
                        print(self.bBtn)

                    elif event.code == self.start:
                        print(self.start)
                    elif event.code == self.select:
                        print(self.select)

                    elif event.code == self.lTrig:
                        print(self.lTrig)
                    elif event.code == self.rTrig:
                        print(self.rTrig)

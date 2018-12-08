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
xBtn = 304
oBtn = 305
viereckBtn = 308
dreieckBtn = 307

start = 315
select = 314

lTrig_1 = 310
lTrig_2 = 312
rTrig_1 = 311
rTrig_2 = 313


class controller():

    def __init__(self, eventnum):
        """
        Hier wird ein Gamepad generiert.
        :param eventnum: Kennung des angeschlossenen Gamepads.
        """

        self.gamepad = InputDevice('/dev/input/event' + str(eventnum))
        self.xBtn = xBtn
        self.oBtn = oBtn
        self.viereckBtn = viereckBtn
        self.dreieckBtn = dreieckBtn
        self.xBtn = xBtn
        self.xBtn = xBtn
        self.start = start
        self.select = select
        self.lTrig_1 = lTrig_1
        self.lTrig_2 = lTrig_2
        self.rTrig_1 = rTrig_1
        self.rTrig_2 = rTrig_2

    def getInput(self):
        """
        Wartet, bis Eingabe getätigt wird und gibt diese als Zahl zurück.
        :return: event code des Tastendrucks
        """
        for event in self.gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value == 1:
                    if event.code == self.xBtn:
                        return self.xBtn
                    elif event.code == self.oBtn:
                        return self.oBtn
                    elif event.code == self.viereckBtn:
                        return self.viereckBtn
                    elif event.code == self.dreieckBtn:
                        return self.dreieckBtn

                    elif event.code == self.start:
                        return self.start
                    elif event.code == self.select:
                        return self.select

                    elif event.code == self.lTrig_1:
                        return self.lTrig_1
                    elif event.code == self.lTrig_2:
                        return self.lTrig_2
                    elif event.code == self.rTrig_1:
                        return self.rTrig_1
                    elif event.code == self.rTrig_2:
                        return self.rTrig_2
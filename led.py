import numpy as np


class LED:
    def __init__(self):
        """Cube- und Buffer-Array initialisieren"""
        self.cube_array = np.zeros(520, dtype=int)
        self.buffer_array = np.zeros(520, dtype=int)

    '''
        Zählweise LED's: Man fängt hinten links unten an zu zählen.
        Gezählt wird von links nach rechts.
        :param x: Zeilenposition (insg. 8 pro Reihe)
        :param y: Höhe/Layer (Ansteuerung: 64 Elemente des Arrays weitergehen)
        :param z: Tiefe (Ansteuerung: Eine Zeile weitergehen <=> 8 Schritte)
    '''

    def nth_layer(self, layer):
        self.cube_array = np.ones(520, dtype=int)
        for x in range(8):
            if x == layer:
                self.cube_array[x+512] = 1
            else:
                self.cube_array[x+512] = 0

    def transmission(self):
        """Buffer-Array mit aktualisiertem Muster füllen."""
        self.buffer_array=self.cube_array

    def turn_on(self, x, y, z):
        """Über die Parameter angesprochenes LED-Bit unabhängig vom derzeitigen Status auf 1 setzen."""
        self.cube_array[x + 64 * y + 8 * z] = 1

    def turn_off(self, x, y, z):
        """Über die Parameter angesprochenes LED-Bit unabhängig vom derzeitigen Status auf 0 setzen."""
        self.cube_array[x + 64 * y + 8 * z] = 0

    def toggle_state(self, x, y, z):
        """
        Zustand wechseln. (1 => 0 bzw. 0 => 1)
        """
        if self.cube_array[x + 64 * y + 8 * z] == 0:
            self.cube_array[x + 64 * y + 8 * z] = 1
        else:
            self.cube_array[x + 64 * y + 8 * z] = 0

    def turn_off_all(self):
        """Alle LED's aus."""
        for x in range(0, 512):
            self.cube_array[x] = 0

    def turn_on_all(self):
        """Alle LED's an."""
        for x in range(0, 512):
            self.cube_array[x] = 1

    def move_led(self, x1, y1, z1, x2, y2, z2):
        """
        Falls Ursprungs-LED aus: return ohne weitere Verarbeitung.
        Ansonsten: Schalte Urpsrung auf 0, Ziel auf 1
        :param x1: Pos. x-Achse Ursprung
        :param y1: Pos. y-Achse Ursprung
        :param z1: Pos. z-Achse Ursprung
        :param x2: Pos. x-Achse Ziel
        :param y2: Pos. y-Achse Ziel
        :param z2: Pos. z-Achse Ziel
        :return:
        """

        if self.cube_array[x1 + 64 * y1 + 8 * z1] == 1:
            self.cube_array[x1 + 64 * y1 + 8 * z1] = 0
            self.cube_array[x2 + 64 * y2 + 8 * z2] = 1

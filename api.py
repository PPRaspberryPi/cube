LED_all = [0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 1&2
           0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 1&2
           0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 3&4
           0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 3&4
           0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 5&6
           0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 5&6
           0, 0, 0, 0, 0, 0, 0, 0,  # Shift-Register 7&8
           0, 0, 0, 0, 0, 0, 0, 0]  # Shift-Register 7&8
GND_all = [0, 0, 0, 0, 0, 0, 0, 0]  # Shift-Register 9


# Eingabebereich: 0-7. Durchlaufe "LED_all" bis zur "8+8*layer"-ten Stelle und setze alle Werte auf 1
def turn_on_layer(layer):
    for x in range(0, 8):
        LED_all[x + 8 * layer] = 1
    '''
    TO-DO: Update der Shift-Register
    '''


def turn_on_all_layers():
    for x in range(0, 63):
        LED_all[x] = 1
    '''
    TO-DO: Update der Shift-Register
    '''


class Vector:
    x: int = None
    y: int = None
    z: int = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z

    def add(self, x, y, z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z


class LED:
    x: int = None
    y: int = None
    z: int = None
    state: bool = False
    lifetime: float = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def turn_on(self):
        self.state = True
        turn_on(self.x, self.y, self.z)

    def turn_off(self):
        self.state = False
        turn_off(self.x, self.y, self.z)

    def toggle_state(self):
        self.state = not self.state


def turn_on(x, y, z):
    leds[x][y][z] = True


def turn_off(x, y, z):
    leds[x][y][z] = False


def move_all(vector: Vector):
    pass


def move_led(x: int, y: int, z: int, vector: Vector):
    leds[x + vector.x][y + vector.y][z + vector.z] = leds[x][y][z]
    leds[x][y][z] = False


def move_leds(m_led, vector: Vector):
    pass


def turn_on_all():
    for x in range(8):
        for y in range(8):
            for z in range(8):
                leds[x][y][z] = True


def turn_off_all():
    for x in range(8):
        for y in range(8):
            for z in range(8):
                leds[x][y][z] = False

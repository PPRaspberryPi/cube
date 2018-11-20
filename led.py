import numpy as np


class LED:
    x: int = None
    y: int = None
    z: int = None
    state: bool = False
    lifetime: float = None

    cube_array = np.zeros(512, dtype=int)
    buffer_array = np.zeros(512, dtype=int)


    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def turn_on(self):
        self.state = True

    #      turn_on(self.x, self.y, self.z)

    def turn_off(self):
        self.state = False

    #   turn_off(self.x, self.y, self.z)

    def toggle_state(self):
        self.state = not self.state

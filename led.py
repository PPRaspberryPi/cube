import numpy as np


class LED:
    x: int = None
    y: int = None
    z: int = None
    state: bool = False
    lifetime: float = None

    cube_array = np.ones(512, dtype=int)
    buffer_array = np.zeros(512, dtype=int)

    def transmission(self, cube_array, buffer_array):
        for x in range(buffer_array.size):
            if buffer_array[x] != cube_array[x]:
                cube_array[x] = buffer_array[x]

    """def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z"""

    def turn_on(self, x, y, z):
        cord = x * y * z
        self.state = True
        self.buffer_array[cord] = 1


    def turn_off(self, x, y, z):
        cord = x * y * z
        self.state = False
        self.buffer_array[cord] = 0

    #   turn_off(self.x, self.y, self.z)

    def toggle_state(self, x, y, z):
        cord = x * y * z
        self.state = not self.state
        self.buffer_array[cord] = not self.buffer_array[cord]

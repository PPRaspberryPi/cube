class Cube:
    size = 0.3
    vertices = (-size, -size, -size), (size, -size, -size), (size, size, -size), (-size, size, -size),\
               (-size, -size, size), (size, -size, size), (size, size, size), (-size, size, size)
    faces = (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)
    colors = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)

    def setOn(self):
        # self.colors = (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)
        self.colors = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)

    def setOff(self):
        self.colors = (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (
        255, 255, 255)

    def __init__(self, on: bool, pos=(0, 0, 0)):
        x, y, z = pos
        if on:
            self.colors = (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)
        else:
            self.colors = (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (
            255, 255, 255)
        self.verts = [(x + X, y + Y, z + Z) for X, Y, Z in self.vertices]

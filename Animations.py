import threading
import time
import vCubeAPI as api
import FrameCollection2D as Frames
import random


class TickerAnimation(threading.Thread):

    def __init__(self, game_name):
        super().__init__()
        self.game_name = game_name

    def run(self):
        for l in self.game_name:
            for i in reversed(range(0, 8)):  # range goes to 0 to 7 (always 1 less than given)
                api.change_face(api.Face.FRONT, i, Frames.letter_to_frame(l))
                time.sleep(0.08)
                api.change_face(api.Face.FRONT, i, Frames.empty)

        time.sleep(0.5)


class Rain:

    def __init__(self, intensity, cube_size, speed):
        self.intensity = int(intensity * 10)
        self.cube_size = cube_size
        self.speed = int(speed * 10)
        self.rain_drops = []
        self.fall_speed = 1 / (self.cube_size - 1)

    def play(self):
        while True:
            for x in self.rain_drops:
                api.cuboid_off(x, 1, 2, 1)

            # Set new location for falling rain_drops
            for rain_drop in self.rain_drops:
                if rain_drop[1] - self.fall_speed < 0:
                    self.rain_drops.remove(rain_drop)
                else:
                    rain_drop[1] -= self.fall_speed

            for x in range(self.intensity):
                self.rain_drops = self.rain_drops + [[random.random(), 1, random.random()]]

            for x in self.rain_drops:
                if x[1] < 1 / (self.cube_size - 1):
                    api.cuboid_on(x, 1, 1, 1)
                else:
                    api.cuboid_on(x, 1, 2, 1)

            time.sleep(1 / self.speed)

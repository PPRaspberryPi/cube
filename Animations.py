import threading
import time
import api
import FrameCollection2D as Frames
import random


class TickerAnimation(threading.Thread):

    def __init__(self, game_name):
        super(TickerAnimation, self).__init__()
        self._stop_event = threading.Event()
        self.game_name = game_name

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        for l in self.game_name:
            for i in reversed(range(0, 8)):  # range goes to 0 to 7 (always 1 less than given)
                api.change_face(api.Face.FRONT, i, Frames.letter_to_frame(l))
                sleep = 0.3 / len(self.game_name)
                time.sleep(sleep)
                api.change_face(api.Face.FRONT, i, Frames.empty)

        time.sleep(0.5)


class Rain(threading.Thread):

    def __init__(self, intensity, cube_size, speed):
        super(Rain, self).__init__()
        self.intensity = int(intensity * 10)
        self.cube_size = cube_size
        self.speed = int(speed * 10)
        self.rain_drops = []
        self.fall_speed = 1 / (self.cube_size - 1)

    def run(self):
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

            api.display(api.leds)


class Snow(threading.Thread):

    def __init__(self, intensity, cube_size, speed):
        super(Snow, self).__init__()
        self.intensity = int(intensity * 10)
        self.cube_size = cube_size
        self.speed = int(speed * 10)
        self.snow_drops = []
        self.fall_speed = 1 / (self.cube_size - 1)

    def run(self):
        while True:
            for x in self.snow_drops:
                api.cuboid_off(x, 1, 1, 1)

            for snow_drop in self.snow_drops:
                if snow_drop[1] - self.fall_speed < 0:
                    self.snow_drops.remove(snow_drop)
                else:
                    snow_drop[1] -= self.fall_speed

            for x in range(self.intensity):
                self.snow_drops = self.snow_drops + [[random.random(), 1, random.random()]]

            for x in self.snow_drops:
                api.cuboid_on(x, 1, 1, 1)

            time.sleep(1 / self.speed)

            api.display(api.leds)


class Fog:

    def __init__(self, intensity, cube_size, speed):
        super(Fog, self).__init__()
        self.intensity = int(intensity * 10)
        self.cube_size = cube_size
        self.speed = int(speed * 10)
        self.fog_stripes = []
        self.fall_speed = 1 / (self.cube_size - 1)

    def run(self):
        while True:
            for x in self.fog_stripes:
                api.cuboid_off(x, 1, 1, 3)

            for fog_stripe in self.fog_stripes:
                if fog_stripe[2] + self.fall_speed > 7:
                    self.fog_stripes.remove(fog_stripe)
                else:
                    fog_stripe[2] += self.fall_speed

            for x in range(self.intensity):
                self.fog_stripes = self.fog_stripes + [[random.random(), random.random(), random.random()]]

            for x in self.fog_stripes:
                api.cuboid_on(x, 1, 1, 3)

            time.sleep(1 / self.speed)

            api.display(api.leds)


class Clouds(threading.Thread):

    def __init__(self, intensity, cube_size, speed):
        super(Clouds, self).__init__()
        self.intensity = int(intensity * 10) % 11
        self.cube_size = cube_size
        self.speed = int(speed * 10) % 11
        self.cloud_stripes = []
        self.fall_speed = 1 / (self.cube_size - 1)

    def run(self):
        c = 0
        while True:
            for x in self.cloud_stripes:
                api.cuboid_off(x, 2, 2, 3)

            for cloud_stripe in self.cloud_stripes:
                if cloud_stripe[2] + self.fall_speed > 1:
                    self.cloud_stripes.remove(cloud_stripe)
                else:
                    cloud_stripe[2] += self.fall_speed

            if c == 0:
                self.cloud_stripes = self.cloud_stripes + [[random.random(), 1, 0]]
                c += 1
            elif c == 11 - (self.intensity % 11):
                c = 0
            else:
                c += 1

            for x in self.cloud_stripes:
                api.cuboid_on(x, 2, 2, 3)

            time.sleep(1 / self.speed)

            api.display(api.leds)


class Sun(threading.Thread):

    def __init__(self):
        super(Sun, self).__init__()

    def run(self):
        api.draw_sun([0.5, 0.5, 0.5], 8, 8, 8)
        api.display(api.leds)
        while True:
            time.sleep(0.5)


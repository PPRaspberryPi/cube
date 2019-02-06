import random
import threading
import time

import Direction
import api
import FrameCollection2D as Frames

import Animations
import Game


class Snake(Game.CubeGame, threading.Thread):
    _name = 'Snake'
    _version = 'v0.1'

    _menu_frame = [0, 0, 1, 0, 0, 0, 0, 0,
                   0, 0, 1, 0, 0, 0, 0, 0,
                   0, 0, 1, 1, 1, 0, 0, 0,
                   0, 0, 0, 0, 1, 0, 0, 0,
                   0, 0, 0, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0, 0,
                   0, 0, 0, 1, 1, 1, 0, 0]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)
        self.an = None

        self.snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
        self.snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
        self.snake_length = 3
        self.pickup_loc = [0, 7, 1]
        self.failed = False
        self.score = 0

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        self.an = Animations.TickerAnimation("snake")
        self.an.start()

    def close_animation(self):
        self.an.stop()

    def stopped_animation(self):
        return self.an.stopped()

    def is_animation_alive(self):
        return self.an.is_alive()

    def done(self):
        pass

    def run(self):
        Direction.direction_p_1.value = int(Direction.Direction.UP)
        while not self.failed:
            if Direction.direction_p_1.value == 0:
                Direction.direction_p_1.value = int(Direction.Direction.UP)
            if self.snake_length > len(self.snake_loc):
                self.snake_loc.append(self.snake_loc[len(self.snake_loc) - 1])
                self.snake_length = len(self.snake_loc)

            api.led_off(self.snake_loc[self.snake_length - 1])
            for x in range(1, self.snake_length):
                self.snake_loc[self.snake_length - x] = self.snake_loc[self.snake_length - x - 1]
            if Direction.direction_p_1.value == int(Direction.Direction.BACK):
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] + 1, y[2]]
            elif Direction.direction_p_1.value == int(Direction.Direction.FORTH):
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] - 1, y[2]]
            elif Direction.direction_p_1.value == int(Direction.Direction.RIGHT):
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] + 1]
            elif Direction.direction_p_1.value == int(Direction.Direction.LEFT):
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] - 1]
            elif Direction.direction_p_1.value == int(Direction.Direction.UP):
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] + 1, y[1], y[2]]
            elif Direction.direction_p_1.value == int(Direction.Direction.DOWN):
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] - 1, y[1], y[2]]
            for s in self.snake_loc:
                api.led_on(s)

            api.led_on(self.pickup_loc)

            if self.snake_loc[0] in self.snake_loc[1:]:
                self.failed = True
                api.change_face(api.Face.LEFT, 0, Frames.number_to_frame(int(self.score / 100)))
                api.change_face(api.Face.FRONT, 0, Frames.number_to_frame(int((self.score % 100) / 10)))
                api.change_face(api.Face.RIGHT, 0, Frames.number_to_frame(int(self.score % 10)))

                # Timer for cooldown
                for x in range(0, 8):
                    api.led_on([0, x, 0], [7, x, 0], [0, x, 7], [7, x, 7])
                    api.display(api.leds)
                    time.sleep(1)

            if self.snake_loc[0][0] % 8 == self.pickup_loc[0] and self.snake_loc[0][1] % 8 == self.pickup_loc[1] and \
                    self.snake_loc[0][2] % 8 == self.pickup_loc[2]:
                self.snake_length += 1
                self.score += 1
                found_spawn = False
                while not found_spawn:
                    self.pickup_loc = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)]
                    if self.pickup_loc not in self.snake_loc:
                        found_spawn = True

            api.display(api.leds)
            time.sleep(0.2)

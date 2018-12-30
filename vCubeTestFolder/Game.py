import random
import threading
from abc import ABC, abstractmethod
import time

import Direction
import vCubeTestFolder.vCubeAPI as api
import FrameCollection2D as Frames


class CubeGame(ABC):
    cube_size = None
    frame_size = None

    _name = None
    _version = 'v0'

    def __init__(self, cube_size, frame_size, name):
        self.cube_size = cube_size
        self.frame_size = frame_size
        self._name = name

    @abstractmethod
    def get_menu_frame(self):
        pass

    @abstractmethod
    def has_menu_animation(self):
        pass

    @abstractmethod
    def play_animation(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def done(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self._name, ' ', self._version


class Snake(CubeGame, threading.Thread):
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
        CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        pass

    def done(self):
        pass

    snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
    direction = Direction.Direction.UP
    snake_length = 3
    pickup_loc = [0, 7, 1]
    failed = False
    score = 0

    def run(self):
        while not self.failed:
            self.direction = Direction.direction
            if self.snake_length > len(self.snake_loc):
                self.snake_loc.append(self.snake_loc[len(self.snake_loc) - 1])
                self.snake_length = len(self.snake_loc)

            api.led_off(self.snake_loc[self.snake_length - 1])
            for x in range(1, self.snake_length):
                self.snake_loc[self.snake_length - x] = self.snake_loc[self.snake_length - x - 1]
            if self.direction == Direction.Direction.UP:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] + 1, y[2]]
            elif self.direction == Direction.Direction.DOWN:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] - 1, y[2]]
            elif self.direction == Direction.Direction.RIGHT:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] + 1]
            elif self.direction == Direction.Direction.LEFT:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] - 1]
            elif self.direction == Direction.Direction.BACK:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] + 1, y[1], y[2]]
            elif self.direction == Direction.Direction.FORTH:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] - 1, y[1], y[2]]
            for s in self.snake_loc:
                api.led_on(s)

            api.led_on(self.pickup_loc)

            if self.snake_loc[0] in self.snake_loc[1:]:
                self.failed = True
                api.change_face(api.Face.LEFT, Frames.get_score_frame(int(self.score / 100)))
                api.change_face(api.Face.FRONT, Frames.get_score_frame(int((self.score % 100) / 10)))
                api.change_face(api.Face.RIGHT, Frames.get_score_frame(int(self.score % 10)))
                time.sleep(7)

            if self.snake_loc[0][0] % 8 == self.pickup_loc[0] and self.snake_loc[0][1] % 8 == self.pickup_loc[1] and \
                    self.snake_loc[0][2] % 8 == self.pickup_loc[2]:
                self.snake_length += 1
                self.score += 1
                found_spawn = False
                while not found_spawn:
                    self.pickup_loc = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)]
                    if self.pickup_loc not in self.snake_loc:
                        found_spawn = True
            time.sleep(0.2)

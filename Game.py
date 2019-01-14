import random
import threading
from abc import ABC, abstractmethod
import time

import Direction
import vCubeAPI as api
import FrameCollection2D as Frames

import Animations


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


# TODO: DO NOT COPY GAME CODE -> USE EXTERNAL .PY FILES
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
        self.snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
        self.snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
        self.direction = Direction.Direction.UP
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
        an = Animations.TickerAnimation("snake")
        an.start()
        an.join()

    def done(self):
        pass

    def run(self):
        while not self.failed:
            self.direction = Direction.direction
            if self.direction is None:
                self.direction = Direction.Direction.UP
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
                api.change_face(api.Face.LEFT, 0, Frames.number_to_frame(int(self.score / 100)))
                api.change_face(api.Face.FRONT, 0, Frames.number_to_frame(int((self.score % 100) / 10)))
                api.change_face(api.Face.RIGHT, 0, Frames.number_to_frame(int(self.score % 10)))

                # Timer for cooldown
                for x in range(0, 8):
                    api.led_on([0, x, 0], [7, x, 0], [0, x, 7], [7, x, 7])
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
            time.sleep(0.2)


class Pong(CubeGame, threading.Thread):
    _name = 'Pong'
    _version = 'v0.1'

    _menu_frame = [0, 0, 0, 1, 0, 0, 0, 0,
                   0, 0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0, 0,
                   1, 0, 0, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 1, 0, 0,
                   0, 0, 1, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0, 0,
                   0, 0, 1, 1, 1, 0, 0, 0]

    def __init__(self, cube_size, frame_size):
        CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)
        self.player_loc = [[2, 0, 1], [3, 0, 1], [2, 0, 2], [3, 0, 2]]
        self.ball_loc = [3, 1, 2]
        self.ball_vel_x = 1
        self.ball_vel_y = 1
        self.ball_vel_z = 1
        self.failed = False
        self.player_action = None

        self.p_loc = [0.5, 0.5]

        self.mov_val = (1 / (self.cube_size - 1))

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        an = Animations.TickerAnimation("pong")
        an.start()
        an.join()

    def done(self):
        pass

    def run(self):
        while not self.failed:
            # Turn off last position
            api.led_off(self.ball_loc)

            # Ball moving
            """
            self.ball_loc[0] += self.ball_vel_x
            self.ball_loc[1] += self.ball_vel_y
            self.ball_loc[2] += self.ball_vel_z
            """

            # TODO: UGLY AF. WE SHOULD FIX THAT. IT ONLY UPDATES PLAYER EACH INTERVAL
            # Player moving
            self.player_action = Direction.direction
            if self.player_action is not None:
                if self.player_action == Direction.Direction.UP:

                    api.pad_led_off(self.p_loc)

                    if self.p_loc[0] + self.mov_val <= 1:
                        self.p_loc[0] += self.mov_val
                    else:
                        self.p_loc[0] = 0.99

                    api.pad_led_on(self.p_loc)

                if self.player_action == Direction.Direction.DOWN:
                    api.pad_led_off(self.p_loc)

                    if self.p_loc[0] - self.mov_val >= 0:
                        self.p_loc[0] -= self.mov_val
                    else:
                        self.p_loc[0] = 0.01

                    api.pad_led_on(self.p_loc)
                if self.player_action == Direction.Direction.RIGHT:
                    api.pad_led_off(self.p_loc)

                    if self.p_loc[1] + self.mov_val <= 1:
                        self.p_loc[1] += self.mov_val
                    else:
                        self.p_loc[1] = 0.99

                    api.pad_led_on(self.p_loc)
                if self.player_action == Direction.Direction.LEFT:
                    api.pad_led_off(self.p_loc)

                    if self.p_loc[1] - self.mov_val >= 0:
                        self.p_loc[1] -= self.mov_val
                    else:
                        self.p_loc[1] = 0.01

                    api.pad_led_on(self.p_loc)
                Direction.direction = None

            # Ball bouncing on walls
            if self.ball_loc[0] > 6 or self.ball_loc[0] < 1:
                self.ball_vel_x *= -1
            if self.ball_loc[1] > 6 or self.ball_loc[1] < 1:
                self.ball_vel_y *= -1
            if self.ball_loc[2] > 6 or self.ball_loc[2] < 1:
                self.ball_vel_z *= -1

            # If Ball hits the ground
            if self.ball_loc[1] == 0 and not any(loc in [self.ball_loc] for loc in self.player_loc):
                self.failed = True

                # Timer for cooldown
                for x in range(0, 8):
                    api.led_on([0, x, 0], [7, x, 0], [0, x, 7], [7, x, 7])
                    time.sleep(1)

            # If Ball hits the paddle bounce off of it and do not go into the paddle
            if self.ball_loc[1] == 0 and any(loc in [self.ball_loc] for loc in self.player_loc):
                self.ball_loc[1] = 1

            # Turn on new position
            api.led_on(self.ball_loc)
            api.pad_led_on(self.p_loc)

            api.display()

            time.sleep(0.22)

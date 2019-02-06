import threading
import time

import Direction
import api
import requests
import Animations
import Game


class Exit(Game.CubeGame, threading.Thread):
    _name = 'Exit'
    _version = 'v0.1'

    _menu_frame = [1, 0, 0, 0, 0, 0, 0, 1,
                   0, 1, 0, 0, 0, 0, 1, 0,
                   0, 0, 1, 0, 0, 1, 0, 0,
                   0, 0, 0, 1, 1, 0, 0, 0,
                   0, 0, 0, 1, 1, 0, 0, 0,
                   0, 0, 1, 0, 0, 1, 0, 0,
                   0, 1, 0, 1, 0, 0, 1, 0,
                   1, 0, 0, 0, 0, 0, 0, 1]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)

        self.an = None

        self.failed = False

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        self.an = Animations.TickerAnimation("weather")
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
        
        Direction.direction_p_1.value = 0

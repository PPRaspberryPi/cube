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

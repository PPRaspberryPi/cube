from abc import ABC, abstractmethod


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
    def start(self, led):
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


class Snake(CubeGame):

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
        super().__init__(cube_size, frame_size, self._name)

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return False

    def start(self, led):
        pass

    def play_animation(self):
        pass

    def done(self):
        pass


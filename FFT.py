import threading
import time
import Direction
import vCubeAPI as api
import requests
import Animations
import Game
import sys, math, wave, numpy
from scipy.fftpack import dct


class AudioVis(Game.CubeGame, threading.Thread):
    _name = 'Audio Visualizer'
    _version = 'v0.1'

    _menu_frame = [0, 0, 1, 1, 0, 0, 0, 0,
                   0, 0, 1, 1, 1, 1, 0, 0,
                   0, 1, 1, 1, 1, 1, 1, 0,
                   0, 0, 0, 0, 1, 0, 0, 0,
                   0, 0, 1, 0, 1, 0, 0, 0,
                   0, 0, 1, 1, 0, 0, 0, 0,
                   0, 0, 0, 1, 0, 1, 0, 0,
                   0, 0, 0, 0, 0, 1, 0, 0]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)
        self.finished = False
        self.file_name = "music.wav"
        self.status = 'stopped'

        self.N = 8  # num of bars
        self.HEIGHT = 8  # height of a bar
        self.WIDTH = 8  # width of a bar

        # process wave data
        self.f = wave.open(self.file_name, 'rb')
        self.params = self.f.getparams()
        self.nchannels, self.sampwidth, self.framerate, self.nframes = self.params[:4]
        self.str_data = self.f.readframes(self.nframes)
        self.f.close()
        self.wave_data = numpy.frombuffer(self.str_data, dtype=numpy.short)
        self.wave_data.shape = -1, 2
        self.wave_data = self.wave_data.T

        self.num = self.nframes


    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        an = Animations.TickerAnimation("audiovis")
        an.start()
        an.join()

    def done(self):
        pass

    def run(self):
        num = int(self.num)
        h = abs(dct(self.wave_data[0][self.nframes - num:self.nframes - num + self.N]))
        h = [min(self.HEIGHT, int(i ** (1 / 2.5) * self.HEIGHT / 100)) for i in h]



        while not self.finished:
            if Direction.direction == Direction.Direction.BACK:
                self.finished = True




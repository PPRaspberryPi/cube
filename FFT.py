import threading
import time
import Direction
import vCubeAPI as api
import requests
import Animations
import Game
import sys, math, wave, numpy
from scipy.fftpack import dct
import Util as util
import PyAudio as audio


class AudioVis(Game.CubeGame, threading.Thread):
    _name = 'Audio Visualizer'
    _version = 'v0.1'

    _menu_frame = [1, 0, 0, 0, 0, 0, 0, 0,
                   1, 0, 0, 0, 0, 0, 0, 0,
                   1, 0, 0, 0, 0, 0, 0, 0,
                   1, 0, 0, 0, 0, 0, 0, 0,
                   1, 1, 0, 0, 0, 0, 0, 0,
                   1, 1, 1, 0, 0, 0, 0, 0,
                   1, 1, 1, 1, 1, 0, 0, 0,
                   1, 1, 1, 1, 1, 1, 1, 1]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)
        self.finished = False
        self.file_name = "music.wav"
        self.status = 'stopped'
        self.chunk = 1024
        self.N = self.cube_size  # num of bars
        self.HEIGHT = self.cube_size  # height of a bar
        self.WIDTH = self.cube_size  # width of a bar

        # process wave data
        self.f = wave.open(self.file_name, 'rb')
        self.p = audio.PyAudio()

        self.stream = self.p.open(format=self.p.get_format_from_width(self.f.getsampwidth()),
                                  channels=self.f.getnchannels(),
                                  rate=self.f.getframerate(),
                                  output=True)
        # read data
        self.data = self.f.readframes(self.chunk)

        self.params = self.f.getparams()
        self.nchannels, self.sampwidth, self.framerate, self.nframes = self.params[:4]
        self.str_data = self.f.readframes(self.nframes)
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
        while not self.finished:
            if Direction.direction == Direction.Direction.BACK:
                self.finished = True

            self.stream.write(self.data)
            self.data = self.f.readframes(self.chunk)
            num = int(self.num)
            h = abs(dct(self.wave_data[0][self.nframes - num:self.nframes - num + self.N]))
            h = [min(self.HEIGHT, int(i ** (1 / 2.5) * self.HEIGHT / 100)) * self.amplifier for i in h]

            self.frames = [h] + self.frames

            i = 0
            for f in self.frames:
                if i < self.cube_size:
                    api.change_face(api.Face.FRONT, self.cube_size - 1 - i, util.construct_2D_audio_frame(self.cube_size, f))
                    i += 1
                else:
                    self.frames.remove(f)

            self.num -= (1 / self.fps) * self.framerate

            if self.num < 0:
                self.finished = True

            time.sleep(1 / self.fps)

        self.stream.stop.stream()
        self.close()
        self.p.terminate()
        self.f.close()

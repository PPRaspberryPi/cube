import threading
import time
import wave

import numpy
import simpleaudio as sa
from scipy.fftpack import dct

import Animations
import Direction
import Game
import Util as util
import api


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
        self.an = None

        self.finished = False
        self.file_name = "music.wav"
        self.status = 'stopped'
        self.N = self.cube_size  # num of bars
        self.HEIGHT = self.cube_size  # height of a bar
        self.WIDTH = self.cube_size  # width of a bar

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

        self.amplifier = 12

        self.fps = 24

        self.frames = []

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        self.an = Animations.TickerAnimation("audiovis")
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
        musicfile = sa.WaveObject.from_wave_file(self.file_name)
        musicfile.play()
        Direction.direction_p_1.value = 0
        while Direction.direction_p_1.value != 7:
            num = int(self.num)
            h = abs(dct(self.wave_data[0][self.nframes - num:self.nframes - num + self.N]))
            h = [min(self.HEIGHT, int(i ** (1 / 2.5) * self.HEIGHT / 100)) * self.amplifier for i in h]

            self.frames = [h] + self.frames

            """
            i = 0
            for f in self.frames:
                if i < self.cube_size:
                    api.change_face(api.Face.FRONT, i, util.construct_2D_audio_frame(self.cube_size, f))
                    i += 1
                else:
                    self.frames.remove(f)
                    """

            for x in range(self.cube_size):
                api.change_face(api.Face.FRONT, self.cube_size - 1 - x,
                                util.construct_2D_audio_frame(self.cube_size, h, x))

            self.num -= (1 / self.fps) * self.framerate

            if self.num < 0:
                self.finished = True

            time.sleep(1 / (self.fps * 2.2))

        sa.stop_all()
        self.finished = True
        Direction.direction_p_1.value = 0

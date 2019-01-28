import threading

import Animations
import Game
import bpm280



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

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        an = Animations.TickerAnimation("temperature")
        an.start()
        an.join()

    def done(self):
        pass

    def run(self):
        #sa.WaveObject.from_wave_file(self.file_name).play()
        while not self.finished:


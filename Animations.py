import threading
import time
import vCubeAPI as api
import FrameCollection2D as Frames


class TickerAnimation(threading.Thread):

    def __init__(self, game_name):
        super().__init__()
        self.game_name = game_name

    def run(self):
        for l in self.game_name:
            for i in reversed(range(0, 7)):
                api.change_face(api.Face.FRONT, i, Frames.letter_to_frame(l))
                time.sleep(0.08)
                api.change_face(api.Face.FRONT, i, Frames.empty)

        time.sleep(0.5)

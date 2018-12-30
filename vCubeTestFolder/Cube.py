import threading
import time

import vCubeTestFolder.vCubeAPI as api
import vCubeTestFolder.Game as Game
import FrameCollection2D as Frames


class LEDCube(threading.Thread):
    cube_games = []
    current_item = 0
    current_game = None
    current_face = api.Face.FRONT

    def __init__(self, cube_size: int, delay):
        super().__init__()
        api.cubeSize = cube_size
        api.delay = delay
        # api.setup()

    def register(self, *games: Game.CubeGame):
        for game in games:
            if game.get_menu_frame() is not None:
                self.cube_games = self.cube_games + [game]

    def run(self):
        self.open_menu()

    def open_menu(self):
        if not self.cube_games:
            self.show_2d_frame(Frames.question_mark)
        else:
            while self.current_game is None:
                self.show_2d_frame(self.cube_games[self.current_item].get_menu_frame())
                # Warten auf Input
                time.sleep(10)
                api.clear_all()
                self.start_game(self.current_item)

    def show_2d_frame(self, frame):
        api.change_face(self.current_face, frame)

    def start_game(self, game_id):
        self.cube_games[game_id].start()
        self.cube_games[game_id].join()

    def kill_game(self, game_id):
        pass


frame_size = (8, 8)

led_cube = LEDCube(8, 0.001)

led_cube.register(Game.Snake(api.cubeSize, frame_size))

led_cube.start()
api.start()

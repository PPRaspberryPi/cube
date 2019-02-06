import threading
import time
import Direction
import FFT
import api
import Game as Game
import FrameCollection2D as Frames
import Snake
import Pong
import PongMulti
import Weather
import Exit


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

    def unregister_all(self):
        self.cube_games = []

    def reset_all(self):
        self.unregister_all()
        Direction.direction = None

    def open_menu(self):
        if not self.cube_games:
            self.show_2d_frame(Frames.question_mark)
        else:
            while True:
                while self.current_game is None:
                    updated = False

                    if self.cube_games[self.current_item].has_menu_animation():
                        self.cube_games[self.current_item].play_animation()

                    while not updated:

                        self.show_menu_state()

                        if api.get_pressed_enter():
                            self.cube_games[self.current_item].close_animation()
                            self.current_game = self.cube_games[self.current_item]
                            api.set_pressed_enter(False)
                            updated = True

                        if Direction.direction_p_1.value == int(Direction.Direction.RIGHT) and self.current_item < len(
                                self.cube_games) - 1:
                            self.cube_games[self.current_item].close_animation()
                            self.current_item += 1
                            Direction.direction_p_1.value = 0
                            api.clear_all()
                            updated = True

                        if Direction.direction_p_1.value == int(Direction.Direction.LEFT) and self.current_item > 0:
                            self.cube_games[self.current_item].close_animation()
                            self.current_item -= 1
                            Direction.direction_p_1.value = 0
                            api.clear_all()
                            updated = True

                        # Otherwise we will get array out of bounds exception (similar to mathf.clamp)
                        # self.current_item = max(0, min(self.current_item, len(self.cube_games) - 1))
                        time.sleep(0.2)

                api.clear_all()
                self.start_game(self.current_item)
                api.clear_all()
                # Reset everything for next menu launch
                self.reset_all()
                register_all()
                api.set_pressed_enter(False)
                self.current_game = None

    def show_2d_frame(self, frame):
        api.change_face(self.current_face, 0, frame)

    def start_game(self, game_id):
        self.cube_games[game_id].start()
        self.cube_games[game_id].join()
        Direction.direction_p_1.value = 0

    def kill_game(self, game_id):
        pass

    def show_menu_state(self):
        if not self.cube_games[self.current_item].is_animation_alive():
            if self.current_item > 0:
                api.change_face(api.Face.LEFT, 0, Frames.arrow_left)
            if self.current_item < len(self.cube_games) - 1:
                api.change_face(api.Face.RIGHT, 0, Frames.arrow_right)

            self.show_2d_frame(self.cube_games[self.current_item].get_menu_frame())


def register_all():
    if led_cube is not None:
        led_cube.register(Snake.Snake(api.cubeSize, frame_size), Pong.Pong(api.cubeSize, frame_size),
                          PongMulti.PongMulti(api.cubeSize, frame_size), Weather.Weather(api.cubeSize, frame_size), FFT.AudioVis(api.cubeSize, frame_size), Exit.Exit(api.cubeSize, frame_size))


frame_size = (8, 8)

led_cube = LEDCube(8, 0.001)

register_all()

led_cube.start()
api.start()

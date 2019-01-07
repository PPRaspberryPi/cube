import threading
import time
import Direction
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
                    if self.cube_games[self.current_item].has_menu_animation():
                        self.cube_games[self.current_item].play_animation()
                    else:
                        self.show_2d_frame(self.cube_games[self.current_item].get_menu_frame())
                    if self.current_item > 0:
                        api.change_face(api.Face.LEFT, Frames.arrow_left)
                    if self.current_item < len(self.cube_games) - 1:
                        api.change_face(api.Face.RIGHT, Frames.arrow_right)

                    if api.cube.pressed_enter:
                        self.current_game = self.cube_games[self.current_item]
                        api.cube.pressed_enter = True

                    if Direction.direction == Direction.Direction.RIGHT and self.current_item < len(
                            self.cube_games) - 1:
                        self.current_item += 1
                        Direction.direction = None
                        api.clear_all()

                    if Direction.direction == Direction.Direction.LEFT and self.current_item > 0:
                        self.current_item -= 1
                        Direction.direction = None
                        api.clear_all()

                    # Otherwise we will get array out of bounds exception (similar to mathf.clamp)
                    self.current_item = max(0, min(self.current_item, len(self.cube_games) - 1))
                    time.sleep(0.2)

                api.clear_all()
                self.start_game(self.current_item)
                api.clear_all()
                # Reset everything for next menu launch
                self.reset_all()
                register_all()
                api.cube.pressed_enter = False
                self.current_game = None

    def show_2d_frame(self, frame):
        api.change_face(self.current_face, frame)

    def start_game(self, game_id):
        self.cube_games[game_id].start()
        self.cube_games[game_id].join()

    def kill_game(self, game_id):
        pass


def register_all():
    if led_cube is not None:
        led_cube.register(Game.Snake(api.cubeSize, frame_size), Game.Pong(api.cubeSize, frame_size))


frame_size = (8, 8)

led_cube = LEDCube(8, 0.001)

# led_cube.register(Game.Snake(api.cubeSize, frame_size), Game.Pong(api.cubeSize, frame_size))

register_all()

led_cube.start()
api.start()
